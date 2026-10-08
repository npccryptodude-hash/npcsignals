"""Refresh current v0.2 integrity only; never regenerate earlier ledgers/source IDs."""
import hashlib,json,pathlib
P=pathlib.Path(__file__).parent.parent
files=[f for f in sorted(P.rglob('*')) if f.is_file() and '__pycache__' not in f.parts and f.name not in ['evidence_index_v0.2.json','SHA256SUMS_v0.2.txt']]
(P/'SHA256SUMS_v0.2.txt').write_text(''.join(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+str(f.relative_to(P))+'\n' for f in files))
index=[{'path':str(f.relative_to(P)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted(files+[P/'SHA256SUMS_v0.2.txt'])]
(P/'evidence_index_v0.2.json').write_text(json.dumps(index,indent=2)+'\n')
print('current v0.2 indexed files',len(index))
