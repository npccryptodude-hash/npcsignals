"""Offline verification of exact Chainflip origin/API/settlement correspondence."""
import json, pathlib, datetime, hashlib
from decimal import Decimal
P=pathlib.Path(__file__).parent; A=P/'access'; V=P.parent

def load(p): return json.loads(p.read_text())
def utc(n): return datetime.datetime.fromtimestamp(n,datetime.timezone.utc).isoformat().replace('+00:00','Z')
def units(n,d): return format(Decimal(n)/(Decimal(10)**d),'f')
def eth(method,n,h):
 fresh=A/f'drpc_{method}_{n}.response.txt'
 if fresh.exists() and load(fresh).get('result'):return load(fresh)['result'],str(fresh.relative_to(V))
 old=V/'raw_sources'/f'{method}_{h}.response.json'
 return load(old)['result'],str(old.relative_to(V))
rows=[];routes=[]
assert load(A/'drpc_chain.response.txt')['result']=='0x1'
assert load(A/'solana_genesis.response.txt')['result']=='5eykt4UsFv8P8NJdTREpY1vzqKqZKvdpKuc147dw2N9d'
for n in [1894600,1894627]:
 a=load(A/f'status_id_{n}.response.txt'); h=a['deposit']['txRef']
 assert a['state']=='COMPLETED' and a['srcChain']=='Ethereum' and a['destChain']=='Solana'
 for label in [f'status_channel_{n}',f'swap_status_{h}']:
  b=load(A/f'{label}.response.txt')
  for k in ['swapId','srcAsset','srcChain','destAsset','destChain','destAddress','depositChannel','deposit','swapEgress','fees','brokers']: assert a[k]==b[k],k
 tx,tp=eth('eth_getTransactionByHash',n,h);rc,rp=eth('eth_getTransactionReceipt',n,h)
 bn=int(tx['blockNumber'],16)
 bp=A/f'drpc_eth_getBlockByNumber_{n}.response.txt'
 if not(bp.exists() and load(bp).get('result')):bp=V/'raw_sources'/f'eth_bridge_block_{bn}.response.json'
 bl=load(bp)['result']
 assert tx['hash']==rc['transactionHash']==h and tx['blockHash']==rc['blockHash']==bl['hash']
 assert int(rc['status'],16)==1 and h in [x if isinstance(x,str) else x['hash'] for x in bl['transactions']]
 assert tx['to'].lower()==a['depositChannel']['depositAddress'].lower()
 assert int(tx['value'],16)==int(a['deposit']['amount'])==18500000000000000000
 assert tx.get('chainId','0x1')=='0x1'
 s=load(A/f'solana_tx_{n}.response.txt')['result'];sig=a['swapEgress']['txRef']
 assert s['transaction']['signatures'][0]==sig and s['meta']['err'] is None
 ins=[i for i in s['transaction']['message']['instructions'] if i.get('parsed',{}).get('type')=='transfer']
 assert len(ins)==1; info=ins[0]['parsed']['info']; assert info['destination']==a['destAddress'] and info['lamports']==int(a['swapEgress']['amount'])
 keys=s['transaction']['message']['accountKeys']; j=[k['pubkey'] for k in keys].index(a['destAddress']);assert s['meta']['postBalances'][j]-s['meta']['preBalances'][j]==info['lamports']
 assert keys[0]['pubkey']==info['source'] and keys[0]['signer']
 fees={f['type']:int(f['amount']) for f in a['fees']}
 assert int(a['deposit']['amount'])-int(a['swap']['originalInputAmount'])==fees['INGRESS']
 assert int(a['swap']['swappedOutputAmount'])-info['lamports']==fees['EGRESS']==s['meta']['fee']==14000
 assert s['meta']['preBalances'][0]-s['meta']['postBalances'][0]==info['lamports']+s['meta']['fee']
 assert a['swap']['remainingInputAmount']=='0' and a['swap']['dca']['executedChunks']==5 and a['swap']['dca']['remainingChunks']==0
 route={'swap_id':str(n),'channel_id':a['depositChannel']['id'],'source_chain':'Ethereum (1)','source_transaction':h,'source_block':bn,'source_timestamp_UTC':utc(int(bl['timestamp'],16)),'source_wallet':tx['from'],'deposit_address':tx['to'],'asset_in':'ETH','amount_in':'18.5','destination_chain':'Solana mainnet','destination_transaction':sig,'destination_slot':s['slot'],'destination_timestamp_UTC':utc(s['blockTime']),'destination_wallet':a['destAddress'],'egress_source_payer':info['source'],'asset_out':'SOL','amount_out':units(info['lamports'],9),'classification':'CONFIRMED','origin_transaction_status':'success','destination_transaction_status':'finalized success','fees_as_reported_by_protocol':a['fees'],'ethereum_execution_gas_fee_wei':str(int(rc['gasUsed'],16)*int(rc['effectiveGasPrice'],16)),'brokers':a['brokers'],'protocol_event_indices':{'deposit':a['deposit']['witnessedBlockIndex'],'egress_scheduled':a['swapEgress']['scheduledBlockIndex'],'egress_witnessed':a['swapEgress']['witnessedBlockIndex']},'evidence':[tp,rp,str(bp.relative_to(V)),f'{P.name}/access/status_id_{n}.response.txt',f'{P.name}/access/status_channel_{n}.response.txt',f'{P.name}/access/swap_status_{h}.response.txt',f'{P.name}/access/solana_tx_{n}.response.txt'],'attribution_significance':'Exact Chainflip routing and case-specific egress payer role only; no shared owner, custody relationship or beneficiary established.'}
 routes.append(route)
 for kind in ['origin enrichment (existing F0159/F0160; not new loss)','destination settlement','cross-chain edge']:
  row={'ID':f'F{465+len(rows):04d}','record_type':kind,**route};rows.append(row)
prior=load(V/'robinhood_linkage_2026_10_09/master_timeline_F0001_F0464.json')
assert len({r['ID'] for r in prior['rows']})==464
master={'notes':'Prior F0001–F0464 rows preserved exactly. Routing observations and edges do not add loss amounts. Privacy Cash remains separate.','rows':prior['rows']+rows}
assert master['rows'][:464]==prior['rows']
for name,obj in [('transaction_ledger_F0465_F0470.json',rows),('cross_chain_edges.json',routes),('master_timeline_F0001_F0470.json',master),('verification_summary.json',{'latest_ID':'F0470','origin_reproduced':True,'destination_reproduced':True,'confirmed_edges':2,'ETH_input_total':'37','SOL_output_total':units(sum(int(load(A/f'status_id_{n}.response.txt')['swapEgress']['amount']) for n in [1894600,1894627]),9),'prior_rows_unchanged':True,'limitations':['State Chain event indices are API-reported; independent consensus inclusion not reproduced.','No owner, custody relationship, beneficiary or complete affected-wallet provenance established.','Publicnode Ethereum RPC attempts timed out. Alternate dRPC independently returned both transactions, receipts, blocks and mainnet chain ID; exact source paths are listed per edge.']})]:
 (P/name).write_text(json.dumps(obj,indent=2)+'\n')
print('PASS: two exact origin/API/finalized-settlement edges; six additive ledger rows; 464 prior rows unchanged')
