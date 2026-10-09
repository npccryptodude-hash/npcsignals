# Robinhood zero-value outer routes: exact native prefunding

Public parent: `b10fd8705cebdb587b6242d828b2840ada2b5a9a`. Additive F0523–F0538.

Seven newly reproduced native transactions, sent by **0x427c4b37de0714821b09c4fc655a713abbcfba83**, prefund contract **0x794dbdbdbfd3f8a3b887f4513bf5ff29edd04a94**. They total **148.875761888326838512 ETH**. Each native transfer has a `PrefundingStored` witness that exactly matches the `PrefundedFunding` witness and Gateway `StepExecuted` step ID in one previously verified zero-value origin transaction.

| Source prefunding transaction | Existing origin | Source nonce | Native ETH |
|---|---|---:|---:|
| 0xc058dff9d6b508df0224303d3d9811f6bc574b77be957c14f84528ffdf03b636 | F0451 | 18 | 18.875767473824278512 |
| 0x36416ac589c7feaba4322aa88ef4753899dc3fcca4c4a7a40a6e6f96748fa49a | F0453 | 19 | 32.50000979552 |
| 0x9d055043a354327c6e4ac9ebc0ec5c6c2e742de3f5f8701de5c931e32f1b9f24 | F0455 | 20 | 24.375007114569688 |
| 0xd16dea86c61c4b12f9d54492fa747ce51992a93204ae0ecf441625ab47ee67a7 | F0457 | 21 | 18.281255103833906 |
| 0x1000e899686a8075da4f977b86152bafb512d8e9c69b3c5726ed62e0acdd55b2 | F0459 | 22 | 13.7109410967039895 |
| 0xbe0531164eed2ef3ffd1889df8ec2dc677eb0cb6ea874210884135f07ee8cecb | F0461 | 23 | 20.56641118377331225 |
| 0x8c8ecc3f37ae37eaa77786015ab2a4ae255def1c39126048d3e1121d99577c48 | F0463 | 24 | 20.56637012010166425 |

The stored native amount equals the actual attached value, native release amount, intermediate wrapped-native mint and Across deposit amount. Release recipient **0xa5166c3e69a933ee547ad908c9f1474f8f61901a** is the path executor encoded in the Gateway calldata. The offline verifier reconstructs each path ID from chain ID, salt, executor and message hash, then verifies the Merkle proof against the step root. This is transaction-specific protocol correspondence, not timing or amount matching alone.

Funding is **PARTIAL / RE-ESTABLISHED** for these exact last-hop sources. Complete affected-wallet-to-native-balance provenance remains **UNRESOLVED**. A native prefund comes from the pooled balance of 0x427c; neither equal amounts nor protocol usage identifies which earlier token sales funded it. No CLEAN full-case funding claim is made.

## Distinct roles

* Native funder: 0x427c…bA83, which also sent the eight direct bridge deposits. Nonces 10–24 establish a continuous sender-account sequence across the two mechanics, not the identity of a person or business.
* Prefunding adapter: 0x794d…4a94, with per-witness native-funding events.
* Outer submitter/gas payer: 0x07ae…0e67. It attaches zero native value and is emitted as the Gateway submitter. It is not relabeled as the native owner/funder.
* Gateway: 0x998d…e707; executor: 0xa516…901a; Across pool: 0xd29c…7978. These are protocol roles, not common ownership or custody findings.

Ethereum verified contract source identifies the Gateway/PrefundedAdapter family and Across V5 mechanics. Robinhood current bytecode and implementation observations are dated contextual evidence; an identically addressed Ethereum contract alone is not a historical Robinhood deployment audit. The source family association remains SUPPORTED, while actual case event linkage and independently reproduced Merkle membership are CONFIRMED. The executor Ethereum metadata lookup failed and is not treated as source verification.

Standalone user-signature validation, native-balance history, fee-funder identification, operator names, custody relationships and beneficiaries remain unresolved. No common fee funder is established. No new exchange boundary or loss is asserted. Privacy Cash remains separate. Next block: Ethereum callback/native-credit and pooled post-bridge disposal reconstruction. No article.
