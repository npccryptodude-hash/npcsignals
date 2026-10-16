"""Deterministic order/ABI decoder. Python 3 + eth-hash[pycryptodome], eth-keys."""
import json,gzip,hashlib,pathlib,sys,base64
from eth_hash.auto import keccak
from eth_keys import keys
R=pathlib.Path(__file__).resolve().parent
BASE='1d057aa9456d2d40401683438cf0468a5cb969cf'
B='0xe5686aae44d392aa6a0637fd38393859502f8667'
SET='0x9008d19f58aabd9ed0d60971565aa8510560ab41'
TOKEN='0x55d398326f99059ff775485246999027b3197955'
DAI='0x6b175474e89094c44da98b954eedeac495271d0f'
H=['0xe4eea89ea32d675baa724d2e3926ffd3d4fbbe8d4f73ce381799bf9550a92347','0xcda9343de4eb5ad1e96d210d3e215bdf55cb33fba1c5f3fe3a6456afbe6781d2']
PRESIGN='0xf7e40d1d02ef78a0c9c898b31d466cb29918f91532eac712c88bff4c7b2afb2a'
def records():
 p=R/'acquisition_archive.json.gz'
 return json.loads(gzip.decompress(p.read_bytes())) if p.exists() else {p.stem:json.loads(p.read_text()) for p in (R/'evidence').glob('*.json')}
def old():return json.loads(gzip.decompress((R.parent/'gamdom-incident-2026-10-g011/rpc_archive.json.gz').read_bytes()))
def n(x):return int(x,16)
def w(x):return x.to_bytes(32,'big')
def a(x):return bytes.fromhex(x[2:]).rjust(32,b'\0')
def hx(x):return '0x'+x.hex()
def word(d,i):return d[i:i+32]
def num(d,i):return int.from_bytes(word(d,i),'big')
def addr(d,i):return hx(word(d,i)[12:])
def dyn(d,i):return d[i+32:i+32+num(d,i)]
def result(e,k):return e[k]['response']['result']
def transfer(l):
 return {'sender':'0x'+l['topics'][1][-40:],'recipient':'0x'+l['topics'][2][-40:],'raw_amount':str(n(l['data'])),'token':l['address'],'log_index':n(l['logIndex'])}
def events(r,topic):return [l for l in r['logs'] if l['address']==SET and l['topics'][0]==hx(keccak(topic.encode()))]
def near_events(r):
 return [{'executor':o['outcome']['executor_id'],'receipt_id':o['id'],**json.loads(l[11:])} for o in r['receipts_outcome'] for l in o['outcome']['logs'] if l.startswith('EVENT_JSON:')]
