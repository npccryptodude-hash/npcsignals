# Claim-specific attribution matrix

| Wallet | Technical role | Organizational attribution | Key/control evidence | Authorization status |
|---|---|---|---|---|
| A `0xd5fbda4c79f38920159fe5f22df9655fde292d47` | CONFIRMED source to E1 and B, Ethereum/BNB/Polygon | UNRESOLVED: explorer labels are third-party assertions | CONFIRMED selected A signatures and same A key across Ethereum/BNB; no source-wide permission history | UNRESOLVED |
| S1 `0x0067cc2416f792cf0ec5629f5506324ac508f859` | CONFIRMED Ethereum E1 and BNB B source | UNRESOLVED: labels/inventory do not authenticate Gamdom control | CONFIRMED selected direct signatures, same S1 key Ethereum/BNB; different key from A | UNRESOLVED |
| S2 `0x580450dff316ae00d0fbef9621a304020a046ce2` | CONFIRMED Ethereum E1 source | UNRESOLVED | CONFIRMED receipt transaction initiator; independent signature recovery NOT ASSESSED here | UNRESOLVED |
| E1 `0x4b304741599c125a244e498d14562487d7109ab8` | CONFIRMED receiving/converting account | UNRESOLVED | Transaction initiators preserved in G010; human operator UNRESOLVED | UNRESOLVED |
| B `0xe5686aae44d392aa6a0637fd38393859502f8667` | CONFIRMED recipient and settlement/order owner | UNRESOLVED | CONFIRMED selected signatures, Ethereum/BNB EIP-7702 authorizations; first BNB order presigned, second EIP-712 | UNRESOLVED |

## Historical comparison

S1 Ethereum baseline: 308 canonical USDT outflows to 217 recipients, maximum 300251.911353 USDT; 268 USDC outflows to 158 recipients, maximum 1800000 USDC. No prior E1 payments in that returned token sample. G015 compares selected incident maxima in historical_behavior_baseline.json. The incident USDT and USDC individual maxima do not exceed these earlier maxima. This defeats a size-only abnormality claim within this bounded comparison; it does not prove normal intent. Frequency distributions, gas funding and organizational withdrawal purpose were not independently established.

S1 BNB earlier intraday canonical sample: 63 outflows, 49 recipients, maximum 30039.043168179440000000 USDT. The 315446.159624488300000000 payment exceeds that sample maximum. The comparison extends to 15:52:48 and overlaps the reported window; it is not a wholly pre-incident baseline or proof of theft. A and S2 have no comparable canonical outflows in the selected Ethereum baseline, so a meaningful value anomaly test is unavailable. Account nonces establish activity, not ownership or historical business purpose.

## Permission interpretation

B changed execution permissions during the incident window. Ethereum authorization chain 1/nonce 1, outer nonce 0; BNB authorization chain 56/nonce 4, outer nonce 3. Both designate 0x63c0c19a282a1b52b07dd5a65b58948a07dae32b. G008 Ethereum code application was initially explorer-supported; G011 BNB historical code transition was directly read. Preserve those distinctions. Outer key, delegated implementation, solver initiator, order owner and human operator are separate roles. No attributable human signing authority or consent is established. B's new approvals do not retroactively explain source-wallet employee permissions.
