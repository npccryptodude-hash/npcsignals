# Binance Evidence Package v2.0 — archival completion

Assessment date: 2026-10-14 UTC. This archive consolidates original completed Work evidence and an independently rerun offline verification. It supersedes the preservation gaps in the previous secondary v2.0 summary. No new wallet history or attribution investigation was conducted. Two already documented linkage receipts were retrieved only to replace missing transport objects, with originals retained separately.

## Executive evidence summary

**CONFIRMED:** Four successful finalized native SOL transfers from the exact ZYROX primary-ledger U300 address, totalling **472.929423997 SOL**, and one successful finalized **995.831502 USDT** transfer authorized by 56HEQ, a direct counterparty of the documented cross-case wallet 6hR7. All five receiving native addresses or historical token-account owners resolve to the exact same public key:

`5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9`.

**SUPPORTED:** That exact receiving owner is Binance-attributed infrastructure according to two independent publishers, Bitquery and Solscan. Bitquery identifies a hot wallet. A Binance-authored exact-address/historical-control attestation was not recovered.

**UNRESOLVED:** Customer credit versus internal custodial movement, source-wallet custodial status, account identity, beneficial ownership, common human control, and exclusive token-sale origin. **NOT ASSESSED:** Wrongdoing or legal liability. No exchange contacted.

Ready for referral to an authorized investigator **as an exchange-infrastructure transfer lead**, not proof of a customer deposit or customer identity. Binance should independently establish historical custody and internal booking.

## Complete five-transfer index

All indices are zero-based. The complete receipt-derived fields, native/token pre/post balances, authorities, full signers, fee payers and source URLs are in [five-transfer-ledger.json](five-transfer-ledger.json) and [five-transfer-ledger.csv](five-transfer-ledger.csv).

| ID | UTC | Slot | Instruction | Asset/amount | Full signature |
|---|---|---:|---|---|---|
| BE001 | 2026-09-30 17:03:07 | 452026176 | outer:2 | 52.383204688 SOL | `3tPBHCeM4Y86RETWoAhmFKD1JjVs4GWduMxzsYwSstKktAKg3jovJbr54dUhaHfh1L8vxQJiGJ3BVgYhRs92vgWY` |
| BE002 | 2026-09-30 17:06:00 | 452026821 | outer:2 | 292.066250817 SOL | `4SxWP8XZRb3z1zg5dcTCsvGvMNtBm92zfibZ2KHySAVCZ34nTN9st6MrcaY7NnDfC8dsRsCMyiX6wMf4KoB9YsNm` |
| BE003 | 2026-09-30 17:12:00 | 452028164 | outer:2 | 105.583014451 SOL | `4xyFCL3f67ejRXTf3NZHgXScUVfXdCiWPsx9NNM1UWeNnmvMWcAFzGzYzGYapWFgHyFBD1aNmM9WDte7DbkpYnGe` |
| BE004 | 2026-10-14 06:00:01 | 456730989 | outer:2 | 22.896954041 SOL | `4m6gaPuwQnwN7KFSeCi3SzaqJzyj6JPzL5sMjq2c3gYuniYAqg3kZMPsseDdomzVJaVjZF3LPXYyHXAqeKKfSuYb` |
| BE005 | 2026-09-24 12:03:01 | 450023141 | outer:2 | 995.831502 USDT | `3QrJH49NS39jAtvEPn8BxCNGqkiwMZk1kSDJ2GU8f8jVU5GxVzxzd9bKSLx2KYkm7G6mPLP8Vsk3S94TuZMiayz2` |

BE001–004: native System Program transfers. Sender, authority, sole signer and fee payer are `8zHcWujHhyJri3CRTcWUGmT5WSRdwW7xrns3WTTkPGvS`. Receiver is the exact 5tz key above. Fees are 9,000 lamports each. Each source decrease equals transferred lamports plus its fee; receiver increase equals transferred lamports. Native SOL has no SPL token-account owner field. September 30 subtotal is 450.032469956 SOL; total is 472.929423997 SOL, plus 36,000 lamports of fees excluded from the transferred total.

BE005: SPL transferChecked, USDT mint `Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB`, six decimals. Source token account `CzissnPHhEu7NifSLfwhuvFMdfu7F8X4vR2HhF1o1PEL`; receiving token account `CyBjGpte4Npi5zNkdtWumPxVW4kpMR8BuFSbA587xZES`. Source historical owner and authority: `56HEQykziUkwvpK5uPzFrRbGD4Ek8HdWgjgeDvNmDoEJ`. Receiving historical owner: exact 5tz key, in both pre/post balances. Signers: fee payer `5JPAWfhLNsYVk3tPpD3gHvpHbvaXDbpUpy1wUfQVYRS2` and 56HEQ. Fee: 14,000 lamports. Fee sponsorship does not establish common control.

USDT source: 995.831502 → 0. Receiving account: 61,843,124.892138 → 61,844,120.723640. Native 56HEQ: 0 → 0 SOL; fee payer: 307.460059488 → 307.460045488 SOL. Source/receiving token-account rent balances remain 1,488,440 / 2,188,548 lamports. No closure or rent release is counted as an external transfer.

