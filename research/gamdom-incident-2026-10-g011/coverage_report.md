# Coverage and reproducibility

## Continuation boundary

G010's route/coverage/blocker and wallet registers establish the two BNB bridge deposits but leave upstream USDT unresolved. G005/G006/G008/G009 are relevant as frozen A/B/C/D financial, authorization and bounded-holdings context. They are not restarted. G010 supplies the two existing bridge receipts/transactions/headers and the saved Ethereum A/S1 transaction objects used for a new cross-chain key comparison. No old transaction is counted as newly verified. All 168 tracked files across the five prior evidence directories are compared byte-for-byte with the starting commit.

## B canonical token interval

Contract 0x55d398326f99059ff775485246999027b3197955 only. Historical symbol returns USDT; decimals returns 18. Two eth_getLogs filters, B in Transfer sender and recipient topic respectively, cover **127400000–127444806 inclusive**, October 13 **12:07:45–17:43:53 UTC**. They return **four outgoing and five incoming events**. Duplicate event keys are not summed twice. The narrower initial query covers 127430000–127435562 and agrees with the overlapping records.

This is a complete returned bounded canonical-event reconstruction with measured zero opening balance at block 127399999, not a lifetime export. Blocks before 127400000 and after 127444806, other tokens, native transactions and nonstandard transfers are outside that ledger. No claim that B never held tokens earlier is made. Earlier history is unnecessary to account for these later debits because the directly measured opening balance is zero; the deeper history itself remains uncollected.

Historical B balances are queried at opening, before/after both bridge blocks, and the zero-balance boundaries around the two settlement debits and A's payment. The anchor blocks each contain only one returned canonical B event, so ordered-log reconstruction aligns the pre-block state with the observed pre-transaction debit. This is not an independent transaction-local state replay or state-root proof.

## Source windows

S1: three 10000-block queries plus a final smaller query cover **127400000–127432896**, from 12:07:45 through the first B payment at 16:14:31. The combined sender/recipient export contains 178 unique canonical events. S1's opening and closing archive balances reconcile exactly. The earlier comparison ends at 127429999, before 15:52:48; it includes a few minutes of the third-party 15:50 incident window and is described as an earlier intraday comparison, not an entirely pre-incident control sample. The receipt at 12:11:04 separately confirms activity clearly before the reported window.

A: five bounded chunks cover **127200000–127444207** with zero returned canonical events, starting October 12 at 11:06:45. Balance at 127199999 already equals the later payment and is unchanged at 127399999 and 127444207. The payment at 127444208 drains it to zero. Earlier provenance is not reconstructed. A's nonce-zero BNB payment does not imply the account had never received funds.

All nine B event hashes have receipt/transaction/header context: seven are new transfers/settlements and two bridge hashes are imported from G010. Two additional source-history receipts, four approval/control receipts and the newly located BNB delegation produce **14 new successful transactions**. The much larger event export is not represented as 178 independently receipt-investigated transactions.

## Providers and exact failed attempts

NodeReal's publicly shareable endpoint supplies historical state, bounded logs and receipts. Official public-key documentation: https://docs.nodereal.io/reference/getting-started-with-your-api. The initial Ethereum-public-key URL also accepts BSC calls; a subsequent BSC-documented public-key URL returns matching pre-bridge balance. Both URLs use NodeReal infrastructure and are not two independent state providers.

BNB's Binance public endpoint returns missing trie node for the historic balance call. It and the separately addressed bnbchain endpoint successfully corroborate the first S1→B and A→B receipt fields/logs. One intervening receipt request returned HTTP 502 and is preserved as a failure. The Tenderly bnb URL returned 404; dRPC returned 403. None are empty-history results.

An initial S1 query exceeded the provider's 50000-block range and returned -32602. A subsequent 50000-block request returned 502; smaller 10000-block windows succeeded. Unretrieved earlier S1 ranges are not described as empty. BNB Chain's own documentation states that eth_getLogs is disabled on its listed mainnet endpoints: https://docs.bnbchain.org/bnb-smart-chain/developers/json_rpc/json-rpc-endpoint/. G011 resolved that limitation through another provider rather than repeating G010's explorer challenge.

## Cryptography and delegated code

Fourteen newly collected BNB signed envelopes and two frozen Ethereum envelopes are independently reconstructed from RPC fields, hash-checked and signature-verified. The BNB type-4 authorization has its own independently recovered authority. Reconstructed bytes, signature values, digest and recovered public key are saved. These checks validate cryptographic content, not legitimate human consent. Code-state calls and the full located transition block are preserved; no complete B lifetime code scan or internal trace is claimed.

## Preservation and precision

rpc_archive.json.gz stores 136 original parsed acquisition records, including JSON-RPC/HTTP failures, without deleting local originals. It is not a raw HTTP wire archive. source_register.json lists endpoint, full parameters, collection timestamp and canonical-record SHA-256. The manifest covers all published top-level files except itself. Raw quantities remain integer strings with 18 decimals. No current balance, rounded explorer valuation, media label, inferred missing transfer or floating-point sum is substituted for historical evidence.

One successful archive provider supports the state/log accounting. Receipt corroboration uses another provider; consensus replay, state-root verification and Merkle inclusion proofs were not performed. No human, company ownership, original compromise instruction or verified unauthorized USD loss is established.
