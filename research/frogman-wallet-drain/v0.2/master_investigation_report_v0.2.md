# NPCsignals — Frogman investigation v0.2

Research update, not an article. English only. Frozen v0.1 is not changed.

## Saved-state inspection and continuity

At first resumption, GitHub main was 29732dcb330bf04d30aede1b781756f0750865b4. It contained the complete frozen package and inventory, but no v0.2 research. Recovered local work was saved in 724ce578b0b1a660253a912123868a5ca39346f1. Ethereum routing reconstruction was saved in 6665899e92c804be996f438e4dae939b07197255. This was also the inspected head when the user repeated the continuation request. Six Relay pairs were saved in 4e9a036fce9171fed915cb9461701b88ba6f33af. Saved files were retrieved and byte-compared; frozen archive paths show no diff. These are content-integrity checks, not a claim that commits are cryptographically signed.

The completed Solana reconstruction was not restarted. F0001–F0102, 28 finalized receipts, original CSV precision and evidence classifications remain frozen. New findings supersede an old assertion only where new primary evidence is identified explicitly.

## New reproduced Ethereum routing

CONFIRMED: Ethereum mainnet chain ID 1. All 15 outgoing transactions from 0x427C4b37de0714821B09C4FC655a713AbbCfbA83, nonces 0 through 14, were reproduced from JSON-RPC transactions, successful receipts, matching block hashes and transaction inclusion in block records. F0113–F0127 record the exact values and network fees.

Total sent: **362.262907164350756807 ETH**. Total network fees for those transactions: **0.000910467051228 ETH**. The queried balance was **0.000113694482353 ETH**; this is a dated snapshot, not a current guarantee. The public 362.26 figure is reproduced as the rounded outgoing total at this address. This does not by itself establish that every unit originated from the affected wallet.

First ordinary funding reproduced at 2026-10-06T20:19:35Z: 0xb644bf8e644a1195ad838180fd015f88938a8664128b9e0ad1e7b4a5eebe2198, from 0xf65954D6d6F877963bAcE359E44c1f01D3b11C2A, 0.036847749668146124 ETH. Funding is a transaction fact, not shared-control or identity evidence.

Twenty-three larger internal native credits totaling **362.226363346190827857 ETH** were independently reproduced using execution traces and their successful transactions. They came from 0x5c7BCd6E7De5423a257D81B442095A1a6ced35C5 and 0x4216E5AE6021C523aae05B6Ac6824F3C096cf905. Incoming source-chain deposit matches are not established merely by identifying these Ethereum credits. Other small credits and ordinary incoming transactions are preserved in history records. Indexed-history arithmetic sums all incoming amounts to 362.263931325884337807 ETH, exactly equal to outgoing value plus outgoing fees plus queried balance. Completeness and origin attribution of every small credit remain separate tests.

## Relay: six independently matched exchanges

CONFIRMED: six native deposits, **212.499 ETH**, to Relay Depository 0x4cd00e387622c35bddb9b4c962c136462338bc31 through LI.FI 0x1231DEB6f5749EF6cE6943a275A1D3E7486F4EaE, correspond to six reproduced Arbitrum fills totaling **561850.214994 USDC**. Arbitrum chain ID 42161 and USDC contract 0xaf88d065e77c8cc2239327c5edb3a432268e5831 decimals 6 were independently queried.

Every exact source hash, source wallet, timestamp, deposited amount, protocol order ID, API request ID, destination hash, recipient, output amount and observed transaction fee is in `relay_verified_pairs_v0.2.csv`. `verify_relay_pairs.py` checks the actual depositNative call, successful source receipt, block inclusion, matching order ID in the source trace/log and destination calldata, successful destination receipt and matching USDC Transfer event.

Five fills use direct token transfers. One fill is batched and its matching USDC Transfer event is from the zero address (mint), not from the generic Relay liquidity wallet. Token event origin and transaction executor are recorded separately. Do not infer a single physical coin path or common owner from either.

