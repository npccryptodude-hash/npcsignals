#!/usr/bin/env python3
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
OUTPUT = RAW / "arkham_hp4q_case_manifest_2026-10-11.json"


def main():
    histories = {}
    transactions = {}
    for path in sorted(RAW.glob("arkham_hp4q_*_2026-10-11/manifest.json")):
        label = path.parent.name.removeprefix("arkham_hp4q_").removesuffix("_2026-10-11")
        rows = json.loads(path.read_text())
        histories[label] = [row["signature"] for row in rows]
        for row in rows:
            signature = row["signature"]
            if signature not in transactions:
                transactions[signature] = dict(row, observed_in=[])
            transactions[signature]["observed_in"].append(label)

    result = {
        "case": "ZYROX Arkham Hp4q funding checkpoint v0.119",
        "generated_utc": "2026-10-11T00:00:00Z",
        "rpc_endpoint": "https://api.mainnet-beta.solana.com",
        "rpc_commitment": "finalized",
        "methods": ["getSignaturesForAddress", "getTransaction(jsonParsed)"],
        "classification_boundary": (
            "Public on-chain transaction evidence only. No exchange, service, "
            "real-world identity, common-owner, or beneficial-owner attribution."
        ),
        "address_histories": histories,
        "transactions": [transactions[key] for key in sorted(transactions)],
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"{OUTPUT}: {len(histories)} histories, {len(transactions)} unique transactions")


if __name__ == "__main__":
    main()
