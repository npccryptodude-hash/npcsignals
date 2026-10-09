"""Read-only follow-up; explicit observation cutoff and immutable primary records."""
import concurrent.futures,datetime,json,pathlib,urllib.request
P=pathlib.Path(__file__).parent; R=P/'raw';R.mkdir(exist_ok=True)
users=[x['address'] for x in json.loads((P.parent/'continuation_2026_10_08/spot_execution_summary.json').read_bytes())['accounts']]
def get(label,url,payload=None):
    out=R/(label+'.response.json')
    if out.exists(): return
    rec={'url':url,'requested_at_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'POST' if payload else 'GET','request':payload}
    try:
        req=urllib.request.Request(url,data=json.dumps(payload).encode() if payload else None,headers={'Content-Type':'application/json','User-Agent':'NPCsignals research'})
        with urllib.request.urlopen(req,timeout=25) as response:
            body=response.read();rec['HTTP_status']=response.status
        out.write_bytes(body);rec['response_file']=out.name
        print(label,body[:120],flush=True)
    except Exception as e:rec['error']=str(e);print(label,e,flush=True)
    (R/(label+'.request.json')).write_text(json.dumps(rec,indent=2)+'\n')
if __name__=='__main__':
    cutoff=P/'query_cutoff.json'
    if not cutoff.exists():cutoff.write_text(json.dumps({'endTime_ms':int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)},indent=2)+'\n')
    end=json.loads(cutoff.read_bytes())['endTime_ms'];jobs=[]
    for user in users:
        for kind in ['userNonFundingLedgerUpdates','userFillsByTime','spotClearinghouseState','clearinghouseState']:
            payload={'type':kind,'user':user}
            if kind in ['userNonFundingLedgerUpdates','userFillsByTime']:payload.update({'startTime':1791317400000,'endTime':end})
            if kind=='userFillsByTime':payload['aggregateByTime']=False
            jobs.append((kind+'_'+user,'https://api.hyperliquid.xyz/info',payload))
    jobs.append(('wagyu_home','https://wagyu.xyz/',None))
    jobs.append(('hl_token_details','https://api.hyperliquid.xyz/info',{'type':'tokenDetails','tokenId':'0xbb2057659bd378d17e2e151bb04bdcaa'}))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:list(e.map(lambda x:get(*x),jobs))
