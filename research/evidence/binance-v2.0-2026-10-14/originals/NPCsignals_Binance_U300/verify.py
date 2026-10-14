"""Offline check: python3 verify.py. Standard library only; no network requests.
Checks preserved RPC objects and arithmetic, not provider authenticity or exchange ownership.
"""
import pathlib,json,csv,hashlib,datetime
from decimal import Decimal
P=pathlib.Path(__file__).resolve().parent
manifest=json.loads((P/'SHA256SUMS.json').read_text())
for name,h in manifest.items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==h,name
statuses=json.loads((P/'finality.rpc.json').read_text())['result']['value'];sigs=json.loads((P/'finality.request.json').read_text())['params'][0];ledger=list(csv.DictReader((P/'instruction-ledger.csv').open(newline='')))
assert json.loads((P/'finality.json').read_text())==dict(zip(sigs,statuses))
assert len(ledger)==len(json.loads((P/'instruction-ledger.json').read_text()))
for sig,status in zip(sigs,statuses):
 envelope=json.loads((P/(sig+'.rpc.json')).read_text());assert 'error' not in envelope;t=envelope['result'];assert t==json.loads((P/(sig+'.json')).read_text());assert t['transaction']['signatures'][0]==sig
 assert status['confirmationStatus']=='finalized' and status['err'] is None and status['slot']==t['slot'] and t['meta']['err'] is None
 keys=t['transaction']['message']['accountKeys'];addr=[k['pubkey'] for k in keys];m=t['meta'];flow={a:0 for a in addr};flow[addr[0]]-=m['fee'];utc=datetime.datetime.fromtimestamp(t['blockTime'],datetime.timezone.utc).isoformat();signers=';'.join(k['pubkey'] for k in keys if k['signer'])
 selected=[r for r in ledger if r['signature']==sig];assert len(selected)==len(t['transaction']['message']['instructions'])+1
 for r in selected:
  assert r['utc']==utc and int(r['slot'])==t['slot'] and r['transaction_index']==str(t.get('transactionIndex','')) and r['signers']==signers and r['fee_payer']==addr[0] and int(r['fee_lamports'])==m['fee']
  if r['instruction_index']=='fee':assert int(r['lamports'])==m['fee'];continue
  ix=t['transaction']['message']['instructions'][int(r['instruction_index'].split(':')[1])];assert r['program_id']==ix['programId'];parsed=ix.get('parsed',{});v=parsed.get('info',{})
  assert r['instruction_type']==parsed.get('type','opaque')
  if 'lamports' in v:
   s,d,n=v['source'],v['destination'],v['lamports'];assert (r['source'],r['destination'],r['authority'],int(r['lamports']))==(s,d,s,n);assert Decimal(r['SOL'])==Decimal(n)/Decimal(10**9)
   a,b=addr.index(s),addr.index(d);assert [int(r[k]) for k in ['source_pre_lamports','source_post_lamports','destination_pre_lamports','destination_post_lamports']]==[m['preBalances'][a],m['postBalances'][a],m['preBalances'][b],m['postBalances'][b]];flow[s]-=n;flow[d]+=n
 for i,a in enumerate(addr):assert m['postBalances'][i]-m['preBalances'][i]==flow[a],(sig,a)
primary=(P/'ZYROX_primary_ledger.md').read_bytes();h=hashlib.sha1(b'blob '+str(len(primary)).encode()+b'\0'+primary).hexdigest();assert h==json.loads((P/'ZYROX_U300_public.json').read_text())['sha']
u=json.loads(next(l for l in primary.decode().splitlines() if '"id":"U300"' in l))
urow=next(r for r in ledger if r['id']=='BP002.I0');assert u['from']==urow['source'] and u['to']==urow['destination'] and u['tx']==urow['signature'] and Decimal(u['amount'])==Decimal(urow['SOL'])
target=next(r for r in ledger if r['id']=='BP001.I2');assert target['lamports']=='22896954041' and target['destination']=='5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9'
assert ledger==json.loads((P/'instruction-ledger.json').read_text())
print('PASS: hashes; 7 successful finalized receipt/status pairs; '+str(len(ledger))+' exact ledger rows; native balances and fees; exact current GitHub U300 blob and target transfer. Attribution is separately SUPPORTED; customer credit UNRESOLVED.')
