#!/usr/bin/env python3
"""Rebuild selected evidence tables using integer accounting; no ownership attribution."""
import json,csv,collections,hashlib
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
M='9XxtEBjxj2Z7DZ775foA1iq2zeZdYMKXD6fq8qCNpump';W='So11111111111111111111111111111111111111112'
def write(name,rows,fields):
 with (ROOT/'data'/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def scale(n,d):return f'{n//10**d}.{n%10**d:0{d}d}'
def instructions(d):
 return [('outer',str(n),i) for n,i in enumerate(d['transaction']['message']['instructions'])]+[('inner',f"{g['index']}.{n}",i) for g in d['meta'].get('innerInstructions',[]) for n,i in enumerate(g['instructions'])]
def analyze():
 tx=[];transfers=[];sales=[];fund=[];launch=[];wallets=collections.defaultdict(set)
 for f in sorted((ROOT/'raw/transactions').glob('*.json')):
  d=json.loads(f.read_text());meta=d['meta'];keys=d['transaction']['message']['accountKeys'];sig=d['transaction']['signatures'][0];ts=datetime.fromtimestamp(d['blockTime'],timezone.utc).isoformat();url='https://solscan.io/tx/'+sig
  assert meta['err'] is None
  signers={k['pubkey'] for k in keys if k['signer']};ix=instructions(d);owners={keys[b['accountIndex']]['pubkey']:b.get('owner','') for b in meta.get('preTokenBalances',[])+meta.get('postTokenBalances',[])}
  for _,_,i in ix:
   a=i.get('parsed',{});info=a.get('info',{})
   if a.get('type') in ['initializeAccount3','initializeAccount2','initializeAccount']:owners[info['account']]=info['owner']
  tx.append(dict(signature=sig,timestamp_utc=ts,slot=d['slot'],block_index=d.get('transaction_index',''),fee_payer=keys[0]['pubkey'],signers=';'.join(sorted(signers)),fee_lamports=meta['fee'],source_url=url,status='CONFIRMED'))
  for w in signers:wallets[w].add('signer')
  rows=[]
  for loc,n,i in ix:
   a=i.get('parsed',{});info=a.get('info',{});typ=a.get('type')
   if typ=='transferChecked':
    mint=info['mint'];raw=int(info['tokenAmount']['amount']);dec=info['tokenAmount']['decimals'];source=info['source'];dest=info['destination'];so=owners.get(source,'');do=owners.get(dest,'')
   elif typ in ['transfer','createAccount','withdraw'] and 'lamports' in info:
    mint='SOL';raw=int(info['lamports']);dec=9;source=info.get('source',info.get('stakeAccount'));dest=info.get('destination',info.get('newAccount'));so=source;do=dest
   else:continue
   row=dict(signature=sig,timestamp_utc=ts,instruction=f'{loc}:{n}',asset=mint,source_account=source,destination_account=dest,source_owner=so,destination_owner=do,amount_raw=raw,amount=scale(raw,dec),source_url=url,status='CONFIRMED');rows.append(row);transfers.append(row)
  if d['slot']==456113658:
   for row in rows:
    if row['asset']==M and row['source_owner']=='9dN1wCpxZ1TcC92ikrsMGvSBJnKKUBkQnCHQHLcdYeNy':
     launch.append(dict(signature=sig,timestamp_utc=ts,block_index=d['transaction_index'],buyer=row['destination_owner'],tokens_raw=row['amount_raw'],tokens=row['amount'],supply_pct=str(row['amount_raw']/10000000000000),in_first_bundle=d['transaction_index'] in range(598,603),source_url=url));wallets[row['destination_owner']].add('launch_buyer')
  if d['blockTime']<1791822753:
   for row in rows:
    if row['asset']=='SOL' and row['destination_account']=='Ft2XtprBymZsGwYUMjsLN6z8WZzguTVa5rFYSuN41S8i':
     idx=next(n for n,k in enumerate(keys) if k['pubkey']==row['source_account']);fund.append(dict(signature=sig,timestamp_utc=ts,source=row['source_account'],destination=row['destination_account'],lamports=row['amount_raw'],sol=row['amount'],source_pre_lamports=meta['preBalances'][idx],source_post_lamports=meta['postBalances'][idx],fee_lamports=meta['fee'],source_url=url));wallets[row['source_account']].add('creator_direct_funder')
  if any('Instruction: Sell' in l for l in meta.get('logMessages',[])):
   for w in sorted(signers):
    inputs=[r for r in rows if r['asset']==M and r['source_owner']==w];receipts=[r for r in rows if r['asset']==W and r['destination_owner']==w and r['source_owner']!=w]
    if inputs:
     amount=sum(r['amount_raw'] for r in inputs);proceeds=sum(r['amount_raw'] for r in receipts);assert proceeds>0,('unresolved proceeds',sig,w)
     sales.append(dict(signature=sig,timestamp_utc=ts,slot=d['slot'],seller=w,tokens_raw=amount,tokens=scale(amount,6),receipt_lamports=proceeds,sol_wsol_receipts=scale(proceeds,9),receipt_accounts=';'.join(r['destination_account'] for r in receipts),source_url=url,status='CONFIRMED gross receipts; net profit NOT ASSESSED'));wallets[w].add('seller')
 sales.sort(key=lambda r:r['tokens_raw'],reverse=True)
 write('transactions.csv',tx,list(tx[0]));write('transfers.csv',transfers,list(transfers[0]));write('launch_buys.csv',launch,list(launch[0]));write('creator_funding.csv',fund,list(fund[0]));write('sales_selected.csv',sales,list(sales[0]) if sales else ['signature','seller','tokens','sol_wsol_receipts']);write('wallets.csv',[dict(address=w,roles=';'.join(sorted(roles)),identity='UNRESOLVED') for w,roles in sorted(wallets.items())],['address','roles','identity'])
 summary={'transaction_receipts':len(tx),'funding_total_lamports':sum(r['lamports'] for r in fund),'bundle_buy_raw':sum(r['tokens_raw'] for r in launch if r['in_first_bundle']),'creation_block_buy_raw':sum(r['tokens_raw'] for r in launch),'selected_sale_token_raw':sum(r['tokens_raw'] for r in sales),'selected_sale_receipt_lamports':sum(r['receipt_lamports'] for r in sales)}
 (ROOT/'data/calculations.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary));print(json.dumps(sales,indent=2))
if __name__=='__main__':analyze()
