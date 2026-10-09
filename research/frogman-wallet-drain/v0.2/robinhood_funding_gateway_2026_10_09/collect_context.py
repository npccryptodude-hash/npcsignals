import concurrent.futures,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
P=pathlib.Path(__file__).parent;c.R=P/'access';A=c.R
jobs=[c.rpc('snapshot','eth_getBlockByNumber',['latest',False]),('executor_eth_metadata','https://eth.blockscout.com/api/v2/smart-contracts/0xa5166c3e69a933ee547ad908c9f1474f8f61901a',None)]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:list(e.map(c.collect,jobs))
b=json.loads((A/'snapshot.response.txt').read_text())['result']['number'];jobs=[]
for label,addr in [('prefunded','0x794dbdbdbfd3f8a3b887f4513bf5ff29edd04a94'),('gateway','0x998d7c178a1f9607b47ea3a8e22426451b3ce707'),('executor','0xa5166c3e69a933ee547ad908c9f1474f8f61901a')]:jobs.append(c.rpc(label+'_snapshot_code','eth_getCode',[addr,b]))
jobs.append(c.rpc('gateway_snapshot_implementation','eth_getStorageAt',['0x998d7c178a1f9607b47ea3a8e22426451b3ce707','0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc',b]))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(c.collect,jobs))
