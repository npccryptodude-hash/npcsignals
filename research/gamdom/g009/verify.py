#!/usr/bin/env python3
"""Offline audit of primary data, derived arithmetic, coverage and frozen files."""
import csv,hashlib,json,pathlib,subprocess,datetime
from derive_records import events,result,balance,D,C,TOKEN,TRANSFER,ANCHOR,generate
R=pathlib.Path(__file__).resolve().parent
BASE='ff920e52ed487b2f0d0a729c6f61f2d31fce4c2a'
REPO=R.parents[1]
def main():
    manifest=json.loads((R/'SHA256SUMS.json').read_text())
    files={str(p.relative_to(R)) for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='SHA256SUMS.json'}
    assert set(manifest)==files
    for n,h in manifest.items():assert hashlib.sha256((R/n).read_bytes()).hexdigest()==h,n
    print('PASS manifest coverage and every SHA-256 digest')
    generated=['canonical_event_ledger.csv','funding_transaction_ledger.csv','historical_balance_reconciliation.csv','inbound_counterparty_totals.csv','upstream_routes.csv','evidence/calculated_summary.json']
    prior={n:(R/n).read_bytes() for n in generated};summary=generate()
    assert prior=={n:(R/n).read_bytes() for n in generated}
    assert result('chain_id')=='0x89'
    logs=events();assert len(logs)==753
    assert len({(x['transactionHash'],x['logIndex']) for x in logs})==753
    for e in logs:
        assert e['address']==TOKEN and e['topics'][0]==TRANSFER and not e['removed']
        assert 93000000<=int(e['blockNumber'],16)<=95434113
        assert D[2:] in [x[-40:] for x in e['topics'][1:]]
        assert len(e['data'])==66 and len(e['topics'])==3
    for pos in [1,2]:
        request=json.loads((R/'evidence'/f'bounded_logs_93000000_95434113_{pos}.json').read_text())['request']
        p=request['params'][0]
        assert p['address']==TOKEN and int(p['fromBlock'],16)==93000000 and int(p['toBlock'],16)==95434113
        assert p['topics'][pos]=='0x'+'0'*24+D[2:]
    print('PASS direct-RPC coverage filters, 753 unique canonical events and deterministic derived records')
    for row in csv.DictReader((R/'funding_transaction_ledger.csv').open()):
        h=row['tx_hash'];receipt=result('receipt_'+h);tx=result('tx_'+h);block=result('block_'+row['block_number'])
        assert receipt['status']=='0x1' and tx['hash']==receipt['transactionHash']==h
        assert tx['from']==row['tx_sender'] and tx['blockHash']==receipt['blockHash']==block['hash']==row['block_hash']
        assert block['transactions'][int(tx['transactionIndex'],16)]==h
        e=next(e for e in receipt['logs'] if int(e['logIndex'],16)==int(row['log_index']))
        assert e['address']==TOKEN and int(e['data'],16)==int(row['raw_amount'])
        assert '0x'+e['topics'][1][-40:]==row['token_sender'] and '0x'+e['topics'][2][-40:]==row['token_recipient']
        assert row['authorization_status']=='UNRESOLVED'
    assert summary['selected_distinct_receipts']==13 and summary['new_distinct_receipts']==12
    print('PASS 13 selected receipts/transactions/header matches; 12 new transactions excluding the existing anchor')
    assert summary['all_reconciliation_variances_raw']==[0,0,0]
    assert balance(95434112)==1579018972 and balance(95434113)==904548002
    assert balance(95399999)==936499001>674470970
    q=[e for e in logs if int(e['blockNumber'],16)==95434113]
    assert len(q)==1 and q[0]['transactionHash']==ANCHOR and int(q[0]['transactionIndex'],16)==19 and int(q[0]['logIndex'],16)==179
    assert int(q[0]['data'],16)==balance(95434112)-balance(95434113)==674470970
    obs=json.loads((R/'evidence/explorer_state_observation.json').read_text())['expanded_storage_tables']
    assert int(obs[0]['before_hex'],16)==balance(95434112) and int(obs[0]['after_hex'],16)==balance(95434113)
    assert int(obs[1]['after_hex'],16)-int(obs[1]['before_hex'],16)==674470970
    print('PASS exact archive balance reconciliation, transaction ordering and independent explorer-display agreement')
    assert summary['prior_D_to_C_event_count']==80 and summary['prior_D_to_C_max_raw']>674470970
    for addr in ['d5fbda4c79f38920159fe5f22df9655fde292d47','e5686aae44d392aa6a0637fd38393859502f8667']:
        assert not any(addr in [t[-40:] for t in e['topics'][1:]] for e in logs)
    print('PASS prior D-to-C relationship and bounded exact-address negative findings')
    for directory in ['research/gamdom-incident-2026-10','research/gamdom-incident-2026-10-g006','research/gamdom-incident-2026-10-g008']:
        names=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'--',directory],cwd=REPO,text=True).splitlines()
        actual={str(p.relative_to(REPO)) for p in (REPO/directory).rglob('*') if p.is_file()}
        assert set(names)==actual
        for n in names:assert (REPO/n).read_bytes()==subprocess.check_output(['git','show',f'{BASE}:{n}'],cwd=REPO),n
    print('PASS G005, G006 and G008 preserved byte-for-byte with no added descendants')
if __name__=='__main__':main()
