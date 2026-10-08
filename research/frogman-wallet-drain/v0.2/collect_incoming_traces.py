from resume_evm import get
import pathlib,json,concurrent.futures
P=pathlib.Path(__file__).parent/'raw_sources';jobs=[]
for t in json.loads((P/'eth_internal-transactions_1.response.json').read_text())['items']:
 h=t['transaction_hash'];jobs.append(('trace_transaction_'+h,'https://eth.drpc.org',{'jsonrpc':'2.0','id':1,'method':'trace_transaction','params':[h]}))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(lambda x:get(*x),jobs))
