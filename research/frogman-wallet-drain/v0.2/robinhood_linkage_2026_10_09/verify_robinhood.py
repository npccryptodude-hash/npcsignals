"""Verify origin receipts and exact Across relay parameters; append IDs only."""
import json, pathlib, datetime
from decimal import Decimal
P=pathlib.Path(__file__).parent; B=P.parent; A=P/'access'
# Reuse the preserved, tested Keccak implementation without running its collector/verifier.
ns={}; prefix=(B/'across_verification_2026_10_09/verify_across.py').read_text().split("SIG=")[0]
# Function globals need the same namespace containing constants and helpers.
ns={'__file__':__file__};exec(prefix,ns);keccak=ns['keccak']
DSIG='FundsDeposited(bytes32,bytes32,uint256,uint256,uint256,uint256,uint32,uint32,uint32,bytes32,bytes32,bytes32,bytes)'
FSIG='FilledRelay(bytes32,bytes32,uint256,uint256,uint256,uint256,uint256,uint32,uint32,bytes32,bytes32,bytes32,bytes32,bytes32,(bytes32,bytes32,uint256,uint8))'
dt='0x'+keccak(DSIG.encode());ft='0x'+keccak(FSIG.encode())
load=lambda n:json.loads((A/(n+'.response.txt')).read_text())['result']
assert int(load('chain_id'),16)==4663
deposits=json.loads((P/'candidate_deposits.json').read_text())
dest=[]
for f in sorted((B/'raw_sources').glob('eth_getTransactionReceipt_*.response.json')):
    r=json.loads(f.read_text()).get('result')
    if not r:continue
    for l in r['logs']:
        if l['topics'] and l['topics'][0]==ft and int(l['topics'][1],16)==4663:dest.append((r,l,str(f.relative_to(B))))
