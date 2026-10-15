# Authorization verification

CONFIRMED offline cryptographic result: raw bytes from Etherscan's Get Raw Tx Hex UI were preserved in evidence/authorization_raw.hex. Keccak-256 equals the requested transaction hash. Strict RLP decoding and re-encoding agree. The authorization list contains one tuple, fully retained in evidence/authorization_verification.json.

- Outer chain ID 1, nonce 0, destination B, value zero.
- Authorization chain ID 1, nonce 1, implementation 0x63c0c19a282a1b52b07dd5a65b58948a07dae32b.
- Authorization yParity 1; r 0x9a32192d2fa65b116114672402860a55cba3a8b77a5dbdbcdbbcc9e0883f6436; s 0x764f846772ebe059db203ac946d10745a929cfbd6bef4472a7f6dba3ee55f232.
- Authorization digest 0x73c37d50a1a39a021d14f800a6e7b8ef6a29e1f8ea5fa2fcbf91ba4a5a58abac.
- Independently recovered authorization address and outer sender both 0xe5686AaE44d392aa6A0637FD38393859502F8667.

The script hashes 0x05 || RLP([chain_id, implementation, nonce]) for the authorization, and 0x04 || RLP(unsigned outer fields) for the outer signature. It verifies both recovered public-key signatures. This demonstrates valid signatures for B, not that an identified person knowingly approved them. A compromised key or induced signature remains possible; neither is proven.

## Historical code state
EIP-7702 processes authorization after incrementing the outer sender nonce, explaining authorization nonce 1 alongside outer nonce 0. The expected applied delegation indicator is 0xef010063c0c19a282a1b52b07dd5a65b58948a07dae32b. This value is a protocol-derived expectation, not a successful eth_getCode result.

Etherscan displays this authorization as valid and the transaction as successful. The dated receipt's calls and logs support application. Direct historical code reads at blocks 26184802/26184803 and an independently verified inclusion/state proof were not obtained. The explorer state view showed ETH and nonce changes, not code bytes. Its displayed Before nonce 1 is not substituted for transaction-prestate. Implementation runtime bytecode was visible on the current contract page; historical bytecode identity was not independently established.

Reproduce with verify_authorization.py and compare the saved deterministic JSON. Raw-transaction hashing does not by itself prove canonical-chain inclusion. Inclusion and receipt effects remain explorer-verified.
