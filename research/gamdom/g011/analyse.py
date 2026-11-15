"""Offline integer accounting of preserved BNB USDT evidence."""
import pathlib,json,gzip,collections,datetime
R=pathlib.Path(__file__).resolve().parent
BASE='2a5fb31c97a39f9aebaf945dee8b5e0d05110b19'
B='0xe5686aae44d392aa6a0637fd38393859502f8667'
A='0xd5fbda4c79f38920159fe5f22df9655fde292d47'
S1='0x0067cc2416f792cf0ec5629f5506324ac508f859'
TOKEN='0x55d398326f99059ff775485246999027b3197955'
T='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
APPROVAL='0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925'
def records():
 if (R/'rpc_archive.json.gz').exists():return json.loads(gzip.decompress((R/'rpc_archive.json.gz').read_bytes()))
 return {p.stem:json.loads(p.read_text()) for p in sorted((R/'evidence').glob('*.json'))}
def n(x):return int(x,16)
def amt(x):
 sign='-' if x<0 else '';x=abs(x)
 return sign+str(x//10**18)+'.'+str(x%10**18).zfill(18)
def timestamp(h):return datetime.datetime.fromtimestamp(n(h['timestamp']),datetime.timezone.utc).isoformat().replace('+00:00','Z')
def derive():
 e=records();old=json.loads(gzip.decompress((R.parent/'gamdom-incident-2026-10-g010/rpc_archive.json.gz').read_bytes()))
 def get(k):return e[k]['response']['result']
 def gettx(h):
  if 'tx_'+h in e:
   t=get('tx_'+h);r=get('receipt_'+h);b=get('block_'+str(n(r['blockNumber'])));record='G011:receipt_'+h;new=True
  else:
   t=old['bnb_tx_'+h]['response']['result'];r=old['bnb_receipt_'+h]['response']['result'];b=old['bnb_block_'+str(n(r['blockNumber']))]['response']['result'];record='G010:bnb_receipt_'+h;new=False
  assert t['hash']==r['transactionHash']==h==b['transactions'][n(r['transactionIndex'])]
  assert t['blockHash']==r['blockHash']==b['hash'] and r['status']=='0x1'
  return t,r,b,record,new
 rows=[];approval=[];registry=[]
 hashes={k[3:] for k in e if k.startswith('tx_')}|{l['transactionHash'] for pos in [1,2] for l in get('B_extended_'+str(pos))}
 for h in sorted(hashes):
  t,r,b,record,new=gettx(h)
  common={'chain':'BNB Smart Chain','chain_id':56,'transaction_hash':h,'block':n(r['blockNumber']),'transaction_index':n(r['transactionIndex']),'timestamp_utc':timestamp(b),'transaction_initiator':t['from'],'transaction_to':t['to'],'nonce':n(t['nonce']),'success':True,'fee_payer':t['from'],'fee_raw_wei':str(n(r['gasUsed'])*n(r['effectiveGasPrice'])),'fee_asset':'BNB','receipt_record':record,'source_url':'https://bscscan.com/tx/'+h,'new_transaction':new,'evidence_level':'CONFIRMED primary transaction representation; unauthorized status UNRESOLVED'}
  registry.append(common)
  for l in r['logs']:
   if l['address']!=TOKEN or len(l['topics'])!=3:continue
   fr='0x'+l['topics'][1][-40:];to='0x'+l['topics'][2][-40:];raw=n(l['data'])
   assert l['transactionHash']==h and l['blockHash']==b['hash']
   if l['topics'][0]==T:
    # Preserve selected upstream edges but avoid duplicate intermediary bridge debits.
    if B in [fr,to]:role='B_funding' if to==B else 'bridge_deposit_existing' if not new else 'settlement_debit_no_verified_onward_consideration'
    elif new:role='selected_S1_upstream_or_baseline' if S1 in [fr,to] else 'settlement_intermediary_do_not_sum_twice'
    else:continue
    rows.append({**common,'log_index':n(l['logIndex']),'token_contract':TOKEN,'symbol':'USDT','decimals':18,'token_sender':fr,'token_recipient':to,'raw_amount':str(raw),'amount':amt(raw),'role':role})
   elif l['topics'][0]==APPROVAL and fr==B:
    approval.append({**common,'log_index':n(l['logIndex']),'token_contract':TOKEN,'owner':fr,'spender':to,'allowance_raw':str(raw),'allowance_units':amt(raw),'direct_approve_call':t['from']==B and t['to']==TOKEN and t['input'].startswith('0x095ea7b3')})
 rows.sort(key=lambda r:(r['block'],r['transaction_index'],r['log_index']))
 b_events=[r for r in rows if B in [r['token_sender'],r['token_recipient']]]
 indexed={(l['transactionHash'],n(l['logIndex'])):l for pos in [1,2] for l in get('B_extended_'+str(pos))}
 assert {(r['transaction_hash'],r['log_index']) for r in b_events}==set(indexed)
 for r in b_events:
  l=indexed[(r['transaction_hash'],r['log_index'])];assert int(r['raw_amount'])==n(l['data']) and r['token_contract']==l['address']
 walk=[];balance=n(get('B_state_127399999'))
 for row in b_events:
  delta=int(row['raw_amount'])*(1 if row['token_recipient']==B else -1)
  walk.append({**row,'opening_balance_raw':str(balance),'delta_raw':str(delta),'closing_balance_raw':str(balance+delta),'closing_balance':amt(balance+delta)});balance+=delta
 rec=[]
 for lo,hi in [(127399999,127435561),(127399999,127435562),(127435562,127444805),(127444805,127444806),(127399999,127444806),(127437353,127444208)]:
  opening=n(get('B_state_'+str(lo)));closing=n(get('B_state_'+str(hi)))
  selected=[r for r in b_events if lo<r['block']<=hi]
  incoming=sum(int(r['raw_amount']) for r in selected if r['token_recipient']==B);outgoing=sum(int(r['raw_amount']) for r in selected if r['token_sender']==B)
  assert opening+incoming-outgoing==closing
  rec.append({'wallet':B,'token':TOKEN,'decimals':18,'opening_block':lo,'closing_block':hi,'opening_raw':str(opening),'incoming_raw':str(incoming),'outgoing_raw':str(outgoing),'closing_raw':str(closing),'closing_amount':amt(closing),'residual_raw':'0'})
 # Source S1 bounded pooled accounting, not exclusive fungible-unit provenance.
 source_logs=[]
 for name in ['S1_short_127400000','S1_short_127410000','S1_short_127420000','S1_finish']:
  for pos in [1,2]:source_logs+=get(name+'_'+str(pos))
 source_logs=list({(l['transactionHash'],l['logIndex']):l for l in source_logs}.values())
 opening=n(get('S1_state_127399999'));closing=n(get('S1_state_127432896'))
 incoming=sum(n(l['data']) for l in source_logs if l['topics'][2][-40:]==S1[2:]);outgoing=sum(n(l['data']) for l in source_logs if l['topics'][1][-40:]==S1[2:])
 assert opening+incoming-outgoing==closing
 rec.append({'wallet':S1,'token':TOKEN,'decimals':18,'opening_block':127399999,'closing_block':127432896,'opening_raw':str(opening),'incoming_raw':str(incoming),'outgoing_raw':str(outgoing),'closing_raw':str(closing),'closing_amount':amt(closing),'residual_raw':'0'})
 # A had the exact later payment before the incident window, without observed intervening USDT flows.
 a_logs=[l for k,o in e.items() if k.startswith('A_baseline_') for l in o.get('response',{}).get('result',[])]
 assert a_logs==[]
 a_open=n(get('A_state_127199999'));a_before=n(get('A_state_127444207'));a_after=n(get('A_state_127444208'))
 a_payment=[r for r in b_events if r['token_sender']==A][0]
 assert a_open==a_before==int(a_payment['raw_amount']) and a_after==0
 rec.append({'wallet':A,'token':TOKEN,'decimals':18,'opening_block':127199999,'closing_block':127444208,'opening_raw':str(a_open),'incoming_raw':'0','outgoing_raw':a_payment['raw_amount'],'closing_raw':'0','closing_amount':amt(0),'residual_raw':'0'})
 before=[r for r in source_logs if n(r['blockNumber'])<127430000 and r['topics'][1][-40:]==S1[2:]]
 values=sorted(n(l['data']) for l in before)
 baseline={'S1_comparison_from_block':127400000,'S1_comparison_to_block':127429999,'outgoing_event_count':len(values),'distinct_recipients':len({l['topics'][2] for l in before}),'outgoing_sum':amt(sum(values)),'maximum_outgoing':amt(max(values)),'median_raw_times_two':str(values[len(values)//2]*2) if len(values)%2 else str(sum(values[len(values)//2-1:len(values)//2+1])),'pre_existing_activity_nonce_at_127199999':n(get('S1_nonce_127199999')),'limits':'Partial intraday canonical-event baseline, not lifetime history or a statistical anomaly score.'}
 result={'new_verified_transactions':sum(r['new_transaction'] for r in registry),'existing_bridge_transactions_imported':sum(not r['new_transaction'] for r in registry),'first_bridge_pre_balance':amt(n(get('B_state_127435561'))),'first_bridge_post_balance':amt(n(get('B_state_127435562'))),'total_B_incoming':amt(sum(int(r['raw_amount']) for r in b_events if r['token_recipient']==B)),'total_B_outgoing':amt(sum(int(r['raw_amount']) for r in b_events if r['token_sender']==B)),'earliest_B_incoming':next(r for r in b_events if r['token_recipient']==B),'verified_unauthorized_loss':None,'reconciliations':len(rec)}
 return {'upstream_funding_ledger':rows,'transaction_register':registry,'B_ordered_balance_walk':walk,'historical_balance_reconciliation':rec,'approval_register':approval,'source_behavior':baseline,'results':result}
if __name__=='__main__':
 for name,value in derive().items():(R/(name+'.json')).write_text(json.dumps(value,indent=2)+'\n')
 print(json.dumps(derive()['results'],indent=2))
