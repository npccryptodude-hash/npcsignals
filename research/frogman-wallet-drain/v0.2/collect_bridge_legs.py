from resume_evm import get
import json,pathlib,concurrent.futures
P=pathlib.Path(__file__).parent/'raw_sources';jobs=[];alltx=[]
for pat in ['eth_node_0x*.response.json','eth_second_*.response.json']:
 for f in P.glob(pat):
  node=f.name.split('eth_node_')[-1].split('eth_second_')[-1].split('.response')[0].lower()
  for t in json.loads(f.read_text()).get('items',[]):
   if t['from']['hash'].lower()==node and int(t['value'])>10**15:alltx.append(t)
for t in alltx:
 h=t['hash']
 for method in ['eth_getTransactionByHash','eth_getTransactionReceipt']:jobs.append((method+'_'+h,'https://ethereum-rpc.publicnode.com',{'jsonrpc':'2.0','id':1,'method':method,'params':[h]}))
 jobs.append(('eth_bridge_block_'+str(t['block_number']),'https://ethereum-rpc.publicnode.com',{'jsonrpc':'2.0','id':1,'method':'eth_getBlockByNumber','params':[hex(t['block_number']),False]}))
jobs.append(('lifi_relay_source','https://raw.githubusercontent.com/lifinance/contracts/main/src/Facets/RelayDepositoryFacet.sol',None))
jobs.append(('relay_bridge_sample','https://api.relay.link/requests/v2?hash=0xa7da5d044b2a34fd2105862dfed7b947254bd7ff12d7567e91be48d649f18d3c&limit=20',None))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:list(e.map(lambda x:get(*x),jobs))
