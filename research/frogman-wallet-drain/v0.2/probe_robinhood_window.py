"""Locate the source incident window without assuming an explorer history."""
from resume_evm import get,A
import pathlib,json,concurrent.futures
P=pathlib.Path(__file__).parent/'raw_sources';U='https://rpc.mainnet.chain.robinhood.com'
latest=json.loads((P/'rh_latest.response.json').read_text())['result']
def find(target,label):
 lo=0;hi=int(latest['number'],16)
 for i in range(28):
  if lo>=hi:break
  mid=(lo+hi)//2;name=label+str(i)
  get(name,U,{'jsonrpc':'2.0','id':1,'method':'eth_getBlockByNumber','params':[hex(mid),False]})
  f=P/(name+'.response.json')
  if not f.exists():return None
  b=json.loads(f.read_text()).get('result')
  if not b:return None
  if int(b['timestamp'],16)<target:lo=mid+1
  else:hi=mid
 return lo
start=find(1791317400,'rh_start_');end=find(1791321000,'rh_end_')
print('window',start,end,flush=True)
if start is not None and end is not None:
 (P/'rh_window_blocks.json').write_text(json.dumps({'first_block_at_or_after_2026_10_06_2010UTC':start,'first_block_at_or_after_2026_10_06_2110UTC':end},indent=2)+'\n')
 jobs=[]
 for i,a in enumerate(A):
  for n,b in [('start',start),('end',end)]:jobs.append((f'rh_window_nonce_{i}_{n}',U,{'jsonrpc':'2.0','id':1,'method':'eth_getTransactionCount','params':[a,hex(b)]}))
  for offset in range(start,end,29999):
   jobs.append((f'rh_window_logs_{i}_{offset}',U,{'jsonrpc':'2.0','id':1,'method':'eth_getLogs','params':[{'fromBlock':hex(offset),'toBlock':hex(min(offset+29998,end-1)),'topics':['0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef','0x'+'0'*24+a[2:].lower()]}]}))
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(lambda j:get(*j),jobs))
