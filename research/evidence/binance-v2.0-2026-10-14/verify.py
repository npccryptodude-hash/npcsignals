"""Offline verifier: Python 3 standard library; no network calls, no writes to archive.
Response consistency/integrity is tested, not cryptographic RPC authenticity or customer credit.
"""
import pathlib,json,hashlib,csv,datetime,tempfile,zipfile,subprocess,sys
from decimal import Decimal
P=pathlib.Path(__file__).resolve().parent
def read(p):return json.loads((P/p).read_text())
manifest=read('SHA256SUMS.json')
actual={str(p.relative_to(P)) for p in P.rglob('*') if p.is_file() and p!=P/'SHA256SUMS.json'}
assert actual==set(manifest),'Manifest coverage mismatch'
for f,h in manifest.items():assert hashlib.sha256((P/f).read_bytes()).hexdigest()==h,f
logs=[]
with tempfile.TemporaryDirectory(prefix='npc-binance-offline-') as tmp:
 for a in read('archive-inventory.json'):
  file=P/a['file'];assert hashlib.sha256(file.read_bytes()).hexdigest()==a['sha256'];assert file.stat().st_size==a['bytes']
  with zipfile.ZipFile(file) as z:
   assert z.testzip() is None and len(z.namelist())==a['members']
   for n in z.namelist():assert not pathlib.PurePosixPath(n).is_absolute() and '..' not in pathlib.PurePosixPath(n).parts
   if a.get('unpacked_root'):
    for n in z.namelist():
     if not n.endswith('/'):assert (P/'originals'/n).read_bytes()==z.read(n),n
   if a['file'].endswith('NPCsignals_Binance_Archive_2026-10-14.zip'):continue
   destination=pathlib.Path(tmp)/file.stem;z.extractall(destination)
   script=next(destination.glob('*/verify.py'))
   r=subprocess.run([sys.executable,str(script)],capture_output=True,text=True,check=True);logs.append(r.stdout.strip())
rows=list(csv.DictReader((P/'five-transfer-ledger.csv').open(newline='')))
assert rows==read('five-transfer-ledger.json') and len(rows)==5
assert read('five-transfer-matrix.json')==[list(rows[0])]+[list(r.values()) for r in rows]
binance='5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9'
u300='8zHcWujHhyJri3CRTcWUGmT5WSRdwW7xrns3WTTkPGvS'
native_sum=0
for r in rows:
 t=read(r['receipt_file'])['result'];m=t['meta'];ks=t['transaction']['message']['accountKeys'];addr=[k['pubkey'] for k in ks];ix=t['transaction']['message']['instructions'][2];v=ix['parsed']['info'];i,j=addr.index(v['source']),addr.index(v['destination'])
 assert t['transaction']['signatures'][0]==r['signature'] and m['err'] is None
 assert r['utc']==datetime.datetime.fromtimestamp(t['blockTime'],datetime.timezone.utc).isoformat() and int(r['slot'])==t['slot']
 assert r['instruction_index']=='outer:2' and r['instruction_type']==ix['parsed']['type']
 assert r['source_account']==v['source'] and r['receiving_account']==v['destination']
 assert r['authority']==v.get('authority',v.get('multisigAuthority',v['source']))
 assert r['signers']==';'.join(k['pubkey'] for k in ks if k['signer']) and r['fee_payer']==addr[0] and int(r['fee_lamports'])==m['fee']
 for field,index,balances in [('source_pre_lamports',i,'preBalances'),('source_post_lamports',i,'postBalances'),('receiver_pre_lamports',j,'preBalances'),('receiver_post_lamports',j,'postBalances')]:assert int(r[field])==m[balances][index]
 assert sum(m['preBalances'])-sum(m['postBalances'])==m['fee']
 n=int(r['raw_amount']);assert Decimal(r['exact_amount'])==Decimal(n)/10**int(r['decimals'])
 if r['asset']=='SOL':
  native_sum+=n;assert v['lamports']==n and v['source']==u300 and v['destination']==binance
  assert m['preBalances'][i]-m['postBalances'][i]==n+m['fee'] and m['postBalances'][j]-m['preBalances'][j]==n
  assert r['signers']==u300 and m['fee']==9000
  root=pathlib.PurePosixPath(r['receipt_file']).parent
  f='candidate-finality.json' if 'Additional' in str(root) else 'finality.json'
  status=read(str(root/f))[r['signature']]
 else:
  assert n==995831502 and v['tokenAmount']['amount']==str(n) and v['tokenAmount']['decimals']==6
  assert v['mint']==r['mint']=='Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB'
  pre={b['accountIndex']:b for b in m['preTokenBalances']};post={b['accountIndex']:b for b in m['postTokenBalances']}
  assert pre[i]['owner']==post[i]['owner']==r['source_historical_owner']==r['authority']
  assert pre[j]['owner']==post[j]['owner']==r['receiver_historical_owner']==binance
  for field,b in [('source_pre_token_raw',pre[i]),('source_post_token_raw',post[i]),('receiver_pre_token_raw',pre[j]),('receiver_post_token_raw',post[j])]:assert r[field]==b['uiTokenAmount']['amount']
  assert int(r['source_pre_token_raw'])-int(r['source_post_token_raw'])==n and int(r['receiver_post_token_raw'])-int(r['receiver_pre_token_raw'])==n
  status=read('originals/NPCsignals_56HE_Binance/finality.json')[r['signature']]
 assert status['confirmationStatus']=='finalized' and status['err'] is None and status['slot']==t['slot']
assert native_sum==472929423997
support=read('supporting/finality.json')
for s,status in support.items():
 t=read('supporting/'+s+'.replacement.rpc.json')['result'];assert status['confirmationStatus']=='finalized' and status['err'] is None and status['slot']==t['slot'];assert t['meta']['err'] is None and t['transaction']['signatures'][0]==s
 old=read('supporting/'+s+'.preserved-parsed.json')
 assert old['slot']==t['slot'] and old['blockTime']==t['blockTime'] and old['transaction']==t['transaction']
 for field in ['preBalances','postBalances','err','fee','innerInstructions']:assert old['meta'][field]==t['meta'][field]
 if s.startswith('61v1'):
  addr=[k['pubkey'] for k in t['transaction']['message']['accountKeys']];m=t['meta'];flow={a:0 for a in addr};flow[addr[0]]-=m['fee']
  target=[]
  for ix in t['transaction']['message']['instructions']:
   v=ix.get('parsed',{}).get('info',{})
   if 'lamports' in v:
    flow[v['source']]-=v['lamports'];flow[v['destination']]+=v['lamports']
    if v['destination']=='6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N':target.append(v)
  assert len(target)==1 and target[0]['lamports']==435460959353 and target[0]['source']=='F2khA1QZooUzidyycMzpJ6x38eQBxuDq4UrvdUUiSwuo'
  for i,a in enumerate(addr):assert m['postBalances'][i]-m['preBalances'][i]==flow[a]
 else:
  key='8uKAGuxowd2eM4vfzgorTq9dCBZoeSNTpsmLhziziWfK';addr=[k['pubkey'] for k in t['transaction']['message']['accountKeys']];i=addr.index(key)
  for field in ['preTokenBalances','postTokenBalances']:assert next(b for b in t['meta'][field] if b['accountIndex']==i)['owner']=='6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N'
print('\n'.join(logs))
print('PASS: complete archive hashes; unchanged original ZIP members; five finalized transfer rows; 472.929423997 SOL + 995.831502 USDT; full signatures, UTC, slots, zero-based indices, owners, authority, signer/payer and balances; two replacement linkage receipts. No customer-credit inference.')
