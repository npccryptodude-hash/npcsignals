import concurrent.futures,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
P=pathlib.Path(__file__).parent;c.R=P/'access';c.RPC='https://eth.drpc.org';A=c.R
jobs=[]
for tag,h in [('router','0xefa46658dead085751916c1368ed2590d72fa34dce36abf5c6b5a8cbcfc0d624'),('supplement','0x48ccd6181b3c6357ba9f29ffd238c20fc129f09b5a5cc1330dbb07ea23c864a6')]:jobs.extend([c.rpc(tag+'_tx','eth_getTransactionByHash',[h]),c.rpc(tag+'_receipt','eth_getTransactionReceipt',[h])])
jobs.append(('router_metadata','https://eth.blockscout.com/api/v2/smart-contracts/0x1231deb6f5749ef6ce6943a275a1d3e7486f4eae',None))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:list(e.map(c.collect,jobs))
jobs=[]
for tag in ['router','supplement']:
 t=json.loads((A/(tag+'_tx.response.txt')).read_text())['result'];jobs.append(c.rpc(tag+'_block','eth_getBlockByNumber',[t['blockNumber'],False]))
 if tag=='router':jobs.extend([c.rpc('router_case_code','eth_getCode',[t['to'],t['blockNumber']]),c.rpc('onward_recipient_pre_router_balance','eth_getBalance',[t['from'],hex(int(t['blockNumber'],16)-1)])])
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(c.collect,jobs))
