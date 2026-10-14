# NPCsignals — Binance U300 evidence package v1.0

Assessment date: 2026-10-14 UTC. Network: Solana Mainnet. No Binance contact and no GitHub changes.

## Referral recommendation

**Ready for referral to an authorized investigator as a reproducible exchange-inbound transaction lead.** This package establishes the on-chain transfer and documented network relationships. Binance affiliation and hot-wallet function are SUPPORTED by independent public sources. Customer credit, sender custodial status and human control remain UNRESOLVED. This is not a finding of fraud, common ownership or a specific customer's receipt. Its purpose is to give an authorized investigator an exact transaction that Binance can locate and classify internally.

## Verified transfer — BP001

Signature: `4m6gaPuwQnwN7KFSeCi3SzaqJzyj6JPzL5sMjq2c3gYuniYAqg3kZMPsseDdomzVJaVjZF3LPXYyHXAqeKKfSuYb`

Source: `8zHcWujHhyJri3CRTcWUGmT5WSRdwW7xrns3WTTkPGvS`

Destination: `5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9`

**CONFIRMED:** successful finalized System Program transfer, outer:2 (zero-based), 22,896,954,041 lamports / 22.896954041 native SOL, 2026-10-14 06:00:01 UTC, slot 456730989. RPC-reported transaction index 351. The source is the native transfer authority, sole signer and fee payer. Fee 9,000 lamports. The new parsed receipt is identical to the prior pass's parsed receipt, and finality was independently rechecked through getSignatureStatuses.

| Account | Pre lamports | Post lamports | Delta lamports |
|---|---:|---:|---:|
| Source | 25,216,560,668 | 2,319,597,627 | -22,896,963,041 |
| Destination | 1,712,155,917,758,799 | 1,712,178,814,712,840 | +22,896,954,041 |

Source decline = transfer + fee. Destination increase = transfer. Native SOL has no SPL mint or token-account owner field. Account-key roles are recorded in the receipt. Outer:0 and outer:1 are Compute Budget instructions, not transfers. There is no wrapping/unwrapping, account closure, swap, bridge or staking instruction in this transaction. The transaction index is preserved as provider-reported; this pass did not independently retrieve the full block to verify its positional index.

Explorer: https://explorer.solana.com/tx/4m6gaPuwQnwN7KFSeCi3SzaqJzyj6JPzL5sMjq2c3gYuniYAqg3kZMPsseDdomzVJaVjZF3LPXYyHXAqeKKfSuYb

## Attribution and receiving function

**SUPPORTED:** exact recipient is Binance infrastructure, described as a Binance hot wallet by Bitquery's own research, with independent exact-address Solscan title corroboration. A hot-wallet classification fits the public attribution; the large transaction-time balance is not independently sufficient to establish ownership or function.

**UNRESOLVED:** the exact recipient binding on Binance's own publication. The dynamic official reserves page exposed no readable exact-address list. Search results on Binance Square were third-party posts and excluded. The starting document's separate Solscan Funded by corroboration was not re-rendered in this pass. All observations, URLs and conflicts are preserved in attribution-sources.json.

**UNRESOLVED:** whether this particular inbound transfer generated customer credit, was an internal custodial sweep, or had another operational purpose. This was not a withdrawal from the attributed hot wallet: the parsed transfer direction is source → hot wallet. Nevertheless, if the source itself is a Binance-controlled address, it may be internal. No deposit-endpoint or customer assignment is inferred from a hot-wallet label.

## Independently verified network connections

**ZYROX — CONFIRMED:** exact U300 primary-ledger public key equals BP001 source. Its primary record identifies receipt of 139.458181476 SOL from `H85KW8sDNzbs2ykUuapYcdNhbwoNQfBn3zFZTvBdx7kG` on 2026-10-02 11:42:19 UTC. BP002 independently reproduces the successful finalized transfer, slot 452599835, outer:0; H85 is sole signer/fee payer and authority, fee 5,000 lamports. H85 drained from 139.458186476 SOL to zero; U300 increased from 0.009996000 to 139.468177476 SOL.

BP002 signature: `T7To7CBLjCmV16JL3vTyuTvgze5kuuRvXjdoP6AgmQiRu8urjsPGpJm3nsxypA9cipPD8UjmyMqeDBEvjAK55zk`.

Current GitHub primary blob SHA: `08cf6b40c8aac00fb5d378ad1bc9b655bce62e55`. The complete preserved primary file matches that Git blob hash. U300 excerpt and source-response metadata are included. The requested single-line API excerpt returned empty content; this is disclosed rather than treated as readable independent text. Source: https://github.com/npccryptodude-hash/npcsignals/blob/main/research/zyrox-investigation/evidence/ZYROX_Devsold_verification_v0_2.md

**GLITCH route — CONFIRMED selected transactional edges:** five prior documented transactions were re-fetched as successful finalized receipts. Roles, signatures, UTC, slots, balances and fees are fully reproduced in the CSV and JSON ledgers:

