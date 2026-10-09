"""Read-only origin reproduction attempts. Access failures are not absent transactions."""
import concurrent.futures, datetime, json, pathlib, urllib.request, urllib.error
P=pathlib.Path(__file__).parent; R=P/'access'; R.mkdir(exist_ok=True)
H='0x2310d627c3c369a73b480bd1bb6bdcffd26615ba84ce02a0f36858722890d366'
def collect(job):
    label,url,payload=job
    out=R/(label+'.json')
    if out.exists(): return
    rec={'url':url,'requested_at_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'POST' if payload else 'GET','request':payload}
    try:
        request=urllib.request.Request(url,data=json.dumps(payload).encode() if payload else None,headers={'Content-Type':'application/json','User-Agent':'NPCsignals public transaction research'})
        with urllib.request.urlopen(request,timeout=20) as response:
            rec['HTTP_status']=response.status; body=response.read()
        (R/(label+'.response.txt')).write_bytes(body)
        rec['response_file']=label+'.response.txt'
    except urllib.error.HTTPError as e:
        rec['HTTP_status']=e.code;rec['error']=str(e)
        rec['limitation']='Access rejected; no transaction or chain conclusion follows.'
    except Exception as e:rec['error']=str(e)
    out.write_text(json.dumps(rec,indent=2)+'\n')
    print(label,rec.get('HTTP_status'),rec.get('error','response saved'),flush=True)
if __name__=='__main__':
    jobs=[('candidate_history','https://explorer.robinhood.com/api/v2/addresses/0x427c4b37de0714821b09c4fc655a713abbcfba83/transactions',None),('candidate_logs','https://explorer.robinhood.com/api/v2/addresses/0x427c4b37de0714821b09c4fc655a713abbcfba83/logs',None),('chain_id','https://rpc.mainnet.chain.robinhood.com',{'jsonrpc':'2.0','id':1,'method':'eth_chainId','params':[]})]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:list(e.map(collect,jobs))
