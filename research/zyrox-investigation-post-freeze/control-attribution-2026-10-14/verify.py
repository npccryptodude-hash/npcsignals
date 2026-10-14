import pathlib,json,hashlib
P=pathlib.Path(__file__).resolve().parent
J=lambda p:json.loads(p.read_text())
manifest=J(P/'SHA256SUMS.json')
assert set(manifest)=={f.relative_to(P).as_posix() for f in P.rglob('*') if f.is_file() and f!=P/'SHA256SUMS.json'}
for name,h in manifest.items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==h,name
raw=P/'raw';q=J(raw/'finality.request.json');statuses=J(raw/'finality.rpc.json')['result']['value'];assert len(statuses)==11
for sig,status in zip(q['params'][0],statuses):
 r=J(raw/f'{sig}.rpc.json')['result'];assert r['meta']['err'] is None;assert status['err'] is None and status['confirmationStatus']=='finalized';assert r['slot']==status['slot'];assert r['transaction']['signatures'][0]==sig
 assert sum(r['meta']['preBalances'])-sum(r['meta']['postBalances'])==r['meta']['fee']
rows=J(P/'new-evidence-ledger.json');assert len(rows)==10
for row in rows:
 r=J(raw/f'{row["signature"]}.rpc.json')['result'];m=r['transaction']['message'];idx=int(row['instruction_index'].split(':')[1]);i=m['instructions'][idx]['parsed']['info'];assert r['slot']==row['slot'];assert m['accountKeys'][0]['pubkey']==row['fee_payer']
 if row['asset'].startswith('GLITCH'):
  assert i['tokenAmount']['amount']==row['raw_amount'];assert i['multisigAuthority']==row['authority'];assert i['source']==row['source_token_account'];assert i['destination']==row['destination_token_account']
  keys=[k['pubkey'] for k in m['accountKeys']];pre={keys[b['accountIndex']]:b for b in r['meta']['preTokenBalances']};post={keys[b['accountIndex']]:b for b in r['meta']['postTokenBalances']};src=i['source'];assert pre[src]['owner']==post[src]['owner']==row['authority'];assert int(pre[src]['uiTokenAmount']['amount'])-int(post[src]['uiTokenAmount']['amount'])==int(row['raw_amount'])
 else:assert str(i['lamports'])==row['raw_amount'] and i['source']==row['authority']
a=J(P/'consolidation-audit.json');assert sum(int(x['raw_amount']) for x in rows[:5])==46513762335674;assert int(a['recipient_after_raw'])-int(a['recipient_before_raw'])==116513762335674
for h in J(P/'history-scope.json'):
 k=h['address'];hist=J(raw/f'{k}.history.rpc.json')['result'];assert len(hist)==h['returned_references'];assert J(raw/f'{k}.terminal.rpc.json')['result']==[];assert J(raw/f'{k}.terminal.request.json')['params'][1]['before']==hist[-1]['signature']
assert sum(x['returned_references'] for x in J(P/'history-scope.json'))==96
assert all(not x['zyrox_text_matches'] for x in J(P/'exact-address-comparison.json')['matches'])
print('PASS: complete manifest; 11 successful finalized receipts; native fee conservation; 10 new ledger rows; consolidation token reconciliation; five terminal histories / 96 references; bounded no-match comparison')