| ID | Date/time UTC | Source → destination | SOL |
|---|---|---|---:|
| BP007 | October 12 17:51:19 | Documented GLITCH seller → R | 6.644549597 |
| BP006 | October 13 19:02:50 | R → Collector | 7.894545597 |
| BP005.I0 | October 13 19:12:13 | Collector → H2fv | 19.313574183 |
| BP004 | October 13 23:08:21 | H2fv → 3wcts | 128.120287252 |
| BP003 | October 13 23:08:24 | 3wcts → U300 | 128.120282252 |

Exact addresses:

- Documented GLITCH seller: `8hiMXA1UHYUAeW6gd6q1XQLWzZkQL48znqgdgY1388B7`
- R: `DYxqyuLyttmd1XbTXeeZCKKEQN1MCGws3aSYLakYeb6f`
- Collector: `7aTpxyyaVhgKY8irjffP2uFkD5379aepfPfJtjYLqZAk`
- H2fv: `H2fvqz3zjr3GgwENZXoWZoafBV3jC48KRShZYfJAuvtv`
- 3wcts: `3wctsmdJtm4EDBmRfLcpCSi4AoZwEMcodqfXgHPK8FJP`

The seller role comes from preserved GLITCH v0.9 documentation; the sale itself was not re-investigated in this pass. Current Exchange Attribution Ledger v0.2 documents R → Collector → H2fv and was fetched again. The exact five outgoing edges, not sale-profit exclusivity, are the new independent receipt checks. BP005 also pays the already documented 99Gc wallet 3.408277796 SOL in outer:1; this instruction is retained for whole-transaction accounting and not investigated further.

**Commingling:** the seller had pre-existing SOL, R/Collector/H2fv received other funds, and U300 held 203.187642544 SOL before BP003, increasing to 331.307924796 SOL. BP001 occurs later with an opening balance of 25.216560668 SOL; intervening U300 activity was not reconstructed here. No claim traces a specific GLITCH-derived amount through this entire route into Binance. Transactional connection and exchange-bound payment are established as separate facts.

## Bounded additional-payment screen

786 unique preserved receipt objects across six existing case folders were screened for successful parsed instructions whose destination exactly equals this receiver. Only BP001 matched. **CONFIRMED bounded null result:** no additional exact parsed-destination transfer found in this set. This is not a claim that no other deposits exist. Two unparsed instruction objects, undiscovered addresses, historical token accounts and exact token-owner matches were not exhaustively tested. Failed transactions were excluded from executed flows. Inventory, hashes, directory counts and match results are preserved in bounded-additional-scan.json; unmatched originals remain in earlier packages.

NOT ASSESSED: all-network lifetime history, complete token-account ownership histories, recipient downstream movements and private ownership. Prior U300 pagination preserved 93,000 references but never reached an empty terminal page; no lifetime completeness claim is made or new pagination started.

## Questions for an authorized Binance records inquiry

Supply BP001's complete signature, network, UTC, slot, source, destination, exact lamports and receipt. Ask Binance to establish:

1. Whether Binance controlled the destination at this transaction time, and its operational classification.
2. Whether the source was also Binance-controlled or a customer deposit/sweep address.
3. Whether the transaction created customer credit, represented an internal sweep, or was booked otherwise; the matching internal transaction identifier and booking timestamps.
4. Any corresponding account identifier and legally disclosable account/verification records, with the distinction between account holder and actual initiating user preserved.
5. Related internal movement records needed to interpret this specific receipt, and record retention/preservation availability under the applicable lawful request.

These are proposed questions, not assertions that the records exist or identify a particular person. A sender's signing authority is not proof of private human control.

Official guidelines: https://www.binance.com/en/support/law-enforcement/guidelines . Access: https://www.binance.com/en/support/law-enforcement . Binance specifies the government/law-enforcement channel, supporting documentation and appropriate legal process. Private parties should not impersonate an authorized requester. No contact was made.

## Preservation, reproducibility and limits

- Seven newly retrieved full JSON-RPC transport response objects, with derived complete parsed result objects and request parameters; separate raw finalized-status response.
- Instruction-level CSV/JSON: 17 rows including every outer instruction and one fee row per selected receipt. All native account deltas reconcile, including the multi-recipient transaction.
- Primary ledger file, exact U300 excerpt, fresh public source metadata and prior GLITCH v0.9 source retained.
- SHA256SUMS.json hashes all package files except itself. Hashes establish integrity, not source authenticity or legal custody certification.
- Run `python3 verify.py` after extraction, requiring only Python's standard library. It checks hashes, receipt/result correspondence, finality, instructions, roles, raw amounts, transaction-level account balances, fees and the primary Git blob match. It does not cryptographically authenticate RPC response objects or establish exchange ownership. `refetch.py` reproduces only the seven selected RPC calls and status query; it does not query new wallets.
- Web evidence consists of targeted observed excerpts/title metadata and exact URLs, not complete original HTML snapshots.
- Host-clock retrieval strings are preserved explicitly as host-clock values; they may differ from conversation date context. Blockchain UTC uses receipt blockTime, not that clock. The package creation date uses the supplied session date context, not a asserted trusted timestamp service.

GitHub source is read-only. Binance, other providers and public accounts were not contacted. Human identity, customer credit, common ownership and wrongdoing remain unproven.
