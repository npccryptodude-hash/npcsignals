from resume_evm import get,A
import pathlib,json,concurrent.futures
P=pathlib.Path(__file__).parent/'raw_sources';targets=set();jobs=[]
for f in P.glob('eth_node_0x*.response.json'):
 node=f.name.split('eth_node_')[1].split('.response')[0].lower()
 for t in json.loads(f.read_text()).get('items',[]):
  if t['from']['hash'].lower()==node and int(t['value'])>10**15:targets.add(t['to']['hash'])
for a in targets:jobs.append(('eth_second_'+a,'https://eth.blockscout.com/api/v2/addresses/'+a+'/transactions?filter=from',None))
# One rate-limited lookup, not a batch retry.
jobs.append(('relay_request_sample','https://api.relay.link/requests/v2?hash=0x05aa98a030faf4e61ef1794b5adacb1ea5c35e499c26bb07cd1fc4fc776037e7&limit=20',None))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(lambda x:get(*x),jobs))
