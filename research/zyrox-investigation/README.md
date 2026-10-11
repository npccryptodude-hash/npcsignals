# ZYROX evidence repository

NPCsignals examined the launch structure, case-related selling, promotional claims and documented movement of sale proceeds for ZYROX on Solana.

**Status:** Ongoing investigation. This repository is updated as new evidence is independently verified and reviewed.

**Mint:** `FACvJMFBWQ1GYm9dgZ7XHvs85V1EcK2SqHf534kspump`

**Frozen technical basis:** v0.114 / ledger U453. Repository preparation does not add research, ledger entries or evidentiary reclassifications.

## Latest investigation update

Post-freeze research has materially strengthened the launch-infrastructure finding.

At checkpoint **v0.121 / U493**, all **10 of 10 examined Hp4q funders** still reproduce the same transaction-construction fingerprint: four batch inflows, full-balance forwarding minus exactly 5,000 lamports, zero ending balance, a second low-value cycle roughly 35 minutes later, and short ten-transaction wallet histories.

The launch-funding network is now verified one layer farther upstream. BZ9m funded all four documented BZ9m child wallets in the same transaction and was the sole signer and fee payer for those transfers. The common upstream wallet `8ySbR18…PLv2` funded all seven relevant direct-source wallets in the same ten-recipient batch, and the same structure repeated at low value roughly 35 minutes later.

The evidence now establishes a **coordinated multi-layer launch-funding network and repeated operational template at the transaction-structure level**. No common external signer, fee payer or authority across the separate relay wallets was established, and no exchange, custody or service attribution was established. The current upstream evidence boundary is `8ySb`, an unlabeled signer wallet with activity concentrated in the launch window.

This does **not** establish shared private keys, common beneficial ownership, a real-world operator identity, final beneficiary, or a definitive ZYROX–Kytro control link. Beneficiary/control attribution and definitive ZYROX–Kytro on-chain control remain unresolved.

Latest post-freeze checkpoint: [ZYROX BZ9m Service Boundary v0.121](../zyrox-investigation-post-freeze/ZYROX_BZ9m_Service_Boundary_v0_121.md).

Further investigation is ongoing and any later verified checkpoint may refine this summary.

## Read the evidence

- [Verified main report](report/ZYROX_Main_Report_v1_1_Verified.md)
- [Technical evidence report](evidence/ZYROX_Devsold_verification_v0_2.md)
- [Evidence guide](evidence/EVIDENCE_GUIDE.md)
- [Transaction links](evidence/TRANSACTION_LINKS.md)
- [Frozen 35-sale manifest](data/frozen_35_sale_manifest.csv)
- [Claim screenshots and captions](evidence/claims/CAPTIONS.md)
- [Public account continuity note](evidence/ACCOUNT_CONTINUITY.md)
- [Figures](figures/) and [datasets](data/)
- [Repository QA](REPOSITORY_QA.md) and [SHA256 integrity manifest](SOURCE_INTEGRITY.json)

## Evidence standards

**CONFIRMED** means a directly verified transaction, control or accounting fact at its stated scope. **SUPPORTED** means multiple concrete evidence lines support an explanation without establishing it conclusively. **UNRESOLVED** means the available evidence does not establish the finding.

The frozen assessment is **SUPPORTED COORDINATED OPERATIONAL STRUCTURE**. Joint authorization does not prove common ownership; funding does not prove control; shared routing does not prove a common operator. Timing and matching amounts do not prove ownership.

The inventory records 17 case-relevant sellers, 35 FACv sales and 606.331808740 SOL/WSOL in verified receipts. Gross sold is trading volume, not unique supply. Sale receipts are revenue, not net profit.

All verified proceeds passed through mixed seller balances. CLEAN onward provenance is 0 SOL; the conservative PARTIAL / RE-ESTABLISHED minimum is 597.487092059 SOL. This lower bound does not establish a final beneficiary. **0 SOL attributed to a finally identified beneficiary does not mean nobody benefited.**

A common operator, common beneficial owner, final beneficiary, intent, legal fraud and a definitive ZYROX–Kytro on-chain control link remain unresolved. The ZYROX and Kytro on-chain cases remain separate.
