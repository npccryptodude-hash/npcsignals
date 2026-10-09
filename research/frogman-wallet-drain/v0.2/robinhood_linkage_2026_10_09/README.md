# Robinhood-to-Ethereum Across linkage — 9 October 2026

Parent verified public checkpoint: a1a3ffadb61db854c381034775364c755e957be9, through F0434. Additive records F0435–F0464. Frozen v0.1 and F0001–F0431 unchanged; the preceding Across Base block also remains unchanged. No article.

## Confirmed result

Fifteen Robinhood Chain (4663) FundsDeposited events are transaction-specifically linked to fifteen previously reproduced Ethereum FilledRelay events. Origin transactions, successful receipts, blocks, block membership and UTC timestamps are retrieved directly from the Robinhood RPC. First-party interface signatures are checked using the preserved Keccak implementation. Matching uses chain IDs, deposit IDs, depositor, recipient, token addresses, exact input/output amounts, deadlines, exclusive relayer and original message hash. Where an original message is nonempty, Keccak of its bytes is compared to the destination event. The destination updated-message hash is preserved without equating it to the original message. All fills are successful FastFill events with unchanged recipient and output amount.

Exact deposited wrapped-native units: **213.215761888326838512**. Exact Ethereum output units: **213.164462838697324465**. These are single-route input/output totals, not additional losses. Fees are not decomposed from amounts; exact per-route input/output differences and separately observed execution gas costs are recorded. No repayment/refund transactions independently verified.

The origin pool is `0xd29c85f15df544ba632c9e25829fd29d767d7978`. The preserved Ethereum Across pool emits the matched destination event. This establishes protocol routing, not a legal identity or full historical contract/permission audit.

Eight direct origin transactions are sent by `0x427c4b37de0714821b09c4fc655a713abbcfba83`, with native value equal to the deposit amount and a matching wrapped-native mint to the pool.

Seven other outer transactions are sent by `0x07ae8551be970cb1cca11dd7a11f47ae82e70e67` to `0x998d7c178a1f9607b47ea3a8e22426451b3ce707` with zero attached native value. Their receipts mint the exact input token amount to an intermediate address and transfer it to the pool; the depositor event field still names `0x427c...bA83`. Their emitted Ethereum recipient is a callback contract, `0x4216e5ae6021c523aae05b6ac6824f3c096cf905`, rather than being silently relabeled as the routing wallet. Existing native-credit execution traces remain separate evidence. These facts do not establish the underlying native funding source, authorization mechanism, custody provider, common key owner or beneficiary.

All fifteen original message hashes and relay parameters are checked. No assumption that the zero-value outer sender owns the deposited value. No claim that all 23 larger Ethereum credits or all 362.26 routed ETH originated on Robinhood. The prior affected-wallet token transfers are preserved, but their complete sale-to-native-proceeds linkage is not proven by the new bridge matches. The separate Base route remains independent. No new inference that each origin deposit funded one of the six Relay routes is added without the corresponding saved onward edges.

## Scope and failures

Indexed-address log searches cover Robinhood blocks 81904000–82073999 in provider-supported ranges for topic positions 1, 2 and 3. This is not a complete account history. One topic-3 range, 81984000–82013999, timed out; its failure is preserved and no completeness assertion crosses that gap. Initial 50000-block queries failed the provider's 30000-block range limit, and smaller queries were used. Explorer address history/log requests returned HTTP 502. JSON-RPC error responses inside HTTP 200 are explicitly treated as failures. Fifteen deposit candidates in the successful logs were each verified against actual receipts, not merely accepted from log search results. Log search timestamps sometimes returned zero; origin timestamps instead come from independently retrieved blocks. The Ethereum destination receipts were reused from the preserved investigation rather than recollected or renumbered.

## Ledger and next target

Two additive records describe each route: an origin deposit and a cross-chain association. These are not summed as distinct losses. The new ledger and edge file update the reconstruction without rewriting any earlier row. No source-credit entry was silently upgraded in place.

Next highest-priority branch: Chainflip. Upstream Robinhood disposal/native provenance, the timed-out log range, remaining source origins and actual service/control attribution remain unresolved. Mayan, NEAR Intents, unlabeled destinations, case-specific XMR1 redemption and Privacy Cash withdrawal linkage remain unchanged.

Run verify_robinhood.py offline against saved sources to reproduce exact event correspondences. The Keccak helper is reused from the preceding saved Across block without invoking that block's collector or modifying it. Source request records capture each adaptive lookup. No fund-moving operations were performed. Next ID: F0465.

