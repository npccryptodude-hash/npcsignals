# binance / visual evidence archive

> npcsignals · research prototype · 30 october 2026

**status: preliminary / third-party-reported transaction leads / independent chain verification pending**

This folder contains a static, locally renderable visual evidence prototype for the reported Binance security incident of 29 October 2026. It does not attribute the incident to any individual or organization. The transaction identifiers and address labels are research leads, not independently verified NPCsignals findings.

Open [`index.html`](./index.html) locally to view the timeline and transaction map. No wallet connection, RPC endpoint, API key, external JavaScript library or live blockchain request is used. The static display must **not** be described as a live monitor.

## Evidence policy

- `reported` — a named source identifies an event; direct chain verification is pending.
- `verified` — primary chain data has been independently inspected, and the verification record is retained.
- `supported` — evidence supports an inference but does not establish identity or control.
- `unresolved` — insufficient evidence to conclude.
- `rejected` — evidence contradicts the hypothesis.

The prototype intentionally marks **all listed transaction leads as `reported`**, not `verified`.

## Sources to independently inspect

1. Binance, *Security Incident Update*, 30 October 2026: https://www.binance.com/en-AU/support/announcement/detail/c5a8729a97ac486d963784d96c5642d7
2. TRM Labs, *North Korea Steals USD 6.36 Billion From Binance in the Largest Hack in History*, 29 October 2026: https://www.trmlabs.com/resources/blog/north-korea-steals-usd-6-36-billion-from-binance-in-the-largest-hack-in-history
3. Bitquery, *Binance Hack: $6.3B Drained on 9 Chains*, figures inspected 30 October 2026: https://bitquery.io/investigations/binance-hack
4. Ethereum transaction leads: https://etherscan.io/tx/0xad99264d5532ae0dd04b2004eebda05f25657e70dacb764f7ac8d4ccd051298b and https://etherscan.io/tx/0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3

## Publication controls

- Compare each transaction hash against a primary blockchain explorer or a trusted Ethereum JSON-RPC receipt and transaction response.
- Preserve `blockNumber`, `blockHash`, `transactionHash`, `from`, `to`, `type`, `status`, authorization list, decoded event logs, evidence retrieval timestamp and source URLs.
- Reconcile amounts by token decimals; do not treat token transfer events as additional native ETH value.
- Distinguish on-chain timestamp, discovery timestamp and publication timestamp.
- Do not sum issuer freezes and recoveries with gross theft or imply that frozen assets are returned to Binance.
- Do not infer common ownership solely from coordinated timing, exchange labels or address proximity.

## Relationship to earlier research

The `research/BINANCE_U300_*` evidence packages concern an earlier, separate Binance-labeled infrastructure lead related to ZYROX/GLITCH. They are **not evidence of a link** to the October 29 Binance incident.
