import concurrent.futures,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent/'robinhood_funding_direct_2026_10_09'));import collect as c
P=pathlib.Path(__file__).parent;A=P/'access';c.R=A;c.RPC='https://eth.drpc.org';U='0x427c4b37de0714821b09c4fc655a713abbcfba83'
ordinary=[]
for f in A.glob('routing_transactions*.response.txt'):ordinary+=json.loads(f.read_text())['items']
internal=json.loads((A/'routing_internal-transactions.response.txt').read_text())['items'];entries=[x for x in ordinary if x['to'] and x['to']['hash'].lower()==U and '2026-10-06T20:00'<x['timestamp']<'2026-10-07T02:19']
jobs=[]
for x in entries:
 h=x['hash'];jobs.extend([c.rpc(h+'_tx','eth_getTransactionByHash',[h]),c.rpc(h+'_receipt','eth_getTransactionReceipt',[h])])
for x in internal:
 if not ('2026-10-06T20:00'<x['timestamp']<'2026-10-07T02:19'):continue
 h=x['transaction_hash'];jobs.extend([c.rpc(h+'_tx','eth_getTransactionByHash',[h]),c.rpc(h+'_receipt','eth_getTransactionReceipt',[h]),c.rpc(h+'_trace','debug_traceTransaction',[h,{'tracer':'callTracer'}])])
jobs.extend([c.rpc('routing_case_start_code','eth_getCode',[U,hex(26136700)]),c.rpc('routing_case_end_code','eth_getCode',[U,hex(26137469)])])
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:list(e.map(c.collect,jobs))
