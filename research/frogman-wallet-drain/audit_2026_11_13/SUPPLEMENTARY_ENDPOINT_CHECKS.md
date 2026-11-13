> subsequent resolution: [additional findings](ADDITIONAL_FINDINGS.md) links the 0.473-sol branch to a separate hyperliquid account and identifies the october 27 ethereum outflow. the descriptions below preserve the preceding scoped observations.

# frogman / supplementary endpoint checks / 13 november 2026

these are separate routes and must not be added to hyperliquid amounts. full source provenance retains the earlier route-specific limits.

## solana receiving wallet

a fresh finalized signature query for `69FnU8vszZSZF6DZCT6VHdsvm3DvvojDgbwqzHJ4cCFS` returned 26 entries (requested limit 1,000). latest returned signature is the previously recorded final privacy cash deposit on 6 october at 21:00:54 utc. its successful transaction was fetched again, reproducing the 1,258.973780900-sol inner deposit. fresh native balance is 0.006403163 sol at slot 468859595. this is a current native-balance observation, not a scan of all associated token accounts or a proof of private-pool withdrawal ownership.

## near intents destination / new onward evidence

the earlier verified destination `JA3iQS6ZSv6L2jhnKR2XMCJThJVorvNydUmYDf6Bwhs6` returned four finalized signature entries. all four successful transactions were fetched. the 44.473890045-sol settlement is followed by two outgoing native-sol amounts:

- 44 sol to `4PMiFg7qoEpqAMwEyZnM7xPqvNotGc6ihboAvp8PcKbk`.
- 0.473 sol to `7iGKnB9CSQLWsVX4V9Q9R61P3PFgJnLdyvPBvQutr5Gm`.

the first recipient forwarded 43.998506547 sol to `DjWN6eDmNcettEf3HWpQQYcQitmMAQvYRcrF9H78jggx`. the latter address returned the maximum 1,000 history entries: this is an explicitly capped, high-activity address boundary, not a complete history or an exclusive allocation of later spending. no operator or service label is assigned.

the second recipient also received a separate 0.015-sol payment. its later successful transaction invokes programs `3i5JeuZuUxeKtVysUnwQNGerJP2bSMX9fTFfS4Nxe3Br` and `99vQwtBwYtrqqD9YSXbdum3KBdxPAVxYTaQ3cfnJSrN2`; an inner transfer pays 0.473 sol to `7uTT8Xi5RWXzy7h9XL244GRgEycDYDhLjr3ZyNdXi8pZ`. protocol role, associated output assets and any cross-chain settlement remain unresolved: no amount-only bridge link is asserted. further completion requires decoding those program instructions/events against a pinned first-party interface and checking destination asset deltas.

lookalike-address small incoming payments appear in the histories and are preserved separately. address resemblance does not establish common control. the original near destination's current native balance is 0.000890035 sol at slot 468859614. this differs from simply treating its historical 44.473890045-sol settlement as an unchanged current holding.

[exact native transfers and source signatures](near_onward_transfers.json) · [raw transactions and request times](raw/).

## ethereum holding check

fresh ethereum state queries for the formerly dated 4-eth holding address `0x4521ef4df51a7689d4db5d8fc598685cb226ff58` returned 3.999999999994704 eth and nonce 1. the old nonce-zero / untouched snapshot must not be repeated as a current fact. a historical nonce search was performed to locate the outgoing transaction; see the separately retained results and request records. native balance and nonce alone do not explain the transaction or identify its beneficiary.

## remaining route refreshes

historical across, relay, mayan, chainflip, near intents, li.fi and robinhood protocol checks were rerun against retained evidence. new 25-route mayan and two chainflip api refreshes failed with http 403. this does not negate the old verified settlements, and it is not evidence of no newer activity. privacy cash withdrawal matching remains unresolved. further high-activity or protocol-specific outputs are not attributed by timing, address similarity or equal amounts.
