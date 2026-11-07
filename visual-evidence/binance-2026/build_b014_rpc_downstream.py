#!/usr/bin/env python3
"""Cross-check selected downstream canonical USDT transfers using public RPC receipts.

Read-only eth_getTransactionReceipt. No transaction submission or credentials.
The output is written only after both providers agree with the local B008 ledger.
"""
import hashlib
import json
import sys
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEDGER = json.loads((ROOT / "b008-third-hop-usdt-ledger.json").read_text())
TOKEN = "0xdac17f958d2ee523a2206206994597c13d831ec7"
TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
PROVIDERS = {"publicnode": "https://ethereum-rpc.publicnode.com", "blastapi": "https://eth-mainnet.public.blastapi.io"}


def rpc(endpoint, hashes):
    calls = [{"jsonrpc": "2.0", "id": i + 1, "method": "eth_getTransactionReceipt", "params": [h]} for i, h in enumerate(hashes)]
    data = json.dumps(calls, separators=(",", ":")).encode()
    req = urllib.request.Request(endpoint, data=data, headers={"Content-Type": "application/json", "User-Agent": "npcsignals-research-readonly/0.1"})
    with urllib.request.urlopen(req, timeout=45) as response:
        result = json.load(response)
    if not isinstance(result, list) or len(result) != len(hashes):
        raise RuntimeError("RPC batch response missing items")
    by_id = {item["id"]: item for item in result}
    receipts = []
    for idx, h in enumerate(hashes, 1):
        item = by_id[idx]
        if "error" in item or not item.get("result"):
            raise RuntimeError(f"RPC receipt unavailable: {h}: {item.get('error')}")
        receipt = item["result"]
        if receipt["transactionHash"].lower() != h.lower() or receipt["status"] != "0x1":
            raise RuntimeError("RPC receipt hash or status disagreement: " + h)
        receipts.append(receipt)
    return receipts


def decode(receipt, e):
    matches = []
    for log in receipt["logs"]:
        topics = log["topics"]
        if log["address"].lower() != TOKEN or len(topics) != 3 or topics[0].lower() != TOPIC:
            continue
        sender = "0x" + topics[1][-40:]
        target = "0x" + topics[2][-40:]
        amount = int(log["data"], 16)
        if sender.lower() == e["token_transfer_from"].lower() and target.lower() == e["token_transfer_to"].lower() and amount == int(e["raw_amount"]):
            matches.append({"log_index": int(log["logIndex"], 16), "from": sender.lower(), "to": target.lower(), "raw_amount": str(amount)})
    if len(matches) != 1:
        raise RuntimeError("Expected exactly one matching canonical USDT transfer in " + e["transaction_hash"])
    match = matches[0]
    return {"transaction_hash": e["transaction_hash"].lower(), "block_number": int(receipt["blockNumber"], 16), "block_hash": receipt["blockHash"].lower(), "token_contract": TOKEN, **match, "amount_usdt": e["amount_usdt"], "transaction_success": True}


def main():
    events = LEDGER["outgoing_transfer_events"]
    hashes = list(dict.fromkeys(e["transaction_hash"] for e in events))
    results = []
    for name, endpoint in PROVIDERS.items():
        receipts = rpc(endpoint, hashes)
        mapped = {r["transactionHash"].lower(): r for r in receipts}
        records = [decode(mapped[e["transaction_hash"].lower()], e) for e in events]
        results.append({"provider": name, "endpoint": endpoint, "records": records, "canonical_receipt_summary_sha256": hashlib.sha256(json.dumps(records, sort_keys=True, separators=(",", ":")).encode()).hexdigest()})
    if results[0]["records"] != results[1]["records"]:
        raise RuntimeError("Provider event details disagree")
    report = {"case": "binance-2026-10-29", "checkpoint": "B014-independent-rpc-selected-third-hop-v1", "checked_on": date.today().isoformat(), "classification": "verified-from-two-public-ethereum-rpc-providers-for-listed-events-only", "canonical_usdt_contract": TOKEN, "sources": results, "verified_event_count": len(events), "verified_transaction_count": len(hashes), "verified_selected_usdt_total": str(sum(int(e["raw_amount"]) for e in events) // 10**6), "limitations": ["This RPC agreement applies only to the listed B008 selected third-hop events; B007, B009-B012 remain explorer-data observations.", "Distinct public RPC endpoints may have overlapping upstream infrastructure.", "Transaction receipt log agreement does not identify wallet controllers, establish cash-out, token freezes, recovery or cross-chain totals."]}
    target = ROOT / "b014-independent-rpc-third-hop.json"
    if target.exists():
        raise RuntimeError("REFUSE_OVERWRITE_EXISTING_CHECKPOINT")
    target.write_text(json.dumps(report, indent=2) + "\n")
    print("B014: VERIFIED", len(events), "events in", len(hashes), "transactions, 365m canonical USDT, two RPC providers")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("B014: NO-GO", str(exc), file=sys.stderr)
        sys.exit(1)
