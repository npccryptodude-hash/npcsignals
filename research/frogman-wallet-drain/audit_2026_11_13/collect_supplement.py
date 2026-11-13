import json,re,urllib.request,concurrent.futures,datetime,hashlib
from pathlib import Path
from collect import call,rpc,P

def get(name,url):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  with urllib.request.urlopen(url,timeout=20) as r:b=r.read();code=r.status
  (P/'raw'/f'{name}.json').write_bytes(b)
  (P/'raw'/f'{name}.meta.json').write_text(json.dumps({'url':url,'request':None,'started_utc':start,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'http_status':code,'sha256':hashlib.sha256(b).hexdigest()},indent=2)+'\n')
  return json.loads(b)
 except Exception as e:
  (P/'raw'/f'{name}.error.json').write_text(json.dumps({'url':url,'checked_utc':start,'error':str(e)},indent=2));return None
s=(P/'external.txt').read_text()
sigs=re.findall(r'<tr>.*?Mayan bridge.*?https://solscan.io/tx/([1-9A-HJ-NP-Za-km-z]+)',s)
(P/'mayan_source_inventory.json').write_text(json.dumps(sigs,indent=2)+'\n')
list(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(lambda x:get('mayan_external_'+str(x[0]+1),'https://explorer-api.mayan.finance/v3/swap/trx/'+x[1]),enumerate(sigs)))
print('mayan lookups',len(sigs),flush=True)
# bounded current source-wallet history, not a pool-wide attribution scan
for n,a in [('receiver','69FnU8vszZSZF6DZCT6VHdsvm3DvvojDgbwqzHJ4cCFS'),('near_recipient','JA3iQS6ZSv6L2jhnKR2XMCJThJVorvNydUmYDf6Bwhs6')]:
 try:call('solana_'+n+'_history','https://api.mainnet-beta.solana.com',{'jsonrpc':'2.0','id':1,'method':'getSignaturesForAddress','params':[a,{'limit':1000,'commitment':'finalized'}]})
 except Exception as e:print('solana',n,str(e),flush=True)
for n in [1894600,1894627]:get('chainflip_refresh_'+str(n),'https://chainflip-swap.chainflip.io/v2/swaps/'+str(n))
# endpoint roles / historical token units; validate fresh decimals
try:rpc('usdc_decimals','eth_call',[{'to':'0xaf88d065e77c8cc2239327c5edb3a432268e5831','data':'0x313ce567'},'latest'])
except Exception as e:print(e)
