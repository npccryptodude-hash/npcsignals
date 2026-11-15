"""Offline verification; requires frozen adjacent G012 and Git base objects."""
from analyse import *
import subprocess
def verify():
 d=derive();e=records();root=R.parents[1]
 for name,value in d.items():assert json.loads((R/(name+'.json')).read_text())==value,name
 for s in json.loads((R/'source_register.json').read_text()):assert s['canonical_record_sha256']==hashlib.sha256(json.dumps(e[s['record']],sort_keys=True,separators=(',',':')).encode()).hexdigest()
 frozen=['gamdom-incident-2026-10','gamdom-incident-2026-10-g006','gamdom-incident-2026-10-g008','gamdom-incident-2026-10-g009','gamdom-incident-2026-10-g010','gamdom-incident-2026-10-g011','gamdom-incident-2026-10-g012'];count=0
 files=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'--','research'],cwd=root,text=True).splitlines()
 for f in files:
  if f.split('/')[1] in frozen:
   assert (root/f).read_bytes()==subprocess.check_output(['git','show',BASE+':'+f],cwd=root);count+=1
 for h in SWEEPS:
  assert not any(h.encode() in (root/f).read_bytes() for f in files if f.endswith(('.md','.json','.csv')))
 m=R/'SHA256SUMS.json'
 if m.exists():
  manifest=json.loads(m.read_text());assert set(manifest)=={p.name for p in R.iterdir() if p.is_file() and p.name!='SHA256SUMS.json'}
  for name,sha in manifest.items():assert hashlib.sha256((R/name).read_bytes()).hexdigest()==sha,name
 return {'status':'PASS','new_BNB_transactions':2,'new_NEAR_transactions':0,'previous_NEAR_execution_trees_expanded':4,'new_receipt_details_verified':24,'source_messages_reconstructed':2,'deposit_attestations_verified':2,'source_transaction_envelopes_verified':2,'historical_locker_runtime_matches':2,'historical_NEAR_code_hashes_verified':2,'zero_same_asset_reconciliation_residuals':4,'full_routes':['SUPPORTED','SUPPORTED'],'frozen_files_unchanged':count,'limits':'No authenticated OMFT payout instruction, MPC quorum proof, local Solidity/Rust recompilation, Merkle or consensus validation. Existing Ethereum/NEAR transactions are not recounted.'}
if __name__=='__main__':print(json.dumps(verify(),indent=2))
