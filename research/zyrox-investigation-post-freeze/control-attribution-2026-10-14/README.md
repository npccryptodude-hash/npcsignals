# ZYROX / GLITCH — bounded control-attribution continuation

Research date: 14 October 2026 UTC. Baseline: `b21e5ec2467ff35cb06369d05f5170f5913a697e`. Additive continuation only; historical reports and frozen evidence are not altered. Research took substantially less than the 4–6 hour maximum; that limit was not treated as a minimum. No 384-file audit was repeated.

## Executive findings

**CONFIRMED:** The GLITCH transaction previously summarized principally as the creator's 70-million-token transfer contains **six source-authorized transfers totalling 116,513,762.335674 GLITCH**, with seven transaction signers and the receiving seller as fee payer. The five additional sources contribute **46,513,762.335674 GLITCH**. All six source token balances decrease to zero; recipient balance increases from 2,936,950.790841 to 119,450,713.126515 GLITCH. The seller pays **35,700 lamports once**, with no native balance change in the other six signers. This directly establishes multiparty transaction execution within GLITCH, not shared possession of their keys.

**CONFIRMED bounded negative:** None of the seven signers or the five first-returned funding sources has an exact address-text match in the two existing ZYROX research trees at the baseline. The five additional authorities have 96 returned finalized account-key references in total, all on 12 October; each pagination check returned an empty older terminal page. No September activity appears in those returned histories. This is not an exhaustive token-owner history or proof the keys did not exist earlier.

**UNRESOLVED:** Common operator between ZYROX and GLITCH. The newly identified GLITCH group does not establish a transaction-specific cross-case signer, fee payer or token-authority edge. Existing 6hR7/U300 routes remain financial-network connections. Human identities and beneficial ownership are unchanged.

## Phase 1: review and duplicate control

Reviewed the frozen main report/primary ledger; post-freeze v0.115–v0.122; GLITCH v0.1–v0.20 and launch/claim documentary checkpoints; Binance v2.0 README, reconciliation, five-transfer ledger, U300 inbound ZIP checkpoint, 56HEQ checkpoint, and independent audit report/results. `exact-address-comparison.json` pins the supplementary text-search inventory and hashes. The audit establishes archived file integrity/replay, not exchange customer identity.

Completed branches were respected: HFAc/99Gc attribution and mixed-funds boundary; FEaT/H85K; Hp4q funding fingerprint; IsItBundled/Proxima; BZ9m/8ySb bounded service test; confirmed historical Jito bundle U494. GLITCH historical 6hR7 payments, EnVAvXw correction, MEXC transfers and Circle fee-sponsor interpretations were not retraced.

U300 is `8zHcWujHhyJri3CRTcWUGmT5WSRdwW7xrns3WTTkPGvS`. Its four infrastructure-bound SOL transfers total 472.929423997 SOL. Three precede the ZYROX creator transaction; they cannot be subsequent launch proceeds. The October 14 transfer cannot be assigned exclusively to GLITCH because balances were mixed. Lifetime history was not completed in the prior 93,000-reference capture.

Case 6hR7 is `6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N`; 56HEQ is `56HEQykziUkwvpK5uPzFrRbGD4Ek8HdWgjgeDvNmDoEJ`. Their September 24 payments and 995.831502-USDT disposition predate both launches. The receiving historical owner is Binance-attributed infrastructure (SUPPORTED), not a proven customer deposit. The similarly abbreviated `6hR7yvr3V8igYCeiZaHpLh443kwKmgiiWL2DXk3ywv1N` is a different address. Sponsoring 56HEQ's fee does not establish ownership.

## Phase 2: exactly one selected lead

Selection: **C — critical-transaction authority comparison**, including the previously incompletely enumerated GLITCH consolidation signers and their first-returned funding receipts. This is a narrow continuation of v0.15's explicitly unassessed signer comparison, not reopening the old 6hR7 identity search.

| Candidate | Evidence / expected information | Feasibility / duplication | Decision |
|---|---|---|---|
| A: U300 historical graph | Confirmed mixed financial node; older pre-launch transfers already known; further counterparties do not necessarily prove control | Very large incomplete history; high fan-out and duplication cost | Not selected |
| B: 6hR7 / 56HEQ history | Historical relationships and sponsored transfer already reproduced; customer-booking question remains private | Completed specified-account histories; high duplication; exchange records needed for booking | Not selected |
| C: critical signer/authority roles | Falsifiable exact-key test at operational events; could reveal genuine cross-case co-authorization | Public named signatures; missing full GLITCH signer enumeration; small, reproducible scope | Selected |

