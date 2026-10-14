import pathlib,json,hashlib
P=pathlib.Path(__file__).resolve().parent
D='5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9'
directories=['exchange-network-pass','exchange-deposit-pass','8hc-verification','glitch-proceeds','glitch-b-disposition','exchange-8zhc-pass']
unique={};matches=[];counts={};undecoded=0
for folder in directories:
 counts[folder]=0
 for f in (P.parent/folder).glob('*.json'):
  try:t=json.loads(f.read_text())
  except Exception:continue
  if not isinstance(t,dict) or not isinstance(t.get('transaction'),dict) or not isinstance(t.get('meta'),dict):continue
  sig=t['transaction']['signatures'][0];counts[folder]+=1
  if sig in unique:continue
  unique[sig]={'path':str(f.relative_to(P.parent)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'execution_result':t['meta']['err']}
  if t['meta']['err'] is not None:continue
  groups=[('outer',t['transaction']['message']['instructions'])]+[('inner:'+str(g['index']),g['instructions']) for g in t['meta'].get('innerInstructions',[]) or []]
  for kind,items in groups:
   for i,ix in enumerate(items):
    parsed=ix.get('parsed',{})
    if not isinstance(parsed,dict):undecoded+=1;continue
    info=parsed.get('info',{})
    if not isinstance(info,dict):undecoded+=1;continue
    if info.get('destination')==D:matches.append({'signature':sig,'index':kind+':'+str(i),'instruction':ix,'slot':t['slot']})
r={'per_directory_receipt_counts':counts,'unique_receipts_tested':len(unique),'exact_destination':D,'matches':matches,'inventory':unique,'unparsed_instruction_count':undecoded,'limitations':'Bounded preserved-receipt exact parsed-destination screen only. No new lifetime histories; separate token owner destinations, raw instruction decoding and undiscovered network addresses not tested. Unmatched receipt originals remain in prior packages and are not duplicated here.'}
(P/'bounded-additional-scan.json').write_text(json.dumps(r,indent=2));print(json.dumps({k:v for k,v in r.items() if k!='inventory'},indent=2))
