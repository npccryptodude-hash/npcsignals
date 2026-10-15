#!/usr/bin/env python3
"""Optional independent RPC reproduction. This collector was not successfully run.

Usage: python3 fetch_receipts.py --chain Polygon --rpc https://YOUR_ARCHIVE_RPC --out /absolute/new-directory
Never put credential-bearing RPC URLs into public output or commit directories.
"""
import argparse
import csv
import json
import urllib.request
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--chain', choices=['Polygon', 'Ethereum'], required=True)
ap.add_argument('--rpc', required=True)
ap.add_argument('--out', type=Path, required=True)
a = ap.parse_args()
root = Path(__file__).resolve().parent
out = a.out.resolve()
if out == root or root in out.parents:
    raise SystemExit('Choose a new output directory outside the frozen checkpoint.')
out.mkdir(parents=True, exist_ok=False)
hashes = set()
for name in ['historical_transfer_ledger.csv', 'control_transaction_ledger.csv']:
    with (root / name).open(newline='') as f:
        hashes.update(r['tx_hash'] for r in csv.DictReader(f) if r['chain'] == a.chain)
def rpc(method, params):
    payload = json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}).encode()
    req = urllib.request.Request(a.rpc, data=payload, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=25) as response:
        result = json.load(response)
    if result.get('error') or result.get('result') is None:
        raise RuntimeError('RPC error or missing result')
    return result['result']
for h in sorted(hashes):
    receipt = rpc('eth_getTransactionReceipt', [h])
    tx = rpc('eth_getTransactionByHash', [h])
    block = rpc('eth_getBlockByNumber', [receipt['blockNumber'], False])
    record = {'chain': a.chain, 'receipt': receipt, 'transaction': tx,
              'block_hash': block['hash'], 'block_number': block['number'],
              'timestamp_unix': int(block['timestamp'], 16)}
    (out / (h + '.json')).write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
print('Collected', len(hashes), 'receipt/transaction/block records. Compare against CSV before upgrading evidence.')
