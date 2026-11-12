#!/usr/bin/env python3
"""read-only frogman receipt verifier. no keys or paid services required.

usage:
  python3 verify_arbitrum_receipts.py --rpc https://YOUR_ARBITRUM_RPC --markdown PRIMARY_TRANSACTION_CHECKS_2026-11-12.md --out receipt_audit.json

requires: python 3.10+ standard library only.
"""
import argparse
import datetime
import json
import re
import sys
import urllib.request
from pathlib import Path

USDC = "0xaf88d065e77c8cc2239327c5edb3a432268e5831"
BRIDGE = "0x2df1c51e09aecf9cacb7bc98cb1742757f163df7"
TRANSFER_TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
PATTERN = re.compile(r"\|\s*arbi-(\d+)\s*\|[^\n]*?https://arbiscan\.io/tx/(0x[a-fA-F0-9]{64})")

def rpc(url, method, params):
    data = json.dumps({"jsonrpc":"2.0","id":1,"method":method,"params":params}).encode()
    request = urllib.request.Request(url, data=data, headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(request, timeout=25) as response:
        body = json.load(response)
    if body.get("error"):
        raise RuntimeError(str(body["error"]))
    if "result" not in body:
        raise RuntimeError("rpc response missing result")
    return body["result"]

def addr(topic):
    return "0x" + topic[-40:].lower()

def check(url, index, tx):
    receipt = rpc(url, "eth_getTransactionReceipt", [tx])
    if not receipt:
        return {"id":index,"hash":tx,"status":"receipt_missing"}
    transfers = []
    for log in receipt.get("logs", []):
        topics = log.get("topics", [])
        if (log.get("address", "").lower() == USDC
            and len(topics) == 3
            and topics[0].lower() == TRANSFER_TOPIC
            and addr(topics[2]) == BRIDGE):
            transfers.append({
                "sender":addr(topics[1]),
                "recipient":BRIDGE,
                "usdc_raw":str(int(log["data"],16)),
                "log_index":int(log["logIndex"],16),
            })
    return {
        "id":index,
        "hash":tx,
        "status":"confirmed" if int(receipt["status"],16)==1 and transfers else "not_confirmed",
        "success":int(receipt["status"],16)==1,
        "block":int(receipt["blockNumber"],16),
        "transfer_events":transfers,
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--rpc",required=True,help="arbitrum one json-rpc url")
    ap.add_argument("--markdown",required=True,type=Path)
    ap.add_argument("--out",required=True,type=Path)
    args=ap.parse_args()
    content=args.markdown.read_text(encoding="utf-8")
    matches=PATTERN.findall(content)
    mapping={}
    for number, tx in matches:
        number=int(number)
        if number in mapping and mapping[number].lower()!=tx.lower():
            raise ValueError(f"conflicting hashes for arbi-{number}")
        mapping[number]=tx.lower()
    if not mapping:
        raise ValueError("no transaction hashes found")
    if len(set(mapping.values())) != len(mapping):
        raise ValueError("duplicate hashes in receipt list")
    chain_id = int(rpc(args.rpc, "eth_chainId", []), 16)
    if chain_id != 42161:
        raise ValueError(f"wrong chain id: {chain_id}; expected arbitrum one (42161)")
    results=[]
    for index, tx in sorted(mapping.items()):
        try:
            results.append(check(args.rpc,index,tx))
        except Exception as exc:
            results.append({"id":index,"hash":tx,"status":"rpc_error","error":str(exc)})
    report={
        "checked_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "chain":"arbitrum one",
        "chain_id_expected":42161,
        "usdc_contract":USDC,
        "bridge_address":BRIDGE,
        "rows_found":len(mapping),
        "results":results,
    }
    args.out.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    confirmed=sum(r["status"]=="confirmed" for r in results)
    print(f"verified {confirmed}/{len(results)} transaction receipts; saved {args.out}")
    return 0 if confirmed==len(results) and len(results)==35 else 1

if __name__=="__main__":
    sys.exit(main())
