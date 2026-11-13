import json,concurrent.futures
from collect import P,call
url='https://api.mainnet-beta.solana.com'
h=json.loads((P/'raw/solana_near_recipient_history.json').read_text())['result']
def one(x):
 i,r=x
 try:call('solana_near_history_tx_'+str(i),url,{'jsonrpc':'2.0','id':1,'method':'getTransaction','params':[r['signature'],{'encoding':'jsonParsed','commitment':'finalized','maxSupportedTransactionVersion':0}]})
 except Exception as e:print(e)
list(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(one,enumerate(h)))
for n,a in [('receiver','69FnU8vszZSZF6DZCT6VHdsvm3DvvojDgbwqzHJ4cCFS'),('near_recipient','JA3iQS6ZSv6L2jhnKR2XMCJThJVorvNydUmYDf6Bwhs6')]:
 try:call('solana_'+n+'_balance',url,{'jsonrpc':'2.0','id':1,'method':'getBalance','params':[a,{'commitment':'finalized'}]})
 except Exception as e:print(e)
url='https://ethereum.publicnode.com'
for n,method,params in [('eth_chain','eth_chainId',[]),('eth_4eth_balance','eth_getBalance',['0x4521ef4df51a7689d4db5d8fc598685cb226ff58','latest']),('eth_4eth_nonce','eth_getTransactionCount',['0x4521ef4df51a7689d4db5d8fc598685cb226ff58','latest'])]:
 try:call(n,url,{'jsonrpc':'2.0','id':1,'method':method,'params':params})
 except Exception as e:print(e)
