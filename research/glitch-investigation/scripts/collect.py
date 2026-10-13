#!/usr/bin/env python3
"""Re-fetch only checkpoint signatures into an explicitly chosen directory.
No market-wide collection, wallet fan-out, payment, signing or broadcasting.
"""
import argparse,json,urllib.request,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RPC='https://api.mainnet-beta.solana.com'
def rpc(method,params):
 req=urllib.request.Request(RPC,data=json.dumps(dict(jsonrpc='2.0',id=1,method=method,params=params)).encode(),headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(req,timeout=30) as r:d=json.load(r)
 if 'error' in d:raise RuntimeError(str(d['error']))
 return d['result']
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True,type=Path);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
 for f in sorted((ROOT/'raw/transactions').glob('*.json')):
  for attempt in range(4):
   try:
    d=rpc('getTransaction',[f.stem,{'encoding':'jsonParsed','commitment':'finalized','maxSupportedTransactionVersion':1}]);assert d is not None
    (a.output/f.name).write_text(json.dumps(d,indent=2));print(f.stem);break
   except Exception:
    if attempt==3:raise
    time.sleep(2**attempt)
  time.sleep(.3)
