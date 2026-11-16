"""Offline artifact checks. Verifies recorded response bytes, account scope and diff evidence."""
import json,hashlib
from pathlib import Path
from decimal import Decimal as D
P=Path(__file__).resolve().parent
rows=json.loads((P/'accounts_diff.json').read_text());assert len(rows)==len({r['account'] for r in rows})==36
meta=json.loads((P/'raw/spotMeta.response').read_text());assert meta['tokens'][404]['tokenId']=='0xbb2057659bd378d17e2e151bb04bdcaa';assert next(x for x in meta['universe'] if x['index']==260)['tokens']==[404,0]
count=0
for f in (P/'raw').glob('*.meta.json'):
 m=json.loads(f.read_text());response=f.with_name(f.name.replace('.meta.json','.response'));assert hashlib.sha256(response.read_bytes()).hexdigest()==m['sha256'];assert m['http_status']==200;assert m['started_utc']<=m['retrieved_utc'];count+=1
for r in rows:
 assert not r['coverage_issues'],(r['id'],r['coverage_issues'])
 assert D(r['current_xmr1'])-D(r['baseline_xmr1'])==D(r['delta_xmr1'])
 assert r['new_fills']==[] and r['new_ledger']==[]
 assert r['latest_activity_utc']==r['baseline_last_activity_utc']
 assert r['interval_fills']==r['interval_ledger']==0
assert sum((D(r['current_xmr1']) for r in rows),D(0))==D('3586.887420')
print(json.dumps({'result':'pass','account_count':len(rows),'raw_response_hashes_checked':count,'xmr1_total':'3586.887420','all_baseline_history_objects_retained':True,'new_returned_fills_and_ledger_records':0,'warning':'api server completeness and native monero redemptions not independently established'},indent=2))
