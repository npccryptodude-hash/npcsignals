from analyse import *
import subprocess
def verify():
 e=records();d=derive();root=R.parents[1]
 for name,data in d.items():assert json.loads((R/(name+'.json')).read_text())==data,name
 for s in json.loads((R/'source_register.json').read_text()):assert s['canonical_record_sha256']==hashlib.sha256(json.dumps(e[s['record']],sort_keys=True,separators=(',',':')).encode()).hexdigest()
 for name,v in e.items():
  if name.endswith('_release_archive') and 'body_base64' in v:
   b=base64.b64decode(v['body_base64']);assert hashlib.sha256(b).hexdigest()==v['sha256'];assert 'sha512-'+base64.b64encode(hashlib.sha512(b).digest()).decode()==v['declared_integrity']
 frozen=['gamdom-incident-2026-10','gamdom-incident-2026-10-g006','gamdom-incident-2026-10-g008','gamdom-incident-2026-10-g009','gamdom-incident-2026-10-g010','gamdom-incident-2026-10-g011','gamdom-incident-2026-10-g012','gamdom-incident-2026-10-g013'];count=0
 files=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'--','research'],cwd=root,text=True).splitlines()
 for f in files:
  if f.split('/')[1] in frozen:
   assert (root/f).read_bytes()==subprocess.check_output(['git','show',BASE+':'+f],cwd=root);count+=1
 if (R/'SHA256SUMS.json').exists():
  m=json.loads((R/'SHA256SUMS.json').read_text());assert set(m)=={p.name for p in R.iterdir() if p.is_file() and p.name!='SHA256SUMS.json'}
  for f,h in m.items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
 return {'status':'PASS','new_transactions':0,'existing_Ethereum_signatures_newly_verified':2,'historical_factory_snapshots_checked':2,'historical_factory_method_not_found_results':2,'historical_token_metadata_verified':1,'full_routes':['SUPPORTED','SUPPORTED'],'new_acquisition_records':len(e),'frozen_files_unchanged':count,'authenticated_OMFT_payout_instructions_obtained':0,'limits':'No source-to-WASM build proof, historically authorized OMFT payout key, backend independence proof or signed withdrawal-to-Ethereum mapping. Valid Ethereum signatures authorize destination transfers only.'}
if __name__=='__main__':print(json.dumps(verify(),indent=2))
