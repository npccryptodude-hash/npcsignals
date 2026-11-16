from pathlib import Path
exec((Path(__file__).parent/'collect.py').read_text().split('end=int(')[0])
u='https://mainnet.gateway.tenderly.co'
def rpc(n,m,p):return call(n,u,{'jsonrpc':'2.0','id':1,'method':m,'params':p})
b=rpc('eth_block','eth_getBlockByNumber',['latest',False]);tag=b['result']['number'] if b and 'result'in b else 'latest'
for name,a in [('source','0x4521ef4df51a7689d4db5d8fc598685cb226ff58'),('destination','0xbbae94f15c551920f45ad9a099e2a6b821822e3e')]:
 for m in ['eth_getBalance','eth_getTransactionCount']:
  rpc('eth_'+name+'_'+m,m,[a,tag])
 for action in ['txlist','txlistinternal']:
  call('eth_'+name+'_'+action,'https://eth.blockscout.com/api?module=account&action='+action+'&address='+a+'&startblock=26100000&endblock=99999999&page=1&offset=1000&sort=desc')
for name,a in [('oct27_destination','AKS15GjeivY1yBN3at6DNSg7q6UBmsPFtA2jWzvTniep'),('mixed_boundary','EfaGnkjvYEtN9yCbetyUyZmmabmBzgeGEc9LMod6pV3y')]:
 for method,params in [('getSignaturesForAddress',[a,{'limit':1000,'commitment':'finalized'}]),('getBalance',[a,{'commitment':'finalized'}])]:
  d=call('sol_'+name+'_'+method,'https://api.mainnet-beta.solana.com',{'jsonrpc':'2.0','id':1,'method':method,'params':params})
  if method=='getSignaturesForAddress' and d and isinstance(d.get('result'),list):
   for i,r in enumerate(d['result'][:3]):call('sol_'+name+'_tx_'+str(i),'https://api.mainnet-beta.solana.com',{'jsonrpc':'2.0','id':1,'method':'getTransaction','params':[r['signature'],{'encoding':'jsonParsed','commitment':'finalized','maxSupportedTransactionVersion':0}]})
call('mayan_oct27','https://explorer-api.mayan.finance/v3/swap/trx/0x38c7c72a6da978ee29e18649d5005d8978fbde862c0f78eb18fd70325e6939bf')
print('route collection finished',now(),flush=True)
