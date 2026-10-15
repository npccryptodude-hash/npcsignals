# NPCsignals — Gamdom G011

BNB Chain Incident-Origin Reconstruction. Research date: 15 October 2026. Starting checkpoint: `2a5fb31c97a39f9aebaf945dee8b5e0d05110b19`.

## Strongest new finding

B's 370000-USDT Relay deposit was preceded by **three direct USDT payments from S1**, the exact G010 Ethereum source address **0x0067cc2416f792cf0ec5629f5506324ac508f859**. They total **373296.947360645719 USDT**. B's historical balance immediately before the deposit is the same amount; the deposit leaves **3296.947360645719 USDT**. Opening balance at block 127399999 is independently queried as zero rather than assumed.

The second bridge has a different immediate source: **A, 0xd5fbda4c79f38920159fe5f22df9655fde292d47**, sends **336943.421822265793499428 USDT** after B has returned to a zero USDT balance. A held exactly this amount before the incident window. It is not the unspent remainder of the first 370000 deposit.

Signatures from the BNB source transactions recover the same respective A and S1 public keys as their saved G010 Ethereum payments to E1. A and S1 have distinct public keys. This establishes cross-chain signing continuity for each address, not shared ownership between A and S1, human identity or legitimate consent.

## Accounting and files

`results.json` gives the final distinct new-transaction count and earliest incoming receipt. `upstream_funding_ledger.json`, `transaction_register.json`, `B_ordered_balance_walk.json` and `historical_balance_reconciliation.json` preserve exact hashes, raw amounts, token decimals, initiators, fees and event ordering. JSON integers larger than safe floating-point precision are stored as strings.

B's bounded accounting: **0 + 714187.786405077034199428 incoming − 714187.786405077034199428 outgoing = 0 USDT**. Eight historical-state reconciliations, including S1 and A windows, have zero residual. Bridge and settlement intermediate transfers are not additional original principal or losses.

`upstream_provenance.md`, `control_assessment.md`, `coverage_report.md`, `blocker_report.md` and `verification_report.md` explain what the evidence proves. `rpc_archive.json.gz` is a deterministic compressed JSON object of named parsed acquisition records, including failures. `source_register.json` registers canonical-record digests. `signature_verification.json` preserves reconstructed signed envelopes, signature fields, recovered public keys and any EIP-7702 authorization tuples. Raw local evidence caches are retained but are not redundantly published.

Install the pinned requirements in an isolated environment, then run `python3 verify.py` offline in this directory inside the repository. See `replay.py --help` for read-only request reproduction into a separate output directory.

CONFIRMED: documented movements, historical states, exact matches and signatures at the stated scope. Gamdom ownership and unauthorized status: **UNRESOLVED**. Evidence checkpoint: **PUBLISH**. Medium and X: **HOLD**. No frozen evidence is modified.
