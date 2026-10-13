# GLITCH v0.3 — Upstream shared-funder network checkpoint

**Provenance:** User-supplied summary of a scoped ChatGPT Work finalized Solana RPC check, 2026-10-13. This repository checkpoint preserves reported observations; raw JSON transaction receipts and all 40 transfer instruction references have NOT been independently imported or checked here.

**Parent:** GLITCH v0.2, commit `8630c3aa8ffe4eb0f7dae16949b411944fc9681e`.

## Finding U001 — Overlapping direct funding

Ten downstream intermediary wallets F001–F010 in v0.2 reportedly received **four transfers apiece from four distinct members of ten upstream wallets A–J**. Each transfer was reported as **0.002858481 SOL**; each F wallet received **0.011433924 SOL**, then paid **0.000005 SOL** in fees to forward **0.011428924 SOL** to seller `8hiMXA1UHYUAeW6gd6q1XQLWzZkQL48znqgdgY1388B7`.

Network totals: **40 funding transfers / 0.114339240 SOL** into the F layer, less **0.000050000 SOL** in F-layer fees = **0.114289240 SOL** forwarded to seller. This reconciles with v0.2.

All first incoming F-wallet transfers were reported at **2026-10-12 16:22:24 UTC**, first recipient balance zero. Work reports five finalized transactions per F wallet with no additional pagination required. Each upstream A–J reportedly funded four F wallets, with the following incidence table.

| Downstream wallet | Four direct upstream senders |
|---|---|
| F001 | G, H, I, J |
| F002 | A, H, I, J |
| F003 | A, B, I, J |
| F004 | A, B, C, J |
| F005 | A, B, C, D |
| F006 | B, C, D, E |
| F007 | C, D, E, F |
| F008 | D, E, F, G |
| F009 | E, F, G, H |
| F010 | F, G, H, I |

## Upstream A–J addresses and reported reference signatures

**Important granularity limit:** Work's supplied table contains **one signature per upstream source**, although it states each source made **four transfers**. These ten signatures are therefore reference receipts, **not yet an exhaustive 40-transfer signature/instruction ledger**. Each signature may contain one or more instructions; inspect its parsed System Program transfers and retrieve all other transaction signatures as needed before claiming all 40 individually reproduced.

| Code | Address | UTC of reference receipt | Reported signature |
|---|---|---|---|
| A | `A1wwXt9qMxVvw9uxzczLtpkjKeNJJPABvQP22F21bAqV` | 16:22:24 | `4SvQ4YoVNAWBTCbJavz57jm8QTNWrs9Wo2wkrFo38uZ2tywJphDXFzSuuf2xMcjuVkUaU3fXYmgW3NyTGTruF3Wb` |
| B | `5VNeTcWWCvAGTv2ebtvxei2iMys52SLCiejMniQq86gf` | 16:22:24 | `3hZs6Ts15wEkqLc2PXL3kfZ7k5oDtR6a83F9RD9w7ty6cW4trNJjiKb8fHv5XEu6YqZv2uwhA6cP1MVbftEmSiSM` |
| C | `GJsYyKH8MAT1KPT7mtr8XiA2Tai7tEQDbH5LK3s7ns2a` | 16:22:24 | `VDaPHoNNUqkaTpTwMTeB5zycZRtpYfQbvDGkLRBDZo5veLvimACbwc5vDXJKx8t7scfU9J9JKnhXbSmVVGtyYLJ` |
| D | `9etBf3iKsZCfKeXe3NjktQ1Xi4tY7VKviuVzzKdkQwPF` | 16:22:24 | `nPtvhD2c4GrgRAagNeeevjjafuUntS8qxNLPh6LaobQSLKHtvFyeMbuuSW4Qbe8mHk5tk876PcaX4dmtDCSc2eZ` |
| E | `F5yYdg9sCTg8WmzMTgBA6Dj7uVDBaHX1QNsUs7WWK5kc` | 16:22:24 | `28ntu3jvoRxJuUr6bXmeTtuV5MDk1MJyGKjhcqUcNFkZF1tqKmzu43C9xcGE1QEN4Z1PrZusbQjwsWkQbPCFKMEq` |
| F | `DqGo29eNibExWk8jZmrhyXjEz2uTvjdUCf5AM9EcgXGh` | 16:22:24 | `5DLgKJ7wxJrUnzDc598C9ywadbaaCa7Y7U9piej2oi4UVHTrFsdnfPzmEbuYsjw5ALZryxNcK8ApYTZVFxaJ32mt` |
| G | `CgDPtbbnuzAfoBSYjK4NLxfe7bQgYadv5yYv412nNnz8` | 16:22:24 | `2XXjyoQaNihBYHkmy5rKG9N41ZrZhmeyakTV9ELg7tjRQGvTgZnucpYQVKUFeBPESZDi1iMDiGSEvy8oMom45smx` |
| H | `BDGM1cuJA5hxza9RABjZg26J3ENsdmJQWi26VfhQe9BL` | 16:22:24 | `5mBqdBL7cg6ZHrev4rjrzjKpcAhdtzcR95KvMjbq4YeXP24QtfDs8gow6WUybUrJMwP3QEqfWMkGiisX8BkSFyRK` |
| I | `Dt3ZWYLzkupnNQatNYZSucTqXr7XKESXDv3WifzLhdCi` | 16:22:24 | `3sQ6mCUuUN2xJH8sv17QRm4AeVoi3WVGydr9ci7yqanNfT9nHrNB7hPv4sckwGGAsZPoa7jY4JcNqDSV6N8MsDrM` |
| J | `4esiDn7jJdzVAfEbxwPdQtxGTH2jxwtWgzvSyRmz5i18` | 16:22:25 | `3fmdhUpoxdNPT7nCGF1g93XcXH97M7KPNsBUquSw9yv9XQAcTTBkBJ9teH8FgZ5h3NouZsDhAZoHqjwqSfj1prMC` |

