"""Offline exact-integer derivation. JSON raw units are strings to avoid IEEE754 loss."""
import pathlib,json,gzip,collections,datetime,hashlib,csv
R=pathlib.Path(__file__).resolve().parent
BASE='00bb8846e65ce0ac44446e02185c5d859bc9bca3'
X='0x4b304741599c125a244e498d14562487d7109ab8'
B='0xe5686aae44d392aa6a0637fd38393859502f8667'
A='0xd5fbda4c79f38920159fe5f22df9655fde292d47'
S1='0x0067cc2416f792cf0ec5629f5506324ac508f859'
S2='0x580450dff316ae00d0fbef9621a304020a046ce2'
T='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
TOK={'0xdac17f958d2ee523a2206206994597c13d831ec7':('USDT',6),'0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48':('USDC',6),'0x6b175474e89094c44da98b954eedeac495271d0f':('DAI',18),'0x8d0d000ee44948fc98c9b98a4fa4921476f08b0d':('USD1',18)}
def records():
 if (R/'rpc_archive.json.gz').exists():return json.loads(gzip.decompress((R/'rpc_archive.json.gz').read_bytes()))
 return {p.stem:json.loads(p.read_text()) for p in sorted((R/'evidence').glob('*.json'))}
def integer(n):return int(n,16)
def amount(n,d):
 sign='-' if n<0 else '';n=abs(n)
 return sign+str(n//10**d)+('.'+str(n%10**d).zfill(d) if d else '')
def iso(n):return datetime.datetime.fromtimestamp(integer(n),datetime.timezone.utc).isoformat().replace('+00:00','Z')
def derive():
 e=records()
 def result(n):return e[n]['response']['result']
 old=set()
 for directory in ['gamdom-incident-2026-10','gamdom-incident-2026-10-g006','gamdom-incident-2026-10-g008','gamdom-incident-2026-10-g009']:
  for p in (R.parent/directory).glob('*.csv'):
   for row in csv.DictReader(p.open()):
    old.update(v.lower() for v in row.values() if v and len(v)==66 and v.startswith('0x'))
 txs={};events=[]
 for n,o in e.items():
  if not (n.startswith('receipt_') or n.startswith('bnb_receipt_')):continue
  r=o.get('response',{}).get('result')
  if not r:continue
  h=r['transactionHash'];pre='bnb_' if n.startswith('bnb_') else ''
  t=result(pre+'tx_'+h);b=result(pre+'block_'+str(integer(r['blockNumber'])))
  assert h==t['hash']==b['transactions'][integer(r['transactionIndex'])]
  assert r['blockHash']==b['hash']==t['blockHash'] and r['status'] in ['0x0','0x1']
  chain=56 if pre else 1;url=('https://bscscan.com/tx/' if pre else 'https://etherscan.io/tx/')+h
  common={'chain_id':chain,'transaction_hash':h,'block':integer(r['blockNumber']),'transaction_index':integer(r['transactionIndex']),'timestamp_utc':iso(b['timestamp']),'initiator':t['from'],'transaction_to':t['to'],'success':r['status']=='0x1','native_value_raw':str(integer(t['value'])),'fee_raw':str(integer(r['gasUsed'])*integer(r['effectiveGasPrice'])),'fee_asset':'BNB' if pre else 'ETH','source_url':url,'rpc_record':n,'evidence_level':'CONFIRMED receipt/status; unauthorized status UNRESOLVED','new_beyond_frozen':h not in old}
  txs[(chain,h)]=common
  for l in r['logs']:
   if len(l['topics'])!=3 or l['topics'][0]!=T:continue
   token=l['address'];fr='0x'+l['topics'][1][-40:];to='0x'+l['topics'][2][-40:]
   if chain==1 and X not in [fr,to] and B not in [fr,to]:continue
   if chain==56 and token!='0x55d398326f99059ff775485246999027b3197955':continue
   if chain==1 and token not in TOK:continue
   symbol,d=TOK[token] if chain==1 else ('USDT',18)
   raw=integer(l['data'])
   classification=('bridge_destination_output_not_original_principal' if B in [fr,to] else 'candidate_original_principal' if to==X and fr in [A,S1,S2] else 'swap_output' if to==X else 'swap_input') if chain==1 else 'bridge_deposit_intermediate_edge_do_not_sum_twice'
   events.append({**common,'log_index':integer(l['logIndex']),'token_contract':token,'token_symbol':symbol,'decimals':d,'token_sender':fr,'token_recipient':to,'raw_amount':str(raw),'amount':amount(raw,d),'classification':classification})
 native=[]
 for (chain,h),t in txs.items():
  if chain!=1 or X not in [t['initiator'],t['transaction_to']]:continue
  raw=int(t['native_value_raw']) if t['success'] else 0
  native.append({**t,'token_sender':t['initiator'],'token_recipient':t['transaction_to'],'token_symbol':'ETH','decimals':18,'raw_amount':str(raw),'amount':amount(raw,18),'classification':'failed_no_principal_movement' if not t['success'] else 'candidate_original_principal' if t['initiator'] in [A,S1,S2] and t['transaction_to']==X else 'return_to_A' if t['transaction_to']==A else 'unsolicited_lookalike_dust' if raw else 'authorization_self_transaction'})
 reconciliation=[]
 for wallet,n in [(X,'E1'),(B,'B')]:
  for token,(symbol,d) in TOK.items():
   alias='USDE' if symbol=='USD1' else symbol
   opening=integer(result(f'state_{n}_{alias}_26184449'));closing=integer(result(f'state_{n}_{alias}_26185250'))
   logs=[]
   for pos in [1,2]:logs+=result(f'{n}_window_{pos}')
   logs=list({(l['transactionHash'],l['logIndex']):l for l in logs}.values())
   incoming=sum(integer(l['data']) for l in logs if l['address']==token and l['topics'][2][-40:]==wallet[2:])
   outgoing=sum(integer(l['data']) for l in logs if l['address']==token and l['topics'][1][-40:]==wallet[2:])
   assert opening+incoming-outgoing==closing
   reconciliation.append({'wallet':wallet,'token':symbol,'contract':token,'decimals':d,'opening_block':26184449,'closing_block':26185250,'opening_raw':str(opening),'inflows_raw':str(incoming),'outflows_raw':str(outgoing),'closing_raw':str(closing),'residual_raw':'0','closing_amount':amount(closing,d)})
 opening=integer(result('native_E1_26184449'));closing=integer(result('native_E1_26185250'))
 incoming=sum(int(t['raw_amount']) for t in native if t['token_recipient']==X and t['token_sender']!=X)
 outgoing=sum(int(t['raw_amount']) for t in native if t['token_sender']==X and t['token_recipient']!=X)
 fees=sum(int(t['fee_raw']) for t in native if t['initiator']==X)
 assert opening+incoming-outgoing-fees==closing,(opening,incoming,outgoing,fees,closing)
 reconciliation.append({'wallet':X,'token':'ETH','decimals':18,'opening_block':26184449,'closing_block':26185250,'opening_raw':str(opening),'inflows_raw':str(incoming),'outflows_raw':str(outgoing),'fees_raw':str(fees),'closing_raw':str(closing),'closing_amount':amount(closing,18),'residual_raw':'0'})
 sums=collections.defaultdict(int)
 for row in events+native:
  if row['classification']=='candidate_original_principal':sums[row['token_symbol']]+=int(row['raw_amount'])
 summary={'new_transactions':sum(t['new_beyond_frozen'] for t in txs.values()),'existing_transactions_extended_not_recounted':sum(not t['new_beyond_frozen'] for t in txs.values()),'new_hashes':[t['transaction_hash'] for t in txs.values() if t['new_beyond_frozen']],'E1_principal_units':{s:amount(v,6 if s in ['USDT','USDC'] else 18) for s,v in sums.items()},'verified_unauthorized_loss_usd':None,'earliest_candidate':min([r for r in events+native if r['classification']=='candidate_original_principal'],key=lambda r:(r['block'],r['transaction_index']))}
 baseline=[]
 for a,n in [(A,'A'),(S1,'S1'),(S2,'S2')]:
  ls={}
  for pos in [1,2]:
   for l in result(f'{n}_baseline_{pos}'):ls[(l['transactionHash'],l['logIndex'])]=l
  for token,(symbol,d) in TOK.items():
   outgoing=[l for l in ls.values() if l['address']==token and l['topics'][1][-40:]==a[2:]]
   vals=sorted(integer(l['data']) for l in outgoing)
   baseline.append({'address':a,'symbol':symbol,'contract':token,'from_block':26177200,'to_block':26184449,'outgoing_event_count':len(outgoing),'outgoing_sum_raw':str(sum(vals)),'maximum_outgoing_raw':str(max(vals)) if vals else None,'distinct_outgoing_recipients':len({l['topics'][2] for l in outgoing}),'prior_transfers_to_E1':sum(l['topics'][2][-40:]==X[2:] for l in outgoing),'native_nonce_at_end':integer(result(f'nonce_{n}_26184449')),'scope':'Event records only; partial two-day baseline; not full receipt verification or anomaly score'})
 principal=[]
 for a in [A,S1,S2]:
  for symbol,d in [('USDT',6),('USDC',6),('USD1',18),('DAI',18),('ETH',18)]:
   v=sum(int(row['raw_amount']) for row in events+native if row['classification']=='candidate_original_principal' and row['token_sender']==a and row['token_symbol']==symbol)
   if v:principal.append({'sender':a,'recipient':X,'symbol':symbol,'decimals':d,'raw_amount':str(v),'amount':amount(v,d)})
 return {'incident_origin_ledger':sorted(events+native,key=lambda r:(r['chain_id'],r['block'],r['transaction_index'],r.get('log_index',-1))),'transaction_register':sorted(txs.values(),key=lambda r:(r['chain_id'],r['block'],r['transaction_index'])),'balance_reconciliation':reconciliation,'baseline_comparison':baseline,'principal_by_source':principal,'results':summary}
if __name__=='__main__':
 for name,value in derive().items():(R/(name+'.json')).write_text(json.dumps(value,indent=2)+'\n')
 print(json.dumps(derive()['results'],indent=2))