The public ~212.5 ETH claim is reproduced at its reported rounding. The deposit amount is not exactly 212.5 ETH. LI.FI's source explicitly warns that its bridge metadata may not correspond to off-chain Relay order data; destination metadata alone was not used as proof.

Provenance: **intact deterministic order association; mixed protocol liquidity**. The verified fills support an exchange linkage, not identical-coin continuity or identity. Onward Arbitrum movements require their own receipts; balance snapshots alone cannot supply destinations.

## Other reported EVM branches

| Public claim | Classification of full route | Reproduced scope / limitation |
|---|---|---|
| 362.26 ETH routing | CONFIRMED at routing address | Exact outgoing total above; affected-wallet origin is a separate question. |
| ~212.5 ETH Relay | CONFIRMED deposit/fill pairs | Exact 212.499 ETH to 561850.214994 USDC on Arbitrum. |
| ~37 ETH Chainflip | UNRESOLVED | Two 18.5 ETH onward funding branches and later vault-related receipts preserved; full bridge order and payout not reproduced. |
| ~35 ETH Across | UNRESOLVED | A 35 ETH LI.FI call indexed as Across V4 is preserved; corresponding destination fill not reproduced. |
| ~34.75 ETH Mayan | UNRESOLVED | Calls indexed as Mayan have attached native values 22.5, 10.251 and 1.999 ETH, summing 34.75; attached value is not a verified destination payout. |
| ~37 ETH unlabeled collector | UNRESOLVED | Two separate 18.5 ETH branches are observable. A single collector, common owner or beneficiary is not established. |
| ~2 ETH NEAR Intents | UNRESOLVED | A 2 ETH transfer is reproduced, but protocol order, receiving chain and payout match remain unverified. |
| ~4 ETH live wallet | CONFIRMED dated balance | 4 ETH observed at 0x4521eF4Df51A7689d4DB5d8FC598685CB226fF58; no future retention or ownership claim. |

These qualified branch observations do not promote full route claims to CONFIRMED. Precise transaction paths are in the expanded ledger and graph. Protocol method labels from an explorer are pointers for reproduction, not proof of destination or identity.

## Preserved and enriched Solana findings

CONFIRMED v0.1 findings retained: first reproduced suspicious outflow 2026-10-06T20:14:54Z; four BP disposals; ten Privacy Cash deposits totaling **13240.973780900 SOL**. No matched withdrawal is established.

New CONFIRMED signer correction: finalized binary transaction 5fFLUqvsAJLEn1cPnypjzfKi8iioUYCnaCgR8QonKtE2U3xf6nk8RduhjURrjLP32yX1pzTT9vy9bXHXfQyNA87t, at 2026-10-06T20:35:41Z, contains two Ed25519 signatures verified with OpenSSL: Grr9WnZdcetQywtFXog81UhqmnJyvFhb4AT3ipw44mZP and 69FnU8vszZSZF6DZCT6VHdsvm3DvvojDgbwqzHJ4cCFS. This supersedes the earlier non-signer assertion, without altering the frozen jsonParsed response. Co-signing an RFQ does not establish common beneficial ownership.

First-party Jupiter documentation/source identifies program 61DFfeTKM7trxYcPQCM78bJ794ddZprZpAwAnLiwTpYH as the order engine. Grr9's observed counterparty inventory settlement is 7859.975842 USDC against 64.925550449 SOL/WSOL. The USDC includes 0.001200 third-party USDC. Human counterparty identity and shared beneficial ownership are NOT ESTABLISHED.

CONFIRMED current snapshot: Just a Backpack Token-2022 mint ZesMGYmokFiEuDvNzWeMhB7jxF6eUW8c512vwSKSTNK has 100 basis point older and newer transfer-fee settings. The historical debit-credit difference, 160314.105600 tokens, is exactly 1%. The historical fee explanation remains SUPPORTED because historical mint-extension state was not obtained.

