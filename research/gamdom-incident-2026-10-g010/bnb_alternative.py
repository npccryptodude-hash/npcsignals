import collect as c
c.URL='https://bsc-rpc.publicnode.com'
if __name__=='__main__':
 print(c.rpc('eth_chainId',[],'bnb_alt_chain'),flush=True)
 topics=[c.T,None,'0x'+'0'*24+c.B[2:]]
 r=c.rpc('eth_getLogs',[{'address':'0x55d398326f99059ff775485246999027b3197955','fromBlock':hex(127420000),'toBlock':hex(127435562),'topics':topics}],'bnb_alt_incoming')
 print('events',len(r),flush=True)
 for l in r:print(l['transactionHash'],int(l['blockNumber'],16),l['topics'][1][-40:],int(l['data'],16),flush=True)
