"""Save indexes and derived views only; no network requests."""
import hashlib,json,pathlib
P=pathlib.Path(__file__).parent
prior=json.loads((P.parent/'continuation_2026_10_08/master_timeline_F0001_F0425.json').read_bytes())['rows']
new=json.loads((P/'transaction_ledger_F0426_F0431.json').read_bytes())
for r in new:r['source_record']='continuation_2026_10_09/'+r['source_record']
rows=prior+new
assert len(rows)==431 and {r['ID'] for r in rows}=={f'F{i:04d}' for i in range(1,432)}
rows.sort(key=lambda r:(r.get('timestamp',''),r['ID']))
(P/'master_timeline_F0001_F0431.json').write_text(json.dumps({'notes':'Derived combined view. Snapshot rows are not transfers. Earlier records remain unchanged. Do not sum hops, account credits, fills and balances as incident losses.','rows':rows},indent=2)+'\n')
sources=[]
for f in sorted((P/'raw').glob('*.request.json')):
    r=json.loads(f.read_bytes());r['source_ID']=f'DAY09S{len(sources)+1:04d}';r['request_file']='raw/'+f.name
    if r.get('response_file'):r['response_sha256']=hashlib.sha256((P/'raw'/r['response_file']).read_bytes()).hexdigest()
    sources.append(r)
(P/'source_inventory.json').write_text(json.dumps(sources,indent=2)+'\n')
summary=json.loads((P/'followup_summary.json').read_bytes())
(P/'wallet_entity_snapshot_update.json').write_text(json.dumps({'classification':'CONFIRMED','scope':'First-party account observations only; no new control attribution or onward graph edges','accounts':summary['accounts'],'provenance_boundaries':['mixed Relay liquidity','mixed Hyperliquid bridge custody','no XMR1-to-native-XMR match','broken Privacy Cash withdrawal linkage']},indent=2)+'\n')
files=[f for f in sorted(P.rglob('*')) if f.is_file() and '__pycache__' not in f.parts and f.name not in ['evidence_index.json','SHA256SUMS.txt']]
items=[{'path':str(f.relative_to(P)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in files]
(P/'evidence_index.json').write_text(json.dumps({'ledger_range':['F0426','F0431'],'files':items},indent=2)+'\n')
(P/'SHA256SUMS.txt').write_text(''.join(x['sha256']+'  '+x['path']+'\n' for x in items))
print({'timeline_rows':len(rows),'source_records':len(sources),'indexed_supplement_files':len(items)})
