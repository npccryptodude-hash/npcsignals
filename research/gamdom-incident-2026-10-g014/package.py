import pathlib,json,gzip,hashlib
R=pathlib.Path(__file__).resolve().parent
e={p.stem:json.loads(p.read_text()) for p in sorted((R/'evidence').glob('*.json'))}
(R/'acquisition_archive.json.gz').write_bytes(gzip.compress(json.dumps(e,sort_keys=True,separators=(',',':')).encode(),mtime=0))
(R/'source_register.json').write_text(json.dumps([{'record':k,'url':v['url'],'requested_at_utc':v.get('requested_at_utc'),'request':v.get('request'),'http_status':v.get('http_status'),'error':v.get('error',v.get('response',{}).get('error')),'canonical_record_sha256':hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()} for k,v in e.items()],indent=2)+'\n')
