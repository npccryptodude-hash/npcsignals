"""Offline G013 deterministic message, signature and receipt-graph verification."""
import pathlib,json,gzip,base64,hashlib,datetime
import rlp
from eth_hash.auto import keccak
from eth_keys import keys
R=pathlib.Path(__file__).resolve().parent;P=R.parent/'gamdom-incident-2026-10-g012'
BASE='cc8262b6891648934a2114495c1542816cb51b53'
LOCKER='0x233c5370ccfb3cd7409d9a3fb98ab94de94cb4cd'
HOT='v2_1.omni.hot.tg';OMFT='eth-0x6b175474e89094c44da98b954eedeac495271d0f.omft.near'
B='0xe5686aae44d392aa6a0637fd38393859502f8667';TOKEN='0x55d398326f99059ff775485246999027b3197955'
SWEEPS=['0x241cc0f33d586d99c2cf1d1382b09fc71129efef29069c5bbb92eb2f26a46123','0xd64d7ef1322cbfa531f71e9dafa937682a0a060ec0de57980840fd4f4b0d4cdc']
DEPS=['7ANgmgCrZnot8uA2NRuLQxCmrtpR5n2E6aURrimmDbvF','HFrVzrvRmLUF4FNd1UyiaMRD9JwCWSS5jnpgsCBNLQkA']
INTENTS=['3CucqT6YmivRFpNMtgsiuR43d2JXJcBuMLUYU9vHzjV6','7dbo8A2xAkge8A6q139CsjcKd7rTHrK5U8aSyMxRMNiT']
ALPHABET='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
def b58(s):
 n=0
 for c in s:n=n*58+ALPHABET.index(c)
 return b'\0'*(len(s)-len(s.lstrip('1')))+n.to_bytes((n.bit_length()+7)//8,'big')
def hx(b):return '0x'+b.hex()
def n(x):return int(x,16)
def num(d,i):return int.from_bytes(d[i:i+32],'big')
def dyn(d,i):return d[i+32:i+32+num(d,i)]
def res(e,k):return e[k]['response']['result']
def call(e,k):return json.loads(bytes(res(e,k)['result']))
def records():
 f=R/'acquisition_archive.json.gz'
 return json.loads(gzip.decompress(f.read_bytes())) if f.exists() else {p.stem:json.loads(p.read_text()) for p in (R/'evidence').glob('*.json')}
def old():return json.loads(gzip.decompress((P/'acquisition_archive.json.gz').read_bytes()))
def receipt(e,rid):
 for key in ['receipt_'+rid,'fastnear_receipt_'+rid]:
  r=e.get(key,{}).get('response',{}).get('result')
  if isinstance(r,dict) and r.get('receipt_id')==rid:return r
 raise AssertionError('Missing receipt '+rid)
def tx_signature(t):
 assert n(t['type'])==1 and n(t['chainId'])==56
 access=[[bytes.fromhex(x['address'][2:]),[bytes.fromhex(k[2:]) for k in x['storageKeys']]] for x in t['accessList']]
 body=[n(t['chainId']),n(t['nonce']),n(t['gasPrice']),n(t['gas']),bytes.fromhex(t['to'][2:]),n(t['value']),bytes.fromhex(t['input'][2:]),access]
 parity=n(t['v']);sig=keys.Signature(vrs=(parity,n(t['r']),n(t['s'])));digest=keccak(b'\1'+rlp.encode(body));pub=sig.recover_public_key_from_msg_hash(digest)
 raw=b'\1'+rlp.encode(body+[parity,n(t['r']),n(t['s'])]);assert hx(keccak(raw))==t['hash'] and pub.to_address()==t['from']
 return {'signing_digest':hx(digest),'recovered_signer':pub.to_address(),'public_key':pub.to_hex(),'signed_envelope':hx(raw),'valid':True}
def derive():
 e=records();o=old();prior=json.loads((P/'decoded_execution_ledger.json').read_text());source=[];attest=[];near=[];payouts=[];ids=[];financial=[]
 s=e['sourcify_locker']['body'];assert s['address'].lower()==LOCKER and str(s['chainId'])=='56' and not s['proxyResolution']['isProxy']
 contracts=[{'chain':'BNB','address':LOCKER,'role':'Observed source MetaWallet locker','runtime_match_record':s['runtimeMatch'],'compiler':s['compilation'],'sourcify_deployment_metadata':s['deployment'],'historical_runtime_sha256':hashlib.sha256(bytes.fromhex(s['runtimeBytecode']['onchainBytecode'][2:])).hexdigest(),'historical_runtime_matches':2,'source':'sourcify_locker','local_recompilation':False}]
 for account,codekey,accountkey,secondkey in [(HOT,'fastnear_view_code_'+HOT,'fastnear_view_account_'+HOT,'hot_account_route2'),(OMFT,'fastnear_view_code_'+OMFT,'fastnear_view_account_'+OMFT,'omft_account_route2')]:
  c=base64.b64decode(res(e,codekey)['code_base64']);state=res(e,accountkey);assert hashlib.sha256(c).digest()==b58(state['code_hash']) and res(e,secondkey)['code_hash']==state['code_hash']
  contracts.append({'chain':'NEAR','account':account,'role':'HOT NEP-245 representation' if account==HOT else 'DAI OMFT token and burn interface','wasm_sha256':hashlib.sha256(c).hexdigest(),'onchain_code_hash':state['code_hash'],'first_state_block':state['block_height'],'second_state_block':res(e,secondkey)['block_height'],'same_code_hash_at_both':True,'wasm_bytes_source':codekey,'verified_source_equivalence':'NOT ASSESSED'})
 assert call(e,'omft_owner')=='omft.near'
 contracts[-1]['historical_owner_get']='omft.near'
 for i,h in enumerate(SWEEPS):
  p=prior[i];r=res(e,'receipt_'+h);t=res(e,'tx_'+h);header=res(e,'block_'+h);block=n(r['blockNumber'])
  assert n(r['status'])==1 and r['blockHash']==t['blockHash']==header['hash'] and t['hash']==h and r['from']==t['from']==p['deposit_address'] and t['to']==LOCKER
  assert res(e,'evm_code_'+p['deposit_address']+'_'+str(p['source_block']))=='0x'
  contracts.append({'chain':'BNB','address':p['deposit_address'],'role':'Order receiver and locker-deposit signer','block':p['source_block'],'code':'0x','limits':'Selected historical code state, not lifetime account classification'})
  assert res(e,'sweep_receiver_code_'+h)==s['runtimeBytecode']['onchainBytecode']
  event=next(l for l in r['logs'] if l['address']==LOCKER and l['topics'][0]==hx(keccak(b'NewTransfer(uint128,uint128,bytes,bytes)')))
  d=bytes.fromhex(event['data'][2:]);nonce,amount=num(d,0),num(d,32);token,receiver=dyn(d,num(d,64)),dyn(d,num(d,96))
  assert hx(token)==TOKEN and amount==int(p['deposit_raw'])
  inp=bytes.fromhex(t['input'][10:]);assert t['input'][:10]==hx(keccak(b'deposit(bytes,address,uint128)')[:4])
  assert dyn(inp,num(inp,0))==receiver and hx(inp[44:64])==TOKEN and num(inp,64)==amount
  transfers=[l for l in r['logs'] if l['address']==TOKEN and l['topics'][0].startswith('0xddf252ad')];assert len(transfers)==1 and n(transfers[0]['data'])==amount
  assert '0x'+transfers[0]['topics'][1][-40:]==t['from'] and '0x'+transfers[0]['topics'][2][-40:]==LOCKER
  nr=res(o,'near_tx_'+DEPS[i]);args=json.loads(base64.b64decode(nr['transaction']['actions'][0]['FunctionCall']['args']))
  assert int(args['nonce'])==nonce and int(args['chain_id'])==56 and int(args['amount'])==amount and b58(args['contract_id'])==token
  receiver_text=json.dumps(args['deposit_call_args'],separators=(',',':'),ensure_ascii=False);assert hashlib.sha256(receiver_text.encode()).digest()==receiver
  raw=rlp.encode([nonce.to_bytes(16,'big'),(56).to_bytes(8,'big'),token,receiver,amount.to_bytes(16,'big')]);digest=hashlib.sha256(raw).digest()
  raw_return=bytes.fromhex(res(e,'messageRaw_'+str(nonce))[2:]);assert dyn(raw_return,num(raw_return,0))==raw
  assert res(e,'storedHash_'+str(nonce))==hx(digest) and n(res(e,'priorHash_'+str(nonce)))==0 and n(res(e,'chainId_'+str(nonce)))==56
  pubhex=call(e,'hot_public_key_chain56' if i==0 else 'hot_public_key_chain56_route2');pub=keys.PublicKey(bytes.fromhex(pubhex));signature=b58(args['signature']);assert len(signature)==64
  assert keys.NonRecoverableSignature(signature_bytes=signature).verify_msg_hash(digest,pub)
  assert call(e,'hot_get_locker_address' if i==0 else 'hot_locker_route2').lower()==LOCKER
  pre=127436959 if i==0 else 127437352
  assert n(res(e,'deposit_balance_'+t['from']+'_'+str(pre)))==0 and n(res(e,'deposit_balance_'+t['from']+'_'+str(block)))==0
  source.append({'route':i+1,'original_settlement':p['source_transaction'],'deposit_address':t['from'],'bridge_deposit_transaction':h,'block':block,'transaction_index':n(r['transactionIndex']),'utc':datetime.datetime.fromtimestamp(n(header['timestamp']),datetime.timezone.utc).isoformat(),'locker':LOCKER,'canonical_token':TOKEN,'decimals':18,'nonce':str(nonce),'amount_raw':str(amount),'receiver_hash':hx(receiver),'receiver_serialization_utf8':receiver_text,'source_message_rlp':hx(raw),'source_message_sha256':hx(digest),'storage_before_raw':res(e,'priorHash_'+str(nonce)),'storage_after_raw':res(e,'storedHash_'+str(nonce)),'transaction_signature':tx_signature(t),'gas_fee_wei':str(n(r['gasUsed'])*n(r['effectiveGasPrice'])),'native_call_value_wei':str(n(t['value'])),'source_to_NEAR_edge':'CONFIRMED','limit':'Exact on-chain nonce/asset/amount/receiver commitment plus valid deposit attestation and successful NEAR execution. No independent MPC threshold audit or consensus proof replay.'})
  attest.append({'route':i+1,'near_deposit_transaction':DEPS[i],'algorithm':'secp256k1 ECDSA, 64-byte r||s, direct SHA-256 digest verification','signature_base58':args['signature'],'signature_hex':hx(signature),'r':hx(signature[:32]),'s':hx(signature[32:]),'recovery_id':None,'message_rlp':hx(raw),'message_sha256':hx(digest),'historical_chain56_public_key':pubhex,'derived_key_address':pub.to_address(),'verification':True,'authority_source':'Historical v2_1.omni.hot.tg get_public_key(chain_id=56)','authorized_key_state_level':'CONFIRMED getter state; internal verification/source equivalence not independently recompiled','locker_withdraw_verify_address':'0x'+res(e,'verifyAddress_'+str(nonce))[-40:],'quorum_and_validator_roster':'NOT ASSESSED','replay_scope':'Message binds source chain 56, nonce, token, receiver hash and amount; locker deployment address is not inside signed bytes. Global/cross-deployment replay resistance not established.'})
  nr2=res(o,'near_tx_'+INTENTS[i]);m={q['id']:q for q in nr2['receipts_outcome']};withdraw_id=next(q['id'] for q in nr2['receipts_outcome'] if q['outcome']['executor_id']==OMFT);wr=receipt(e,withdraw_id);fc=wr['receipt']['Action']['actions'][0]['FunctionCall'];wa=json.loads(base64.b64decode(fc['args']))
  assert wr['predecessor_id']=='intents.near' and wr['receiver_id']==OMFT and fc['method_name']=='ft_transfer' and wa['memo'].lower()=='withdraw_to:'+B
  api=res(e,'omft_status_raw_by_tx_'+INTENTS[i]);data=api['data'];assert api['status']=='COMPLETED' and data['tx_hash']==INTENTS[i] and data['transfer_tx_hash']==p['destination_transaction'] and data['withdraw_amount']==p['destination_amount_raw']
  account=json.loads(args['deposit_call_args']['msg'])['receiver_id'];assert data['account_id']==account and int(wa['amount'])==int(data['withdraw_amount'])+int(data['withdrawal_fee'])
  dest=p['destination_transaction'];dt=res(o,'eth_tx_'+dest);dr=res(o,'eth_receipt_'+dest)
  assert res(e,'evm_code_'+dt['from']+'_'+str(p['destination_block']))=='0x' and len(bytes.fromhex(dt['input'][2:]))==68
  contracts.append({'chain':'Ethereum','address':dt['from'],'role':'Observed DAI treasury payout initiator','block':p['destination_block'],'code':'0x','first_party_operational_label':'NEAR Intents treasury in retrieved current official documentation; not historical human ownership proof'})
  payouts.append({'route':i+1,'near_intent_execution':INTENTS[i],'withdrawal_action_receipt_id':withdraw_id,'near_withdrawal_amount_raw':wa['amount'],'withdrawal_recipient':B,'omft_api_mapping':data,'api_numeric_amount_ignored':True,'ethereum_transaction':dest,'ethereum_block':p['destination_block'],'ethereum_sender_code':'0x','ethereum_sender':dt['from'],'ethereum_token_sender':dt['from'],'token':p['destination_token'],'receiver':B,'payout_raw':p['destination_amount_raw'],'input':dt['input'],'receipt_log_count':len(dr['logs']),'onchain_withdrawal_identifier_in_ethereum':None,'offchain_payout_instruction_or_signature':None,'withdrawal_to_payout_edge':'SUPPORTED','full_route':'SUPPORTED'})
  ids.append({'route':i+1,'cow_order_uid':p['order_uid'],'source_bridge_nonce':str(nonce),'source_message_sha256':hx(digest),'source_receiver_sha256':hx(receiver),'near_deposit_transaction_hash':DEPS[i],'near_intent_transaction_hash':INTENTS[i],'intent_hash':p['protocol_status']['swapDetails']['intentHashes'][0],'withdrawal_action_receipt_id':withdraw_id,'ethereum_transaction_hash':dest,'types_are_distinct':True})
  financial.append({'route':i+1,'decimals':18,'source_usdt_principal_raw':p['source_principal_raw'],'settlement_receiver_usdt_raw':p['deposit_raw'],'actual_locker_usdt_raw':str(amount),'source_difference_usdt_raw':p['source_sell_buy_difference_raw'],'near_source_asset_raw':str(amount),'near_dai_output_and_withdrawal_raw':wa['amount'],'omft_reported_dai_fee_raw':data['withdrawal_fee'],'ethereum_dai_receipt_raw':data['withdraw_amount'],'source_residual_raw':str(int(p['source_principal_raw'])-amount-int(p['source_sell_buy_difference_raw'])),'dai_residual_after_reported_fee_raw':str(int(wa['amount'])-int(data['withdrawal_fee'])-int(data['withdraw_amount'])),'verified_unauthorized_loss_raw':None,'cross_asset_loss_residual':None})
 # Expand all 24 outcome receipts from G012, including data/refund receipts.
 for k,v in o.items():
  if not k.startswith('near_tx_'):continue
  nr=v['response']['result'];outcomes={x['id']:x for x in nr['receipts_outcome']};roots=nr['transaction_outcome']['outcome']['receipt_ids'];visited=set();todo=list(roots)
  while todo:
   rid=todo.pop()
   if rid in visited:continue
   assert rid in outcomes;visited.add(rid);todo+=outcomes[rid]['outcome']['receipt_ids']
  assert visited==set(outcomes)
  for rid in sorted(outcomes):
   detail=receipt(e,rid);assert detail['receiver_id']==outcomes[rid]['outcome']['executor_id']
   assert 'Failure' not in outcomes[rid]['outcome']['status']
   near.append({'transaction_hash':nr['transaction']['hash'],'receipt_id':rid,'parent_receipt_ids':[x for x,y in outcomes.items() if rid in y['outcome']['receipt_ids']],'is_transaction_root':rid in roots,'detail':detail,'outcome':outcomes[rid]})
 assert len(near)==24 and all(x['source_residual_raw']==x['dai_residual_after_reported_fee_raw']=='0' for x in financial)
 return {'bridge_contract_register':contracts,'source_deposit_proofs':source,'attestation_verification':attest,'near_receipt_proofs':near,'ethereum_payout_proofs':payouts,'message_identifier_register':ids,'financial_reconciliation':financial}
if __name__=='__main__':
 for name,data in derive().items():(R/(name+'.json')).write_text(json.dumps(data,indent=2)+'\n')
