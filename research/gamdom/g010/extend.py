"""Bounded collection for newly located E1 route and selected E2 provenance."""
from collect import *
import concurrent.futures
X='0x4b304741599c125a244e498d14562487d7109ab8'
A='0xd5fbda4c79f38920159fe5f22df9655fde292d47'
S1='0x0067cc2416f792cf0ec5629f5506324ac508f859'
S2='0x580450dff316ae00d0fbef9621a304020a046ce2'
TOK={'USDT':('0xdac17f958d2ee523a2206206994597c13d831ec7',6),'USDC':('0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',6),'DAI':('0x6b175474e89094c44da98b954eedeac495271d0f',18),'USDE':('0x8d0d000ee44948fc98c9b98a4fa4921476f08b0d',18)}
def safe(job):
 try:return job()
 except Exception as e:return str(e)
if __name__=='__main__':
 import sys
 mode=sys.argv[1]
 jobs=[]
 if mode=='state':
  for a,n in [(X,'E1'),(B,'B'),(A,'A'),(S1,'S1'),(S2,'S2')]:
   for block in [26184449,26184625,26185250]:
    for symbol,(token,d) in TOK.items():
     if n not in ['E1','B'] and symbol not in ['USDT','USDC','DAI']:continue
     jobs.append(lambda a=a,n=n,block=block,symbol=symbol,token=token: (n,block,symbol,rpc('eth_call',[{'to':token,'data':'0x70a08231'+'0'*24+a[2:]},hex(block)],f'state_{n}_{symbol}_{block}')))
    jobs.append(lambda a=a,n=n,block=block: (n,block,'nonce',rpc('eth_getTransactionCount',[a,hex(block)],f'nonce_{n}_{block}')))
  for block in [26184450,26185250]:jobs.append(lambda block=block:rpc('eth_getBlockByNumber',[hex(block),False],f'block_{block}'))
 elif mode=='baseline':
  for a,n in [(A,'A'),(S1,'S1'),(S2,'S2')]:jobs.append(lambda a=a,n=n:(n,len(logs(a,26177200,26184449,n+'_baseline'))))
  jobs.append(lambda:('E1_prior',len(logs(X,26100000,26184449,'E1_prior'))))
 elif mode=='traces':
  for h in ['0x70a41ee50eb9277365900b8a23e8e30fe20ba4818b2db1a4e626b1fb11f92b14','0xf110d179d86cd74ee3b7e6bda3fa1724258274571d66c1909a05fcbc899d66a1']:
   jobs.append(lambda h=h:rpc('debug_traceTransaction',[h,{'tracer':'callTracer'}],'trace_'+h))
 elif mode=='E2source':
  a='0x2cff890f0378a11913b6129b2e97417a2c302680'
  jobs.append(lambda:('E2source',len(logs(a,26184450,26185250,'E2source_window'))))
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
  for r in ex.map(safe,jobs):print(str(r)[:200],flush=True)
