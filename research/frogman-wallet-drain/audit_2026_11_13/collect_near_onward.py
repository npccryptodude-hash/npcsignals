import json
from collect import P,call
url='https://api.mainnet-beta.solana.com'
for n,a in [('near_44sol_recipient','4PMiFg7qoEpqAMwEyZnM7xPqvNotGc6ihboAvp8PcKbk'),('near_0473sol_recipient','7iGKnB9CSQLWsVX4V9Q9R61P3PFgJnLdyvPBvQutr5Gm')]:
 try:
  h=call(n+'_history',url,{'jsonrpc':'2.0','id':1,'method':'getSignaturesForAddress','params':[a,{'limit':1000,'commitment':'finalized'}]})
  call(n+'_balance',url,{'jsonrpc':'2.0','id':1,'method':'getBalance','params':[a,{'commitment':'finalized'}]})
  if len(h.get('result',[]))<=10:
   for i,t in enumerate(h['result']):call(n+'_tx_'+str(i),url,{'jsonrpc':'2.0','id':1,'method':'getTransaction','params':[t['signature'],{'encoding':'jsonParsed','commitment':'finalized','maxSupportedTransactionVersion':0}]})
 except Exception as e:print(n,str(e),flush=True)
