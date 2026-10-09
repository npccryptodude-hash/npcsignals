"""Verify saved exact Mayan Swift V2 origin/fulfillment/message/unlock evidence offline."""
import pathlib,json,datetime,base64
from decimal import Decimal
from keccak_utils import keccak
P=pathlib.Path(__file__).parent;A=P/'access';V=P.parent
SOURCE='0x40ffe85a28dc9993541449464d7529a922142960';DEST='0xd78d199f8c402e7b5cc2abe278df0412400a3bae';FORWARD='0x337685fdab40d39bd02028545a4ffa7d287cc3e2';WETH='0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2';USDC='0xaf88d065e77c8cc2239327c5edb3a432268e5831';DRIVER='0x754dcfb2861547015b221e963b4133a71dbdc024'
def load(label):return json.loads((A/(label+'.response.txt')).read_text())
def result(label):return load(label)['result']
def dump(name,a):(P/name).write_text(json.dumps(a,indent=2)+'\n')
def topic(s):return '0x'+keccak(s.encode())
def words(h):return [h[j:j+64] for j in range(2,len(h),64)]
def addr(w):return '0x'+w[-40:]
def utc(n):return datetime.datetime.fromtimestamp(n,datetime.timezone.utc).isoformat().replace('+00:00','Z')
def amount(n,d):return format(Decimal(n)/Decimal(10)**d,'f')
def dynamic(d,off):n=int.from_bytes(d[off:off+32],'big');return d[off+32:off+32+n]
def inclusion(tx,rc,bl):
 assert tx['hash']==rc['transactionHash'] and tx['blockHash']==rc['blockHash']==bl['hash']
 assert tx['blockNumber']==rc['blockNumber']==bl['number'] and int(rc['status'],16)==1
 assert tx['hash'] in [x if isinstance(x,str) else x['hash'] for x in bl['transactions']]
 assert all(l['transactionHash']==tx['hash'] and l['blockHash']==bl['hash'] and not l['removed'] for l in rc['logs'])
