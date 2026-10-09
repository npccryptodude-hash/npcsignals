import json,pathlib,hashlib
p=pathlib.Path(__file__).parent
old=json.loads((p.parent/'unlabeled_824a_verification_2026_10_09/master_timeline_F0001_F0490.json').read_text())['rows'];new=json.loads((p/'master_timeline_F0001_F0494.json').read_text())['rows']
assert new[:490]==old and sorted(r['ID'] for r in new)==[f'F{i:04}' for i in range(1,495)]
def r(n):return json.loads((p/'access'/(n+'.response.txt')).read_text())['result']
for l in ['inbound','outbound','onward']:
 t=r(l+'_tx');q=r(l+'_receipt');b=r(l+'_block');assert q['status']=='0x1' and t['hash']==q['transactionHash'] and t['blockHash']==b['hash'] and t['input']=='0x'
assert r('inbound_tx')['to']==r('outbound_tx')['from'] and r('outbound_tx')['to']==r('onward_tx')['from']
assert r('destination_code')=='0x' and r('collector_code')=='0x'
assert int(r('destination_inbound_pre_balance'),16)==0
assert int(r('collector_onward_pre_balance'),16)==int(r('collector_inbound_pre_balance'),16)+int(r('outbound_tx')['value'],16)
assert int(r('collector_onward_post_balance'),16)==int(r('collector_onward_pre_balance'),16)-int(r('onward_tx')['value'],16)-int(r('onward_receipt')['gasUsed'],16)*int(r('onward_receipt')['effectiveGasPrice'],16)
assert int(r('onward_tx')['value'],16)>int(r('outbound_tx')['value'],16)
for rel,h in json.loads((p/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((p/rel).read_bytes()).hexdigest()==h
print('PASS: prior 490 objects, exact transactions, pooled accounting, account types and evidence hashes')
