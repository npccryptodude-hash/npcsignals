import urllib.request,json,concurrent.futures,time,pathlib
out=pathlib.Path(__file__).resolve().parent;out.mkdir(exist_ok=True);(out/'raw').mkdir(exist_ok=True)
sigs=['5xrGXTXnf7ZDe731C7EB5cNVnERshsZhT3E66udWiXmCtzaBGSVbmFygDovhJmzSrvUpG6m1PBRWQcq6S8UT18FV','3ttmcRNck85nUEcnaTZ3nmMWpq9sAdCwjq8EF56Zz4wzsi3dz2AB1G18FibKKmqNzShVexFVanogoAUSJeJXojy1','yH7hEtrWaAN5df8GgVzAZVbwQVKXTrLTBSFHMcVWQZVfjHKi5FHYD2JojrSFppD7FA1i82MTENqwxwitZCtP6Uv','2RRBTvJ43pasWVzrseXVJT3DpXdsAMwKvPgksrH1gtin7z12A1uzsg4vG7fMJd3FM6pBoj4WUXi2rD2deiJzciDa','5nRVLSVpSVDsmJ22zLL1ywrThq7y4VpybrdJnetbSi2KwTaAao5o7fy9aRPdkjF8tuvLvW21Zn99pBuEqboTjMkE','5ubvNRPDbdXtHaiexB4zroZxUDFS9mwDmDwJ3HnvdGrxuiqxDDGsZnkjdAGVHysDZgiCFqVASoinDu1bADPAbowo']
def fetch(s):
 q={'jsonrpc':'2.0','id':s,'method':'getTransaction','params':[s,{'encoding':'jsonParsed','commitment':'finalized','maxSupportedTransactionVersion':0}]};(out/'raw'/f'{s}.request.json').write_text(json.dumps(q,indent=2)+'\n')
 try:
  r=urllib.request.urlopen(urllib.request.Request('https://api.mainnet-beta.solana.com',data=json.dumps(q).encode(),headers={'Content-Type':'application/json'}),timeout=25);b=r.read();(out/'raw'/f'{s}.rpc.json').write_bytes(b);j=json.loads(b);v=j.get('result');return {'signature':s,'http':r.status,'result_present':bool(v),'error':j.get('error'),'slot':v.get('slot') if v else None}
 except Exception as e:return {'signature':s,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:r=list(ex.map(fetch,sigs))
(out/'retrieval-log.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
