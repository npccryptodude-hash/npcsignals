#!/usr/bin/env python3
"""Validate saved evidence and preserve the frozen directories. Does not query nodes."""
import csv,hashlib,json,pathlib,re,subprocess
from decimal import Decimal
from verify_authorization import calculate
R=pathlib.Path(__file__).resolve().parent
BASE='bc834822f0e4956fc78c1746eb958fecb290ef39'
REPO=R.parents[1]
manifest=json.loads((R/'SHA256SUMS.json').read_text())
actual={str(p.relative_to(R)) for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='SHA256SUMS.json'}
assert set(manifest)==actual
for name,digest in manifest.items():assert hashlib.sha256((R/name).read_bytes()).hexdigest()==digest,name
print('PASS manifest coverage and every SHA-256 digest')
result=calculate()
assert result==json.loads((R/'evidence/authorization_verification.json').read_text())
print('PASS raw transaction hash, strict RLP, both recovered B signatures and batch calldata')
obs=json.loads((R/'evidence/execution_observations.json').read_text())
assert obs['logs'][0]['raw_value']==result['decoded_approval']['allowance_raw']
assert obs['logs'][0]['spender'].lower()==result['decoded_approval']['spender']
assert obs['logs'][1]['order_uid']==result['decoded_pre_signature']['order_uid']
assert obs['logs'][1]['signed']==result['decoded_pre_signature']['signed']
assert len(obs['advanced_internal_call_table'])==len(result['calls'])==2
for a,b in zip(obs['advanced_internal_call_table'],result['calls']):assert a['to'].lower()==b['target']
print('PASS decoded calls agree with saved approval, pre-signature and explorer call observations')
rows=list(csv.DictReader((R/'funding_transaction_ledger.csv').open()))
assert len(rows)==5 and len({r['tx_hash'] for r in rows})==5
assert rows==[{k:str(v) for k,v in r.items()} for r in json.loads((R/'evidence/funding_observations.json').read_text())['events']]
C='0xacc0c1f672b03b9a5fed4535f840f09b85f40e98';D='0xe757683a51cfd002de479385c2f4c9db10a5e8d2'
incoming=outgoing=0
for r in rows:
 assert re.fullmatch('0x[0-9a-f]{64}',r['tx_hash'])
 assert r['token_contract']=='0xc2132d05d31c914a87c6611c10748aeb04b58e8f'
 assert r['success']=='true' and r['authorization_status']=='UNRESOLVED'
 assert Decimal(r['amount'])==Decimal(r['raw_amount'])/(10**int(r['decimals']))
 assert r['tx_sender']==r['token_sender']==r['fee_payer']
 assert 95434113<=int(r['block_number'])<95472497
 if r['token_recipient'].lower()==C:
  assert r['token_sender'].lower()==D;incoming+=int(r['raw_amount'])
 else:
  assert r['token_sender'].lower()==C;outgoing+=int(r['raw_amount'])
assert incoming==714470970 and outgoing==539775442 and incoming-outgoing==174695528
print('PASS five unique funding receipts, raw units, chronology and exact +174.695528 USDT0 sample delta')
for directory in ['research/gamdom-incident-2026-10','research/gamdom-incident-2026-10-g006']:
 names=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'--',directory],cwd=REPO,text=True).splitlines()
 found={str(p.relative_to(REPO)) for p in (REPO/directory).rglob('*') if p.is_file()}
 assert set(names)==found
 for name in names:assert (REPO/name).read_bytes()==subprocess.check_output(['git','show',f'{BASE}:{name}'],cwd=REPO),name
print('PASS both frozen evidence directories preserved byte-for-byte with no extra descendants')
