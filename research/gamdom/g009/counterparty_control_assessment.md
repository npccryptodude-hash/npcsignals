# Financial relationships versus control

CONFIRMED RPC event history: 80 positive D→C events precede the anchor in the bounded interval, totalling 62,235.066339 USDT0. Values range from 1.001717 to 15,034.086265. The 674.470970 anchor is therefore not the first or largest observed D→C transfer. Two selected earlier transactions directly initiated by D are additionally receipt-verified: 1,348.792079 USDT0 on October 8 and 79 USDT0 on October 11. The remaining event rows are not individually recovered-signature evidence. No statistical anomaly score is calculated.

This establishes a repeated financial relationship predating the incident window. It does not establish that D and C share a signing key, an operator or a business purpose. It cannot identify which earlier transactions, if any, were legitimate or unauthorized.

The full bounded canonical event query involving D contains no exact A or B token counterparty. This is a negative finding limited to this token, chain and interval. It is not an absence claim for native assets, other tokens, other chains or intermediary routes. C is exact-match; lookalike addresses in the log export are retained as distinct full addresses.

The newly selected upstream initiators 0x37c29b046d2253ac7291bcf131282e0441cc9282, 0x938711f3c125f165cbcdcbc0711eec4512316118, 0x532857ca20ee151295d7d4085a6dde7132758904 and 0x9f273c1fd76b09cb09278019a50991a5f6265b0d were not found as exact addresses in the frozen G005/G006/G008 files searched. That sample comparison is not a complete audit of A/B/C funding histories.

Repeated upstream initiation toward D supports financial routing relationships. Generic router, Multicall and pool appearances are excluded as standalone common-control evidence. No shared recovered authorization, private key or human identity is established. G008's B-key recovery remains unchanged and is not extended to D. D's contract approvals and delegated authority history were not reconstructed; ordinary transaction sender fields are RPC metadata, not new independent signature recovery.

Reproduce: filter canonical_event_ledger.csv on full normalized addresses, compare saved transaction senders for selected receipts, and search the frozen checkpoint files. Never compare only shortened prefixes/suffixes.
