# NPCsignals v0.2 continuation — 8 October 2026

English research checkpoint, not an article. Frozen v0.1 and completed Solana reconstruction are unchanged.

## Precisely saved before this continuation

Inspected GitHub main: `8543f9e964089612c0a1a3f52b26709e12f6f95b`, tree `4e7319f46386925519a7c202f9c91b4d52ad1997`. Its parent research checkpoint is `6d681dd5ae57d6629c3f0582a606512035f72020`. The head adds retrieval-integrity verification, not new fund-flow findings.

The saved package contains F0001–F0206, the unchanged frozen Solana record, 15 reproduced Ethereum outgoing transactions, six Relay deposit/fill pairs, three Robinhood source token transfers and six Arbitrum USDC consolidation transfers. Relay's exact reproduced exchange is 212.499 ETH to 561850.214994 USDC, not exactly 212.5 ETH. All saved classifications and limitations remain in force.

The unresolved Relay-related next node is Arbitrum address `0x2df1c51e09aecf9cacb7bc98cb1742757f163df7`. This continuation queries its USDC inflows/outflows from block 512422000 to a recorded latest block, with receipt/block reproduction for returned events. This window does not establish its complete lifetime history or history of other tokens. Other funding must be considered before extending exclusive provenance.

## Reproduction

Run `python collect_collector.py` from this directory. Successful saved responses are reused; raw request metadata and response bytes are retained in `raw/`. JSON-RPC errors and transport failures are evidence of query limitations, not evidence of absent transactions. Transaction event validation and ledger generation will be saved separately after collection completes. No ledger ID is allocated by collection alone; the next available ID is F0207.

No matched Privacy Cash withdrawal, identity, compromise method, recovery or ultimate beneficiary is newly established here. A transaction path is not proof of identity. A fund-flow reconstruction is not proof of compromise method.

## Reproduced collector boundary

CONFIRMED: the receiving address has deployed contract code at block 512881298. Its USDC balance at that block (2026-10-08T12:31:48Z) is 393259622.336699. This is a pooled contract balance, not an incident balance or a recovery figure. Contract identity and operator are NOT ESTABLISHED by these queries.

CONFIRMED: an additional 51 USDC inflow at 2026-10-07T01:51:25Z, transaction `0x4919141b0ae81c4abfc4ac8fd0674184086a647432a920cc24f7249e686984ce`, is recorded as F0207. A 150395.42 USDC outflow at 2026-10-07T01:53:56Z to `0x023a3d058020fb76cca98f01b3c48c8938a22355`, transaction `0x5d0803e0bfa074fad49f000d7a8e387c6e20ec2ebbabcd336b412648b71db86a`, is F0208. Both have successful receipts, matching token events, matching block hashes and block inclusion. They are context events, not additional incident losses or a matched payout of incident funds.

Scoped RPC log reproduction returned 4264 positive USDC events over blocks 512422000–512881298: 2098 inflows totaling 25935939.636907 and 2166 outflows totaling 32445986.601148. Six previously reproduced case transfers account for 561850.214994 of the inflows; the other observed inflows total 25374089.421913. Full receipt reproduction is limited to those six saved case events and the two new context events; the aggregate log observation is not represented as thousands of individually receipt-verified ledger rows.

Provenance is **mixed** at this contract. The specific association between a case deposit and any later outflow is NOT ESTABLISHED. No FIFO, timing-only, equal-amount or proportional allocation is applied. The opening balance query failed with historical state unavailable. Complete lifetime, other-token funding, contract permissions, exchange identity and ultimate beneficiary remain UNRESOLVED.

`verify_collector.py` reproduces F0207–F0208 and scoped totals; `collector_summary.json` and `wallet_graph_update.json` preserve the boundary. `evidence_index.json` and `SHA256SUMS.txt` inventory this supplement only. Previously saved v0.2 indexes remain historical checkpoint inventories, not an assertion that later additions are absent. Partial receipt collection was stopped after the high-traffic scope became evident; its already retrieved records are retained but not promoted into new findings.
