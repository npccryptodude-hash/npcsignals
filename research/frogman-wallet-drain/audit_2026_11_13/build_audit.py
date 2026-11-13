"""offline decimal reconciliation of preserved responses; fails on incomplete collection."""
import json,csv,datetime,hashlib
from decimal import Decimal as D
from pathlib import Path
P=Path(__file__).resolve().parent;R=P/'raw'
def load(n):return json.loads((R/(n+'.json')).read_text())
def utc(t):return datetime.datetime.fromtimestamp(t/1000,datetime.timezone.utc).isoformat()
def s(n):return format(n,'f')
meta=load('spotMeta');token=next(t for t in meta['tokens'] if t['name']=='XMR1');pair=next(t for t in meta['universe'] if t['tokens']==[token['index'],0]);coin=pair['name']
old=json.loads((P.parent/'v0.2/continuation_2026_10_08/hyperliquid_summary.json').read_text())
oldset={r['destination'].split()[0].lower() for r in old['rows'] if r['action']=='deposit'}
extra='0x3e2d81f7a5659e4760ba929ef88eed40ef6640a1';a3='0xa3ca6199d8692ec40d0287e615b48d0e8cde9abe'
rows=[];allfills=[];allledger=[]
cut=int(datetime.datetime(2026,10,14,tzinfo=datetime.timezone.utc).timestamp()*1000)
for r in json.loads((P/'receipts.json').read_text()):
 assert r['status']=='confirmed'
 n=r['id'];addr=r['sender'];rc=load(n+'_receipt')['result'];tx=load(n+'_tx')['result'];bl=load(n+'_block')['result']
 assert rc['transactionHash'].lower()==tx['hash'].lower()==r['tx']
 assert rc['blockHash']==tx['blockHash']==bl['hash'] and r['tx'] in [x.lower() if isinstance(x,str) else x['hash'].lower() for x in bl['transactions']]
 assert int(bl['number'],16)==r['block'] and tx['from'].lower()==addr
 f=load(n+'_userFillsByTime');l=load(n+'_userNonFundingLedgerUpdates');state=load(n+'_spotClearinghouseState');perp=load(n+'_clearinghouseState');orders=load(n+'_openOrders')
 assert isinstance(f,list) and len(f)<500 and isinstance(l,list) and len(l)<500
 assert len({(x['hash'],x['tid']) for x in f})==len(f)
 deposits=[x for x in l if x['delta']['type']=='deposit'];matched=[x for x in deposits if x['hash'].lower()==r['tx']]
 amount=D(r['usdc_raw'])/10**6
 assert len(matched)==1 and D(matched[0]['delta']['usdc'])==amount
 xf=[x for x in f if x['coin']==coin]
 buys=sum((D(x['sz']) for x in xf if x['side']=='B'),D(0));sells=sum((D(x['sz']) for x in xf if x['side']=='A'),D(0));fees=sum((D(x['fee']) for x in xf if x['feeToken']=='XMR1'),D(0))
 feeusdc=sum((D(x['fee']) for x in xf if x['feeToken']=='USDC'),D(0))
 net=buys-sells-fees
 xb=next((x for x in state['balances'] if x['token']==token['index']),{'total':'0','hold':'0'})
 spotusdc=sum((D(x['total']) for x in state['balances'] if x['token']==0),D(0));trans=sum((D(x['delta']['usdc'])*(1 if not x['delta']['toPerp'] else -1) for x in l if x['delta']['type']=='accountClassTransfer'),D(0))
 spent=sum((D(x['sz'])*D(x['px'])*(1 if x['side']=='B' else -1) for x in xf),D(0))
 other=[x for x in l if x['delta']['type'] not in ['deposit','accountClassTransfer']]
 # never silently reconcile unexplained transfers or other markets
 assert not other and len(f)==len(xf) and len(deposits)==1
 assert net==D(xb['total']) and trans-spent-feeusdc==spotusdc
 assert amount-trans==D(perp['marginSummary']['accountValue'])
 times=[x['time'] for x in f+l]
 checked=json.loads((R/(n+'_spotClearinghouseState.meta.json')).read_text())['retrieved_utc']
 row={**r,'verified_usdc':s(amount),'hyperliquid_credit_usdc':s(D(matched[0]['delta']['usdc'])),'credit_time_utc':utc(matched[0]['time']),'xmr1_fills':len(xf),'xmr1_bought':s(buys),'xmr1_sold':s(sells),'xmr1_fees':s(fees),'usdc_trade_fees':s(feeusdc),'net_xmr1':s(net),'current_xmr1':xb['total'],'xmr1_on_hold':xb['hold'],'usdc_spent':s(spent),'spot_usdc':s(spotusdc),'perp_usdc':perp['marginSummary']['accountValue'],'withdrawals_or_other_transfers_returned':len(other),'post_13_oct_records':sum(x['time']>=cut for x in f+l),'last_documented_activity_utc':utc(max(times)),'checked_at_utc':checked,'history_end_utc':utc(json.loads((R/(n+'_userFillsByTime.meta.json')).read_text())['request']['endTime']),'open_orders':len(orders),'earlier_scope':'six relay accounts' if addr in oldset else 'separate mayan account' if addr==extra else 'additional across credit already in archive' if addr==a3 else 'newly reconciled account','evidence_status':'confirmed','primary_url':'https://arbiscan.io/tx/'+r['tx'],'hl_url':'https://app.hyperliquid.xyz/explorer/address/'+addr,'raw_prefix':'raw/'+n}
 rows.append(row)
 allfills.extend({'account_id':n,'account':addr,**x} for x in f);allledger.extend({'account_id':n,'account':addr,**x} for x in l)
