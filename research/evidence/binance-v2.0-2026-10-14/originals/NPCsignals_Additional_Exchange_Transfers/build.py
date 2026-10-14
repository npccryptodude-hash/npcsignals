import pathlib,json,datetime,re,hashlib,shutil
from decimal import Decimal
P=pathlib.Path(__file__).resolve().parent
W=['6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N','8zHcWujHhyJri3CRTcWUGmT5WSRdwW7xrns3WTTkPGvS']
columns=['id','signature','utc','slot','transaction_index','instruction_index','instruction_type','source','recipient','lamports','SOL','authority','signers','fee_payer','fee_lamports','source_pre_lamports','source_post_lamports','recipient_pre_lamports','recipient_post_lamports','token_mint','historical_token_owner','execution_result','finality','receipt_file','source_url']
statuses=json.loads((P/'candidate-finality.json').read_text());sigs=sorted(statuses,key=lambda s:json.loads((P/(s+'.json')).read_text())['blockTime']);rows=[];audits=[]
for n,sig in enumerate(sigs,1):
 t=json.loads((P/(sig+'.json')).read_text());keys=t['transaction']['message']['accountKeys'];addr=[k['pubkey'] for k in keys];m=t['meta'];sg=';'.join(k['pubkey'] for k in keys if k['signer']);payer=addr[0];utc=datetime.datetime.fromtimestamp(t['blockTime'],datetime.timezone.utc).isoformat();flow={a:0 for a in addr};flow[payer]-=m['fee']
 assert m['err'] is None and statuses[sig]['confirmationStatus']=='finalized' and statuses[sig]['err'] is None and statuses[sig]['slot']==t['slot']
 for i,ix in enumerate(t['transaction']['message']['instructions']):
  v=ix.get('parsed',{});v=v if isinstance(v,dict) else {};info=v.get('info',{});s=info.get('source','');d=info.get('destination','');amt=info.get('lamports');a=addr.index(s) if s else None;b=addr.index(d) if d else None
  if amt is not None:flow[s]-=amt;flow[d]+=amt
  r=[f'SC{n:03d}.I{i}',sig,utc,t['slot'],t.get('transactionIndex',''),f'outer:{i}',v.get('type','opaque'),s,d,amt if amt is not None else '',str(Decimal(amt)/10**9) if amt is not None else '',s if amt is not None else '',sg,payer,m['fee'],m['preBalances'][a] if a is not None else '',m['postBalances'][a] if a is not None else '',m['preBalances'][b] if b is not None else '',m['postBalances'][b] if b is not None else '','N/A native SOL','N/A native SOL','SUCCESS','finalized',sig+'.rpc.json','https://explorer.solana.com/tx/'+sig];rows.append([str(x) for x in r])
 for i,a in enumerate(addr):assert m['postBalances'][i]-m['preBalances'][i]==flow[a]
 audits.append({'id':f'SC{n:03d}','signature':sig,'accounts':[{'address':a,'pre_lamports':m['preBalances'][i],'post_lamports':m['postBalances'][i],'modeled_delta_lamports':flow[a]} for i,a in enumerate(addr)],'fee_lamports':m['fee'],'reconciliation':'PASS'})
 rows.append([str(x) for x in [f'SC{n:03d}.FEE',sig,utc,t['slot'],t.get('transactionIndex',''),'fee','transaction_fee',payer,'network',m['fee'],str(Decimal(m['fee'])/10**9),'',sg,payer,m['fee'],m['preBalances'][0],m['postBalances'][0],'','','N/A native SOL','N/A native SOL','SUCCESS','finalized',sig+'.rpc.json','https://explorer.solana.com/tx/'+sig]])
(P/'csv-rows.json').write_text(json.dumps([columns]+rows));(P/'exchange-ledger.json').write_text(json.dumps([dict(zip(columns,r)) for r in rows],indent=2));(P/'balance-audit.json').write_text(json.dumps(audits,indent=2))
registry=P/'registry';registry.mkdir(exist_ok=True);regkeys={}
registry_source=registry if list(registry.glob('*.js')) else P.parent/'exchange-deposit-pass'/'registry'
for f in registry_source.glob('*.js'):
 if f.parent!=registry:shutil.copyfile(f,registry/f.name)
 for key in re.findall(r'[1-9A-HJ-NP-Za-km-z]{32,44}',f.read_text()):regkeys.setdefault(key,[]).append(f.name)
