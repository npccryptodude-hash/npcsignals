"""Offline verification of exact Ethereum/NEAR Intents/OmniBridge/Solana correspondence."""
import json,pathlib,datetime,base64,hashlib
from decimal import Decimal
P=pathlib.Path(__file__).parent;A=P/'access';V=P.parent
ETH='nep141:eth.omft.near';SOL='nep141:sol.omft.near';WRAP='nep141:wrap.near';TREASURY='0x2cff890f0378a11913b6129b2e97417a2c302680';PROGRAM='dahPEoZGXfyV58JqqH85okdHmpN8U2q8owgPUXSCPxe';ALPHABET='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
def load(label):return json.loads((A/(label+'.response.txt')).read_text())
def result(label):return load(label)['result']
def dump(name,a):(P/name).write_text(json.dumps(a,indent=2)+'\n')
def utc(n):return datetime.datetime.fromtimestamp(n,datetime.timezone.utc).isoformat().replace('+00:00','Z')
def units(n,d):return format(Decimal(n)/Decimal(10)**d,'f')
def b58decode(s):
 n=0
 for c in s:n=n*58+ALPHABET.index(c)
 return bytes(len(s)-len(s.lstrip('1')))+n.to_bytes((n.bit_length()+7)//8,'big')
def ethereum(prefix):
 t=result(prefix+'_eth_getTransactionByHash');r=result(prefix+'_eth_getTransactionReceipt');b=result(prefix+'_eth_getBlockByNumber')
 assert t['hash']==r['transactionHash'] and t['blockHash']==r['blockHash']==b['hash'] and t['blockNumber']==b['number']==r['blockNumber'] and int(r['status'],16)==1
 assert t['hash'] in [x if isinstance(x,str) else x['hash'] for x in b['transactions']]
 assert t['input']=='0x' and int(t['value'],16)==2000000000000000000 and r['logs']==[]
 return t,r,b
assert result('origin_eth_chainId')=='0x1' and result('solana_genesis')=='5eykt4UsFv8P8NJdTREpY1vzqKqZKvdpKuc147dw2N9d'
a=load('origin_address_status');sd=a['swapDetails'];qr=a['quoteResponse']['quoteRequest'];q=a['quoteResponse']['quote'];intent=sd['intentHashes'][0]
dt,dr,db=ethereum('deposit');st,sr,sb=ethereum('origin')
assert a['status']=='SUCCESS' and dt['hash']==sd['originChainTxHashes'][0]['hash'] and dt['to']==q['depositAddress'].lower()==st['from']
assert dt['from']==qr['refundTo'].lower() and st['to']==TREASURY and qr['originAsset']==ETH and qr['destinationAsset']==SOL
assert result('code_deposit')=='0x' and result('code_treasury')=='0x'
assert TREASURY in (A/'docs_treasury_md.response.txt').read_text().lower()
tokens={x['assetId']:x for x in load('token_list')};assert tokens[ETH]['decimals']==18 and tokens[SOL]['decimals']==9
# Actual NEAR results determine signers; RPC routing hints never determine account identity.
n0=result('archive_tx_0');n1=result('archive_tx_1')
for i,n in enumerate([n0,n1]):
 assert n['transaction']['hash']==sd['nearTxHashes'][i] and 'SuccessValue' in n['status']
 assert all('Failure' not in o['outcome']['status'] for o in [n['transaction_outcome']]+n['receipts_outcome'])
 assert n.get('final_execution_status','FINAL')=='FINAL'
def event_records(n):
 es=[]
 for o in n['receipts_outcome']:
  for l in o['outcome']['logs']:
   if l.startswith('EVENT_JSON:'):
    e=json.loads(l[len('EVENT_JSON:'):]);es.append({'executor_id':o['outcome']['executor_id'],'receipt_id':o['id'],'block_hash':o['block_hash'],**e})
 return es
e0=event_records(n0);e1=event_records(n1)
call0=n0['transaction']['actions'][0]['FunctionCall'];args0=json.loads(base64.b64decode(call0['args']));memo=json.loads(args0['memo'].split('BRIDGED_FROM:',1)[1]);case=json.loads(args0['msg'])['receiver_id']
assert n0['transaction']['signer_id']=='bridge-mng.near' and n0['transaction']['receiver_id']=='omft.near' and call0['method_name']=='ft_deposit'
assert memo['txHash']==dt['hash'] and memo['chainId']=='1' and memo['networkType']=='eth' and args0['amount']==sd['amountIn']==sd['depositedAmount']=='2000000000000000000'
mint=next(e for e in e0 if e['executor_id']=='intents.near' and e['event']=='mt_mint' and e['data'][0]['owner_id']==case);assert mint['data'][0]['token_ids']==[ETH] and mint['data'][0]['amounts']==[sd['amountIn']]
bridge_transfer=next(e for e in e0 if e['executor_id']=='eth.omft.near' and e['event']=='ft_transfer' and e['data'][0].get('memo')==args0['memo']);assert bridge_transfer['data'][0]['new_owner_id']=='intents.near'
call1=n1['transaction']['actions'][0]['FunctionCall'];args1=json.loads(base64.b64decode(call1['args']));signed_messages=[json.loads(s['payload']['message']) for s in args1['signed']]
assert call1['method_name']=='execute_intents' and n1['transaction']['signer_id']==n1['transaction']['receiver_id']=='intents.near'
assert {m['signer_id'] for m in signed_messages}=={'crux-solver.near','solver-priv-liq.near',case}
executed=next(e for e in e1 if e['executor_id']=='intents.near' and e['event']=='intents_executed');assert any(d['intent_hash']==intent and d['account_id']==case for d in executed['data'])
ce=[e for e in e1 if e['executor_id']=='intents.near' and any(d.get('intent_hash')==intent for d in e['data'])]
withdraw=next(e for e in ce if e['event']=='ft_withdraw')['data'][0];msg=json.loads(withdraw['msg'])
assert withdraw['token']=='sol.omft.near' and withdraw['receiver_id']=='omni.bridge.near' and withdraw['amount']==sd['amountOut']=='44473890045' and msg['recipient']=='sol:'+qr['recipient']
init_o=next(o for o in n1['receipts_outcome'] if o['outcome']['executor_id']=='omni.bridge.near' and any('InitTransferEvent' in l for l in o['outcome']['logs']))
init=json.loads(next(l for l in init_o['outcome']['logs'] if 'InitTransferEvent' in l))['InitTransferEvent']['transfer_message']
assert init['amount']==withdraw['amount'] and init['recipient']==msg['recipient'] and init['token']=='near:sol.omft.near' and init['sender']=='near:intents.near'
sol=result('solana_destination');sig=sd['destinationChainTxHashes'][0]['hash'];assert sol['transaction']['signatures'][0]==sig and sol['meta']['err'] is None
ix=sol['transaction']['message']['instructions'][0];raw=b58decode(ix['data']);assert ix['programId']==PROGRAM and raw[:8]==hashlib.sha256(b'global:finalize_transfer_sol').digest()[:8]
nonced=int.from_bytes(raw[8:16],'little');chain=raw[16];nonceo=int.from_bytes(raw[17:25],'little');out=int.from_bytes(raw[25:41],'little');assert chain==1 and nonced==init['destination_nonce']==437739 and nonceo==init['origin_nonce']==606162 and out==int(init['amount'])
assert raw[41]==1;strlen=int.from_bytes(raw[42:46],'little');fee_recipient=raw[46:46+strlen].decode();assert len(raw)==46+strlen+65 and fee_recipient=='omni-relayer.bridge.near'
assert ix['accounts'][3]==qr['recipient'];vault=ix['accounts'][4]
inners=[i for group in sol['meta']['innerInstructions'] for i in group['instructions']];transfer=next(i['parsed']['info'] for i in inners if i.get('parsed',{}).get('type')=='transfer' and i['parsed']['info']['destination']==qr['recipient']);assert transfer['source']==vault and transfer['lamports']==out
keys=[k['pubkey'] for k in sol['transaction']['message']['accountKeys']];j=keys.index(qr['recipient']);k=keys.index(vault);assert sol['meta']['postBalances'][j]-sol['meta']['preBalances'][j]==out and sol['meta']['preBalances'][k]-sol['meta']['postBalances'][k]==out
payer=keys[0];assert sol['transaction']['message']['accountKeys'][0]['signer'];assert sol['meta']['fee']==5000
# Exact fees and solver transfers in the executed receipt, distinct from quoted fee estimates.
transfers=next(e['data'] for e in e1 if e['event']=='mt_transfer' and e['executor_id']=='intents.near')
case_eth_transfers=[d for d in transfers if d['old_owner_id']==case and ETH in d['token_ids']]
eth_alloc=[{'recipient':d['new_owner_id'],'raw':d['amounts'][d['token_ids'].index(ETH)]} for d in case_eth_transfers];assert sum(int(x['raw']) for x in eth_alloc)==int(sd['amountIn'])
for app in qr['appFees']:
 actual=next(x for x in eth_alloc if x['recipient']==app['recipient']);assert int(actual['raw'])==int(sd['amountIn'])*app['fee']//10000
assert next(x for x in eth_alloc if x['recipient']=='crux-solver.near')['raw']=='1988998011000000000'
assert next(x for x in eth_alloc if x['recipient']=='7066024d3f20f94de601c003163367873cca78507eeca4df66d9be645f197f05')['raw']=='1989000000000'
case_sol_diffs=[d for e in ce if e['event']=='token_diff' for d in e['data'] if SOL in d['diff']];assert sum(int(d['diff'][SOL]) for d in case_sol_diffs)==out
fees={'input_ETH_allocation':eth_alloc,'app_fee_total_ETH':'0.011','app_fee_basis_points':55,'case_ETH_protocol_fee_raw':'1989000000000','case_ETH_protocol_fee':'0.000001989','SOL_received_in_case_token_diff_raw':'44473976022','SOL_spent_for_withdrawal_funding_raw':'85977','SOL_native_output_raw':str(out),'NEAR_native_fee_parameter_yocto':msg['native_token_fee'],'NEAR_native_fee_parameter':units(msg['native_token_fee'],24),'withdraw_fee_API_quote_lamports':sd['withdrawFee'],'refund_fee_API_quote_wei':sd['refundFee'],'Solana_transaction_network_fee_lamports':sol['meta']['fee'],'Ethereum_deposit_gas_fee_wei':str(int(dr['gasUsed'],16)*int(dr['effectiveGasPrice'],16)),'Ethereum_sweep_gas_fee_wei':str(int(sr['gasUsed'],16)*int(sr['effectiveGasPrice'],16)),'limitation':'Quote withdrawal fee 86107 lamports differs from observed SOL funding debit 85977; do not force equality. Native storage/bridge funding parameter is not independently proved fully consumed. No independent market spread or USD loss is asserted.'}
# Three core NEAR event blocks, independently fetched; historical RPC failures retained separately.
def block(label,h):
 b=result(label)['header'];assert b['hash']==h;return {'hash':h,'height':b['height'],'timestamp_nanosec':b['timestamp_nanosec'],'timestamp_UTC':utc(int(b['timestamp_nanosec'])//10**9)}
credit_block=block('near_block_'+mint['block_hash'],mint['block_hash']);settlement_block=block('near_block_retry_settlement',n1['transaction_outcome']['block_hash']);withdraw_block=block('near_block_retry_withdrawal',init_o['block_hash'])
evidence={'api_correlation_id':a['correlationId'],'intent_hash':intent,'deposit_address':dt['to'],'Ethereum_origin_transaction':dt['hash'],'Ethereum_sweep_transaction':st['hash'],'deposit_manager':'bridge-mng.near','NEAR_bridge_contract':'omft.near','NEAR_asset_contract':'eth.omft.near','NEAR_verifier':'intents.near','NEAR_case_account':case,'NEAR_deposit_transaction':n0['transaction']['hash'],'NEAR_settlement_transaction':n1['transaction']['hash'],'NEAR_transaction_submitter':n1['transaction']['signer_id'],'primary_solver_account':'crux-solver.near','withdrawal_funding_solver_account':'solver-priv-liq.near','NEAR_withdrawal_contract':'omni.bridge.near','OmniBridge_transfer':init,'Solana_program':PROGRAM,'Solana_signature':sig,'Solana_decoded_instruction':{'origin_chain_enum':chain,'origin_nonce':nonceo,'destination_nonce':nonced,'amount_lamports':out,'fee_recipient_account':fee_recipient,'signature_hex':raw[-65:].hex()},'Solana_transfer':transfer,'Solana_payer':payer,'Solana_vault':vault,'Solana_destination':qr['recipient'],'Solana_slot':sol['slot'],'Solana_timestamp_UTC':utc(sol['blockTime']),'NEAR_credit_block':credit_block,'NEAR_settlement_block':settlement_block,'NEAR_withdrawal_block':withdraw_block,'input_transaction_block':int(db['number'],16),'input_transaction_timestamp_UTC':utc(int(db['timestamp'],16)),'sweep_transaction_block':int(sb['number'],16),'sweep_timestamp_UTC':utc(int(sb['timestamp'],16)),'fees':fees,'NEAR_deposit_events':[mint,bridge_transfer],'NEAR_execution_events':ce,'signed_intent_messages':signed_messages,'NEAR_mt_transfers':transfers,'attribution_significance':'Exact protocol/account roles and publicly documented treasury endpoint only. Solver account labels do not identify a human or business operator, common control, custody relationship or final beneficiary. Internal case account is not independently assigned to the origin wallet owner.'}
common={'classification':'CONFIRMED','protocol_identifier':'NEAR Intents 1Click / OMFT / OmniBridge','intent_hash':intent,'correlation_id':a['correlationId'],'attribution_significance':evidence['attribution_significance']}
edges=[{**common,'edge_type':'Ethereum → NEAR deposit credit','source_transaction':dt['hash'],'destination_transaction':n0['transaction']['hash'],'source_chain':'Ethereum (1)','destination_chain':'NEAR mainnet','source_wallet':dt['from'],'source_deposit_address':dt['to'],'destination_protocol':'intents.near','destination_wallet':case,'asset_in':'native ETH','amount_in':'2','asset_out':ETH,'amount_out':'2','protocol_role':'OMFT deposit manager explicitly records original Ethereum transaction in BRIDGED_FROM memo; mint credits exact case account','fees':'Ethereum execution gas separately recorded; no credit deduction observed'},{**common,'edge_type':'NEAR → Solana withdrawal finalization','source_transaction':n1['transaction']['hash'],'destination_transaction':sig,'source_chain':'NEAR mainnet','destination_chain':'Solana mainnet','source_wallet':case,'source_protocol':'intents.near → omni.bridge.near','destination_wallet':qr['recipient'],'asset_in':SOL,'amount_in':units(out,9),'asset_out':'native SOL','amount_out':units(out,9),'origin_nonce':nonceo,'destination_nonce':nonced,'solver_accounts':['crux-solver.near','solver-priv-liq.near'],'protocol_role':'OmniBridge signed transfer payload matches both protocol nonces, amount and recipient','fees':fees}]
route={**common,'record_type':'composite Ethereum → Solana route; underlying edges are not separate additional losses','source_transaction':dt['hash'],'destination_transaction':sig,'source_wallet':dt['from'],'destination_wallet':qr['recipient'],'asset_in':'ETH','amount_in':'2','asset_out':'SOL','amount_out':units(out,9),'source_chain':'Ethereum (1)','destination_chain':'Solana mainnet','protocol_role':'NEAR Intents 1Click deposit, canonical intent execution and OmniBridge withdrawal','solver_accounts':['crux-solver.near','solver-priv-liq.near'],'settlement_transaction':n1['transaction']['hash'],'fees':fees,'evidence_files':['access/origin_address_status.response.txt','access/deposit_eth_getTransactionByHash.response.txt','access/deposit_eth_getTransactionReceipt.response.txt','access/deposit_eth_getBlockByNumber.response.txt','access/archive_tx_0.response.txt','access/archive_tx_1.response.txt','access/solana_destination.response.txt','access/solana_genesis.response.txt','access/docs_treasury_md.response.txt','access/omni_source_1.response.txt','access/omni_source_5.response.txt','access/omni_source_8.response.txt','access/omni_near_types.response.txt']}
rows=[{'ID':'F0481','record_type':'origin enrichment (existing F0157; not new loss)',**common,'transaction':dt['hash'],'source':dt['from'],'destination':dt['to'],'asset':'ETH','amount':'2','block':int(db['number'],16),'timestamp_UTC':utc(int(db['timestamp'],16))},{'ID':'F0482','record_type':'treasury sweep enrichment (existing F0158; not new loss)',**common,'transaction':st['hash'],'source':st['from'],'destination':st['to'],'asset':'ETH','amount':'2','service_role':'Receiving address independently documented as NEAR Intents treasury; no private custody/beneficiary inference'},{'ID':'F0483',**edges[0],'record_type':'cross-chain edge'}, {'ID':'F0484',**common,'record_type':'canonical NEAR intent settlement observation','transaction':n1['transaction']['hash'],'case_account':case,'solver_accounts':['crux-solver.near','solver-priv-liq.near'],'fees':fees,'block':settlement_block},{'ID':'F0485',**edges[1],'record_type':'cross-chain edge'},{'ID':'F0486',**route}]
prior=json.loads((V/'mayan_verification_2026_10_09/master_timeline_F0001_F0480.json').read_text())['rows'];assert len(prior)==480
for name,obj in [('protocol_correspondence.json',evidence),('cross_chain_edges.json',edges),('route_reconstruction.json',route),('transaction_ledger_F0481_F0486.json',rows),('master_timeline_F0001_F0486.json',{'notes':'Prior 480 objects preserved exactly. Composite route and two settlement edges describe one flow, not additive losses. Privacy Cash stays separate.','rows':prior+rows}),('verification_summary.json',{'latest_ID':'F0486','origin_reproduced':True,'destination_reproduced':True,'classification':'CONFIRMED','composite_routes':1,'underlying_cross_chain_edges':2,'ETH_input':'2','SOL_output':units(out,9),'canonical_NEAR_execution_reproduced':True,'both_OmniBridge_nonces_match':True,'prior_rows_unchanged':True,'remaining_gaps':['Complete upstream provenance and owner/control/custody/beneficiary attribution unresolved.','Solver account roles verified without independent human/business identity.','Standalone quote, signed-intent and MPC signature validation, deployed bytecode audit and consensus inclusion proof not performed.']})]:dump(name,obj)
print('PASS: exact Ethereum tx → NEAR credit/matching intent → OmniBridge nonce pair → finalized Solana transfer; fees reconcile; 480 prior rows unchanged')
