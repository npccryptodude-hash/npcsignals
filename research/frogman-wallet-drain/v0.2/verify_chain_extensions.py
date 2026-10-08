"""Verify newly found token transfers; preserve signer vs token sender distinction."""
import json,pathlib,csv,decimal,datetime
P=pathlib.Path(__file__).parent;R=P/'raw_sources';D=decimal.Decimal
TOPIC='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
def read(n):return json.loads((R/n).read_text())
def text(hexdata):
 b=bytes.fromhex(hexdata[2:]);return b[64:64+int.from_bytes(b[32:64],'big')].decode() if len(b)>64 else b.rstrip(b'\0').decode()
groups=[]
for chain,pat in [('rh','rh_window_logs_0_*.response.json'),('arb','arb_USDC_logs_*.response.json'),('rh','rh_window_logs_1_*.response.json')]:
 logs=[]
 for f in R.glob(pat):logs+=read(f.name).get('result',[])
 groups.append((chain,sorted(logs,key=lambda l:(int(l['blockNumber'],16),int(l['transactionIndex'],16),int(l['logIndex'],16)))))
fields=list(next(csv.DictReader((P/'evm_extended_ledger_v0.2.csv').open())));fields+=['token_contract','raw_token_units','log_index','transaction_sender']
rows=[];zero=[]
for chain,logs in groups:
 for l in logs:
  h=l['transactionHash'];tx=read(chain+'_eth_getTransactionByHash_'+h+'.response.json')['result'];rc=read(chain+'_eth_getTransactionReceipt_'+h+'.response.json')['result'];b=read(chain+'_block_'+str(int(l['blockNumber'],16))+'.response.json')['result'];assert tx['blockHash']==rc['blockHash']==b['hash']==l['blockHash'];assert h in b['transactions'];assert int(rc['status'],16)==1;assert l['topics'][0]==TOPIC
  matched=[x for x in rc['logs'] if x['logIndex']==l['logIndex'] and x['address']==l['address'] and x['topics']==l['topics'] and x['data']==l['data']];assert len(matched)==1
  source='0x'+l['topics'][1][-40:];dest='0x'+l['topics'][2][-40:];units=int(l['data'],16)
  if units==0:zero.append({'tx':h,'token_sender_in_event':source,'destination':dest,'transaction_sender':tx['from'],'notes':'Zero-value event, not a monetary outflow; token sender is not necessarily transaction signer.'});continue
  decimals=int(read(chain+'_token_'+l['address']+'_decimals.response.json')['result'],16);symbol=text(read(chain+'_token_'+l['address']+'_symbol.response.json')['result']);row={k:'' for k in fields};row.update({'ID':f'F{187+len(rows):04d}','timestamp':datetime.datetime.fromtimestamp(int(b['timestamp'],16),datetime.timezone.utc).isoformat().replace('+00:00','Z'),'chain':'Robinhood Chain (4663)' if chain=='rh' else 'Arbitrum (42161)','tx/signature':h,'source':source,'destination':dest,'asset':symbol+' (current metadata)','amount':format(D(units)/(10**decimals),'f'),'action':'token transfer event','protocol':'UNRESOLVED','signer/authority if known':tx['from']+' (transaction sender only)','provenance status':'intact token event; downstream mixing/source-chain bridge matches require separate analysis','classification':'CONFIRMED','source_record':'raw_sources/'+chain+'_eth_getTransactionReceipt_'+h+'.response.json','notes':'Token sender and transaction sender recorded separately. Current token metadata is not historical extension-state proof. Transaction fee repeated for context, not allocated per log.','network_fee_ETH':format(D(int(rc['gasUsed'],16)*int(rc['effectiveGasPrice'],16))/10**18,'f'),'nonce':int(tx['nonce'],16),'record_type':'fund transfer event','token_contract':l['address'],'raw_token_units':str(units),'log_index':int(l['logIndex'],16),'transaction_sender':tx['from']});rows.append(row)
with (P/'chain_extension_ledger_v0.2.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
(P/'zero_value_events_v0.2.json').write_text(json.dumps(zero,indent=2)+'\n')
source_rows=[r for r in rows if r['source']=='0x14aa2a71dbb5ef87b81f92205e2699aa4aa65794'];arb_rows=[r for r in rows if r['chain']=='Arbitrum (42161)'];assert len(source_rows)==3;assert len(arb_rows)==6;assert sum(D(r['amount']) for r in arb_rows)==D('561850.214994')
summary={'ledger_range':[rows[0]['ID'],rows[-1]['ID']],'rows':len(rows),'earliest_reproduced_Robinhood_transfer_UTC':source_rows[0]['timestamp'],'source_transfers':source_rows,'Arbitrum_consolidation_destination':'0x2df1c51e09aecf9cacb7bc98cb1742757f163df7','Arbitrum_USDC_consolidated':str(sum(D(r['amount']) for r in arb_rows)),'zero_value_events_excluded':len(zero),'scope':'Robinhood source and candidate Transfer events in 20:10–21:10 UTC window; Arbitrum USDC sender-filter logs in blocks 512422000–512820654. Does not establish no earlier native/approval transactions or later outflows.'}
(P/'chain_extension_summary_v0.2.json').write_text(json.dumps(summary,indent=2)+'\n');print({k:v for k,v in summary.items() if k!='source_transfers'})
