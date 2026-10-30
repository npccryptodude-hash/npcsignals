#!/usr/bin/env python3
"""Offline, read-only consistency checks for the Binance visual archive.

No network requests and no mainnet interaction. Run from any working directory.
"""
import json
from collections import Counter
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
USDT = "0xdac17f958d2ee523a2206206994597c13d831ec7"
checks = []


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def check(name, truth):
    if not truth:
        raise AssertionError("FAIL: " + name)
    checks.append(name)


def total(events, field="amount_usdt"):
    return sum((Decimal(str(e[field])) for e in events), Decimal(0))


def canonical(events, from_key="from"):
    for e in events:
        check("canonical contract " + e["transaction_hash"][:12], e["token_contract"].lower() == USDT)
        check("six decimals " + e["transaction_hash"][:12], e["decimals"] == 6)
        check("integer denomination " + e["transaction_hash"][:12], Decimal(e["raw_amount"]) == Decimal(str(e["amount_usdt"])) * 10**6)
        check("source address " + e["transaction_hash"][:12], e[from_key].startswith("0x"))


b006 = load("b006-receiver-outgoing-summary.json")
b007 = load("b007-second-hop-usdt-ledger.json")
b008 = load("b008-third-hop-usdt-ledger.json")
b009 = load("b009-large-recipient-continuation.json")
b010 = load("b010-blacklist-and-80m.json")
b011 = load("b011-80m-recipient-infrastructure.json")
b012 = load("b012-30m-and-pool-receipts.json")
b013 = load("b013-independent-rpc-usdt.json")
b014 = load("b014-independent-rpc-third-hop.json")
b015 = load("b015-independent-rpc-80m.json")

first = b006["canonical_usdt_positive_outflows"]
check("two first-hop transfers", len(first) == 2)
check("first-hop 700m", total(first) == Decimal(700_000_000))
check("first-hop ledger total", Decimal(str(b006["canonical_usdt_positive_outflow_total"])) == total(first))
check("first-hop canonical", b006["canonical_usdt_contract"].lower() == USDT)
check("rpc providers", len(b013["providers"]) == 2)
rpc_records = [p["transactions"] for p in b013["providers"]]
check("provider agreement", rpc_records[0] == rpc_records[1])
check("rpc provider names differ", len({p["provider"] for p in b013["providers"]}) == 2)
for explorer, rpc in zip(first, rpc_records[0]):
    for field in ("transaction_hash", "raw_amount", "amount_usdt"):
        check("first hop RPC matches " + field, str(explorer[field]).lower() == str(rpc[field]).lower())
    for field in ("from", "to"):
        check("first hop address matches " + field, explorer[field].lower() == rpc[field].lower())
    check("rpc canonical token", rpc["token_contract"] == USDT)
    check("rpc success", rpc["transaction_status"] == "success")

second = b007["outgoing_events"]
canonical(second)
check("second-hop gross", total(second) == Decimal(700_000_000))
check("second-hop 19 positive", sum(Decimal(e["amount_usdt"]) > 0 for e in second) == 19)
check("second-hop branch reconciliation", {k: total([e for e in second if e["branch"] == k]) for k in ("A", "B")} == {"A": Decimal(500_000_000), "B": Decimal(200_000_000)})
check("no duplicate second-hop records", len({(e["transaction_hash"], e["from"].lower(), e["to"].lower(), e["raw_amount"]) for e in second}) == len(second))

third = b008["outgoing_transfer_events"]
canonical(third, "token_transfer_from")
check("third-hop 365m", total(third) == Decimal(365_000_000))
check("third-hop reported total", total(third) == Decimal(str(b008["value_traced_usdt"])))
check("third-hop successful transactions", all(e["transaction_status"] == "ok" for e in third))
check("third-hop two RPC providers", len(b014["sources"]) == 2)
check("third-hop provider agreement", b014["sources"][0]["records"] == b014["sources"][1]["records"])
check("third-hop matching exact events", len(b014["sources"][0]["records"]) == len(third))
for ledger, receipt in zip(third, b014["sources"][0]["records"]):
    check("third-hop tx matched", ledger["transaction_hash"].lower() == receipt["transaction_hash"])
    check("third-hop amount matched", ledger["raw_amount"] == receipt["raw_amount"])
    check("third-hop sender matched", ledger["token_transfer_from"].lower() == receipt["from"])
    check("third-hop recipient matched", ledger["token_transfer_to"].lower() == receipt["to"])

branches = {b["branch"]: b for b in b009["branches"]}
check("130m branch reconciliation", Decimal(branches["130m"]["outgoing_usdt_total"]) == Decimal(130_000_000))
check("175m branch retained arithmetic", Decimal(branches["175m"]["inbound_traced_usdt"]) - Decimal(branches["175m"]["outgoing_usdt_total"]) == Decimal(branches["175m"]["remaining_from_traced_inbound_by_arithmetic"]))
check("175m balance includes dust", Decimal(branches["175m"]["remaining_from_traced_inbound_by_arithmetic"]) + Decimal(branches["175m"]["additional_incoming_usdt_in_snapshot"]) == Decimal(branches["175m"]["reported_current_usdt_balance"]))

eighty = b010["80m_continuation"]
canonical(eighty["events"])
check("80m sum", total(eighty["events"]) == Decimal(80_000_000))
check("80m 20 records", len(eighty["events"]) == 20)
check("80m 11 distinct recipients", len({e["to"].lower() for e in eighty["events"]}) == 11)
check("80m not added to first hop", total(eighty["events"]) < total(first))
check("80m two provider receipts", len(b015["providers"]) == 2)
check("80m provider event agreement", b015["providers"][0]["records"] == b015["providers"][1]["records"])
check("80m check 20 events plus onward", len(b015["providers"][0]["records"]) == len(eighty["events"]) + 1)
for original, receipt in zip(eighty["events"], b015["providers"][0]["records"][:-1]):
    check("80m tx agreement", original["transaction_hash"].lower() == receipt["transaction_hash"])
    check("80m raw agreement", original["raw_amount"] == receipt["raw_amount"])
    check("80m sender agreement", original["from"].lower() == receipt["from"])
    check("80m target agreement", original["to"].lower() == receipt["to"])
check("onward 30m tx agreement", b012["30m_branch"]["canonical_usdt_transfer_hash"].lower() == b015["providers"][0]["records"][-1]["transaction_hash"])
check("onward 30m raw agreement", Decimal(b015["providers"][0]["records"][-1]["raw_amount"]) == Decimal(30_000_000 * 10**6))
check("80m contract/no-code split", Decimal(str(b011["canonical_usdt_to_contracts"])) + Decimal(str(b011["canonical_usdt_to_no_contract_code_address"])) == Decimal(80_000_000))

for page in ("README.md", "index.html", "flow.html", "medium-draft.md", "x-draft.md"):
    check("page exists " + page, (ROOT / page).is_file())
check("flow offline no scripts", "<script src=" not in (ROOT / "flow.html").read_text())
check("draft X link placeholder", "http" not in (ROOT / "x-draft.md").read_text().lower())

print("BINANCE_ARCHIVE_AUDIT: PASS")
print("CHECKS:", len(checks))
print("FIRST_HOP_CANONICAL_USDT:", total(first))
print("SECOND_HOP_CANONICAL_USDT:", total(second), "(same funds, not additive)")
print("THIRD_HOP_SELECTED_USDT:", total(third), "(subset, not additive)")
print("80M_SUBBRANCH_USDT:", total(eighty["events"]), "(subset, not additive)")
print("MAINNET_TRANSACTIONS: NONE")
