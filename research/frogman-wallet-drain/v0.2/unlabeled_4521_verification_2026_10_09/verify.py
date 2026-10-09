import json,pathlib,hashlib
p=pathlib.Path(__file__).parent
old=json.loads((p.parent/'unlabeled_2625_verification_2026_10_09/master_timeline_F0001_F0494.json').read_text())['rows'];new=json.loads((p/'master_timeline_F0001_F0497.json').read_text())['rows']
assert new[:494]==old and sorted(x['ID'] for x in new)==[f'F{i:04}' for i in range(1,498)]
def r(s):return json.loads((p/'access'/(s+'.response.txt')).read_text())['result']
t=r('inbound_tx');q=r('inbound_receipt');b=r('inbound_block');assert q['status']=='0x1' and t['hash']==q['transactionHash'] and t['blockHash']==b['hash'] and int(t['value'],16)==4*10**18
assert r('destination_code')==r('destination_snapshot_code')=='0x'
assert int(r('destination_snapshot_nonce'),16)==0 and int(r('destination_snapshot_balance'),16)==4*10**18
d=json.loads((p/'access/destination_transactions.response.txt').read_text());assert len(d['items'])==1 and d['next_page_params'] is None
for rel,h in json.loads((p/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((p/rel).read_bytes()).hexdigest()==h
print('PASS: prior 494 objects, case receipt, code, balance, nonce, bounded history and evidence hashes')
