import json,concurrent.futures,datetime
from collect import P,call
u='https://mainnet.gateway.tenderly.co';a='0xbbae94f15c551920f45ad9a099e2a6b821822e3e'
def rpc(n,m,p):
 d=call(n,u,{'jsonrpc':'2.0','id':1,'method':m,'params':p})
 if 'error'in d:raise ValueError(d['error'])
 return d['result']
try:
 lo=26282040;hi=int(json.loads((P/'raw/ethereum_latest_block.json').read_text())['result']['number'],16)
 while hi-lo>1:
  points=sorted(set(lo+(hi-lo)*i//8 for i in range(1,8)))
  points=[x for x in points if lo<x<hi]
  if not points:break
  def probe(b):return b,int(rpc('eth_bbae_nonce_'+str(b),'eth_getTransactionCount',[a,hex(b)]),16)
  data=list(concurrent.futures.ThreadPoolExecutor(max_workers=4).map(probe,points))
  zeros=[b for b,n in data if n==0];ones=[b for b,n in data if n>0]
  if zeros:lo=max(zeros)
  if ones:hi=min(ones)
 b=rpc('eth_bbae_first_outgoing_block','eth_getBlockByNumber',[hex(hi),True]);tx=[x for x in b['transactions'] if x['from'].lower()==a]
 (P/'bbae_outgoing_candidates.json').write_text(json.dumps(tx,indent=2)+'\n')
 for i,t in enumerate(tx):rpc('eth_bbae_outgoing_receipt_'+str(i),'eth_getTransactionReceipt',[t['hash']])
 print('bbae outgoing',hi,len(tx),flush=True)
except Exception as e:(P/'bbae_lookup_limit.json').write_text(json.dumps({'error':str(e)},indent=2)+'\n');print(e)
# new relay destination records, kept outside the 35-account totals
u='https://arbitrum.gateway.tenderly.co';h='0x430a6d5eb90fcd7cda103bd502fd3b82953749b98317402e3a5945571b05f9eb'
for n,m,p in [('new_relay_arb_receipt','eth_getTransactionReceipt',[h]),('new_relay_arb_tx','eth_getTransactionByHash',[h]),('new_relay_arb_block','eth_getBlockByNumber',[hex(512429691),False])]:
 try:call(n,u,{'jsonrpc':'2.0','id':1,'method':m,'params':p})
 except Exception as e:print(e)
a='0xa8f219e59033fe2593151d951a142c1f958fd949';end=int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
for typ in ['spotClearinghouseState','userNonFundingLedgerUpdates','userFillsByTime']:
 q={'type':typ,'user':a}
 if typ!='spotClearinghouseState':q.update(startTime=0,endTime=end)
 try:call('new_relay_destination_'+typ,'https://api.hyperliquid.xyz/info',q)
 except Exception as e:print(e)
