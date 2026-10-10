"""Read-only collection scoped to one previously matched account; captured bytes retained."""
import concurrent.futures,datetime,json,pathlib,time,urllib.request
P=pathlib.Path(__file__).parent; A=P/'access'; A.mkdir(exist_ok=True)
USER='0x3e2d81f7a5659e4760ba929ef88eed40ef6640a1'
END=int(time.time()*1000); START=1791244800000

def get(label,url,payload=None):
    rec={'url':url,'method':'POST' if payload else 'GET','request':payload,'requested_at_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        req=urllib.request.Request(url,data=json.dumps(payload).encode() if payload else None,headers={'Content-Type':'application/json','User-Agent':'NPCsignals read-only research'})
        with urllib.request.urlopen(req,timeout=25) as r: data=r.read();rec['HTTP_status']=r.status
        (A/(label+'.response.txt')).write_bytes(data);rec['response_file']=label+'.response.txt'
    except Exception as e: rec['error']=str(e);rec['HTTP_status']=getattr(e,'code',None)
    rec['completed_at_UTC']=datetime.datetime.now(datetime.timezone.utc).isoformat();(A/(label+'.json')).write_text(json.dumps(rec,indent=2)+'\n')
    print(label,rec.get('HTTP_status'),rec.get('error','saved'),flush=True)
    if 'error' not in rec:
        try:return json.loads(data)
        except:return None

def query(label,payload):return get(label,'https://api.hyperliquid.xyz/info',payload)
if __name__=='__main__':
    (P/'scope.json').write_text(json.dumps({'account':USER,'startTime':START,'endTime':END,'max_pages':5,'scope':'single matched account; no lifetime completeness claim'},indent=2)+'\n')
    jobs=[('spot_state',{'type':'spotClearinghouseState','user':USER}),('perp_state',{'type':'clearinghouseState','user':USER}),('spot_meta',{'type':'spotMeta'}),('funding',{'type':'userFunding','user':USER,'startTime':START,'endTime':END})]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(lambda x:query(*x),jobs))
    for typ,label in [('userNonFundingLedgerUpdates','ledger'),('userFillsByTime','fills')]:
        start=START
        for page in range(5):
            payload={'type':typ,'user':USER,'startTime':start,'endTime':END}
            if typ=='userFillsByTime':payload['aggregateByTime']=False
            rows=query(label+'_'+str(page),payload)
            if not isinstance(rows,list) or not rows:break
            latest=max(x['time'] for x in rows)
            if latest<start:break
            start=latest+1
            # fetch a subsequent page even for a short first response
    get('info_docs','https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint.md')