def matching(rc,address,sig):return [l for l in rc['logs'] if l['address']==address and l['topics'][0]==topic(sig)]
assert result('eth_chain')=='0x1' and int(result('arb_chain'),16)==42161
assert int(result('usdc_decimals'),16)==6
sym=bytes.fromhex(result('usdc_symbol')[2:]);assert dynamic(sym,int.from_bytes(sym[:32],'big'))==b'USDC'
s=(A/'swift_v2_artifact.response.txt').read_text();abi=json.JSONDecoder().raw_decode(s[s.index('{'):])[0]['abi']
for name,sig in [('OrderCreated','OrderCreated(bytes32)'),('OrderFulfilled','OrderFulfilled(bytes32,uint64,uint256)'),('OrderUnlocked','OrderUnlocked(bytes32)')]:assert any(x['type']=='event' and x['name']==name for x in abi)
# Exact VAA and compressed batch accepted in the Ethereum unlock transaction.
ut=result('unlock_eth_getTransactionByHash');ur=result('unlock_eth_getTransactionReceipt');ub=result('unlock_block');inclusion(ut,ur,ub)
assert ut['to']==SOURCE and ut['from']==DRIVER and ut['input'][:10]=='0x'+keccak(b'unlockCompressedBatch(bytes,bytes,uint16[])')[:8]
d=bytes.fromhex(ut['input'][10:]);offs=[int.from_bytes(d[j:j+32],'big') for j in (0,32,64)];vm=dynamic(d,offs[0]);batch=dynamic(d,offs[1]);ixcount=int.from_bytes(d[offs[2]:offs[2]+32],'big');indexes=[int.from_bytes(d[offs[2]+32*(j+1):offs[2]+32*(j+2)],'big') for j in range(ixcount)]
w=load('wormhole_vaa_8323')['data'];assert vm==base64.b64decode(w['vaa'])
bod=vm[6+66*vm[5]:];emitter=bod[10:42].hex();seq=int.from_bytes(bod[42:50],'big');payload=bod[51:]
assert vm[0]==1 and int.from_bytes(vm[1:5],'big')==7 and int.from_bytes(bod[8:10],'big')==23 and emitter=='0'*24+DEST[2:] and seq==8323
assert payload[:3]==bytes([5,0,8]) and payload[3:].hex()==keccak(batch) and len(batch)==8*172
assert seq==w['sequence'] and emitter==w['emitterAddr'] and int.from_bytes(bod[:4],'big')==int(datetime.datetime.fromisoformat(w['timestamp'].replace('Z','+00:00')).timestamp())
pt=result('publish_eth_getTransactionByHash');pr=result('publish_eth_getTransactionReceipt');pb=result('publish_block');inclusion(pt,pr,pb);assert pt['hash']=='0x'+w['txHash']
msg=next(l for l in pr['logs'] if l['topics'][0]==topic('LogMessagePublished(address,uint64,uint32,bytes,uint8)') and addr(l['topics'][1])==DEST)
md=bytes.fromhex(msg['data'][2:]);assert int.from_bytes(md[:32],'big')==seq and dynamic(md,int.from_bytes(md[64:96],'big'))==payload
assert int.from_bytes(bod[:4],'big')==int(pb['timestamp'],16)
constants=(A/'wormhole_mainnet_constants.response.txt').read_text().split('const MAINNET =',1)[1].split('const TESTNET',1)[0].lower()
assert msg['address'] in constants and msg['address']=='0xa5f208e072434bc67592e4c49c1b991ba79bca46'
message={'classification':'CONFIRMED','publication_transaction':pt['hash'],'publication_block':int(pb['number'],16),'publication_timestamp_UTC':utc(int(pb['timestamp'],16)),'publication_sender':pt['from'],'wormhole_core_emitter':msg['address'],'wormhole_emitter_chain_id':23,'wormhole_emitter_address':emitter,'sequence':seq,'guardian_set_index':7,'signature_count':vm[5],'encoded_VAA_hex':vm.hex(),'VAA_body_double_keccak':keccak(bytes.fromhex(keccak(bod))),'payload_hex':payload.hex(),'compressed_batch_hex':batch.hex(),'compressed_batch_keccak':keccak(batch),'batch_count':8,'executed_indexes':indexes,'unlock_transaction':ut['hash'],'unlock_block':int(ub['number'],16),'unlock_timestamp_UTC':utc(int(ub['timestamp'],16)),'unlock_sender':ut['from'],'limitation':'VAA bytes independently match Wormholescan and successful contract calldata; standalone guardian ECDSA validation and bytecode-level verification were not performed.'}
assert message['VAA_body_double_keccak']==w['digest']
rows=[];edges=[];case_unlocks=[]
for i,old in enumerate(['F0162','F0178','F0180']):
 a=load(f'mayan_status_{i}');ot=result(f'origin_eth_getTransactionByHash_{i}');orr=result(f'origin_eth_getTransactionReceipt_{i}');ob=result(f'origin_eth_getBlockByNumber_{i}');dt=result(f'dest_eth_getTransactionByHash_{i}');dr=result(f'dest_eth_getTransactionReceipt_{i}');db=result(f'dest_block_{i}');inclusion(ot,orr,ob);inclusion(dt,dr,db)
 assert a['sourceTxHash']==ot['hash'] and a['fulfillTxHash']==dt['hash'] and a['redeemTxHash']==ut['hash'] and a['service']=='SWIFT_V2' and a['clientStatus']=='COMPLETED'
 assert a['sourceChain']=='2' and a['destChain']=='23' and a['sourceTxBlockNo']==int(ob['number'],16)
 assert ot['from']==a['trader'].lower()==a['destAddress'] and ot['to']==a['initiateContractAddress'].lower()
 assert dt['from']==a['driverAddress'].lower()==DRIVER
 assert int(ot['value'],16)==int(a['fromAmount64']) and a['fromTokenSymbol']=='ETH' and a['toTokenAddress']==USDC
 created=next(l for l in matching(orr,SOURCE,'OrderCreated(bytes32)') if l['data']==a['orderHash'])
 fulfilled=next(l for l in matching(dr,DEST,'OrderFulfilled(bytes32,uint64,uint256)') if words(l['data'])[0]==a['orderHash'][2:]);fw=words(fulfilled['data']);assert int(fw[2],16)==int(a['toAmount64'])
 transfer=next(l for l in matching(dr,USDC,'Transfer(address,address,uint256)') if addr(l['topics'][1])==DEST and addr(l['topics'][2])==a['destAddress'] and int(l['data'],16)==int(a['toAmount64']))
 # Lock ingress is native wrapping -> Forwarder -> Swift source in the same receipt.
 wethpath=[]
 for frm,to in [('0x529863940bf6065d8c122a550c2ff37c1cfefa16',FORWARD),(FORWARD,SOURCE)]:
  l=next(l for l in matching(orr,WETH,'Transfer(address,address,uint256)') if addr(l['topics'][1])==frm and addr(l['topics'][2])==to and int(l['data'],16)==int(a['fromAmount64']));wethpath.append(l)
 wrap=next(l for l in matching(orr,WETH,'Deposit(address,uint256)') if int(l['data'],16)==int(a['fromAmount64']))
 # Inner order calldata preserved in the forwarder event, decoded by the SDK ABI.
 fl=next(l for l in orr['logs'] if l['address']==FORWARD and 'a3a30834' in l['data']);fd=bytes.fromhex(fl['data'][2:]);inner=dynamic(fd,int.from_bytes(fd[160:192],'big'));assert inner[:4].hex()=='a3a30834';iw=[inner[j:j+32] for j in range(4,len(inner),32)];ival=lambda j:int.from_bytes(iw[j],'big');ia=lambda j:'0x'+iw[j][-20:].hex()
 assert ival(1)==int(a['fromAmount64']) and ia(3)==ot['from'] and ia(4)==a['destAddress'] and ival(5)==23 and ia(7)==USDC and ival(8)==int(a['minAmountOut64']) and ival(9)==0 and ival(13)==0 and ival(14)==a['auctionMode']
 assert int(a['toAmount64'])>=ival(8) and a['mayanBps']==a['referrerBps']==a['protocolFeeUsd']==a['referrerFeeUsd']==0
 unlocked=next(l for l in matching(ur,SOURCE,'OrderUnlocked(bytes32)') if l['data']==a['orderHash']);uindex=ur['logs'].index(unlocked);reimbursement=ur['logs'][uindex-1]
 assert reimbursement['address']==WETH and reimbursement['topics'][0]==topic('Transfer(address,address,uint256)') and addr(reimbursement['topics'][1])==SOURCE and addr(reimbursement['topics'][2])==DRIVER and int(reimbursement['data'],16)==int(a['fromAmount64'])
 batchindex=a['postedBatchUnlockIndex'];record=batch[batchindex*172:(batchindex+1)*172];assert record[:32].hex()==a['orderHash'][2:] and batchindex in indexes and int.from_bytes(record[32:34],'big')==2
 assert record[98:100]==bytes(2) and record[100:132].hex()=='0'*24+DRIVER[2:] and int.from_bytes(record[164:172],'big')==int(db['timestamp'],16)
 decoded={'input_token_parameter':ia(0),'input_amount_raw':str(ival(1)),'payloadType':ival(2),'trader':ia(3),'destination':ia(4),'destination_Wormhole_chain_id':ival(5),'referrer':ia(6),'output_token':ia(7),'min_output_raw':str(ival(8)),'gas_drop_raw':str(ival(9)),'cancel_fee_parameter_raw':str(ival(10)),'refund_fee_parameter_raw':str(ival(11)),'deadline_UTC':utc(ival(12)),'referrer_bps':ival(13),'auction_mode':ival(14),'random_key':'0x'+iw[15].hex()}
 edge={'source_transaction':ot['hash'],'source_chain':'Ethereum (EVM 1; Wormhole 2)','source_block':int(ob['number'],16),'source_timestamp_UTC':utc(int(ob['timestamp'],16)),'source_wallet':ot['from'],'origin_outer_router':ot['to'],'mayan_forwarder':FORWARD,'mayan_source_contract':SOURCE,'input_asset':'ETH (locked as WETH)','input_amount':a['fromAmount'],'input_raw':a['fromAmount64'],'destination_transaction':dt['hash'],'destination_chain':'Arbitrum One (EVM 42161; Wormhole 23)','destination_block':int(db['number'],16),'destination_timestamp_UTC':utc(int(db['timestamp'],16)),'destination_wallet':a['destAddress'],'output_asset':'USDC','output_token_contract':USDC,'output_amount':a['toAmount'],'output_raw':a['toAmount64'],'mayan_destination_contract':DEST,'fulfillment_outer_router':dt['to'],'order_id':a['orderId'],'order_hash':a['orderHash'],'service':'Mayan Swift V2','classification':'CONFIRMED','transaction_status':'origin, fulfillment, publication and unlock successful','protocol_role':'LI.FI outer routing; Mayan Swift input lock and destination fulfillment; Wormhole batch message; case-specific driver reimbursement','driver_fulfiller':DRIVER,'auction_address_API_only':a['auctionAddress'],'auction_state_API_only':a['auctionStateAddr'],'auction_winner_status':'API driver and on-chain fulfiller reproduced; independent Solana auction competition/winner event not decoded','relayer_address_API':a['relayerAddress'],'wormhole_message_id':w['id'],'shared_unlock_transaction':ut['hash'],'batch_unlock_index':batchindex,'unlock_receiver':DRIVER,'reimbursement_asset':'WETH','reimbursement_amount':a['fromAmount'],'fees':{'protocol_bps':a['mayanBps'],'referrer_bps':a['referrerBps'],'protocol_fee_USD_API':a['protocolFeeUsd'],'bridge_fee_API':a['bridgeFee'],'redeem_relayer_fee_API':a['redeemRelayerFee'],'refund_relayer_fee_API':a['refundRelayerFee'],'origin_execution_gas_wei':str(int(orr['gasUsed'],16)*int(orr['effectiveGasPrice'],16)),'fulfillment_execution_gas_wei':str(int(dr['gasUsed'],16)*int(dr['effectiveGasPrice'],16)),'limitation':'API fee fields and cancellation/refund parameters are not an independently proved deduction from this successful output. Shared transaction gas is not allocated per order. No independent market spread asserted.'},'decoded_order_parameters':decoded,'events':{'origin_created':created,'destination_fulfilled':fulfilled,'destination_USDC_transfer':transfer,'origin_wrap':wrap,'origin_WETH_path':wethpath,'source_unlocked':unlocked,'WETH_reimbursement':reimbursement},'evidence':[f'access/{label}.response.txt' for label in [f'mayan_status_{i}',f'origin_eth_getTransactionByHash_{i}',f'origin_eth_getTransactionReceipt_{i}',f'origin_eth_getBlockByNumber_{i}',f'dest_eth_getTransactionByHash_{i}',f'dest_eth_getTransactionReceipt_{i}',f'dest_block_{i}','unlock_eth_getTransactionByHash','unlock_eth_getTransactionReceipt','unlock_block','wormhole_vaa_8323','publish_eth_getTransactionByHash','publish_eth_getTransactionReceipt','publish_block','swift_v2_artifact']],'attribution_significance':'Protocol routing and driver reimbursement only. Same literal address across chains is a routing observation, not independent common-control proof. No custody firm, human owner or final beneficiary identified.'}
 edges.append(edge);case_unlocks.append({'order_hash':a['orderHash'],'batch_index':batchindex,'WETH_amount':a['fromAmount'],'recipient':DRIVER,'transfer_log_index':reimbursement['logIndex']})
 for kind in ['origin enrichment (existing '+old+'; no additional loss)','destination settlement','cross-chain edge']:
  rows.append({'ID':f'F{471+len(rows):04d}','record_type':kind,**edge})
