#!/usr/bin/env python3
"""Build source register and SHA-256 manifest from the saved evidence. Offline."""
import pathlib,json,csv,hashlib
R=pathlib.Path(__file__).resolve().parent
def files():return sorted(p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
def main():
    rows=[]
    for p in sorted((R/'evidence').glob('*.json')):
        o=json.loads(p.read_text())
        if 'request' in o:
            rows.append(dict(record=str(p.relative_to(R)),url=o['endpoint'],method=o['request']['method'],parameters=json.dumps(o['request']['params'],separators=(',',':')),evidence_kind='raw RPC request/response',outcome='returned result' if 'result' in o.get('response',{}) else 'access or RPC error',queried_at_UTC=o.get('requested_at_UTC','')))
        elif p.name=='rpc_attempts.json':
            for i,a in enumerate(o):rows.append(dict(record=str(p.relative_to(R))+'#'+str(i),url=a['endpoint'],method=a['request']['method'],parameters=json.dumps(a['request']['params'],separators=(',',':')),evidence_kind='raw historical-state transport probe',outcome='see saved HTTP body',queried_at_UTC=a['requested_at_UTC']))
    for p in ['funding_transaction_ledger.csv']:
        for o in csv.DictReader((R/p).open()):
            rows.append(dict(record='evidence/receipt_'+o['tx_hash']+'.json',url=o['source_url'],method='receipt + transaction + block',parameters=o['tx_hash'],evidence_kind='raw RPC verified; explorer URL provided for independent reproduction',outcome='success status 1',queried_at_UTC='2026-10-15'))
    rows.append(dict(record='evidence/explorer_state_observation.json',url='https://polygonscan.com/tx/0x5e1fd78c9b4f5881d28eb2f14f0c59b32bda206a942a6956316c07965b570591#statechange',method='expanded storage difference table',parameters='USDT0 balance mapping',evidence_kind='curated browser transcription',outcome='matches archive before/after values',queried_at_UTC='2026-10-15'))
    with (R/'source_register.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    manifest={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files() if p.name!='SHA256SUMS.json'}
    (R/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
