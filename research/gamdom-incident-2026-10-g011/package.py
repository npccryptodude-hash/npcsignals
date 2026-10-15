"""Deterministic parsed-evidence archive; original local cache remains intact."""
import pathlib,json,gzip,hashlib
R=pathlib.Path(__file__).resolve().parent
if __name__=='__main__':
 e={p.stem:json.loads(p.read_text()) for p in sorted((R/'evidence').glob('*.json'))}
 (R/'rpc_archive.json.gz').write_bytes(gzip.compress(json.dumps(e,sort_keys=True,separators=(',',':')).encode(),mtime=0))
 sources=[]
 for k,o in e.items():sources.append({'record':k,'endpoint':o['endpoint'],'request':o['request'],'requested_at_utc':o['requested_at_utc'],'canonical_record_sha256':hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'result_available':'result' in o.get('response',{}),'scope':'Parsed primary RPC representation; not HTTP wire capture or consensus proof.'})
 (R/'source_register.json').write_text(json.dumps(sources,indent=2)+'\n')
 print('archive records',len(e),'gzip bytes',(R/'rpc_archive.json.gz').stat().st_size)
