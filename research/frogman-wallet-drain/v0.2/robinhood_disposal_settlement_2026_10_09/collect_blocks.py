import concurrent.futures,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
P=pathlib.Path(__file__).parent;A=P/'access';c.R=A;c.RPC='https://eth.drpc.org';blocks=set()
for f in A.glob('0x*_tx.response.txt'):
 t=json.loads(f.read_text()).get('result')
 if t:blocks.add(t['blockNumber'])
jobs=[]
for bn in blocks:jobs.extend([c.rpc('block_'+bn,'eth_getBlockByNumber',[bn,False]),c.rpc('routing_code_'+bn,'eth_getCode',['0x427c4b37de0714821b09c4fc655a713abbcfba83',bn])])
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:list(e.map(c.collect,jobs))
