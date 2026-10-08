"""Supplemental index avoids rewriting the earlier saved v0.2 checkpoint."""
import hashlib,json,pathlib
P=pathlib.Path(__file__).parent
files=[f for f in sorted(P.rglob('*')) if f.is_file() and '__pycache__' not in f.parts and f.name not in {'evidence_index.json','SHA256SUMS.txt'}]
items=[{'path':str(f.relative_to(P)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in files]
(P/'evidence_index.json').write_text(json.dumps({'base_commit':'8543f9e964089612c0a1a3f52b26709e12f6f95b','ledger_range':['F0207','F0425'],'files':items,'scope':'Supplement to the saved v0.2 package; original indexes describe their earlier checkpoint. All preserved partial-collection records included; only explicitly verified events receive ledger IDs.'},indent=2)+'\n')
(P/'SHA256SUMS.txt').write_text(''.join(x['sha256']+'  '+x['path']+'\n' for x in items))
print('indexed',len(items),'files')
