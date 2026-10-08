import json,csv,pathlib,datetime,decimal,hashlib,zipfile
P=pathlib.Path(__file__).parent;D=decimal.Decimal
V='9wMSNoA7TzhwUjqsACVGEvzAxAibCHnsZTgXEAGov8zQ';H='69FnU8vszZSZF6DZCT6VHdsvm3DvvojDgbwqzHJ4cCFS';POOL='4AV2Qzp3N4c9RfzyEbNZs2wqWfW4EwKnnxFAZCndvfGh';PC='9fhQBbumKEFuXtMBDw8AaQyAjCorLGJQiS3skWZdQyQD';BP='BPxxfRCXkUVhig4HS1Lh7kZqV6SPJhzfEk4x6fVBjPCy';Z='ZesMGYmokFiEuDvNzWeMhB7jxF6eUW8c512vwSKSTNK';USDC='EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v';WSOL='So11111111111111111111111111111111111111112'
def ts(t):return datetime.datetime.fromtimestamp(t,datetime.timezone.utc).isoformat().replace('+00:00','Z')
def num(n,d=9):return format(D(n)/D(10)**d,'f')
def writecsv(name,rows,fields=None):
 with (P/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rows[0]));w.writeheader();w.writerows(rows)
txs=sorted([(f,json.loads(f.read_text())['result']) for f in (P/'raw_transactions').glob('*.json')],key=lambda x:(x[1]['blockTime'],x[1]['slot'],x[0].stem))
ledger=[];timeline=[];deps=[];sales=[];entities={};tokenaccounts=[]
for f,j in txs:
 sig=f.stem;m=j['transaction']['message'];meta=j['meta'];keys=m['accountKeys'];pub=[x['pubkey'] for x in keys];signers=[x['pubkey'] for x in keys if x['signer']];failed=meta['err'] is not None;time=ts(j['blockTime']);fee=num(meta['fee']);programs=sorted(set(i['programId'] for i in m['instructions']));ins=m['instructions']+sum([x['instructions'] for x in meta.get('innerInstructions',[])],[])
 owners={};mints={};decs={}
 for x in meta.get('preTokenBalances',[])+meta.get('postTokenBalances',[]):
  a=pub[x['accountIndex']];owners[a]=x.get('owner','');mints[a]=x['mint'];decs[a]=x['uiTokenAmount']['decimals']
 for a,o in owners.items():
  tokenaccounts.append({'tx/signature':sig,'token_account':a,'owner':o,'mint':mints[a],'decimals':decs[a]})
 def row(source,dest,asset,amount,action,notes,prov='mixed',classification='CONFIRMED',protocol=''):
  ledger.append({'ID':f'F{len(ledger)+1:04d}','timestamp':time,'chain':'Solana mainnet','tx/signature':sig,'source':source,'destination':dest,'asset':asset,'amount':amount,'USD value if available':'','action':action,'protocol':protocol,'signer/authority if known':';'.join(signers),'fee_payer':pub[0],'network_fee_SOL':fee,'provenance status':prov,'classification':classification,'source':'raw_transactions/'+f.name,'notes':notes})
 for ix,i in enumerate(ins):
  pa=i.get('parsed',{});info=pa.get('info',{});typ=pa.get('type');pr=i['programId']
  if typ not in ['transfer','transferChecked']:continue
  source=info.get('source','');dest=info.get('destination','');asset=info.get('mint',mints.get(source,''));amount=info.get('tokenAmount',{}).get('uiAmountString')
  if 'lamports' in info:asset='SOL';amount=num(info['lamports'])
  elif amount is None:amount=num(int(info.get('amount',0)),decs.get(source,0))
  auth=info.get('authority',info.get('multisigAuthority',''));prov='intact' if source==V or owners.get(source)==V else 'mixed'
  note=f'instruction flattened index={ix}; program={pr}; authority={auth}; source owner={owners.get(source,source)}; destination owner={owners.get(dest,dest)}. '
  if failed:note+='Attempt only: transaction failed; no transfer committed.';action='failed transfer instruction';prov='intact'
  else:action='native transfer' if asset=='SOL' else 'token transfer'
  if dest==POOL and asset=='SOL' and not failed:
   action='Privacy Cash deposit';deps.append({'timestamp':time,'signature':sig,'source_wallet':source,'pool':POOL,'program':PC,'amount_SOL':amount,'fee_SOL':fee,'other_balance_cost_SOL':num(meta['preBalances'][0]-meta['postBalances'][0]-info['lamports']-meta['fee']),'mechanism':'Transact; System Program transfer; commitment events','provenance':'mixed at source; broken deposit-to-withdrawal linkage','classification':'CONFIRMED'});note+='Pool entry confirmed; no withdrawal match.'
  row(source,dest,asset,amount,action,note,prov,protocol=PC if action=='Privacy Cash deposit' else pr)
 row(pub[0],'network','SOL',fee,'network fee','Fee occurs even for failed transaction; repeated network_fee_SOL columns are metadata, not additional fees.')
 pre={};post={}
 for x in meta.get('preTokenBalances',[]):
  if x.get('owner')==H:pre[x['mint']]=pre.get(x['mint'],0)+int(x['uiTokenAmount']['amount'])
 for x in meta.get('postTokenBalances',[]):
  if x.get('owner')==H:post[x['mint']]=post.get(x['mint'],0)+int(x['uiTokenAmount']['amount'])
 changes={a:post.get(a,0)-pre.get(a,0) for a in pre.keys()|post.keys()}
 if not failed and any(n<0 for n in changes.values()):
  ix=pub.index(H);delta=meta['postBalances'][ix]-meta['preBalances'][ix];out=[]
  for a,n in changes.items():
   if n<0:out.append(a+':'+num(-n,next(x['uiTokenAmount']['decimals'] for x in meta['preTokenBalances'] if x['mint']==a)))
  receipts=0
  for i in ins:
   info=i.get('parsed',{}).get('info',{});dest=info.get('destination');src=info.get('source');mint=info.get('mint',mints.get(src))
   # WSOL recipient token account may be created and closed in same transaction; known account is audited in receipts.
   if dest=='2kDWUhGyv6yz1Ta3okLMaSnuRpAgVabCUgcFfGfGjxZa' and (mint==WSOL or 'amount' in info):receipts+=int(info.get('tokenAmount',{}).get('amount',info.get('amount',0)))
  sales.append({'timestamp':time,'signature':sig,'source_wallet':H,'asset_decrease':';'.join(out),'top_level_programs':';'.join(programs),'WSOL_gross_receipts_SOL':num(receipts) if receipts else '', 'native_balance_change_SOL':num(delta),'network_fee_SOL':fee,'fee_payer':pub[0],'destination_wallet':H,'slippage':'not independently measured','classification':'CONFIRMED','notes':'Native balance delta differs from gross receipt due to fee/tips/rent. Intermediate routing transfers must not be summed as separate sale proceeds.'})
 timeline.append({'timestamp_UTC':time,'timestamp_SGT':datetime.datetime.fromtimestamp(j['blockTime'],datetime.timezone(datetime.timedelta(hours=8))).isoformat(),'chain':'Solana mainnet','slot':j['slot'],'tx/signature':sig,'status':'failed' if failed else 'success','signers':';'.join(signers),'fee_payer':pub[0],'fee_SOL':fee,'top_level_programs':';'.join(programs),'classification':'CONFIRMED','interpretation':'Receipt-confirmed activity; unauthorized status derives from public incident report, not chain alone.'})
 for a in signers+[H,V,POOL,PC]+programs:
  if a not in entities:entities[a]={'address':a,'chain':'Solana mainnet','role':'transaction signer' if a in signers else 'program' if a in programs else 'pool' if a==POOL else 'receiving wallet' if a==H else 'affected wallet','first appearance':time,'funding source':'see ledger; not assumed','outflows':'see ledger','known protocol interaction':PC if a in [H,POOL,PC] else '', 'control evidence':'Transaction signer' if a in signers else 'no human-control inference','classification':'CONFIRMED','notes':'First appearance means first in captured incident-window receipts, not first ever.'}
