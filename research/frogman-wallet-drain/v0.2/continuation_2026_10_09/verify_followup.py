"""Snapshot reconciliation and scoped negative findings; no inferred payouts."""
import datetime,hashlib,json,pathlib
from decimal import Decimal as D
P=pathlib.Path(__file__).parent;R=P/'raw';OLD=P.parent/'continuation_2026_10_08'
previous=json.loads((OLD/'spot_execution_summary.json').read_bytes())
old_ledger=json.loads((OLD/'hyperliquid_summary.json').read_bytes())['rows']
rows=[];comparisons=[]
for account in previous['accounts']:
    user=account['address']
    read=lambda label:json.loads((R/(label+'_'+user+'.response.json')).read_bytes())
    request=lambda label:json.loads((R/(label+'_'+user+'.request.json')).read_bytes())
    ledger=read('userNonFundingLedgerUpdates');fills=read('userFillsByTime');spot=read('spotClearinghouseState');perp=read('clearinghouseState')
    old_updates=json.loads((OLD/'raw'/('hl_ledger_'+user+'.response.json')).read_bytes())
    old_fills=json.loads((OLD/'raw'/('hl_fills_'+user+'.response.json')).read_bytes())
    new_updates=[x for x in ledger if x not in old_updates];new_fills=[x for x in fills if x not in old_fills]
    assert len(ledger)<2000 and len(fills)<2000
    assert not new_updates and not new_fills,'New activity needs separate ledger allocation and review'
    balances={x['coin']:x for x in spot['balances']}
    assert D(balances['XMR1']['total'])==D(account['net_XMR1'])
    assert D(balances['USDC']['total'])==D(account['remaining_spot_USDC'])
    deposits=sum(D(x['amount']) for x in old_ledger if x['action']=='deposit' and x['destination'].startswith(user))
    internal=sum(D(x['amount']) for x in old_ledger if x['action']=='accountClassTransfer' and x['source'].startswith(user))
    balance=D(perp['marginSummary']['totalRawUsd'])
    assert deposits-internal==balance==D(perp['withdrawable'])==D(perp['marginSummary']['accountValue'])
    assert not perp['assetPositions']
    comparisons.append({'address':user,'new_returned_nonfunding_updates':len(new_updates),'new_returned_fills':len(new_fills),'XMR1_snapshot':balances['XMR1']['total'],'spot_USDC_snapshot':balances['USDC']['total'],'perpetual_raw_USD_balance':str(balance),'classification':'CONFIRMED','notes':'Returned API observations only; not proof of complete funding history, no funding-rate review, consensus inclusion, signer or beneficial owner.'})
    rows.append({'ID':f'F{426+len(rows):04d}','timestamp':request('clearinghouseState')['requested_at_UTC'],'timestamp_kind':'request observation UTC, not transaction timestamp','chain':'Hyperliquid account ledger (first-party API)','tx/signature':'','source':user,'destination':user,'asset':'USDC-denominated perpetual account balance','amount':str(balance),'action':'balance snapshot and deposit-to-spot arithmetic reconciliation','protocol':'Hyperliquid','signer/authority':'NOT ESTABLISHED','provenance_status':'intact account association; mixed custody','classification':'CONFIRMED','source_record':'raw/clearinghouseState_'+user+'.response.json','record_type':'balance snapshot, not a fund transfer','notes':'Exact deposit minus internal spot transfer equals observed perpetual raw USD/withdrawable balance; this is not a fee or new loss. Full historical causes and physical coin continuity are not inferred.'})
assert sum(D(r['amount']) for r in rows)==D('0.024994')
(P/'transaction_ledger_F0426_F0431.json').write_text(json.dumps(rows,indent=2)+'\n')
summary={'classification':'CONFIRMED','starting_commit':'8ae2af0c9e3e58f4cb3c0f92a28c5406b7752a33','previous_last_ID':'F0425','new_ID_range':['F0426','F0431'],'query_cutoff':json.loads((P/'query_cutoff.json').read_bytes()),'perpetual_balance_total':'0.024994','accounts':comparisons,'negative_finding_scope':'Six users, two history endpoints from incident start to explicit cutoff, plus separately timed spot/perpetual snapshots. No new returned fills or non-funding updates relative to saved responses; unchanged XMR1 spot balances. Not a claim of absolute absence of withdrawals, undisclosed orders or other-chain activity.','provenance':'No native Monero output or matched Wagyu withdrawal is established.'}
(P/'followup_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
