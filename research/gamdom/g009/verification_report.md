# Verification report — G009.2

## Verification depth

- Successful direct RPC chain ID 137, canonical-token Transfer queries, historical balanceOf and transaction/receipt/block reads are preserved as raw JSON.
- Thirteen selected receipts match transaction objects and block headers, including success status, actual initiating sender, canonical token, full addresses, raw value, transaction index and log index. Twelve are new beyond G008; the anchor is extended verification, not a new transaction count.
- The April 299.826616-USDT0 swap candidate is verified through raw transaction and receipt and separately observed explorer overview.
- The archive balance before the anchor is corroborated by a separately accessed explorer storage table. This is not a second independent node proof.
- Integer accounting reconciles the full bounded interval, recent funding window and anchor block against saved historical state with zero residual.
- Hash manifests, unique events, fixed query boundaries, deterministic derivation and frozen-directory preservation are checked offline by verify.py. Test output is saved in verification_results.txt.

## Reproduce offline

Run `PYTHONDONTWRITEBYTECODE=1 python3 verify.py` from this directory in the repository. Python standard library only. The Git object for starting commit ff920e52ed487b2f0d0a729c6f61f2d31fce4c2a is required for frozen-file comparison. No network call is made by this verifier. The deterministic derivation regenerates output CSVs and checks byte equality with the saved versions.

## Reproduce online

probe_historical_rpc.py repeats the fixed pre/post historical calls and records access results. collect_evidence.py collects the short initial query; collect_bounded_history.py collects both canonical event directions for the fixed broad interval. continue_collection.py and collect_final_checks.py reuse successful response files and add the selected transaction/header checks. These collectors write responses in their own G009 evidence directory; run in a separate copy to preserve the checkpoint. Endpoint access and response timestamps may differ later; byte-identical live responses are not promised.

## Limits

Checksums cover all published files except the manifest itself; __pycache__ is excluded and not published. A passing checksum does not prove chain consensus, ownership, intent or explorer correctness. No Merkle proof, independent node replay, complete lifetime history or recovered D signature is claimed. Event-only rows do not acquire invented initiating-sender metadata.

## Publication validation

Publish only the G009 sibling directory. After the branch update, fetch the remote commit, compare all package bytes, check that the diff adds only G009, and read back the README and reconciliation table. The final response supplies the verified remote commit SHA; this pre-publication report alone does not assert a successful push.
