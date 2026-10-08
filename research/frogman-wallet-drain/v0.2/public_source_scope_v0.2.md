# Public source scope

Protocol documentation consulted on 8 October 2026:

- https://docs.relay.link/references/api/get-requests-v2 — documented hash and orderId lookup; public v2 endpoint, reduced rate limits. The richer v3 endpoint requires authentication. No credentials were repurposed or acquired.
- https://docs.relay.link/references/api/get-requests — confirmed v3 authentication requirement and distinction between request identifiers and transaction lookup fields.
- https://docs.robinhood.com/chain/connecting/ — official chain 4663 RPC and explorer; corresponding request/response saved as rh_network_docs.
- https://github.com/lifinance/contracts/blob/main/src/Facets/RelayDepositoryFacet.sol — preserved source of depositNative routing and warning about off-chain order metadata.
- https://github.com/lifinance/contracts/blob/main/src/Interfaces/IRelayDepository.sol — preserved ABI interface.
- https://jupiterz.jup.ag/docs/faq and https://github.com/jup-ag/rfq-webhook-toolkit — earlier recovered primary protocol identification evidence.

Exact public-wallet searches included the two supplied EVM addresses, Relay request lookup documentation, LI.FI Relay facet source and official Robinhood RPC/explorer documentation. Generic Relay searches returned unrelated services; those were not used for bridge attribution. Search-result visibility is not evidence of relevance.

This resumed run prioritized on-chain EVM and bridge reproduction. It did not complete a new post-8-October recovery/freeze/law-enforcement or compromise-vector review. Do not interpret that unexamined scope as proof that no development occurred. Earlier frozen public claims remain claims except for the narrowly reproduced transactions/amounts identified in the report.

Program source retrieved from current main is a source snapshot, not a historical deployed-bytecode audit. Primary transaction traces and events, rather than source naming alone, establish the recorded movements.
