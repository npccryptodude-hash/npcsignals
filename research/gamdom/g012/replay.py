"""Optional read-only acquisition replay into a separate directory; never overwrites evidence."""
import json,gzip,pathlib,sys,urllib.request,urllib.error,datetime
R=pathlib.Path(__file__).resolve().parent
out=pathlib.Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
e=json.loads(gzip.decompress((R/'acquisition_archive.json.gz').read_bytes()))
for name,v in e.items():
 o={'url':v['url'],'requested_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 data=json.dumps(v['request']).encode() if 'request' in v else None
 try:
  with urllib.request.urlopen(urllib.request.Request(v['url'],data=data,headers={'Content-Type':'application/json'}),timeout=25) as h:
   text=h.read().decode();o['http_status']=h.status
   try:o['response' if data else 'body']=json.loads(text)
   except ValueError:o['body_text']=text
 except Exception as ex:o['error']=str(ex)
 (out/(name+'.json')).write_text(json.dumps(o,indent=2)+'\n')
