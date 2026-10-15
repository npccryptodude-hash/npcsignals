"""Deterministic compression and source register. Does not delete acquisition files."""
import pathlib,json,gzip,hashlib
R=pathlib.Path(__file__).resolve().parent
def digest(b):return hashlib.sha256(b).hexdigest()
if __name__=='__main__':
 records={p.stem:json.loads(p.read_text()) for p in sorted((R/'evidence').glob('*.json'))}
 raw=json.dumps(records,sort_keys=True,separators=(',',':')).encode()
 (R/'rpc_archive.json.gz').write_bytes(gzip.compress(raw,mtime=0))
 sources=[]
 for k,o in records.items():
  sources.append({'record':k,'url':o.get('endpoint',o.get('url')),'request':o.get('request'),'requested_at_utc':o.get('requested_at_utc'),'record_sha256_canonical_json':digest(json.dumps(o,sort_keys=True,separators=(',',':')).encode()),'result_available':'result' in o.get('response',{}) or 'body' in o,'limitations':'Single-provider RPC or public service index. See coverage report. HTTP bodies preserved after JSON parsing where applicable.'})
 (R/'source_register.json').write_text(json.dumps(sources,indent=2)+'\n')
 print('preserved acquisition records',len(records),'compressed_bytes',len((R/'rpc_archive.json.gz').read_bytes()))
