#!/usr/bin/env python3
"""read-only evidence collector; preserves exact response bytes and request metadata."""
import urllib.request,urllib.error,json,re,datetime,hashlib,concurrent.futures
from pathlib import Path
P=Path(__file__).resolve().parent
RPC='https://arbitrum.gateway.tenderly.co'
HL='https://api.hyperliquid.xyz/info'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def call(name,url,payload):
 out=P/'raw';out.mkdir(exist_ok=True)
 start=now();req=urllib.request.Request(url,data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=35) as r:b=r.read();code=r.status
  (out/(name+'.json')).write_bytes(b)
  meta={'url':url,'request':payload,'started_utc':start,'retrieved_utc':now(),'http_status':code,'sha256':hashlib.sha256(b).hexdigest()}
  (out/(name+'.meta.json')).write_text(json.dumps(meta,indent=2)+'\n')
  return json.loads(b)
 except Exception as e:
  (out/(name+'.error.json')).write_text(json.dumps({'url':url,'request':payload,'started_utc':start,'finished_utc':now(),'error':str(e)},indent=2));raise

def rpc(name,method,params):
 d=call(name,RPC,{'jsonrpc':'2.0','id':1,'method':method,'params':params})
 if 'error' in d:raise ValueError(d['error'])
 return d['result']
def receipts():
 text=(P.parent/'PRIMARY_TRANSACTION_CHECKS_2026-11-12.md').read_text()
 matches=re.findall(r'\|\s*arbi-(\d+)\s*\|[^\n]*?https://arbiscan\.io/tx/(0x[a-fA-F0-9]{64})',text)
 mapping={int(i):h.lower() for i,h in matches}
 assert len(mapping)==len(set(mapping.values()))==35
 assert int(rpc('chain','eth_chainId',[]),16)==42161
 def one(item):
  i,h=item;n=f'arbi-{i:02}'
  try:
   r=rpc(n+'_receipt','eth_getTransactionReceipt',[h]);t=rpc(n+'_tx','eth_getTransactionByHash',[h]);b=rpc(n+'_block','eth_getBlockByNumber',[r['blockNumber'],False])
   ev=[l for l in r['logs'] if l['address'].lower()=='0xaf88d065e77c8cc2239327c5edb3a432268e5831' and len(l['topics'])==3 and l['topics'][0].lower()=='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef' and l['topics'][2][-40:].lower()=='2df1c51e09aecf9cacb7bc98cb1742757f163df7']
   assert int(r['status'],16)==1 and len(ev)==1
   e=ev[0]
   return {'id':n,'tx':h,'sender':'0x'+e['topics'][1][-40:].lower(),'tx_from':t['from'].lower(),'recipient':'0x'+e['topics'][2][-40:].lower(),'usdc_raw':str(int(e['data'],16)),'block':int(r['blockNumber'],16),'timestamp_utc':datetime.datetime.fromtimestamp(int(b['timestamp'],16),datetime.timezone.utc).isoformat(),'status':'confirmed'}
  except Exception as e:return {'id':n,'tx':h,'status':'unresolved','error':str(e)}
 rows=list(concurrent.futures.ThreadPoolExecutor(max_workers=4).map(one,sorted(mapping.items())))
 (P/'receipts.json').write_text(json.dumps(rows,indent=2)+'\n');print('receipts',len(rows),sum(x['status']=='confirmed' for x in rows),flush=True)

def account(row):
 if row['status']!='confirmed':return
 addr=row['sender'];n=row['id'];end=int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
 for typ in ['spotClearinghouseState','clearinghouseState','userFillsByTime','userNonFundingLedgerUpdates','openOrders']:
  q={'type':typ,'user':addr}
  if typ in ['userFillsByTime','userNonFundingLedgerUpdates']:q.update(startTime=0,endTime=end)
  try:
   d=call(n+'_'+typ,HL,q)
   if typ in ['userFillsByTime','userNonFundingLedgerUpdates']:
    assert isinstance(d,list)
    # conservatively flag 500+ records for pagination review, never silently truncate
    if len(d)>=500:print('PAGINATION REQUIRED',n,typ,len(d),flush=True)
  except Exception as e:print('error',n,typ,str(e),flush=True)
 print('account',n,'done',flush=True)
if __name__=='__main__':
 receipts()
 call('spotMeta',HL,{'type':'spotMeta'})
 list(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(account,json.loads((P/'receipts.json').read_text())))
