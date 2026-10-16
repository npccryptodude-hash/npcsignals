"""Package captured responses deterministically and register every attempt."""
import json,gzip,hashlib,pathlib
R=pathlib.Path(__file__).resolve().parent
e={p.stem:json.loads(p.read_text()) for p in sorted((R/'evidence').glob('*.json'))}
(R/'acquisition_archive.json.gz').write_bytes(gzip.compress(json.dumps(e,sort_keys=True,separators=(',',':')).encode(),mtime=0))
rows=[]
for k,v in e.items():
 rows.append({'record':k,'url':v['url'],'request':v.get('request'),'requested_at_utc':v['requested_at_utc'],'http_status':v.get('http_status'),'error':v.get('error',v.get('response',{}).get('error')),'canonical_record_sha256':hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()})
(R/'source_register.json').write_text(json.dumps(rows,indent=2)+'\n')
