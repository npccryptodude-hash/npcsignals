# frogman / confirmed findings and open questions

## confirmed within the recorded scope

35 successful usdc bridge transfers; 35 exact account-credit matches; 537 xmr1 buy fills; token fees and current balances reconciled on every account. original ten privacy cash deposits remain reproduced. historical route checks are retained with their original provenance qualifications. identities and attack mechanics are separate questions.

## unresolved and concrete completion requirements

| question | actual work / obstacle | what would resolve it |
|---|---|---|
| do particular privacy cash withdrawals belong to the case deposits? | external time/amount clustering reviewed; no deterministic match | protocol-specific verifiable linkage or independently authenticated disclosure; a larger timing sample alone is insufficient |
| all 25 externally listed solana → mayan routes? | all 25 source signatures extracted; all 25 current official explorer-api lookups returned http 403, preserved individually | permitted api access, retained first-party order records, or source/destination order-event reconstruction with exact recipient and amounts |
| current chainflip API refresh? | both known swap-id lookups returned http 403; original origin/api/settlement verifier passed offline | functioning documented status endpoint; separately trace destination-wallet history before claiming a new terminal location |
| newer native monero redemption? | all 35 returned ledgers inspected; current xmr1 balances reconcile; no returned token outflow or withdrawal | actual redemption request/settlement evidence; no private service record was obtained, no native monero output verified |
| exhaustive hyperliquid history? | returned counts below pagination thresholds; separate recent-window checks; no consensus or archival replay | independent historical node/archive replay if stronger absence/lifetime claims are needed; api documentation limits available fills to 10,000 most recent |
| 41-account public claim? | no complete corresponding address inventory retrieved | full list, inclusion criteria and dated primary account records; compare exact addresses before changing totals |
| november compromise-method reporting? | newer e27 contribution and syndicated articles inspected; no device forensic report, police case document or authenticated new victim technical disclosure obtained | original evidence showing causal link to this case, rather than generic attack possibilities |
| recovery / freeze / returned funds? | no case-specific authenticated recovery proof found in inspected sources | transaction and recipient confirmation or authoritative case-specific statement |
| upstream funding explorer-label integrity? | one preserved html response fails historical checksum; associated offline verifier fails | resolved as lf/crlf conversion: reconstructed bytes match the original digest and isolated verifier passes; original byte mismatch preserved |
| whole mixed evm balance provenance? | earlier route-specific verifiers rerun; mixed-balance boundaries retained | transaction-specific additional funding/exit evidence; no fifo or equal-amount attribution |

## access attempts

arbitrum official rpc, publicnode, drpc, meowrpc and blockscout returned http 403 during probes; 1rpc returned 405; llamarpc returned 503; ankr required an api key. tenderly and onfinality returned chain id 42161. tenderly supplied all 35 successful receipts, transactions and containing blocks. hyperliquid supplied current first-party data, superseding the earlier dns-blocked status. initial probes were exploratory; the successful evidence queries and later failed mayan/chainflip attempts have individual retained manifests. no access failure is an empty history.

## new reporting source register

- [e27 contribution](https://e27.co/hackers-drain-us4m-using-fake-wi-fi-at-major-crypto-conferences-20261106/): discusses conference attack scenarios. classified claimed, not a verified explanation of the frogman compromise.
- [lookonchain relay of that story](https://www.lookonchain.com/feeds/81213): points back to e27 and explicitly qualifies reported allegations. it is not an independent forensic confirmation.
- [tokenpost november report](https://www.tokenpost.com/news/technology/52772): attributes further statements to frogman; original supporting disclosure was not reproduced in this audit. claimed.
- [the defiant linked article](https://thedefiant.io/news/hacks/trader-frogman-drained-of-4-million-on-the-first-morning-of-token2049): retrieved view exposes an older incident summary, not new device/police evidence proving the november mechanism.
- [onchain files original](https://www.onchainfiles.io/files/014-frogman-token2049/): raw page preserved in `external.txt`; monitor still reports 13 october. independently reproducing its published account set does not independently prove its private-pool attribution.

## editorial use

publish the verified account results and explain the unresolved private-pool link. do not state that the full reported four-million-dollar loss is audited, that every xmr1 unit is exclusively victim-owned, that a specific person operated the accounts, or that fake wi-fi caused this compromise. no contact with subjects, fund transaction or medium publication was performed.

## additional concrete boundaries

- new 27 october mayan order: current official status lookup timed out. the expected solana recipient is decoded from ethereum calldata, and a mayan payment to that recipient is reproduced; independent order-state/pda correspondence is still needed before labeling the cross-chain link confirmed.
- the approximately 4-eth source balance increased after its recorded spend. blockscout native-history lookups returned 403; trace-filter attempt is retained separately. exact incoming transaction allocation remains unresolved.
- one new solana endpoint has a capped 1,000-entry history; another combines three funding sources in one transaction. full index pagination or transaction-specific protocol evidence is needed before allocating later spending.
- the 0.473-sol branch was subsequently resolved through first-party relay records, an identical on-chain event/calldata field, arbitrum receipt and a separate hyperliquid credit; it is no longer an unidentified-program-only boundary. [additional findings](ADDITIONAL_FINDINGS.md).

native return-history trace lookup: `trace_filter` for the ethereum holding address returned http 429. full requests and the failure time are retained in `raw/eth_source_return_trace_filter.error.json`. an accessible native-transfer index or an archival provider with that method and sufficient query allowance is required to identify the later incoming transaction(s).
