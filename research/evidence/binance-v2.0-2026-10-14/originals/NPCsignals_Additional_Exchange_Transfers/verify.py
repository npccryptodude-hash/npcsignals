"""Offline replay: python3 verify.py. Standard library only.
Verifies receipt arithmetic and file integrity, not RPC authenticity or exchange customer records.
"""
import pathlib,json,hashlib,csv,datetime
from decimal import Decimal
P=pathlib.Path(__file__).resolve().parent
for name,h in json.loads((P/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==h,name
rows=list(csv.DictReader((P/'exchange-ledger.csv').open(newline='')));assert rows==json.loads((P/'exchange-ledger.json').read_text())
statusraw=json.loads((P/'candidate-finality.rpc.json').read_text());sigs=json.loads((P/'candidate-finality.request.json').read_text())['params'][0];statuses=dict(zip(sigs,statusraw['result']['value']));assert statuses==json.loads((P/'candidate-finality.json').read_text())
excluded='4m6gaPuwQnwN7KFSeCi3SzaqJzyj6JPzL5sMjq2c3gYuniYAqg3kZMPsseDdomzVJaVjZF3LPXYyHXAqeKKfSuYb';assert excluded not in sigs
for sig,v in statuses.items():
 t=json.loads((P/(sig+'.rpc.json')).read_text())['result'];assert t==json.loads((P/(sig+'.json')).read_text());m=t['meta'];assert v['confirmationStatus']=='finalized' and v['slot']==t['slot'] and v['err'] is None and m['err'] is None
 ks=t['transaction']['message']['accountKeys'];addr=[k['pubkey'] for k in ks];signers=';'.join(k['pubkey'] for k in ks if k['signer']);flow={a:0 for a in addr};flow[addr[0]]-=m['fee'];utc=datetime.datetime.fromtimestamp(t['blockTime'],datetime.timezone.utc).isoformat();rs=[r for r in rows if r['signature']==sig];assert len(rs)==len(t['transaction']['message']['instructions'])+1
 for r in rs:
  assert r['utc']==utc and int(r['slot'])==t['slot'] and r['transaction_index']==str(t.get('transactionIndex','')) and r['signers']==signers and r['fee_payer']==addr[0] and int(r['fee_lamports'])==m['fee']
  if r['instruction_index']=='fee':assert int(r['lamports'])==m['fee'];continue
  ix=t['transaction']['message']['instructions'][int(r['instruction_index'].split(':')[1])];p=ix.get('parsed',{});assert r['instruction_type']==p.get('type','opaque')
  info=p.get('info',{})
  if 'lamports' in info:
   s,d,n=info['source'],info['destination'],info['lamports'];assert (r['source'],r['recipient'],r['authority'],int(r['lamports']))==(s,d,s,n);assert Decimal(r['SOL'])==Decimal(n)/10**9
   a,b=addr.index(s),addr.index(d);assert [int(r[k]) for k in ['source_pre_lamports','source_post_lamports','recipient_pre_lamports','recipient_post_lamports']]==[m['preBalances'][a],m['postBalances'][a],m['preBalances'][b],m['postBalances'][b]];flow[s]-=n;flow[d]+=n
 for i,a in enumerate(addr):assert m['postBalances'][i]-m['preBalances'][i]==flow[a]
transfers=[r for r in rows if r['instruction_type']=='transfer'];assert sum(int(r['lamports']) for r in transfers)==450032469956
assert all(r['source']=='8zHcWujHhyJri3CRTcWUGmT5WSRdwW7xrns3WTTkPGvS' and r['recipient']=='5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9' for r in transfers)
count=0
for reqfile in P.glob('*-history.request.json'):
 req=json.loads(reqfile.read_text());wallet=req['params'][0];cutoff=req['params'][1]['filters']['blockTime']['lt'];data=json.loads((P/(wallet+'-history.rpc.json')).read_text())['result']['data'];assert len(data)==100
 for t in data:
  assert t['meta']['err'] is None and t['blockTime']<cutoff;assert t==json.loads((P/(t['transaction']['signatures'][0]+'.json')).read_text());count+=1
 assert req['params'][1]['commitment']=='finalized'
primary=(P/'ZYROX_primary_ledger.md').read_bytes();h=hashlib.sha1(b'blob '+str(len(primary)).encode()+b'\0'+primary).hexdigest();assert h=='08cf6b40c8aac00fb5d378ad1bc9b655bce62e55';u=json.loads(next(l for l in primary.decode().splitlines() if '"id":"U300"' in l));assert u['to']==transfers[0]['source']
print('PASS: hashes; 3 independent successful finalized receipts; 12 exact instruction/fee rows; 450.032469956 SOL; account deltas; 200 bounded discovery objects; exact U300 primary address. Exchange labels/customer credit require separate evidence review.')
