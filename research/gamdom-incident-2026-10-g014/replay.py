"""Read-only replay of saved acquisitions into a new directory."""
import pathlib,json,gzip,urllib.request,datetime,sys,base64
R=pathlib.Path(__file__).resolve().parent;out=pathlib.Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
for name,v in json.loads(gzip.decompress((R/'acquisition_archive.json.gz').read_bytes())).items():
 o={'url':v['url'],'requested_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()};data=json.dumps(v['request']).encode() if 'request' in v else None
 try:
  with urllib.request.urlopen(urllib.request.Request(v['url'],data=data,headers={'Content-Type':'application/json','User-Agent':'NPCsignals-evidence-replay'}),timeout=25) as h:
   raw=h.read();o['http_status']=h.status;o['body_base64']=base64.b64encode(raw).decode()
 except Exception as ex:o['error']=str(ex)
 (out/(name+'.json')).write_text(json.dumps(o,indent=2)+'\n')