## Two documented network routes

### Route A — documented U300 to Binance-attributed infrastructure

ZYROX primary record U300 exactly names `8zHcWujHhyJri3CRTcWUGmT5WSRdwW7xrns3WTTkPGvS`, funded by `H85KW8sDNzbs2ykUuapYcdNhbwoNQfBn3zFZTvBdx7kG` with 139.458181476 SOL on 2026-10-02 11:42:19 UTC. Receipt:

`T7To7CBLjCmV16JL3vTyuTvgze5kuuRvXjdoP6AgmQiRu8urjsPGpJm3nsxypA9cipPD8UjmyMqeDBEvjAK55zk`.

The complete preserved primary ledger has Git blob SHA `08cf6b40c8aac00fb5d378ad1bc9b655bce62e55`, checked offline against the archived GitHub source record. Primary path: `research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md`. It is an address-level case linkage, not attribution of ownership.

Five previously verified GLITCH-linked routing transactions are preserved with original raw responses, finality and 17-row instruction/fee ledger in `originals/NPCsignals_Binance_U300/`:

| Direct edge | SOL | Full signature |
|---|---:|---|
| Documented GLITCH seller → R | 6.644549597 | `29d75Pa2Pu33b7r3dQam1FyKQTAP1e1YzwpejkkhxCHYwneJSFwJW1AGgnrgcC5hu2TfU5U7D6b1ppJvC5nwuqrB` |
| R → collector | 7.894545597 | `4oAiLXHcNk6sVYZJuQHPiKY3dWeoNstuKKABC2UZ1JmJKFQCfhdjCD84QNxRUvLuzhSLo57bYFCrieuw8uBnmeQp` |
| Collector → H2fv | 19.313574183 | `3VFwG45pKTaYCHMfqMQD426UkjWGMwooyMzWSwGjrFAqCHU4FReF8ZVSiUxeDsUiifV3zsUbh39AMHdf8DAJ9jtg` |
| H2fv → intermediary | 128.120287252 | `3hYxbjuVEGz6pvfRXW3smZyfeTv67TUrUHWfAL4PsN5h5ia9gvBb1accAEDuvNHANnTheZPkqL6FU7BqKe7XTtNh` |
| Intermediary → U300 | 128.120282252 | `4tKWJNnFjwr7J7JsVY8dMAAS1u2KfYpvQDHf9aHcbHpeP7pMCBMZ5xeQPRMFhgxMsnbdFMiKQfseKxz796t195zh` |

The original machine-readable route ledger contains full addresses, UTC, slots, instructions, signers and balances. Commingling precludes equating later U300 transfers to exclusive GLITCH proceeds. September 30 transfers predate the recorded ZYROX creator purchase and the October GLITCH launch. They are historical transfers by the same later-documented wallet, not launch-sale proceeds.

### Route B — documented 6hR7 to 56HEQ to Binance-attributed token account

Case wallet: `6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N`. Exact primary-ledger records U326/U327 document its token authority. U326 receipt is preserved in `supporting/`, with separately labelled replacement raw transport/finality; signature:

`2vj3WSdQ4LRhTzE5EGjutkAfXrtmhLMqaCRxYdAVeJqByPn5GmGsM7YYCASWhFP9uovjydBL91NZFJmtBcu1o51E`.

The documented GLITCH-linked B → 6hR7 receipt, 435.460959353 SOL at 2026-10-12 17:52:55 UTC, is also preserved/replaced separately:

`61v1KxQkjSpMTenBBKE3nCSyh4EBZFV8gffPdaNojEjXvvzavdCqEbHqWQ8ewf3eWPTiqrsLbUErdpbPzDFGp13B`.

B and 6hR7 balances were commingled. The September payments below precede that October receipt and the launches. This establishes historical transactional relationships, not forward tracing of October proceeds back into September.

| UTC 2026-09-24 | Slot | Instruction | USDT | Full signature |
|---|---:|---|---:|---|
| 11:49:54 | 450020165 | outer:4 | 4.028124 | `45zVBfuvgtptBZuABucUsMiPHYQfG4pf4ium1629LREQyeFqCWF1rEh5VM5pVT4ukmYPPr3LDMbs7F6ku2RDg1kw` |
| 11:57:57 | 450021997 | outer:2 | 991.803278 | `64voUTp7NHZMZieXJDnJ1yNfMHaCN9GtNFP39AqQxcgS6QTKCeeGzmJgeB3qPmsAFNpzZky3c6kYcYjVAUQ81MUJ` |

Both historical source token owners, authorities, sole signers and fee payers are the full case 6hR7 key. Receiving owner 56HEQ is established by historical token balances and initial initializeAccount3 evidence, not current account ownership.