These are qualitative judgments grounded in the reviewed record, not calibrated numeric probabilities.

## Bounded primary investigation

Provider: `https://api.mainnet-beta.solana.com`. Eleven successful jsonParsed transaction receipts were fetched using finalized commitment; separate getSignatureStatuses responses report all eleven finalized and successful. Six are validation/comparison anchors, five are newly examined first funding receipts. Five authority histories plus five empty terminal pages were captured. Original request and response bodies are preserved in `raw/`; write-time provenance is explicit.

The anchor transaction is `3ttmcRNck85nUEcnaTZ3nmMWpq9sAdCwjq8EF56Zz4wzsi3dz2AB1G18FibKKmqNzShVexFVanogoAUSJeJXojy1`, **2026-10-12T17:51:18Z, slot 456135125, outer:2–7**. Full authority keys, token accounts, integer amounts and shared transaction signers are in `new-evidence-ledger.json`. CA001–CA005 contain only the five additional source transfers; the already known creator's 70M transfer is excluded from new edge counts. CA006–CA010 record the five first-returned native-SOL funding receipts. Existing anchor revalidation appears only in the supporting ledger; it is not new research-edge inflation.

Signer/payer comparison of the ZYROX and GLITCH creator receipts gives different creator/mint signer pairs. Both creation receipts show the same non-transaction-signer mint authority `TSLvdd1pWpHVjahSpsvCXUbgwsL3JAcvokwaKt1eokM`, with mintTokens authority revoked at **inner:2.13**. That shared invocation-level authority is infrastructure context, not a shared private transaction signer. Its program-level ownership was not independently looked up here; no operator attribution is based on it.

## Control-attribution assessment and alternatives

- **CONFIRMED:** six GLITCH source token owners participate as transaction signers and authorize their own debits; seller signs and pays for the joint consolidation. Direct operational collaboration for that transaction is stronger than timing coincidence.
- **SUPPORTED:** coordinated GLITCH consolidation operation. A single builder/service or multiple cooperating holders could assemble a valid transaction with separately supplied signatures.
- **UNRESOLVED:** common human operator even within that group, and any common operator across ZYROX/GLITCH. Source keys retain separate debit authority; the seller's fee payment does not show it could independently debit the other owners.
- **CLAIMED:** External account/customer/operator allegations are not adopted or upgraded.
- **NOT ASSESSED:** private exchange booking/KYC, legal liability, malicious intent, full historic token-account discovery, formal multisig account configuration, off-chain coordination and second-provider RPC agreement.

Similar multiparty collection structures in both launches support a comparison of methods, not ownership. Shared infrastructure, independently cooperating holders, custody, aggregation of separately signed transactions, and different actors using the same tooling remain alternatives. GLITCH funding sources differ in this bounded comparison. The pre-existing 2025 6hR7 payment network and September 2026 exchange-bound events contradict interpreting every overlap as launch-specific coordination.

## Limitations and stop

Single RPC provider; status requests are separate but not provider-independent. No cryptographic authentication of RPC transport or block-signature validation. Account-key history does not find all closed/discovered token accounts; 96 history references were not exhaustively decoded. Address-text absence does not exclude undiscovered ZYROX activity. A zero first-returned recipient balance does not prove first-ever account use. Parsed `multisigAuthority`/`signers` fields are preserved without calling these wallets formal multisig accounts. No block transaction-order query was made, so same-slot follow-on ordering is not newly confirmed. Net profit, specific sale-token allocation and exclusive proceeds provenance remain unresolved.

Stop condition: the selected exact-key comparison is complete for its declared scope and yielded no cross-case control edge. Further arbitrary funding expansion would repeat graph tracing without a specific new control hypothesis. The broader attribution question is **not** declared globally exhausted. No private account access, customer contact, provider contact or unauthorized identification was attempted.

## Publication readiness and final decision

New evidence **materially strengthens the GLITCH coordinated-consolidation account**, expanding the documented source group from the highlighted creator transfer to six owners. It **does not materially strengthen common-operator attribution between ZYROX and GLITCH**. Publish the verified record with this additive finding, clear source limitations, and common operator/beneficiary explicitly unresolved. A factual transaction/claim analysis is ready; an article alleging common ownership or fraud is not supported. Exchange customer identity is not necessary for the narrower article.

**PUBLISH NOW** — the verified record supports a bounded factual article. The selected public test produced a useful GLITCH finding but no cross-case control edge; additional undirected history expansion has low expected attribution value. Reopen only upon a specific new primary authority, submitter or independently verifiable address binding.

Connections are not identities. Visibility is not verification. Absence of a cross-case finding is a valid result.