rows.append({'ID':'F0480','record_type':'shared protocol reimbursement observation; not additional loss','classification':'CONFIRMED','transaction':ut['hash'],'source':SOURCE,'recipient':DRIVER,'case_asset':'WETH','case_amount':'34.75','case_orders':case_unlocks,'batch_total_orders':8,'message_id':w['id'],'attribution_significance':'Only three case orders assigned here; remaining five batch orders are unrelated/unattributed. Driver reimbursement endpoint does not establish a final beneficiary.'})
prior=json.loads((V/'chainflip_verification_2026_10_09/master_timeline_F0001_F0470.json').read_text())['rows'];assert len(prior)==470
assert sum(Decimal(e['input_amount']) for e in edges)==Decimal('34.75');assert sum(Decimal(e['output_amount']) for e in edges)==Decimal('92468.737932')
dump('cross_chain_edges.json',edges);dump('wormhole_batch_correspondence.json',message);dump('transaction_ledger_F0471_F0480.json',rows);dump('master_timeline_F0001_F0480.json',{'notes':'F0001–F0470 rows unchanged. Origin, fulfillment, cross-chain edge and driver reimbursement are not additive losses. Privacy Cash stays separate.','rows':prior+rows});dump('verification_summary.json',{'latest_ID':'F0480','origin_reproduced':True,'destination_reproduced':True,'classification':'CONFIRMED','new_edges':3,'input_total_ETH':'34.75','output_total_USDC':'92468.737932','Wormhole_message':w['id'],'source_driver_reimbursement_WETH':'34.75','prior_rows_unchanged':True,'remaining_gaps':['Standalone guardian signature validation and deployed bytecode audit not performed.','Solana auction competition/winner events not independently decoded.','Complete upstream provenance, common control, custody identity and final beneficiary remain unresolved.']})
print('PASS: three exact origin/order/fulfillment/USDC edges; published VAA hash/bytes/batch match; three exact driver reimbursements; 470 prior rows unchanged')
