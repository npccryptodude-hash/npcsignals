"""Offline replay: python3 verify.py. Standard library only. No network access.
Verifies preserved provider data and arithmetic; does not cryptographically authenticate responses or prove customer credit.
"""
import pathlib,json,hashlib,csv,datetime
P=pathlib.Path(__file__).resolve().parent
W='56HEQykziUkwvpK5uPzFrRbGD4Ek8HdWgjgeDvNmDoEJ';T='CzissnPHhEu7NifSLfwhuvFMdfu7F8X4vR2HhF1o1PEL';B='5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9';D='CyBjGpte4Npi5zNkdtWumPxVW4kpMR8BuFSbA587xZES';S='3QrJH49NS39jAtvEPn8BxCNGqkiwMZk1kSDJ2GU8f8jVU5GxVzxzd9bKSLx2KYkm7G6mPLP8Vsk3S94TuZMiayz2'
for name,h in json.loads((P/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==h,name
sigs=json.loads((P/'selected-signatures.json').read_text());sr=json.loads((P/'finality-0.request.json').read_text())['params'][0];st=dict(zip(sr,json.loads((P/'finality-0.rpc.json').read_text())['result']['value']));assert st==json.loads((P/'finality.json').read_text())
for a,expected in [(W,4),(T,5)]:
 h=json.loads((P/(a+'-history.json')).read_text());assert len(h['rows'])==expected and h['terminal_empty_page'] and h['pages'][-1]['rows']==[]
 first=json.loads((P/(a+'-page0.rpc.json')).read_text())['result'];terminal=json.loads((P/(a+'-terminal.rpc.json')).read_text())['result'];assert first==h['rows'] and terminal==[]
csvrows=list(csv.DictReader((P/'evidence-ledger.csv').open(newline='')));assert csvrows==json.loads((P/'ledger-matrix.json').read_text()) and len(csvrows)==28
records=json.loads((P/'instruction-ledger.json').read_text())
for s in sigs:
 t=json.loads((P/(s+'.rpc.json')).read_text())['result'];assert t==json.loads((P/(s+'.json')).read_text());m=t['meta'];assert st[s]['confirmationStatus']=='finalized' and st[s]['err'] is None and st[s]['slot']==t['slot'] and m['err'] is None
 assert sum(m['preBalances'])-sum(m['postBalances'])==m['fee']
 keys=t['transaction']['message']['accountKeys'];addr=[k['pubkey'] for k in keys];signers=[k['pubkey'] for k in keys if k['signer']];groups={'outer':t['transaction']['message']['instructions'],**{'inner:'+str(g['index']):g['instructions'] for g in m.get('innerInstructions',[]) or []}}
 for r in [r for r in records if r['signature']==s]:
  assert r['signers']==signers and r['fee_payer']==addr[0] and r['fee_lamports']==m['fee'] and r['utc']==datetime.datetime.fromtimestamp(t['blockTime'],datetime.timezone.utc).isoformat() and r['slot']==t['slot']
  if r['instruction_index']=='fee':continue
  label,i=r['instruction_index'].rsplit(':',1);ix=groups[label][int(i)];assert r['instruction_json']==json.dumps(ix,sort_keys=True)
t=json.loads((P/(S+'.json')).read_text());m=t['meta'];keys=t['transaction']['message']['accountKeys'];addr=[k['pubkey'] for k in keys];i,j=addr.index(T),addr.index(D);pre={b['accountIndex']:b for b in m['preTokenBalances']};post={b['accountIndex']:b for b in m['postTokenBalances']};v=t['transaction']['message']['instructions'][2]['parsed']['info'];n=995831502
assert v['source']==T and v['destination']==D and v['authority']==W and v['mint']=='Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB' and int(v['tokenAmount']['amount'])==n
assert pre[i]['owner']==post[i]['owner']==W and pre[j]['owner']==post[j]['owner']==B
assert int(pre[i]['uiTokenAmount']['amount'])-int(post[i]['uiTokenAmount']['amount'])==n and int(post[j]['uiTokenAmount']['amount'])-int(pre[j]['uiTokenAmount']['amount'])==n
assert m['fee']==14000 and addr[0]=='5JPAWfhLNsYVk3tPpD3gHvpHbvaXDbpUpy1wUfQVYRS2' and [k['pubkey'] for k in keys if k['signer']]==[addr[0],W]
flow=json.loads((P/'token-flow-ledger.json').read_text());known=other=out=0;balance=0
for r in flow:
 t=json.loads((P/(r['signature']+'.json')).read_text());m=t['meta'];addr=[k['pubkey'] for k in t['transaction']['message']['accountKeys']];index=addr.index(T);pre={b['accountIndex']:b for b in m['preTokenBalances']};post={b['accountIndex']:b for b in m['postTokenBalances']};pr=int(pre[index]['uiTokenAmount']['amount']) if index in pre else 0;po=int(post[index]['uiTokenAmount']['amount']) if index in post else 0;assert balance==pr
 n=int(r['raw_amount'])
 if r['source']==T:out+=n;balance-=n
 else:
  balance+=n
  if r['classification']=='known_case_inbound':
   source_index=addr.index(r['source']);assert pre[source_index]['owner']==post[source_index]['owner']=='6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N' and post[index]['owner']==W
   known+=n
  else:other+=n
 assert balance==po
assert known==995831402 and other==1100 and out==995831502 and balance==1000
created=json.loads((P/'45zVBfuvgtptBZuABucUsMiPHYQfG4pf4ium1629LREQyeFqCWF1rEh5VM5pVT4ukmYPPr3LDMbs7F6ku2RDg1kw.json').read_text());assert any(ix.get('parsed',{}).get('type')=='initializeAccount3' and ix['parsed']['info'].get('account')==T and ix['parsed']['info'].get('owner')==W for g in created['meta']['innerInstructions'] for ix in g['instructions'])
assert json.loads((P/'summary.json').read_text())['outgoing_raw']==out
print('PASS: checksums, two complete returned histories, five successful finalized receipts, 28 ledger rows, historical owners/signers/fee payer, 995.831502 USDT exchange-infrastructure transfer and 0.001000 USDT closing balance. Exchange affiliation separately SUPPORTED; customer credit UNRESOLVED.')
