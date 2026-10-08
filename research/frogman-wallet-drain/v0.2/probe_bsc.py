import json,urllib.request,pathlib,datetime
P=pathlib.Path(__file__).parent/'raw_sources';U='https://bsc-dataseed.binance.org';N=0
def rpc(method,params,label):
 global N
 N+=1;d={'jsonrpc':'2.0','id':N,'method':method,'params':params};rec={'url':U,'request':d,'requested_at_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  b=urllib.request.urlopen(urllib.request.Request(U,data=json.dumps(d).encode(),headers={'Content-Type':'application/json'}),timeout=10).read();(P/(label+'.response.json')).write_bytes(b);j=json.loads(b);rec['response_file']=label+'.response.json';res=j.get('result');
 except Exception as e:rec['error']=str(e);res=None
 (P/(label+'.request.json')).write_text(json.dumps(rec,indent=2)+'\n');return res
for a in ['0x14AA2A71dbb5eF87b81F92205E2699AA4aa65794','0x427C4b37de0714821B09C4FC655a713AbbCfbA83']:
 print(a,'nonce',rpc('eth_getTransactionCount',[a,'latest'],'bsc_nonce_'+a),'balance',rpc('eth_getBalance',[a,'latest'],'bsc_balance_'+a))
latest=rpc('eth_getBlockByNumber',['latest',False],'bsc_latest')
if not latest:raise SystemExit('Latest block unavailable; no block-range or history claim made.')
print('latest',latest.get('number'),latest.get('timestamp'))
if not latest.get('number') or not latest.get('timestamp'):raise SystemExit('Malformed block response')
# Binary search first block at/after incident-window endpoints.
def find(target,label):
 lo=0;hi=int(latest['number'],16)
 for i in range(28):
  if lo>=hi:break
  mid=(lo+hi)//2;b=rpc('eth_getBlockByNumber',[hex(mid),False],label+str(i))
  if not b or not b.get('timestamp'):return None
  if int(b['timestamp'],16)<target:lo=mid+1
  else:hi=mid
 return lo
start=find(1791316800,'bsc_start_');end=find(1791345600,'bsc_end_');print('range',start,end)
if start is not None and end is not None:
 topic='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
 for a in ['0x14AA2A71dbb5eF87b81F92205E2699AA4aa65794','0x427C4b37de0714821B09C4FC655a713AbbCfbA83']:
  filt={'fromBlock':hex(start),'toBlock':hex(end),'topics':[topic,'0x'+'0'*24+a[2:].lower()]};logs=rpc('eth_getLogs',[filt],'bsc_token_outflows_'+a);print('logs',a,str(logs)[:600])
