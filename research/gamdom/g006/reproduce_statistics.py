#!/usr/bin/env python3
"""Recalculate coverage-limited DAI metrics from saved records; no network calls."""
import csv,json
from pathlib import Path
from decimal import Decimal,getcontext
getcontext().prec=80
p=Path(__file__).resolve().parent
with (p/'historical_transfer_ledger.csv').open() as f:rows=list(csv.DictReader(f))
B='0xe5686aae44d392aa6a0637fd38393859502f8667'
D='0x6b175474e89094c44da98b954eedeac495271d0f'
rr=[r for r in rows if r['chain']=='Ethereum' and r['token_contract'].lower()==D]
def delta(records):return sum((Decimal(r['raw_amount'])/Decimal(10)**int(r['decimals']))*(1 if r['token_recipient'].lower()==B else -1) for r in records)
print(json.dumps({'scope':'saved canonical DAI sample; not a balance proof','pre_G005_net_inflow':str(delta([r for r in rr if r['utc_timestamp']<'2026-10-13T18:14:35Z'])),'post_G005_additional_net_inflow':str(delta([r for r in rr if r['utc_timestamp']>'2026-10-13T18:16:35Z'])),'total_observed_delta':str(delta(rr))},indent=2))
