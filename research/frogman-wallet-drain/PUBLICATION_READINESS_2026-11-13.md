> **current verification / 13 november 2026:** the previous live-access limitation is superseded by the [35-account audit](./audit_2026_11_13/README.md). all 35 receipts, exact account credits, fills and current balances have now been reconciled. the older text below is a historical checkpoint and must not be used as the current account-audit status. privacy cash withdrawal provenance, identity and native monero receipt remain unresolved.

# frogman / publication readiness review — 13 november 2026

**editorial status: ready for a bounded historical reconstruction; not ready for a claimed complete current balance / final destination report. no medium publication authorized or performed.**

## what the evidence supports

- the preserved npcsignals checkpoint dated 10 october (finding f0607) records ten independently reconstructed privacy cash deposits totalling **13,240.973780900 sol**. the provenance and withdrawal matching boundary must be preserved.
- the existing npcsignals v0.2 evidence reconstructs selected evm bridge settlements, six hyperliquid deposit credits totalling **561,850.214994 usdc**, and **205 xmr1 spot fills** spending **561,824.8582 usdc**.
- a separate mayan-linked account shows a **26,823.206875 usdc** matched credit and **28 xmr1 fills**; 47.146974 xmr1 net at the recorded checkpoint.
- the onchain files #014 ledger reports **35** hyperliquid accounts, **2,029,874 usdc** and **3,586.8 xmr1** as a **third-party historical report**, last checked **13 october 2026**. its 29 privacy cash withdrawals are *inferred*, not proven pool withdrawal matches. https://www.onchainfiles.io/files/014-frogman-token2049/
- 35 corresponding arbitrum explorer transaction links are now indexed in [primary transaction checks](./PRIMARY_TRANSACTION_CHECKS_2026-11-12.md); **do not mistake 35 hashes for 35 fully independently verified account histories**.
- two sampled receipts were reopened on 13 november: [arbi-21](https://arbiscan.io/tx/0xec3aa8fcd37f2fdaa0634fcb2b1ad3f825ef1f7b3f75d3b799f3408af3e5843b) and [arbi-35](https://arbiscan.io/tx/0xa970e51cfa2a4b189b544cca97704be36854a1867d1d14e33377e73cdc67f4b3). both show successful usdc transfers to the hyperliquid-labelled bridge, for **48,887.615010 usdc** and **41,827.339837 usdc** respectively. these are spot checks, not a full 35-row receipt audit.

## live verification limitation

on 13 november, direct api access from the execution environment to `https://api.hyperliquid.xyz/info` and `https://arb1.arbitrum.io/rpc` failed with dns resolution errors. the public web reader could access onchain files and arbitrum explorer pages, but **cannot issue the required hyperliquid post requests**. no first-party current spot balances, fills, ledger withdrawals or monero redemption were retrieved. do not claim xmr1 remains untouched in november.

## publication gate

| gate | status | editorial action |
|---|---|---|
| frozen original evidence preserved | pass | cite original 10 october checkpoint |
| reproducible historical case narrative | pass with limits | distinguish verified/supported/claimed/inferred |
| clear primary explorer examples | pass | use sampled tx links and full repo |
| third-party 35-address reconciliation | partial | attribute to onchain files, no new independently confirmed total |
| full receipt automation against arbitrum rpc | blocked | script exists, no successful run |
| live hyperliquid 35-account audit | blocked | no api response |
| november no-movement claim | **fail** | do not include |
| native monero redemption conclusion | **fail** | state not independently established at last verified checkpoint |
| identity or exploit method attribution | **fail** | unresolved |
| editorial copy and visuals | draft-ready | final fact-check and approval before medium |

## required wording

- **correct:** “our independently reproduced trail reaches selected hyperliquid credits and xmr1 purchases. a separate external report lists 35 accounts. the last independently reproduced npcsignals checkpoint is dated 10 october; the external monitoring page says last checked 13 october.”
- **incorrect:** “we verified all 35 hyperliquid accounts and confirmed that no xmr1 was redeemed as of 13 november.”
- **correct:** “we cannot cryptographically match privacy cash withdrawals to specific deposits based only on amounts and timing.”
- **incorrect:** “privacy cash withdrawals prove who received frogman's deposits.”
- **correct:** “xmr1 is a token associated with a potential monero redemption process; token purchases alone do not establish a native monero transfer.”

## final editorial decision

a **historical reconstruction with a transparent 13 november research-status note** is defensible for publication once the text, source links and diagrams receive final review. a **full current-status investigation** is not ready. the remaining live checks are material if the article's headline or conclusion depends on the present location of the funds.

## reproducibility and follow-up

- [original summary and evidence classification](./README.md)
- [visual evidence](./EDUCATIONAL_VISUAL_EVIDENCE.md)
- [trace tracker](./EVIDENCE_TRACE_TRACKER.md)
- [timeline](./TIMELINE.md)
- [external ledger comparison](./PHASE_2_EXTERNAL_RECONCILIATION.md)
- [receipt source ledger](./PRIMARY_TRANSACTION_CHECKS_2026-11-12.md)
- [read-only arbitrum verifier](./verify_arbitrum_receipts.py)
- [hyperliquid first-party verification limitation](./HYPERLIQUID_FIRST_PARTY_CHECK_2026-11-12.md)

**next reproducible milestone:** obtain an arbitrum rpc and hyperliquid info api response, capture raw timestamped outputs, verify all 35 receipts, map unique addresses to the seven earlier accounts, and compare fills and withdrawals against the historical checkpoint. update this gate before making any stronger current-status claim.
