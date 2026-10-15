"""Read-only BNB RPC collector; preserves successful and failed requests."""
import pathlib,json,urllib.request,datetime,sys,concurrent.futures
R=pathlib.Path(__file__).resolve().parent
E=R/'evidence';E.mkdir(exist_ok=True)
B='0xe5686aae44d392aa6a0637fd38393859502f8667'
TOKEN='0x55d398326f99059ff775485246999027b3197955'
TRANSFER='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
def rpc(url,m,p,label):
 f=E/(label+'.json')
 if f.exists():
  o=json.loads(f.read_text())
  if 'result' in o.get('response',{}):return o['response']['result']
  raise RuntimeError(str(o)[:300])
 request={'jsonrpc':'2.0','id':1,'method':m,'params':p};o={'endpoint':url,'requested_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'request':request}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,data=json.dumps(request).encode(),headers={'Content-Type':'application/json'}),timeout=20) as h:o['response']=json.load(h)
 except Exception as ex:o['error']=str(ex)
 f.write_text(json.dumps(o,indent=2)+'\n')
 if 'result' not in o.get('response',{}):raise RuntimeError(str(o)[:300])
 return o['response']['result']
def state(url,a,block,label):return rpc(url,'eth_call',[{'to':TOKEN,'data':'0x70a08231'+'0'*24+a[2:]},hex(block)],label)
def logs(url,a,lo,hi,label):
 out=[]
 for pos in [1,2]:
  topics=[TRANSFER,None,None];topics[pos]='0x'+'0'*24+a[2:]
  out+=rpc(url,'eth_getLogs',[{'address':TOKEN,'fromBlock':hex(lo),'toBlock':hex(hi),'topics':topics}],label+'_'+str(pos))
 return out
def tx(url,h,label=''):
 r=rpc(url,'eth_getTransactionReceipt',[h],label+'receipt_'+h)
 t=rpc(url,'eth_getTransactionByHash',[h],label+'tx_'+h)
 b=rpc(url,'eth_getBlockByNumber',[r['blockNumber'],False],label+'block_'+str(int(r['blockNumber'],16)))
 assert r['transactionHash']==t['hash']==h and r['blockHash']==t['blockHash']==b['hash']
 return r,t,b
def probe(url,n):
 try:
  print(n,'chain',rpc(url,'eth_chainId',[],n+'_chain'),flush=True)
  print(n,'balance',state(url,B,127435561,n+'_pre_balance'),flush=True)
  ls=logs(url,B,127430000,127435562,n+'_logs');print(n,'logs',len(ls),flush=True)
  for l in ls:print(n,l['transactionHash'],int(l['blockNumber'],16),l['topics'][1][-40:],l['topics'][2][-40:],int(l['data'],16),flush=True)
 except Exception as ex:print(n,str(ex),flush=True)
if __name__=='__main__':
 providers=[('https://bnb.gateway.tenderly.co','tenderly_bnb'),('https://bsc-dataseed.binance.org','binance'),('https://bsc.drpc.org','drpc'),('https://bsc-mainnet.nodereal.io/v1/1659dfb40aa24bbb8153a677b98064d7','nodereal_public')]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(lambda x:probe(*x),providers))
