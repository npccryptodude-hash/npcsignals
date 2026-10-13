#!/usr/bin/env python3
"""Exact address equality against read-only ZYROX text evidence."""
import json,re,csv
from pathlib import Path
R=Path(__file__).resolve().parents[3];G=R/'research/glitch-investigation'
S=json.loads((G/'data/comparison_scope.json').read_text());actors=set(S['glitch_actors_examined']);accounts=set(S['glitch_all_accounts_examined']);rows=[]
for folder in ['zyrox-investigation','zyrox-investigation-post-freeze']:
 for f in sorted((R/'research'/folder).rglob('*')):
  if not f.is_file() or f.suffix not in S['reference_suffixes']:continue
  try:text=f.read_text()
  except UnicodeDecodeError:continue
  addresses=set(re.findall(r'(?<![1-9A-HJ-NP-Za-km-z])[1-9A-HJ-NP-Za-km-z]{32,44}(?![1-9A-HJ-NP-Za-km-z])',text))
  for a in sorted(accounts&addresses):rows.append(dict(address=a,glitch_role='signer_or_direct_funder' if a in actors else 'non_signing_account',zyrox_reference=str(f.relative_to(R)),status='OBSERVED exact address in verified-reference corpus; shared control UNRESOLVED'))
with (G/'data/address_overlap.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['address','glitch_role','zyrox_reference','status']);w.writeheader();w.writerows(rows)
assert not [r for r in rows if r['glitch_role']=='signer_or_direct_funder'], 'New actor overlap requires review'
print('Examined actors:',len(actors),'Actor overlaps: 0; non-signing matches require role review.')
