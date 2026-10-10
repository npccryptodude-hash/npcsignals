"""Offline review: chain inclusion, exact order correlation, token logs and scope limits."""
import hashlib,json,pathlib
P=pathlib.Path(__file__).parent;A=P/'access';U='0x18dd3c14e34c1bc379f7538068c59160d9f68e25';F='0xae06669dfd3e932476f00ea49fce82e5e63f83bf'
def raw(n):return json.loads((A/(n+'.response.txt')).read_text())
def r(n):return raw(n)['result']
old=json.loads((P.parent/'common_funder_bounded_2026_10_10/master_timeline_F0001_F0597.json').read_text())['rows'];new=json.loads((P/'master_timeline_F0001_F0602.json').read_text())['rows'];assert new[:597]==old and sorted(x['ID'] for x in new)==[f'F{i:04}' for i in range(1,603)]
assert r('case_code')==r('snapshot_code')=='0x';assert not raw('metadata')['is_contract'];assert r('snapshot_nonce')=='0x93083'
h=raw('ordinary_history');assert h['message']=='OK' and len(h['result'])==179<1000;hist=h['result'];assert all(26135406<=int(x['blockNumber'])<=26135606 for x in hist);out=[x for x in hist if x['from'].lower()==U];assert len(out)==178 and sorted(int(x['nonce']) for x in out)==list(range(585108,585286));assert int(r('nonce_after'),16)-int(r('nonce_before'),16)==178;assert len(set(x['to'].lower() for x in out))==70;assert raw('internal_history')['result']==[]
for n,chain in [('case',1),('origin',42161),('replenishment',1)]:
 t,q,b=r(n+'_tx'),r(n+'_receipt'),r(n+'_block');assert q['status']=='0x1' and t['hash']==q['transactionHash'] and t['blockHash']==q['blockHash']==b['hash'] and t['blockNumber']==q['blockNumber']==b['number'] and t['hash'] in b['transactions'] and int(t['chainId'],16)==chain
 if chain==1:
  hh=[x for x in hist if x['hash']==t['hash']];assert len(hh)==1;z=hh[0];assert int(z['value'])==int(t['value'],16) and z['from']==t['from'] and z['to']==t['to'] and int(z['gasUsed'])==int(q['gasUsed'],16)
a,b=raw('relay_case_hash'),raw('relay_case_order');assert len(a['requests'])==len(b['requests'])==1;req=a['requests'][0];assert req==b['requests'][0] and req['status']=='success';t,q=r('case_tx'),r('case_receipt');assert t['from']==U and t['to']==F and int(t['value'],16)==372051536035073867
order=req['protocol']['orderId'];assert order==t['input'];dest=req['data']['outTxs'];assert len(dest)==1;d=dest[0];assert d['hash']==t['hash'] and d['chainId']==1 and int(d['data']['value'])==int(t['value'],16) and d['data']['from']==t['from'] and d['data']['to']==t['to'] and d['data']['data']==t['input'] and int(d['fee'])==int(q['gasUsed'],16)*int(q['effectiveGasPrice'],16)
t,q=r('origin_tx'),r('origin_receipt');assert t['from']==F and int(t['value'],16)==0;origin=req['protocol']['deposit']['origin'];assert origin['transactionId']==t['hash'] and origin['depositor']==F and int(origin['amount'])==1002533798;assert req['recipient'].lower()==F
log=q['logs'][2];assert log['address']==origin['depository'];words=[log['data'][2+i*64:2+(i+1)*64] for i in range(4)];assert '0x'+words[0][-40:]==F and '0x'+words[1][-40:]==origin['currency'] and int(words[2],16)==1002533798 and '0x'+words[3]==order
edges=json.loads((P/'origin_token_edges.json').read_text());assert len(edges)==2;assert [(x['source'],x['destination'],x['raw_amount']) for x in edges]==[(F,t['to'],'1002533798'),(t['to'],origin['depository'],'1002533798')];assert all(x['token']==origin['currency'] for x in edges);assert order[2:] in t['input']
f=r('replenishment_tx');assert f['from']==req['protocol']['solver']['address'] and f['to']==U and int(f['value'],16)==5728397486280078839;assert int(r('replenishment_block')['timestamp'],16)>int(r('case_block')['timestamp'],16)
for x in new[597:]:
 for n in x['evidence_files']:assert (P/n).exists()
for n,h in json.loads((P/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((P/n).read_bytes()).hexdigest()==h
print('PASS: 597 prior rows preserved; bounded nonces; successful receipt/block inclusion; exact Relay order/hash/fee match; Arbitrum USDC log chain and order payload; replenishment chronology; evidence and checksums')