for row in rows:
 for typ in ['userFillsByTime','userNonFundingLedgerUpdates']:
  assert load(row['id']+'_post_13_oct_'+typ)==[]
assert len(rows)==len({r['sender'] for r in rows})==35
assert len([r for r in rows if r['sender'] in oldset])==6
summary={'accounts':len(rows),'metadata_token':token,'market':pair,'totals':{k:s(sum((D(r[k]) for r in rows),D(0))) for k in ['verified_usdc','hyperliquid_credit_usdc','xmr1_bought','xmr1_sold','xmr1_fees','net_xmr1','current_xmr1','usdc_spent','spot_usdc','perp_usdc']},'fills':len(allfills),'ledger_records':len(allledger),'post_13_oct_records':sum(r['post_13_oct_records'] for r in rows),'withdrawals_or_other_transfers_returned':sum(r['withdrawals_or_other_transfers_returned'] for r in rows),'snapshot_start_utc':min(r['checked_at_utc'] for r in rows),'snapshot_end_utc':max(r['checked_at_utc'] for r in rows),'earliest_history_end_utc':min(r['history_end_utc'] for r in rows),'last_activity_utc':max(r['last_documented_activity_utc'] for r in rows),'overlap':{x:sum(r['earlier_scope']==x for r in rows) for x in {r['earlier_scope'] for r in rows}}}
for n,d in [('accounts',rows),('summary',summary),('fills',allfills),('ledger',allledger)]: (P/(n+'.json')).write_text(json.dumps(d,indent=2)+'\n')
with (P/'accounts.csv').open('w') as out:w=csv.DictWriter(out,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
header='# frogman / 35-account audit\n\nall amounts are token units, not a dollar valuation. confirmed means reproduced rpc/api facts within the recorded scope; no human attribution or native monero receipt is established. current spot balances were collected at different timestamps; see each row. histories are bounded by each recorded request end time.\n\n'
header+='[machine-readable table](accounts.csv) · [exact totals](summary.json) · [method and limitations](README.md)\n\n'
header+='| id / primary tx | full account | usdc deposit / matched credit | xmr1 bought / sold / fee / net | withdrawals returned | last activity utc | checked utc | status / raw |\n|---|---|---:|---|---|---|---|---|\n'
for r in rows:header+=f"| [{r['id']}]({r['primary_url']}) | `{r['sender']}` | {r['verified_usdc']} / {r['hyperliquid_credit_usdc']} | {r['xmr1_bought']} / {r['xmr1_sold']} / {r['xmr1_fees']} / {r['net_xmr1']} | {r['withdrawals_or_other_transfers_returned']} | {r['last_documented_activity_utc']} | {r['checked_at_utc']} | confirmed / [ledger]({r['raw_prefix']}_userNonFundingLedgerUpdates.json) / [fills]({r['raw_prefix']}_userFillsByTime.json) / [state]({r['raw_prefix']}_spotClearinghouseState.json) |\n"
(P/'ACCOUNT_AUDIT.md').write_text(header)
print(json.dumps(summary,indent=2))
