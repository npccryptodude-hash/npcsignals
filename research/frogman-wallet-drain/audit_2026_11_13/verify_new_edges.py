import json,datetime,base64
from decimal import Decimal as D
from pathlib import Path
P=Path(__file__).resolve().parent;R=P/'raw'
def load(n):return json.loads((R/(n+'.json')).read_text())
def result(n):return load(n)['result']
def inclusion(t,r,b):
 assert t['hash']==r['transactionHash'] and t['blockHash']==r['blockHash']==b['hash']
 assert int(r['status'],16)==1 and t['hash'] in [x if isinstance(x,str) else x['hash'] for x in b['transactions']]
def utc(b):return datetime.datetime.fromtimestamp(int(b['timestamp'],16),datetime.timezone.utc).isoformat()
t=json.loads((P/'holding_outgoing_candidates.json').read_text())[0];r=result('eth_holding_outgoing_receipt_0');b=result('eth_holding_first_outgoing_block');inclusion(t,r,b)
assert int(result('eth_source_before'),16)-int(result('eth_source_after'),16)==int(t['value'],16)+int(r['gasUsed'],16)*int(r['effectiveGasPrice'],16)
first={'hash':t['hash'],'utc':utc(b),'from':t['from'],'to':t['to'],'eth':str(D(int(t['value'],16))/10**18),'gas_eth':str(D(int(r['gasUsed'],16)*int(r['effectiveGasPrice'],16))/10**18),'source_before_eth':str(D(int(result('eth_source_before'),16))/10**18),'source_after_eth':str(D(int(result('eth_source_after'),16))/10**18),'source_later_eth':str(D(int(result('ethereum_4eth_balance_retry'),16))/10**18),'classification':'confirmed transfer and dated states; later replenishment origin unresolved'}
t2=json.loads((P/'bbae_outgoing_candidates.json').read_text())[0];r2=result('eth_bbae_outgoing_receipt_0');b2=result('eth_bbae_first_outgoing_block');inclusion(t2,r2,b2)
created=next(x for x in r2['logs'] if x['address']=='0x40ffe85a28dc9993541449464d7529a922142960' and x['topics'][0]=='0x918554b6bd6e2895ce6553de5de0e1a69db5289aa0e4fe193a0dcd1f14347477')
second={'hash':t2['hash'],'utc':utc(b2),'from':t2['from'],'to':t2['to'],'eth':str(D(int(t2['value'],16))/10**18),'order_hash':created['data'],'classification':'confirmed ethereum native/weth lock and order event; solana settlement association supported pending independent order-state/pda verification'}
# extra account is outside the 35 inventory
l=load('new_relay_destination_userNonFundingLedgerUpdates');credit=next(x for x in l if x['delta']['type']=='deposit');t=result('new36_deposit_tx');r=result('new36_deposit_receipt');b=result('new36_deposit_block');inclusion(t,r,b);assert t['hash']==credit['hash']
a='0xa8f219e59033fe2593151d951a142c1f958fd949';assert a not in {x['sender'] for x in json.loads((P/'accounts.json').read_text())}
ev=[x for x in r['logs'] if x['address'].lower()=='0xaf88d065e77c8cc2239327c5edb3a432268e5831' and len(x['topics'])==3 and x['topics'][1][-40:].lower()==a[2:] and x['topics'][2][-40:].lower()=='2df1c51e09aecf9cacb7bc98cb1742757f163df7'];assert len(ev)==1
amount=D(int(ev[0]['data'],16))/10**6;assert amount==D(credit['delta']['usdc'])==D('55.56914')
f=load('new_relay_destination_userFillsByTime');assert len(f)==1 and f[0]['coin']=='@260' and f[0]['side']=='B' and f[0]['feeToken']=='XMR1';net=D(f[0]['sz'])-D(f[0]['fee']);state=load('new_relay_destination_spotClearinghouseState');assert net==D(next(x['total'] for x in state['balances'] if x['coin']=='XMR1'))
perp=load('new_relay_destination_clearinghouseState');spotusdc=D(next(x['total'] for x in state['balances'] if x['coin']=='USDC'));cost=D(f[0]['px'])*D(f[0]['sz']);assert cost+spotusdc+D(perp['marginSummary']['accountValue'])==amount
extra={'account':a,'deposit_tx':credit['hash'],'usdc':str(amount),'xmr1_gross':f[0]['sz'],'xmr1_fee':f[0]['fee'],'xmr1_net':str(net),'spot_usdc':str(spotusdc),'perp_usdc':perp['marginSummary']['accountValue'],'classification':'confirmed deposit/credit/fill/balance facts; retained separately from external 35','check_time_utc':json.loads((R/'new_relay_destination_spotClearinghouseState.meta.json').read_text())['retrieved_utc']}
# relay source/destination exact 32-byte correspondence plus first-party hash pair
relay=load('near_0473_relay_lookup')['requests'][0];sol=result('near_0473sol_recipient_tx_0');arb=result('new_relay_arb_tx');ar=result('new_relay_arb_receipt');ab=result('new_relay_arb_block');inclusion(arb,ar,ab)
assert relay['data']['inTxs'][0]['hash']==sol['transaction']['signatures'][0] and relay['data']['outTxs'][0]['hash']==arb['hash']
event=base64.b64decode(next(x[14:] for x in sol['meta']['logMessages'] if x.startswith('Program data: ')));identifier=event[-32:].hex();assert arb['input'].endswith(identifier)
assert any(x['address'].lower()=='0xaf88d065e77c8cc2239327c5edb3a432268e5831' and x['topics'][2][-40:].lower()==a[2:] and int(x['data'],16)==55569140 for x in ar['logs'] if len(x['topics'])==3)
summary={'oct27_outflow':first,'oct27_mayan_lock':second,'additional_hyperliquid_account':extra,'relay_correspondence':{'api_request':relay['id'],'source_signature':sol['transaction']['signatures'][0],'destination_hash':arb['hash'],'matching_32_byte_identifier':'0x'+identifier,'output_usdc':'55.56914','scope':'exact first-party in/out pair, successful source transfer and destination receipt, identical 32-byte event/calldata field; standalone program-source decoding not performed'},'scope':'no human identity, exclusive mixed-balance allocation, native monero redemption or exhaustive platform inventory claim'}
(P/'new_edges_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
