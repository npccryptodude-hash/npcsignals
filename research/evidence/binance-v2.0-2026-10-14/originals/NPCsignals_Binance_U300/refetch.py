import json,pathlib,urllib.request,datetime,time
P=pathlib.Path(__file__).resolve().parent
S=[
'4m6gaPuwQnwN7KFSeCi3SzaqJzyj6JPzL5sMjq2c3gYuniYAqg3kZMPsseDdomzVJaVjZF3LPXYyHXAqeKKfSuYb',
'T7To7CBLjCmV16JL3vTyuTvgze5kuuRvXjdoP6AgmQiRu8urjsPGpJm3nsxypA9cipPD8UjmyMqeDBEvjAK55zk',
'4tKWJNnFjwr7J7JsVY8dMAAS1u2KfYpvQDHf9aHcbHpeP7pMCBMZ5xeQPRMFhgxMsnbdFMiKQfseKxz796t195zh',
'3hYxbjuVEGz6pvfRXW3smZyfeTv67TUrUHWfAL4PsN5h5ia9gvBb1accAEDuvNHANnTheZPkqL6FU7BqKe7XTtNh',
'3VFwG45pKTaYCHMfqMQD426UkjWGMwooyMzWSwGjrFAqCHU4FReF8ZVSiUxeDsUiifV3zsUbh39AMHdf8DAJ9jtg',
'4oAiLXHcNk6sVYZJuQHPiKY3dWeoNstuKKABC2UZ1JmJKFQCfhdjCD84QNxRUvLuzhSLo57bYFCrieuw8uBnmeQp',
'29d75Pa2Pu33b7r3dQam1FyKQTAP1e1YzwpejkkhxCHYwneJSFwJW1AGgnrgcC5hu2TfU5U7D6b1ppJvC5nwuqrB']
def call(method,params):
 reqbody={'jsonrpc':'2.0','id':1,'method':method,'params':params}
 for attempt in range(3):
  try:
   req=urllib.request.Request('https://api.mainnet-beta.solana.com',data=json.dumps(reqbody).encode(),headers={'Content-Type':'application/json'})
   with urllib.request.urlopen(req,timeout=25) as f:raw=f.read()
   d=json.loads(raw)
   if d.get('error'):raise RuntimeError(str(d['error']))
   return raw,d,reqbody
  except Exception:
   if attempt==2:raise
   time.sleep(2**attempt)
for s in S:
 raw,d,req=call('getTransaction',[s,{'encoding':'jsonParsed','commitment':'finalized','maxSupportedTransactionVersion':1}]);assert d.get('result') is not None
 (P/(s+'.rpc.json')).write_bytes(raw);(P/(s+'.json')).write_text(json.dumps(d['result'],indent=2))
 (P/(s+'.request.json')).write_text(json.dumps({'request':req,'retrieved_utc_host_clock':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2))
 print(s,d['result']['slot'],d['result']['meta']['err'],flush=True)
raw,d,req=call('getSignatureStatuses',[S,{'searchTransactionHistory':True}]);(P/'finality.rpc.json').write_bytes(raw)
(P/'finality.json').write_text(json.dumps(dict(zip(S,d['result']['value'])),indent=2));(P/'finality.request.json').write_text(json.dumps(req,indent=2))
