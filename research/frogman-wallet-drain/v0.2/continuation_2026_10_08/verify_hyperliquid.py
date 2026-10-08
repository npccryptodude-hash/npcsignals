"""Reproduce first-party account-ledger associations without coin or owner inference."""
import csv,datetime,json,pathlib
from decimal import Decimal
P=pathlib.Path(__file__).parent; R=P/'raw'
original=list(csv.DictReader((P.parent/'chain_extension_ledger_v0.2.csv').open()))
case=[r for r in original if r['ID'] in ['F0190','F0191','F0192','F0193','F0194','F0195']]
rows=[]
for r in case:
    updates=json.loads((R/('hl_ledger_'+r['source']+'.response.json')).read_bytes())
    deposits=[x for x in updates if x['delta']['type']=='deposit' and x['hash']==r['tx/signature']]
    assert len(deposits)==1 and Decimal(deposits[0]['delta']['usdc'])==Decimal(r['amount'])
    assert len(updates)<2000, 'Do not claim completeness if API result cap is reached'
    for x in updates:
        assert x['delta']['type'] in ['deposit','accountClassTransfer']
        d=x['delta']; isdeposit=d['type']=='deposit'
        rows.append({'ID':f'F{209+len(rows):04d}','timestamp':datetime.datetime.fromtimestamp(x['time']/1000,datetime.timezone.utc).isoformat(timespec='milliseconds').replace('+00:00','Z'),'chain':'Hyperliquid account ledger (first-party API)','tx/signature':x['hash'],'source':'Arbitrum bridge credit' if isdeposit else r['source']+' perpetual account','destination':r['source']+(' Hyperliquid account' if isdeposit else ' spot account'),'asset':'USDC ledger units','amount':d['usdc'],'USD value if available':'','action':d['type'],'protocol':'Hyperliquid','signer/authority if known':'NOT ESTABLISHED by unsigned read-only API response','provenance status':'intact exact deposit-hash/account linkage; mixed bridge custody' if isdeposit else 'intact account-ledger association; physical pooled funds mixed','classification':'CONFIRMED','source_record':'raw/hl_ledger_'+r['source']+'.response.json','notes':'First-party API observation, not independently reproduced HyperCore consensus inclusion or signer proof. Deposit credit is the accounting representation of an already ledgered Arbitrum transfer, not new proceeds. Transfer to spot is internal, not an external payout.','related_ledger_ID':r['ID'],'record_type':'accounting representation' if isdeposit else 'internal account ledger update','toPerp':str(d.get('toPerp',''))})
rows.sort(key=lambda r:r['timestamp'])
for n,r in enumerate(rows,209):r['ID']=f'F{n:04d}'
with (P/'hyperliquid_ledger_F0209_F0220.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
total=sum(Decimal(r['amount']) for r in rows if r['action']=='deposit')
spot=sum(Decimal(r['amount']) for r in rows if r['action']=='accountClassTransfer')
assert total==Decimal('561850.214994')
summary={'classification':'CONFIRMED','scope':'Six first-party account-ledger responses; query period 1791317400000–1791464400000 ms. Not a HyperCore consensus proof, lifetime completeness assertion, signer verification or physical coin match.','exact_hash_and_amount_matched_deposits':6,'deposit_credits_USDC':str(total),'internal_transfers_to_spot_USDC':str(spot),'arithmetic_difference_USDC':str(total-spot),'difference_explanation':'UNRESOLVED; not assigned to a fee, loss, retained balance or rounding without account evidence.','ledger_range':['F0209','F0220'],'rows':rows,'provenance':'Deterministic deposit-account association reproduced; physical custody mixed. Arbitrary bridge withdrawals remain unmatched.','negative_findings':'No beneficial owner, compromise method, recovery or ultimate beneficiary established.'}
(P/'hyperliquid_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print({k:v for k,v in summary.items() if k!='rows'})
