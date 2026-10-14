import pathlib,json,csv,hashlib,datetime,re,subprocess
R=pathlib.Path(__file__).resolve().parents[3];P=R/'research/zyrox-investigation-post-freeze/control-attribution-2026-10-14';raw=P/'raw';J=lambda p:json.loads(p.read_text());dump=lambda n,v:(P/n).write_text(json.dumps(v,indent=2)+'\n')
receipts={f.name.split('.')[0]:J(f)['result'] for f in raw.glob('*.rpc.json') if '.history.' not in f.name and '.terminal.' not in f.name and not f.name.startswith('finality')}
rows=[];summ=[]
for sig,r in sorted(receipts.items()):
 m=r['transaction']['message'];keys=[k['pubkey'] for k in m['accountKeys']];sg=[k['pubkey'] for k in m['accountKeys'] if k['signer']];utc=datetime.datetime.fromtimestamp(r['blockTime'],datetime.timezone.utc).isoformat().replace('+00:00','Z')
 assert r['meta']['err'] is None;assert sum(r['meta']['preBalances'])-sum(r['meta']['postBalances'])==r['meta']['fee']
 summ.append({'signature':sig,'utc':utc,'slot':r['slot'],'signers':sg,'fee_payer':keys[0],'fee_lamports':r['meta']['fee'],'native_sum_decrease':sum(r['meta']['preBalances'])-sum(r['meta']['postBalances']),'pre_balances':dict(zip(keys,r['meta']['preBalances'])),'post_balances':dict(zip(keys,r['meta']['postBalances']))})
 instructions=[(f'outer:{n}',i) for n,i in enumerate(m['instructions'])]+[(f'inner:{g["index"]}.{n}',i) for g in r['meta'].get('innerInstructions') or [] for n,i in enumerate(g['instructions'])]
 for idx,i in instructions:rows.append({'signature':sig,'utc':utc,'slot':r['slot'],'instruction_index':idx,'signers':sg,'fee_payer':keys[0],'fee_lamports':r['meta']['fee'],'program_id':i['programId'],'parsed':i.get('parsed'),'opaque_data':i.get('data'),'accounts':i.get('accounts')})
dump('supporting-instruction-ledger.json',rows);dump('receipt-balance-audit.json',summ)
csg=next(s for s in receipts if s.startswith('3ttmc'));r=receipts[csg];m=r['transaction']['message'];keys=[k['pubkey'] for k in m['accountKeys']];sg=[k['pubkey'] for k in m['accountKeys'] if k['signer']];pre={keys[x['accountIndex']]:x for x in r['meta']['preTokenBalances']};post={keys[x['accountIndex']]:x for x in r['meta']['postTokenBalances']}
new=[];total=0
for n,i in enumerate(m['instructions']):
 p=i.get('parsed',{});
 if p.get('type')!='transferChecked':continue
 q=p['info'];a=int(q['tokenAmount']['amount']);src=q['source'];dst=q['destination'];owner=pre[src]['owner'];assert owner in sg;assert q['multisigAuthority']==owner;assert int(pre[src]['uiTokenAmount']['amount'])-int(post[src]['uiTokenAmount']['amount'])==a;total+=a
 if n==2:continue
 new.append({'id':f'CA{len(new)+1:03}','status':'CONFIRMED','finding':'previously undocumented GLITCH consolidation source in reviewed baseline','signature':csg,'utc':'2026-10-12T17:51:18Z','slot':r['slot'],'instruction_index':f'outer:{n}','asset':'GLITCH SPL Token-2022','mint':q['mint'],'raw_amount':str(a),'decimals':6,'source_token_account':src,'source_historical_owner':owner,'authority':q['multisigAuthority'],'instruction_signers':q['signers'],'destination_token_account':dst,'destination_historical_owner':pre[dst]['owner'],'transaction_signers':sg,'fee_payer':keys[0],'transaction_fee_lamports':35700,'fee_counting':'one shared transaction fee; not per row','source_before_raw':pre[src]['uiTokenAmount']['amount'],'source_after_raw':post[src]['uiTokenAmount']['amount']})
