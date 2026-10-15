"""Bounded BNB Chain verification of Relay source transactions."""
import collect as c
c.URL='https://bsc-dataseed.binance.org'
def tx(h):
 r=c.rpc('eth_getTransactionReceipt',[h],'bnb_receipt_'+h)
 t=c.rpc('eth_getTransactionByHash',[h],'bnb_tx_'+h)
 b=c.rpc('eth_getBlockByNumber',[r['blockNumber'],False],'bnb_block_'+str(int(r['blockNumber'],16)))
 assert t['hash']==r['transactionHash']==h and b['hash']==r['blockHash']
 return r,t,b
if __name__=='__main__':
 print('chain',c.rpc('eth_chainId',[],'bnb_chain'),flush=True)
 for h in ['0xb4e697fc1cb8406ca6e18ee3a1b4f975428e2642caa57076df5d9b166848c1b1','0xcc827fd1fef937ac1942dd53a7f049061b827bf5292e1aa9a7e79610c00f200b']:
  r,t,b=tx(h);print(h,t['from'],len(r['logs']),flush=True)
 # Covers both deposits and approximately two hours before the first.
 for pos in [1,2]:
  topics=[c.T,None,None];topics[pos]='0x'+'0'*24+c.B[2:]
  a=[]
  for lo in range(127420000,127445001,5000):
   a+=c.rpc('eth_getLogs',[{'fromBlock':hex(lo),'toBlock':hex(min(lo+4999,127445000)),'topics':topics}],'bnb_B_'+str(lo)+'_'+str(pos))
  print('logs',pos,len(a),flush=True)
  for l in a:
   if len(l['topics'])==3:print(l['transactionHash'],int(l['blockNumber'],16),l['address'],l['topics'][1][-40:],l['topics'][2][-40:],int(l['data'],16),flush=True)
