#!/usr/bin/env python3
"""Reproduce the bounded ZYROX launch-bundle verification.

The script queries only the known launch slot, four known transaction signatures,
the known Jito bundle identifier, and the corresponding Jito transaction lookup
endpoints. It performs no wallet-history or counterparty fan-out.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SOLANA_RPC = "https://api.mainnet-beta.solana.com"
JITO_INDEX = "https://bundles.jito.wtf/api/v1/bundles"
JITO_BLOCK_ENGINE = "https://mainnet.block-engine.jito.wtf/api/v1/bundles"
JITO_EXPLORER = "https://explorer.jito.wtf"
SLOT = 452_029_524
BUNDLE_ID = "bf5d05ae5acb728d02bd0f6e15c8e944f0dbe77874c5a6e6291b374cbcd011ed"
VALIDATOR_IDENTITY = "E1r4Psq84tHfQ6aPTvvDka4U3u8zPVD7gEUrH25RdxHL"
PROGRAM_8GXK = "8gxk64hYgGAEnHVhRMvBGVvBXZM5WhkGkaQ6DVgVV2kn"

TRANSACTIONS = [
    {
        "role": "creator_create_and_buy",
        "signature": "5ubvNRPDbdXtHaiexB4zroZxUDFS9mwDmDwJ3HnvdGrxuiqxDDGsZnkjdAGVHysDZgiCFqVASoinDu1bADPAbowo",
    },
    {
        "role": "hp4q_launch_purchase",
        "signature": "52ZjUbg4bzdQoAsFeJuLgqM5b5kmeQpgp79ndnAi13D7W795N8A7BLon9t7LhENRi5wUGcqMb5RWzNDs2AB9nKkw",
    },
    {
        "role": "intermediate_migration",
        "signature": "2MP6ABDBuCgMyAysTyNYjuFdR1AJ9eHJn4tzr1ae7DgHsYhEAsGgetnWVVpaatbZ1Dunk5Ns96PHxPm6q8gawdLB",
    },
    {
        "role": "hrpa_launch_purchase",
        "signature": "4JrhsmKT44mQpZh5kTYFMcFWXi2Hu8Lg3U5BkUS4WEw66pWeR7GkiR299KY2WFD5XZQTH5pvBMW957WrdjjRh5Xf",
    },
]

JITO_TIP_ACCOUNTS = {
    "96gYZGLnJYVFmbjzopPSU6QiEV5fGqZNyN9nmNhvrZU5",
    "HFqU5x63VTqvQss8hp11i4wVV8bD44PvwucfZ2bU7gRe",
    "Cw8CFyM9FkoMi7K7Crf6HNQqf4uEMzpKw6QNghXLvLkY",
    "ADaUMid9yfUytqMBgopwjb2DTLSokTSzL1zt6iGPaS49",
    "DfXygSm4jCyNCybVYYK6DwvWqjKee8pbDmJGcLWNDXjh",
    "ADuUkR4vqLUMWXxW9gh6D6L8pMSawimctcNZ5pGwDcEt",
    "DttWaMuVvTiduZRnguLF7jNxTgiMBZ1hyAumKUiL2KRL",
    "3AVi9Tg9Uo68tJfuvoKvqKNWKkC5wPdSSdeBnizKZ6jT",
}


def get_json(url: str) -> Any:
    request = urllib.request.Request(url, headers={"User-Agent": "NPCsignals/ZYROX-v0.122"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.load(response)


def post_json(url: str, payload: dict[str, Any]) -> Any:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json", "User-Agent": "NPCsignals/ZYROX-v0.122"},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.load(response)


def rpc(method: str, params: list[Any]) -> Any:
    response = post_json(
        SOLANA_RPC,
        {"jsonrpc": "2.0", "id": 1, "method": method, "params": params},
    )
    if "error" in response:
        raise RuntimeError(f"Solana RPC {method} failed: {response['error']}")
    return response["result"]


def canonical_hash(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def instruction_name(instruction: dict[str, Any]) -> str:
    parsed = instruction.get("parsed")
    if parsed:
        return f"{instruction.get('program')}:{parsed.get('type')}"
    return instruction.get("programId", "unknown")


def all_instructions(transaction: dict[str, Any]) -> list[tuple[str, str, dict[str, Any]]]:
    message = transaction["transaction"]["message"]
    rows: list[tuple[str, str, dict[str, Any]]] = [
        ("outer", str(index), instruction)
        for index, instruction in enumerate(message["instructions"])
    ]
    for group in transaction["meta"].get("innerInstructions") or []:
        rows.extend(
            ("inner", f"{group['index']}.{index}", instruction)
            for index, instruction in enumerate(group["instructions"])
        )
    return rows


def summarize_transaction(
    role: str,
    signature: str,
    transaction: dict[str, Any],
    block_signatures: list[str],
) -> dict[str, Any]:
    message = transaction["transaction"]["message"]
    meta = transaction["meta"]
    account_keys = message["accountKeys"]
    jito_tip_transfers: list[dict[str, Any]] = []
    native_transfers: list[dict[str, Any]] = []
    invoked_programs: list[str] = []

    for location, index, instruction in all_instructions(transaction):
        program_id = instruction.get("programId")
        if program_id and program_id not in invoked_programs:
            invoked_programs.append(program_id)
        parsed = instruction.get("parsed") or {}
        info = parsed.get("info") or {}
        if parsed.get("type") == "transfer" and "lamports" in info:
            transfer = {
                "location": location,
                "instruction_index": index,
                "source": info.get("source"),
                "destination": info.get("destination"),
                "lamports": info["lamports"],
                "sol": f"{info['lamports'] / 1_000_000_000:.9f}",
            }
            native_transfers.append(transfer)
            if info.get("destination") in JITO_TIP_ACCOUNTS:
                jito_tip_transfers.append(transfer)

    return {
        "role": role,
        "signature": signature,
        "slot": transaction["slot"],
        "transaction_index": block_signatures.index(signature),
        "block_time": transaction["blockTime"],
        "signers": [key["pubkey"] for key in account_keys if key["signer"]],
        "fee_payer": account_keys[0]["pubkey"],
        "fee_lamports": meta["fee"],
        "compute_units_consumed": meta.get("computeUnitsConsumed"),
        "outer_instruction_sequence": [instruction_name(ix) for ix in message["instructions"]],
        "invoked_programs": invoked_programs,
        "jito_tip_transfers": jito_tip_transfers,
        "native_transfers": native_transfers,
        "program_8gxk_present": any(key["pubkey"] == PROGRAM_8GXK for key in account_keys),
        "canonical_rpc_json_sha256": canonical_hash(transaction),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    block = rpc(
        "getBlock",
        [
            SLOT,
            {
                "encoding": "json",
                "transactionDetails": "signatures",
                "rewards": True,
                "commitment": "finalized",
                "maxSupportedTransactionVersion": 0,
            },
        ],
    )
    block_signatures = block["signatures"]

    jito_bundle_url = f"{JITO_INDEX}/bundle/{BUNDLE_ID}"
    jito_bundle_response = get_json(jito_bundle_url)
    transaction_lookups: dict[str, Any] = {}
    transactions: list[dict[str, Any]] = []
    for item in TRANSACTIONS:
        signature = item["signature"]
        transaction_lookups[signature] = get_json(f"{JITO_INDEX}/transaction/{signature}")
        raw_transaction = rpc(
            "getTransaction",
            [
                signature,
                {
                    "encoding": "jsonParsed",
                    "commitment": "finalized",
                    "maxSupportedTransactionVersion": 0,
                },
            ],
        )
        transactions.append(
            summarize_transaction(item["role"], signature, raw_transaction, block_signatures)
        )

    leader_schedule = rpc(
        "getLeaderSchedule",
        [SLOT, {"identity": VALIDATOR_IDENTITY, "commitment": "finalized"}],
    )
    epoch_slot_index = SLOT % 432_000

    tip_accounts_response = post_json(
        JITO_BLOCK_ENGINE,
        {"jsonrpc": "2.0", "id": 1, "method": "getTipAccounts", "params": []},
    )

    official_status = post_json(
        JITO_BLOCK_ENGINE,
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBundleStatuses",
            "params": [[BUNDLE_ID]],
        },
    )
    inflight_status = post_json(
        JITO_BLOCK_ENGINE,
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getInflightBundleStatuses",
            "params": [[BUNDLE_ID]],
        },
    )

    result = {
        "schema": "npcsignals.zyrox.launch_bundle_verification.v1",
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Known launch slot, four known signatures and one recovered bundle ID only; no wallet fan-out.",
        "sources": {
            "solana_rpc": SOLANA_RPC,
            "jito_historical_index": JITO_INDEX,
            "jito_explorer_bundle_url": f"{JITO_EXPLORER}/bundle/{BUNDLE_ID}",
            "jito_block_engine_status_rpc": JITO_BLOCK_ENGINE,
            "jito_documentation": "https://docs.jito.wtf/lowlatencytxnsend/",
        },
        "source_classification": {
            "solana_rpc": "primary finalized chain data",
            "jito_historical_index": (
                "Jito-hosted official Explorer historical bundle index referenced by Jito documentation; "
                "not the recent-status Block Engine RPC and not a third-party scanner"
            ),
            "jito_block_engine_status_rpc": "Jito Block Engine RPC with bounded recent-history retention",
        },
        "bundle_id": BUNDLE_ID,
        "jito_bundle_response": jito_bundle_response,
        "jito_transaction_lookup_responses": transaction_lookups,
        "block": {
            "slot": SLOT,
            "block_time": block["blockTime"],
            "block_height": block["blockHeight"],
            "blockhash": block["blockhash"],
            "previous_blockhash": block["previousBlockhash"],
            "transaction_count": len(block_signatures),
            "indices_1330_through_1333": block_signatures[1330:1334],
            "rewards": block["rewards"],
        },
        "transactions": transactions,
        "leader_verification": {
            "validator_identity": VALIDATOR_IDENTITY,
            "epoch_slot_index": epoch_slot_index,
            "getLeaderSchedule_available": leader_schedule is not None,
            "identity_returned_by_getLeaderSchedule": (
                VALIDATOR_IDENTITY in leader_schedule if leader_schedule is not None else None
            ),
            "slot_index_assigned_to_identity": (
                epoch_slot_index in leader_schedule.get(VALIDATOR_IDENTITY, [])
                if leader_schedule is not None
                else None
            ),
            "block_fee_reward_pubkeys": [
                reward["pubkey"]
                for reward in block["rewards"]
                if reward.get("rewardType") == "Fee"
            ],
            "historical_index_validator_receives_block_fee_reward": VALIDATOR_IDENTITY
            in {
                reward["pubkey"]
                for reward in block["rewards"]
                if reward.get("rewardType") == "Fee"
            },
        },
        "jito_block_engine_historical_status_attempts": {
            "getTipAccounts": tip_accounts_response,
            "getBundleStatuses": official_status,
            "getInflightBundleStatuses": inflight_status,
            "interpretation": (
                "These live methods do not retain definitive status for this ten-day-old bundle. "
                "An empty value or Invalid inflight result is not evidence that the historical bundle failed."
            ),
        },
        "checks": {
            "all_four_finalized_in_expected_slot": all(tx["slot"] == SLOT for tx in transactions),
            "all_four_lookup_to_same_bundle_id": all(
                transaction_lookups[tx["signature"]]
                == [{"bundle_id": BUNDLE_ID}]
                for tx in transactions
            ),
            "historical_bundle_lists_exact_four_in_block_order": bool(jito_bundle_response)
            and jito_bundle_response[0].get("txSignatures")
            == [item["signature"] for item in TRANSACTIONS],
            "block_indices_are_contiguous_1330_to_1333": [
                tx["transaction_index"] for tx in transactions
            ]
            == [1330, 1331, 1332, 1333],
            "bundle_landed_compute_units_equal_transaction_sum": bool(jito_bundle_response)
            and jito_bundle_response[0].get("landedCu")
            == sum(tx["compute_units_consumed"] for tx in transactions),
            "direct_jito_tip_lamports_equal_bundle_record": bool(jito_bundle_response)
            and sum(
                transfer["lamports"]
                for tx in transactions
                for transfer in tx["jito_tip_transfers"]
            )
            == jito_bundle_response[0].get("landedTipLamports"),
            "direct_jito_tip_destination_in_live_tip_account_list": all(
                transfer["destination"] in tip_accounts_response.get("result", [])
                for tx in transactions
                for transfer in tx["jito_tip_transfers"]
            ),
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(args.output)
    print(canonical_hash(result))


if __name__ == "__main__":
    main()
