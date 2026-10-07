# Evidence guide

The authority is the [technical investigation](ZYROX_Devsold_verification_v0_2.md#v0-114) at **v0.114 / U453**. Historical updates within that report retain their original evidentiary scope; later frozen findings supersede earlier interim figures where explicitly documented.

The [main report](../report/ZYROX_Main_Report_v1_1_Verified.md) provides the reader-facing narrative. Its eight reference groups identify the underlying technical sections and versions. The [transaction-link list](TRANSACTION_LINKS.md) contains nine central transactions; it is not the complete ledger.

## Data

- [35-sale manifest](../data/frozen_35_sale_manifest.csv): one row per verified FACv sale, including seller, timestamp, token input, SOL/WSOL receipts, proceeds account, unwrap destination and signature.
- [Cumulative proceeds](../data/figure_3_cumulative_proceeds.csv): exact sale-event step series. Same-second rows retain manifest order; no millisecond timing or interpolation is inferred.
- [Core transaction links](../data/publication_transaction_links.csv): nine existing signatures and signature-derived Solscan URLs.

The 35-sale inventory contains 17 case-relevant sellers and reconciles to 1,527,248,306.725914 FACv gross sold and 606.331808740 SOL/WSOL received. It does not claim to cover every ordinary market seller or unavailable archival history.

## Provenance accounting

The 597.487092059 SOL conservative minimum is a subset of mixed principal, not an additional amount or clean provenance. Category minima sum to 594.088880729 SOL; the joint-only unallocated minimum is 3.398211330 SOL. The difference from total verified receipts is 8.844716681 SOL in uncertainty/cost room, not a separately identified transfer.

Category minima are lower bounds at receiving/routing points, not an exact allocation or ownership finding. Attribution stops at mixed collectors without new independent provenance. No later collector payout is assigned back to FACv by this repository.

## Claims and public sources

[IMG_4204](claims/IMG_4204.jpeg) and [IMG_4205](claims/IMG_4205.jpeg) remain screenshot evidence. Original post IDs and absolute timestamps have not been independently recovered. Neither screenshot establishes creator-wallet ownership or documents the no-presale/no-KOL claims. See [captions](claims/CAPTIONS.md).

The [account continuity note](ACCOUNT_CONTINUITY.md) distinguishes canonical handle resolution from continuity of human control.

## Figures

Each figure has PNG and SVG versions with the same filename stem. Figure 4 compares three separate valuation benchmarks, not a reconstructed price series. Figure 5 ends at the attribution boundary; its joint-only accounting note is not a receiving branch.

## Limits

Co-signing confirms authorization of particular actions, not a common owner. Funding identifies a source relationship, not an external controller. Price candles, reserve-based marginal prices and execution prices are separate metrics. Proceeds are revenue, not net profit. The investigation does not establish legal fraud, intent to deceive or an identified final beneficiary.
