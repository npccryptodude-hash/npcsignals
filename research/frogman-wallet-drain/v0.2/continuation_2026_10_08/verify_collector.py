"""Validate scoped primary evidence and append unique ledger IDs after F0206."""
import csv, datetime, hashlib, json, pathlib
from decimal import Decimal
from collect_collector import ADDRESS,TOKEN,TRANSFER
P=pathlib.Path(__file__).parent; R=P/'raw'
def read(name): return json.loads((R/(name+'.response.json')).read_bytes())['result']
def amount(units): return format(Decimal(units)/Decimal(10**6),'f')
latest=int(read('arb_latest'),16)
logs={}
for direction in ['in','out']:
    for start in range(512422000,latest+1,100000):
        stop=min(start+99999,latest)
        result=read(f'collector_{direction}_{start}_{stop}')
        for l in result:
            assert start<=int(l['blockNumber'],16)<=stop
            assert l['address'].lower()==TOKEN and l['topics'][0]==TRANSFER
            assert '0x'+l['topics'][2 if direction=='in' else 1][-40:]==ADDRESS
            logs[(l['transactionHash'],l['logIndex'])]=l
ordered=sorted(logs.values(),key=lambda x:(int(x['blockNumber'],16),int(x['transactionIndex'],16),int(x['logIndex'],16)))
known={'0xd7efd720adf271b7173dd01a9b81668892bee6b1','0x68d6e20a28f9d50ebf798ccf9fae9e3d5e4f1ac4','0x888795f84f5f81352a7639f1254662ae5897e223','0x4079067aa1bdff060c6c45155966d81c79e754e9','0x68b3a77db46418905c7eaf63324d4adcce06a680','0xd9249de6224382ce7791600d1d1f9e5fdf633abb'}
incoming=[x for x in ordered if '0x'+x['topics'][2][-40:]==ADDRESS and int(x['data'],16)>0]
outgoing=[x for x in ordered if '0x'+x['topics'][1][-40:]==ADDRESS and int(x['data'],16)>0]
extra=[x for x in incoming if '0x'+x['topics'][1][-40:] not in known]
selected=extra[:1]+outgoing[:1]; rows=[]
for index,l in enumerate(selected,207):
    h=l['transactionHash']; tx=read(h+'_tx'); receipt=read(h+'_receipt'); block=read('block_'+l['blockNumber'])
    assert tx['hash']==receipt['transactionHash']==h
    assert tx['blockHash']==receipt['blockHash']==l['blockHash']==block['hash']
    assert h in block['transactions'] and int(receipt['status'],16)==1
    assert any(e['address']==l['address'] and e['logIndex']==l['logIndex'] and e['topics']==l['topics'] and e['data']==l['data'] for e in receipt['logs'])
    rows.append({'ID':f'F{index:04d}','timestamp':datetime.datetime.fromtimestamp(int(block['timestamp'],16),datetime.timezone.utc).isoformat().replace('+00:00','Z'),'chain':'Arbitrum (42161)','tx/signature':h,'source':'0x'+l['topics'][1][-40:],'destination':'0x'+l['topics'][2][-40:],'asset':'USDC','amount':amount(int(l['data'],16)),'USD value if available':'','action':'token transfer event','protocol':'UNRESOLVED','signer/authority if known':tx['from']+' (transaction sender only)','provenance status':'mixed; no exclusive incident allocation to onward outflow','classification':'CONFIRMED','source_record':'raw/'+h+'_receipt.response.json','notes':'Context event, not an additional incident loss. Sender identity, common ownership and linkage to a particular Relay deposit are NOT ESTABLISHED.','token_contract':TOKEN,'raw_token_units':str(int(l['data'],16)),'log_index':int(l['logIndex'],16),'block_number':int(l['blockNumber'],16),'network_fee_ETH':format(Decimal(int(receipt['gasUsed'],16)*int(receipt['effectiveGasPrice'],16))/Decimal(10**18),'f')})
with (P/'transaction_ledger_F0207_F0208.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
case=[l for l in incoming if '0x'+l['topics'][1][-40:] in known]
assert len(case)==6 and sum(int(x['data'],16) for x in case)==561850214994
balance=int(read('collector_usdc_balance'),16)
snapshot=read('block_'+hex(latest))
code=read('collector_code')
assert len(code)>2
summary={'classification':'CONFIRMED','chain_id':int(read('arb_chain'),16),'address':ADDRESS,'token':TOKEN,'examined_block_range':[512422000,latest],'snapshot_timestamp':datetime.datetime.fromtimestamp(int(snapshot['timestamp'],16),datetime.timezone.utc).isoformat(),'USDC_balance':amount(balance),'event_count':len(logs),'positive_inflow_events':len(incoming),'positive_outflow_events':len(outgoing),'all_observed_USDC_inflows':amount(sum(int(x['data'],16) for x in incoming)),'all_observed_USDC_outflows':amount(sum(int(x['data'],16) for x in outgoing)),'case_linked_USDC_inflows':amount(sum(int(x['data'],16) for x in case)),'other_observed_USDC_inflows':amount(sum(int(x['data'],16) for x in extra)),'receipt_verified_context_events':rows,'provenance':'mixed','limits':'Only USDC in the specified window. Full lifetime and other-token history not examined. Aggregate events are RPC log observations; only the two context events and six previously saved case transfers have individual receipt/block reproduction. No exclusive attribution of subsequent outflows, exchange identity, beneficiary or common control is established.'}
(P/'collector_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
summary['contract_code_bytes']=(len(code)-2)//2
summary['opening_balance_query']='UNRESOLVED: provider returned historical state unavailable; inferred opening balance is not independently confirmed.'
(P/'collector_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
graph={'nodes':[{'address':ADDRESS,'chain':42161,'role':'mixed-fund receiving contract','classification':'CONFIRMED','control_evidence':'NOT ESTABLISHED'}],'edges':rows,'boundary':'Case-specific exclusive allocation stops at collector; no particular onward event is matched to a case deposit.'}
(P/'wallet_graph_update.json').write_text(json.dumps(graph,indent=2)+'\n')
print(json.dumps(summary,indent=2))
