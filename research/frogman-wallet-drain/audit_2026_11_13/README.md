# frogman / final account verification / 13 november 2026

## result and scope

35 distinct externally listed deposit transactions and 35 distinct hyperliquid accounts have been independently reconciled. this establishes account activity, not common human control or exclusive victim provenance. [technical report](TECHNICAL_REPORT.md) · [all 35 accounts](ACCOUNT_AUDIT.md) · [csv](accounts.csv) · [totals](summary.json) · [visual timeline and flow map](VISUAL_TIMELINE_AND_FLOW.md) · [remaining questions](LIMITATIONS.md).

## sources and reproduction

- arbitrum one json-rpc: https://arbitrum.gateway.tenderly.co ; chain id 42161 was checked. each successful receipt, transaction and containing block is preserved. usdc contract: `0xaf88d065e77c8cc2239327c5edb3a432268e5831`; recipient: `0x2df1c51e09aecf9cacb7bc98cb1742757f163df7`. logs are matched by contract, transfer topic, recipient and raw integer amount. transaction hash, block hash and block membership are checked separately.
- hyperliquid: `post https://api.hyperliquid.xyz/info`. the account is not assumed from a bridge label: each queried depositor must have a ledger credit matching the exact arbitrum hash and amount. all 35 match.
- requests used: `spotMeta`, `spotClearinghouseState`, `clearinghouseState`, `userFillsByTime`, `userNonFundingLedgerUpdates`, `openOrders`. official sdk source is preserved in `official_sdk_info.py.txt`; the [official info documentation](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint) and [ledger documentation](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals) explain formats and scope.
- metadata identifies xmr1 token 404, token id `0xbb2057659bd378d17e2e151bb04bdcaa`, spot market `@260`, quoted in usdc. another monero-related token is not silently treated as xmr1.
- request/response pairs in `raw/` preserve exact response bytes, request payload, source endpoint, retrieval utc and sha256. `accounts.csv` supplies per-account observation and history end times. snapshots are sequential observations, not a simultaneous consensus snapshot.
- historical requests start at zero and end at recorded request times. each account returned fewer than 500 fills and fewer than 500 ledger updates. the documentation gives a general 500-element/distinct-block pagination note; fills-specific documentation gives 2,000 per response and a 10,000 most-recent history cap. none of the 35 returned histories approaches even 500. separate post-13-october queries check the recent period directly. server retention/completeness cannot be independently guaranteed.
- deposits, internal spot transfers and spot buys are successive states of the same value. no additive loss total is made. fees are deducted according to the actual fee token. decimal arithmetic avoids binary floating-point rounding.

## running checks

`python build_audit.py` reads saved data only and checks all 35 exact credit matches, unique fill identifiers, block inclusion, token fees and all three account reconciliations: net xmr1 against spot state; internal usdc credit minus trade cost against spot usdc; deposit minus internal credit against perpetual account value. it fails on unexpected markets, extra deposits, other ledger types or a pagination threshold, rather than silently declaring completion.

`collect.py`, `collect_supplement.py` and `collect_current.py` are read-only collectors. do not rerun them over this checkpoint: copy them and the source ledger into a new dated directory first, or use a fresh checkout. their filenames identify this particular collection. no keys, signing, quotes, orders, swaps or transactions are submitted.

## classification

confirmed: directly reproduced transaction/api fact and exact arithmetic within scope. supported: a concrete interpretation with remaining verification limits. claimed: an external assertion. inferred: a reasoned association without deterministic linkage. unresolved: evidence does not settle the question. a confirmed deposit is not confirmed ownership, attack method or exclusive provenance.

## additional independently examined branches

[one extra hyperliquid account, the october 27 ethereum spend and new solana boundaries](ADDITIONAL_FINDINGS.md) · [offline new-edge verifier](verify_new_edges.py). the combined audited count is 36, comprising the external 35 plus one separately tracked account.
