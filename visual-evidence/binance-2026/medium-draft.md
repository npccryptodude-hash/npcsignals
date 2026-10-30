# following the transfer, not the headline

*npcsignals | research note | editorial draft / not published | 30 october 2026*

the reported binance incident of 29 october produced an estimated multichain loss of roughly $6.3 billion in external reporting. that estimate is not a number independently established by this investigation.

our scope is narrower: what can be documented from one ethereum trail?

blockscout recorded a 167,464.247856558836135296 eth internal transfer and 63 token-transfer events from a binance-labelled address during the main sweep. an explorer label is not proof of beneficial ownership. the incident's authorization mechanism and ultimate attribution are not independently resolved here.

we followed the canonical ethereum usdt contract, rather than relying on token names. the first visible transfers of 500 million and 200 million usdt were matched to transaction receipts and transfer logs returned by two public ethereum rpc endpoints. the two receiving addresses then distributed the same 700 million through 19 positive downstream events to 15 recipient addresses, according to the retained explorer ledger. later transfers represent movement of those funds, **not additional losses**.

four selected third-hop transfers totaling 365 million usdt were also matched through two rpc endpoints. on one branch, 175 million reached a later address. a blockscout balance snapshot showed 174,999,872.327620 usdt, after a small observed outbound transfer. two rpc calls to tether's `isBlackListed(address)` function returned `false` at the blocks queried. neither result establishes the address's historical freeze status or why funds remained.

on another branch, 80 million was redistributed through 20 canonical-usdt events: 50 million into contracts identified by blockscout as liquidity infrastructure and 30 million to an address with no contract code reported by that explorer. the 30 million then moved to another address, where a snapshot showed a 30-million canonical-usdt balance. these 20 transfers and the next 30-million transfer were matched to retained rpc receipts from two endpoints.

pool labels and transfers into contracts are not evidence that a swap settled, a cash-out occurred or a particular party controlled the destination. likewise, a different token using the symbol "usdt" was excluded because its contract address was not the canonical usdt contract.

**evidence tiers:** selected b013–b015 token logs are rpc-receipt matched. remaining balances, address labels and downstream classifications are explorer observations. estimates of overall damage, attribution, ownership, authorization mechanism and final disposition remain externally reported or unresolved.

the accompanying visual archive preserves transaction hashes, source files and limitations so readers can check the trail without mistaking movement for attribution. it is a static research checkpoint, not a live monitor.

*observe first. verify before concluding.*

sources and verification register: [approved public evidence archive url — pending]. external incident context: [binance](https://www.binance.com/en-AU/support/announcement/detail/c5a8729a97ac486d963784d96c5642d7), [trm labs](https://www.trmlabs.com/resources/blog/north-korea-steals-usd-6-36-billion-from-binance-in-the-largest-hack-in-history), [bitquery](https://bitquery.io/investigations/binance-hack).

*publication hold: verify external links and public archive url; do not publish draft branch as final evidence archive.*
