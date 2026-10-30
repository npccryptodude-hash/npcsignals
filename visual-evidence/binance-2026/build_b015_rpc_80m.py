#!/usr/bin/env python3
"""Read-only RPC receipt checks for 80m split and canonical 30m onward event."""
import hashlib
import json
import sys
from datetime import date
from pathlib import Path
from build_b014_rpc_downstream import PROVIDERS, TOKEN, decode, rpc

ROOT = Path(__file__).resolve().parent


def main():
    b010 = json.loads((ROOT / "b010-blacklist-and-80m.json").read_text())
    b012 = json.loads((ROOT / "b012-30m-and-pool-receipts.json").read_text())
    branch = b010["80m_continuation"]
    events = []
    for e in branch["events"]:
        events.append({**e, "token_transfer_from": e["from"], "token_transfer_to": e["to"]})
    onward = b012["30m_branch"]
    events.append({"transaction_hash": onward["canonical_usdt_transfer_hash"],
                   "token_transfer_from": onward["first_address"],
                   "token_transfer_to": onward["second_address"],
                   "raw_amount": str(int(onward["canonical_usdt_forwarded"]) * 10**6),
                   "amount_usdt": onward["canonical_usdt_forwarded"]})
    hashes = list(dict.fromkeys(e["transaction_hash"] for e in events))
    providers = []
    for name, endpoint in PROVIDERS.items():
        receipts = rpc(endpoint, hashes)
        receipt_lookup = {r["transactionHash"].lower(): r for r in receipts}
        records = [decode(receipt_lookup[e["transaction_hash"].lower()], e) for e in events]
        if len({(r["transaction_hash"], r["log_index"]) for r in records}) != len(records):
            raise RuntimeError("Duplicate log reference among events")
        providers.append({"provider": name, "endpoint": endpoint, "records": records,
                          "canonical_receipt_summary_sha256": hashlib.sha256(json.dumps(records, sort_keys=True, separators=(",", ":")).encode()).hexdigest()})
    if providers[0]["records"] != providers[1]["records"]:
        raise RuntimeError("Provider disagreement")
    subbranch_raw = sum(int(e["raw_amount"]) for e in events[:-1])
    if subbranch_raw != 80_000_000 * 10**6 or int(events[-1]["raw_amount"]) != 30_000_000 * 10**6:
        raise RuntimeError("Unexpected amount: no publication")
    result = {"case": "binance-2026-10-29", "checkpoint": "B015-independent-rpc-80m-and-onward-v1", "checked_on": date.today().isoformat(),
              "classification": "verified-from-two-public-ethereum-rpc-providers-for-listed-events-only", "canonical_usdt_contract": TOKEN,
              "providers": providers, "80m_branch_verified_events": len(events) - 1,
              "80m_branch_value_usdt": "80000000", "onward_30m_verified_events": 1, "onward_value_usdt": "30000000",
              "verified_unique_transactions": len(hashes),
              "limitations": ["The 30m onward transfer is a subset of the already counted 80m branch; total value is NOT 110m and is not additional to 700m first hop.",
                              "Receipt/log checks do not establish liquidity swaps, recipient identity, cash-out, recovery or present balance.",
                              "Two public RPC endpoints may share infrastructure. Other downstream transfers remain explorer data."]}
    target = ROOT / "b015-independent-rpc-80m.json"
    if target.exists():
        raise RuntimeError("REFUSE_OVERWRITE_EXISTING_CHECKPOINT")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print("B015: VERIFIED", len(events), "USDT transfer events,", len(hashes), "transactions, two RPC providers; amounts not additive")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("B015: NO-GO", exc, file=sys.stderr)
        sys.exit(1)
