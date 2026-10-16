"""Offline integrity, lineage, exact accounting and deterministic derivation checks."""
import pathlib,json,hashlib,collections,decimal,tempfile,shutil,subprocess,sys
P=pathlib.Path(__file__).resolve().parent;repo=P.parent.parent;decimal.getcontext().prec=80
J=lambda f:json.loads((P/f).read_text())
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=J('SHA256SUMS.json');assert set(manifest)=={str(f.relative_to(P)) for f in P.rglob('*') if f.is_file() and '__pycache__' not in f.parts and f.name!='SHA256SUMS.json'}
for f,h in manifest.items():assert H(P/f)==h,f
for f,h in J('source_register.json')['frozen_inputs'].items():assert H(repo/f)==h,f
for f,h in J('frozen_file_integrity.json').items():assert H(repo/f)==h,f
rows=J('original_principal_ledger.json');assert len(rows)==34
keys=[(r['chain_id'],r['transaction_hash'],r.get('log_index') if r.get('log_index') is not None else 'native_or_frozen_explorer_single') for r in rows];assert len(set(keys))==34
sums=collections.defaultdict(int)
for r in rows:
 assert int(r['raw_amount'])>0 and decimal.Decimal(r['amount'])==decimal.Decimal(int(r['raw_amount']))/(10**r['decimals'])
 assert r['unauthorized_status']=='UNRESOLVED'
 sums[(r['chain_id'],r.get('token_contract') or 'native',r['token_symbol'],r['decimals'])]+=int(r['raw_amount'])
assert sums=={(r['chain_id'],r['contract'],r['symbol'],r['decimals']):int(r['raw_amount']) for r in J('principal_totals.json')}
assert sum(int(r['raw_amount']) for r in rows if r['chain_id']==56)==706943421822265793499428+7244364582811240700000==714187786405077034199428
assert rows[0]['transaction_hash']=='0xb2cca150592b3ba9344ff17a6f39888a40a855fc1619e8946b8b87e17217578f'
b=J('historical_behavior_baseline.json');s1='0x0067cc2416f792cf0ec5629f5506324ac508f859'
for r in b['ethereum']:
 if r['address']==s1 and r['symbol'] in ['USDT','USDC']:assert r['maximum_exceeds_bounded_baseline'] is False
c=J('authorization_control_register.json');assert all(x['hash_matches_requested'] and x['signature_verified'] for x in c['reused_signature_results'])
assert [x['signing_scheme'] for x in c['bnb_orders']]==['presign','eip712']
# Rebuild only in a disposable tree. No acquisition/network calls and no edits to published inputs.
with tempfile.TemporaryDirectory() as t:
 R=pathlib.Path(t)/'research';R.mkdir();Q=R/P.name;shutil.copytree(P,Q,ignore=shutil.ignore_patterns('__pycache__'))
 for f in J('source_register.json')['frozen_inputs']:
  rel=pathlib.Path(f).relative_to('research');root=rel.parts[0]
  if not (R/root).exists():(R/root).symlink_to(repo/'research'/root,target_is_directory=True)
 subprocess.run([sys.executable,str(Q/'derive.py')],check=True,stdout=subprocess.DEVNULL)
 for f in Q.iterdir():
  if f.is_file() and f.name not in ['SHA256SUMS.json']:assert f.read_bytes()==(P/f.name).read_bytes(),f.name
print(json.dumps(dict(result='PASS',principal_rows=34,new_transactions=0,frozen_files_checked=len(J('frozen_file_integrity.json')),manifest_files_checked=len(manifest),checks=['exact integer asset totals','BNB principal deduplication','unique movement keys','frozen input provenance','bounded maxima','reused signing checks','deterministic offline derivation','SHA256 integrity']),indent=2))
