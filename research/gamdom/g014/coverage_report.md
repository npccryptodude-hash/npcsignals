# Bounded coverage

New chain work is limited to historical OMFT source metadata and omft.near factory code/account snapshots/method-availability probes at the two relevant NEAR blocks. G013's captured token WASM and G012's Ethereum objects/receipts are reused solely to test source provenance, code exports and destination signature scope. No historical fund-flow search is restarted.

Repository checks: near/intents current tree and pinned token/factory source blobs; dated historical commits for the older poa-token path and its pre-reorganization source; a defuse-sdk commit selected before the incident cutoff and its package/client dependencies; bounded public repository searches for omft, chaindefuser and near poa-bridge. These searches do not prove repository or archive absence. The historical SDK commit returned is dated August 2025; it is a published client snapshot available before the incident, not proof of the production client's exact October 2026 version.

The pinned SDK dependencies @defuse-protocol/internal-utils 0.1.2 and @defuse-protocol/bridge-sdk 0.10.0 were downloaded. Their package tarball SHA-512 integrity values match the captured npm registry records. Static client files were inspected without installing or executing package code. This establishes artifact integrity against the registry value, not publisher identity or authentication of any actual payout. The withdrawal_status typed response carries mappings/status, without a signature/attestation field in that version. The service may implement additional behavior.

No undocumented mutating endpoint was invoked. The historical get_withdrawal calls use the actual receipt IDs only as method-availability probes; the historical runtime fails before argument deserialization. The current source's 20-byte caller-digested identifier is not guessed from 32-byte NEAR IDs. No one was contacted.

Two existing Ethereum EIP-1559 transaction signatures are newly recovered offline and their complete signed envelopes hash-matched. This adds two cryptographic verifications, zero new transaction identities. No new fees or balances are acquired. No independent source-to-WASM rebuild, MPC audit, global replay analysis, source-request census or backend-provenance audit is claimed.

The archive retains every new successful and failed response, exact HTTP response text or binary base64, timestamps and URLs. Prior unsuccessful trace/provider work remains frozen in G013 and is not repeated. Every source record has a canonical SHA-256; every published file is covered by the manifest except the manifest itself.
