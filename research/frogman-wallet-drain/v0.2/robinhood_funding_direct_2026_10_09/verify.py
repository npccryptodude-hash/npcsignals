import hashlib,json,pathlib
P=pathlib.Path(__file__).parent; B=P.parent
old=json.loads((B/'unlabeled_a3ca_verification_2026_10_09/master_timeline_F0001_F0504.json').read_text())['rows'];new=json.loads((P/'master_timeline_F0001_F0522.json').read_text())['rows']
assert new[:504]==old and sorted(x['ID'] for x in new)==[f'F{i:04}' for i in range(1,523)]
def raw(n):return json.loads((P/'access'/(n+'.response.txt')).read_text())
def r(n):return raw(n)['result']
assert r('chain_id')=='0x1237'
origins=[x for x in json.loads((B/'robinhood_linkage_2026_10_09/transaction_ledger_F0435_F0464.json').read_text()) if x['record_type']=='origin deposit']
for o in origins[:8]:
    q=r(o['ID']+'_receipt');assert q['transactionHash']==o['transaction_hash'] and q['status']=='0x1'
    prior=json.loads((B/'robinhood_linkage_2026_10_09/access'/('eth_getTransactionReceipt_'+o['transaction_hash']+'.response.txt')).read_text())['result'];assert q==prior
    assert 'error' in raw(o['ID']+'_pre_balance') and 'error' in raw(o['ID']+'_post_balance')
assert sum(int(x['input_amount_wei']) for x in origins[:8])==64340000000000000000
for f in (P/'access').glob('0x*_tx.response.txt'):
    t=json.loads(f.read_text())['result'];q=r(f.name.replace('_tx.response.txt','_receipt'));b=r('block_'+t['blockNumber']);assert t['hash']==q['transactionHash'] and q['status']=='0x1' and t['blockHash']==q['blockHash']==b['hash'] and t['hash'] in b['transactions']
rows=new[504:];assert sum(int(x['V4_raw_debit']) for x in rows if 'V4_raw_debit' in x)==int(next(x['raw_amount'] for x in rows if x.get('asset_label')=='V4 (prior metadata)'))
assert r('direct_snapshot_code')=='0xef010063c0c19a282a1b52b07dd5a65b58948a07dae32b'
assert '63c0c19a282a1b52b07dd5a65b58948a07dae32b' in (P/'access/metamask_deployments.response.txt').read_text().lower()
for label in ['first_direct_trace','first_contract_trace','first_cashcat_trace','unwrap_trace']:assert 'error' in raw(label)
for rel,h in json.loads((P/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((P/rel).read_bytes()).hexdigest()==h
print('PASS: prior 504 objects preserved, eight origin receipts, source/disposal receipts and totals, dated designator, explicit state/trace failures, evidence hashes')
