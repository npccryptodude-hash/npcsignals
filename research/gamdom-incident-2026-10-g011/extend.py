from collect import *
# Public, shareable endpoint published in NodeReal's API overview.
URL='https://bsc-mainnet.nodereal.io/v1/64a9df0874fb4a93b9d0a3849de012d3'
S1='0x0067cc2416f792cf0ec5629f5506324ac508f859'
if __name__=='__main__':
 mode=sys.argv[1]
 if mode=='B':
  print('chain',rpc(URL,'eth_chainId',[],'nr_bsc_chain'),flush=True)
  arr=logs(URL,B,127400000,127444806,'B_extended')
  print('events',len(arr),flush=True)
  for l in arr:print(l['transactionHash'],int(l['blockNumber'],16),l['topics'][1][-40:],l['topics'][2][-40:],int(l['data'],16),flush=True)
  for block in [127399999,127430000,127435561,127435562,127444805,127444806]:
   print('state',block,state(URL,B,block,'B_state_'+str(block)),flush=True)
   print('nonce',block,rpc(URL,'eth_getTransactionCount',[B,hex(block)],'B_nonce_'+str(block)),flush=True)
 elif mode=='receipts':
  e=json.loads((E/'B_extended_2.json').read_text())['response']['result']
  for h in sorted({l['transactionHash'] for l in e}):
   r,t,b=tx(URL,h);print(h,t['from'],int(b['timestamp'],16),r['status'],flush=True)
 elif mode=='S1':
  a=[]
  for lo in range(127200000,127432896,50000):a+=logs(URL,S1,lo,min(lo+49999,127432895),'S1_baseline_'+str(lo))
  print('S1 baseline events',len(a),flush=True)
  for block in [127200000,127399999,127432895,127444806]:
   print('S1',block,state(URL,S1,block,'S1_state_'+str(block)),flush=True)
  for block in [127200000,127400000,127430000,127444806]:
   b=rpc(URL,'eth_getBlockByNumber',[hex(block),False],'block_'+str(block));print('block',block,int(b['timestamp'],16),flush=True)
 elif mode=='checks':
  for block in [127399999,127435561,127435562,127444805,127444806]:
   print(block,state('https://bsc.nodereal.io',B,block,'public_alias_state_'+str(block)),flush=True)
 elif mode=='outgoing':
  arr=json.loads((E/'B_extended_1.json').read_text())['response']['result']
  old={'0xb4e697fc1cb8406ca6e18ee3a1b4f975428e2642caa57076df5d9b166848c1b1','0xcc827fd1fef937ac1942dd53a7f049061b827bf5292e1aa9a7e79610c00f200b'}
  for h in sorted({l['transactionHash'] for l in arr}-old):
   r,t,b=tx(URL,h);print(h,t['from'],t['to'],len(r['logs']),flush=True)
 elif mode=='A':
  a='0xd5fbda4c79f38920159fe5f22df9655fde292d47'
  for lo in range(127200000,127444208,50000):
   ls=logs(URL,a,lo,min(lo+49999,127444207),'A_baseline_'+str(lo));print('A logs',lo,len(ls),flush=True)
  for block in [127199999,127399999,127444207,127444208]:print('A',block,state(URL,a,block,'A_state_'+str(block)),flush=True)
 elif mode=='S1_short':
  for lo in [127400000,127410000,127420000]:
   ls=logs(URL,S1,lo,lo+9999,'S1_short_'+str(lo));print('S1 logs',lo,len(ls),flush=True)
  for block in [127199999,127399999,127432895,127444806]:
   print('S1',block,state(URL,S1,block,'S1_state_'+str(block)),flush=True)
   print('nonce',block,rpc(URL,'eth_getTransactionCount',[S1,hex(block)],'S1_nonce_'+str(block)),flush=True)
  for block in [127200000,127400000,127420000,127430000,127444806]:
   b=rpc(URL,'eth_getBlockByNumber',[hex(block),False],'block_'+str(block));print('header',block,int(b['timestamp'],16),flush=True)
 elif mode=='upstream':
  a=logs(URL,S1,127430000,127432896,'S1_finish');print('finish events',len(a),flush=True)
  for block in [127429999,127432896]:print('S1',block,state(URL,S1,block,'S1_state_'+str(block)),flush=True)
  # One large recent inbound and one earlier outgoing chosen from returned logs.
  incoming=[];outgoing=[]
  for name in ['S1_short_127400000','S1_short_127410000','S1_short_127420000','S1_finish']:
   incoming+=json.loads((E/(name+'_2.json')).read_text())['response']['result']
   outgoing+=json.loads((E/(name+'_1.json')).read_text())['response']['result']
  chosen=[max(incoming,key=lambda l:int(l['data'],16)),min(outgoing,key=lambda l:(int(l['blockNumber'],16),int(l['logIndex'],16)))]
  for l in chosen:
   r,t,b=tx(URL,l['transactionHash']);print('selected upstream',t['hash'],t['from'],int(b['timestamp'],16),flush=True)
  for sig,n in [('0x313ce567','decimals'),('0x95d89b41','symbol')]:print(n,rpc(URL,'eth_call',[{'to':TOKEN,'data':sig},hex(127435561)],'token_'+n),flush=True)
