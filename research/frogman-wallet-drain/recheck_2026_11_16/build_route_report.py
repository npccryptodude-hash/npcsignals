import json,datetime
from pathlib import Path
from decimal import Decimal as D
P=Path(__file__).resolve().parent
R=P/'raw'
def get(n):
 try:return json.loads((R/(n+'.response')).read_text())
 except Exception:return None
def utc(t):return datetime.datetime.fromtimestamp(int(t),datetime.timezone.utc).isoformat()
lines=['# frogman / 4 eth route follow-up / 16 november 2026','','## what changed in the evidence','','the 13 november checkpoint established the 27 october spend and left the source replenishment unexplained. normal ethereum explorer history is now available; matching transaction, successful receipt and block records are retained for the later incoming transfers. this improves historical documentation, not a claim of new post-13-november transactions.','','## ethereum states','','| address role | native eth at pinned block | nonce |','|---|---:|---:|']
for n in ['source','destination']:
 b=get('eth_'+n+'_eth_getBalance');c=get('eth_'+n+'_eth_getTransactionCount');lines.append(f"| {n} | {D(int(b['result'],16))/D(10**18) if b and 'result' in b else 'unknown'} | {int(c['result'],16) if c and 'result'in c else 'unknown'} |")
block=get('eth_block')['result'];lines+=['',f"pinned ethereum block: {int(block['number'],16)} / `{block['hash']}` / {utc(int(block['timestamp'],16))}. both nonces remain 1, as in the 13 november checkpoint. this rules out a second ordinary account-originated transaction through the pinned block, not all possible internal/token activity.",'','## replenishment after the original spend','','| utc | sender | eth | transaction | rpc verification |','|---|---|---:|---|---|']
for i,t in enumerate(get('eth_source_txlist')['result']):
 if int(t['blockNumber'])<=26282041:continue
 tx=get('replenishment_'+str(i)+'_tx');rr=get('replenishment_'+str(i)+'_receipt');bb=get('replenishment_'+str(i)+'_block');ok=False
 if tx and rr and bb and tx.get('result') and rr.get('result') and bb.get('result'):
  a=tx['result'];r=rr['result'];b=bb['result'];ok=(a['hash']==t['hash'] and a['to'].lower()==t['to'].lower() and a['from'].lower()==t['from'].lower() and int(a['value'],16)==int(t['value']) and r['status']=='0x1' and r['blockHash']==b['hash'] and t['hash'] in b['transactions'])
 lines.append(f"| {utc(t['timeStamp'])} | `{t['from']}` | {D(t['value'])/D(10**18)} | `{t['hash']}` | {'pass' if ok else 'incomplete'} |")
lines+=['','the two larger incoming payments plus a small additional payment explain replenishment; the separate 0.000000001-eth incoming payment is also retained. similar-looking sender addresses are distinct addresses; no common operator, refund identity or victim provenance is inferred. source internal-history request failed with http 500; destination internal history explicitly reports unprocessed records (status 2). neither result supports a zero-internal-activity claim. normal history lists are bounded to 1,000 entries, with fewer returned; indexer completeness is not independently guaranteed.','','## mayan correspondence','','the newly successful first-party mayan response directly identifies source transaction `0x38c7c72a6da978ee29e18649d5005d8978fbde862c0f78eb18fd70325e6939bf`, order `0x47ecec44471cd15a4550897590a825a94e50aa43900e893f88ca2fa0a75b5fcb`, recipient `AKS15GjeivY1yBN3at6DNSg7q6UBmsPFtA2jWzvTniep`, input 3.998918422844160119 eth and output 92.375240889 sol. it lists settlement signature `3acQkJbsmUo3cj5NoSngvGH2oWoZst9pujcHh41DvCKNZ9J3yR1usKNW1bDgj49cuGfMKHX2dmLjSePg733K4kHC`. this strengthens the supported cross-chain correspondence with an explicit protocol record; independent order-state/pda verification remains outstanding. its `redeem`/`unlock` fields concern this mayan bridge operation, not xmr1 redemption.','','## solana continuation','','the previously documented 92.375240889-sol recipient forwards into mixed recipient `EfaGnkjvYEtN9yCbetyUyZmmabmBzgeGEc9LMod6pV3y`. fresh transactions below show account activity at that mixed boundary. no exclusive allocation of the original 4-eth value is made.','','| account queried | returned signatures | latest returned utc | native sol snapshot |','|---|---:|---|---:|']
for n in ['oct27_destination','mixed_boundary','next_boundary']:
 h=get('sol_'+n+('_history' if n=='next_boundary' else '_getSignaturesForAddress'));b=get('sol_'+n+('_balance' if n=='next_boundary' else '_getBalance'));rr=h.get('result') if h else None
 lines.append(f"| {n} | {len(rr) if isinstance(rr,list) else 'unknown'} | {utc(rr[0]['blockTime']) if rr else 'unknown'} | {D(b['result']['value'])/D(10**9) if b and b.get('result') else 'unknown'} |")
lines+=['','### parsed system transfers in the newly fetched mixed-boundary transactions','','| utc | source | destination | sol | signature |','|---|---|---|---:|---|']
for f in sorted(list(R.glob('sol_mixed_boundary_tx_*.response'))+list(R.glob('sol_next_boundary_tx_*.response'))):
 d=json.loads(f.read_text()).get('result')
 if not d or d['meta']['err'] is not None:continue
 ins=d['transaction']['message']['instructions']+sum([x['instructions'] for x in d['meta'].get('innerInstructions',[])],[])
 for x in ins:
  if x.get('program')=='system' and x.get('parsed',{}).get('type')=='transfer':
   q=x['parsed']['info'];lines.append(f"| {utc(d['blockTime'])} | `{q['source']}` | `{q['destination']}` | {D(q['lamports'])/D(10**9)} | `{d['transaction']['signatures'][0]}` |")
lines+=['','the next boundary also shows a 458.52-sol outgoing transfer on 27 october and a multi-source small-balance sweep on 9 november (0.0100047 sol from that address). these are account-level facts beyond mixed funding; no exclusive allocation is made. the mixed account forwarded 216.46 sol to `G82K2R2RgJyBwfezs6ey2TXPzjR7oNEGr9WTMWinGTda` on 27 october. a fresh bounded history/balance query for that next address is retained. this is an account-level continuation past a mixed-funding boundary, not a deterministic attribution of 216.46 sol to the 4-eth branch. no human beneficiary or platform label is assigned.','','## publication effect','','the historical narrative can now explain the source replenishment and show a stronger protocol-supported mayan correspondence and later mixed-account transfer. these are older events newly documented in this recheck. the remaining internal-history and cross-chain verification limits must stay visible. the endpoint is not a proven final beneficiary. no medium publication was performed.']
(P/'ROUTE_REPORT.md').write_text('\n'.join(lines)+'\n')
print('route report built')
