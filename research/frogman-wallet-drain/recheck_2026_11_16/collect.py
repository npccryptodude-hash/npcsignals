#!/usr/bin/env python3
"""Read-only dated follow-up. Never overwrite the baseline."""
import json,datetime,urllib.request,hashlib,concurrent.futures
from pathlib import Path
P=Path(__file__).resolve().parent; B=P.parent/'audit_2026_11_13'; (P/'raw').mkdir(exist_ok=True)
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def call(n,u,q=None):
 start=now(); req=urllib.request.Request(u,data=json.dumps(q).encode() if q is not None else None,headers={'Content-Type':'application/json','User-Agent':'npcsignals-read-only-recheck'})
 meta={'url':u,'request':q,'started_utc':start}
 try:
  with urllib.request.urlopen(req,timeout=25) as r:b=r.read();meta.update(http_status=r.status,headers=dict(r.headers))
 except Exception as e:
  meta.update(error=str(e),finished_utc=now());(P/'raw'/f'{n}.error.json').write_text(json.dumps(meta,indent=2));return None
 (P/'raw'/f'{n}.response').write_bytes(b);meta.update(retrieved_utc=now(),sha256=hashlib.sha256(b).hexdigest());(P/'raw'/f'{n}.meta.json').write_text(json.dumps(meta,indent=2))
 try:return json.loads(b)
 except Exception:return None
end=int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
rows=json.loads((B/'accounts.json').read_text())
e=json.loads((B/'new_edges_summary.json').read_text())['additional_hyperliquid_account']
rows.append({'id':'additional-36','sender':e['account'],'current_xmr1':e['xmr1_net'],'history_end_utc':json.loads((B/'raw/new_relay_destination_userFillsByTime.meta.json').read_text())['request']['endTime'],'raw_prefix':'raw/new_relay_destination'})
assert len(rows)==len({r['sender'] for r in rows})==36
(P/'baseline_accounts.json').write_text(json.dumps(rows,indent=2))
(P/'run.json').write_text(json.dumps({'started_utc':now(),'history_end_ms':end,'baseline_commit':__import__('subprocess').check_output(['git','-C',str(P),'rev-parse','HEAD'],text=True).strip()},indent=2))
call('spotMeta','https://api.hyperliquid.xyz/info',{'type':'spotMeta'})
call('official_info_docs','https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint.md')
call('official_ledger_docs','https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals.md')
def one(r):
 n=r['id'];a=r['sender'];s=r['history_end_utc'];start=s if isinstance(s,int) else int(datetime.datetime.fromisoformat(s).timestamp()*1000)
 for typ in ['spotClearinghouseState','clearinghouseState','openOrders','userFillsByTime','userNonFundingLedgerUpdates']:
  q={'type':typ,'user':a}
  if typ in ['userFillsByTime','userNonFundingLedgerUpdates']:
   q.update(startTime=max(0,start-1000),endTime=end)
  call(n+'_'+typ,'https://api.hyperliquid.xyz/info',q)
 # Independent full returned history checks the overlap and last documented activity.
 for typ in ['userFillsByTime','userNonFundingLedgerUpdates']:
  call(n+'_full_'+typ,'https://api.hyperliquid.xyz/info',{'type':typ,'user':a,'startTime':0,'endTime':end})
 print(n,'collected',flush=True)
if __name__=='__main__':
 list(concurrent.futures.ThreadPoolExecutor(max_workers=5).map(one,rows))
 print('hyperliquid collection finished',now(),flush=True)
