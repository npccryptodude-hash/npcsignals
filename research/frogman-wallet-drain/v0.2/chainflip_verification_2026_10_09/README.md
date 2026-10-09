# Chainflip transaction-specific verification — 2026-10-09

Checkpoint: public main e782917cd4f212d1dfc83af0da5c282722050653, through F0464. This additive block records F0465–F0470. Frozen v0.1 and all prior ledger files remain unchanged. This is an evidence report, not an article.

## Result: two CONFIRMED Ethereum → Solana edges

| Origin observation | Swap ID | Channel ID | Ethereum block / UTC | Input | Solana slot / UTC | Output |
|---|---|---|---|---|---|---|
| Existing F0159; enrichment F0465; settlement F0466; edge F0467 | 1894600 | 15137950-Ethereum-676 | 26137189 / 2026-10-07T01:21:47Z | 18.5 ETH | 454074616 / 2026-10-07T01:25:26Z | 410.977610441 SOL |
| Existing F0160; enrichment F0468; settlement F0469; edge F0470 | 1894627 | 15138057-Ethereum-2572 | 26137244 / 2026-10-07T01:32:47Z | 18.5 ETH | 454077123 / 2026-10-07T01:36:39Z | 411.389572055 SOL |

Total routing: 37 ETH → 822.367182496 SOL. These are subsequent routing observations, not additional losses. Do not add the origin, settlement and edge rows together as separate losses.

The full source/destination transaction identifiers, wallets, raw-unit fees, broker accounts, protocol event indices and evidence paths are in `cross_chain_edges.json`. Its entries also extend the cross-chain reconstruction without rewriting earlier branches. The merged timeline preserves the prior 464 objects exactly.

## Reproduction and linkage

Fresh read-only dRPC mainnet queries reproduce both Ethereum transactions, successful receipts and containing blocks, including sender, deposit address, native value, block number and UTC time. Publicnode attempts timed out; those errors are retained. No conclusion of absent history follows from those failures. The successful alternate requests establish origin reproduction independently of the earlier F0159/F0160 files.

The first-party Chainflip SDK source establishes the mainnet backend URL and `/v2/swaps/{id}` status endpoint. Three lookups per route—origin hash, channel ID and swap ID—return the same completed swap, exact deposit transaction, 18.5 ETH deposit, deposit address, destination address, asset conversion and egress signature. Each completed five DCA chunks, with zero remaining input/chunks. Exact protocol correspondence supplies the cross-chain link; timing and amount similarity are not used as attribution evidence.

Solana mainnet RPC, requested with finalized commitment, reproduces both egress signatures independently. Each contains one System Program transfer to the exact Chainflip destination for the exact net amount. Recipient balance increases equal the transfers; payer balance decreases equal transfer plus transaction fee. Both transaction errors are null. Mainnet genesis is independently checked. Raw transaction instructions, balances and protocol status objects are preserved under `access/`.

Chainflip's API reports the deposit, scheduled-egress and witnessed-egress State Chain event indices. These are protocol-native records preserved verbatim, but independent State Chain consensus inclusion and event decoding were not reproduced. The CONFIRMED routing claim rests on exact first-party protocol records joined to independently reproduced successful origin and finalized settlement transactions.

## Fees and spread

| Swap | Ingress ETH fee (wei) | Protocol network fee (USDC raw units) | Broker fee (USDC raw units) | Egress SOL fee (lamports) |
|---|---|---|---|---|
| 1894600 | 54306997050000 | 49721646 | 273195587 | 14000 |
| 1894627 | 37013312400000 | 49706343 | 273111501 | 14000 |

USDC uses six decimals; ETH eighteen; SOL nine. Ingress deductions reconcile deposit value minus original swap input. Gross converted SOL minus net settlement equals 14,000 lamports on each route, matching each Solana transaction fee. This comparison does not create a second additional fee/loss. API-reported USDC fee execution is not independently audited. Origin Ethereum gas costs are separately calculated from reproduced receipt gasUsed × effectiveGasPrice in the edge records. No ETH/SOL subtraction or independent market spread is asserted.

## Attribution limits and endpoint roles

CONFIRMED: case-specific Chainflip deposit channels, exact swaps and Solana settlement endpoint role. Both egress transactions have payer/source `AYVYJRA4FMtSbf16MwdZnaKsxonQGtyeWFGwnevv4En3`. Chainflip's current documented Solana vault differs; the observed payer is therefore described only by its reproduced historical egress role. Historical vault rotation or authorization was not audited.

The API identifies two broker accounts on each swap: `cFNwtr2mPhpUEB5AyJq38DqMKMkSdzaL9548hajN2DRTwh7Mq` at 5 bps and `cFLdvBS9Gq9iqB8Zdb5cmnWgmhqvEojQYGMBquDz7xRiSvsJV` at 50 bps. No human, custody firm or service identity is assigned to these accounts. Shared brokers, deposit infrastructure or egress payer do not establish common ownership or operation of the origin/destination wallets. The recorded refund addresses equal the respective origin senders, but this is protocol configuration, not identity proof.

UNRESOLVED: complete provenance from the affected wallet, custody relationship, shared control, downstream beneficiary and independent State Chain inclusion. No new owner, custody attribution, final beneficiary or external XMR1 redemption is established. Existing SUPPORTED and CLAIMED findings elsewhere remain unchanged.

## Negative candidate checks

The separate prior 18.5 ETH transactions F0152 (`0xbee5625019a5eabaefb69384016b22b4db5ab65a1e2fb3233b84528127b1a44e`) and F0153 (`0x6af96ed173b572ab313de0e061c94572d7c4db07552c770d1b583a692269526f`) returned HTTP 404 from the Chainflip swap-status endpoint. This closes those specific lookup attempts, not all possible bridge involvement. They remain separate unlabeled branches; they are not matched to these swaps. Limited address-history responses are retained as candidate context, not ownership evidence.

## Reproduce and continue

Run `python verify_chainflip.py` offline to check exact transaction/API correspondence, fee arithmetic, mainnet identity, balances and immutable prior timeline rows. `SHA256SUMS.json` indexes this block's source bytes and derived files. Request records contain endpoint, UTC retrieval time, payload and HTTP/access outcome. `collect_chainflip.py` is the generic read-only request collector; the saved payloads are the authoritative collection manifest. No channel was created, swap requested or funds moved.

The two reported Chainflip routes are resolved as far as the collected evidence allows. Next branch: Mayan. Privacy Cash remains separate and was not reopened. No article was written.
