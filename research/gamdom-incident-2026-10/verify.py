#!/usr/bin/env python3
"""Offline integrity and arithmetic checks; does not query or re-execute chains."""
import csv
import hashlib
import json
import re
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 80
root = Path(__file__).resolve().parent
manifest = json.loads((root / 'SHA256SUMS.json').read_text())
files = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name != 'SHA256SUMS.json'}
assert files == set(manifest), 'Manifest coverage mismatch'
for name, digest in manifest.items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
print('PASS: complete manifest coverage and SHA-256 integrity (manifest excludes itself)')
for p in root.glob('*.csv'):
    with p.open(newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            assert None not in row and None not in row.values(), p.name
with (root / 'transaction_ledger.csv').open(newline='') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 6
assert len({r['tx_hash'] for r in rows}) == 6
for r in rows:
    assert re.fullmatch(r'0x[0-9a-f]{64}', r['tx_hash'])
    assert Decimal(r['raw_amount']) / 10 ** int(r['decimals']) == Decimal(r['amount'])
    for key in ('tx_sender', 'tx_to', 'token_sender', 'token_recipient', 'token_contract'):
        assert re.fullmatch(r'0x[0-9a-fA-F]{40}', r[key]), (r['record_id'], key)
    assert r['unauthorized_status'] == 'UNRESOLVED'
    assert not r['usd_value']
print('PASS: CSV shape, unique IDs, address/hash syntax, exact token conversions and classification guards')
observations = json.loads((root / 'evidence/receipt_observations.json').read_text())['transactions']
assert [{k: str(v) for k, v in r.items()} for r in observations] == rows
pairs = json.loads((root / 'evidence/bridge_matches.json').read_text())
by_hash = {r['tx_hash']: r for r in rows}
for pair in pairs:
    src, dst = by_hash[pair['source_tx']], by_hash[pair['destination_tx']]
    assert src['role'] == 'bridge_source' and dst['role'] == 'bridge_destination'
    assert src['route_id'] == dst['route_id'] == pair['route_id']
    assert src['raw_amount'] == pair['source_input_raw']
    assert dst['raw_amount'] == pair['destination_dai_raw']
    assert src['tx_sender'].lower() == dst['token_recipient'].lower()
    assert re.fullmatch(r'0x[0-9A-F]{64}', pair['payload_hash'])
    assert Decimal(pair['bridge_raw']) / 10 ** pair['bridge_decimals'] == Decimal(pair['bridge_amount'])
print('PASS: transcribed bridge pair consistency; external event matching remains an online reviewer check')
principal = sum(Decimal(r['amount']) for r in rows if r['role'] == 'candidate_outflow')
assert principal == Decimal('31749.767002')
dai = sum(Decimal(r['amount']) for r in rows if r['role'] == 'bridge_destination')
assert dai == Decimal('31660.126542059029946225')
assert sum(r['unauthorized_status'] == 'CONFIRMED' for r in rows) == 0
print('PASS: original candidate principal = 31749.767002 mixed stablecoin units; destination = 31660.126542059029946225 DAI; neither is a verified USD loss')
