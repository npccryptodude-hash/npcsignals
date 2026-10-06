# Five figure specifications and final captions

Five PNG/SVG pairs are included. Their publication QA is recorded in [REPOSITORY_QA.md](../REPOSITORY_QA.md); corrections remain. Use a restrained white/charcoal palette, readable labels at mobile width, and accessible contrast. Never use colour alone for evidence status. Keep exact numbers in data/notes; round only visibly labelled display values. All times UTC on 30 September 2026.

## Figure 1 — The First 60 Seconds

**Layout:** vertical mobile timeline with five groups: 17:18:06 launch → first Hp4q sale → Tmcg buy; 17:18:09 Hp4q/Hrpa subtotal; 17:18:10–17:19:03 Tmcg sales. Separate the three 17:18:06 entries vertically and label slot/index: launch 452029524:1330; Hp4q sale 452029526:608; Tmcg buy 452029526:610. Do not draw milliseconds.

**Callouts:** 142.089113597 SOL/WSOL received by three Hp4q/Hrpa sales within approximately 3 seconds. Final: **251.752785673 SOL/WSOL received by 19 case sales within 57 seconds**. Tmcg completion +57 seconds.

**Caption:** The first case sale shares the launch timestamp-second but occurs two slots later. By 57 seconds, 19 verified case sales had received 251.752785673 SOL/WSOL. Timing proves rapid selling, not intent.

**Placement:** section 4. Source: v0.112 timeline, frozen 35-sale manifest.

## Figure 2 — Consolidation / Control

**Layout:** two source groups, HZrAo (100M FACv) and 63 other source wallets, entering G16. Group total: **581,307,162.351855 FACv / 11 transactions / 17:58:26–27**. This is a grouped view; D12 supports HZrAo and relevant co-signatures, not all 11 transactions by itself.

**Legend:** solid arrow = token transfer; dashed bracket = co-signing in a specific transaction; payer badge = transaction fee payer; grey detached box = routing/program infrastructure. Show HZrAo–G16 D12 co-sign bracket and G16 payer badge. A separate inset identifies Hp4q–Tmcg D06 tip/RecordMevBuy, Hp4q payer. Place P1/CUo7 in a detached routing-context box with no invented transfer line into the consolidation. No owner-group enclosures or same-owner lines.

**Status labels:** SUPPORTED COORDINATED OPERATIONAL STRUCTURE. NO CONFIRMED CONTROL OVERLAP across the six core wallets.

**Caption:** Sixty-four sources consolidated 581,307,162.351855 FACv into G16 in 11 transactions. Signatures and fee-payer roles document specific cooperation, not common ownership or unilateral control over other wallets.

**Placement:** section 5. Sources: v0.100 matrix and D12; v0.98 D06; v0.110 consolidation manifest.

## Figure 3 — Cumulative Verified Sale Proceeds

**Dataset:** data/figure_3_cumulative_proceeds.csv, 35 exact sale rows. data/frozen_35_sale_manifest.csv retains accounts, destination and ledger references. Decimal amounts are authoritative. Sort same-second entries by stored slot/index. Plot a step function, not interpolation. Add a pre-sale zero marker at launch, clearly distinguished from the first sale at that same timestamp-second; actual tx ordering resolves it.

**Axes:** x elapsed seconds/minutes since 17:18:06; y cumulative SOL/WSOL sale receipts. Range ends +40m22s at **606.331808740**. Annotate +3s **142.089113597**, +57s **251.752785673**, and +40m22s G16 largest sale **145.975602514**. Largest sale is the final jump, not the final cumulative total. Provide a first-minute inset so early sales remain legible.

**Caption:** Thirty-five verified case sales received 606.331808740 SOL/WSOL within 40 minutes and 22 seconds. The line sums sale receipts; it does not measure net profit, unique underlying capital or proceeds attributed to an identified person.

**Placement:** section 6. Source: frozen v0.71 35-sale manifest; ordering from already stored v0.112 record. No new transaction retrieval.

## Figure 4 — Documented Market Value vs Promoted Target

**Layout:** three labelled value panels or horizontal comparison bars: promoted target $10M; highest documented aggregator-candle initial-supply-normalized FDV $516,491.95 (~$516,492), 17:23:00–59; +60-minute proxy $5,312.93 (~$5,313), target 18:18:06, source candle 18:17:00–59. Do not connect these three points as a reconstructed time series. A separate inset may show G16 same-tx reserve price change, but must not mix reserve-price percentages and dollar candles on one unlabeled axis.

**Metric note:** token price × initial 1B tokens; not circulating cap, cash value or a verified exact lifetime ATH. Linear bars need numeric labels for the tiny proxy value; if log scale is chosen it must be explicit.

**Caption:** The documented high reached about 5.16% of the promoted $10M target within available coverage. Values use initial-supply-normalized FDV; the high is an aggregator-candle observation and the one-hour value is a preceding-candle proxy, not an exact target-second price.

**Placement:** section 7. Source: v0.109 definitions/ATH/dekking; v0.112 price response for any separate inset.

## Figure 5 — Where the Money Can Be Documented

**Layout:** top box **606.331808740 SOL/WSOL verified proceeds**, then **mixed seller balances: 606.331808740 SOL; CLEAN onward: 0 SOL**. Inside the mixed-principal accounting area, show **597.487092059 SOL conservative PARTIAL / RE-ESTABLISHED minimum**. Use a containing bracket/subset visual, not additive boxes or a clean-flow arrow.

**Category minima:** P1/CUo7/5B3 240.989588659; 6cn 188.148898454; F1dC 148.663295380; HFAc 7.723304078; unidentified intermediates 8.563794158. Category sum 594.088880729. A separate dashed accounting note is **joint-only unallocated minimum: 3.398211330**. It is not a wallet or a sixth receiving branch. Sum with category minima: 597.487092059. Do not use a Sankey suggesting exact allocations.

**Boundary:** terminate category boxes at a labelled **ATTRIBUTION BOUNDARY — no later mixed-collector payouts allocated to FACv**. Below that boundary, a disconnected conclusion box says **0 SOL attributed to a finally identified beneficiary**. No arrows to people, exchanges or a named beneficiary. The 8.844716681 difference from principal is uncertainty/cost room, not a separately discovered payment; only include as accounting annotation if needed.

**Caption:** Balance accounting establishes a conservative 597.487092059 SOL component in documented onward flows after seller-level mixing. These are lower bounds within mixed proceeds, not clean provenance or an exact terminal distribution. The joint-only remainder cannot be assigned to an individual category. Attribution stops here: 0 SOL is attributed to a finally identified beneficiary.

**Placement:** section 8. Source: frozen v0.89 seller joint-bounds/category table and v0.114 money assessment.
