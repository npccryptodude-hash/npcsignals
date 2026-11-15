"""Verify exact accounting, source receipts, signatures and frozen evidence."""
from analyse import *
import hashlib,subprocess
def verify():
 e=records();derived=derive()
 for name,value in derived.items():assert json.loads((R/(name+'.json')).read_text())==value,name
 for s in json.loads((R/'source_register.json').read_text()):assert hashlib.sha256(json.dumps(e[s['record']],sort_keys=True,separators=(',',':')).encode()).hexdigest()==s['canonical_record_sha256']
 for row in derived['upstream_funding_ledger']:
  if not row['new_transaction'] or row['role']!='B_funding':continue
  t=e['tx_'+row['transaction_hash']]['response']['result'];data=bytes.fromhex(t['input'][2:])
  assert t['from']==row['token_sender'] and t['to']==TOKEN and len(data)==68 and data[:4].hex()=='a9059cbb'
  assert '0x'+data[16:36].hex()==B and int.from_bytes(data[36:68],'big')==int(row['raw_amount'])
 for a in derived['approval_register']:
  if not a['direct_approve_call']:continue
  t=e['tx_'+a['transaction_hash']]['response']['result'];d=bytes.fromhex(t['input'][2:])
  assert len(d)==68 and '0x'+d[16:36].hex()==a['spender'] and int.from_bytes(d[36:68],'big')==int(a['allowance_raw'])
 # Source receipts independently accessed through another provider match selected key fields/logs.
 matched=[]
 for label,other in e.items():
  if not label.startswith(('binance_check_receipt_','bnbchain_check_receipt_')) or 'result' not in other.get('response',{}):continue
  r=other['response']['result'];primary=e['receipt_'+r['transactionHash']]['response']['result']
  for field in ['transactionHash','blockHash','blockNumber','transactionIndex','status']:assert r[field]==primary[field]
  for fields in ['address','topics','data','logIndex']:
   assert [l[fields] for l in r['logs']]==[l[fields] for l in primary['logs']]
  matched.append(r['transactionHash'])
 assert len(matched)==2
 assert n(e['token_decimals']['response']['result'])==18
 assert bytes.fromhex(e['token_symbol']['response']['result'][130:138]).decode()=='USDT'
 assert n(e['B_state_127399999']['response']['result'])==0
 assert e['B_eth_getCode_pre']['response']['result']=='0x'
 # NodeReal's alternate public-key URL is the same provider, not independent infrastructure.
 assert e['nodereal_public_pre_balance']['response']['result']==e['B_state_127435561']['response']['result']
 from verify_signatures import calculate
 sigs=calculate();assert json.loads((R/'signature_verification.json').read_text())==sigs
 auth=[r for r in sigs if r['authorizations']];assert len(auth)==1
 row=auth[0];a=row['authorizations'][0]
 assert row['chain_id']==a['chain_id']==56 and row['nonce']==3 and a['nonce']==4
 assert row['recovered_signer'].lower()==a['recovered_authority'].lower()==B
 expected='0xef0100'+a['implementation'][2:]
 assert e['B_code_127436780']['response']['result']=='0x' and e['B_code_127436781']['response']['result']==expected
 for block in [127435562,127444806]:assert len([r for r in derived['B_ordered_balance_walk'] if r['block']==block])==1
 for address in [A,S1]:
  rows=[r for r in sigs if r['recovered_signer'].lower()==address]
  assert {r['chain_id'] for r in rows}=={1,56} and len({r['recovered_public_key'] for r in rows})==1
 frozen=['gamdom-incident-2026-10','gamdom-incident-2026-10-g006','gamdom-incident-2026-10-g008','gamdom-incident-2026-10-g009','gamdom-incident-2026-10-g010'];count=0;root=R.parents[1]
 for directory in frozen:
  files=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'--','research/'+directory],cwd=root,text=True).splitlines()
  for f in files:assert (root/f).read_bytes()==subprocess.check_output(['git','show',BASE+':'+f],cwd=root);count+=1
 if (R/'SHA256SUMS.json').exists():
  manifest=json.loads((R/'SHA256SUMS.json').read_text());assert set(manifest)=={p.name for p in R.iterdir() if p.is_file() and p.name!='SHA256SUMS.json'}
  for f,sha in manifest.items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==sha,f
 return {'status':'PASS','new_verified_transactions':derived['results']['new_verified_transactions'],'existing_bridge_transactions_not_recounted':2,'zero_residual_reconciliations':len(derived['historical_balance_reconciliation']),'signature_envelopes_verified':len(sigs),'old_Ethereum_transactions_used_for_new_key_comparison':2,'source_receipts_corroborated_by_second_provider':matched,'frozen_files_unchanged':count,'limits':'No ownership, legitimate-consent, human-operator or unauthorized-loss proof; no state-root or consensus replay.'}
if __name__=='__main__':print(json.dumps(verify(),indent=2))
