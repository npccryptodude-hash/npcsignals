# NPCsignals — Gamdom G008
Upstream Funding and EIP-7702 Authorization Audit — 15 October 2026.

Starting checkpoint: `bc834822f0e4956fc78c1746eb958fecb290ef39`. Both previous evidence directories are preserved unchanged. This is a versioned sibling checkpoint; no G007 is asserted or reconstructed.

## Strongest new result
The saved 979-byte type-4 transaction independently hashes to `0xf1d9478bfcccf3dcc7ea5211fd7924230226be0bee7a5b96d767cc9f7167e9a2`. Cryptographic recovery identifies B as both outer transaction signer and EIP-7702 authorizing key. The authorization is chain ID 1, nonce 1, delegating to `0x63c0c19a282a1b52b07dd5a65b58948a07dae32b`. Outer nonce is 0. The calldata batches a USDT approval and an order pre-signature; receipt logs and the explorer's advanced call table show both effects.

This closes G006's authorization-signature recovery gap. It does not identify a human operator or establish that any extraction was unauthorized.

## Funding result
Five new Polygon transfer receipts are recorded: two D-to-C USDT0 inflows totalling 714.470970 USDT0 and three intervening C outflows totalling 539.775442 USDT0. The observed net change is +174.695528 USDT0 before the known anchor. Opening balances, exhaustive logs and exclusive provenance remain unresolved. D = `0xE757683a51CfD002De479385c2F4C9DB10A5E8D2`.

The five receipts are new; the previously recorded delegation and anchor are extended verification of existing transactions, not new transaction counts. No new native receipt was fully verified.

## Status
Evidence checkpoint PUBLISH; article HOLD. H1/H2/H3 remain unresolved. Historical RPC code state and later delegated-execution traces are blocked, documented in `blocker_report.md`.

Install `requirements.txt`, then run `python3 verify.py`. The cryptographic verification is offline and reproducible. Funding records and execution effects are transcribed explorer observations; integrity checks do not independently certify explorer completeness or blockchain inclusion.
