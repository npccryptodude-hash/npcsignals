"""Generate integrity/source indexes and align preserved timelines without rewriting originals."""
import pathlib,json,csv,hashlib,decimal
P=pathlib.Path(__file__).parent;R=P/'raw_sources'
records=[]
for f in sorted(R.glob('*.request.json')):
 j=json.loads(f.read_text());records.append({'source_ID':f'V02S{len(records)+1:04d}','request_file':str(f.relative_to(P)),'url':j.get('url',''),'requested_at_UTC':j.get('requested_at_UTC',''),'method':j.get('method') or j.get('request',{}).get('method',''),'response_file':j.get('response_file') or j.get('response_filename',''),'error':j.get('error',''),'notes':j.get('notes','')})
with (P/'source_inventory_v0.2.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
rows=[]
for name in ['transaction_ledger_v0.2.csv','evm_transaction_ledger_v0.2.csv','evm_extended_ledger_v0.2.csv','chain_extension_ledger_v0.2.csv']:
 for r in csv.DictReader((P/name).open()):
  rows.append({'ID':r['ID'],'timestamp':r['timestamp'],'chain':r['chain'],'tx/signature':r['tx/signature'],'source':r['source'],'destination':r['destination'],'asset':r['asset'],'amount':r['amount'],'action':r['action'],'classification':r['classification'],'provenance status':r['provenance status'],'record_type':r['record_type']})
assert len(rows)==104;assert len({r['ID'] for r in rows})==104;assert {r['ID'] for r in rows}=={f'F{i:04d}' for i in range(103,207)}
V=P.parent/'frogman_research_v0_1'
if not V.exists():V=P.parent/'frozen_v0_1/frogman_research_v0_1'
old=[]
for r in csv.DictReader((V/'transaction_ledger.csv').open()):
 old.append({**{k:r.get(k,'') for k in rows[0]},'record_type':'frozen v0.1 instruction/event'})
assert len(old)==102;assert len({r['ID'] for r in old+rows})==206
with (P/'master_timeline_v0.2.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(sorted(old+rows,key=lambda r:(r['timestamp'],r['chain'],r['ID'])))
g={'scope':'New v0.2 evidence edges only; frozen Solana timeline/ledger remain sibling v0.1 evidence. No identity or source-chain fill equivalence inferred.','edges':rows}
(P/'wallet_graph_combined_v0.2.json').write_text(json.dumps(g,indent=2)+'\n')
balances=[]
for f in sorted(R.glob('eth_remaining_balance_*.response.json')):
 a=f.name[len('eth_remaining_balance_'):-len('.response.json')];j=json.loads(f.read_text());q=json.loads(f.with_name(f.name.replace('.response.json','.request.json')).read_text());balances.append({'address':a,'chain':'Ethereum (1)','balance_ETH':format(decimal.Decimal(int(j['result'],16))/10**18,'f'),'requested_at_UTC':q.get('requested_at_UTC'),'classification':'CONFIRMED','scope':'Latest-state snapshot only; future retention/control NOT ESTABLISHED','source_file':str(f.relative_to(P))})
(P/'observable_balance_snapshots_v0.2.json').write_text(json.dumps(balances,indent=2)+'\n')
files=[p for p in P.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name not in ['evidence_index_v0.2.json','SHA256SUMS_v0.2.txt']]
(P/'SHA256SUMS_v0.2.txt').write_text(''.join(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+str(f.relative_to(P))+'\n' for f in sorted(files)))
index=[{'path':str(f.relative_to(P)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted(files+[P/'SHA256SUMS_v0.2.txt'])]
(P/'evidence_index_v0.2.json').write_text(json.dumps(index,indent=2)+'\n');print({'new_ledger_rows':len(rows),'highest_ID':'F0206','source_records':len(records),'indexed_files':len(index)})
