import hashlib,json,pathlib
from protocol import gateway_path,keccak
P=pathlib.Path(__file__).parent;B=P.parent
old=json.loads((B/'robinhood_funding_direct_2026_10_09/master_timeline_F0001_F0522.json').read_text())['rows'];new=json.loads((P/'master_timeline_F0001_F0538.json').read_text())['rows'];assert new[:522]==old and sorted(x['ID'] for x in new)==[f'F{i:04}' for i in range(1,539)]
def raw(n):return json.loads((P/'access'/(n+'.response.txt')).read_text())
def r(n):return raw(n)['result']
edges=json.loads((P/'funding_edges.json').read_text());assert len(edges)==7 and sum(int(x['amount_wei']) for x in edges)==148875761888326838512
for e in edges:
    tag=e['existing_bridge_origin_ID'];h=e['funding_transaction'];t=r(tag+'_tx');q=r(tag+'_receipt');b=r(tag+'_block');pt=r(h+'_tx');pq=r(h+'_receipt');pb=r('block_'+pt['blockNumber'])
    for tx,receipt,block in [(t,q,b),(pt,pq,pb)]:assert receipt['status']=='0x1' and tx['hash']==receipt['transactionHash'] and tx['blockHash']==receipt['blockHash']==block['hash'] and tx['hash'] in block['transactions']
    assert int(t['value'],16)==0 and t['from']==e['outer_transaction_sender'] and int(pt['value'],16)==int(e['amount_wei']) and pt['from']==e['native_source_wallet']
    event=e['gateway_event'];assert event in q['logs'] and event['topics'][0]=='0x'+keccak(b'StepExecuted(bytes32,bytes32,address)')
    assert gateway_path(t,event)==e['gateway_path'] and e['native_release_event'] in q['logs'] and e['bridge_deposit_event'] in q['logs']
    store=next(x for x in pq['logs'] if x['topics'][0]=='0x'+keccak(b'PrefundingStored(bytes32,address,uint256)'));assert store['topics'][1]==e['protocol_identifier']==e['native_release_event']['topics'][1]
    assert int(store['data'][2:66],16)==0 and int(store['data'][66:130],16)==int(e['amount_wei'])
    rel=e['native_release_event'];assert rel['topics'][0]=='0x'+keccak(b'PrefundedFunding(bytes32,address,uint256,address)') and rel['data'][2:130]==store['data'][2:130] and '0x'+rel['data'][-40:]==e['execution_contract']==e['gateway_path']['executor']
    assert e['funding_provenance'].startswith('PARTIAL')
for x in new[522:]:
    for file in x.get('evidence_files',[]):assert (P/file).exists(),file
for rel,h in json.loads((P/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((P/rel).read_bytes()).hexdigest()==h
print('PASS: prior 522 objects; seven prefund/bridge pairs, exact native values, events, full receipts/blocks, Merkle roots and hashes')
