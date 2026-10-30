# following the transfer, not the headline

*npcsignals | research note | draft / not published | 30 october 2026*

the reported binance incident of 29 october generated a headline figure of roughly $6.3 billion. that figure describes a reported multi-chain event. our narrower question was different: what can we independently document about one ethereum transfer path?

we began with the observed movement from a binance-labelled wallet to a single receiving address. blockscout's records show 167,464.247856558836135296 eth in an internal transfer and 63 token-transfer events in the same transaction. the token records require individual contract checks: a name or ticker is not proof of an asset's identity.

one canonical ethereum usdt path offered a clear test. two transfers of 500 million and 200 million usdt reached separate addresses; their receipts and exact token logs now agree across two public ethereum rpc providers. downstream explorer events reconciled to the full 700 million, distributed across 19 positive transfers and 15 direct recipients. this is the same 700 million moving through subsequent hops, not additional losses.

following two of the largest branches led to different outcomes. four selected downstream transfers totaling 365 million usdt were also matched to transaction receipts across both rpc providers. one path of 175 million usdt was largely retained at a later address. direct calls to tether's `isBlackListed(address)` function through two ethereum rpc providers returned `false` at the observed block heights. that does not establish historical blacklist status or explain the retained balance.

another 80-million-usdt sub-branch was split between 50 million sent to explorer-identified liquidity contracts and 30 million sent to an address without reported contract code. the latter 30 million moved once more and was still shown as canonical usdt at the next recipient when checked. a separate transfer carrying the symbol "usdt" used a noncanonical token contract and was excluded.

the complete token logs for two pool-related transactions contain 132 events. they do not by themselves establish the output received by the original sender, a cash-out or the ultimate controller. those conclusions remain open.

the investigation is documented as a static visual evidence archive, with transaction hashes, token contract addresses, source checks and unresolved claims. it is a research checkpoint, not a live monitoring product.

**method:** observe first. verify before concluding.

*draft link to visual archive: https://github.com/npccryptodude-hash/npcsignals/tree/draft/visual-evidence-binance-2026/visual-evidence/binance-2026*

*editorial hold: remaining downstream events are explorer observations; replace draft branch link with approved public archive URL before publication.*
