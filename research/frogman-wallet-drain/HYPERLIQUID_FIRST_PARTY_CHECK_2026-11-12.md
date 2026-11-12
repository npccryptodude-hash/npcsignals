# frogman / hyperliquid first-party reconciliation — 12 november 2026

**status: blocked — live first-party API data not obtained.**

## what was attempted

A direct HTTPS POST to `https://api.hyperliquid.xyz/info` using the documented `spotClearinghouseState` query and a listed Arbitrum depositor address was attempted on 12 november 2026. The execution environment could not resolve the API host (DNS `NameResolutionError`). **No Hyperliquid balance, trade or withdrawal response was returned.** Therefore this investigation must not claim current XMR1 holdings or zero redemption in november.

The Onchain Files #014 page is accessible and states 35 Hyperliquid accounts, 2,029,874 USDC deposits, 3,586.8 XMR1 and no redemption **at its last check on 13 october 2026**. These are third-party historical assertions, not independently validated current balances. Source: https://www.onchainfiles.io/files/014-frogman-token2049/

## evidence separation

| question | available evidence | finding |
|---|---|---|
| did arbitrum usdc reach the labelled hyperliquid deposit bridge? | 35 explorer transaction links, 20 previously field-transcribed and five more later transcribed | historical transfer evidence available; comprehensive event audit still needed |
| did hyperliquid credit each specific trading account? | no first-party response in this check | **not verified** |
| were the deposits spent on xmr1? | third-party report and earlier npcsignals sample of seven accounts | **not independently reconciled for all 35** |
| what is the xmr1 balance on 12 november? | no first-party response | **unknown** |
| was xmr1 redeemed for native monero after 13 october? | no current redemption ledger | **unknown** |
| are all 35 accounts under one human controller? | no identity evidence | **unknown** |

## reproducible first-party procedure

1. build the complete 35-address list from Arbitrum transaction receipt `from` fields, **not** from abbreviated display labels.
2. query `POST https://api.hyperliquid.xyz/info` for each address with `{"type":"spotClearinghouseState","user":"0x..."}`. Record the raw JSON and retrieval UTC time.
3. separately query `{"type":"userNonFundingLedgerUpdates","user":"0x...","startTime":...}`, `{"type":"userFillsByTime","user":"0x...","startTime":...}` (paginated if necessary), and the documented historical ledger/withdrawal endpoints. Verify actual endpoint availability and response schema before automation.
4. identify the XMR1 spot token by its current Hyperliquid metadata, **not** by guessing a token index. Record the exact token ID and asset identifier used for fill filtering.
5. for each address, reconcile Arbitrum deposit transaction → Hyperliquid credit → XMR1 fills → spot balances → withdrawal/redemption evidence. Store transaction IDs, API response hashes, UTC timestamps and source URLs.
6. retain separate labels: `confirmed on-chain`, `confirmed first-party hyperliquid`, `reported externally`, `inferred`, `unknown`. Never treat an absence of API data as a zero balance.
7. compare the 35-address set with npcsignals' existing seven account records; do not double-count overlapping deposits or XMR1 quantities.

## correction to previous progress messaging

**35/35 transaction hashes recovered does not equal 35/35 Hyperliquid account histories verified.** A complete current balance or redemption conclusion is unavailable as of this check. This document is a recorded negative result, not a completed Hyperliquid audit.

**do not publish new November movement or no-movement claims based solely on the October monitor.**