prior=json.loads((B/'across_verification_2026_10_09/master_timeline_F0001_F0434.json').read_text())['rows']
rows=[];edges=[]
def words(l):return [bytes.fromhex(l['data'][2:])[i:i+32] for i in range(0,(len(l['data'])-2)//2,32)]
def integer(w,i):return int.from_bytes(w[i],'big')
def addr(w,i):return '0x'+w[i][-20:].hex()
for candidate in sorted(deposits,key=lambda l:(int(l['blockNumber'],16),int(l['logIndex'],16))):
    h=candidate['transactionHash'];tx=load('eth_getTransactionByHash_'+h);r=load('eth_getTransactionReceipt_'+h);block=load('block_'+candidate['blockNumber'])
    assert tx['hash']==r['transactionHash']==h and int(tx['chainId'],16)==4663 and r['status']=='0x1'
    assert block['hash']==tx['blockHash']==r['blockHash'] and block['number']==tx['blockNumber']==r['blockNumber']
    assert h in block['transactions']
    dep=next(l for l in r['logs'] if l['topics'][0]==dt and l['topics'][2]==candidate['topics'][2])
    assert all(dep[k]==candidate[k] for k in ['address','topics','data','blockHash','blockNumber','transactionHash','logIndex']) and not dep['removed'] 
    dw=words(dep);assert int(dep['topics'][1],16)==1
    depositor='0x'+dep['topics'][3][-40:]
    assert depositor=='0x427c4b37de0714821b09c4fc655a713abbcfba83' and tx['from']==r['from']
    msg_offset=integer(dw,9);db=bytes.fromhex(dep['data'][2:]);msg_len=int.from_bytes(db[msg_offset:msg_offset+32],'big');message=db[msg_offset+32:msg_offset+32+msg_len];assert len(message)==msg_len;message_hash=bytes.fromhex(keccak(message)) if message else bytes(32)
    matches=[(rr,l,f) for rr,l,f in dest if l['topics'][2]==dep['topics'][2]]
    assert len(matches)==1
    dr,fill,dfile=matches[0];fw=words(fill)
    assert dr['status']=='0x1' and not fill['removed']
    assert dw[:4]==fw[:4] # input/output tokens and amounts
    assert dw[5]==fw[5] and dw[6]==fw[6] # deadlines
    assert dw[8]==fw[7] # exclusive relayer
    assert dep['topics'][3]=='0x'+fw[8].hex() and dw[7]==fw[9] # depositor and recipient
    assert fw[10]==message_hash and fw[11]==fw[9]
    assert integer(fw,13)==integer(fw,3) and integer(fw,14)==0
    transfer_topic='0x'+keccak(b'Transfer(address,address,uint256)')
    input_events=[l for l in r['logs'] if l['address']==addr(dw,0) and l['topics'][0]==transfer_topic and '0x'+l['topics'][2][-40:]==dep['address'] and int(l['data'],16)==integer(dw,2)]
    assert len(input_events)==1
    token_sender='0x'+input_events[0]['topics'][1][-40:]
    if tx['from']==depositor:
        assert int(tx['value'],16)==integer(dw,2) and int(input_events[0]['topics'][1],16)==0
        logic='Direct native value equals inputAmount; matching zero-address-to-pool wrapped-native mint. Prior funding remains separate.'
    else:
        assert int(tx['value'],16)==0
        mint=[l for l in r['logs'] if l['address']==addr(dw,0) and l['topics'][0]==transfer_topic and int(l['topics'][1],16)==0 and '0x'+l['topics'][2][-40:]==token_sender and int(l['data'],16)==integer(dw,2)]
        assert len(mint)==1
        logic='Zero-value outer transaction; wrapped input minted to intermediate address and transferred to deposit pool. Underlying native source, authority and ownership unresolved.'
    existing=[x['ID'] for x in prior if x.get('transaction_hash',x.get('transaction',''))==dr['transactionHash']]
    # Historic rows use several field schemas; exact hash lookup is only a reference aid.
    if not existing:existing=[x['ID'] for x in prior if dr['transactionHash'] in x.values()]
    oid=f'F{435+len(rows):04d}';eid=f'F{436+len(rows):04d}'
    o={'ID':oid,'classification':'CONFIRMED','record_type':'origin deposit','chain':'Robinhood Chain','chain_id':4663,
       'transaction_hash':h,'block_number':int(block['number'],16),'timestamp_UTC':datetime.datetime.fromtimestamp(int(block['timestamp'],16),datetime.timezone.utc).isoformat(),
       'sender':tx['from'],'transaction_recipient':tx['to'],'deposit_contract':dep['address'],'status':'success','event_signature':DSIG,'log_index':int(dep['logIndex'],16),
       'deposit_id':str(int(dep['topics'][2],16)),'deposit_id_hex':dep['topics'][2],'deposited_token':addr(dw,0),
       'native_value_wei':str(int(tx['value'],16)),'input_amount_wei':str(integer(dw,2)),'output_amount_wei':str(integer(dw,3)),
       'destination_chain_id':1,'destination_recipient':addr(dw,7),'output_token':addr(dw,1),'quote_timestamp':integer(dw,4),
       'fill_deadline':integer(dw,5),'exclusivity_deadline':integer(dw,6),'exclusive_relayer':addr(dw,8),'message_hex':'0x'+message.hex(),'message_hash':'0x'+message_hash.hex(),
       'execution_fee_ETH':str(Decimal(int(r['gasUsed'],16)*int(r['effectiveGasPrice'],16))/Decimal(10**18)),
       'asset_logic':logic,'depositor_event_field':depositor,'token_sender_to_pool':token_sender,
       'source_records':['access/eth_getTransactionByHash_'+h+'.response.txt','access/eth_getTransactionReceipt_'+h+'.response.txt','access/block_'+candidate['blockNumber']+'.response.txt']}
    e={'ID':eid,'classification':'CONFIRMED','record_type':'cross_chain_edge; not additional loss','origin_chain_id':4663,'destination_chain_id':1,
       'origin_transaction':h,'destination_transaction':dr['transactionHash'],'origin_record_ID':oid,'existing_destination_records':existing,
       'deposit_id':o['deposit_id'],'origin_amount_wei':o['input_amount_wei'],'destination_amount_wei':o['output_amount_wei'],
       'input_output_difference_ETH':str(Decimal(integer(dw,2)-integer(dw,3))/Decimal(10**18)),
       'fee_limitation':'Exact protocol input-output difference, no verified bridge/relayer/LP fee decomposition or refund transaction.',
       'origin_sender':tx['from'],'destination_recipient':addr(fw,9),'origin_pool':dep['address'],'destination_pool':fill['address'],
       'destination_block':int(dr['blockNumber'],16),'destination_timestamp_UTC':datetime.datetime.fromtimestamp(int(fill['blockTimestamp'],16),datetime.timezone.utc).isoformat(),
       'destination_status':'success','relayer':'0x'+fill['topics'][3][-40:],'repayment_chain_id':integer(fw,4),'fill_type':integer(fw,14),'updated_message_hash':'0x'+fw[12].hex(),'message_limitation':'Original message hash reproduced. Updated-message hash is preserved without assuming it equals original content.',
       'matched_parameters':['chain IDs','deposit ID','depositor','recipient','tokens','input/output amounts','exclusive relayer','deadlines','message hash','updated recipient/output'],
       'source_record':dfile,'provenance_boundary':'Matched mixed-liquidity bridge routing, not owner/beneficiary attribution; upstream token-sale/native provenance remains separate.'}
    rows.extend([o,e]);edges.append(e)
assert len(rows)==30
summary={'classification':'CONFIRMED','new_ID_range':['F0435','F0464'],'matched_routes':len(edges),
 'origin_ETH':str(sum(Decimal(e['origin_amount_wei']) for e in edges)/Decimal(10**18)),
 'destination_ETH':str(sum(Decimal(e['destination_amount_wei']) for e in edges)/Decimal(10**18)),
 'origin_senders':sorted({o['sender'] for o in rows if o['record_type']=='origin deposit'}),'service_or_owner_attribution':'NOT ESTABLISHED',
 'limits':'15 routes only; does not establish all 23 Ethereum credits came from Robinhood or all origin deposits derive from affected-wallet assets.'}
(P/'transaction_ledger_F0435_F0464.json').write_text(json.dumps(rows,indent=2)+'\n')
(P/'cross_chain_edges.json').write_text(json.dumps(edges,indent=2)+'\n')
(P/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(P/'master_timeline_F0001_F0464.json').write_text(json.dumps({'notes':'Prior 434 rows unchanged. Transfer hops and edges are not additive losses.','rows':prior+rows},indent=2)+'\n')
print(json.dumps(summary,indent=2))
