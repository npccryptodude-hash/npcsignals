# Methodology

Labels: CONFIRMED = independently reproduced receipt or exact calculation; SUPPORTED = evidence supports attribution/interpretation but direct underlying proof incomplete; CLAIMED = public assertion; UNRESOLVED = question pending; NOT ESTABLISHED = evidential threshold not reached in examined material.

CONFIRMED receipt status does not confirm human identity or unauthorized intent. Ledger classifications apply to the stated on-chain event only. Provenance words: intact = deterministic link; mixed = multiple source components share balance; probabilistic = heuristic only (none used here); broken = no deterministic onward linkage established. These words are separate from evidence labels.

Use finalized Solana JSON-RPC getSignaturesForAddress and getTransaction/jsonParsed, maxSupportedTransactionVersion=0. Preserve raw amounts, decimals, inner instructions, signers, account owner fields, fees, errors, logs and balances. Transaction blockTime is the chain's recorded time; do not substitute file capture or search crawl time. Within a timestamp-second use slot and transactionIndex if strict ordering matters; current captured events have distinct times.

Failed transactions commit no token movements but still pay fees. Ledger fee columns repeat metadata across rows; sum network fee action rows only. Intermediate DEX route movements are not separate disposals. Native SOL and WSOL are separate accounting measures. USD valuations are left blank absent valuation evidence. Unknown mints are retained by address. Mint debit-credit discrepancy is not automatically trading slippage.

Program identity: Privacy Cash mainnet ID matched to primary project README and Rust declare_id. No bytecode equivalence/build verification or historic upgrade analysis was performed. Router addresses remain exact even if names are provisional.

No wallet clustering from address resemblance, timing, proximity, a single common funder or protocol fee payer. Signer, token authority and beneficial owner are distinct concepts. No compromise vector inferred from fund flow.
