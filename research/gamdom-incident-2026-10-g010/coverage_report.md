# Coverage and provenance

## Frozen research review

G005 assessments/ledger identify A/B Polygon transfers and bridge arrivals, but no independently established unauthorized status. G006 ledgers, route/accounting records, hypothesis test and verification/coverage reports already contain B's earlier Ethereum arrivals and BUSD path. G008's funding/authorization verification and coverage distinguish raw recovered signatures from explorer transcriptions. G009 provides a bounded D balance reconstruction and repeated D→C history, not incident-origin proof. Those findings are imported rather than reinvestigated. All 138 frozen tracked files are checked byte-for-byte against the starting commit.

## New Ethereum collection

Endpoint: https://mainnet.gateway.tenderly.co. Chain ID 1. E1/B all-contract Transfer topic queries cover blocks 26184450–26185250 inclusively: October 13 15:24:47–18:05:35 UTC. This envelope contains the requested 15:30–18:00 interval. Closing state is at 18:05:35, not exactly 18:00. E1 returns 34 events (7 outgoing, 27 incoming), including seven swap-output credits. Receipt/transaction/header data are saved for every distinct E1 token event and ten explorer-listed normal transactions. Two of those normal transactions failed. One failed lookalike-address dust attempt is not a true A edge.

E1 prior-topic queries cover blocks 26100000–26184449, October 1 20:56:59–October 13 15:24:35, returning zero events. This does not cover lifetime activity, the first 20 hours of October 1, native/internal history, NFTs, nonstandard token events, earlier account delegation, or other chains. Its zero tracked opening balances and nonce are direct historical calls, not inferred from an incomplete event sum.

A/S1/S2 baseline queries cover blocks 26177200–26184449, October 12 15:10:35–October 13 15:24:35. These have 0/1288/1 returned all-contract Transfer events respectively. Only canonical USDT/USDC/DAI/USD1 are used in reported token accounting; arbitrary contracts can emit misleading events. S1's filtered canonical outflow comparison is event-level, not full receipt verification. No September baseline or lifetime completeness is claimed.

The f70da978 and 2cff890 service-source windows yielded 1853 and 1049 all-contract event records respectively. These are discovery context only, not all independently verified transfers or victim-wallet inventories. No aggregate theft value is calculated from them.

State calls cover tracked balances and account nonces at 26184449, 26184625 and 26185250; E1/B native states at opening/closing are preserved. The USD1 contract's historical symbol and decimals are independently called. Acquisition record names `state_*_USDE_*` and `token_USDS_*` are provisional labels retained for fidelity; their contract is 0x8d0d000ee44948fc98c9b98a4fa4921476f08b0d, whose returned symbol is USD1 and decimals 18. Published accounting uses USD1, not either provisional alias.

## BNB / bridge coverage

https://bsc-dataseed.binance.org returns chain ID 56 and both selected source receipts, transaction objects and headers. It rejects the 25001-block log request and a reduced 5000-block request with -32005 limit exceeded. The smaller failure is not an empty event result. https://bsc-rpc.publicnode.com returns HTTP 403 for chain ID. Routescan's BNB indexed query returns chain not supported. The browser BscScan history page remains on a Cloudflare security/human-verification screen. These attempts do not establish absence of earlier B inflows. Two deposits are verified, but B's preceding BNB funding is not reconstructed.

Relay requests/v2 maps two known Ethereum hashes to the source deposits. Three other lookups return HTTP 429; one returns no matched requests. Empty service-index results are not proof that no bridge or transaction exists. API metadata is corroborating discovery evidence, not substituted for source receipts or initiator identities. The source/destination 32-byte match is independently reproducible from preserved chain representations.

## Evidence depth

Original parsed RPC request/response objects and service HTTP response bodies are compressed losslessly into rpc_archive.json.gz. This is not a byte-for-byte HTTP wire capture. Each canonicalized record is SHA-256 registered. Both HTTP errors and JSON-RPC errors are retained. All contracts, topics, raw amounts, log indices, transaction indices and headers used by the ledger are preserved.

Verification checks returned hash/index/header consistency and exact state/event arithmetic. It does not reconstruct state roots, obtain Merkle inclusion proofs, run an independent consensus node or recover new transaction signatures. One Ethereum provider supports the state/log accounting. The earliest candidate is separately corroborated in the Etherscan browser. Provider independence behind the explorer is not claimed.

Solana, TRON, XRP, remaining BNB originating outflows, Bitcoin, Hyperliquid and THORChain are NOT ASSESSED in G010. Their claimed incident-origin hashes remain unlocated. Current balances and current USD prices are never used as historical states or prices.
