import hashlib,json,pathlib
P=pathlib.Path(__file__).parent
old=json.loads((P.parent/'inbound_sender_attribution_2026_10_10/master_timeline_F0001_F0602.json').read_text())['rows'];new=json.loads((P/'master_timeline_F0001_F0603.json').read_text())['rows'];assert new[:602]==old and sorted(x['ID'] for x in new)==[f'F{i:04}' for i in range(1,604)]
s=json.loads((P/'withdrawal_recheck_scope.json').read_text());m=json.loads((P/'access/hyperliquid_new_ledger.json').read_text());assert s['startTime']==1791624537691 and s['endTime']>s['startTime']
assert json.loads((P/'access/hyperliquid_new_ledger.response.txt').read_text())==[]
assert m['HTTP_status']==200 and m['url']=='https://api.hyperliquid.xyz/info' and m['request']=={'type':'userNonFundingLedgerUpdates','user':s['user'],'startTime':s['startTime'],'endTime':s['endTime']}
# Exact request preserved in the collector access manifest.
assert s['user']=='0x3e2d81f7a5659e4760ba929ef88eed40ef6640a1'
for n,h in json.loads((P/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((P/n).read_bytes()).hexdigest()==h
print('PASS: 602 prior records preserved; F0603 only appended; dated empty ledger response; checksums')
