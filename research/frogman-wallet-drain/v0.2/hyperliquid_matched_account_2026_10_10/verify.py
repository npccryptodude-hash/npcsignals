import decimal,hashlib,json,pathlib
P=pathlib.Path(__file__).parent;A=P/'access';D=decimal.Decimal
USER='0x3e2d81f7a5659e4760ba929ef88eed40ef6640a1';H='0x963c56253dedcfd5ff9f944c91eb9cb9e94d12701d9165f66a40b9aa0b4cfc1f'
def raw(n):return json.loads((A/(n+'.response.txt')).read_text())
def r(n):return raw(n)['result']
old=json.loads((P.parent/'robinhood_disposal_settlement_2026_10_09/master_timeline_F0001_F0585.json').read_text())['rows'];new=json.loads((P/'master_timeline_F0001_F0593.json').read_text())['rows'];assert new[:585]==old and sorted(x['ID'] for x in new)==[f'F{i:04}' for i in range(1,594)]
t,q,b=r('deposit_tx'),r('deposit_receipt'),r('deposit_block');assert r('arb_chain')=='0xa4b1';assert t['hash']==q['transactionHash']==H and q['status']=='0x1' and t['blockHash']==q['blockHash']==b['hash'] and t['blockNumber']==q['blockNumber']==b['number'] and H in b['transactions'] and t['from']==USER
logs=[x for x in q['logs'] if x['address']=='0xaf88d065e77c8cc2239327c5edb3a432268e5831' and x['topics'][1][-40:]==USER[2:] and x['topics'][2][-40:]=='2df1c51e09aecf9cacb7bc98cb1742757f163df7'];assert len(logs)==1 and int(logs[0]['data'],16)==26823206875
l=raw('ledger_0');assert len(l)==2 and l[0]['hash']==H and D(l[0]['delta']['usdc'])*10**6==26823206875 and l[1]['delta']=={'type':'accountClassTransfer','usdc':'26823.2','toPerp':False};assert raw('ledger_1')==[] and raw('fills_1')==[]
f=raw('fills_0');assert len(f)==28 and len({x['tid'] for x in f})==28 and len({x['oid'] for x in f})==3 and all(x['coin']=='@260' and x['side']=='B' and x['feeToken']=='XMR1' for x in f)
net=D(0);cost=D(0)
for x in f:
 assert D(x['startPosition'])==net;net+=D(x['sz'])-D(x['fee']);cost+=D(x['sz'])*D(x['px'])
s=raw('spot_state')['balances'];assert next(D(x['total']) for x in s if x['coin']=='XMR1')==net==D('47.146974');assert next(D(x['total']) for x in s if x['coin']=='USDC')==D('26823.2')-cost==D('5.8332');assert cost==D('26817.3668')
p=raw('perp_state');assert p['assetPositions']==[] and D(p['marginSummary']['totalRawUsd'])==D('26823.206875')-D('26823.2')==D('0.006875') and raw('funding')==[]
m=raw('spot_meta');market=next(x for x in m['universe'] if x['index']==260);assert market['tokens']==[404,0];assert next(x['name'] for x in m['tokens'] if x['index']==404)=='XMR1';assert next(x['name'] for x in m['tokens'] if x['index']==0)=='USDC'
scope=json.loads((P/'scope.json').read_text());assert scope['account']==USER and all(scope['startTime']<=x['time']<=scope['endTime'] for x in l+f)
for x in new[585:]:
 for n in x['evidence_files']:assert (P/n).exists()
for n,h in json.loads((P/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((P/n).read_bytes()).hexdigest()==h
print('PASS: prior 585 objects unchanged; deposit receipt/block/account credit; 28 distinct fills/three orders; position chain and exact spot arithmetic; dated residual/state; no returned external ledger event in scope; checksums')
