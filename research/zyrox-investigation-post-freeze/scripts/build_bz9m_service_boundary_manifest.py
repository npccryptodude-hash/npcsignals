#!/usr/bin/env python3
import hashlib
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
CASE = RAW / "bz9m_service_boundary_2026-10-11"
INFRA = RAW / "hp4q_known_infrastructure_2026-10-11"
OUTPUT = RAW / "bz9m_service_boundary_manifest_2026-10-11.json"

CHILDREN = {
    "62DW": "62DWdupxLroTc2jfiHEXdnzbg5aWemMHwkkTrpU9SNrN",
    "HuJg": "HuJgSFkbEGvfzmQgewAKRowAXZM3xMGjrxGyHQDTN5y4",
    "Aft6": "Aft6HWo4f4j32ALBLXWsU8LtxMHT4eWwaysVLW2msYow",
    "5vaQ": "5vaQEDDUw8NX5DDnpaxmDMxKGFCx7nXqkW43r7b6YSAF",
}

CHILD_PATHS = {
    "62DW": CASE / "62dw" / "manifest.json",
    "HuJg": CASE / "hujg" / "manifest.json",
    "Aft6": INFRA / "aft6" / "manifest.json",
    "5vaQ": INFRA / "5vaq" / "manifest.json",
}

SOURCE_PATHS = {
    "BZ9m": CASE / "bz9m" / "manifest.json",
    "FfRJ": CASE / "ffrj" / "manifest.json",
    "42D8": CASE / "42d8" / "manifest.json",
    "Goys": CASE / "goys" / "manifest.json",
    "HF7h": CASE / "hf7h" / "manifest.json",
    "APZk": CASE / "apzk" / "manifest.json",
    "Av44": CASE / "av44" / "manifest.json",
}

EIGHTYSB = "8ySbR18BZrfW98cKoroYLffSfUSwEJZyWQSrTkdyPLv2"
LARGE_SIGNATURE = "5FjePPLz2TRTk4Axzso1mTR4QpdbhLbM7zK7Nco122CyNyQ749v9VwTKoxGU1otHtXNErYTDEmFgGZBdezuBDhat"
SMALL_SIGNATURE = "2b7koW521Hmhy2R95t4bvpBBUBCZbb8v2MH5L1Ctg1ni5XrMGXBU5R6cQGaz7UYuyeyq2hU3bhtEXcmeRNpufkhX"


def read(path):
    return json.loads(path.read_text())


def tx_ref(row):
    return {
        "signature": row["signature"],
        "UTC": row["UTC"],
        "slot": row["slot"],
        "transaction_index": row["transaction_index"],
        "fee_lamports": row["fee_lamports"],
        "fee_payer": row["fee_payer"],
        "signers": row["signers"],
        "canonical_json_sha256": row["canonical_json_sha256"],
    }


def summarize_child(label, address, rows):
    incoming = []
    for row in rows:
        for transfer in row["native_transfers"]:
            if transfer["destination"] == address and transfer["source"] != address:
                incoming.append((row, transfer))
    incoming.sort(key=lambda item: (item[0]["slot"], item[0]["transaction_index"]))
    large = incoming[:4]
    small = incoming[4:]
    first = large[0]
    return {
        "label": label,
        "address": address,
        "history_transaction_count": len(rows),
        "history_first_UTC": rows[0]["UTC"],
        "history_last_UTC": rows[-1]["UTC"],
        "account_type_at_activity": "signer-capable native SOL system wallet; not a program account",
        "current_finalized_account_state": "null after zero-balance closure",
        "earliest_relevant_source": first[1]["source"],
        "earliest_relevant_edge": {
            **tx_ref(first[0]),
            "amount_lamports": first[1]["lamports"],
            "amount_SOL": first[1]["SOL"],
            "recipient_pre_balance_lamports": first[0]["subject_balance"]["pre_lamports"],
            "recipient_post_balance_lamports": first[0]["subject_balance"]["post_lamports"],
        },
        "large_cycle_sources": [item[1]["source"] for item in large],
        "small_cycle_sources": [item[1]["source"] for item in small],
        "same_sources_repeat": [item[1]["source"] for item in large] == [item[1]["source"] for item in small],
    }


