import json,datetime,concurrent.futures
from collect import P,call
end=int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
start=int(datetime.datetime(2026,10,13,tzinfo=datetime.timezone.utc).timestamp()*1000)
def one(r):
 for typ in ['userFillsByTime','userNonFundingLedgerUpdates']:
  try:call(r['id']+'_post_13_oct_'+typ,'https://api.hyperliquid.xyz/info',{'type':typ,'user':r['sender'],'startTime':start,'endTime':end})
  except Exception as e:print(r['id'],str(e),flush=True)
list(concurrent.futures.ThreadPoolExecutor(max_workers=5).map(one,json.loads((P/'receipts.json').read_text())))
for label in ['receiver','near_recipient']:
 h=json.loads((P/'raw'/('solana_'+label+'_history.json')).read_text())['result']
 if h:
  sig=h[0]['signature']
  try:call('solana_'+label+'_latest_tx','https://api.mainnet-beta.solana.com',{'jsonrpc':'2.0','id':1,'method':'getTransaction','params':[sig,{'encoding':'jsonParsed','commitment':'finalized','maxSupportedTransactionVersion':0}]})
  except Exception as e:print(e)
print('current followups complete',flush=True)
