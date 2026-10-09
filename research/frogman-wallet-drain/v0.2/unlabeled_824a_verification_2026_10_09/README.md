# Unlabeled destination 0x824a — completed scoped block

Parent public checkpoint: `8ff43e352ba92e741b0ffa0fde8d98878c283304`. F0487–F0490 are additive; F0152/F0154 are reproduced, not rewritten or counted again.

Ethereum native path:

| Sender | Recipient | ETH | Classification |
|---|---|---:|---|
| 0x13afa986366ab4cd731ea6cc4b4c185527a1a48a | 0x824a50d903e13661f879a1055c3eb64583a2cebe | 18.5 | CONFIRMED inbound |
| 0x824a50d903e13661f879a1055c3eb64583a2cebe | 0x7da9dc31a143452ab40d3a8fb670eb5cd43c7226 | 18.499983905037284 | CONFIRMED forwarding |
| 0x7da9dc31a143452ab40d3a8fb670eb5cd43c7226 | 0x9be5b8a7314552fa47feb1355cd5b4adc7bb7516 | 18.499938758095934 | CONFIRMED new onward edge |

The ledger includes exact hashes, blocks, UTC timestamps, successful receipts and paid gas. Fixed-block RPC code is empty for all three recipients. The two forwarding accounts had zero balance before the case receipt; the second forwarder's balance immediately before its nonce-zero transfer equals its incoming case value and reconciles after paid gas. This establishes direct forwarding without using timing or similar amounts as the link. Empty code at these blocks identifies account type, not an exchange deposit or a private custody relationship.

The last recipient held ETH before the case arrival and had already sent transactions. Stop at this pooled-balance boundary: no later debit is assigned to case funds. Service identity, operator, common control, custody and beneficiary remain UNRESOLVED. Exact-address searches found third-party risk/label material but no independently adopted service evidence. Risk or sanctions labels are not findings of this block.

Blockscout address histories are contextual indexed evidence; the large boundary history is only a first page, not an exhaustive account audit. Small later transfers from lookalike addresses are distinct addresses and are not the actual 0x7da9dc31… forwarding account. Token spam and labels are not ownership evidence. NEAR status endpoint failures are access/status limitations, not proof that an address never used a bridge. No cross-chain conversion is established here.

Next documented candidate: 0x2625857ea267f4a1a150f6c9d6491b69d3bab324 (F0153/F0155); then 0x4521ef4df51a7689d4db5d8fc598685cb226ff58 (F0156). The 35 ETH LI.FI route F0170 remains a separate unresolved routing target. No final article was written.
