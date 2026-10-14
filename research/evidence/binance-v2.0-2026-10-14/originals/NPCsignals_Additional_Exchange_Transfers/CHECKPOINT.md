# NPCsignals — Additional exchange-inbound transfers, checkpoint v1.0

Date context: 2026-10-14 UTC. Existing GitHub exchange ledgers v0.1/v0.2, completed Binance U300 package checkpoint and independent-label supplement were read before this pass. No GitHub modifications or provider contact.

## Result

**Three additional successful finalized payments were independently reproduced from exact documented U300 wallet into the same Binance-attributed receiving infrastructure, all on September 30 before ZYROX's reported 17:18 UTC launch.** Their gross total is **450.032469956 SOL**. This satisfies a second distinct transfer objective and establishes repeated use of the existing address pair. It does **not** establish a second exchange, different source wallet, new independently controlled branch, specific customer credit or sale-proceeds provenance. No second independently attributed receiver was established in this bounded pass.

Completed October 14 signature `4m6gaPuwQnwN7KFSeCi3SzaqJzyj6JPzL5sMjq2c3gYuniYAqg3kZMPsseDdomzVJaVjZF3LPXYyHXAqeKKfSuYb` was excluded from fresh retrieval and candidate totals; its transaction analysis was not repeated.

Source for all three: `8zHcWujHhyJri3CRTcWUGmT5WSRdwW7xrns3WTTkPGvS`.

Receiver for all three: `5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9`.

| Evidence ID | UTC on 2026-09-30 | Slot | SOL | Instruction |
|---|---|---:|---:|---|
| SC001.I2 | 17:03:07 | 452026176 | 52.383204688 | outer:2 |
| SC002.I2 | 17:06:00 | 452026821 | 292.066250817 | outer:2 |
| SC003.I2 | 17:12:00 | 452028164 | 105.583014451 | outer:2 |

All CONFIRMED as System Program transfers, zero-based indices. Source is native transfer authority, sole signer and fee payer in each receipt. Fee is **9,000 lamports per transaction**, **27,000 lamports total**. SPL mint and historical token-account owner are N/A for these native SOL payments. No swap, bridge, staking, wrapping/unwrapping or account closure occurs in any of these three receipts. The other two outer instructions are Compute Budget instructions. RPC-reported transaction positions are retained but were not independently checked through full block retrieval.

Complete signatures:

- SC001: `3tPBHCeM4Y86RETWoAhmFKD1JjVs4GWduMxzsYwSstKktAKg3jovJbr54dUhaHfh1L8vxQJiGJ3BVgYhRs92vgWY`
- SC002: `4SxWP8XZRb3z1zg5dcTCsvGvMNtBm92zfibZ2KHySAVCZ34nTN9st6MrcaY7NnDfC8dsRsCMyiX6wMf4KoB9YsNm`
- SC003: `4xyFCL3f67ejRXTf3NZHgXScUVfXdCiWPsx9NNM1UWeNnmvMWcAFzGzYzGYapWFgHyFBD1aNmM9WDte7DbkpYnGe`

## Exact balance reconciliation

| ID | Source pre SOL | Source post SOL | Recipient delta SOL |
|---|---:|---:|---:|
| SC001 | 102.408154966 | 50.024941278 | +52.383204688 |
| SC002 | 297.148953208 | 5.082693391 | +292.066250817 |
| SC003 | 105.593019451 | 0.009996000 | +105.583014451 |

For each receipt, source decline equals transfer plus 0.000009000 SOL fee; receiver increase equals exact transfer. Full recipient pre/post integer balances and every account role are in balance-audit.json and the CSV. These are per-transaction balances. No continuity across intervening U300 transactions or total-wallet income is asserted.

## Exchange and network attribution

**SUPPORTED Binance infrastructure / hot wallet:** two independent publishers were checked again: Bitquery's own exact-address hot-wallet attribution and the exact-address Solscan page title Binance 2. Exact URLs, captured observations and limits are in attribution-sources.json. Direct Binance-published exact-address ownership remains UNRESOLVED from the prior check. Historical affiliation at September 30 is supported by published independent attribution and earlier historical context; no direct exchange confirmation at each timestamp is claimed.

