"""Offline verification of saved destination evidence; no origin attribution."""
import json, pathlib, datetime
from decimal import Decimal
P = pathlib.Path(__file__).parent
B = P.parent
MASK = (1 << 64) - 1
RC = [0x1,0x8082,0x800000000000808a,0x8000000080008000,0x808b,0x80000001,0x8000000080008081,0x8000000000008009,0x8a,0x88,0x80008009,0x8000000a,0x8000808b,0x800000000000008b,0x8000000000008089,0x8000000000008003,0x8000000000008002,0x8000000000000080,0x800a,0x800000008000000a,0x8000000080008081,0x8000000000008080,0x80000001,0x8000000080008008]
ROT = [[0,36,3,41,18],[1,44,10,45,2],[62,6,43,15,61],[28,55,25,21,56],[27,20,39,8,14]]
def rol(a,n): return ((a << n) | (a >> (64-n))) & MASK if n else a
def keccak(data):
    data=bytearray(data); data.append(1)
    data.extend(bytes((-len(data)) % 136)); data[-1] |= 128
    a=[0]*25
    for start in range(0,len(data),136):
        for i in range(17): a[i] ^= int.from_bytes(data[start+8*i:start+8*i+8],'little')
        for rc in RC:
            c=[a[x]^a[x+5]^a[x+10]^a[x+15]^a[x+20] for x in range(5)]
            d=[c[(x-1)%5]^rol(c[(x+1)%5],1) for x in range(5)]
            for x in range(5):
                for y in range(5): a[x+5*y] ^= d[x]
            b=[0]*25
            for x in range(5):
                for y in range(5): b[y+5*((2*x+3*y)%5)]=rol(a[x+5*y],ROT[x][y])
            for x in range(5):
                for y in range(5): a[x+5*y]=b[x+5*y]^((~b[(x+1)%5+5*y])&b[(x+2)%5+5*y])
            a[0]^=rc
    return b''.join(x.to_bytes(8,'little') for x in a)[:32].hex()
assert keccak(b'')=='c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'
SIG='FilledRelay(bytes32,bytes32,uint256,uint256,uint256,uint256,uint256,uint32,uint32,bytes32,bytes32,bytes32,bytes32,bytes32,(bytes32,bytes32,uint256,uint8))'
H='0x5d6b414f8b7ecdcee5ffdb378ceb3de228cec732037437d759900ed7b34d1b1a'
receipt_path='raw_sources/eth_getTransactionReceipt_'+H+'.response.json'
r=json.loads((B/receipt_path).read_text())['result']
log=next(x for x in r['logs'] if x['topics'] and x['topics'][0]=='0x'+keccak(SIG.encode()))
assert r['status']=='0x1' and not log['removed']
raw=bytes.fromhex(log['data'][2:])
words=[raw[i:i+32] for i in range(0,len(raw),32)]
num=lambda i:int.from_bytes(words[i],'big')
addr=lambda i:'0x'+words[i][-20:].hex()
assert int(log['topics'][1],16)==8453 and int(log['topics'][2],16)==6301830
assert addr(9)==addr(8)=='0x427c4b37de0714821b09c4fc655a713abbcfba83'
# FilledRelay has a static execution tuple; preserve message hashes without inferring content.
assert len(words)==15
updated_recipient=addr(11)
assert num(10)==num(12)==0
assert updated_recipient==addr(9) and num(13)==num(3) and num(14)==0
hint=json.loads((B/'continuation_2026_10_09/raw/across_deposit_status_hint.response.json').read_text())
assert hint['fillTx']==H and hint['originChainId']==8453 and int(hint['depositId'])==6301830
out={'ID':'F0432','classification':'CONFIRMED','record_type':'destination protocol event; not a new transfer or confirmed cross-chain edge',
 'scope':'Destination event reproduced offline from saved receipt and first-party interface. Origin independently reproduced in F0433 and association established in F0434. F0129 remains unchanged.',
 'transaction_hash':H,'chain':'Ethereum','chain_id':1,'block_number':int(r['blockNumber'],16),
 'timestamp_UTC':datetime.datetime.fromtimestamp(int(log['blockTimestamp'],16),datetime.timezone.utc).isoformat(),
 'transaction_sender':r['from'],'transaction_to':r['to'],'transaction_status':'success',
 'event_contract':log['address'],'event_signature':SIG,'event_topic':log['topics'][0],'log_index':int(log['logIndex'],16),
 'origin_chain_id_as_emitted':8453,'deposit_id_as_emitted':6301830,
 'input_token_as_emitted':addr(0),'output_token':addr(1),
 'input_amount_wei_as_emitted':str(num(2)),'output_amount_wei':str(num(3)),
 'input_amount_token_units_as_emitted':str(Decimal(num(2))/Decimal(10**18)),
 'output_amount_token_units':str(Decimal(num(3))/Decimal(10**18)),
 'input_minus_output_as_emitted':str(Decimal(num(2)-num(3))/Decimal(10**18)),
 'fee_limitation':'Emitted input/output difference only, not independently reproduced origin debit or verified breakdown of protocol/relayer fees.',
 'repayment_chain_id_as_emitted':num(4),'relayer_as_emitted':'0x'+log['topics'][3][-40:],
 'fill_deadline':num(5),'exclusivity_deadline':num(6),'exclusive_relayer_as_emitted':addr(7),
 'depositor_as_emitted':addr(8),'recipient_as_emitted':addr(9),'message_hash':'0x'+words[10].hex(), 'updated_message_hash':'0x'+words[12].hex(),
 'updated_recipient':updated_recipient,'updated_output_amount_wei':str(num(13)),'fill_type':num(14),
 'origin_transaction_hint':hint['depositTxHash'],'origin_transaction_reproduced':True,
 'origin_to_fill_classification':'CONFIRMED; see F0433-F0434','service_or_owner_attribution':'Origin sender reproduced separately in F0433; no custody or beneficial-owner identification',
 'source_record':receipt_path,'interface_record':'continuation_2026_10_09/raw/across_interface_source.response.json'}
