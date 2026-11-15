# Order and delegated authorization

B: `0xe5686aae44d392aa6a0637fd38393859502f8667`.

The historical BNB settlement runtime at both target blocks matches byte for byte the chain-56 on-chain runtime returned by Sourcify's exact-match verified deployment. Sourcify reports direct GPv2Settlement, not a proxy, Solidity 0.7.6. The preserved source, compiler settings, ABI and runtime are in `sourcify_v2`. No local Solidity recompilation or deployment-state proof is claimed. This is a chain-specific check, not an assumption from the matching Ethereum address.

The domain separator is independently recomputed from name `Gnosis Protocol`, version `v2`, chain ID 56 and the deployed settlement address. It matches historical `domainSeparator()` value `0x0cbb18dfca28d2ceac8c72a17289168e03c1ad121338f5573e3b0c3255207fc7`. Verified-source order-field and flag semantics reconstruct both UID digests exactly, including the receiver, sell/buy token and amounts, expiration and metadata hash. Both orders use ERC-20 balances and fill-or-kill sell semantics. Source sell token and buy token are both canonical BNB USDT.

## First order: presignature

Actual trade flags are 96: presign scheme, with B's 20-byte owner address as settlement signature payload. This is not a 65-byte EOA signature on the order.

Frozen G011 transaction `0xf7e40d1d02ef78a0c9c898b31d466cb29918f91532eac712c88bff4c7b2afb2a` is B's nonce-5 type-2 self-call at block 127436947, 16:44:55 UTC. G011 preserves its valid outer transaction signature. New callTracer evidence shows successful B→token approve and B→settlement `setPreSignature(bytes,bool)`. The latter's calldata names the **precise executed first UID**, with true. Its matching PreSignature event identifies owner B.

Historical preSignature[UID] is zero at block 127436946; at 127436947 and settlement block 127436960 it equals keccak(`GPv2Signing.Scheme.PreSign`), `0xf59c009283ff87aa78203fc4d9c2df025ee851130fb69cc3e068941f6b5e2d6f`. The prior block's frozen code state is B's EIP-7702 designator to `0x63c0c19a282a1b52b07dd5a65b58948a07dae32b`. G011 independently recovered B from the BNB chain-56 authorization tuple, nonce 4, in the preceding type-4 transaction. G008's separate Ethereum signatures remain unchanged.

These observations confirm the selected delegated self-call's actual internal presignature effect and its use by order 1. The trace is provider-reexecuted evidence, not a consensus trace commitment. This improves the earlier no-trace limitation without repeating G011's signature recovery.

## Second order: EIP-712

Actual flags are zero; settlement calldata contains a 65-byte signature. Independent secp256k1 recovery over the recomputed chain-56 order digest returns B. Raw signature, r/s/v bytes, digest, full trade fields and owner are preserved in `settlement_order_register.json` (signature hex stores r[0:32], s[32:64], v[64]). No presignature is required for this executed order. G011's first presignature must not be generalized to the second order.

## Roles and conclusions

| Role | Evidence | Limit |
| --- | --- | --- |
| Order owner and first presign caller | B, UID encoding, event, state, trace | No human identity or legitimate purpose |
| Second EIP-712 signer | B, independent signature recovery | Does not establish consent |
| Settlement initiators/solvers | Route 1 `0x53227a6d5a129143b6ad760810ece62c79ab8e97`; route 2 `0x993118b07f47fae57379827ddb515ae3337893e4`; each matching Settlement event | Different solver keys do not imply different beneficial owners |
| Source buy receivers | Two unique deposit addresses listed in the order register | Service custody/routing addresses, not proven human identities |
| Intended and observed final recipient | B on Ethereum | Receipt proves account credit, not corporate ownership |
| Ethereum payout initiator | `0x2cff890f0378a11913b6129b2e97417a2c302680` | Network service association only |
| Delegated implementation | BNB designator to `0x63c0…e32b` | Code provider is not necessarily signing-key holder or beneficiary |

A receiver differing from the order owner is explicitly allowed by the verified order/settlement source and is expected in this deposit route. Technical signature validity, delegated execution, precise trade presignature and successful settlement are separate findings. None establishes the fifth question: legitimate human authorization. That remains UNRESOLVED.
