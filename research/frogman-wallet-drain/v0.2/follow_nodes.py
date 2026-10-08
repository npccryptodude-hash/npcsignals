from resume_evm import get,A
import pathlib,json,concurrent.futures
P=pathlib.Path(__file__).parent/'raw_sources';ts=json.loads((P/'eth_history_combined.json').read_text())['items'];nodes=sorted({t['to']['hash'] for t in ts if t['from']['hash'].lower()==A[1].lower()});jobs=[]
for a in nodes:
 jobs.append(('eth_node_'+a,'https://eth.blockscout.com/api/v2/addresses/'+a+'/transactions',None))
 jobs.append(('eth_node_code_'+a,'https://ethereum-rpc.publicnode.com',{'jsonrpc':'2.0','id':1,'method':'eth_getCode','params':[a,'latest']}))
for i,a in enumerate(A):
 for kind in ['internal-transactions','token-transfers']:
  jobs.append(('eth_'+kind+'_'+str(i),'https://eth.blockscout.com/api/v2/addresses/'+a+'/'+kind,None))
# Verify initial ordinary incoming funding transaction as well.
h='0xb644bf8e644a1195ad838180fd015f88938a8664128b9e0ad1e7b4a5eebe2198'
for meth in ['eth_getTransactionByHash','eth_getTransactionReceipt']:jobs.append((meth+'_'+h,'https://ethereum-rpc.publicnode.com',{'jsonrpc':'2.0','id':1,'method':meth,'params':[h]}))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:list(e.map(lambda x:get(*x),jobs))
