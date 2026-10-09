"""Read-only HTTP/RPC evidence collector; error responses are not absent activity."""
import concurrent.futures,datetime,json,pathlib,urllib.request,urllib.error
P=pathlib.Path(__file__).parent; R=P/'access'; R.mkdir(exist_ok=True)
RPC='https://rpc.mainnet.chain.robinhood.com'
def collect(job):
    label,url,payload=job; f=R/(label+'.json')
    if f.exists(): return
    rec={'url':url,'requested_at_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'POST' if payload else 'GET','request':payload}
    try:
        request=urllib.request.Request(url,data=json.dumps(payload).encode() if payload else None,headers={'Content-Type':'application/json','User-Agent':'NPCsignals public transaction research'})
        with urllib.request.urlopen(request,timeout=22) as response: rec['HTTP_status']=response.status; body=response.read()
        (R/(label+'.response.txt')).write_bytes(body); rec['response_file']=label+'.response.txt'
    except Exception as e: rec['error']=str(e); rec['HTTP_status']=getattr(e,'code',None)
    f.write_text(json.dumps(rec,indent=2)+'\n'); print(label,rec.get('HTTP_status'),rec.get('error','saved'),flush=True)
def rpc(label,method,params):return (label,RPC,{'jsonrpc':'2.0','id':1,'method':method,'params':params})
if __name__=='__main__':
    jobs=[]
    for f in sorted(R.glob('*.json')):
        rec=json.loads(f.read_text());jobs.append((f.stem,rec['url'],rec.get('request')))
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as e:list(e.map(collect,jobs))
