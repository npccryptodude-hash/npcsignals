import pathlib,json,datetime
from decimal import Decimal
P=pathlib.Path(__file__).resolve().parent
W='56HEQykziUkwvpK5uPzFrRbGD4Ek8HdWgjgeDvNmDoEJ';T='CzissnPHhEu7NifSLfwhuvFMdfu7F8X4vR2HhF1o1PEL';B='5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9';D='CyBjGpte4Npi5zNkdtWumPxVW4kpMR8BuFSbA587xZES'
sigs=sorted(json.loads((P/'selected-signatures.json').read_text()),key=lambda s:(json.loads((P/(s+'.json')).read_text())['slot'],json.loads((P/(s+'.json')).read_text()).get('transactionIndex',0)));statuses=json.loads((P/'finality.json').read_text());records=[];audit=[];token_flow=[];opening=None;closing=None
headers=['id','signature','utc','slot','transaction_index','instruction_index','instruction_type','program_id','source','recipient','raw_amount','decimals','exact_amount','mint','source_owner','source_owner_evidence','recipient_owner','recipient_owner_evidence','authority','signers','fee_payer','fee_lamports','source_pre_lamports','source_post_lamports','recipient_pre_lamports','recipient_post_lamports','source_token_balances_json','recipient_token_balances_json','instruction_json','classification','execution_result','confirmation','source_url'];matrix=[headers]
for ti,sig in enumerate(sigs,1):
 t=json.loads((P/(sig+'.json')).read_text());m=t['meta'];keys=t['transaction']['message']['accountKeys'];addr=[k['pubkey'] for k in keys];sg=[k['pubkey'] for k in keys if k['signer']];utc=datetime.datetime.fromtimestamp(t['blockTime'],datetime.timezone.utc).isoformat();groups=[('outer',t['transaction']['message']['instructions'])]+[('inner:'+str(g['index']),g['instructions']) for g in m.get('innerInstructions',[]) or []];owners={};oe={};tb={};mint={}
 assert m['err'] is None and statuses[sig]['confirmationStatus']=='finalized' and statuses[sig]['err'] is None and statuses[sig]['slot']==t['slot']
 for kind,items in groups:
  for ii,ix in enumerate(items):
   v=ix.get('parsed',{});v=v if isinstance(v,dict) else {};info=v.get('info',{})
   if v.get('type','').startswith('initializeAccount') and info.get('owner') and info.get('account'):owners[info['account']]=info['owner'];oe[info['account']]=kind+':'+str(ii)+' initialization';mint[info['account']]=info.get('mint')
 for side in ['preTokenBalances','postTokenBalances']:
  for v in m.get(side,[]):
   a=addr[v['accountIndex']];tb.setdefault(a,{})[side]=v
   if v.get('owner'):owners[a]=v['owner'];oe[a]=side+' owner field'
   mint[a]=v['mint']
 for kind,items in groups:
  for ii,ix in enumerate(items):
   v=ix.get('parsed',{});v=v if isinstance(v,dict) else {};info=v.get('info',{});itype=v.get('type','opaque');s=info.get('source') or info.get('account');d=info.get('destination') or info.get('newAccount');a=addr.index(s) if s in addr else None;b=addr.index(d) if d in addr else None;ta=info.get('tokenAmount',{});raw=ta.get('amount',info.get('lamports'));dec=ta.get('decimals',9 if 'lamports' in info else None);authority=info.get('authority') or info.get('multisigAuthority') or (s if ix.get('programId')=='11111111111111111111111111111111' and itype in ['transfer','createAccount'] else info.get('owner'));classification='instruction'
   if itype=='transferChecked' and d==T:classification='known_case_inbound' if owners.get(s)=='6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N' else 'other_inbound_distinct_address'
   if itype=='transferChecked' and s==T:classification='CEX_INFRASTRUCTURE_INBOUND_supported_attribution' if owners.get(d)==B else 'outgoing_unresolved'
   r={'id':f'F{ti:03d}.{kind}:{ii}','signature':sig,'utc':utc,'slot':t['slot'],'transaction_index':t.get('transactionIndex'),'instruction_index':kind+':'+str(ii),'instruction_type':itype,'program_id':ix.get('programId'),'source':s,'recipient':d,'raw_amount':None if raw is None else str(raw),'decimals':dec,'exact_amount':str(Decimal(str(raw))/Decimal(10)**dec) if raw is not None and dec is not None else None,'mint':info.get('mint') or mint.get(s) or mint.get(d),'source_owner':owners.get(s),'source_owner_evidence':oe.get(s),'recipient_owner':owners.get(d),'recipient_owner_evidence':oe.get(d),'authority':authority,'signers':sg,'fee_payer':addr[0],'fee_lamports':m['fee'],'source_pre_lamports':m['preBalances'][a] if a is not None else None,'source_post_lamports':m['postBalances'][a] if a is not None else None,'recipient_pre_lamports':m['preBalances'][b] if b is not None else None,'recipient_post_lamports':m['postBalances'][b] if b is not None else None,'source_token_balances_json':json.dumps(tb.get(s),sort_keys=True),'recipient_token_balances_json':json.dumps(tb.get(d),sort_keys=True),'instruction_json':json.dumps(ix,sort_keys=True),'classification':classification,'execution_result':'SUCCESS','confirmation':'finalized','source_url':'https://explorer.solana.com/tx/'+sig};records.append(r)
   if itype=='transferChecked' and (s==T or d==T):token_flow.append(r)
 fee={'id':f'F{ti:03d}.FEE','signature':sig,'utc':utc,'slot':t['slot'],'transaction_index':t.get('transactionIndex'),'instruction_index':'fee','instruction_type':'transaction_fee','source':addr[0],'recipient':'network','raw_amount':str(m['fee']),'decimals':9,'exact_amount':str(Decimal(m['fee'])/10**9),'signers':sg,'fee_payer':addr[0],'fee_lamports':m['fee'],'classification':'fee','execution_result':'SUCCESS','confirmation':'finalized','source_url':'https://explorer.solana.com/tx/'+sig};records.append(fee)
 residual=sum(m['preBalances'])-sum(m['postBalances'])-m['fee'];assert residual==0
 audit.append({'signature':sig,'utc':utc,'slot':t['slot'],'fee_lamports':m['fee'],'native_residual_lamports':residual,'accounts':[{'address':k['pubkey'],'signer':k['signer'],'pre_lamports':m['preBalances'][i],'post_lamports':m['postBalances'][i]} for i,k in enumerate(keys)],'token_balances':tb})
 # The specified token account's per-transaction balance must be continuous.
 if T in tb:
  pre=tb[T].get('preTokenBalances');post=tb[T].get('postTokenBalances');pr=int(pre['uiTokenAmount']['amount']) if pre else 0;po=int(post['uiTokenAmount']['amount']) if post else 0
  if opening is None:opening=pr
  if closing is not None:assert closing==pr,(sig,closing,pr)
  closing=po
