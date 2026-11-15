#!/usr/bin/env python3
"""Deterministically derive integer ledgers from saved RPC requests/responses. Offline."""
import csv, json, pathlib, collections, datetime
R=pathlib.Path(__file__).resolve().parent
E=R/'evidence'
D='0xe757683a51cfd002de479385c2f4c9db10a5e8d2'
C='0xacc0c1f672b03b9a5fed4535f840f09b85f40e98'
TOKEN='0xc2132d05d31c914a87c6611c10748aeb04b58e8f'
TRANSFER='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
ANCHOR='0x5e1fd78c9b4f5881d28eb2f14f0c59b32bda206a942a6956316c07965b570591'
def result(name):return json.loads((E/(name+'.json')).read_text())['response']['result']
def amount(n):return f'{n//1000000}.{n%1000000:06d}'
def utc(n):return datetime.datetime.fromtimestamp(n,datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def balance(b):return int(result('balance_'+str(b)),16)
def events():
    logs=[]
    for pos in [1,2]:logs+=result('bounded_logs_93000000_95434113_'+str(pos))
    unique={(x['transactionHash'],x['logIndex']):x for x in logs}
    return sorted(unique.values(),key=lambda e:tuple(int(e[k],16) for k in ['blockNumber','transactionIndex','logIndex']))
def writecsv(name,rows):
    with (R/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def eventrow(e):
    return dict(chain='Polygon',tx_hash=e['transactionHash'],block_number=int(e['blockNumber'],16),block_hash=e['blockHash'],transaction_index=int(e['transactionIndex'],16),log_index=int(e['logIndex'],16),utc_timestamp=utc(int(e['blockTimestamp'],16)),token_contract=e['address'],token_sender='0x'+e['topics'][1][-40:],token_recipient='0x'+e['topics'][2][-40:],raw_amount=str(int(e['data'],16)),decimals=6,amount=amount(int(e['data'],16)),event_verification='CONFIRMED RPC eth_getLogs',receipt_and_tx_metadata='NOT ASSESSED unless matched in funding_transaction_ledger.csv')
def generate():
    logs=events()
    writecsv('canonical_event_ledger.csv',[eventrow(e) for e in logs])
    receipts={p.stem[8:]:json.loads(p.read_text())['response']['result'] for p in E.glob('receipt_*.json')}
    selected=[]
    for h,receipt in receipts.items():
        tx=result('tx_'+h);block=result('block_'+str(int(receipt['blockNumber'],16)))
        for e in receipt['logs']:
            if e['address']!=TOKEN or len(e['topics'])!=3 or e['topics'][0]!=TRANSFER:continue
            if D[2:] not in [x[-40:] for x in e['topics'][1:]]:continue
            q=dict(e);q['blockTimestamp']=block['timestamp'];row=eventrow(q)
            row.update(tx_sender=tx['from'],tx_to=tx['to'] or 'contract creation',tx_nonce=int(tx['nonce'],16),tx_success=int(receipt['status'],16)==1,fee_payer=tx['from'],fee_raw_wei=str(int(receipt['gasUsed'],16)*int(receipt['effectiveGasPrice'],16)),fee_asset='POL',source_url='https://polygonscan.com/tx/'+h,raw_receipt='evidence/receipt_'+h+'.json',raw_transaction='evidence/tx_'+h+'.json',evidence_level='CONFIRMED',new_transaction=h!=ANCHOR,authorization_status='UNRESOLVED')
            if h==ANCHOR:row['role']='existing G008 anchor; new RPC/state verification only'
            elif row['token_sender']==D:row['role']='historical D outflow'
            elif tx['to']==TOKEN:row['role']='direct canonical-token transfer'
            elif tx['to'] is None:row['role']='contract-creation transaction; unsolicited micro-transfer; no control inference'
            else:row['role']='contract-routed inflow; same-transaction input route assessed separately'
            selected.append(row)
    selected.sort(key=lambda x:(x['block_number'],x['transaction_index'],x['log_index']))
    writecsv('funding_transaction_ledger.csv',selected)
    cases=[('full bounded interval',93000000,95434113),('recent pre-anchor',95400000,95434112),('anchor block',95434113,95434113)]
    reconciliation=[]
    for label,lo,hi in cases:
        q=[e for e in logs if lo<=int(e['blockNumber'],16)<=hi]
        inf=sum(int(e['data'],16) for e in q if '0x'+e['topics'][2][-40:]==D)
        outf=sum(int(e['data'],16) for e in q if '0x'+e['topics'][1][-40:]==D)
        op=balance(lo-1);cl=balance(hi)
        reconciliation.append(dict(scope=label,start_block=lo,end_block=hi,opening_state_block=lo-1,opening_raw=op,inflow_raw=inf,outflow_raw=outf,calculated_closing_raw=op+inf-outf,observed_closing_raw=cl,variance_raw=cl-(op+inf-outf),decimals=6,opening=amount(op),inflows=amount(inf),outflows=amount(outf),closing=amount(cl),source='Tenderly archive eth_call and eth_getLogs; no zero-opening assumption'))
    writecsv('historical_balance_reconciliation.csv',reconciliation)
    sources=collections.defaultdict(lambda:{'events':0,'raw':0})
    prior=[]
    for e in logs:
        fr='0x'+e['topics'][1][-40:];to='0x'+e['topics'][2][-40:]
        if to==D:sources[fr]['events']+=1;sources[fr]['raw']+=int(e['data'],16)
        if fr==D and to==C and e['transactionHash']!=ANCHOR:prior.append(e)
    writecsv('inbound_counterparty_totals.csv',[dict(token_sender=k,event_count=v['events'],raw_total=v['raw'],decimals=6,total=amount(v['raw']),scope='bounded canonical logs; token sender is not necessarily transaction signer') for k,v in sorted(sources.items(),key=lambda x:-x[1]['raw'])])
    routes=[]
    for h in receipts:
        tx=result('tx_'+h);rr=receipts[h]
        credits=[x for x in selected if x['tx_hash']==h and x['token_recipient']==D]
        if not credits:continue
        inputs=[]
        for e in rr['logs']:
            if len(e['topics'])==3 and e['topics'][0]==TRANSFER and '0x'+e['topics'][1][-40:]==tx['from'] and tx['to'] is not None and ('0x'+e['topics'][2][-40:]==D or tx['to']!=TOKEN):
                inputs.append(dict(contract=e['address'],raw_amount=str(int(e['data'],16)),recipient='0x'+e['topics'][2][-40:]))
        routes.append(dict(tx_hash=h,initiator=tx['from'],entry_contract=tx['to'] or 'creation',native_input_wei=str(int(tx['value'],16)),observed_initiator_erc20_inputs=json.dumps(inputs,separators=(',',':')),USDT0_to_D_raw=sum(int(x['raw_amount']) for x in credits),route_class='direct transfer' if tx['to']==TOKEN else 'contract transaction; same-chain swap evidence only where reciprocal token logs exist',cross_chain_source='NOT ESTABLISHED',exclusive_anchor_funding='UNRESOLVED'))
    writecsv('upstream_routes.csv',routes)
    summary=dict(event_count=len(logs),incoming_events=sum('0x'+x['topics'][2][-40:]==D for x in logs),outgoing_events=sum('0x'+x['topics'][1][-40:]==D for x in logs),selected_distinct_receipts=len(receipts),new_distinct_receipts=len(receipts)-1,prior_D_to_C_event_count=len(prior),prior_D_to_C_raw_total=sum(int(x['data'],16) for x in prior),prior_D_to_C_min_raw=min(int(x['data'],16) for x in prior),prior_D_to_C_max_raw=max(int(x['data'],16) for x in prior),anchor_block_D_events=sum(int(x['blockNumber'],16)==95434113 for x in logs),opening_state_raw=balance(92999999),pre_anchor_state_raw=balance(95434112),post_anchor_state_raw=balance(95434113),pre_recent_state_raw=balance(95399999),all_reconciliation_variances_raw=[x['variance_raw'] for x in reconciliation])
    (E/'calculated_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    return summary
if __name__=='__main__':print(json.dumps(generate(),indent=2,sort_keys=True))
