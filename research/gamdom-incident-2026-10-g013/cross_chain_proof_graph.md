# Per-edge proof graph

The following sequence applies separately to each route. Transaction hashes, bridge nonces, receiver hashes, intent hashes and receipt IDs are different identifier types. Complete values and the source message bytes are in `message_identifier_register.json`, `source_deposit_proofs.json` and `near_receipt_proofs.json`.

| Edge | Route 1 | Route 2 | Verification / limit |
| --- | --- | --- | --- |
| BNB CoW settlement→unique source receiver credit | CONFIRMED, reused G012 | CONFIRMED, reused G012 | Exact canonical USDT Transfer in settlement receipt and signed order receiver. |
| Receiver→actual HOT locker deposit | CONFIRMED, new transaction | CONFIRMED, new transaction | Signed type-1 envelope, direct deposit calldata, canonical Transfer and NewTransfer event. Same full amount. Selected opening/closing token states are zero; this is not lifetime/exclusive token-identity tracing. |
| Locker message→NEAR deposit/mint | CONFIRMED, new proof | CONFIRMED, new proof | Exact nonce, chain 56, token bytes, amount and receiver hash; source historical stored digest; reconstructed message bytes; valid secp256k1 attestation under historical chain-56 key; successful NEAR deposit and mint. |
| NEAR mint→internal account | CONFIRMED | CONFIRMED | Receiver commitment is SHA-256 of exact compact deposit_call_args JSON; mt_on_transfer receipt and mint event credit that internal account. |
| Internal account→intent and wrapped-DAI withdrawal | CONFIRMED | CONFIRMED | Account-matched token_diff/ft_withdraw events and connected child receipts. NEAR receipt tree is authenticated through RPC execution status, not independently verified Merkle proofs. |
| OMFT withdrawal→Ethereum treasury payout | SUPPORTED | SUPPORTED | OMFT withdrawal_status explicitly maps the NEAR execution hash to the exact Ethereum transfer hash. 1Click independently exposes a corresponding endpoint mapping, but backend independence is unknown. Ethereum payment contains no withdrawal identifier. No signed treasury instruction was obtained. |
| Ethereum payout→B DAI credit | CONFIRMED, reused G012 | CONFIRMED, reused G012 | Canonical DAI transfer receipt/input; exact token sender, recipient and raw amount. |

**Full routes: SUPPORTED.** Every required edge would need CONFIRMED evidence for a full-route upgrade. A deterministic source deposit proof does not close the last treasury-payment boundary.

## Message reconstruction

The historically deployed BNB locker uses:

`SHA256(RLP([nonce:16-byte big-endian, chainId:8-byte big-endian, token:20 bytes, receiverHash:32 bytes, amount:16-byte big-endian]))`.

Integer fields use fixed-width byte strings inside RLP, not minimal integer encoding. Independently encoded bytes equal the historical getMessageRaw return bytes. Their SHA-256 equals deposits[nonce]; the preceding block returns zero. The chain-specific source and ABI come from Sourcify's chain-56 record, and the historical runtime matches its on-chain runtime bytes at both deposits. Current upstream MetaWallet source differs in guard logic and is not substituted for this deployed source.

Receiver commitments are SHA-256 of the exact UTF-8 compact JSON object with `account_id` then `msg`, where msg itself is the exact JSON string naming the internal intents account. The resulting hashes equal both BNB deposit receiver bytes. This binds the internal credit target without the 1Click status API.

The message binds source chain 56, nonce, token, receiver commitment and amount. It does not contain the BNB transaction hash, CoW UID, explicit destination chain ID, locker address or Ethereum payout hash. Its event/log position and historical nonce-indexed storage link it to the actual BNB deposit transaction. The historical NEAR get_locker_address(56) returns the same locker address.

## Architecture observed

BNB: deposit-address EOAs→MetaWallet locker. NEAR: HOT NEP-245 asset on v2_1.omni.hot.tg→intents.near internal balances→DAI OMFT token withdrawal/burn. Ethereum: plain DAI transfer by an EOA publicly documented by the protocol as its treasury. The observed path therefore mixes a signed HOT deposit bridge with an OMFT treasury payout. It is not demonstrated to be a single HOT withdraw call on Ethereum.

Official bridge documentation distinguishes HOT, POA and Omni bridge services; matching names do not establish identical implementations. Current treasury documentation names both observed service addresses, providing first-party operational attribution only. It is not Gamdom ownership, human identity or historical custody proof. No conclusion is drawn that every possible OMFT route lacks a cryptographic proof; this investigation did not obtain one for these two payouts.