for r in records:
 d={**r,'signers':';'.join(r['signers'])};matrix.append(['' if d.get(k) is None else str(d[k]) for k in headers])
(P/'instruction-ledger.json').write_text(json.dumps(records,indent=2));(P/'ledger-matrix.json').write_text(json.dumps([dict(zip(headers,r)) for r in matrix[1:]],indent=2));(P/'csv-rows.json').write_text(json.dumps(matrix));(P/'balance-audit.json').write_text(json.dumps(audit,indent=2));(P/'token-flow-ledger.json').write_text(json.dumps(token_flow,indent=2))
known=sum(int(r['raw_amount']) for r in token_flow if r['classification']=='known_case_inbound');other=sum(int(r['raw_amount']) for r in token_flow if r['classification']=='other_inbound_distinct_address');out=sum(int(r['raw_amount']) for r in token_flow if r['source']==T);assert known==995831402 and other==1100 and out==995831502 and opening+known+other-out==closing==1000
summary={'unique_receipts':len(sigs),'ledger_rows':len(records),'token_account_opening_raw':opening,'known_case_incoming_raw':known,'other_incoming_raw':other,'outgoing_raw':out,'closing_raw':closing,'known_case_incoming_USDT':str(Decimal(known)/10**6),'other_incoming_USDT':str(Decimal(other)/10**6),'outgoing_USDT':str(Decimal(out)/10**6),'closing_USDT':str(Decimal(closing)/10**6),'exchange_receiver_token_account':D,'historical_receiver_owner':B,'attribution':'SUPPORTED by independent sources; on-chain transfer and token owner CONFIRMED','same_receiver_owner_as_U300':'Yes, different case-network sending wallet; no U300 receipt reanalysed','opaque_instructions':sum(r.get('instruction_type')=='opaque' for r in records),'fee_lamports_total':sum(a['fee_lamports'] for a in audit)}
(P/'summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
