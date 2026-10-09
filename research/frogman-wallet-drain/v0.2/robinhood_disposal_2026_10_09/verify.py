import hashlib,json,pathlib
from build import calls
P=pathlib.Path(__file__).parent;B=P.parent
def raw(n):return json.loads((P/'access'/(n+'.response.txt')).read_text())
def r(n):return raw(n)['result']
old=json.loads((B/'robinhood_funding_gateway_2026_10_09/master_timeline_F0001_F0538.json').read_text())['rows'];new=json.loads((P/'master_timeline_F0001_F0552.json').read_text())['rows'];assert new[:538]==old and sorted(x['ID'] for x in new)==[f'F{i:04}' for i in range(1,553)]
assert r('eth_chain_id')=='0x1'
oldedges=json.loads((B/'robinhood_linkage_2026_10_09/cross_chain_edges.json').read_text())
for e in oldedges:
 tag=e['origin_record_ID'];t=r(tag+'_fill_tx');q=r(tag+'_fill_receipt');b=r(tag+'_fill_block');assert t['hash']==e['destination_transaction']==q['transactionHash'] and q['status']=='0x1' and t['blockHash']==q['blockHash']==b['hash'] and t['hash'] in b['transactions'] and int(t['blockNumber'],16)==e['destination_block']
for e in json.loads((P/'disposal_edges.json').read_text())[:7]:
 cs=list(calls(r(e['existing_origin_ID']+'_callback_trace')));assert e['native_credit_call'] in cs and e['native_unwrap_call'] in cs and not any(x.get('error') for x in cs);assert int(e['native_credit_call']['value'],16)==int(e['amount_wei']) and e['fill_event'] in r(e['existing_origin_ID']+'_fill_receipt')['logs']
for tag in ['terminal','onward','supplement','router']:
 t=r(tag+'_tx');q=r(tag+'_receipt');b=r(tag+'_block');assert t['hash']==q['transactionHash'] and q['status']=='0x1' and t['blockHash']==q['blockHash']==b['hash'] and t['hash'] in b['transactions']
assert r('terminal_case_code')==r('onward_case_code')=='0x'
assert int(r('forwarder_pre_incoming_balance'),16)==0 and int(r('onward_recipient_pre_balance'),16)==0
assert int(r('forwarder_pre_onward_balance'),16)==int(r('terminal_tx')['value'],16) and int(r('onward_tx')['nonce'],16)==0
assert r('onward_tx')['from']==r('terminal_tx')['to'] and r('onward_tx')['to']==r('supplement_tx')['to']==r('router_tx')['from']
assert int(r('onward_recipient_pre_router_balance'),16)==int(r('onward_tx')['value'],16)+int(r('supplement_tx')['value'],16)
assert int(r('onward_tx')['value'],16)==int(r('router_tx')['value'],16)==10251000000000000000
assert int(r('routing_wallet_pre_first_fill_balance'),16)>0
assert raw('router_metadata')['is_verified'] and raw('router_metadata')['name']=='LiFiDiamond' and len(r('router_case_code'))>2
status=raw('router_lifi_status');assert status['sending']['txHash']==r('router_tx')['hash'] and status['sending']['amount']==str(int(r('router_tx')['value'],16)) and status['transactionId'][2:] in r('router_receipt')['logs'][-1]['data']
assert new[-2]['classification']=='SUPPORTED' and new[-1]['classification']=='UNRESOLVED' and not new[-1]['beneficiary_attribution_advanced']
for x in new[538:]:
 for f in x.get('evidence_files',[]):assert (P/f).exists(),f
for rel,h in json.loads((P/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((P/rel).read_bytes()).hexdigest()==h
print('PASS: old 538 objects; 15 fresh fill receipts/blocks; seven native callback traces; four disposal/funding transactions; historical balances and service boundary; destination API lead stays SUPPORTED')
