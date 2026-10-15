"""Save the completed verification result and publishable-file manifest."""
from analyse import R
import json,hashlib
if __name__=='__main__':
 from verify import verify
 (R/'verification_results.json').write_text(json.dumps(verify(),indent=2)+'\n')
 manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(R.iterdir()) if p.is_file() and p.name!='SHA256SUMS.json'}
 (R/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print(json.dumps(verify(),indent=2))