The first payment created the receiving account (1,488,440 lamports rent funded by 6hR7); fees were 80,000 and 79,938 lamports, excluded from token amounts. Total **995.831402 USDT**. A different address, `6hR7yvr3V8igYCeiZaHpLh443kwKmgiiWL2DXk3ywv1N`, supplied 0.000100 USDT before BE005 and 0.001000 after it. It is **not** the case wallet; similar abbreviations are not evidence of a connection. Exact raw rollforward:

`0 + 995831402 + 100 - 995831502 + 1000 = 1000` (six decimals, closing 0.001000 USDT).

All five account-flow receipts, finality objects, 28-row instruction/fee ledger, rent/native balance audit and provider-returned owner/token-account histories with terminal pages are preserved unchanged in the 56HEQ package. Completeness is limited to the two specified account-key histories returned by the provider, not all possible closed or undiscovered accounts.

## Exchange attribution sources

- Bitquery: https://bitquery.io/investigations/libra-case-dismissed — exact 5tz key labelled Binance hot wallet. Its assertion about reserves is independent publisher evidence, not a retrieved Binance-authored binding. No relationship to LIBRA is inferred.
- Solscan: https://solscan.io/account/5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9 — captured title “Binance 2” corroborates exact-address attribution. Dynamic body was incompletely rendered.
- Binance official reserves page: https://www.binance.com/en/proof-of-reserves — exact-address binding not independently recovered.
- Binance official authorized-request guidance: https://www.binance.com/en/support/law-enforcement/guidelines . No contact made.

Original source registers retain URLs, targeted excerpts, provenance, conflicting limitations and unsuccessful endpoint checks. Full original HTML, notarized captures and Binance historical ownership confirmation are **NOT RECOVERED**. This archival pass did not refresh public labels or search new counterparties.

## Questions for authorized Binance records inquiries

For BE001–005, provide full signatures, UTC, slots, chain, exact amounts, receiving keys and USDT mint/account:

1. Did Binance control the receiving key and token account at each historical timestamp? What was their operational purpose?
2. Was each transfer a customer-credit deposit, internal treasury/sweep movement, uncredited transfer or other operation? Which internal IDs reconcile to it?
3. Did Binance also control U300, 56HEQ or the separate USDT fee payer? Confirm from internal records rather than public labels.
4. What relevant deposit/withdrawal instructions, booking, custody and legally available account records correspond to these signatures?
5. Preserve records and disclose only through a properly authorized lawful request. No claim is made that a source address identifies a particular customer.

## Preservation, reproducibility and limitations

- `original_archives/`: four original Work ZIPs, unchanged, plus the previous secondary-report ZIP unchanged. `archive-inventory.json` records exact byte sizes, member counts and SHA-256.
- `originals/`: exact member bytes unpacked from the three focused receipt archives for direct inspection. No receipt, original ledger, script or original checksum has been edited.
- `supporting/`: two unchanged previously captured parsed linkage objects, two replacement raw finalized getTransaction responses, requests, replacement status response/request and explicit provenance. Missing original transport objects have not been reconstructed.
- `five-transfer-ledger.json` / `.csv`: new consolidated index, not original RPC material. All five rows are recomputed and compared to source instructions/balances.
- `SHA256SUMS.json`: every file under this evidence directory except the checksum manifest itself. Git commits pin the manifest. The original archives retain their own internal manifests.
- `original-verification-results.json` and `offline-verification-results.txt`: actual passing replay results, not reported success alone.

Run from a clean checkout, with Python 3 standard library only:

```sh
python3 research/evidence/binance-v2.0-2026-10-14/verify.py
```

The verifier checks every manifest entry and file coverage; ZIP hashes/member bytes; replays all four original ZIP verifiers in isolated temporary directories; compares CSV/JSON fields; verifies five finalized status/receipt pairs, full signatures, UTC/slots/indices, amounts, historical owners, authority, signers/payer, fees and balances; and checks both replacement linkage receipts. It makes no network requests and does not modify the evidence tree. Do not run Python with `-O`, which disables assertions.

Optional CSV regeneration uses the supplied `build-ledger-csv.mjs` with `@oai/artifact-tool` in the documented Codex primary runtime. A small temporary directory must link runtime `node_modules`; run the copied builder with this evidence directory as its argument. Python replay does not require Node or this authoring dependency. Historical original builders may contain their original absolute Work paths; use each packaged `verify.py`, which resolves its own directory, for portable replay.

Checks demonstrate preserved-response consistency and integrity since capture, not cryptographic authentication of a remote provider, raw wire transaction signature verification, a fullblock independently verified transaction index, or Binance internal booking. Some responses expose provider-specific transactionIndex fields; UTC and slot are receipt fields. Original capture host-clock metadata is preserved but not trusted as event time; receipt blockTime supplies event UTC. RPC endpoint was `https://api.mainnet-beta.solana.com`; finalized receipts and separate getSignatureStatuses objects are archived.

No frozen research baseline was deleted or rewritten. Historical “none yet” and “not archived” findings remain dated observations; [documentation-reconciliation.md](documentation-reconciliation.md) records their supersession. The user's small test transaction is not intentionally introduced or used as evidence; this package preserves the scoped prior exports and no test-transaction investigation was performed.
