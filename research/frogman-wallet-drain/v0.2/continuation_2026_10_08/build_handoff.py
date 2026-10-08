import csv,hashlib,json,pathlib
P=pathlib.Path(__file__).parent
base=list(csv.DictReader((P.parent/'master_timeline_v0.2.csv').open()))
new=[]
for name in ['transaction_ledger_F0207_F0208.csv','hyperliquid_ledger_F0209_F0220.csv','spot_fills_F0221_F0425.csv']:
    for r in csv.DictReader((P/name).open()):
        r['source_record']='continuation_2026_10_08/'+r['source_record'];new.append(r)
allrows=base+new
assert len(allrows)==425 and len({r['ID'] for r in allrows})==425
assert {r['ID'] for r in allrows}=={f'F{i:04d}' for i in range(1,426)}
allrows.sort(key=lambda r:(r.get('timestamp',''),r['ID']))
(P/'master_timeline_F0001_F0425.json').write_text(json.dumps({'note':'Chronological combined view, not a sum of losses. Existing ledger records and classifications unchanged. Deposit credits represent already recorded bridge transfers. Context events are not incident-specific outflows.','rows':allrows},indent=2)+'\n')
hl=json.loads((P/'hyperliquid_summary.json').read_bytes());spot=json.loads((P/'spot_execution_summary.json').read_bytes())
wallets=[{'address':'0x2df1c51e09aecf9cacb7bc98cb1742757f163df7','chain':'Arbitrum (42161)','role':'Hyperliquid legacy USDC bridge (first-party documentation); mixed custody','classification':'SUPPORTED','control_evidence':'NOT ESTABLISHED: no historical bytecode/source or operator/permission audit','notes':'Six case transfers and matching first-party deposit credits reproduced. Arbitrary bridge outflows are not linked to particular case deposits.'}]
for a in spot['accounts']:
    wallets.append({'address':a['address'],'chain':'Hyperliquid account ledger','role':'Account with exact-hash matched deposit, internal spot transfer and reproduced buy fills','classification':'CONFIRMED','funding_source':'Previously reproduced Arbitrum transfer and first-party deposit credit','outflows':'Internal account transfer and spot executions; external withdrawal NOT ESTABLISHED','known_protocol_interaction':'Hyperliquid @260 spot market, XMR1/USDC current metadata','control_evidence':'NOT ESTABLISHED: API account attribution is not signer or beneficial-owner proof','notes':a})
(P/'wallet_entity_update.json').write_text(json.dumps(wallets,indent=2)+'\n')
(P/'wallet_graph_account_update.json').write_text(json.dumps({'nodes':wallets,'edges':new,'boundaries':['Relay has deterministic order linkage but mixed physical liquidity.','Hyperliquid bridge has exact deposit-account ledger association but pooled physical custody.','Spot XMR1 holdings do not establish a native Monero redemption or beneficiary.','Privacy Cash withdrawal matching remains broken as recorded in v0.1.']},indent=2)+'\n')
records=[]
for f in sorted((P/'raw').glob('*.request.json')):
    x=json.loads(f.read_bytes());x['ID']=f'CONT{len(records)+1:04d}';x['request_record']='raw/'+f.name
    if x.get('response_file'):
        b=(P/'raw'/x['response_file']).read_bytes();x['response_sha256']=hashlib.sha256(b).hexdigest()
    records.append(x)
(P/'source_inventory.json').write_text(json.dumps({'scope':'Read-only primary requests for this supplement, including failed and partial collection. No source identifiers from earlier checkpoints are renumbered.','sources':records},indent=2)+'\n')
print('combined timeline',len(allrows),'new records',len(new),'request records',len(records))
