import pathlib,json
from discover import rpc
P=pathlib.Path(__file__).resolve().parent
rows=json.loads((P/'8zHcWujHhyJri3CRTcWUGmT5WSRdwW7xrns3WTTkPGvS-outgoing.json').read_text());sigs=[r['signature'] for r in rows]
for sig in sigs:
 raw,d,req=rpc('getTransaction',[sig,{'encoding':'jsonParsed','commitment':'finalized','maxSupportedTransactionVersion':1}]);assert d['result'] is not None and d['result']['meta']['err'] is None
 (P/(sig+'.rpc.json')).write_bytes(raw);(P/(sig+'.request.json')).write_text(json.dumps(req,indent=2));prior=json.loads((P/(sig+'.json')).read_text());(P/(sig+'.json')).write_text(json.dumps(d['result'],indent=2));print(sig,'same_as_discovery',prior==d['result'],'slot',d['result']['slot'],flush=True)
raw,d,req=rpc('getSignatureStatuses',[sigs,{'searchTransactionHistory':True}]);(P/'candidate-finality.rpc.json').write_bytes(raw);(P/'candidate-finality.request.json').write_text(json.dumps(req,indent=2));(P/'candidate-finality.json').write_text(json.dumps(dict(zip(sigs,d['result']['value'])),indent=2))
for s,v in zip(sigs,d['result']['value']):assert v['confirmationStatus']=='finalized' and v['err'] is None
