#!/usr/bin/env python3
"""Read-only balanceOf at fixed pre/post blocks. Outputs transport evidence, never invents balance."""
import concurrent.futures,datetime,json,urllib.request,urllib.error
TOKEN='0xc2132d05d31c914a87c6611c10748aeb04b58e8f'
D='e757683a51cfd002de479385c2f4c9db10a5e8d2'
URLS=['https://polygon-bor-rpc.publicnode.com','https://polygon.drpc.org','https://1rpc.io/matic','https://rpc.ankr.com/polygon','https://polygon.gateway.tenderly.co']
def run(pair):
 url,block=pair
 payload={'jsonrpc':'2.0','id':1,'method':'eth_call','params':[{'to':TOKEN,'data':'0x70a08231'+'0'*24+D},hex(block)]}
 record={'endpoint':url,'block':block,'request':payload,'requested_at_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(url,data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=12) as r:record.update(http_status=r.status,body=r.read().decode())
 except urllib.error.HTTPError as e:record.update(http_status=e.code,body=e.read().decode(errors='replace')[:2000])
 except Exception as e:record.update(error=type(e).__name__,detail=str(e))
 return record
if __name__=='__main__':
 pairs=[(u,b) for u in URLS for b in [95434112,95434113]]
 with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool: print(json.dumps(list(pool.map(run,pairs)),indent=2))