The supplied summary says A–J were sole signer and fee payer for each respective transfer, each paid 5000 lamports in fees and ended with zero lamports. These are **Work-reported**, not independently audited here.

## Evidence assessment

- **CONFIRMED WITHIN WORK'S REPORTED FINALIZED RPC ANALYSIS:** Same upstream addresses appear across multiple F-wallet histories (direct sender reuse, not merely shared Jito/service addresses). No one address is represented as funding all ten.
- **NUMERICALLY RECONCILED:** 40 × 0.002858481 = 0.114339240 SOL; 10 × 0.000005 SOL in F fees; net 0.114289240 SOL to seller.
- **UNRESOLVED:** Original sources funding A–J; possible common control; whether A–J are a service; human/Kytro identity; potential wider ZYROX ties.
- **LIMITATION:** Complete line-item evidence for all forty transfers requires source transaction signature + parsed instruction index (not just ten sample signatures). Raw receipts absent in repository.
- **NOT ASSESSED:** Coordination as human intent, fraud, ultimate beneficiaries.

## Next single validation task

Export a reproducible **40-row** transfer ledger with exact signature, instruction index, UTC, from, to, lamports and signer/fee-payer for each A–J → F001–F010 edge. Attach raw JSON or hashes/source references. Only after validation should research advance another hop upstream; keep ZYROX separate.


## v0.4 follow-up — 40 instructions reproduced by Work (2026-10-13)

**Source:** User supplied screenshots of Work response. Work reports independently re-fetching **ten finalized transaction receipts** (the A–J reference signatures above). Each receipt contains **four outer System Program transfer instructions**. Thus the full set is **10 transaction signatures × 4 instruction indices = 40 individual transfers**, rather than 40 independent transaction signatures. Work reports sender = sole signer = fee payer in each transaction, and the instruction index is zero-based in `transaction.message.instructions`.

- Each reported transfer: **2,858,481 lamports**
- Total: **114,339,240 lamports = 0.114339240 SOL**
- Fee: **5,000 lamports per transaction, NOT per transfer**
- Ten source addresses each funded four distinct F-layer recipients; each recipient received four transfers.
- Work reports no sender/recipient/amount discrepancy against the v0.3 incidence matrix.

**Evidence label:** CONFIRMED IN WORK'S PARSED-RECEIPT REVIEW; NOT YET RAW-RECEIPT ARCHIVED IN REPOSITORY.

**Outstanding reproducibility artifact:** Screenshots show Work's conclusion and only the beginning of the 40-row table. The complete 40-row ledger, with signature + instruction index for every transfer, has not yet been supplied or stored. Retrieve the full existing Work output (do not conduct new chain research), export as CSV and retain raw JSON or SHA-256 hashes if available.

**Caution:** The structured four-output funding pattern establishes repeated transfers among wallets, not their common human controller, Kytro attribution, or fraud.
