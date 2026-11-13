import json
from collect import P,call
u='https://mainnet.gateway.tenderly.co';a='0x4521ef4df51a7689d4db5d8fc598685cb226ff58'
def rpc(n,m,p):
 d=call(n,u,{'jsonrpc':'2.0','id':1,'method':m,'params':p})
 if 'error' in d:raise ValueError(d['error'])
 return d['result']
try:
 latest=json.loads((P/'raw/ethereum_latest_block.json').read_text())['result'];hi=int(latest['number'],16);lo=26100000
 n=int(rpc('eth_holding_nonce_low','eth_getTransactionCount',[a,hex(lo)]),16)
 if n!=0:raise ValueError('opening nonce is not zero')
 while hi-lo>1:
  mid=(hi+lo)//2;n=int(rpc('eth_holding_nonce_'+str(mid),'eth_getTransactionCount',[a,hex(mid)]),16)
  if n==0:lo=mid
  else:hi=mid
 b=rpc('eth_holding_first_outgoing_block','eth_getBlockByNumber',[hex(hi),True])
 matches=[t for t in b['transactions'] if t['from'].lower()==a]
 (P/'holding_outgoing_candidates.json').write_text(json.dumps(matches,indent=2)+'\n')
 for i,t in enumerate(matches):rpc('eth_holding_outgoing_receipt_'+str(i),'eth_getTransactionReceipt',[t['hash']])
 print('outgoing block',hi,'matches',len(matches),flush=True)
except Exception as e:
 (P/'eth_holding_status.json').write_text(json.dumps({'status':'unresolved historical lookup','error':str(e)},indent=2)+'\n');print(str(e),flush=True)
