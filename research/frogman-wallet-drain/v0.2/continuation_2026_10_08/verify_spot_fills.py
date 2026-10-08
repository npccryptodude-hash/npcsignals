"""Preserve each API-reproduced execution and reconcile with observed spot state."""
import csv,datetime,json,pathlib
from decimal import Decimal as D
P=pathlib.Path(__file__).parent;R=P/'raw'
meta=json.loads((R/'hl_spot_meta.response.json').read_bytes())
market=next(x for x in meta['universe'] if x['index']==260)
assert market['tokens']==[404,0]
base=next(x for x in meta['tokens'] if x['index']==404);quote=next(x for x in meta['tokens'] if x['index']==0)
assert base['name']=='XMR1' and quote['name']=='USDC'
case=[r for r in csv.DictReader((P.parent/'chain_extension_ledger_v0.2.csv').open()) if r['ID'] in ['F0190','F0191','F0192','F0193','F0194','F0195']]
events=[]; accounts=[]
for original in case:
    user=original['source'];fills=json.loads((R/('hl_fills_'+user+'.response.json')).read_bytes())
    assert len(fills)<2000 and all(f['coin']=='@260' and f['side']=='B' and f['feeToken']=='XMR1' for f in fills)
    assert len({f['tid'] for f in fills})==len(fills)
    state=json.loads((R/('hl_spot_state_'+user+'.response.json')).read_bytes())
    balances={x['coin']:x for x in state['balances']}
    gross=sum(D(f['sz']) for f in fills);fee=sum(D(f['fee']) for f in fills);cost=sum(D(f['px'])*D(f['sz']) for f in fills)
    assert gross-fee==D(balances['XMR1']['total'])
    assert cost==D(balances['XMR1']['entryNtl'])
    updates=json.loads((R/('hl_ledger_'+user+'.response.json')).read_bytes())
    spot_credit=sum(D(x['delta']['usdc']) for x in updates if x['delta']['type']=='accountClassTransfer' and x['delta']['toPerp'] is False)
    assert spot_credit-cost==D(balances['USDC']['total'])
    accounts.append({'address':user,'fill_count':len(fills),'gross_XMR1':str(gross),'fees_XMR1':str(fee),'net_XMR1':str(gross-fee),'USDC_cost':str(cost),'remaining_spot_USDC':balances['USDC']['total'],'classification':'CONFIRMED','scope':'First-party API execution records and separately retrieved current spot-state arithmetic. Not a native Monero receipt, external withdrawal, signer or beneficial-owner proof.'})
    for f in fills:
        events.append((user,f,original['ID']))
events.sort(key=lambda e:(e[1]['time'],e[1]['tid']))
rows=[]
for n,(user,f,related) in enumerate(events,221):
    rows.append({'ID':f'F{n:04d}','timestamp':datetime.datetime.fromtimestamp(f['time']/1000,datetime.timezone.utc).isoformat(timespec='milliseconds').replace('+00:00','Z'),'chain':'Hyperliquid spot account ledger (first-party API)','tx/signature':f['hash'],'source':user+' spot USDC account','destination':user+' spot XMR1 account','asset':'XMR1 (Hyperliquid token index 404)','amount':f['sz'],'USD value if available':'','action':'spot buy fill','protocol':'Hyperliquid spot market @260','signer/authority if known':'NOT ESTABLISHED by read-only API response','provenance status':'intact account execution association; mixed protocol custody','classification':'CONFIRMED','source_record':'raw/hl_fills_'+user+'.response.json','notes':'API execution record, not independently reproduced HyperCore consensus inclusion. XMR1 is not proof of native Monero receipt. Gross bought amount before separately recorded XMR1 fee. No extra incident loss counted.','price_USDC':f['px'],'USDC_spent':str(D(f['px'])*D(f['sz'])),'fee_asset':f['feeToken'],'fee_amount':f['fee'],'order_ID':f['oid'],'trade_ID':f['tid'],'client_order_ID':f.get('cloid',''),'related_ledger_ID':related,'record_type':'spot execution account record'})
with (P/'spot_fills_F0221_F0425.csv').open('w',newline='') as output:
    writer=csv.DictWriter(output,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
assert len(rows)==205 and rows[-1]['ID']=='F0425'
summary={'classification':'CONFIRMED','ledger_range':['F0221','F0425'],'fill_count':len(rows),'market_snapshot':market,'base_token_snapshot':base,'quote_token_snapshot':quote,'accounts':accounts,'total_USDC_cost':str(sum(D(a['USDC_cost']) for a in accounts)),'total_net_XMR1':str(sum(D(a['net_XMR1']) for a in accounts)),'total_fees_XMR1':str(sum(D(a['fees_XMR1']) for a in accounts)),'total_remaining_spot_USDC':str(sum(D(a['remaining_spot_USDC']) for a in accounts)),'limits':'Current metadata and separately timed account snapshots are not historical consensus proofs. Full lifetime funding, native Monero conversion, issuer redemption, ultimate beneficiary and account control remain UNRESOLVED.'}
(P/'spot_execution_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print({k:v for k,v in summary.items() if k not in ['accounts','base_token_snapshot','quote_token_snapshot','market_snapshot']})
