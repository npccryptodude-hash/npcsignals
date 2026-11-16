from pathlib import Path
exec((Path(__file__).parent/'collect.py').read_text().split('end=int(')[0])
def rpc(n,m,p):return call(n,'https://mainnet.gateway.tenderly.co',{'jsonrpc':'2.0','id':1,'method':m,'params':p})
d=json.loads((P/'raw/eth_source_txlist.response').read_text())
for i,t in enumerate(d['result']):
 if int(t['blockNumber'])>26282041:
  rpc('replenishment_'+str(i)+'_tx','eth_getTransactionByHash',[t['hash']]);rpc('replenishment_'+str(i)+'_receipt','eth_getTransactionReceipt',[t['hash']]);rpc('replenishment_'+str(i)+'_block','eth_getBlockByNumber',[hex(int(t['blockNumber'])),False])
for label,b in [('before',26293496),('after',26293520)]:rpc('replenishment_'+label+'_balance','eth_getBalance',['0x4521ef4df51a7689d4db5d8fc598685cb226ff58',hex(b)])
a='G82K2R2RgJyBwfezs6ey2TXPzjR7oNEGr9WTMWinGTda'
d=call('sol_next_boundary_history','https://api.mainnet-beta.solana.com',{'jsonrpc':'2.0','id':1,'method':'getSignaturesForAddress','params':[a,{'limit':1000,'commitment':'finalized'}]})
call('sol_next_boundary_balance','https://api.mainnet-beta.solana.com',{'jsonrpc':'2.0','id':1,'method':'getBalance','params':[a,{'commitment':'finalized'}]})
if d and isinstance(d.get('result'),list):
 for i,t in enumerate(d['result'][:3]):call('sol_next_boundary_tx_'+str(i),'https://api.mainnet-beta.solana.com',{'jsonrpc':'2.0','id':1,'method':'getTransaction','params':[t['signature'],{'encoding':'jsonParsed','commitment':'finalized','maxSupportedTransactionVersion':0}]})
print('route verification collected',now(),flush=True)
