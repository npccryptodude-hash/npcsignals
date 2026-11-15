"""Read-only replay into a new directory; original evidence is never overwritten."""
import pathlib,json,gzip,urllib.request,datetime,sys
R=pathlib.Path(__file__).resolve().parent;out=pathlib.Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
for name,v in json.loads(gzip.decompress((R/'acquisition_archive.json.gz').read_bytes())).items():
 o={'url':v['url'],'requested_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()};body=json.dumps(v['request']).encode() if 'request' in v else None
 try:
  with urllib.request.urlopen(urllib.request.Request(v['url'],data=body,headers={'Content-Type':'application/json','User-Agent':'NPCsignals-evidence-replay'}),timeout=25) as h:
   text=h.read().decode();o['raw_response_text']=text;o['http_status']=h.status
   try:o['response' if body else 'body']=json.loads(text)
   except ValueError:o['body_text']=text
 except Exception as ex:o['error']=str(ex)
 (out/(name+'.json')).write_text(json.dumps(o,indent=2)+'\n')
