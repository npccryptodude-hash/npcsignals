import pathlib
exec(open(pathlib.Path(__file__).resolve().parent/'collect-critical-receipts.py').read().split('with concurrent.futures')[0])
r=json.loads((out/'raw'/f'{sigs[1]}.rpc.json').read_text())['result'];keys=[k['pubkey'] for k in r['transaction']['message']['accountKeys'] if k['signer']][1:-1]
def call(k):
 q={'jsonrpc':'2.0','id':k,'method':'getSignaturesForAddress','params':[k,{'limit':1000,'commitment':'finalized'}]};(out/'raw'/f'{k}.history.request.json').write_text(json.dumps(q,indent=2)+'\n')
 try:
  b=urllib.request.urlopen(urllib.request.Request('https://api.mainnet-beta.solana.com',data=json.dumps(q).encode(),headers={'Content-Type':'application/json'}),timeout=25).read();(out/'raw'/f'{k}.history.rpc.json').write_bytes(b);j=json.loads(b);return {'address':k,'count':len(j.get('result') or []),'error':j.get('error')}
 except Exception as e:return {'address':k,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:r=list(ex.map(call,keys))
(out/'history-retrieval-log.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
