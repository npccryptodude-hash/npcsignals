# b016 / fbi attribution update

npcsignals | source update | 1 november 2026

## source

- issuing authority: federal bureau of investigation (fbi cyber)
- title: *north korea responsible for $6 billion+ binance attack*
- publication date: 31 october 2026
- primary source: https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack
- independent press reporting: https://en.yna.co.kr/view/AEN20261101000300315

## what the fbi states

the fbi publicly attributes the theft of more than $6 billion in virtual assets from binance on or about 29 october 2026 to the democratic people's republic of korea (north korea). the agency calls this operation **tradertraitor**.

according to the fbi, investigators working with the us secret service and irs criminal investigation observed actors converting stolen assets primarily into ethereum. the fbi expects additional laundering through decentralized finance and instant-swap services.

the fbi published ethereum addresses it describes as holding or having held stolen assets and being operated by or closely connected to tradertraitor actors. its list is an **official attribution statement**, not independent proof that a particular person owns or controls each address.

## classification

- **confirmed publication:** the fbi issued this advisory dated 31 october 2026.
- **official attribution (fbi):** north korea / tradertraitor. this is a government assessment. npcsignals has **not** independently proven the operator's identity.
- **individual identity:** no named physical suspect or arrest was established by this fbi advisory. the listing of blockchain addresses is not identification of a named person.
- **b006–b015 ethereum receipts:** existing verified transfer-log facts are unchanged.
- **overlap with the b006–b015 address set:** **not assessed in this checkpoint**. no matches, non-matches, common ownership or direct criminal control are asserted. a complete reproducible address comparison is necessary before such statements.

## follow-up verification protocol

1. preserve the dated source text, retrieval time, full ethereum address list and content digest.
2. normalize case for ethereum hex addresses and compare exact 20-byte addresses against all ledger senders, receivers, contract addresses and transfer-event counterparties; distinguish transfer counterparties from token contract addresses.
3. inspect any exact match for transaction hash, direction, timing and value; use independent ethereum rpc receipts rather than explorer labels alone.
4. record indirect links separately by hop count and time ordering, without treating graph proximity as shared control.
5. keep **fbi attribution**, **on-chain transfer evidence** and **human identity** as different evidence tiers.

## restrictions

do not imply the fbi has publicly named an individual suspect on the basis of this alert. do not infer that a token transfer proves ownership, successful swap, money laundering intent or recovery. do not add a later hop to the same stolen-funds total. this update does not make the existing visual reconstruction a live monitor.

status: **source update documented; cross-check pending; publication hold unchanged.**
