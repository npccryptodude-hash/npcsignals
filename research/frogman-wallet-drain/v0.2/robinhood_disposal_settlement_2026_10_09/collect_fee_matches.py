import concurrent.futures,json,pathlib,re,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
P=pathlib.Path(__file__).parent;A=P/'access';c.R=A;c.RPC='https://eth.drpc.org'
known=set(x.lower() for x in re.findall(r'0x[0-9a-fA-F]{40}(?![0-9a-fA-F])',(P.parent/'robinhood_disposal_2026_10_09/master_timeline_F0001_F0552.json').read_text()))
data=json.loads((A/'fee_source_case_history.response.txt').read_text())['result'];jobs=[]
for x in data:
 if x['to'] not in known or x['to']=='0xae06669dfd3e932476f00ea49fce82e5e63f83bf':continue
 h=x['hash'];bn=int(x['blockNumber']);jobs.extend([c.rpc(h+'_tx','eth_getTransactionByHash',[h]),c.rpc(h+'_receipt','eth_getTransactionReceipt',[h]),c.rpc('block_'+hex(bn),'eth_getBlockByNumber',[hex(bn),False])])
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(c.collect,jobs))
