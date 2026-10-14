# NPCsignals — 56HE USDT disposition and Binance-infrastructure receipt v1.0

Date context: 2026-10-14 UTC. Network: Solana Mainnet. Scope: the two specified accounts and their immediate returned transactions. No GitHub modification or provider contact. No U300 receipt analysis was repeated.

## Outcome

**CONFIRMED on-chain:** 56HE authorized **995.831502 USDT** from the specified receiving account into another SPL token account whose transaction-time owner is the exact **Binance-attributed 5tzFki…uAi9 public key**.

**SUPPORTED exchange affiliation:** two independent public sources, Bitquery and Solscan, identify the exact owner as Binance hot-wallet infrastructure. Direct official Binance confirmation of historical control was not obtained. **Customer credit, internal custodial sweep versus external deposit, customer identity and common human control remain UNRESOLVED.**

This is a new transactional route from a different documented case-network counterparty, not another U300 payment. Both branches reach the same independently attributed exchange infrastructure; they do not identify a common person or specific exchange account.

## New outgoing transfer — F004.outer:2

Complete signature:

`3QrJH49NS39jAtvEPn8BxCNGqkiwMZk1kSDJ2GU8f8jVU5GxVzxzd9bKSLx2KYkm7G6mPLP8Vsk3S94TuZMiayz2`

UTC: **2026-09-24 12:03:01**. Slot: **450023141**. Provider-reported transaction index: **81** (not independently checked through full block retrieval).

Instruction: **outer:2**, zero-based, SPL Token `transferChecked`.

| Role | Exact public key |
|---|---|
| Sender token-account historical owner / transfer authority | `56HEQykziUkwvpK5uPzFrRbGD4Ek8HdWgjgeDvNmDoEJ` |
| Source USDT token account | `CzissnPHhEu7NifSLfwhuvFMdfu7F8X4vR2HhF1o1PEL` |
| Receiving USDT token account | `CyBjGpte4Npi5zNkdtWumPxVW4kpMR8BuFSbA587xZES` |
| Receiving token-account historical owner | `5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9` |
| Fee payer / additional signer | `5JPAWfhLNsYVk3tPpD3gHvpHbvaXDbpUpy1wUfQVYRS2` |
| USDT mint | `Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB` |

Raw amount: **995,831,502**, six decimals = **995.831502 USDT**. Signer set: fee payer 5JPA and token authority 56HE. **14,000 lamports** network fee. Successful finalized receipt, separately verified with `getSignatureStatuses`.

The source and recipient historical owners appear identically in the receipt's pre/post token balances. No current ownership lookup is needed for this finding. The fee payer's affiliation and the purpose of its co-signature are UNRESOLVED; fee payment alone does not establish common control or exchange operation of the source wallet.

## Exact outgoing reconciliation

| Account | Before | After | Change |
|---|---:|---:|---:|
| Source token account USDT | 995.831502 | 0 | -995.831502 |
| Receiving token account USDT | 61,843,124.892138 | 61,844,120.723640 | +995.831502 |
| Fee payer SOL | 307.460059488 | 307.460045488 | -0.000014000 |
| 56HE owner wallet SOL | 0 | 0 | 0 |
| Source token-account native SOL | 0.001488440 | 0.001488440 | 0 |
| Receiver token-account native SOL | 0.002188548 | 0.002188548 | 0 |

No rent was withdrawn and no token account closed in this outgoing transaction. Native account-sum decline equals the fee. All remaining account native balances are unchanged. This is an SPL payment into the attributed owner's token account, not wrapping/unwrapping, a swap, bridge, staking operation or native-account drain.

## Starting receipt re-verification

The initial 56HE token account was created at 11:49:54, with explicit ATA wallet and inner initialization evidence for 56HE. The receiving historical owner is also present in token-balance fields. Both starting receipts were freshly retrieved with finalized commitment and separately successful finalized statuses:

| ID | September 24 UTC | Slot | Instruction | USDT |
|---|---|---:|---|---:|
| F001 | 11:49:54 | 450020165 | outer:4 | 4.028124 |
| F002 | 11:57:57 | 450021997 | outer:2 | 991.803278 |

F001 signature:

`45zVBfuvgtptBZuABucUsMiPHYQfG4pf4ium1629LREQyeFqCWF1rEh5VM5pVT4ukmYPPr3LDMbs7F6ku2RDg1kw`

F002 signature:

`64voUTp7NHZMZieXJDnJ1yNfMHaCN9GtNFP39AqQxcgS6QTKCeeGzmJgeB3qPmsAFNpzZky3c6kYcYjVAUQ81MUJ`

Both send from token account `8uKAGuxowd2eM4vfzgorTq9dCBZoeSNTpsmLhziziWfK`, historically owned by `6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N`. That exact case wallet is authority, sole signer and fee payer. Fees: F001 80,000 lamports; F002 79,938. F001 also funds 1,488,440 lamports rent for the receiver ATA; rent is separate from the USDT transfer.

The current public Exchange Attribution Ledger v0.1 documents this exact 6hR7 key as the shared ZYROX/GLITCH wallet and commingled GLITCH-route recipient. Its fresh read-only source snapshot and Git blob SHA are included. These September payments predate the token launches; no sale-proceeds origin is claimed or needed.