| Origin transaction | Destination transaction | Input wei | Output wei | Origin record | Edge |
| --- | --- | ---: | ---: | --- | --- |
| 0xd5d15936a30c21415cbf4e39f14ac50bb6936d3f6ad4cdd57c808c1732a4cfd5 | 0xcff34a0c22261839ef69e4039ad6726e01fc95663bdc192d21bf35699d7883a3 | 8000000000000000000 | 7994853008400480312 | F0435 | F0436 |
| 0xc5a4dcdecb4cee5e6be83fa1adc2982c7cd69d879838d285c42c84880014edfa | 0x7934a9f4945e9a8499d7967a922ccf8bd54f5c38c642d22b506c34edf24dd663 | 8000000000000000000 | 7994854152497038032 | F0437 | F0438 |
| 0x9680e837c5b4cc6c7a59f2244e8a399e73ecdde3ee03e9cd74f3c6d272a9f689 | 0x85ac8c0202089c79a04a9f91a7e17b37144b4c1b74af4295da23e2969d4b352a | 8000000000000000000 | 7994852363662127816 | F0439 | F0440 |
| 0x79bdbf44da9909e691bf34fb2edc7828b9dad69e8579378473b2aeb03cfdfe17 | 0xd660af041faddd964b1d59cecc709beeb9e425282ab93a4d8f229455af69ff37 | 8000000000000000000 | 7994852363662127816 | F0441 | F0442 |
| 0xd442e00deb23288942118e3ff724799215e5aed37e1ef181e32a9a262929f96b | 0x5b8ab3e41fe8eb1ababc70fee036100af41e9afa9588c8a53ba99bec25c3530b | 8000000000000000000 | 7994853879122892392 | F0443 | F0444 |
| 0x4906396cfabba1bbb8d92b1883cf42e814f137075eb1aa65180bedf5aca7ad8d | 0xa8b7de369a499a844c12f59905ef4c52386272b10aac66d9e3aeeaa9d02a145b | 8000000000000000000 | 7994854522359981440 | F0445 | F0446 |
| 0xc0b7f45cd5cdbf2c923302ec240dbbd315331343df75bdd04f5e31b263d29b15 | 0xaedc189291428449d48139f7e9866653f2d3c7ff6bb6150836ffc4b135369e2e | 8340000000000000000 | 8334586201987309819 | F0447 | F0448 |
| 0xea927aad2489ff07fe9e2e476d406ebd8ce55d9a0152a0cbda4acabf86fc06f4 | 0x5ae46f2541d52f0f1b907c6a02ebe6cd71f3525a4ee3e6bbfe8d8341661f7ce9 | 8000000000000000000 | 7994855953276813640 | F0449 | F0450 |
| 0x6f8da68489c3bb1a585fab4d035c3bf35aa70009df259a71dc12b562210e086e | 0x7873e900cc196ea94a7c671f7f299fe6842412e6048fac07411655e1161ec9cf | 18875767473824278512 | 18874470654663653144 | F0451 | F0452 |
| 0x25a6a2aa5ea0f6808b47987692a7460360932bca2019427ff7da52938b2a78ce | 0x794649aaa990c10f12c40b94d4d198280abb2645e134bf5a4fcede4cb098a405 | 32500009795520000000 | 32497970839479074400 | F0453 | F0454 |
| 0x8934174248a9d8f17ba7ef4ac0dfbc7b9088853202faddd21df966d2eb920d5d | 0x3b55306138fd68b7a3863aa8ac29cdf786f4807deb4e36ed237671b59220d988 | 24375007114569688000 | 24373434305384634707 | F0455 | F0456 |
| 0x97a07da42d62a948bebed67c1f9c9973a9032d5128b8b5e383c24a35ff058126 | 0x2b422b1831483eb9158ef56d9faed48e150d907e5773e4b97f6d8147cc5204c3 | 18281255103833906000 | 18280017451009445335 | F0457 | F0458 |
| 0x279c1a0eeff370007bb08e238168de7ade2906d1de0a646cfdf3626cb8961423 | 0x7768d5b0506bf88fbc4c5d94f51eb8fff49dc67d55fd1d632811f8ce78087b8c | 13710941096703989500 | 13709954811149920040 | F0459 | F0460 |
| 0x0706d7c5f04ab89b49779ead6c84c410ae40844d0ba1c2d01e7aa905879652dc | 0x3d417a0ebec865a9889dd5469fd14532a48a0b36c3a145e54230364532944252 | 20566411183773312250 | 20565046696727485944 | F0461 | F0462 |
| 0xd46993136ef26338ba391fd35461a8f36d0ab4f96116057510b109b188ffc351 | 0x82baf0241ef2cbaa4d05cf1a5279705a330ec2cb27054f782f3b602697475d8f | 20566370120101664250 | 20565005635314339628 | F0463 | F0464 |
