"""Read-only public ownership/statement acquisition; no account interaction."""
import pathlib,json,urllib.request,urllib.error,datetime,concurrent.futures
R=pathlib.Path(__file__).resolve().parent;E=R/'evidence';E.mkdir(exist_ok=True)
def get(url,label):
 f=E/(label+'.json')
 if f.exists():return json.loads(f.read_text())
 o={'url':url,'requested_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'NPCsignals-public-evidence-research'}),timeout=25) as h:
   s=h.read().decode();o.update(http_status=h.status,raw_response_text=s)
   try:o['body']=json.loads(s)
   except ValueError:pass
 except urllib.error.HTTPError as ex:o.update(http_status=ex.code,error=str(ex),error_body=ex.read().decode(errors='replace'))
 except Exception as ex:o['error']=str(ex)
 f.write_text(json.dumps(o,indent=2)+'\n');return o
def run(jobs):
 with concurrent.futures.ThreadPoolExecutor(3) as p:
  for o in p.map(lambda j:get(*j),jobs):print(o['url'],o.get('http_status'),o.get('error','saved'),flush=True)
if __name__=='__main__':
 run([('https://help.gamdom.com/en/articles/8818767-how-to-deposit','official_deposit_help'),('https://help.gamdom.com/en/articles/7997071-someone-contacted-me-on-3rd-party-social-media-sites-posing-as-gamdom-staff-what-should-i-do','official_deposit_channels'),('https://help.gamdom.com/en/articles/9593458-pending-withdrawals-and-problems-that-coin-mixing-can-cause','official_withdrawal_help'),('https://x.com/gamdom/status/2110213246410227730','official_incident_statement'),('https://x.com/Romer/status/2110411281350230457','founder_incident_statement'),('https://x.com/vxdb/status/2110500301056979368','external_loss_estimate')])
