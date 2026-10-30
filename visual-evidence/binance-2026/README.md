# binance / visual evidence archive

> npcsignals · research prototype · 30 october 2026

**status: limited independent explorer-data confirmation / broader incident and attribution unresolved**

This folder contains a static, locally renderable visual evidence prototype for the reported Binance security incident of 29 October 2026. It does not attribute the incident to any individual or organization. The three Ethereum transactions have now been checked against Blockscout API responses; the scope of that verification is precisely recorded in `evidence-checkpoint.json`. Broader asset flows, exchange labels, signing-system compromise and human attribution are not independently established.

Open [`index.html`](./index.html) locally to view the timeline and transaction map. No wallet connection, RPC endpoint, API key, external JavaScript library or live blockchain request is used. The static display must **not** be described as a live monitor.

## Evidence policy

- `reported` — a named source identifies an event; direct chain verification is pending.
- `verified` — primary chain data has been independently inspected, and the verification record is retained.
- `supported` — evidence supports an inference but does not establish identity or control.
- `unresolved` — insufficient evidence to conclude.
- `rejected` — evidence contradicts the hypothesis.

Only the Ethereum transaction facts explicitly checked in the checkpoint qualify for `verified`. `b004-token-ledger.json` contains all 63 token transfer events returned across the two pages of Blockscout's API: 63 distinct contracts, one sender and one receiver. Address roles, motives and cross-chain claims remain `reported` or `unresolved`.

## Sources to independently inspect

1. Binance, *Security Incident Update*, 30 October 2026: https://www.binance.com/en-AU/support/announcement/detail/c5a8729a97ac486d963784d96c5642d7
2. TRM Labs, *North Korea Steals USD 6.36 Billion From Binance in the Largest Hack in History*, 29 October 2026: https://www.trmlabs.com/resources/blog/north-korea-steals-usd-6-36-billion-from-binance-in-the-largest-hack-in-history
3. Bitquery, *Binance Hack: $6.3B Drained on 9 Chains*, figures inspected 30 October 2026: https://bitquery.io/investigations/binance-hack
4. Ethereum transaction leads: https://etherscan.io/tx/0xad99264d5532ae0dd04b2004eebda05f25657e70dacb764f7ac8d4ccd051298b and https://etherscan.io/tx/0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3

## Publication controls

- Compare each transaction hash against a primary blockchain explorer or a trusted Ethereum JSON-RPC receipt and transaction response.
- Preserve `blockNumber`, `blockHash`, `transactionHash`, `from`, `to`, `type`, `status`, authorization list, decoded event logs, evidence retrieval timestamp and source URLs.
- Reconcile amounts by token decimals; do not treat token transfer events as additional native ETH value.
- Recheck token contract identifiers, log indices and decimals against an independent chain node before publication as fully independently verified Ethereum facts. The current register is **explorer-data verified**, not multi-provider verified.
- Distinguish on-chain timestamp, discovery timestamp and publication timestamp.
- Do not sum issuer freezes and recoveries with gross theft or imply that frozen assets are returned to Binance.
- Do not infer common ownership solely from coordinated timing, exchange labels or address proximity.
- **Do not classify a token by symbol alone.** A first-page inspection of the receiving wallet's outgoing events found a `USDT`-labelled token under contract `0x11D0647b8Fee5662eAb6f0257404Ee57C7261cAc`, which differs from the canonical Ethereum USDT contract. See `receiver-label-collision.json`. This is an observed contract mismatch, not an attribution or proof of malicious intent.
- The first completed B006 outgoing-ERC-20 snapshot spans 14 pages / 663 events and records two positive canonical-USDT outflows of 500m and 200m USDT. See `b006-receiver-outgoing-summary.json`. Other-chain transfers and native ETH remain separate investigations; this does not constitute a complete stolen-asset reconciliation.
- The B006 visual branches show only the two direct recipients of those canonical-USDT transfer events. They do not show subsequent destinations, beneficiary identities or a recovered-asset balance.
- `b007-second-hop-usdt-ledger.json` traces the outgoing canonical-USDT events from each of the two B006 recipients, with 20 events (19 positive, one zero) to 15 distinct positive-value destination addresses. Branch A sends a total of 500m USDT; branch B sends 200m USDT. These values reconcile exactly to the two first-hop transfers, without adding subsequent transfers to the initial theft total. The Blockscout response SHA-256 hashes and full transaction hashes are included in the ledger. This checkpoint remains **single-provider explorer-data verification**; no ultimate recipient, beneficial ownership, exchange deposit or fund recovery has been established.
- `b008-third-hop-usdt-ledger.json` follows only the two largest B007 recipients (190m and 175m USDT). Their four outgoing canonical-USDT events reconcile to 365m USDT across three recipient addresses (130m + 50m + 10m + 175m). Individual transaction responses returned `status: ok`; their full hashes and the response SHA-256 values are retained. Two transactions have a smart-contract outer `to` that differs from the recipient in the USDT transfer log. This distinction is deliberate. The remaining B007 addresses and all subsequent destinations are not yet traced here.
- `b009-large-recipient-continuation.json` checks the subsequent 130m and 175m recipients. The former sent its 130m USDT onward through 18 positive transfer events; its observed 0.0002 USDT balance matches later small inbound transfers. The latter sent only 127.67248 USDT outward, while Blockscout's token-balance endpoint reported 174,999,872.327620 USDT including a 0.0001 USDT later inbound transfer. **This is not a verified token freeze.** The record preserves source response SHA-256 hashes and precise, non-double-counted amounts.
- `b010-blacklist-and-80m.json` records a direct `isBlackListed(address)` read against canonical Ethereum USDT for the 175m recipient. Two distinct public Ethereum mainnet RPC providers returned `false` at their respective `latest` block heights. This narrows the claim to **not blacklisted at those observed heads**; historical freeze status and reasons for balance retention are unresolved. The same checkpoint records all 20 positive canonical-USDT transfers from the 80m sub-branch (80m total, 11 destinations). It is a subset of the previous flows, not an additional amount.
- `b011-80m-recipient-infrastructure.json` classifies those 11 direct recipients through individual Blockscout address metadata. Ten have explorer-reported verified contract code and received 50m USDT (35.31m to UniswapV3Pool, 13.41m to PoolManager and 1.28m to Uniswap V2-style contracts). One unlabelled address without reported contract code received 30m USDT. **Do not infer that transfers into pool contracts were successfully swapped, bridged or cashed out** without inspecting the full transaction execution, output token logs and subsequent balances. No-code address is not a verified identity.
- `b012-30m-and-pool-receipts.json` follows the non-contract-code recipient's canonical 30m USDT to one further address. The next address still showed 30m canonical USDT in a balance snapshot, without positive outgoing canonical-USDT events. A separate token called USDT under a different contract is excluded. The two pool-related transactions were fully paginated (64 and 68 token events); no token-log transfer directly back to the initiating 80m sender was found. Swap output routing remains unresolved.

## Draft editorial package (not published)

`medium-draft.md` and `x-draft.md` are lower-case, source-limited drafts for a future short Medium research note and an X post. Hold both until independent receipt checks and a public archive URL are approved. The draft X post intentionally contains a placeholder link; it is not ready to publish.

## Relationship to earlier research

The `research/BINANCE_U300_*` evidence packages concern an earlier, separate Binance-labeled infrastructure lead related to ZYROX/GLITCH. They are **not evidence of a link** to the October 29 Binance incident.
