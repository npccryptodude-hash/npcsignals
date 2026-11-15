# NPCsignals — Gamdom G006

Independent Historical Behavior & Recipient Control Audit — 15 October 2026.

Frozen starting checkpoint: `2a67eaa900e7137c5230a080cf5b2f4207c0822a`. G005 files are unchanged. This is a sibling versioned directory because G005's integrity script covers all descendants; placing G006 inside it would invalidate its frozen manifest.

## Strongest independently reproduced findings
1. On Polygon, B funded A with 20 POL at 17:56:30 UTC on October 13. A's two G005 token outflows followed 58 and 64 seconds later with transaction nonces 0 and 1. These are its first ordinary sender transactions on Polygon, not an established pattern of routine outgoing payments.
2. Before that, a transaction initiated and paid by C (`0xaCc0c1f672B03B9a5fED4535f840f09B85f40E98`) swapped funds through Squid and delivered 148.787119217835216906 native POL to B. The same C later initiated two Ethereum operations delivering DAI to B. This is repeated direction of financial operations to B, not proof that C controls B's signing key.
3. A also sent B 10,456.137361559383267328 BUSD on Ethereum at 17:45:23 UTC. B later spent exactly that quantity through Squid, receiving 10,346.405126060613426143 DAI. This is an additional independently verified A-to-B movement on another chain.
4. The observed Ethereum DAI ledger has a net positive change of 816,635.912748421658923307 DAI before G005's first Ethereum arrival. Following G005's second arrival, four more DAI inflows total 21,072.036962590546379139 DAI. No later nonzero canonical DAI outgoing event appears in the displayed history. This does not prove the opening balance, exhaustive absence of other events, or an ultimate beneficiary.
5. Lookalike addresses and noncanonical token contracts imitate earlier amounts in third-party initiated transactions. These rows are excluded from behavioral and financial attribution. A token log's `from` field does not identify the transaction signer.

**36 new transaction receipts inspected** beyond G005, including native funding, approvals, delegation and contamination checks. This is not 36 theft transactions. There are 38 selected transfer records and 10 control records; transaction fees must be deduplicated by chain/hash.

## Decision
Evidence checkpoint: PUBLISH. Article: **HOLD**. The record establishes financial links and an activation sequence, but does not distinguish unauthorized extraction from legitimate or protective relocation. No human identity or beneficiary is attributed.

Read `coverage_report.md` before interpreting absence or frequency. This is a coverage-limited explorer reconstruction, not a complete raw-chain export or a scored anomaly model.

Run `python3 verify.py` for integrity, G005-preservation, exact arithmetic, duplicate checks and evidence-classification validation. See `verification_report.md` for what those checks do and do not establish.
