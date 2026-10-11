#!/usr/bin/env python3
import argparse
import datetime as dt
import hashlib
import json
import pathlib
import time
import urllib.request

RPC = "https://api.mainnet-beta.solana.com"


def rpc(method, params):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    req = urllib.request.Request(RPC, data=body, headers={"content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as response:
        value = json.loads(response.read())
    if value.get("error"):
        raise RuntimeError(value["error"])
    return value["result"]


def key_value(key):
    return key if isinstance(key, str) else key["pubkey"]


def transfers(tx):
    rows = []
    groups = [("outer", tx["transaction"]["message"].get("instructions", []))]
    for group in tx.get("meta", {}).get("innerInstructions") or []:
        groups.append((f"inner:{group['index']}", group["instructions"]))
    for scope, instructions in groups:
        for index, instruction in enumerate(instructions):
            parsed = instruction.get("parsed") if isinstance(instruction, dict) else None
            if not isinstance(parsed, dict) or parsed.get("type") != "transfer":
                continue
            info = parsed.get("info", {})
            if "lamports" in info and "source" in info and "destination" in info:
                rows.append({
                    "scope": scope,
                    "instruction_index": index,
                    "source": info["source"],
                    "destination": info["destination"],
                    "lamports": int(info["lamports"]),
                    "SOL": f"{int(info['lamports']) / 1_000_000_000:.9f}",
                })
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("address")
    parser.add_argument("outdir", type=pathlib.Path)
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    signatures = rpc("getSignaturesForAddress", [args.address, {"limit": 1000, "commitment": "finalized"}])
    (args.outdir / "signatures.json").write_text(json.dumps(signatures, indent=2) + "\n")
    manifest = []
    for offset, item in enumerate(reversed(signatures)):
        signature = item["signature"]
        tx = rpc("getTransaction", [signature, {"encoding": "jsonParsed", "commitment": "finalized", "maxSupportedTransactionVersion": 0}])
        raw = json.dumps(tx, indent=2, sort_keys=True) + "\n"
        (args.outdir / f"tx_{signature}.json").write_text(raw)
        keys = tx["transaction"]["message"]["accountKeys"]
        signers = [key_value(key) for key in keys if isinstance(key, dict) and key.get("signer")]
        payer = key_value(keys[0])
        manifest.append({
            "signature": signature,
            "slot": tx["slot"],
            "transaction_index": tx.get("transactionIndex", item.get("transactionIndex")),
            "block_time": tx["blockTime"],
            "UTC": dt.datetime.fromtimestamp(tx["blockTime"], dt.timezone.utc).isoformat().replace("+00:00", "Z"),
            "success": tx["meta"]["err"] is None,
            "fee_lamports": tx["meta"]["fee"],
            "fee_payer": payer,
            "signers": signers,
            "native_transfers": transfers(tx),
            "canonical_json_sha256": hashlib.sha256(json.dumps(tx, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
        })
        if offset + 1 < len(signatures):
            time.sleep(0.15)
    (args.outdir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"address": args.address, "transactions": len(manifest), "manifest": manifest}, indent=2))


if __name__ == "__main__":
    main()