CONFIRMED native accounting in the preserved incident receipts: 13240.996153263 SOL inflows = 13240.973780900 deposits + 0.002050000 deposit network fees + 0.013919200 new-account allocations + 0.006403163 remaining. Residual is 0.000000000 SOL. Includes third-party native dust; not exclusive incident provenance. BP gross WSOL receipts total 13060.251206492; routing deductions are 6.686352013 SOL. Intermediate forwarding is not charged twice.

## Subsequent primary-source verification: Robinhood origin and Arbitrum consolidation

CONFIRMED token-transfer linkage on Robinhood Chain 4663: affected 0x14AA2A71dbb5eF87b81F92205E2699AA4aa65794 to receiving 0x427C4b37de0714821B09C4FC655a713AbbCfbA83. All three transfers occurred in block 81904175 at **2026-10-06T20:14:00Z**. This is the earliest reproduced token outflow in the examined 20:10–21:10 UTC window, not a claim that all earlier native/approval/failed transactions have been excluded.

| Transaction | Contract / current symbol | Exact token amount |
|---|---|---|
| 0x49e05a92a0b08841fac2b475877cd02732e957412d0e1a3cad706f489641c596 | 0x020bfc650a365f8bb26819deaabf3e21291018b4 / CASHCAT | 3700227.867433114634814141 |
| 0xbf1158177a2f350f092b2426025b339bfeeaa77923e4e51c6bb216d3292b8171 | 0xc60ba256b44334a0cd2c7242e98b88f031abb006 / V4, Programmable | 13705666.431273061609772002 |
| 0xa71e132f397b427cc6f1bb58252a5c56b2e0a5dde14733c840103ec3552456a7 | 0x0bd7d308f8e1639fab988df18a8011f41eacad73 / WETH | 0.500012122639901441 |

Do not relabel V4/Programmable as MARSCOIN. Current metadata and contract identity are recorded explicitly. Receipt transaction indices 2, 9 and 10 establish same-block order. All three transaction senders are the affected address, with nonces 10, 11 and 12. Earlier wallet activity and the reported MARSCOIN disposal remain separate unresolved tests.

Eleven candidate-wallet CASHCAT transfer events during the window are also reproduced. Some transaction senders differ from the token sender. The ledger therefore distinguishes transaction authority from token Transfer.from and does not infer shared ownership. These events do not alone establish final native proceeds from swaps; WETH unwrap recipient and routing fees need execution evidence.

CONFIRMED: the six matched Arbitrum recipients transferred **561850.214994 USDC** in six positive-value transactions to **0x2df1c51e09aecf9cacb7bc98cb1742757f163df7**. F0190–F0195 record the exact six consolidation movements. Their transaction/receipt/block and token-event checks are reproduced by `verify_chain_extensions.py`. All six queried recipient USDC balances were zero at query time. The consolidation recipient's other funding and later outflows remain UNRESOLVED; exclusive provenance must not extend past it without those checks.

Six adjacent zero-value events name **0x2df1df582d0a1efc7178fd78b2bcd9aa08a73df7**, a different address. They are preserved in `zero_value_events_v0.2.json`, excluded from monetary totals and do not establish the purported token sender signed or controlled the transaction.

The expanded unique ledger range is **F0103–F0206**: F0103–F0112 evidence enrichments, F0113–F0127 routing-address outgoing transactions, F0128–F0186 funding/internal credits/onward routing/Relay fills, F0187–F0206 Robinhood and Arbitrum token events. Transfers at successive hops must not be summed as distinct losses or as additional proceeds. Network fees shown on multiple events in one transaction must be counted once per transaction.

A dated Ethereum snapshot confirms **4 ETH** at 0x4521eF4Df51A7689d4DB5d8FC598685CB226fF58. This reproduces a four-ETH retained branch, not a future balance guarantee. Two separately funded 18.5 ETH nodes, 0x1d68935c108b380CBb86198b002bC4D4A13c89F2 and 0x4bf5bb54C43E3ADDc3F62AB5ec943E16F3806ad0, each returned zero native balance at query time. Their onward transactions remain unresolved; do not describe 37 ETH as currently retained or infer a common collector.

