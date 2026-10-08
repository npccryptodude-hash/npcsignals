from resume_evm import get,A
import json,pathlib,concurrent.futures
P=pathlib.Path(__file__).parent/'raw_sources';j=json.loads((P/'eth_internal-transactions_1.response.json').read_text());jobs=[]
for t in j['items']:
 if int(t['value'])<=10**15:continue
 h=t['transaction_hash']
 for method,params in [('eth_getTransactionByHash',[h]),('eth_getTransactionReceipt',[h]),('debug_traceTransaction',[h,{'tracer':'callTracer'}])]:jobs.append((method+'_'+h,'https://ethereum-rpc.publicnode.com',{'jsonrpc':'2.0','id':1,'method':method,'params':params}))
 b=t['block_number'];jobs.append(('eth_incoming_block_'+str(b),'https://ethereum-rpc.publicnode.com',{'jsonrpc':'2.0','id':1,'method':'eth_getBlockByNumber','params':[hex(b),False]}))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:list(e.map(lambda x:get(*x),jobs))
