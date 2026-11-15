# Exact remaining blockers and closed leads

## Closed source boundary

The BNB deposit→NEAR credit boundary is now reconstructed without relying on 1Click: two actual locker deposits, matching nonce-indexed message digests, identical NEAR call parameters and receiver commitment, and valid deposit signatures under historical chain-56 HOT public keys. Full source message bytes, signatures, public keys and deterministic checks are preserved.

## Open payout boundary

Both Ethereum payout senders have empty historical code and call canonical DAI transfer directly. The payments execute no observed HOT withdrawal-verification contract and carry no receipt ID, intent hash, deposit nonce or signed bridge payload. OMFT status independently names both destination hashes using the NEAR execution hashes, but this is a primary service index, not an authenticated treasury instruction. A signed/countersigned OMFT payout record binding the exact NEAR withdrawal receipt to the exact Ethereum transaction was not obtained.

No conclusion is drawn that such a record does not exist. The public SDK snapshot exposes bridge deposit APIs but no authenticated payout-instruction retrieval. OMFT service root returns 404. Read-only withdrawal_status probes succeed by NEAR transaction hash and fail by action receipt ID. Preserve the latter as bounded negative query results; they do not disprove the withdrawals.

## Signature authority limits

The historical HOT contract returns a chain-56 public key that verifies both deposit signatures and a locker address matching the observed source contract. This establishes the historical getter-state/key association and valid signatures. The internal Rust implementation, MPC validator roster, threshold, quorum transcript and global replay controls have not been independently compiled/audited. The BNB locker withdrawal verifyAddress is a different key and must not be substituted for the NEAR deposit-attestation key. No OMFT payout signature or authorized signer set was obtained.

## Technical limitations preserved

Legacy NEAR archival calls hit HTTP 429; FastNear's supported archival alternative completed the receipt/code/state work. Some exploratory getter schemas returned input-deserialization errors, preserved verbatim. No missing historical data are filled with current balances. API numeric amount fields are lossy and excluded from exact arithmetic. Current protocol documentation supplies operational context, not proof of 13 October deployment source or company ownership.

Ethereum internal traces remain unavailable after two providers and two trace interfaces: Tenderly HTTP 429; PublicNode debug_traceTransaction -32601; PublicNode trace_transaction HTTP 403. All responses are retained. No hidden calls or payout instructions are invented from these failures.

## Highest-value next lead

Locate a publicly retrievable OMFT treasury payout instruction or relayer receipt keyed to withdrawal action receipt `79y1EMdKhP2AgryCjgjmJnMo4rTxs59mM78kWkmcSCsZ`, then verify whether its signed bytes bind that receipt to Ethereum `0x6b282435dc06107a499c8b8ef0ed83632a51d32738d81c143dc7e2d53542fd40` under a historically authorized payout key. This targets the weakest edge directly; another amount/time match would not close it.

Evidence checkpoint publication is justified by two new locker transactions, authenticated deposit-message reconstruction and 24 expanded receipt records. Full routes remain SUPPORTED; Medium and X HOLD.