**CONFIRMED documented network wallet:** current GitHub completed checkpoint identifies this exact address as ZYROX U300 and documents its GLITCH route connection. The complete preserved ZYROX primary file, exact U300 excerpt and current checkpoint snapshots are included. Primary Git blob SHA `08cf6b40c8aac00fb5d378ad1bc9b655bce62e55` is checked offline. U300's documented October 2 incoming from H85 is a network connection; no claim requires the earlier September 30 exchange payments to contain those later funds. The previously reproduced GLITCH route remains contextual linkage, not attribution of these pre-launch funds.

**UNRESOLVED:** customer credit versus internal sweep, whether the source is itself Binance-controlled, customer/account identity, common human control or token-sale provenance. These transfers run into the attributed receiving wallet, not out of it. Direction alone does not prove a credited customer deposit. They may supplement the existing provider inquiry with historical transaction identifiers; Binance internal records would be needed to classify them.

## Bounded discovery and negative findings

Two 100-receipt pre-launch samples were retrieved with finalized commitment, full parsed account data and provider-supported token-account coverage. Requests and complete original history response objects are preserved:

- 6hR7: September 24 16:44:17 through September 30 17:15:04 UTC.
- U300: September 30 17:02:21 through 17:17:55 UTC.

Both samples retained non-empty continuation cursors. They are not complete histories. Three candidates were separately re-fetched using standard getTransaction and separately checked with getSignatureStatuses; other discovery objects were requested finalized but not individually status-rechecked.

The movement extraction uses historical token-balance owner fields and initialization evidence, including closed accounts. It recovered 96 outgoing-or-internal movements. These are not all external payments: at least one large native funding movement belongs to a token account initialized for the sender and is explicitly classified INTERNAL_OWNER_MOVEMENT. Program/pool interactions remain unresolved where independent purpose is not established. No service, swap, bridge or internal movement was promoted to a CEX deposit based on amount or shape.

Exact recipient/account-owner screening against the 22 previously preserved CEX adapter lists produced no matching candidates. Those lists omit the independently attributed Binance receiver and are not exhaustive. The new positive result uses the two public independent sources instead. No exhaustive public-label search of all remaining sample recipients was performed. Thus this is a bounded null finding for an additional independently attributed receiver, not evidence that none exists.

## Strongest next actionable lead

Continue the **older, not exhausted 6hR7 history window before 2026-09-24 16:44:17 UTC**, using the exact preserved provider continuation token:

`2N9wXGZFCakFhot7P951285Fj2VpBftHNWKWWcs6jU99gQgcR3K9UZoJwC7gPpLDzmm1Z4mMg79ejQr4gouhwCEK`

Retrieve one further 100-receipt page with the same pre-launch cutoff, decode direct SOL/token transfers and historical owners, exclude wrapping/pools/internal flows, and test new direct recipients for at least two independent exchange attribution sources. This is an untested older window, not a restart of the already screened post-launch period. Cursor format differs from the cited extension documentation; use the actual returned cursor, preserve errors, and validate time/ordering.

An authorized Binance records inquiry can already add SC001–SC003 and ask for historical control of both addresses, classification as external customer deposit/internal sweep/other, and corresponding legally disclosable booking records. No inquiry was sent.

## Reproducibility and preservation

Run `python3 verify.py` after extraction. It checks file hashes; three fresh successful finalized receipt/status pairs; all 12 instruction/fee CSV rows; exact lamports, signer/fee payer roles, balances and gross total; all 200 discovery objects and cutoff; and exact U300 primary address. The script does not authenticate RPC responses cryptographically or prove exchange ownership. Discovery uses a nonstandard provider extension; independent candidate verification uses standard Solana receipt/status methods. Raw response envelopes, requests, complete derived receipt objects and selected historical-owner analysis are retained.

Hash integrity is not a trusted timestamp or certified chain of custody. Public-source evidence consists of targeted observed excerpts and title metadata rather than full original HTML snapshots. GitHub unchanged; customer identity, fraud and common private-key control unproven.
