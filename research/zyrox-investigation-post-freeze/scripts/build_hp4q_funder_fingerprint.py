#!/usr/bin/env python3
import json
import pathlib
from collections import defaultdict


ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
FUNDER_ROOT = RAW / "hp4q_funder_fingerprint_2026-10-11"
UPSTREAM_ROOT = RAW / "hp4q_funder_upstream_2026-10-11"
INFRA_ROOT = RAW / "hp4q_known_infrastructure_2026-10-11"
OUTPUT = RAW / "hp4q_funder_fingerprint_manifest_2026-10-11.json"
HP4Q = "Hp4q9Tfeo5Cp7BuFNe6pRo3DqfPZVAiEampauGzPyyod"


def read_manifests(root):
    result = {}
    for path in sorted(root.glob("*/manifest.json")):
        rows = json.loads(path.read_text())
        result[path.parent.name] = rows
    return result


def incoming(tx, address):
    return [
        transfer for transfer in tx["native_transfers"]
        if transfer["destination"] == address and transfer["source"] != address
    ]


def outgoing_to(tx, source, destination):
    return [
        transfer for transfer in tx["native_transfers"]
        if transfer["source"] == source and transfer["destination"] == destination
    ]


def tx_ref(tx):
    return {
        "signature": tx["signature"],
        "UTC": tx["UTC"],
        "slot": tx["slot"],
        "transaction_index": tx["transaction_index"],
        "fee_lamports": tx["fee_lamports"],
        "signers": tx["signers"],
        "fee_payer": tx["fee_payer"],
        "subject_balance": tx["subject_balance"],
        "canonical_json_sha256": tx["canonical_json_sha256"],
    }


def cycle_summary(inbound_rows, outbound_tx, outbound_transfer):
    aggregate = sum(item[1]["lamports"] for item in inbound_rows)
    first_time = min(item[0]["block_time"] for item in inbound_rows)
    last_time = max(item[0]["block_time"] for item in inbound_rows)
    slot_counts = defaultdict(int)
    for tx, _ in inbound_rows:
        slot_counts[tx["slot"]] += 1
    balance = outbound_tx["subject_balance"]
    full_balance = (
        balance["pre_lamports"] == aggregate
        and balance["post_lamports"] == 0
        and outbound_transfer["lamports"] + outbound_tx["fee_lamports"] == aggregate
    )
    return {
        "inbound_count": len(inbound_rows),
        "upstream_wallets": [item[1]["source"] for item in inbound_rows],
        "aggregate_inbound_lamports": aggregate,
        "aggregate_inbound_SOL": f"{aggregate / 1_000_000_000:.9f}",
        "funding_span_seconds": last_time - first_time,
        "seconds_first_funding_to_forward": outbound_tx["block_time"] - first_time,
        "seconds_last_funding_to_forward": outbound_tx["block_time"] - last_time,
        "funding_slots": sorted(slot_counts),
        "same_slot_max_deposits": max(slot_counts.values()),
        "all_inbound_transactions_are_multi_recipient_batches": all(
            sum(1 for transfer in tx["native_transfers"] if transfer["source"] == transfer_row["source"]) == 4
            for tx, transfer_row in inbound_rows
        ),
        "inbound": [
            {
                **tx_ref(tx),
                "source": transfer["source"],
                "amount_lamports": transfer["lamports"],
                "amount_SOL": transfer["SOL"],
            }
            for tx, transfer in inbound_rows
        ],
        "outbound": {
            **tx_ref(outbound_tx),
            "destination": outbound_transfer["destination"],
            "amount_lamports": outbound_transfer["lamports"],
            "amount_SOL": outbound_transfer["SOL"],
        },
        "forward_equals_aggregate_minus_fee": (
            outbound_transfer["lamports"] == aggregate - outbound_tx["fee_lamports"]
        ),
        "full_balance_relay": full_balance,
    }


