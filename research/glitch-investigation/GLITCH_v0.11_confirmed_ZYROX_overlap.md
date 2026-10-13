# GLITCH v0.11 — Confirmed exact-wallet overlap with ZYROX

**Reported verification:** ChatGPT Work finalized Solana RPC, 2026-10-13. User supplied complete evidence table. Existing ZYROX primary ledger wallet register C3 was checked by Work at GitHub commit `6a70d5c1e2e3494de6854c74c385e97be3a5bb57`. The five historical ZYROX receipts were **not freshly fetched** in this pass; the GLITCH receipt **was freshly fetched and its finalized status checked**. This document records Work evidence; raw JSON not bundled here.

## CROSS001 — Exact address match

Both case ledgers identify wallet:

`6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N`

The entire 44-character base58 public key matched exactly, not merely abbreviated prefix. Wallet-level overlap **CONFIRMED**. Identity, operator, beneficial ownership and Kytro attribution **UNRESOLVED**.

## ZYROX recorded role (primary-ledger references)

| ID | Direct link | UTC | SOL | Signature |
|---|---|---|---:|---|
| U238 | 6cn → 6hR7 | 2026-09-30 17:50:20 | 468.432649156 | `5weXc9NJeVf146desr178oLTG212TcWA4BGL6kg8evYPkv7GSkgpBF8gi2zcnigsbmBhd7Yv9d4KXXj6XzUguMoc` |
| U223 | F1dC → 6hR7 | 2026-09-30 17:59:50 | 175.588375882 | `4FCWGXKuXEL1hP5xedobbPD3p1brbhxvYC5MYt7uJ9Q3XmUtphrq9SU4VbMTNJBZk9xwU5geeYqaXywjLBqsD4MF` |
| U310 | 6hR7 → HZrAo creator | 2026-10-01 00:43:38 | 0.033895331 | `3JWGXtN3zexApXRScudWYNW7mQsRzkBps32BfQ6N7A28rupXEWQwovG1AbsqYfBgWQLVHmmUwcDpUxqaXoPW35AM` |
| U233 | 6hR7 → CAxTx | 2026-10-01 00:46:41 | 0.033886730 | `9GsTfDm5Fvs3ZwGrMUZYZAt67V6WdLJpBjwYvNcVTKVrDJgtTkDjXe562eaX1eJShEnmUWi7h4vYipEasw55zVL` |
| U232 | 6hR7 → BbBZ | 2026-09-06 20:32:13 | 2.947003195 | `4S3zbUE8PLkNJFUHxHFHi1PbZfkgNZ8snGb93gTTKEHoYFKj2Tr3VcBCN7XVvSUXoumWNgTowYBea2qNmNURgmzo` |

Counterparties:
- 6cn `6cnRXniBFNYrxnMebd5vqEv2d5wuXumbKwWkBjV8b88L`
- F1dC `F1dCFudwvrwCmUUbVTG1oYt3iWJpXEajrNgr3RNX5mpG`
- ZYROX creator HZrAo `HZrAoEWQGd5dsTzkj7YbzQq5ou3YQEWQQWvjBNRG9Atu`
- CAxTx `CAxTxHsiBB6Y5kAAMQuPbQdAwyLrEuFYoio5YGwMwtGD`
- BbBZ `BbBZuboLxyw3LBjjMBb6RCn9UP3Bz9DwctNgRmuwvR1f`

ZYROX's previous v0.91 control assessment remains UNRESOLVED; it did not establish control of counterparties' private keys.

## GLITCH confirmed direct receipt into 6hR7

Sender `F2khA1QZooUzidyycMzpJ6x38eQBxuDq4UrvdUUiSwuo` (B).
Recipient `6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N`.
Transaction `61v1KxQkjSpMTenBBKE3nCSyh4EBZFV8gffPdaNojEjXvvzavdCqEbHqWQ8ewf3eWPTiqrsLbUErdpbPzDFGp13B`.
Timestamp `2026-10-12T17:52:55Z`. Slot `456135573`, transaction index 47, outer instruction index 1; parsed System Program transfer `435460959353` lamports = **435.460959353 SOL**.
Signer and fee payer B alone. Finalized, `meta.err=null`, status Ok.
6hR7 before/after: 316.491815962 → 751.952775315 SOL.
6hR7 was **recipient, not signer**, for this GLITCH-linked receipt.

Prior GLITCH v0.9 documents seller → B 150.173828355 SOL, and B later also received 157.926482647 SOL through other inflows. Hence **435.460959353 SOL is commingled, not exclusively attributable to GLITCH sale**.

## Conclusion and strict limits

**CONFIRMED:** one exact Solana wallet participated as a recipient/funder in ZYROX-documented transfers and later received SOL from a direct downstream recipient of a major GLITCH seller. This is a cross-case *transaction-network connection*, not a proven shared operator.

**UNRESOLVED:** Kytro control, common individual/operator, ultimate beneficial owner, whether the shared wallet is a service, economic ownership of the commingled SOL, human identity.

**Next focused test:** inspect 6hR7's immediate subsequent outgoing activity after GLITCH receipt; preserve receipts; compare exact signers and ZYROX-known counterparties, without equating shared infrastructure with common control. No publication of individual allegations.
