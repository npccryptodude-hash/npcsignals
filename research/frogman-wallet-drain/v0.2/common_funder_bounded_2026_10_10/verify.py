import decimal,hashlib,json,pathlib
P=pathlib.Path(__file__).parent;A=P/'access';B=P.parent;D=decimal.Decimal
U='0xae06669dfd3e932476f00ea49fce82e5e63f83bf'
def raw(n):return json.loads((A/(n+'.response.txt')).read_text())
def r(n):return raw(n)['result']
old=json.loads((B/'hyperliquid_matched_account_2026_10_10/master_timeline_F0001_F0593.json').read_text())['rows'];new=json.loads((P/'master_timeline_F0001_F0597.json').read_text())['rows'];assert new[:593]==old and sorted(x['ID'] for x in new)==[f'F{i:04}' for i in range(1,598)]
h=raw('ordinary_history');assert h['message']=='OK' and len(h['result'])==178<1000;rows=h['result'];assert all(26130000<=int(x['blockNumber'])<=26137480 for x in rows);out=[x for x in rows if x['from'].lower()==U];assert len(out)==177 and sorted(int(x['nonce']) for x in out)==list(range(5342,5519));assert len(set(x['to'].lower() for x in out))==122 and sum(x['value']=='1500000000000000' for x in out)==99
roots={'0x427c4b37de0714821b09c4fc655a713abbcfba83','0x07ae8551be970cb1cca11dd7a11f47ae82e70e67','0x14aa2a71dbb5ef87b81f92205e2699aa4aa65794'};assert not any(roots.intersection({x['from'].lower(),x['to'].lower()}) for x in rows);assert raw('internal_history')['result']==[]
inv=json.loads((P/'case_recipient_inventory.json').read_text());assert len(inv)==10 and [x['nonce'] for x in inv]==list(range(5509,5519));assert sum(D(x['ETH']) for x in inv)==D('0.045284691009863277')
for x in inv:
 hh=x['transaction_hash'];hist=x['ordinary_history_record'];t=json.loads((B/'robinhood_disposal_settlement_2026_10_09/access'/f'{hh}_tx.response.txt').read_text())['result'];q=json.loads((B/'robinhood_disposal_settlement_2026_10_09/access'/f'{hh}_receipt.response.txt').read_text())['result'];assert t['hash']==q['transactionHash']==hist['hash'] and q['status']=='0x1' and t['blockHash']==hist['blockHash']==q['blockHash'] and t['from']==U and t['to']==x['recipient'] and int(t['value'],16)==int(hist['value']) and D(x['ETH'])*10**18==int(hist['value'])
t,q,b=r('inbound_tx'),r('inbound_receipt'),r('inbound_block');assert t['hash']==q['transactionHash'] and q['status']=='0x1' and t['blockHash']==q['blockHash']==b['hash'] and t['blockNumber']==q['blockNumber']==b['number'] and t['hash'] in b['transactions'] and t['to']==U and t['chainId']=='0x1' and int(t['value'],16)==372051536035073867;assert r('funder_case_code')==r('inbound_sender_case_code')=='0x';assert t['hash'] in [x['hash'] for x in rows if x['to'].lower()==U]
for n in ['metadata','inbound_sender_metadata']:
 d=raw(n);assert d['name'] is None and d['public_tags']==[] and not d['is_contract']
for x in new[593:]:
 for f in x['evidence_files']:assert (P/f).exists()
for n,h in json.loads((P/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((P/n).read_bytes()).hexdigest()==h
print('PASS: 593 prior records preserved; ten existing funding edges and total; bounded 178 history records/nonce sequence; new inbound receipt/block inclusion; EOA code; no metadata identity; checksums')
