import json,pathlib,hashlib
p=pathlib.Path(__file__).parent
old=json.loads((p.parent/'near_intents_verification_2026_10_09/master_timeline_F0001_F0486.json').read_text())['rows']
new=json.loads((p/'master_timeline_F0001_F0490.json').read_text())['rows']
assert new[:486]==old and sorted(r['ID'] for r in new)==[f'F{i:04}' for i in range(1,491)]
a=p/'access'
def r(n):return json.loads((a/(n+'.response.txt')).read_text())['result']
for tx,receipt,block in [('inbound_eth_getTransactionByHash','inbound_eth_getTransactionReceipt','inbound_eth_getBlockByNumber'),('outbound_eth_getTransactionByHash','outbound_eth_getTransactionReceipt','outbound_eth_getBlockByNumber'),('onward_tx','onward_receipt','onward_block')]:
 t=r(tx);s=r(receipt);b=r(block);assert s['status']=='0x1' and t['hash']==s['transactionHash'] and t['blockHash']==b['hash']
assert r('outbound_eth_getTransactionByHash')['to']==r('onward_tx')['from']
assert int(r('collector_onward_pre_balance'),16)==int(r('outbound_eth_getTransactionByHash')['value'],16)
assert int(r('collector_onward_post_balance'),16)==int(r('collector_onward_pre_balance'),16)-int(r('onward_tx')['value'],16)-int(r('onward_receipt')['gasUsed'],16)*int(r('onward_receipt')['effectiveGasPrice'],16)
for x in ['destination','collector','boundary']:assert r(x+'_onward_code')=='0x'
assert int(r('boundary_onward_pre_balance'),16)>0
for rel,h in json.loads((p/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((p/rel).read_bytes()).hexdigest()==h
print('PASS: 486 prior objects unchanged; transactions, continuity, accounting, account types and raw evidence hashes verified')
