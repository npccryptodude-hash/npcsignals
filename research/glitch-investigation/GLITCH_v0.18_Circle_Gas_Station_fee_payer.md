# GLITCH / ZYROX v0.18 — Circle Gas Station fee payer classification

Date: 2026-10-13. Evidence: user-supplied Work finalized RPC checkpoint and Circle documentation about Gas Station architecture. Exact 6nvUky listing in Circle address documentation was **reported by Work**, but not independently reproduced through search here.

## Transaction
Signature: `56DhD8nNeLGxNzsTNQDQAEymkAgpfayANggNKxN8K4rqrG7rC41PB7JxoPWkevv7QpWPpoV2yw7ETJbrXQhz8to2`
UTC 2026-10-03T19:51:05Z, slot 453032726, index 609. Finalized, meta.err=null.
- 159.006259 USDC, outer instruction 3, transfer authority and signer: `8HCSEeC98fR2BcDs8mkyiRq3ahSc7GNEqNEsW5oWote2`.
- Recipient token account `EfYzVpDkA9fQjJmytfWuqsNSgTBetS1u6rdtLgNx5rbD`; pre/post owner `AVUbPESe87nx9DqhJp2Xi5x8omd4bT9TRod9dk2P31yD`.
- Independent signer and fee payer `6nvUkyJG5j6rH3Hfm15mJNgPMJ1cxHQapfm5K3k647iv`; fee 10335 lamports; it is **not** the token transfer authority.
- Sender token balance 160.006259→1.000000 USDC. Recipient 849365.154798→849524.161057 USDC. Fee-payer native balance 15360432187→15360421852 lamports.
- Outer instruction 2 was createIdempotent, but recipient already existed and retained rent; no account closure.

## Circle service connection

Work reports 6nvUky and four additional 8HCSEe fee payer addresses explicitly listed by Circle for Solana Mainnet Gas Station. All 35 outgoing transfers in its checked ledger were sponsored by one of those five payer addresses; 6nvUky was present in eight observed 8HCSEe transactions, March 2025 to October 2026.

Circle official technical explanation: https://www.circle.com/blog/how-circles-gas-station-uses-fee-payers-to-enable-gasless-transactions-on-solana . Service fee payer signs to cover network costs separately from user wallet signing the token transfer. Independent technical explanation: https://solana.com/docs/payments/send-payments/payment-processing/fee-abstraction .

Classification: **CONFIRMED per Work's reported address-list matching**; technical fee sponsor interpretation **SUPPORTED**, and consistent with Circle's first-party service design. This GitHub checkpoint does not contain the original exact-address Circle list text, so first-party literal-match reproduction remains open.

## Attribution implications
6nvUky should be treated as a likely **shared service payer**, not a linked private operator. Its co-signing alone cannot be used to infer Circle, AVUb, 8HCSEe or ZYROX/GLITCH common control. Actual user/app initiating sponsored transactions remains unknown. No independent archival RPC of 6nvUky, no verified MEXC or other funding origin for 6nvUky in this pass.

Research direction: preserve Circle's exact versioned address list; investigate 8HCSEe/AVUb payer-controlled transaction authorities and their pre-existing finance/service connections, rather than interpreting common Gas Station sponsor as wallet-key reuse.