(P/'destination_event_F0432.json').write_text(json.dumps(out,indent=2)+'\n')
prior=json.loads((B/'continuation_2026_10_09/master_timeline_F0001_F0431.json').read_text())['rows']
assert len(prior)==431
(P/'master_timeline_F0001_F0432.json').write_text(json.dumps({'notes':'Additive event observation. F0001-F0431 unchanged. F0432 does not count another transfer or a verified cross-chain edge.','rows':prior+[out]},indent=2)+'\n')
print(json.dumps(out,indent=2))

# Origin reproduction and deterministic protocol parameter correspondence.
access=P/'access'
load=lambda name:json.loads((access/(name+'.response.txt')).read_text())['result']
tx=load('base_official_eth_getTransactionByHash')
origin=load('base_official_eth_getTransactionReceipt')
assert load('base_official_eth_chainId')=='0x2105'
assert load('base_drpc_eth_getTransactionReceipt')==origin
assert load('base_drpc_eth_getTransactionByHash')==tx
assert tx['hash']==origin['transactionHash']==hint['depositTxHash']
assert int(tx['chainId'],16)==8453 and origin['status']=='0x1'
block=load('base_official_origin_block')
assert block['hash']==origin['blockHash']==tx['blockHash']
assert block['number']==origin['blockNumber']==tx['blockNumber']
assert tx['hash'] in block['transactions']
DSIG='FundsDeposited(bytes32,bytes32,uint256,uint256,uint256,uint256,uint32,uint32,uint32,bytes32,bytes32,bytes32,bytes)'
deposit=next(x for x in origin['logs'] if x['topics'][0]=='0x'+keccak(DSIG.encode()))
assert not deposit['removed'] and deposit['address']==tx['to']==origin['to']
dbytes=bytes.fromhex(deposit['data'][2:])
dw=[dbytes[i:i+32] for i in range(0,len(dbytes),32)]
dn=lambda i:int.from_bytes(dw[i],'big')
da=lambda i:'0x'+dw[i][-20:].hex()
assert int(deposit['topics'][1],16)==1
assert int(deposit['topics'][2],16)==out['deposit_id_as_emitted']
assert '0x'+deposit['topics'][3][-40:]==tx['from']==origin['from']==out['depositor_as_emitted']
assert da(0)==addr(0) and da(1)==addr(1)
assert dn(2)==num(2) and dn(3)==num(3)
assert dn(5)==num(5) and dn(6)==num(6)
assert da(7)==addr(9) and da(8)==addr(7)
message_offset=dn(9)
assert int.from_bytes(dbytes[message_offset:message_offset+32],'big')==0
assert int(tx['value'],16)==dn(2)
wrapping=next(x for x in origin['logs'] if x['address']==da(0) and x['topics'][0]=='0x'+keccak(b'Deposit(address,uint256)'))
assert '0x'+wrapping['topics'][1][-40:]==tx['to']
assert int(wrapping['data'],16)==dn(2)
origin_record={'ID':'F0433','classification':'CONFIRMED','record_type':'origin deposit; same bridge value, not additive loss',
 'chain':'Base','chain_id':8453,'transaction_hash':tx['hash'],'block_number':int(block['number'],16),
 'timestamp_UTC':datetime.datetime.fromtimestamp(int(block['timestamp'],16),datetime.timezone.utc).isoformat(),
 'sender':tx['from'],'recipient_contract':tx['to'],'status':'success','event_signature':DSIG,'event_topic':deposit['topics'][0],
 'log_index':int(deposit['logIndex'],16),'native_ETH_value_wei':str(int(tx['value'],16)),
 'deposited_token_address':da(0),'deposited_amount_wei':str(dn(2)),
 'asset_logic':'Native ETH value equals FundsDeposited inputAmount; matching WETH Deposit event wraps value at origin pool.',
 'destination_chain_id':1,'destination_recipient':da(7),'output_token':da(1),'output_amount_wei':str(dn(3)),
 'deposit_id':int(deposit['topics'][2],16),'quote_timestamp':dn(4),'fill_deadline':dn(5),'exclusivity_deadline':dn(6),
 'exclusive_relayer':da(8),'message_hex':'0x',
 'execution_fee_ETH':str(Decimal(int(origin['gasUsed'],16)*int(origin['effectiveGasPrice'],16))/Decimal(10**18)),
 'L1_fee_ETH':str(Decimal(int(origin['l1Fee'],16))/Decimal(10**18)),
 'fee_limitations':'Separate receipt execution/L1 components, not asserted complete fee decomposition or bridge fee split.',
 'source_records':['access/base_official_eth_getTransactionByHash.response.txt','access/base_official_eth_getTransactionReceipt.response.txt','access/base_drpc_eth_getTransactionReceipt.response.txt','access/base_official_origin_block.response.txt']}
