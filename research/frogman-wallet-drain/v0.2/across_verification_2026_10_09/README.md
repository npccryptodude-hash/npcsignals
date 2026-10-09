# Across Base-to-Ethereum verification — 9 October 2026

Starting verified public commit: 6fad8815fdab6b2cc7d7e9e2c58d3eacf503c574. Frozen v0.1 and F0001–F0431 unchanged. No article. New records F0432–F0434; next F0435.

## CONFIRMED transaction-specific bridge edge

Base origin: `0x2310d627c3c369a73b480bd1bb6bdcffd26615ba84ce02a0f36858722890d366`.
Ethereum fill: `0x5d6b414f8b7ecdcee5ffdb378ceb3de228cec732037437d759900ed7b34d1b1a`.

Official Base RPC independently reproduces chain 8453, the transaction, successful receipt and block. dRPC reproduces an identical transaction and receipt result. Exact block number, UTC time, amounts and addresses are preserved in F0433. Both transactions are successful. Native origin ETH value equals the deposit amount; the origin receipt includes a matching WETH wrapping Deposit event. Origin contract `0x09aea4b2242abc8bb4bb78d537a67a245a7bec64` emits FundsDeposited; Ethereum contract `0x5c7bcd6e7de5423a257d81b442095a1a6ced35c5` emits FilledRelay. These signatures are verified against the preserved first-party Across interface using Keccak, including a known empty-input test vector.

Deposit ID 6301830 links the two events alongside matching origin/destination chain IDs, depositor, recipient, input/output token addresses, input/output amounts, exclusive relayer, fill deadline, exclusivity deadline and empty-message/zero-message-hash fields. The saved Across API hint independently names the same pair. The link rests on protocol-specific correspondence, not timing or similar amounts.

Origin amount: **43.625009525741763214 ETH**, wrapped at the origin pool.
Ethereum amount: **43.614308988719623177**, transferred as WETH to the pool and unwrapped into the existing F0129 native ETH credit.
Exact input/output difference: **0.010700537022140037**. This difference is not a reproduced decomposition of bridge, relayer or LP fees. Receipt execution/L1 fee components are recorded separately. Relayer and exclusive-relayer field: `0xfd03abcadaf3f930fa4e37eb2f6ea3a44a41b7f0`; repayment chain 8453; fill type 0 (FastFill). No repayment/refund transaction independently reproduced.

Origin sender and destination recipient are both `0x427c4b37de0714821b09c4fc655a713abbcfba83`. This is a reproduced address-level relationship, not a person or exchange/custody attribution. No new service owner, human identity, final beneficiary or compromise evidence. Origin-side prior funding and Robinhood linkage remain unresolved. The relationship of this credit to the existing Relay path must follow preserved transaction edges; no new link to those six routes is asserted here.

## Collection limitations

Initial ad hoc requests returned HTTP 403. Recorded follow-up queries subsequently succeeded on official Base RPC, Publicnode transaction lookup, and dRPC. Failed Publicnode receipt and Blockscout requests remain preserved as failures. A failed request never substitutes for absence of a transaction. Origin block membership and timestamp were separately checked. No block-header consensus proof or signer recovery performed.

## Ledger and reconstruction

F0432 is the destination protocol event. F0433 is the origin deposit. F0434 is the matched cross-chain edge. They describe one route and must not be summed as distinct losses. F0129 and all existing records are unchanged; the bridge association is additive. The combined timeline and separate edge file update the reconstruction without rewriting frozen historical files. The Privacy Cash branch remains separate; XMR1 redemption and beneficiary remain unresolved.

Run verify_across.py offline to reproduce parameter comparisons. collect_origin.py records requests and exact response bytes, reuses saved files and performs no fund-moving operation. Next unresolved branch: Robinhood-to-Ethereum.

Origin block: 52270327; timestamp: 2026-10-06T23:40:01+00:00.
