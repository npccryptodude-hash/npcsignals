"""Read-only, cached Ethereum RPC evidence collection. No signed transactions."""
import json,pathlib,datetime,urllib.request,concurrent.futures
R=pathlib.Path(__file__).resolve().parent
E=R/'evidence'; E.mkdir(exist_ok=True)
URL='https://mainnet.gateway.tenderly.co'
T='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
B='0xe5686aae44d392aa6a0637fd38393859502f8667'
F='0xf70da97812cb96acdf810712aa562db8dfa3dbef'
def rpc(m,p,label):
 f=E/(label+'.json')
 if f.exists():
  o=json.loads(f.read_text())
  if 'result' in o.get('response',{}): return o['response']['result']
 req={'jsonrpc':'2.0','id':1,'method':m,'params':p}
 o={'endpoint':URL,'requested_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'request':req}
 try:
  with urllib.request.urlopen(urllib.request.Request(URL,data=json.dumps(req).encode(),headers={'Content-Type':'application/json'}),timeout=25) as h:
   o['response']=json.load(h)
 except Exception as ex:o['error']=str(ex)
 f.write_text(json.dumps(o,indent=2)+'\n')
 if 'result' not in o.get('response',{}):raise RuntimeError(str(o)[:400])
 return o['response']['result']
def logs(a,lo,hi,label):
 out=[]
 for pos in (1,2):
  topics=[T,None,None];topics[pos]='0x'+'0'*24+a[2:]
  out+=rpc('eth_getLogs',[{'fromBlock':hex(lo),'toBlock':hex(hi),'topics':topics}],label+'_'+str(pos))
 return out
def tx(h):
 r=rpc('eth_getTransactionReceipt',[h],'receipt_'+h)
 t=rpc('eth_getTransactionByHash',[h],'tx_'+h)
 b=rpc('eth_getBlockByNumber',[r['blockNumber'],False],'block_'+str(int(r['blockNumber'],16)))
 assert r['transactionHash']==t['hash']==h and r['blockHash']==b['hash']
 return r,t,b
if __name__=='__main__':
 import sys
 if sys.argv[1]=='initial':
  print('chain',rpc('eth_chainId',[],'chain'))
  r,t,b=tx('0x70a41ee50eb9277365900b8a23e8e30fe20ba4818b2db1a4e626b1fb11f92b14')
  print('source transfer input',t['input'],'sender',t['from'],'to',t['to'])
  for a,n in [(B,'B'),(F,'F')]:
   ls=logs(a,26184450,26185250,n+'_window')
   print(n,'logs',len(ls))
   for l in ls[:20]:
    if len(l['topics'])==3:print(l['transactionHash'],int(l['blockNumber'],16),l['address'],l['topics'][1][-40:],l['topics'][2][-40:],int(l['data'],16))
 elif sys.argv[1]=='logs':
  ls=logs(sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),sys.argv[5])
  print('count',len(ls))
  for l in ls[:50]:
   if len(l['topics'])==3:print(l['transactionHash'],int(l['blockNumber'],16),l['address'],l['topics'][1][-40:],l['topics'][2][-40:],int(l['data'],16))
 elif sys.argv[1]=='tx':
  for h in sys.argv[2:]:
   r,t,b=tx(h);print(h,t['from'],t['to'],t['input'][:80],int(b['timestamp'],16),'logs',len(r['logs']))
