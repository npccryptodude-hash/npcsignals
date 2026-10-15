#!/usr/bin/env python3
"""Read-only RPC collector; stores requests and responses without changing earlier checkpoints."""
import json,pathlib,datetime,urllib.request,urllib.error,sys,hashlib
ROOT=pathlib.Path(__file__).resolve().parent
ENDPOINT='https://polygon.gateway.tenderly.co'
TOKEN='0xc2132d05d31c914a87c6611c10748aeb04b58e8f'
D='0xe757683a51cfd002de479385c2f4c9db10a5e8d2'
TRANSFER='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
def rpc(method,params,label,endpoint=ENDPOINT):
 request={'jsonrpc':'2.0','id':1,'method':method,'params':params}
 out={'endpoint':endpoint,'requested_at_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'request':request}
 try:
  req=urllib.request.Request(endpoint,data=json.dumps(request).encode(),headers={'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=25) as r:out.update(http_status=r.status,response=json.loads(r.read()))
 except Exception as e:out.update(error=type(e).__name__,detail=str(e))
 (ROOT/'evidence'/f'{label}.json').write_text(json.dumps(out,indent=2)+'\n')
 if 'result' not in out.get('response',{}):raise RuntimeError(str(out)[:1000])
 return out['response']['result']
def logs(lo,hi,label):
 p={'address':TOKEN,'fromBlock':hex(lo),'toBlock':hex(hi),'topics':[TRANSFER,None,None]}
 topic='0x'+'0'*24+D[2:]
 arr=[]
 for pos in [1,2]:
  p['topics']=[TRANSFER,None,None];p['topics'][pos]=topic
  arr+=rpc('eth_getLogs',[p],label+f'_{pos}')
 return arr
if __name__=='__main__':
 print('chainId',rpc('eth_chainId',[],'chain_id'))
 block=rpc('eth_getBlockByNumber',[hex(95434113),False],'anchor_block')
 print('anchor',block['hash'],'timestamp',int(block['timestamp'],16),'txs',len(block['transactions']))
 arr=logs(95400000,95434113,'recent_logs_test')
 print('recentlogs',len(arr));print(json.dumps(arr,indent=2))
