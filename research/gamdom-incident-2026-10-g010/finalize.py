"""Save offline result and manifest covering published top-level package files."""
import pathlib,json,hashlib
R=pathlib.Path(__file__).resolve().parent
if __name__=='__main__':
 from verify import verify
 # Existing manifest must already pass; changing files requires deliberate regeneration.
 result=verify()
 (R/'verification_results.json').write_text(json.dumps(result,indent=2)+'\n')
 files=[p for p in R.iterdir() if p.is_file() and p.name!='SHA256SUMS.json']
 manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)}
 (R/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print('manifest entries',len(manifest));print(json.dumps(verify(),indent=2))
