"""Offline integrity and semantic verification. Run from any directory."""
from analyse import *
import subprocess
def verify():
 derived=derive()
 for name,value in derived.items():assert json.loads((R/(name+'.json')).read_text())==value,name
 e=records()
 for entry in json.loads((R/'source_register.json').read_text()):
  assert hashlib.sha256(json.dumps(e[entry['record']],sort_keys=True,separators=(',',':')).encode()).hexdigest()==entry['canonical_record_sha256']
 # Preserve all prior evidence byte for byte at the supplied checkpoint.
 root=R.parents[1];files=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'--','research'],cwd=root,text=True).splitlines();count=0
 frozen_names=['gamdom-incident-2026-10','gamdom-incident-2026-10-g006','gamdom-incident-2026-10-g008','gamdom-incident-2026-10-g009','gamdom-incident-2026-10-g010','gamdom-incident-2026-10-g011']
 for f in files:
  if f.split('/')[1] in frozen_names:
   assert (root/f).read_bytes()==subprocess.check_output(['git','show',BASE+':'+f],cwd=root);count+=1
 # New transaction count is NEAR only. EVM receipts and the presignature are prior work.
 for row in derived['near_execution_register']:
  assert not any(row['transaction_hash'].encode() in (root/f).read_bytes() for f in files if f.endswith(('.json','.md','.csv'))),row['transaction_hash']
 assert len({x['transaction_hash'] for x in derived['near_execution_register']})==4
 assert sum(int(x['source_principal_raw'])-int(x['deposit_raw']) for x in derived['decoded_execution_ledger'])==5274027522735778
 assert all(x['route_evidence_level']=='SUPPORTED' for x in derived['decoded_execution_ledger'])
 manifest=R/'SHA256SUMS.json'
 if manifest.exists():
  m=json.loads(manifest.read_text());assert set(m)=={p.name for p in R.iterdir() if p.is_file() and p.name!='SHA256SUMS.json'}
  for name,sha in m.items():assert hashlib.sha256((R/name).read_bytes()).hexdigest()==sha,name
 return {'status':'PASS','source_order_uids_recomputed':2,'full_app_data_hashes_verified':2,'eip712_order_signature_recovered':1,'precise_uid_presign_trace_and_state_verified':1,'historical_settlement_runtime_matches':2,'new_verified_NEAR_transactions':4,'previously_verified_EVM_transactions_reused':5,'destination_block_balance_residuals':['0','0'],'frozen_files_unchanged':count,'route_classification':'SUPPORTED; protocol index required for cross-chain execution mapping','limitations':'No consensus/state-proof replay; no independent human consent or company ownership proof; NEAR signatures accepted through RPC execution status, not independently Borsh/NEP-413 verified.'}
if __name__=='__main__':print(json.dumps(verify(),indent=2))
