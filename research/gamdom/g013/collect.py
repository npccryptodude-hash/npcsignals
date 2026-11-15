"""Cached read-only G013 acquisition; frozen G012 is imported without mutation."""
import pathlib,json,gzip,urllib.request,urllib.error,datetime,sys,concurrent.futures,base64
R=pathlib.Path(__file__).resolve().parent;E=R/'evidence';E.mkdir(exist_ok=True)
BNB='https://bsc-mainnet.nodereal.io/v1/64a9df0874fb4a93b9d0a3849de012d3';ETH='https://mainnet.gateway.tenderly.co';NEAR='https://archival-rpc.mainnet.near.org'
def old():return json.loads(gzip.decompress((R.parent/'gamdom-incident-2026-10-g012/acquisition_archive.json.gz').read_bytes()))
def get(url,label,method=None,params=None):
 p=E/(label+'.json')
 if p.exists():return json.loads(p.read_text())
 o={'url':url,'requested_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()};data=None
 if method:o['request']={'jsonrpc':'2.0','id':1,'method':method,'params':params};data=json.dumps(o['request']).encode()
 try:
  with urllib.request.urlopen(urllib.request.Request(url,data=data,headers={'Content-Type':'application/json','User-Agent':'NPCsignals-evidence-research'}),timeout=25) as h:
   text=h.read().decode();o['http_status']=h.status;o['raw_response_text']=text
   try:o['response' if method else 'body']=json.loads(text)
   except ValueError:o['body_text']=text
 except urllib.error.HTTPError as ex:o.update(http_status=ex.code,error=str(ex),error_body=ex.read().decode(errors='replace'))
 except Exception as ex:o['error']=str(ex)
 p.write_text(json.dumps(o,indent=2)+'\n');return o
def run(jobs):
 with concurrent.futures.ThreadPoolExecutor(4) as pool:
  for x in pool.map(lambda j:get(*j),jobs):print(x['url'],x.get('http_status'),str(x.get('response',{}).get('error',x.get('error','saved')))[:100],flush=True)
if __name__=='__main__':
 mode=sys.argv[1];e=old()
 if mode=='trees':run([('https://api.github.com/repos/hot-dao/'+repo+'/git/trees/main?recursive=1','tree_'+repo) for repo in ['omni-sdk','omni-wallet-solidity','hot-validation-sdk','docs']])
 elif mode=='receipts':
  ids={q['id'] for k,v in e.items() if k.startswith('near_tx_') for q in v['response']['result']['receipts_outcome']}
  run([(NEAR,'receipt_'+rid,'EXPERIMENTAL_receipt',{'receipt_id':rid}) for rid in sorted(ids)])
 elif mode=='code':
  jobs=[]
  for k,v in e.items():
   if not k.startswith('near_tx_'):continue
   r=v['response']['result'];bh=r['transaction_outcome']['block_hash'];account=r['transaction']['receiver_id']
   for method in ['view_code','view_account']:jobs.append((NEAR,method+'_'+account+'_'+bh,'query',{'request_type':method,'block_id':bh,'account_id':account}))
   if account=='intents.near':
    account='eth-0x6b175474e89094c44da98b954eedeac495271d0f.omft.near'
    for method in ['view_code','view_account']:jobs.append((NEAR,method+'_'+account+'_'+bh,'query',{'request_type':method,'block_id':bh,'account_id':account}))
  for address,block,url in [('0x16ee1ef93df4657a52f8ea6eebe950b54bc91265',127436960,BNB),('0x66e6a2a0a9d871011b60b2e39902f10a33da4a2c',127437353,BNB),('0x2cff890f0378a11913b6129b2e97417a2c302680',26184851,ETH),('0x2cff890f0378a11913b6129b2e97417a2c302680',26184865,ETH)]:jobs.append((url,'evm_code_'+address+'_'+str(block),'eth_getCode',[address,hex(block)]))
  run(jobs)
