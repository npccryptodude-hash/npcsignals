# frogman / additional findings beyond the external 35-account set

## additional hyperliquid account / separate scope

an independently captured near intents destination forwarded 0.473 sol to `7iGKnB9CSQLWsVX4V9Q9R61P3PFgJnLdyvPBvQutr5Gm`. a later successful solana transaction, `2v4LbSYLeXydAn11Q5NrYkk96VYA3WaLTGuP1fsHqEDDVFkVftuDM9zZLNz5aUU5WcGUHnX8Z4aQ9dqQkga4GZhN`, transferred exactly 0.473 sol through the observed deposit program.

the first-party relay response links that exact source signature to arbitrum output transaction [0x430a…f9eb](https://arbiscan.io/tx/0x430a6d5eb90fcd7cda103bd502fd3b82953749b98317402e3a5945571b05f9eb). both chains' actual transaction records are preserved. the source program event's final 32-byte identifier matches the appended destination calldata field exactly: `0xa4a2a75e06b787f17b76b82aa20e07e4f7457a0b2eee4f3e11343dc97e1b3fc5`. the arbitrum receipt transfers **55.569140 usdc** to `0xa8f219e59033fe2593151d951a142c1f958fd949`. standalone source-program/consensus decoding was not performed; the exact first-party in/out pair and matching on-chain field are documented rather than inferring the route from amount alone.

this address is absent from the external 35-account set. its separate bridge deposit [0xcf22…d9d3](https://arbiscan.io/tx/0xcf22021a2e1c38c911ad92e5642e40de0a86c99c0730f94a591f9b5f72bed9d3) matches its hyperliquid ledger credit exactly. one buy fill records 0.09 xmr1 gross and 0.000063 xmr1 fee, giving **0.089937 xmr1**, equal to its queried spot balance. remaining spot usdc is 4.602 and perpetual account value is 0.00914; execution cost 50.958 plus those residuals equals 55.56914 usdc.

the separate spot observation is dated **2026-11-13t08:36:23.123692+00:00**. no additional deposits or transfers appear in its returned two-entry non-funding ledger. this is a bounded current account check, not a lifetime-history or human-ownership proof.

| coverage | unique accounts | reproduced usdc credits | observed net xmr1 |
|---|---:|---:|---:|
| external published inventory | 35 | 2,029,874.462280 | 3,586.797483 |
| separate new account | 1 | 55.569140 | 0.089937 |
| combined audited accounts / different query times | 36 | 2,029,930.031420 | 3,586.887420 |

these are distinct account credits, not a new victim-loss valuation. the extra account does not reconcile the separate public 41-account claim without its full address list. its original upstream mixed-balance qualifications remain in force. [machine-readable results](new_edges_summary.json) · [offline checker](verify_new_edges.py).

## 27 october / the old 4-eth holding was spent

at **2026-10-27 05:46:47 utc**, address `0x4521ef4df51a7689d4db5d8fc598685cb226ff58` sent **3.999998840651572 eth** to `0xbbae94f15c551920f45ad9a099e2a6b821822e3e`, transaction [0x40fd…cc2f](https://etherscan.io/tx/0x40fdd541a98a97bb30da88a4370b78a7bd370467cfcfe6fc718ddec93dcbcc2f). successful receipt, block inclusion and historical native balances reproduce the debit. the source held exactly 4 eth immediately before that block and 0.000000224992677 eth afterward; gas accounts for the remaining difference.

the current returned source balance is **3.999999999994704 eth**, despite that earlier spend. this later net increase has not been allocated to an authenticated incoming transaction or sender in this review. therefore a current approximately four-eth balance cannot support a claim that the original funds remained untouched. native-history explorer requests failed; retained lookup attempts and historical/current state records expose the gap rather than inventing a return transaction.

at **06:30:11 utc** the same day, the recipient sent **3.998918422844160119 eth** into the documented mayan forwarder in [0x38c7…39bf](https://etherscan.io/tx/0x38c7c72a6da978ee29e18649d5005d8978fbde862c0f78eb18fd70325e6939bf). the successful receipt wraps the native input and transfers the exact weth amount into the known swift source contract. its order-created event gives hash `0x47ecec44471cd15a4550897590a825a94e50aa43900e893f88ca2fa0a75b5fcb`.

using the previously pinned mayan abi, the forwarder event's inner calldata decodes a destination on wormhole chain 1, with raw recipient bytes corresponding to solana address `AKS15GjeivY1yBN3at6DNSg7q6UBmsPFtA2jWzvTniep`. a finalized solana transaction at **06:30:40 utc** invokes the mayan program and pays **92.375240889 sol** to that exact address. this association is **supported**, not promoted to a fully confirmed cross-chain order match: an independent order-state/pda check has not been completed, and the new mayan api lookup timed out.

at **06:32:41 utc**, a successful multi-source transaction transfers that **92.375240889 sol** onward to `EfaGnkjvYEtN9yCbetyUyZmmabmBzgeGEc9LMod6pV3y`. two other sources in the same transaction pay 99.839084078 and 24.250813331 sol into the same recipient. this is a documented mixed-funding boundary. the three senders sign the same transaction, an execution relationship which does not identify a human controller. no subsequent debit is allocated exclusively to this route. [decoded order](oct27_mayan_decoded_order.json) · [raw solana transactions](raw/).

## near route / separate larger sol forwarding

another branch forwards **44 sol**, then **43.998506547 sol**, to `DjWN6eDmNcettEf3HWpQQYcQitmMAQvYRcrF9H78jggx`. that address returns the requested maximum 1,000 history entries; the capture is explicitly incomplete. no lifetime balance allocation, service identity or final beneficiary is inferred. small lookalike-address incoming transfers are retained separately rather than mistaken for the actual onward recipients. [transfer rows](near_onward_transfers.json).

## integrity exception explained

the older explorer-label response has lf line endings while its saved checksum corresponds exactly to the same content with crlf endings. reconstructing crlf produces the historical digest exactly. an isolated-copy verifier passes with those reconstructed bytes. [reconstruction and verifier result](integrity_normalization_recheck.json) · [digest-matching copy](explorer_label_original_digest_crlf.txt). the original repository file and manifest remain unchanged; the original byte-level mismatch is still disclosed. this resolves the content-integrity question as a line-ending difference, without inventing new source metadata or attribution.