writecsv('transaction_ledger.csv',ledger);writecsv('timeline.csv',timeline);writecsv('privacy_cash_deposits.csv',deps);writecsv('asset_disposal.csv',sales);writecsv('token_account_authorities.csv',tokenaccounts)
for a,role,c in [('0x14AA2A71dbb5eF87b81F92205E2699AA4aa65794','reported affected EVM wallet','SUPPORTED'),('0x427C4b37de0714821B09C4FC655a713AbbCfbA83','publicly reported downstream EVM wallet','CLAIMED')]:entities[a]={'address':a,'chain':'EVM; chain-specific history not reproduced','role':role,'first appearance':'public sources captured 2026-10-08','funding source':'UNRESOLVED','outflows':'UNRESOLVED','known protocol interaction':'UNRESOLVED','control evidence':'NOT ESTABLISHED','classification':c,'notes':'Address reuse across EVM chains does not prove activity on each chain.'}
writecsv('wallet_entity_table.csv',list(entities.values()))
total=sum(D(x['amount_SOL']) for x in deps)
summary={'raw_receipts':len(txs),'ledger_rows':len(ledger),'deposit_count':len(deps),'privacy_deposits_SOL':format(total,'f'),'BP_sent':num(1429939158705563),'BP_disposed':num(4*357484789676390),'BP_remaining_raw_units':3,'sale_count':len(sales),'capture_date':'2026-10-08','rpc':'https://api.mainnet-beta.solana.com'}
(P/'calculated_summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary));
