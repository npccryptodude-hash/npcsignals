import decimal,hashlib,json,pathlib,sys
P=pathlib.Path(__file__).parent;B=P.parent;A=P/'access';sys.path.insert(0,str(B/'mayan_verification_2026_10_09'));from keccak_utils import keccak
def raw(n):return json.loads((A/(n+'.response.txt')).read_text())
def r(n):return raw(n)['result']
def inclusion(t,q,b):
 assert t['hash']==q['transactionHash'] and q['status']=='0x1' and t['blockHash']==q['blockHash']==b['hash'] and t['blockNumber']==q['blockNumber']==b['number'] and t['hash'] in b['transactions']
def calls(t):
 yield t
 for x in t.get('calls',[]):yield from calls(x)
old=json.loads((B/'robinhood_disposal_2026_10_09/master_timeline_F0001_F0552.json').read_text())['rows'];new=json.loads((P/'master_timeline_F0001_F0585.json').read_text())['rows'];assert new[:552]==old and sorted(x['ID'] for x in new)==[f'F{i:04}' for i in range(1,586)]
pool=json.loads((P/'pool_accounting.json').read_text());s=pool['summary'];assert int(s['native_inflow_wei'])-int(s['native_principal_out_wei'])-int(s['wallet_paid_gas_wei'])==int(s['end_balance_wei']) and s['residual_wei']=='0' and s['native_outflow_count']==15
bal=int(r('routing_pre_initial_balance'),16);assert bal==0
lo={'seven':0,'rh15':0};hi={'seven':0,'rh15':0};bounds={};block_before={};block_after={}
for e in pool['chronological_events']:
 bn=e['block_number'];block_before.setdefault(bn,bal);assert bal==int(e['balance_before_wei'])
 if e['kind']=='in':
  bal+=e['amount']
  for group in lo:
   if e[group]:lo[group]+=e['amount'];hi[group]+=e['amount']
 else:
  bounds[e['tx']]={g:{'minimum_group_principal_wei':str(max(0,lo[g]-bal+e['amount'])),'maximum_group_principal_wei':str(min(e['amount'],hi[g])),'minimum_group_balance_before_wei':str(lo[g]),'maximum_group_balance_before_wei':str(hi[g])} for g in lo};bal-=e['amount']+e['fee']
  for group in lo:lo[group]=max(0,lo[group]-e['amount']-e['fee']);hi[group]=min(hi[group],bal)
 assert bal==int(e['balance_after_wei']);block_after[bn]=bal
assert bounds==pool['outflow_group_bounds'] and bal==int(s['end_balance_wei']);assert not any(int(b['seven']['minimum_group_principal_wei']) for b in bounds.values());assert sum(int(b['rh15']['minimum_group_principal_wei'])>0 for b in bounds.values())==2
for x in s['inbound_edges']:
 h=x['transaction_hash'];t=r(h+'_tx');q=r(h+'_receipt');b=r('block_'+t['blockNumber']);inclusion(t,q,b)
 if x['record_type']=='ordinary credit':assert t['to']==x['destination_wallet'] and t['from']==x['source_wallet'] and int(t['value'],16)==int(x['amount_wei'])
 else:
  cs=list(calls(r(h+'_trace')));assert x['matched_call'] in cs and not any(v.get('error') for v in cs) and int(x['matched_call']['value'],16)==int(x['amount_wei'])
outrows=[x for x in new[552:] if x['record_type'].startswith('Routing-wallet outflow')];assert [x['sender_nonce'] for x in outrows]==list(range(15))
for x in outrows:
 h=x['transaction_hash'];t=r(h+'_tx');q=r(h+'_receipt');b=r('block_'+t['blockNumber']);inclusion(t,q,b);bn=int(t['blockNumber'],16);assert int(r(h+'_pre_balance'),16)==block_before[bn] and int(r(h+'_post_balance'),16)==block_after[bn] and t['input']=='0x' and int(t['value'],16)==int(x['amount_wei'])
for f in A.glob('routing_code_*.response.txt'):assert json.loads(f.read_text())['result']=='0x'
hops=json.loads((P/'legacy_native_hop_reproductions.json').read_text());assert len(hops)==29
for x in hops:
 h=x['transaction_hash'];t=r(h+'_tx');q=r(h+'_receipt');b=r('block_'+t['blockNumber']);inclusion(t,q,b);o=next(z for z in old if z['ID']==x['existing_ID']);assert t['from']==o['source'].lower() and t['to']==o['destination'].lower() and decimal.Decimal(o['amount'])*10**18==int(t['value'],16)
funds=json.loads((P/'funding_edges.json').read_text());assert len(funds)==10 and len({x['destination_wallet'] for x in funds})==10
for x in funds:
 h=x['transaction_hash'];t=r(h+'_tx');q=r(h+'_receipt');b=r('block_'+t['blockNumber']);inclusion(t,q,b);assert t['from']=='0xae06669dfd3e932476f00ea49fce82e5e63f83bf' and t['input']=='0x' and int(t['value'],16)==int(x['amount_wei'])
assert r('arb_chain')=='0xa4b1'
for tag in ['destination','credit']:inclusion(r(tag+'_tx'),r(tag+'_receipt'),r(tag+'_block'))
route=next(x for x in new[552:] if x['record_type'].startswith('Previously confirmed LI.FI'))
legacy=next(x for x in old if x['ID']=='F0479');assert route['source_transaction']==legacy['source_transaction'] and route['destination_transaction']==legacy['destination_transaction'] and route['order_hash']==legacy['order_hash']
assert route['destination_order_event'] in r('destination_receipt')['logs'] and route['destination_transfer_event'] in r('destination_receipt')['logs'] and route['destination_order_event']['topics'][0]=='0x'+keccak(b'OrderFulfilled(bytes32,uint64,uint256)')
assert r('destination_code')=='0x' and int(r('destination_pre_balance'),16)==0 and int(r('destination_post_balance'),16)==26823206875
credit=next(x for x in new[552:] if x['record_type'].startswith('New exact USDC'))
assert credit['transfer_event'] in r('credit_receipt')['logs'] and credit['Hyperliquid_deposit_record'] in raw('hyperliquid_credit') and credit['Hyperliquid_deposit_record']['hash']==credit['transaction_hash'] and decimal.Decimal(credit['Hyperliquid_deposit_record']['delta']['usdc'])*10**6==int(credit['transfer_event']['data'],16)
positive=[x for x in r('destination_outgoing_USDC_logs') if int(x['data'],16)>0];assert len(positive)==1 and positive[0]['transactionHash']==credit['transaction_hash'];assert len(r('destination_incoming_USDC_logs'))==1
for x in new[552:]:
 for f in x.get('evidence_files',[]):assert (P/f).exists(),f
for rel,h in json.loads((P/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((P/rel).read_bytes()).hexdigest()==h
print('PASS: prior 552 objects; exact scoped pool reconciliation; 15 outflows/nonce sequence; 29 onward native hops; ten funding-source edges; prior Mayan order/settlement; exact Hyperliquid hash+credit; no individual seven-fill allocation')
