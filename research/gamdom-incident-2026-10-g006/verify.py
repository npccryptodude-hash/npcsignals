#!/usr/bin/env python3
"""Offline integrity and evidence-record checks; no chain verification implied."""
import csv,hashlib,json,re,subprocess
from pathlib import Path
from decimal import Decimal,getcontext
getcontext().prec=80
p=Path(__file__).resolve().parent
m=json.loads((p/'SHA256SUMS.json').read_text())
actual={f.relative_to(p).as_posix() for f in p.rglob('*') if f.is_file() and f.name!='SHA256SUMS.json'}
assert actual==set(m),'manifest coverage mismatch'
for n,d in m.items():assert hashlib.sha256((p/n).read_bytes()).hexdigest()==d,n
print('PASS manifest coverage and every SHA-256 digest')
def read(n):
 with (p/n).open(newline='') as f:
  r=list(csv.DictReader(f));assert r and all(None not in x and None not in x.values() for x in r),n;return r
r=read('historical_transfer_ledger.csv');c=read('control_transaction_ledger.csv')
for f in p.glob('*.csv'):read(f.name)
assert len(r)==38 and len(c)==10
keys=[(x['chain'],x['tx_hash'],x['event_kind'],x['token_contract'].lower(),x['token_sender'].lower(),x['token_recipient'].lower(),x['displayed_amount']) for x in r]
assert len(keys)==len(set(keys))
for x in r:
 assert re.fullmatch('0x[0-9a-f]{64}',x['tx_hash'])
 assert x['success']=='true' and x['unauthorized_status']=='UNRESOLVED'
 if x['raw_amount']:
  assert Decimal(x['raw_amount'])/(Decimal(10)**int(x['decimals']))==Decimal(x['displayed_amount'])
 else:assert x['role'].startswith('excluded_noncanonical')
print('PASS event uniqueness, CSV structure, raw/decimal conversion and unresolved-authorization guards')
s=json.loads((p/'evidence/collection_summary.json').read_text())
allhash={x['tx_hash'] for x in r+c};old=set(s['existing_G005_receipts_not_recounted']);new=set(s['new_receipt_hashes'])
assert new==allhash-old and len(new)==s['new_receipts_verified']==36
print('PASS 36 distinct new receipt hashes, excluding six G005 hashes')
B='0xe5686aae44d392aa6a0637fd38393859502f8667';D='0x6b175474e89094c44da98b954eedeac495271d0f'
dai=[x for x in r if x['chain']=='Ethereum' and x['token_contract'].lower()==D]
def net(xx):return sum(Decimal(x['raw_amount'])/10**18*(1 if x['token_recipient'].lower()==B else -1) for x in xx)
pre=[x for x in dai if x['utc_timestamp']<'2026-10-13T18:14:35Z'];post=[x for x in dai if x['utc_timestamp']>'2026-10-13T18:16:35Z']
assert net(pre)==Decimal('816635.912748421658923307')
assert net(post)==Decimal('21072.036962590546379139')
assert len(post)==4 and not any(x['token_sender'].lower()==B for x in post)
assert all('excluded_noncanonical' not in x['role'] for x in dai)
assert sum(x['token_sender'].lower()==B for x in pre)==3
print('PASS pre-arrival DAI delta, four subsequent inflows, no saved later DAI outgoing event, contamination exclusion')
pol=[x for x in r if x['chain']=='Polygon' and x['role']=='gas_funding'][0]
assert pol['utc_timestamp']=='2026-10-13T17:56:30Z' and pol['displayed_amount']=='20'
assert [x['nonce'] for x in c if x['kind']=='existing_G005_nonce_observation']==['0','1']
assert len([x for x in c if x['kind']=='approve' and x['allowance_raw'] in ['12139456905','19610310097']])==2
print('PASS recipient-to-sender funding, first-use nonces and exact allowance records')
repo=p.parent.parent;frozen='research/gamdom-incident-2026-10';base='2a67eaa900e7137c5230a080cf5b2f4207c0822a'
paths=subprocess.check_output(['git','-C',str(repo),'ls-tree','-r','--name-only',base,'--',frozen],text=True).splitlines()
assert paths
for path in paths:
 expected=subprocess.check_output(['git','-C',str(repo),'show',base+':'+path])
 assert (repo/path).read_bytes()==expected,path
assert {f.relative_to(repo).as_posix() for f in (repo/frozen).rglob('*') if f.is_file()}==set(paths)
print('PASS every frozen G005 file preserved byte-for-byte; no added descendants')
