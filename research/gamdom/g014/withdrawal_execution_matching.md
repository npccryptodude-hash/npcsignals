# Target matching and competing settlement explanations

| Route | NEAR execution | Exact withdrawal action receipt | Ethereum transfer |
| --- | --- | --- | --- |
| 1 | 3CucqT6YmivRFpNMtgsiuR43d2JXJcBuMLUYU9vHzjV6 | 79y1EMdKhP2AgryCjgjmJnMo4rTxs59mM78kWkmcSCsZ | 0x6b282435dc06107a499c8b8ef0ed83632a51d32738d81c143dc7e2d53542fd40 |
| 2 | 7dbo8A2xAkge8A6q139CsjcKd7rTHrK5U8aSyMxRMNiT | 96ktG3EwUqmz24aeen7ptcQLJfKrFdox8rsUF1kqHEwq | 0x3afe0536e5a7bc6f33da46ecef12c11a0591c9b13df90cb58f73c6839c99efaf |

Both mappings remain specific primary-protocol associations from G012/G013, corroborated by actual chain executions. No fresh copy of the same mutable status result is counted as new proof.

New EIP-1559 signature verification reconstructs the complete two typed signed envelopes. Both hashes match the requested Ethereum transactions and recover the same treasury public key. Both are chain-1, zero-native-value transactions directly to canonical DAI, with empty access lists and exactly 68-byte ERC-20 transfer calldata. Selector, B recipient and exact amount exhaust the calldata; each receipt has one canonical DAI Transfer event. No additional bridge identifier field is present.

The Ethereum signing messages contain destination transaction fields, not a declared source withdrawal reference. This does not disprove an independently signed off-chain instruction; none was recovered. A valid destination transaction signature cannot be repurposed as a source-referenced OMFT payout signature.

| Alternative | Bounded result |
| --- | --- |
| Multiple Ethereum recipients batched in either selected transfer | Excluded within each selected transaction's fully decoded transfer input and one Transfer event. |
| Multiple NEAR withdrawals economically pooled into one payment to B | Not excluded. One on-chain transfer does not prove one source liability. |
| Netting across independent operations | Not excluded. No treasury settlement book or authenticated operation record obtained. |
| Another NEAR withdrawal to the same recipient | Not excluded by exhaustive source-request coverage. No broad withdrawal census was performed. |
| Liquidity-provider/treasury payment rather than direct verification-contract redemption | Consistent with observed empty-code sender and direct token transfer; precise contractual/economic role remains unproved. |

## Independence of protocol mappings

1Click and OMFT withdrawal_status are distinct primary interfaces, not demonstrated independent data provenance. Their agreement is preserved as corroboration with unknown backend dependency. The examined historical SDK package uses an ordinary JSON-RPC wrapper for withdrawal_status and a response schema with source/destination hashes and status fields. It exposes no signature, attestation or public-key field in that version's typed response. The client is not the service implementation; undocumented extensions or separate archives cannot be ruled out.

The public repository/package checks did not reveal an actual authenticated payout instruction for either target. No third API repeating the same mapping was sought. An API lookup, repository Git commit, package integrity hash or signature on the Ethereum transaction does not authenticate the economic correspondence by itself.