edge={'ID':'F0434','classification':'CONFIRMED','record_type':'cross_chain_edge; association only, not additional transfer/loss',
 'origin_transaction':tx['hash'],'origin_chain_id':8453,'destination_transaction':H,'destination_chain_id':1,
 'deposit_id':6301830,'origin_amount_wei':str(dn(2)),'destination_amount_wei':str(num(3)),
 'sender':tx['from'],'destination_recipient':addr(9),'bridge':'Across deposit/fill protocol event correspondence',
 'matched_parameters':['origin chain','destination chain','deposit ID','depositor','recipient','input token','output token','input amount','output amount','exclusive relayer','fill deadline','exclusivity deadline','empty origin message and zero fill message hash'],
 'evidence':['F0432','F0433','continuation_2026_10_09/raw/across_deposit_status_hint.response.json'],
 'input_output_difference_token_units':out['input_minus_output_as_emitted'],
 'fee_limitation':'Exact difference established; division among bridge/relayer/LP fees unresolved.',
 'provenance_boundary':'Deterministic protocol linkage through mixed bridge liquidity. No common owner, final beneficiary, prior funding source or Robinhood association inferred.'}
(P/'origin_deposit_F0433.json').write_text(json.dumps(origin_record,indent=2)+'\n')
(P/'cross_chain_edge_F0434.json').write_text(json.dumps(edge,indent=2)+'\n')
rows=prior+[out,origin_record,edge]
assert len(rows)==434 and len({x['ID'] for x in rows})==434
(P/'master_timeline_F0001_F0434.json').write_text(json.dumps({'notes':'Prior 431 rows unchanged. Destination event, origin deposit and matched bridge edge describe one route; do not sum as separate losses.','rows':rows},indent=2)+'\n')
print(json.dumps({'origin':origin_record,'edge':edge},indent=2))
