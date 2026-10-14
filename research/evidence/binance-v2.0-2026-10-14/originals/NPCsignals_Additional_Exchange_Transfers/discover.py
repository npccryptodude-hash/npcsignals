import pathlib,json,urllib.request,time,datetime
P=pathlib.Path(__file__).resolve().parent
W=['6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N','8zHcWujHhyJri3CRTcWUGmT5WSRdwW7xrns3WTTkPGvS']
cutoff=int(datetime.datetime(2026,9,30,17,18,tzinfo=datetime.timezone.utc).timestamp())
def rpc(method,params):
 req={'jsonrpc':'2.0','id':1,'method':method,'params':params}
 for attempt in range(3):
  try:
   with urllib.request.urlopen(urllib.request.Request('https://api.mainnet-beta.solana.com',data=json.dumps(req).encode(),headers={'Content-Type':'application/json'}),timeout=30) as f:raw=f.read()
   d=json.loads(raw)
   if d.get('error'):raise RuntimeError(str(d['error']))
   return raw,d,req
  except Exception:
   if attempt==2:raise
   time.sleep(2**attempt)
if __name__=='__main__':
 for wi,w in enumerate(W):
  opts={'limit':100,'transactionDetails':'full','encoding':'jsonParsed','sortOrder':'desc','commitment':'finalized','maxSupportedTransactionVersion':1,'filters':{'blockTime':{'lt':cutoff},'status':'succeeded','tokenAccounts':'all'}}
  raw,d,req=rpc('getTransactionsForAddress',[w,opts]);(P/(w+'-history.rpc.json')).write_bytes(raw);(P/(w+'-history.request.json')).write_text(json.dumps(req,indent=2))
  rows=d['result']['data'];out=[]
  for t in rows:
   sig=t['transaction']['signatures'][0];(P/(sig+'.json')).write_text(json.dumps(t,indent=2));assert t['blockTime']<cutoff
   owners={v['accountIndex']:v.get('owner') for v in (t['meta'].get('preTokenBalances',[])+t['meta'].get('postTokenBalances',[]))};keys=t['transaction']['message']['accountKeys'];addr=[k['pubkey'] for k in keys];groups=[('outer',t['transaction']['message']['instructions'])]+[('inner:'+str(g['index']),g['instructions']) for g in t['meta'].get('innerInstructions',[]) or []]
   for kind,items in groups:
    for i,ix in enumerate(items):
     v=ix.get('parsed',{});v=v if isinstance(v,dict) else {};info=v.get('info',{});s=info.get('source');dst=info.get('destination');so=owners.get(addr.index(s)) if s in addr else None;do=owners.get(addr.index(dst)) if dst in addr else None
     if (s==w or so==w) and dst and t['meta']['err'] is None:out.append({'signature':sig,'utc':datetime.datetime.fromtimestamp(t['blockTime'],datetime.timezone.utc).isoformat(),'slot':t['slot'],'instruction_index':kind+':'+str(i),'source':s,'source_owner':so,'destination':dst,'destination_owner':do,'type':v.get('type'),'info':info})
  (P/(w+'-outgoing.json')).write_text(json.dumps(out,indent=2));print(json.dumps({'wallet':w,'transactions':len(rows),'outgoing':len(out),'destinations':sorted(set(x['destination_owner'] or x['destination'] for x in out)),'paginationToken':d['result'].get('paginationToken')}),flush=True)
