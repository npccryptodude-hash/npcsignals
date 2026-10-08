"""Append newly reproduced EVM transfers without renumbering saved ledgers."""
import pathlib,json,csv,decimal,datetime
P=pathlib.Path(__file__).parent;R=P/'raw_sources';D=decimal.Decimal
def read(n):return json.loads((R/n).read_text())
def stamp(b):return datetime.datetime.fromtimestamp(int(b['timestamp'],16),datetime.timezone.utc).isoformat().replace('+00:00','Z')
base=list(csv.DictReader((P/'evm_transaction_ledger_v0.2.csv').open()));fields=list(base[0]);rows=[]
def add(timestamp,chain,h,source,dest,asset,amount,action,protocol,prov,record,fee='',notes=''):
 row={k:'' for k in fields};row.update({'ID':f'F{128+len(rows):04d}','timestamp':timestamp,'chain':chain,'tx/signature':h,'source':source,'destination':dest,'asset':asset,'amount':amount,'action':action,'protocol':protocol,'provenance status':prov,'classification':'CONFIRMED','source_record':record,'network_fee_ETH':fee,'notes':notes,'record_type':'fund transfer'});rows.append(row)
def validate(h,prefix):
 tx=read('eth_getTransactionByHash_'+h+'.response.json')['result'];rc=read('eth_getTransactionReceipt_'+h+'.response.json')['result'];b=read(prefix+str(int(tx['blockNumber'],16))+'.response.json')['result'];assert tx['hash']==rc['transactionHash']==h;assert tx['blockHash']==rc['blockHash']==b['hash'];assert h in b['transactions'];assert int(rc['status'],16)==1;return tx,rc,b
def fee(rc):return format(D(int(rc['gasUsed'],16)*int(rc['effectiveGasPrice'],16))/10**18,'f')
h='0xb644bf8e644a1195ad838180fd015f88938a8664128b9e0ad1e7b4a5eebe2198';tx,rc,b=validate(h,'eth_funding_block_');add(stamp(b),'Ethereum (1)',h,tx['from'],tx['to'],'ETH',format(D(int(tx['value'],16))/10**18,'f'),'initial ordinary funding','UNRESOLVED','intact transfer; source-to-affected-wallet link UNRESOLVED','raw_sources/eth_getTransactionByHash_'+h+'.response.json',fee(rc),'No identity inferred from gas funding.')
# Credit amounts in internal transfers are reproduced from execution traces.
internals=read('eth_internal-transactions_1.response.json')['items']
for t in sorted(internals,key=lambda t:(t['block_number'],t['transaction_index'],t['index'])):
 if int(t['value'])<=10**15:continue
 h=t['transaction_hash'];tx,rc,b=validate(h,'eth_incoming_block_');tr=read('trace_transaction_'+h+'.response.json')['result'];matches=[c for c in tr if c.get('action',{}).get('to')==t['to']['hash'].lower() and c['action'].get('from')==t['from']['hash'].lower() and int(c['action'].get('value','0x0'),16)==int(t['value']) and 'error' not in c];assert len(matches)==1
 add(stamp(b),'Ethereum (1)',h,t['from']['hash'],t['to']['hash'],'ETH',format(D(t['value'])/10**18,'f'),'execution-trace native credit','UNRESOLVED','intact execution credit; source-chain match not established','raw_sources/trace_transaction_'+h+'.response.json',notes='Successful transaction receipt; exact internal call reproduced. Protocol attribution/source deposit still requires separate proof.')
# First and second onward hops. Protocol calls are not labelled as fills.
outtx={}
for pat,prefix in [('eth_node_0x*.response.json','eth_node_'),('eth_second_*.response.json','eth_second_')]:
 for f in R.glob(pat):
  a=f.name[len(prefix):-len('.response.json')].lower()
  for t in json.loads(f.read_text()).get('items',[]):
   if t['from']['hash'].lower()==a and int(t['value'])>10**15:outtx[t['hash']]=t
relay=list(csv.DictReader((P/'relay_verified_pairs_v0.2.csv').open()));relay_by_hash={r['source_transaction']:r for r in relay}
for t in sorted(outtx.values(),key=lambda t:(t['block_number'],t.get('position',0))):
 h=t['hash'];tx,rc,b=validate(h,'eth_bridge_block_');is_relay=h in relay_by_hash;add(stamp(b),'Ethereum (1)',h,tx['from'],tx['to'],'ETH',format(D(int(tx['value'],16))/10**18,'f'),'Relay deposit via LI.FI' if is_relay else 'native transfer or protocol call','Relay' if is_relay else 'UNRESOLVED','intact transfer; protocol destination match confirmed separately' if is_relay else 'intact transfer; any cross-chain continuation UNRESOLVED','raw_sources/eth_getTransactionByHash_'+h+'.response.json',fee(rc),'Native value attached to call is not necessarily net bridge output. No double counting across routing stages.')
for r in relay:
 add(r['destination_timestamp_UTC'],'Arbitrum (42161)',r['destination_transaction'],r['destination_token_source'],r['destination_wallet'],'USDC',r['received_USDC'],'matched Relay fill','Relay','deterministic matched order; mixed protocol liquidity','raw_sources/fill_42161_eth_getTransactionReceipt_'+r['destination_transaction']+'.response.json',r['destination_network_fee_ETH'],'Order '+r['order_id']+'; request '+r['request_id']+'. Batched transaction fee is not solely attributable to this order.')
with (P/'evm_extended_ledger_v0.2.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
allrows=base+rows
with (P/'evm_timeline_v0.2.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(sorted(allrows,key=lambda r:(r['timestamp'],r['tx/signature'],r['ID'])))
graph={'scope':'Ethereum routing address and independently reproduced onward hops and Relay fills; affected-wallet origin UNRESOLVED','edges':[{'ledger_id':r['ID'],'timestamp':r['timestamp'],'chain':r['chain'],'source':r['source'],'destination':r['destination'],'asset':r['asset'],'amount':r['amount'],'tx':r['tx/signature'],'classification':r['classification'],'provenance':r['provenance status']} for r in allrows]}
(P/'wallet_graph_evm_v0.2.json').write_text(json.dumps(graph,indent=2)+'\n')
wallets={}
for r in allrows:
 for a in [r['source'],r['destination']]:
  k=(a.lower(),r['chain']);e=wallets.setdefault(k,{'address':a,'chain':r['chain'],'role':'observed transaction participant','first appearance':r['timestamp'],'funding source':'see ledger; not an ownership attribution','outflows':'','known protocol interaction':'','control evidence':'transaction authority only; common beneficial ownership NOT ESTABLISHED','classification':'CONFIRMED','notes':'Role limited to independently reproduced transactions.'});e['first appearance']=min(e['first appearance'],r['timestamp'])
  if a==r['source']:e['outflows']+=r['ID']+';'
  if r['protocol']=='Relay':e['known protocol interaction']='Relay matched deposit/fill'
with (P/'wallet_entity_evm_v0.2.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(next(iter(wallets.values()))));w.writeheader();w.writerows(wallets.values())
ids=[r['ID'] for r in rows];assert len(ids)==len(set(ids));print({'new_ID_range':[ids[0],ids[-1]],'new_rows':len(rows),'wallet_chain_records':len(wallets)})
