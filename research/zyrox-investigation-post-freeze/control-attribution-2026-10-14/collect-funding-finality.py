import pathlib
exec(open(pathlib.Path(__file__).resolve().parent/'collect-critical-receipts.py').read().split('with concurrent.futures')[0])
initial=[];logs=[]
for f in sorted((out/'raw').glob('*.history.rpc.json')):
 k=f.name.split('.')[0];r=json.loads(f.read_text())['result'];initial.append(r[-1]['signature']);q={'jsonrpc':'2.0','id':k,'method':'getSignaturesForAddress','params':[k,{'limit':1000,'commitment':'finalized','before':r[-1]['signature']}]};(out/'raw'/f'{k}.terminal.request.json').write_text(json.dumps(q,indent=2)+'\n')
 try:
  b=urllib.request.urlopen(urllib.request.Request('https://api.mainnet-beta.solana.com',data=json.dumps(q).encode(),headers={'Content-Type':'application/json'}),timeout=25).read();(out/'raw'/f'{k}.terminal.rpc.json').write_bytes(b);logs.append({'address':k,'terminal':json.loads(b)})
 except Exception as e:logs.append({'address':k,'error':str(e)})
print('terminal',json.dumps(logs));initial=list(dict.fromkeys(initial))
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:r=list(ex.map(fetch,initial))
(out/'followup-retrieval-log.json').write_text(json.dumps({'terminal':logs,'initial_receipts':r},indent=2)+'\n');print('initial',json.dumps(r))
all_sigs=[f.name.split('.')[0] for f in (out/'raw').glob('*.rpc.json') if '.history.' not in f.name and '.terminal.' not in f.name]
q={'jsonrpc':'2.0','id':'finality','method':'getSignatureStatuses','params':[all_sigs,{'searchTransactionHistory':True}]};(out/'raw/finality.request.json').write_text(json.dumps(q,indent=2)+'\n')
b=urllib.request.urlopen(urllib.request.Request('https://api.mainnet-beta.solana.com',data=json.dumps(q).encode(),headers={'Content-Type':'application/json'}),timeout=25).read();(out/'raw/finality.rpc.json').write_bytes(b)
print('finality',[(x['confirmationStatus'],x['err']) if x else None for x in json.loads(b)['result']['value']])
