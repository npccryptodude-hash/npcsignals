import json,pathlib,urllib.request,concurrent.futures,time
P=pathlib.Path(__file__).parent;T=P/'raw_transactions';T.mkdir(exist_ok=True)
sigs=set()
for f in (P/'access').glob('*.json'):
 for x in json.loads(f.read_text()).get('result',[]):
  if x.get('blockTime') and 1791316000<x['blockTime']<1791324000:sigs.add(x['signature'])
def fetch(s):
 f=T/(s+'.json')
 if f.exists():return
 d={'jsonrpc':'2.0','id':1,'method':'getTransaction','params':[s,{'encoding':'jsonParsed','commitment':'finalized','maxSupportedTransactionVersion':0}]}
 for attempt in range(3):
  try:
   r=urllib.request.urlopen(urllib.request.Request('https://api.mainnet-beta.solana.com',data=json.dumps(d).encode(),headers={'Content-Type':'application/json'}),timeout=15);b=r.read();j=json.loads(b)
   if j.get('result'):f.write_bytes(b);return
   print('unavailable',s,str(j)[:100]);return
  except Exception as e:
   if attempt==2:print('failed',s,str(e));return
   time.sleep(1)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(fetch,sorted(sigs)))
print('saved',len(list(T.glob('*.json'))),'requested',len(sigs))
