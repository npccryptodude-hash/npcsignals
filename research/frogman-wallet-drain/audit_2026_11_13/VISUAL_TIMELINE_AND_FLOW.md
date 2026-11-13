# frogman / visual timeline and evidence flow

## chronological record

```mermaid
timeline
 title frogman / utc evidence chronology
 6 oct 20:14:54 : earliest reproduced suspicious solana outflow
 6 oct 20:18–20:35 : token disposals and conversion
 6 oct 20:36–21:00 : ten privacy cash deposits / 13,240.973780900 sol
 6 oct 23:40 : reproduced base to ethereum across route
 7 oct 01:13–01:36 : near intents and chainflip settlements / separate branches
 7 oct 01:45–03:37 : 35 arbitrum usdc deposits and matched hyperliquid credits
 7 oct 03:37:25 : last activity returned across the 35 accounts
 10 oct : original npcsignals research checkpoint
 13 oct : external monitor's stated last check
 27 oct : formerly held eth spent / new mayan order
 13 nov : 35-account receipt, credit, fill and balance reconciliation
```

## money-flow map

```mermaid
flowchart TD
 A["reported affected wallets"] -->|"selected reproduced transactions"| B["solana receiving wallet"]
 A -->|"selected evm routes; provenance limits"| C["evm routing and mixed balances"]
 B -->|"10 deposits / 13,240.973780900 sol"| D["privacy cash"]
 D -. "inferred by external source; unproven withdrawal linkage" .-> E["candidate withdrawal wallets"]
 E -. "25 new route-api checks blocked" .-> F["arbitrum rows 11–35 / 1,284,323.292841 usdc"]
 C -->|"historical matched relay / mayan / across routes"| G["arbitrum rows 01–10 / 745,551.169439 usdc"]
 F -->|"exact receipt and credit match"| H["35 hyperliquid accounts / 2,029,874.462280 usdc"]
 G -->|"exact receipt and credit match"| H
 H -->|"537 buys / fees deducted"| I["3,586.797483 xmr1 / reconciled november balances"]
 H --> J["163.826580 usdc residual / spot and perpetual accounts"]
 I -. "no native monero receipt established" .-> K["redemption / beneficiary unresolved"]
 C --> L["separate chainflip and near intents settlements"]
 C --> M["forwarders / mixed accounts / dated holding boundaries"]
```

solid edges refer to reproduced evidence within the attached scope. dotted edges are unresolved or inferred. the diagram does not establish an uninterrupted path from every victim asset to every hyperliquid balance. row group labels preserve the external grouping without upgrading private-pool attribution. successive protocol inputs, settlements, credits and purchases must not be added as new losses.

## inspect an arrow

- privacy cash entry: [original deposits](../frogman_research_v0_1/privacy_cash_deposits.csv).
- evm routes: [v0.2 evidence](../v0.2/), including route-specific `cross_chain_edges.json` and verifiers.
- all arbitrum → hyperliquid arrows: [35-account audit](ACCOUNT_AUDIT.md), [receipts](receipts.json), exact receipt/transaction/block/ledger files in [raw](raw/).
- hyperliquid → xmr1: [all 537 fills](fills.json), [metadata](raw/spotMeta.json), [account reconciliation](accounts.json).
- residual balances and no returned external-transfer entries: [ledger](ledger.json), individual spot/perpetual states and query metadata in [raw](raw/).

## additional routes / do not merge with the external 35

```mermaid
flowchart TD
 A["near intents destination / verified historical settlement"] -->|"0.473 sol"| B["relay source transaction"]
 B -->|"first-party exact hash pair and matching field"| C["55.569140 usdc / arbitrum"]
 C -->|"exact receipt and account credit"| D["separate account / 0.089937 net xmr1"]
 E["formerly held 4 eth"] -->|"27 oct / confirmed debit"| F["3.999998840651572 eth forwarded"]
 F -->|"3.998918422844160119 eth / confirmed order"| G["mayan order / expected solana recipient"]
 G -. "supported; independent order-state match pending" .-> H["92.375240889 sol observed"]
 H -->|"confirmed local transfer"| I["three-source consolidation / mixed-funding boundary"]
```

[additional route evidence and exact timestamps](ADDITIONAL_FINDINGS.md). the last arrow does not identify a final beneficiary or allocate later spending from the mixed balance.
