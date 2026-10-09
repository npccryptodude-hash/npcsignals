import concurrent.futures,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
P=pathlib.Path(__file__).parent;A=P/'access';c.R=A;c.RPC='https://eth.drpc.org'
rows=json.loads((P.parent/'robinhood_disposal_2026_10_09/master_timeline_F0001_F0552.json').read_text())['rows'];jobs=[]
for x in rows:
 if x.get('record_type')!='fund transfer' or x.get('asset')!='ETH' or not (152<=int(x['ID'][1:])<=180):continue
 h=x['tx/signature'];jobs.extend([c.rpc(h+'_tx','eth_getTransactionByHash',[h]),c.rpc(h+'_receipt','eth_getTransactionReceipt',[h])])
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:list(e.map(c.collect,jobs))
jobs=[]
for x in rows:
 if x.get('record_type')!='fund transfer' or x.get('asset')!='ETH' or not (152<=int(x['ID'][1:])<=180):continue
 h=x['tx/signature'];t=json.loads((A/(h+'_tx.response.txt')).read_text())['result'];bn=t['blockNumber'];jobs.extend([c.rpc('block_'+bn,'eth_getBlockByNumber',[bn,False]),c.rpc(h+'_sender_code','eth_getCode',[t['from'],bn]),c.rpc(h+'_recipient_code','eth_getCode',[t['to'],bn]),c.rpc(h+'_sender_pre_balance','eth_getBalance',[t['from'],hex(int(bn,16)-1)])])
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:list(e.map(c.collect,jobs))
