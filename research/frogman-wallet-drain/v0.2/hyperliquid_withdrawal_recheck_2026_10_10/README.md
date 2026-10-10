# Hyperliquid withdrawal-only dated recheck — F0603

Base public checkpoint after funding-sender block: `554963adad68fffab14595885584a7d772542c24` (F0602). Added F0603 only; F0001–F0602 copied without edits into the additive timeline snapshot.

For the previously matched account `0x3e2d81f7a5659e4760ba929ef88eed40ef6640a1`, first-party `userNonFundingLedgerUpdates` was requested for the exact interval after previous cutoff 1791624537690 milliseconds. Start: 2026-10-10 09:28:57.691 UTC. End: 2026-10-10 09:42:59.270 UTC. The response was an empty array. No new external withdrawal was returned; no destination chain, address, asset or transaction can be supplied.

This is a dated endpoint observation, not permanent absence or proof covering every possible transfer mechanism. The existing XMR1 account boundary remains closed. No spot/perp fill reconstruction, unrelated account search, bridge-out reconstruction or native Monero claim was made. Beneficiary remains unidentified. Reopen only if a new external withdrawal is independently recorded.

Raw API response and access manifest preserve the exact request, capture times and outcome. Read-only collector is supplied; build and verification operate on saved responses. Frozen v0.1 and original F IDs were not edited. No article written.
