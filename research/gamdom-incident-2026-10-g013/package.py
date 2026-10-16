"""Preserve all acquisition attempts in a deterministic normalized JSON archive."""
import pathlib,json,gzip,hashlib
R=pathlib.Path(__file__).resolve().parent
e={p.stem:json.loads(p.read_text()) for p in sorted((R/'evidence').glob('*.json'))}
(R/'acquisition_archive.json.gz').write_bytes(gzip.compress(json.dumps(e,sort_keys=True,separators=(',',':')).encode(),mtime=0))
rows=[{'record':k,'url':v['url'],'request':v.get('request'),'requested_at_utc':v['requested_at_utc'],'http_status':v.get('http_status'),'error':v.get('error',v.get('response',{}).get('error')),'canonical_record_sha256':hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()} for k,v in e.items()]
(R/'source_register.json').write_text(json.dumps(rows,indent=2)+'\n')
