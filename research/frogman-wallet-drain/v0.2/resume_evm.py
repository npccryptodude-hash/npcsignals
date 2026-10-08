import json,urllib.request,pathlib,datetime,concurrent.futures
P=pathlib.Path(__file__).parent/'raw_sources'
A=['0x14AA2A71dbb5eF87b81F92205E2699AA4aa65794','0x427C4b37de0714821B09C4FC655a713AbbCfbA83']
def get(label,url,payload=None):
 base=label;attempt=1
 while (P/(label+'.request.json')).exists() or (P/(label+'.response.json')).exists():
  attempt+=1;label=base+'_attempt'+str(attempt)
 rec={'url':url,'requested_at_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'POST' if payload else 'GET','request':payload}
 try:
  req=urllib.request.Request(url,data=json.dumps(payload).encode() if payload else None,headers={'Content-Type':'application/json','User-Agent':'NPCsignals research'})
  with urllib.request.urlopen(req,timeout=18) as r:b=r.read();rec['HTTP_status']=r.status
  (P/(label+'.response.json')).write_bytes(b);rec['response_file']=label+'.response.json'
  try:j=json.loads(b);print(label,str(j)[:350],flush=True)
  except:print(label,'bytes',len(b),flush=True)
 except Exception as e:rec['error']=str(e);print(label,str(e),flush=True)
 (P/(label+'.request.json')).write_text(json.dumps(rec,indent=2)+'\n')
jobs=[]
for i,a in enumerate(A):
 for v in ['v2','v3']:jobs.append((f'relay_{v}_{i}','https://api.relay.link/requests/'+v+'?user='+a+'&limit=50',None))
 for host,label in [('https://eth.blockscout.com','eth'),('https://explorer.robinhood.com','rh')]:jobs.append((f'{label}_transactions_{i}',host+'/api/v2/addresses/'+a+'/transactions',None))
 jobs.append((f'bscscan_transactions_{i}','https://bscscan.com/txs?a='+a,None))
jobs.append(('relay_requests_docs','https://docs.relay.link/references/api/get-requests-v2',None))
for host,label in [('https://ethereum-rpc.publicnode.com','eth_publicnode_retry'),('https://eth.drpc.org','eth_drpc_retry'),('https://rpc.flashbots.net','eth_flashbots'),('https://eth-mainnet.public.blastapi.io','eth_blast')]:jobs.append((label,host,{'jsonrpc':'2.0','id':1,'method':'eth_getTransactionCount','params':[A[1],'latest']}))
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(lambda j:get(*j),jobs))
