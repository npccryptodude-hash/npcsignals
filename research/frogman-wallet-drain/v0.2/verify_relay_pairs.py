"""Verify source deposit calls, order identifiers and Arbitrum transfer fills."""
import json,pathlib,decimal,csv,datetime
from Crypto.Hash import keccak
P=pathlib.Path(__file__).parent;R=P/'raw_sources';D=decimal.Decimal
def read(n):return json.loads((R/n).read_text())
def selector(s):k=keccak.new(digest_bits=256);k.update(s.encode());return k.hexdigest()[:8]
def topic(s):k=keccak.new(digest_bits=256);k.update(s.encode());return '0x'+k.hexdigest()
def time(b):return datetime.datetime.fromtimestamp(int(b['timestamp'],16),datetime.timezone.utc).isoformat().replace('+00:00','Z')
assert int(read('arb_usdc_decimals.response.json')['result'],16)==6
rows=[]
for c in sorted(read('relay_order_candidates.json'),key=lambda x:x['source_tx']):
 h=c['source_tx'];o=c['order_id'];tx=read('eth_getTransactionByHash_'+h+'.response.json')['result'];receipt=read('eth_getTransactionReceipt_'+h+'.response.json')['result'];b=read('eth_bridge_block_'+str(int(tx['blockNumber'],16))+'.response.json')['result'];assert tx['blockHash']==receipt['blockHash']==b['hash'];assert h in b['transactions'];assert int(receipt['status'],16)==1
 trace=read('relay_source_trace_'+h+'.response.json')['result'];calls=[t for t in trace if t.get('action',{}).get('to')=='0x4cd00e387622c35bddb9b4c962c136462338bc31' and t['action'].get('input','').startswith('0x'+selector('depositNative(address,bytes32)'))];assert len(calls)==1;call=calls[0];assert 'error' not in call;assert call['action']['input'][-64:]==o[2:];assert int(call['action']['value'],16)==int(c['source_wei']);assert ('0x'+call['action']['input'][34:74]).lower()==c['depositor'].lower()
 event=[l for l in receipt['logs'] if l['address']=='0x4cd00e387622c35bddb9b4c962c136462338bc31' and l['data'].endswith(o[2:])];assert len(event)==1;assert int(event[0]['data'][66:130],16)==int(c['source_wei'])
 fn='relay_order_sample.response.json' if h=='0xa7da5d044b2a34fd2105862dfed7b947254bd7ff12d7567e91be48d649f18d3c' else 'relay_order_'+o+'.response.json';rs=read(fn)['requests'];rs=[r for r in rs if any(t['hash']==h for t in r['data']['inTxs'])];assert len(rs)==1;r=rs[0];assert r['status']=='success';outs=r['data']['outTxs'];assert len(outs)==1;out=outs[0];assert out['chainId']==42161;fh=out['hash'];ft=read('fill_42161_eth_getTransactionByHash_'+fh+'.response.json')['result'];fr=read('fill_42161_eth_getTransactionReceipt_'+fh+'.response.json')['result'];fb=read('fill_block_42161_'+str(int(ft['blockNumber'],16))+'.response.json')['result'];assert ft['blockHash']==fr['blockHash']==fb['hash'];assert fh in fb['transactions'];assert int(fr['status'],16)==1
 # Some fills are batched. Bind the order in calldata and the actual token
 # movement in its receipt; do not assume the outer call is ERC20.transfer.
 assert o[2:] in ft['input'];recipient=r['recipient'].lower();rawamount=int(r['data']['price']);assert recipient==c['depositor'].lower()
 token='0xaf88d065e77c8cc2239327c5edb3a432268e5831'
 logs=[l for l in fr['logs'] if l['address']==token and l['topics'][0]==topic('Transfer(address,address,uint256)') and l['topics'][2][-40:]==recipient[2:] and int(l['data'],16)==rawamount];assert len(logs)==1
 rows.append({'source_timestamp_UTC':time(b),'source_chain_id':1,'source_transaction':h,'source_wallet':tx['from'],'depository_contract':'0x4cd00e387622c35bddb9b4c962c136462338bc31','deposited_ETH':format(D(c['source_wei'])/10**18,'f'),'order_id':o,'request_id':r['id'],'destination_timestamp_UTC':time(fb),'destination_chain_id':42161,'destination_transaction':fh,'destination_wallet':recipient,'destination_token':token,'received_USDC':format(D(rawamount)/10**6,'f'),'classification':'CONFIRMED','provenance_status':'deterministic matched order; mixed protocol liquidity; no ownership inference','API_source_record':'raw_sources/'+fn,'source_network_fee_ETH':format(D(int(receipt['gasUsed'],16)*int(receipt['effectiveGasPrice'],16))/10**18,'f'),'destination_network_fee_ETH':format(D(int(fr['gasUsed'],16)*int(fr['effectiveGasPrice'],16))/10**18,'f')})
rows.sort(key=lambda r:r['source_timestamp_UTC'])
with (P/'relay_verified_pairs_v0.2.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
s={'confirmed_pairs':len(rows),'deposited_ETH':format(sum(D(r['deposited_ETH']) for r in rows),'f'),'received_USDC':format(sum(D(r['received_USDC']) for r in rows),'f'),'receiving_chain_id':42161,'notes':'Exact same protocol order ID appears in source deposit call/log and destination transfer calldata; API supplies independently reproduced fill hash. This verifies an order-level exchange, not identical coin continuity or common beneficial ownership.'};assert len(rows)==6
(P/'relay_verification_summary_v0.2.json').write_text(json.dumps(s,indent=2)+'\n');print(s)
