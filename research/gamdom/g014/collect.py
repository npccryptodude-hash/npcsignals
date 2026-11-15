"""Read-only bounded G014 repository/interface acquisition, exact HTTP bodies retained."""
import pathlib,json,urllib.request,urllib.error,datetime,concurrent.futures
R=pathlib.Path(__file__).resolve().parent;E=R/'evidence';E.mkdir(exist_ok=True)
def get(url,label,method=None,params=None):
 f=E/(label+'.json')
 if f.exists():return json.loads(f.read_text())
 o={'url':url,'requested_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()};data=None
 if method:o['request']={'jsonrpc':'2.0','id':1,'method':method,'params':params};data=json.dumps(o['request']).encode()
 try:
  with urllib.request.urlopen(urllib.request.Request(url,data=data,headers={'Content-Type':'application/json','User-Agent':'NPCsignals-G014-research'}),timeout=25) as h:
   s=h.read().decode();o['http_status']=h.status;o['raw_response_text']=s
   try:o['response' if method else 'body']=json.loads(s)
   except ValueError:pass
 except urllib.error.HTTPError as ex:o.update(http_status=ex.code,error=str(ex),error_body=ex.read().decode(errors='replace'))
 except Exception as ex:o['error']=str(ex)
 f.write_text(json.dumps(o,indent=2)+'\n');return o
def run(j):
 with concurrent.futures.ThreadPoolExecutor(3) as p:
  for o in p.map(lambda x:get(*x),j):print(o['url'],o.get('http_status'),o.get('error','saved'),flush=True)
if __name__=='__main__':
 run([('https://api.github.com/search/repositories?q=omft','repo_search_omft'),('https://api.github.com/repos/near/intents/git/trees/main?recursive=1','tree_near_intents'),('https://api.github.com/repos/defuse-protocol/defuse-sdk/commits?path=src/services/poaBridgeClient&until=2026-10-13T16:45:00Z&per_page=1','historical_poa_client_commit')])