def summarize_funder(label, rows):
    address = rows[0]["subject_address"]
    outbound = []
    inbound = []
    for tx in rows:
        for transfer in incoming(tx, address):
            inbound.append((tx, transfer))
        for transfer in outgoing_to(tx, address, HP4Q):
            outbound.append((tx, transfer))
    outbound.sort(key=lambda item: (item[0]["slot"], item[0]["transaction_index"]))
    large_out, small_out = outbound
    large_in = [item for item in inbound if item[0]["block_time"] <= large_out[0]["block_time"]]
    small_in = [item for item in inbound if item[0]["block_time"] > large_out[0]["block_time"]]
    large_in.sort(key=lambda item: (item[0]["slot"], item[0]["transaction_index"]))
    small_in.sort(key=lambda item: (item[0]["slot"], item[0]["transaction_index"]))
    large = cycle_summary(large_in, *large_out)
    small = cycle_summary(small_in, *small_out)
    same_sources = large["upstream_wallets"] == small["upstream_wallets"]
    return {
        "label": label,
        "address": address,
        "history_transaction_count": len(rows),
        "history_first_UTC": rows[0]["UTC"],
        "history_last_UTC": rows[-1]["UTC"],
        "history_profile": "short-history; exactly ten finalized transactions",
        "large_cycle": large,
        "small_cycle": small,
        "same_upstream_wallets_repeat_in_small_cycle": same_sources,
        "outbound_signer_and_fee_payer_are_subject": all(
            tx["signers"] == [address] and tx["fee_payer"] == address
            for tx, _ in outbound
        ),
        "classification": (
            "CONFIRMED full-balance relay"
            if large["full_balance_relay"] and small["full_balance_relay"] and same_sources
            else "unresolved"
        ),
    }


def immediate_upstream_batches(funders):
    grouped = {}
    for funder in funders:
        for cycle_name in ("large_cycle", "small_cycle"):
            for item in funder[cycle_name]["inbound"]:
                key = item["signature"]
                row = grouped.setdefault(key, {
                    "cycle": cycle_name,
                    "source": item["source"],
                    "signature": key,
                    "UTC": item["UTC"],
                    "slot": item["slot"],
                    "transaction_index": item["transaction_index"],
                    "fee_lamports": item["fee_lamports"],
                    "signers": item["signers"],
                    "fee_payer": item["fee_payer"],
                    "recipients": [],
                })
                row["recipients"].append({
                    "address": funder["address"],
                    "amount_lamports": item["amount_lamports"],
                    "amount_SOL": item["amount_SOL"],
                })
    return sorted(grouped.values(), key=lambda row: (row["slot"], row["transaction_index"]))


def unique_transactions(manifest_sets):
    result = {}
    for label, rows in manifest_sets:
        for row in rows:
            signature = row["signature"]
            if signature not in result:
                result[signature] = {**row, "observed_in": []}
            result[signature]["observed_in"].append(label)
    return [result[key] for key in sorted(result)]


def main():
    funder_manifests = read_manifests(FUNDER_ROOT)
    upstream_manifests = read_manifests(UPSTREAM_ROOT)
    infra_manifests = read_manifests(INFRA_ROOT)
    funders = [summarize_funder(label, rows) for label, rows in sorted(funder_manifests.items())]
    batches = immediate_upstream_batches(funders)
    all_sets = []
    for prefix, manifests in (
        ("funder", funder_manifests),
        ("upstream", upstream_manifests),
        ("infrastructure", infra_manifests),
    ):
        all_sets.extend((f"{prefix}:{label}", rows) for label, rows in manifests.items())
    result = {
        "case": "ZYROX Hp4q ten-funder batch-construction fingerprint v0.120",
        "generated_utc": "2026-10-11T00:00:00Z",
        "baseline_commit": "d38a3ace79547f70b8f03dfa3fc237c2dffe4651",
        "rpc_endpoint": "https://api.mainnet-beta.solana.com",
        "rpc_commitment": "finalized",
        "classification_boundary": (
            "Repeated construction supports coordinated launch operations and common infrastructure. "
            "It does not establish shared private keys, common beneficial ownership, or real-world identity."
        ),
        "funder_count": len(funders),
        "confirmed_full_balance_relay_count": sum(
            funder["classification"] == "CONFIRMED full-balance relay" for funder in funders
        ),
        "funders": funders,
        "immediate_upstream_batches": batches,
        "unique_immediate_upstream_wallets": sorted({row["source"] for row in batches}),
        "unique_transactions": unique_transactions(all_sets),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        f"{OUTPUT}: {len(funders)} funders, {len(batches)} immediate batches, "
        f"{len(result['unique_transactions'])} unique transactions"
    )


if __name__ == "__main__":
    main()