def derive():
 e=records();o=old();s=e['sourcify_v2']['body']
 assert s['chainId']=='56' or s['chainId']==56
 assert s['address'].lower()==SET and s['runtimeMatch']=='exact_match' and not s['proxyResolution']['isProxy']
 domain=keccak(keccak(b'EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)')+keccak(b'Gnosis Protocol')+keccak(b'v2')+w(56)+a(SET))
 assert hx(domain)==result(e,'bnb_domain_separator')
 orders=[];executions=[];nearrows=[]
 for ix,h in enumerate(H):
  r=result(o,'receipt_'+h);t=result(o,'tx_'+h);block=n(r['blockNumber'])
  assert n(r['status'])==1 and t['to']==SET and t['blockHash']==r['blockHash']
  assert result(e,'bnb_settlement_code_'+str(block))==s['runtimeBytecode']['onchainBytecode']
  solver=events(r,'Settlement(address)');assert len(solver)==1 and '0x'+solver[0]['topics'][1][-40:]==t['from']
  d=bytes.fromhex(t['input'][10:]);assert t['input'][:10]=='0x13d79a0b'
  tp=num(d,0);tokens=[addr(d,tp+32+j*32) for j in range(num(d,tp))]
  cp=num(d,32);prices=[str(num(d,cp+32+j*32)) for j in range(num(d,cp))]
  ar=num(d,64);assert num(d,ar)==1
  p=ar+32+num(d,ar+32)
  fields=['sellTokenIndex','buyTokenIndex','receiver','sellAmount','buyAmount','validTo','appData','feeAmount','flags','executedAmount','signature']
  trade={k:num(d,p+j*32) for j,k in enumerate(fields)}
  trade.update(receiver=addr(d,p+64),appData=hx(word(d,p+192)),signature=hx(dyn(d,p+num(d,p+320))))
  flags=trade['flags'];scheme=['eip712','ethsign','eip1271','presign'][flags>>5]
  kind='buy' if flags&1 else 'sell';sellbal='erc20' if not flags&8 else ('internal' if flags&4 else 'external');buybal='internal' if flags&16 else 'erc20'
  order={'sellToken':tokens[trade['sellTokenIndex']],'buyToken':tokens[trade['buyTokenIndex']],'receiver':trade['receiver'],'sellAmount':str(trade['sellAmount']),'buyAmount':str(trade['buyAmount']),'validTo':trade['validTo'],'appData':trade['appData'],'feeAmount':str(trade['feeAmount']),'kind':kind,'partiallyFillable':bool(flags&2),'sellTokenBalance':sellbal,'buyTokenBalance':buybal}
  struct=bytes.fromhex('d5a25ba2e97094ad7d83dc28a6572da797d6b3e7fc6663bd93efb789fc17e489')+a(order['sellToken'])+a(order['buyToken'])+a(order['receiver'])+w(trade['sellAmount'])+w(trade['buyAmount'])+w(trade['validTo'])+bytes.fromhex(trade['appData'][2:])+w(trade['feeAmount'])+keccak(kind.encode())+w(int(bool(flags&2)))+keccak(sellbal.encode())+keccak(buybal.encode())
  digest=keccak(b'\x19\x01'+domain+keccak(struct));sig=bytes.fromhex(trade['signature'][2:])
  owner=hx(sig) if scheme=='presign' else keys.Signature(signature_bytes=sig[:64]+bytes([sig[64]-27])).recover_public_key_from_msg_hash(digest).to_address()
  assert owner==B
  uid=hx(digest+bytes.fromhex(owner[2:])+trade['validTo'].to_bytes(4,'big'))
  ev=events(r,'Trade(address,address,address,uint256,uint256,uint256,bytes)');assert len(ev)==1
  l=ev[0];ed=bytes.fromhex(l['data'][2:]);assert hx(dyn(ed,num(ed,160)))==uid and '0x'+l['topics'][1][-40:]==owner
  assert addr(ed,0)==order['sellToken'] and addr(ed,32)==order['buyToken']
  sell,buy,fee=[num(ed,j*32) for j in [2,3,4]]
  api=e['order_bnb_'+uid]['body'];assert all(api[k]==v for k,v in order.items())
  assert api['signingScheme']==scheme and int(api['executedSellAmount'])==sell and int(api['executedBuyAmount'])==buy
  assert hx(keccak(api['fullAppData'].encode()))==order['appData']
  bridging=json.loads(api['fullAppData'])['metadata']['bridging'];q=json.loads(bridging['quoteBody'])
  transfers=[transfer(l) for l in r['logs'] if l['address']==TOKEN and l['topics'][0]==hx(keccak(b'Transfer(address,address,uint256)'))]
  assert sum(int(l['raw_amount']) for l in transfers if l['sender']==B)-sum(int(l['raw_amount']) for l in transfers if l['recipient']==B)==sell
  assert sum(int(l['raw_amount']) for l in transfers if l['recipient']==order['receiver'])==buy
  api2=e['near_status_'+order['receiver']]['body'];sd=api2['swapDetails']
  assert api2['status']=='SUCCESS' and sd['originChainTxHashes'][0]['hash']==h and int(sd['depositedAmount'])==buy
  assert api2['quoteResponse']['quote']['depositAddress'].lower()==order['receiver'] and api2['quoteResponse']['quoteRequest']['recipient'].lower()==B
  dest=sd['destinationChainTxHashes'][0]['hash'];dr=result(e,'eth_receipt_'+dest);dt=result(e,'eth_tx_'+dest)
  dl=[transfer(l) for l in dr['logs'] if l['address']==DAI and l['topics'][0]==hx(keccak(b'Transfer(address,address,uint256)'))]
  assert n(dr['status'])==1 and len(dl)==1 and dl[0]['recipient']==B and dl[0]['raw_amount']==sd['amountOut']
  assert dt['to']==DAI and len(bytes.fromhex(dt['input'][2:]))==68 and dt['input'][:10]=='0xa9059cbb'
  assert dt['blockHash']==dr['blockHash']==result(e,'eth_block_'+str(n(dr['blockNumber'])))['hash']
  nrs=[result(e,'near_tx_'+nh) for nh in sd['nearTxHashes']]
  for nr in nrs:
   assert nr['final_execution_status']=='FINAL' and 'SuccessValue' in nr['status']
   assert all('Failure' not in z['outcome']['status'] for z in nr['receipts_outcome'])
  nes=[near_events(nr) for nr in nrs]
  mint=next(x for x in nes[0] if x['executor']=='intents.near' and x['event']=='mt_mint')['data'][0]
  assert mint['amounts']==[str(buy)]
  ne=next(x for x in nes[1] if x['event']=='ft_withdraw' and x['data'][0]['intent_hash']==sd['intentHashes'][0])['data'][0]
  assert ne['account_id']==mint['owner_id'] and ne['memo'].lower()=='withdraw_to:'+B and ne['token']=='eth-'+DAI+'.omft.near'
  # The NEAR withdrawal includes a separately reported 0.3 DAI withdrawal fee.
  assert int(ne['amount'])==int(sd['amountOut'])+int(sd['withdrawFee'])
  diff=next(x for x in nes[1] if x['event']=='token_diff' and x['data'][0]['intent_hash']==sd['intentHashes'][0])['data'][0]
  assert diff['account_id']==mint['owner_id'] and int(diff['diff'][q['originAsset']])==-buy
  assert int(diff['diff'][q['destinationAsset']])==int(ne['amount'])
  orders.append({'order_uid':uid,'order_digest':hx(digest),'chain_id':56,'domain_separator':hx(domain),'owner':owner,'signing_scheme':scheme,'recovered_eip712_signer':owner if scheme=='eip712' else None,'trade_calldata':trade,'order':order,'full_app_data':api['fullAppData'],'app_data_keccak_verified':True,'bridging':bridging,'quote':q,'evidence_level':'CONFIRMED'})
  if scheme=='eip712':
   pub=keys.Signature(signature_bytes=sig[:64]+bytes([sig[64]-27])).recover_public_key_from_msg_hash(digest)
   orders[-1]['signature_verification']={'r':hx(sig[:32]),'s':hx(sig[32:64]),'v':sig[64],'recovered_public_key':pub.to_hex(),'valid':True}
   prior=json.loads((R.parent/'gamdom-incident-2026-10-g011/signature_verification.json').read_text())
   assert any(x['recovered_public_key'].lower()==pub.to_hex().lower() and x['recovered_signer'].lower()==B for x in prior)
  executions.append({'source_transaction':h,'source_block':block,'source_transaction_initiator':t['from'],'source_transaction_index':n(r['transactionIndex']),'order_uid':uid,'tokens':tokens,'clearing_prices':prices,'source_transfers':transfers,'source_principal_raw':str(sell),'deposit_raw':str(buy),'onchain_trade_fee_raw':str(fee),'source_sell_buy_difference_raw':str(sell-buy),'api_executed_fee_raw':api['executedFee'],'source_transaction_gas_fee_wei':str(n(r['gasUsed'])*n(r['effectiveGasPrice'])),'deposit_address':order['receiver'],'protocol_status':api2,'destination_transaction':dest,'destination_block':n(dr['blockNumber']),'destination_initiator':dt['from'],'destination_token':DAI,'destination_amount_raw':sd['amountOut'],'destination_receiver':B,'destination_gas_fee_wei':str(n(dr['gasUsed'])*n(dr['effectiveGasPrice'])),'route_evidence_level':'SUPPORTED','route_limitation':'Unique deposit-address mapping is primary protocol API evidence, corroborated by source/destination receipts and NEAR intents. No single consensus-verifiable identifier binds all three chains; Ethereum transfer has no order UID.'})
  for nr,evs in zip(nrs,nes):
   bh=nr['transaction_outcome']['block_hash'];header=result(e,'near_block_'+bh)['header'];assert header['hash']==bh
   nearrows.append({'transaction_hash':nr['transaction']['hash'],'block_height':header['height'],'block_hash':bh,'timestamp_nanosec':header['timestamp_nanosec'],'signer_id':nr['transaction']['signer_id'],'receiver_id':nr['transaction']['receiver_id'],'events':evs,'decoded_actions':[{'method_name':x['FunctionCall']['method_name'],'args':json.loads(base64.b64decode(x['FunctionCall']['args']))} for x in nr['transaction']['actions'] if 'FunctionCall' in x]})
 # Exact UID 1 was pre-signed in the frozen G011 transaction.
 pr=result(o,'receipt_'+PRESIGN);pt=result(o,'tx_'+PRESIGN)
 pe=events(pr,'PreSignature(address,bytes,bool)');assert len(pe)==1
 pd=bytes.fromhex(pe[0]['data'][2:]);assert hx(dyn(pd,num(pd,0)))==orders[0]['order_uid'] and num(pd,32)==1
 assert '0x'+pe[0]['topics'][1][-40:]==B and pt['from']==pt['to']==B
 assert n(result(e,'presign_state_127436946'))==0
 for block in [127436947,127436960]:assert result(e,'presign_state_'+str(block))==hx(keccak(b'GPv2Signing.Scheme.PreSign'))
 trace=result(e,'presign_call_trace');assert trace['from']==trace['to']==B and trace['input']==pt['input'] and not trace.get('error')
 call=next(x for x in trace['calls'] if x['to']==SET);assert call['from']==B and not call.get('error')
 cd=bytes.fromhex(call['input'][10:]);assert call['input'][:10]==hx(keccak(b'setPreSignature(bytes,bool)')[:4]) and hx(dyn(cd,num(cd,0)))==orders[0]['order_uid'] and num(cd,32)==1
 assert result(o,'B_code_127436946')=='0xef010063c0c19a282a1b52b07dd5a65b58948a07dae32b'
 totals={'source_principal_usdt_raw':str(sum(int(x['source_principal_raw']) for x in executions)),'source_deposit_usdt_raw':str(sum(int(x['deposit_raw']) for x in executions)),'source_difference_usdt_raw':str(sum(int(x['source_sell_buy_difference_raw']) for x in executions)),'destination_dai_raw':str(sum(int(x['destination_amount_raw']) for x in executions)),'verified_unauthorized_loss_raw':None,'unknown_consideration_raw':None,'cross_asset_loss_or_fee_residual':None,'new_distinct_transactions':4,'existing_EVM_transactions_reused':5}
 balances=[]
 for x in executions:
  block=x['destination_block'];before=n(result(e,'eth_dai_balance_'+str(block-1)));after=n(result(e,'eth_dai_balance_'+str(block)))
  logs={l['logIndex']:l for i in [1,2] for l in result(e,'eth_dai_block_logs_'+str(block)+'_'+str(i))}
  rows=[transfer(l) for l in sorted(logs.values(),key=lambda l:n(l['logIndex']))];running=before;local=None
  for l in rows:
   if logs[hex(l['log_index'])]['transactionHash']==x['destination_transaction'] and local is None:local=running
   running+=(int(l['raw_amount']) if l['recipient']==B else 0)-(int(l['raw_amount']) if l['sender']==B else 0)
  assert running==after
  balances.append({'block':block,'block_opening_raw':str(before),'immediate_pre_receipt_raw':str(local),'block_closing_raw':str(after),'ordered_transfers':rows,'residual_raw':'0'})
 authorization={'presign_transaction':PRESIGN,'order_uid':orders[0]['order_uid'],'delegated_code_at_prior_block':result(o,'B_code_127436946'),'trace_verified_setPreSignature_call':call,'prior_state_raw':result(e,'presign_state_127436946'),'after_state_raw':result(e,'presign_state_127436947'),'at_execution_state_raw':result(e,'presign_state_127436960'),'second_order_eip712_recovered_owner':orders[1]['recovered_eip712_signer'],'human_consent':'UNRESOLVED'}
 return {'settlement_order_register':orders,'decoded_execution_ledger':executions,'near_execution_register':nearrows,'financial_totals':totals,'destination_balance_checks':balances,'authorization_verification':authorization}
if __name__=='__main__':
 for name,value in derive().items():(R/(name+'.json')).write_text(json.dumps(value,indent=2)+'\n')