allflows=[];scope=[]
for wi,w in enumerate(W):
 envelope=json.loads((P/(w+'-history.rpc.json')).read_text());ts=envelope['result']['data'];scope.append({'wallet':w,'receipt_count':len(ts),'earliest_utc':datetime.datetime.fromtimestamp(min(t['blockTime'] for t in ts),datetime.timezone.utc).isoformat(),'latest_utc':datetime.datetime.fromtimestamp(max(t['blockTime'] for t in ts),datetime.timezone.utc).isoformat(),'pagination_token':envelope['result'].get('paginationToken'),'terminal_page':not bool(envelope['result'].get('paginationToken'))})
 for t in ts:
  keys=t['transaction']['message']['accountKeys'];addr=[k['pubkey'] for k in keys];owner={};evidence={};groups=[('outer',t['transaction']['message']['instructions'])]+[('inner:'+str(g['index']),g['instructions']) for g in t['meta'].get('innerInstructions',[]) or []]
  for kind,items in groups:
   for j,ix in enumerate(items):
    parsed=ix.get('parsed',{});parsed=parsed if isinstance(parsed,dict) else {};info=parsed.get('info',{})
    if parsed.get('type','').startswith('initializeAccount') and info.get('account') and info.get('owner'):owner[info['account']]=info['owner'];evidence[info['account']]='historical initialization '+kind+':'+str(j)
  for side in ['preTokenBalances','postTokenBalances']:
   for b in t['meta'].get(side,[]):
    if b.get('owner'):owner[addr[b['accountIndex']]]=b['owner'];evidence[addr[b['accountIndex']]]=side+' owner field'
  for kind,items in groups:
   for j,ix in enumerate(items):
    parsed=ix.get('parsed',{});parsed=parsed if isinstance(parsed,dict) else {};info=parsed.get('info',{});s=info.get('source');d=info.get('destination')
    if not d or not (s==w or owner.get(s)==w) or t['meta']['err'] is not None:continue
    internal=owner.get(d)==w or d==w;exchange_matches=regkeys.get(d,[])+regkeys.get(owner.get(d,''),[])
    allflows.append({'wallet':w,'signature':t['transaction']['signatures'][0],'utc':datetime.datetime.fromtimestamp(t['blockTime'],datetime.timezone.utc).isoformat(),'slot':t['slot'],'instruction_index':kind+':'+str(j),'program_id':ix.get('programId'),'instruction_type':parsed.get('type'),'source':s,'source_owner':owner.get(s),'source_owner_evidence':evidence.get(s),'recipient':d,'recipient_owner':owner.get(d),'recipient_owner_evidence':evidence.get(d),'info':info,'classification':'INTERNAL_OWNER_MOVEMENT' if internal else 'UNRESOLVED external/service/program movement','registry_exact_candidates':exchange_matches})
(P/'discovery-movements.json').write_text(json.dumps(allflows,indent=2));(P/'scope.json').write_text(json.dumps(scope,indent=2))
transfers=[r for r in rows if r[6]=='transfer'];total=sum(int(r[9]) for r in transfers);summary={'verified_additional_transfers':len(transfers),'lamports_total':total,'SOL_total':str(Decimal(total)/10**9),'fees_total_lamports':sum(a['fee_lamports'] for a in audits),'discovery_receipts':sum(s['receipt_count'] for s in scope),'discovery_outgoing_or_internal_movements':len(allflows),'internal_owner_movements':sum(r['classification']=='INTERNAL_OWNER_MOVEMENT' for r in allflows),'registry_candidate_matches':[r for r in allflows if r['registry_exact_candidates']],'same_wallet_and_receiver_as_first_checkpoint':True,'independent_second_exchange_or_wallet_branch':False}
(P/'summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
