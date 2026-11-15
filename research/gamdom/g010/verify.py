"""Offline verification of records, cross-chain correlators, arithmetic and frozen trees."""
from analyse import *
import subprocess
def verify():
 e=records();data=derive()
 for name,value in data.items():assert json.loads((R/(name+'.json')).read_text())==value,name
 for s in json.loads((R/'source_register.json').read_text()):
  raw=json.dumps(e[s['record']],sort_keys=True,separators=(',',':')).encode()
  assert hashlib.sha256(raw).hexdigest()==s['record_sha256_canonical_json']
 pairs=[('0xb4e697fc1cb8406ca6e18ee3a1b4f975428e2642caa57076df5d9b166848c1b1','0x70a41ee50eb9277365900b8a23e8e30fe20ba4818b2db1a4e626b1fb11f92b14',370000000000000000000000,369592897320),('0xcc827fd1fef937ac1942dd53a7f049061b827bf5292e1aa9a7e79610c00f200b','0xf110d179d86cd74ee3b7e6bda3fa1724258274571d66c1909a05fcbc899d66a1',336943421822265793499428,336199051906277094220550)]
 matches=[]
 for src,dst,rawin,rawout in pairs:
  r=e['bnb_receipt_'+src]['response']['result'];t=e['tx_'+dst]['response']['result'];dr=e['receipt_'+dst]['response']['result']
  deposit=[l for l in r['logs'] if l['address']=='0x4cd00e387622c35bddb9b4c962c136462338bc31'][0]
  identifier=deposit['data'][-64:]
  assert len(identifier)==64 and identifier in t['input'] and integer(deposit['data'][130:194])==rawin
  debit=[l for l in r['logs'] if l['topics'][0]==T and l['topics'][1][-40:]==B[2:]]
  assert len(debit)==1 and integer(debit[0]['data'])==rawin
  credits=[l for l in dr['logs'] if l['topics'][0]==T and l['topics'][2][-40:]==B[2:]]
  assert len(credits)==1 and integer(credits[0]['data'])==rawout
  matches.append({'source_hash':src,'destination_hash':dst,'opaque_32byte_identifier':'0x'+identifier,'source_raw':str(rawin),'destination_raw':str(rawout),'result':'matched source deposit event and destination signed-transaction input representation; matching service index also preserved'})
 # Historical symbol decoding caught an acquisition alias error before publication.
 symbol=e['token_USDS_symbol']['response']['result'];assert bytes.fromhex(symbol[130:138]).decode()=='USD1'
 assert integer(e['token_USDS_decimals']['response']['result'])==18
 # Independent receipt and query log representations agree for every E1 event.
 indexed={(l['transactionHash'],l['logIndex']):l for n in ['E1_window_1','E1_window_2'] for l in e[n]['response']['result']}
 for row in data['incident_origin_ledger']:
  if row['chain_id']!=1 or 'log_index' not in row or X not in [row['token_sender'],row['token_recipient']]:continue
  l=indexed[(row['transaction_hash'],hex(row['log_index']))]
  assert l['address']==row['token_contract'] and integer(l['data'])==int(row['raw_amount'])
 root=R.parents[1]
 dirs=['research/gamdom-incident-2026-10','research/gamdom-incident-2026-10-g006','research/gamdom-incident-2026-10-g008','research/gamdom-incident-2026-10-g009']
 frozen_count=0
 for d in dirs:
  files=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'--',d],cwd=root,text=True).splitlines()
  for f in files:
   assert (root/f).read_bytes()==subprocess.check_output(['git','show',BASE+':'+f],cwd=root),f
   frozen_count+=1
 manifests=R/'SHA256SUMS.json'
 if manifests.exists():
  for f,h in json.loads(manifests.read_text()).items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h,f
 return {'status':'PASS','new_verified_transactions':data['results']['new_transactions'],'new_successful_transactions':sum(t['success'] and t['new_beyond_frozen'] for t in data['transaction_register']),'new_failed_transactions':sum(not t['success'] and t['new_beyond_frozen'] for t in data['transaction_register']),'existing_transactions_not_recounted':data['results']['existing_transactions_extended_not_recounted'],'zero_residual_balance_reconciliations':len(data['balance_reconciliation']),'frozen_files_unchanged':frozen_count,'cross_chain_matches':matches,'limits':'No consensus replay, Merkle proof, signature recovery for new transactions, ownership or unauthorized-status proof.'}
if __name__=='__main__':print(json.dumps(verify(),indent=2))
