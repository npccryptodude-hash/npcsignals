from resume_evm import get
import pathlib,json,concurrent.futures
P=pathlib.Path(__file__).parent/'raw_sources';jobs=[];seen=set();blocks=set();tokens=set()
for chain,pat,U in [('rh','rh_window_logs_*.response.json','https://rpc.mainnet.chain.robinhood.com'),('arb','arb_USDC_logs_*.response.json','https://arb1.arbitrum.io/rpc')]:
 for f in P.glob(pat):
  for l in json.loads(f.read_text()).get('result',[]):
   h=l['transactionHash'];b=l['blockNumber'];tokens.add((chain,l['address'],U));blocks.add((chain,b,U))
   if (chain,h) in seen:continue
   seen.add((chain,h))
   for m in ['eth_getTransactionByHash','eth_getTransactionReceipt']:jobs.append((chain+'_'+m+'_'+h,U,{'jsonrpc':'2.0','id':1,'method':m,'params':[h]}))
for chain,b,U in blocks:jobs.append((chain+'_block_'+str(int(b,16)),U,{'jsonrpc':'2.0','id':1,'method':'eth_getBlockByNumber','params':[b,False]}))
for chain,t,U in tokens:
 for name,data in [('decimals','0x313ce567'),('symbol','0x95d89b41'),('name','0x06fdde03')]:jobs.append((chain+'_token_'+t+'_'+name,U,{'jsonrpc':'2.0','id':1,'method':'eth_call','params':[{'to':t,'data':data},'latest']}))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(lambda j:get(*j),jobs))