def summarize_source(label, rows):
    address = rows[0]["subject_address"]
    incoming = []
    outgoing = []
    for row in rows:
        for transfer in row["native_transfers"]:
            if transfer["destination"] == address and transfer["source"] != address:
                incoming.append((row, transfer))
            if transfer["source"] == address:
                outgoing.append((row, transfer))
    incoming.sort(key=lambda item: (item[0]["slot"], item[0]["transaction_index"]))
    batch_rows = []
    seen = set()
    for row, _ in outgoing:
        if row["signature"] in seen:
            continue
        seen.add(row["signature"])
        transfers = [transfer for transfer in row["native_transfers"] if transfer["source"] == address]
        batch_rows.append({
            **tx_ref(row),
            "source_pre_balance_lamports": row["subject_balance"]["pre_lamports"],
            "source_post_balance_lamports": row["subject_balance"]["post_lamports"],
            "transfers": transfers,
        })
    return {
        "label": label,
        "address": address,
        "history_transaction_count": len(rows),
        "history_first_UTC": rows[0]["UTC"],
        "history_last_UTC": rows[-1]["UTC"],
        "history_profile": "short-lived four-transaction full-balance batch relay",
        "account_type_at_activity": "signer-capable native SOL system wallet; not a program account",
        "current_finalized_account_state": "null after zero-balance closure",
        "first_funder": incoming[0][1]["source"],
        "first_inbound": {
            **tx_ref(incoming[0][0]),
            "amount_lamports": incoming[0][1]["lamports"],
            "amount_SOL": incoming[0][1]["SOL"],
            "recipient_pre_balance_lamports": incoming[0][0]["subject_balance"]["pre_lamports"],
            "recipient_post_balance_lamports": incoming[0][0]["subject_balance"]["post_lamports"],
        },
        "outbound_batch_transaction_count": len({row["signature"] for row, _ in outgoing}),
        "outbound_batches": batch_rows,
        "self_signed_and_self_fee_paid_outbounds": all(
            row["signers"] == [address] and row["fee_payer"] == address for row, _ in outgoing
        ),
        "service_attribution": "UNRESOLVED; no independent service boundary",
    }


def batch_from_raw(signature):
    path = CASE / "bz9m" / f"tx_{signature}.json"
    tx = read(path)
    keys = tx["transaction"]["message"]["accountKeys"]
    payer = keys[0]["pubkey"] if isinstance(keys[0], dict) else keys[0]
    transfers = []
    for instruction in tx["transaction"]["message"]["instructions"]:
        parsed = instruction.get("parsed") if isinstance(instruction, dict) else None
        if not isinstance(parsed, dict) or parsed.get("type") != "transfer":
            continue
        info = parsed.get("info", {})
        if info.get("source") == payer and "lamports" in info:
            transfers.append({
                "destination": info["destination"],
                "amount_lamports": int(info["lamports"]),
                "amount_SOL": f"{int(info['lamports']) / 1_000_000_000:.9f}",
            })
    canonical = hashlib.sha256(json.dumps(tx, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {
        "signature": signature,
        "UTC": __import__("datetime").datetime.fromtimestamp(
            tx["blockTime"], __import__("datetime").timezone.utc
        ).isoformat().replace("+00:00", "Z"),
        "slot": tx["slot"],
        "transaction_index": tx["transactionIndex"],
        "fee_lamports": tx["meta"]["fee"],
        "pre_balance_lamports": tx["meta"]["preBalances"][0],
        "post_balance_lamports": tx["meta"]["postBalances"][0],
        "signers": [payer],
        "fee_payer": payer,
        "recipient_count": len(transfers),
        "transfers": transfers,
        "canonical_json_sha256": canonical,
    }


def main():
    children = [summarize_child(label, CHILDREN[label], read(CHILD_PATHS[label])) for label in CHILDREN]
    sources = [summarize_source(label, read(path)) for label, path in SOURCE_PATHS.items()]
    signatures = read(CASE / "8ysb" / "signatures.json")
    result = {
        "case": "ZYROX bounded service/custody attribution upstream of BZ9m children",
        "baseline_commit": "dfecd6c9d26b994d3d9887f15fac03fde007147d",
        "research_date_UTC": "2026-10-11",
        "rpc_endpoint": "https://api.mainnet-beta.solana.com",
        "rpc_commitment": "finalized",
        "children_examined": children,
        "direct_source_wallets": sources,
        "common_upstream_wallet": {
            "address": EIGHTYSB,
            "history_transaction_count": len(signatures),
            "history_first_UTC": __import__("datetime").datetime.fromtimestamp(
                signatures[-1]["blockTime"], __import__("datetime").timezone.utc
            ).isoformat().replace("+00:00", "Z"),
            "history_last_UTC": __import__("datetime").datetime.fromtimestamp(
                signatures[0]["blockTime"], __import__("datetime").timezone.utc
            ).isoformat().replace("+00:00", "Z"),
            "account_type_at_activity": "signer-capable native SOL system wallet; not a program account",
            "current_finalized_account_state": "null after zero-balance closure",
            "large_batch": batch_from_raw(LARGE_SIGNATURE),
            "small_repeat_batch": batch_from_raw(SMALL_SIGNATURE),
            "service_attribution": "UNRESOLVED; no independent service boundary",
        },
        "current_account_check": {
            "finalized_context_slot": 455641632,
            "addresses_checked": 12,
            "non_null_accounts": 0,
            "interpretation": "All examined zero-balance accounts currently return null; activity-time signatures remain authoritative.",
        },
        "public_attribution_check": {
            "exact_address_search_result": "No relevant exact-address results or first-party service documentation found.",
            "official_address_list_match": False,
            "protocol_owned_account_or_contract": False,
            "unmistakable_protocol_specific_infrastructure": False,
            "confirmed_service_exchange_custody_attribution": None,
        },
        "classification_boundary": (
            "The common 8ySb funding batch strengthens launch-operation topology only. "
            "It does not establish service custody, shared private keys, beneficial ownership, identity, or Kytro control."
        ),
        "branch_status": "PAUSED / EXHAUSTED at unlabeled signer-wallet boundary",
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"{OUTPUT}: {len(children)} children, {len(sources)} direct sources, {len(signatures)} 8ySb signatures")


if __name__ == "__main__":
    main()
