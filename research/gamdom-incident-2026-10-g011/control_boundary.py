"""Locate B's intervening code transition by archive reads, without guessing a transaction."""
from collect import *
from extend import URL
def code(block):return rpc(URL,'eth_getCode',[B,hex(block)],'B_code_'+str(block))
if __name__=='__main__':
 lo,hi=127435561,127436946
 first,last=code(lo),code(hi);print('boundary codes',first,last,flush=True)
 if first!=last:
  # This finds a transition under the documented single-transition assumption;
  # the resulting full block and authorization are then independently examined.
  while hi-lo>1:
   mid=(lo+hi)//2
   if code(mid)==first:lo=mid
   else:hi=mid
  block=rpc(URL,'eth_getBlockByNumber',[hex(hi),True],'B_code_transition_full_block')
  print('transition candidates',hi,flush=True)
  for t in block['transactions']:
   if t['from']==B or (t['to'] or '').lower()==B:
    print(t['hash'],t['from'],t['to'],t['type'],flush=True)
    r,tt,b=tx(URL,t['hash']);print('receipt saved',tt.get('authorizationList'),flush=True)
