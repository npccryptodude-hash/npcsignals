"""Read-only first-party ledger queries; no trading or account mutations."""
import concurrent.futures,csv,datetime,json,pathlib,urllib.request
P=pathlib.Path(__file__).parent; R=P/'raw'
def get(label,url,payload=None):
    target=R/(label+'.response.json')
    if target.exists(): return
    record={'url':url,'requested_at_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'POST' if payload else 'GET','request':payload}
    try:
        req=urllib.request.Request(url,data=json.dumps(payload).encode() if payload else None,headers={'Content-Type':'application/json','User-Agent':'NPCsignals research'})
        with urllib.request.urlopen(req,timeout=25) as response:
            body=response.read();record['HTTP_status']=response.status
        target.write_bytes(body);record['response_file']=target.name
        print(label,body[:220],flush=True)
    except Exception as e:record['error']=str(e);print(label,e,flush=True)
    (R/(label+'.request.json')).write_text(json.dumps(record,indent=2)+'\n')
if __name__=='__main__':
    rows=list(csv.DictReader((P.parent/'chain_extension_ledger_v0.2.csv').open()))
    users=[r['source'] for r in rows if r['ID'] in ['F0190','F0191','F0192','F0193','F0194','F0195']]
    jobs=[('hl_ledger_'+u,'https://api.hyperliquid.xyz/info',{'type':'userNonFundingLedgerUpdates','user':u,'startTime':1791317400000,'endTime':1791464400000}) for u in users]
    jobs += [('hl_fills_'+u,'https://api.hyperliquid.xyz/info',{'type':'userFillsByTime','user':u,'startTime':1791317400000,'endTime':1791464400000,'aggregateByTime':False}) for u in users]
    jobs += [('hl_spot_state_'+u,'https://api.hyperliquid.xyz/info',{'type':'spotClearinghouseState','user':u}) for u in users]
    jobs+=[('hl_bridge_docs','https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/bridge2',None),('hl_info_docs','https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals',None)]
    jobs += [('hl_spot_meta','https://api.hyperliquid.xyz/info',{'type':'spotMeta'})]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:list(e.map(lambda job:get(*job),jobs))
