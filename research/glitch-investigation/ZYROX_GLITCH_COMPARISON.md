# ZYROX–GLITCH comparison v0.1

ZYROX reference: v0.122/U494 and prior v0.121/U493, at repository commit `a0f7ae3256d13c6e17bf110a880754a1004ece2c`. The frozen v0.114/U453 was not altered.

| Test | ZYROX verified reference | GLITCH finding | Conclusion |
| --- | --- | --- | --- |
| Creator-wallet equality | HZrAo creator, latest bundle table and frozen report | Ft2Xt creator; exact corpus comparison | No exact sampled actor match; OBSERVED bounded negative |
| Direct creator funding | Existing multi-layer launch-source documentation | Ten sources, each 0.240469594 SOL, full balance minus 5000 lamports | No exact source match in sampled comparison; deeper upstream NOT ASSESSED |
| Repeated actor signer/fee payer | HZrAo/Hp4q/Hrpa and documented relays | 71 selected signers/direct creator funders, including mint signer | Zero exact matches to reference corpus; does not exclude undiscovered actors |
| Historical Jito bundle | Four transactions, indices 1330–1333, slot 452029524, bundle bf5d…11ed | Five transactions, indices 598–602, slot 456113658, bundle 966d…fc92 | CONFIRMED distinct bundles; comparable ordered execution, no common submitter identified |
| Concentrated initial acquisition | Frozen ZYROX launch accounting | Six buyers acquired about 79% in first bundle | Comparable concentration; quantities are not controller identity |
| Funding fingerprint | v0.120/v0.121 full-balance forwarding, 5000 fee, zero endpoint balance, repeated low-value cycle | Ten initial creator funders reproduce first forwarding/fee/zero-balance pattern; later low-value payments seen in discovery but not fully reconstructed | INFERRED structural similarity only; complete network/repetition comparison UNRESOLVED |
| Multi-signer consolidation | Prior G16 seller consolidation evidence | Eight collector transfer receipts with 49 unique signers, including creator | CONFIRMED authorization structure; common beneficial ownership UNRESOLVED |
| Intermediate routing equality | Existing verified ZYROX routing corpus | Collector 8hiMX, DYxq and F2kh in selected receipt set | No exact sampled actor/destination link to case-specific routes established |
| Shared non-signing accounts | Jito tips and execution-payment destinations recorded in ZYROX | Exact matching infrastructure addresses in address_overlap.csv | Shared service/program appearance only; not case-control evidence |
| Stake withdrawal routing | Prior ZYROX stake withdrawal receipts to 6cn | Collector creates/withdraws stake account to F2kh | Comparable transfer mechanism; recipient equality/control not established |
| Kytro wallet control | Unresolved in latest ZYROX checkpoint | No independent wallet-to-human control proof | UNRESOLVED in both cases; off-chain promotion is not a signing-key attribution |

Exact match rows, source paths and scope are machine-readable in `data/address_overlap.csv` and `data/comparison_scope.json`. Corpus occurrence alone does not independently verify that account's role; service matches cannot supply a missing control link.