## Access scope, negative findings and remaining work

Ethereum explorer pagination returned 54 ordinary transactions and no further cursor for the candidate address, and 27 internal records without a further cursor. Empty affected-address Ethereum history is only the examined index result, not proof of no activity on other chains. Ethereum debug_traceTransaction was unavailable; trace_transaction on dRPC supplied primary execution traces.

BSC chain ID 56 responded, with nonces 4 and 34 at query time. The large and 1000-block Transfer requests returned limit exceeded; historical nonce queries returned missing trie node. Routescan returned chain not supported. No BSC incident history was reconstructed from those failed requests.

Official Robinhood Chain RPC identifies chain 4663 and returned nonces 14 and 25. Its official explorer history requests returned HTTP 403. RPC Transfer logs in the 2026-10-06 20:10–21:10 UTC window located source-to-candidate token transfers; these have now been verified as detailed above. Historical nonce state was unavailable. Neither access failures nor current nonces supply an earliest suspicious transaction by themselves.

Arbitrum explorer HTTP 403 did not establish no outflow. An initial combined-address RPC query exceeded the 100000-block limit; scoped subqueries and their results are retained. Zero-value Transfer events are not monetary flows and do not prove the named token account authorized a transaction.

No matched Privacy Cash withdrawal, ultimate beneficiary, shared beneficial ownership across routing addresses, exchange deposit, freeze, negotiated recovery or compromise method is established in this examined evidence. SIM swap, email compromise, malicious dApp/signature, browser/session compromise, QR code, physical access, WiFi compromise and conference-attendee involvement remain UNRESOLVED. Fund-flow reconstruction cannot resolve them.

Publication readiness: suitable for a clearly scoped research checkpoint; not mature for a comprehensive incident article or identity/compromise attribution. No article has been written or published.

Attention is not evidence. Visibility is not evidence of relevance. A transaction path is not proof of identity. A fund-flow reconstruction is not proof of compromise method.

## Continuation from verified head 8543f9e — Arbitrum mixed-fund boundary

The saved head was inspected before new research. It contained the above findings through F0206 and retrieval verification, not unfinished unsaved findings. See `continuation_2026_10_08/README.md` for the precise saved-state inspection and supplemental evidence inventory.

CONFIRMED: the Arbitrum consolidation address `0x2df1c51e09aecf9cacb7bc98cb1742757f163df7` has deployed contract code. At block 512881298, timestamp 2026-10-08T12:31:48Z, its USDC balance was 393259622.336699. This is not an incident-only balance, recovery or identification of an exchange.

F0207 reproduces an additional 51 USDC inflow at 2026-10-07T01:51:25Z. F0208 reproduces a 150395.42 USDC outflow at 2026-10-07T01:53:56Z. Successful transaction receipts, token events, matching block hashes and transaction inclusion independently confirm both context events. They are not counted as new incident losses. Exact hashes and authority distinctions are in `continuation_2026_10_08/transaction_ledger_F0207_F0208.csv`.

Scoped USDC logs over blocks 512422000–512881298 reproduce substantial other inflows and outflows. Provenance at this contract is mixed. Assignment of any particular outflow to the six case-related deposits is NOT ESTABLISHED. No timing-only or accounting convention is substituted for deterministic linkage. Contract operator, permissions, exchange identity, full lifetime funding, ultimate beneficiary and compromise method remain UNRESOLVED. Historical opening balance was unavailable from the examined provider.

The supplemental inventory and checksums are additive to the earlier saved v0.2 checkpoint inventory. Original v0.1 and original transaction/classification records are unchanged. The supplemental ledger extends unique IDs through F0208; no previous ledger entry is renumbered. Publication assessment remains a scoped research checkpoint, not a mature comprehensive article.
