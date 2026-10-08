# Relay verification checkpoint

Six source deposits and corresponding Arbitrum fills have been independently reproduced. Classification: CONFIRMED for the individual deposit/fill pairs. Exact totals: 212.499 ETH deposited and 561850.214994 USDC received on chain 42161.

The affected-wallet origin remains UNRESOLVED. These are downstream transactions linked deterministically to the Ethereum routing address, not a finding that every unit originated from Frogman's affected wallet.

Run `python -m pip install pycryptodome`, then `python verify_relay_pairs.py`. The script checks source transaction and receipt block hashes, block inclusion, successful status, the actual `depositNative(address,bytes32)` trace to 0x4cd00e387622c35bddb9b4c962c136462338bc31, exact wei and order ID, the matching Relay order response, and destination transaction/receipt/block inclusion. Each destination transaction includes the same order ID in calldata and a matching USDC Transfer event to the independently identified recipient. One destination fill is batched: its outer call is not ERC20.transfer. Token decimals were queried on Arbitrum and reproduced as six.

`relay_verified_pairs_v0.2.csv` records every source hash, order ID, request ID, fill hash, exact timestamp, destination, amount and observed transaction fee. A transaction fee for a batched fill is not automatically the fee attributable to this one order. Quoted/API fee components are not substituted for observed balances or network fees.

Provenance: deterministic order-level exchange linkage is reproduced; protocol liquidity is mixed. The record does not assert identical-coin continuity, shared beneficial ownership, or ultimate beneficiary. Subsequent Arbitrum activity is not yet reconstructed; the explorer query returned HTTP 403. That is an access limitation, not proof that no outflow exists.

The LI.FI source warning is preserved: bridge metadata does not guarantee the off-chain data associated with a Relay order. This investigation therefore does not use the LI.FI destination-chain field alone as a fill match.

The public ~212.5 ETH amount is reproduced at the precision of its public rounding (exact deposit total 212.499). It must not be promoted into confirmation of all other public route claims or of the source-wallet attribution.