## Additional incoming funds and token-account continuity

Two small payments were made by a DIFFERENT address:

`6hR7yvr3V8igYCeiZaHpLh443kwKmgiiWL2DXk3ywv1N`

It is not the case wallet `6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N`. The shared abbreviated prefix/suffix does not establish a connection. Purpose and human control are not assessed.

| Event | UTC | Raw USDT amount | Token account balance after |
|---|---|---:|---:|
| F001 case receipt | 11:49:54 | +4,028,124 | 4.028124 USDT |
| F002 case receipt | 11:57:57 | +991,803,278 | 995.831402 USDT |
| F003 other incoming | 11:58:06 | +100 | 995.831502 USDT |
| F004 outgoing | 12:03:01 | -995,831,502 | 0 USDT |
| F005 later other incoming | 12:03:10 | +1,000 | 0.001000 USDT |

F003 signature:

`jTMFJTR1HttuuyKXwhEwYKUGy4htp6hwrfnh9tzmoB2TsZkUPBnpc9evhEisCCHtfAFXvCMUeyWGqtPB8YUm4Dn`

F005 signature:

`2tf6yfHRFNXnxS9bcssybjNETTT7Agv5CsUTBGutCcSxCQgpe2tUM1RBqtMvm8dESroqR3RnE8YcLuyd8todfF4v`

Their source token account is `C5dQZKbvM1Smtd8cyoMZjye4vat8ubDEPzJHw1hGLMvu`, historically owned by the distinct sender above. That sender is authority, sole signer and fee payer; each fee is 5,050 lamports. They were encountered solely through the specified account's receipt history, not by investigating their sender.

Full token-account reconciliation in raw units:

`0 + 995831402 + 1100 - 995831502 = 1000`

Thus the outgoing amount contains all 995.831402 USDT of the documented starting receipts plus the 0.000100 USDT earlier small payment. The later 0.001000 USDT remains in the last returned account snapshot. This is exact fungible-token balance accounting within the specified account, not attribution to a token sale, a person or a private exchange customer.

## Scope, null findings and classification limits

- Owner account-key history: **4 returned references**, followed by an explicit empty terminal page.
- Specified token-account history: **5 returned references**, followed by an explicit empty terminal page.
- Union: **5 unique receipts**, all retrieved directly as original JSON-RPC response bodies and separately confirmed successful/finalized. The starting large transfer appears in the token-account history but not the owner-key history; historical token-owner fields, not owner-key-only indexing, establish that receipt.
- No earlier returned account-key activity before the initial creation/payment. No later returned activity beyond the final 12:03:10 token receipt, through this capture. This is provider-returned history completeness for the two specified addresses, not a guarantee of every historic/closed token account associated with 56HE.
- No outgoing native SOL by 56HE, no swap, bridge, staking instruction or account closure in the five receipts. Eleven opaque instruction objects remain preserved (ten Compute Budget instructions and one unresolved DeJBGdM program instruction); no unsupported decoding was invented.
- Receiver historical SPL owner is CONFIRMED by receipt fields. Binance affiliation/hot-wallet function is SUPPORTED by two independent publishers, not officially confirmed by Binance at the September timestamp.
- Whether 56HE or 5JPA were Binance-controlled, customer deposit credit versus internal custodial sweep, customer/account identity and common private human control remain UNRESOLVED.
- No claim that fee sponsorship proves custody/control. No trace of Binance receiver history, fee payer history or any second-hop wallet was performed. No U300 receipts were retrieved or analysed.

## Attribution sources and next action

Bitquery: https://bitquery.io/investigations/libra-case-dismissed — exact owner appears in its own Binance hot-wallet table. Solscan: https://solscan.io/account/5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9 — exact-address page title Binance 2. Token account page: https://solscan.io/account/CyBjGpte4Npi5zNkdtWumPxVW4kpMR8BuFSbA587xZES — dynamic content did not independently expose the owner; finalized receipt provides historical owner proof.

The previous official-address publication gap is retained. This pass did not reopen completed U300 official-source searches. Public labels and historical token-owner fields do not prove the provider's internal customer assignment.

**Recommended next action:** add this new source-wallet/token-account transaction to the evidence submitted to an authorized investigator. Ask Binance to verify control of the receiving token account and owner at 2026-09-24 12:03:01 UTC, whether 56HE/fee payer belong to its operations, and whether the event was a customer credit, internal sweep or another booking, with relevant internal identifiers if legally disclosable. No request was sent. No new downstream chain investigation is required to establish this public transaction lead.

## Preservation and replay

Package includes original receipt envelopes and complete parsed results for five transactions; history pages, terminal empty responses and requests; finality responses; 28-row CSV/JSON instruction/fee ledger; token-flow ledger and account balance audits; source register and case-ledger snapshot; checksums and offline verification script.

Run `python3 verify.py` after extracting. Checksums, complete returned histories, successful finalized statuses, instruction correspondence, source and recipient token owners, authority/signers/fee payer and the complete token-account roll-forward are checked. Receipt/account arithmetic is independently reproducible from raw integers. The script does not cryptographically authenticate RPC responses, notarize source captures or establish exchange ownership/customer credit. Published-source observations are targeted metadata/excerpts and URLs, not full archived HTML. GitHub and all earlier evidence packages remain unchanged.
