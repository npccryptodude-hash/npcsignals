from resume_evm import get
import pathlib,json,concurrent.futures
P=pathlib.Path(__file__).parent/'raw_sources';records=[];jobs=[]
files=list(P.glob('relay_order_0x*.response.json'))+[P/'relay_order_sample.response.json']
for f in files:
 if not f.exists():continue
 for r in json.loads(f.read_text()).get('requests',[]):
  for t in r['data'].get('outTxs',[]):
   chain=t['chainId'];h=t['hash'];url={42161:'https://arb1.arbitrum.io/rpc',1:'https://ethereum-rpc.publicnode.com'}.get(chain)
   records.append({'request_id':r['id'],'source_record':f.name,'chain':chain,'hash':h,'recipient':r['recipient'],'amount':r['data'].get('price')})
   if not url:continue
   for m in ['eth_getTransactionByHash','eth_getTransactionReceipt']:jobs.append(('fill_'+str(chain)+'_'+m+'_'+h,url,{'jsonrpc':'2.0','id':1,'method':m,'params':[h]}))
   if t.get('block'):jobs.append(('fill_block_'+str(chain)+'_'+str(t['block']),url,{'jsonrpc':'2.0','id':1,'method':'eth_getBlockByNumber','params':[hex(t['block']),False]}))
   jobs.append(('fill_chain_'+str(chain),url,{'jsonrpc':'2.0','id':1,'method':'eth_chainId','params':[]}))
(P/'relay_fill_candidates.json').write_text(json.dumps(records,indent=2)+'\n');print('fills',records,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(lambda x:get(*x),jobs))
