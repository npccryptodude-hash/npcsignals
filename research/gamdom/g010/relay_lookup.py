"""Read-only Relay index discovery. Index associations require chain corroboration."""
from collect import *
def get(url,label):
 o={'url':url,'requested_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url,timeout=20) as r:o['body']=r.read().decode();o['http_status']=r.status
 except Exception as e:o['error']=str(e)
 (E/(label+'.json')).write_text(json.dumps(o,indent=2)+'\n')
 print(label,str(o)[:250],flush=True)
 return o
if __name__=='__main__':
 import sys
 if len(sys.argv)>1:
  for h in sys.argv[1:]:get('https://api.relay.link/requests/v2?hash='+h,'relay_'+h)
 else:
  get('https://docs.relay.link/llms.txt','relay_docs_index')
  get('https://api.relay.link/requests/v2?hash=0xf110d179d86cd74ee3b7e6bda3fa1724258274571d66c1909a05fcbc899d66a1','relay_lookup_B')