delta=int(post[dst]['uiTokenAmount']['amount'])-int(pre[dst]['uiTokenAmount']['amount']);assert delta==total
dump('consolidation-audit.json',{'signature':csg,'total_raw':str(total),'known_creator_transfer_raw':'70000000000000','new_five_source_total_raw':str(total-70000000000000),'recipient_before_raw':pre[dst]['uiTokenAmount']['amount'],'recipient_after_raw':post[dst]['uiTokenAmount']['amount'],'recipient_delta_raw':str(delta),'native_fee_lamports':35700,'native_fee_payer_decrease':r['meta']['preBalances'][0]-r['meta']['postBalances'][0],'source_owners_and_signers':sg,'formal_multisig_configuration':'NOT ASSESSED: parsed multisigAuthority/signers is not account configuration proof'})
for s,r in receipts.items():
 if s in [x['signature'] for x in J(P/'retrieval-log.json')]:continue
 m=r['transaction']['message'];k=[x['pubkey'] for x in m['accountKeys']];i=m['instructions'][1]['parsed']['info'];assert r['meta']['preBalances'][k.index(i['destination'])]==0
 new.append({'id':f'CA{len(new)+1:03}','status':'CONFIRMED','finding':'first returned account-key funding of new GLITCH consolidation authority; no cross-case control implication','signature':s,'utc':datetime.datetime.fromtimestamp(r['blockTime'],datetime.timezone.utc).isoformat().replace('+00:00','Z'),'slot':r['slot'],'instruction_index':'outer:1','asset':'native SOL','raw_amount':str(i['lamports']),'decimals':9,'source':i['source'],'destination':i['destination'],'authority':i['source'],'signers':[x['pubkey'] for x in m['accountKeys'] if x['signer']],'fee_payer':k[0],'fee_lamports':r['meta']['fee'],'destination_before_lamports':0,'destination_after_lamports':r['meta']['postBalances'][k.index(i['destination'])],'source_before_lamports':r['meta']['preBalances'][0],'source_after_lamports':r['meta']['postBalances'][0]})
dump('new-evidence-ledger.json',new)
fields=['id','status','signature','utc','slot','instruction_index','asset','raw_amount','decimals','authority','fee_payer']
with (P/'new-evidence-ledger.csv').open('w') as f:
 w=csv.DictWriter(f,fields,extrasaction='ignore');w.writeheader();w.writerows(new)
base_files=[]
for d in ['research/zyrox-investigation','research/zyrox-investigation-post-freeze','research/glitch-investigation','research/evidence/binance-v2.0-2026-10-14','research/audits/binance-v2.0-2026-10-14']:
 for f in (R/d).rglob('*'):
  if f.is_file() and P not in f.parents and f.suffix in ['.md','.json','.csv','.py']:
   base_files.append(f)
targets=sg+list({x['source'] for x in new if 'source' in x});matches=[]
for k in targets:
 z=[];g=[]
 for f in base_files:
  if k in f.read_text(errors='replace'):
   if 'research/zyrox-investigation/' in str(f) or 'research/zyrox-investigation-post-freeze/' in str(f):z.append(str(f.relative_to(R)))
   elif 'research/glitch-investigation/' in str(f):g.append(str(f.relative_to(R)))
 matches.append({'address':k,'zyrox_text_matches':z,'glitch_text_matches':g})
dump('exact-address-comparison.json',{'baseline_commit':'b21e5ec2467ff35cb06369d05f5170f5913a697e','scope':'exact case-sensitive address text in two ZYROX research trees; supplementary GLITCH duplicate check; not exhaustive on-chain comparison','matches':matches,'files':[{'path':str(f.relative_to(R)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in base_files if 'binance-v2.0' not in str(f)]})
hist=[]
for f in raw.glob('*.history.rpc.json'):
 k=f.name.split('.')[0];h=J(f)['result'];assert J(raw/f'{k}.terminal.rpc.json')['result']==[]
 hist.append({'address':k,'returned_references':len(h),'earliest_utc':datetime.datetime.fromtimestamp(h[-1]['blockTime'],datetime.timezone.utc).isoformat().replace('+00:00','Z'),'earliest_signature':h[-1]['signature'],'earliest_slot':h[-1]['slot'],'latest_utc':datetime.datetime.fromtimestamp(h[0]['blockTime'],datetime.timezone.utc).isoformat().replace('+00:00','Z'),'terminal_empty':True,'all_references_decoded':False})
dump('history-scope.json',hist)
req=J(raw/'finality.request.json')['params'][0];sts=J(raw/'finality.rpc.json')['result']['value'];assert len(req)==len(sts)==11;assert all(x and x['confirmationStatus']=='finalized' and x['err'] is None for x in sts)
dump('provenance.json',{'provider':'https://api.mainnet-beta.solana.com','baseline_commit':'b21e5ec2467ff35cb06369d05f5170f5913a697e','capture_files':[{'path':str(f.relative_to(P)),'retrieved_at_utc':datetime.datetime.fromtimestamp(f.stat().st_mtime,datetime.timezone.utc).isoformat().replace('+00:00','Z'),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in raw.glob('*')],'timestamp_note':'retrieved_at is local file-write time immediately after response, not server attestation; original response bodies unchanged','provider_independence':'one RPC provider, separate status requests; second-provider agreement NOT ASSESSED'})
print('NEW_TOTAL',total,total-70000000000000,'new rows',len(new),'hist refs',sum(x['returned_references'] for x in hist));print('funding matches',[(x['address'],len(x['zyrox_text_matches'])) for x in matches])
