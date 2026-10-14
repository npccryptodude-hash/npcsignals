import pathlib,json,urllib.request,time,datetime,concurrent.futures
P=pathlib.Path(__file__).resolve().parent
W='56HEQykziUkwvpK5uPzFrRbGD4Ek8HdWgjgeDvNmDoEJ';T='CzissnPHhEu7NifSLfwhuvFMdfu7F8X4vR2HhF1o1PEL'
START=['45zVBfuvgtptBZuABucUsMiPHYQfG4pf4ium1629LREQyeFqCWF1rEh5VM5pVT4ukmYPPr3LDMbs7F6ku2RDg1kw','64voUTp7NHZMZieXJDnJ1yNfMHaCN9GtNFP39AqQxcgS6QTKCeeGzmJgeB3qPmsAFNpzZky3c6kYcYjVAUQ81MUJ']
def rpc(method,params):
 req={'jsonrpc':'2.0','id':1,'method':method,'params':params}
 for attempt in range(3):
  try:
   with urllib.request.urlopen(urllib.request.Request('https://api.mainnet-beta.solana.com',data=json.dumps(req).encode(),headers={'Content-Type':'application/json'}),timeout=25) as f:raw=f.read()
   d=json.loads(raw)
   if d.get('error'):raise RuntimeError(str(d['error']))
   return raw,d,req
  except Exception:
   if attempt==2:raise
   time.sleep(2**attempt)
def history(a):
 pages=[];rows=[];before=None
 for pi in range(2):
  opts={'limit':1000,'commitment':'finalized'}
  if before:opts['before']=before
  raw,d,req=rpc('getSignaturesForAddress',[a,opts]);part=d['result'];(P/(a+'-page'+str(pi)+'.rpc.json')).write_bytes(raw);(P/(a+'-page'+str(pi)+'.request.json')).write_text(json.dumps(req,indent=2));pages.append({'request':req,'rows':part});rows+=part
  if not part:break
  before=part[-1]['signature']
  if len(part)<1000:
   # Preserve an explicit terminal page rather than infer completeness from a short page.
   opts={'limit':1000,'commitment':'finalized','before':before};raw,d,req=rpc('getSignaturesForAddress',[a,opts]);part=d['result'];(P/(a+'-terminal.rpc.json')).write_bytes(raw);(P/(a+'-terminal.request.json')).write_text(json.dumps(req,indent=2));pages.append({'request':req,'rows':part});rows+=part;break
 report={'address':a,'rows':rows,'pages':pages,'terminal_empty_page':not bool(pages[-1]['rows']),'resume_before':rows[-1]['signature'] if rows else None};(P/(a+'-history.json')).write_text(json.dumps(report,indent=2));print('HISTORY',a,len(rows),'terminal',report['terminal_empty_page'],flush=True);return report
def receipt(s):
 raw,d,req=rpc('getTransaction',[s,{'encoding':'jsonParsed','commitment':'finalized','maxSupportedTransactionVersion':1}]);(P/(s+'.rpc.json')).write_bytes(raw);(P/(s+'.request.json')).write_text(json.dumps(req,indent=2));(P/(s+'.json')).write_text(json.dumps(d.get('result'),indent=2));print('RECEIPT',s,d['result']['slot'] if d.get('result') else None,flush=True);return s,d.get('result') is not None
if __name__=='__main__':
 reports=[history(a) for a in [W,T]];sigs=set(START);selection=[];boundary=int(datetime.datetime(2026,9,24,11,49,54,tzinfo=datetime.timezone.utc).timestamp())
 for h in reports:
  rows=h['rows'];chosen=rows
  if len(rows)>300:
   pre=sorted([r for r in rows if (r.get('blockTime') or 0)<boundary],key=lambda r:r.get('blockTime') or 0,reverse=True)[:100];post=sorted([r for r in rows if (r.get('blockTime') or 0)>=boundary],key=lambda r:r.get('blockTime') or 0)[:200];chosen=pre+post
  sigs.update(r['signature'] for r in chosen);selection.append({'address':h['address'],'indexed_count':len(rows),'selected_count':len(chosen),'history_terminal_empty_page':h['terminal_empty_page'],'receipt_selection_complete':len(rows)==len(chosen),'selection_rule':'all if <=300; otherwise 100 closest pre-payment and 200 earliest post-payment among indexed rows'})
 (P/'selection.json').write_text(json.dumps(selection,indent=2));sigs=sorted(sigs);(P/'selected-signatures.json').write_text(json.dumps(sigs,indent=2))
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(receipt,sigs))
 (P/'receipt-retrieval.json').write_text(json.dumps(results,indent=2));statuses={}
 for i in range(0,len(sigs),50):
  raw,d,req=rpc('getSignatureStatuses',[sigs[i:i+50],{'searchTransactionHistory':True}]);(P/f'finality-{i//50}.rpc.json').write_bytes(raw);(P/f'finality-{i//50}.request.json').write_text(json.dumps(req,indent=2));statuses.update(dict(zip(sigs[i:i+50],d['result']['value'])))
 (P/'finality.json').write_text(json.dumps(statuses,indent=2));print('DONE',len(sigs),flush=True)
