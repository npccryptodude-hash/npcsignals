# Financial and cryptographic control assessment

## Exact address and key comparisons

| G010 identity | G011 evidence | What is established | What remains unproved |
| --- | --- | --- | --- |
| S1: 0x0067cc2416f792cf0ec5629f5506324ac508f859 | Four direct BNB USDT payments to B; earlier direct token activity. | Exact financial source and initiating key. Reconstructed BNB envelopes recover the identical public key as S1's saved G010 Ethereum payment to E1. | Gamdom ownership, private-key custodian, compromise or legitimate consent. |
| A: 0xd5fbda4c79f38920159fe5f22df9655fde292d47 | Full pre-existing BNB USDT balance paid to B in its nonce-zero transaction. | Exact source of the second deposit. Same recovered public key as A's G010 Ethereum DAI payment to E1. | Whether the first signed BNB transaction was malicious, treasury consolidation or rescue. |
| S2: 0x580450dff316ae00d0fbef9621a304020a046ce2 | No exact direct B canonical-USDT edge in this interval. | Bounded negative result. | An all-token, native, lifetime or all-chain absence claim. |
| E1: 0x4b304741599c125a244e498d14562487d7109ab8 | No exact direct B canonical-USDT edge in this interval. Existing G010 A/S1 payments to E1 are preserved. | The two recipient networks share exact A/S1 source addresses and their respective signing keys. | E1/B common ownership or one human operator. |

A and S1 recover **different** public keys. Each is consistent across the selected Ethereum/BNB transactions. This does not make the two source wallets one key, one human, or one company. Shared routers, solvers and delegation addresses add no standalone ownership evidence. No C/D relationship is newly established.

## B's source permissions and delegated execution

B directly approves 370000-USDT spending to 0x512000a034e154908efb1ec48579f4ffdb000512 twice, in nonce 0/1 transactions at 16:34:04 and 16:34:20. Both have matching signed approve inputs and Approval logs. The first bridge is nonce 2. Before that bridge B's historical code is empty; Ethereum G008's delegation cannot simply be assumed to apply to BNB.

G011 independently locates the BNB code change: code at block **127436780** is `0x`; at **127436781** it is `0xef010063c0c19a282a1b52b07dd5a65b58948a07dae32b`. The full transition block contains the successful type-4 self-transaction **0x87fae2f01950c2f3e25758e647e87bfd07088d616c545c97b5aec544e9876b02**, at **16:43:41**, transaction index 7. Its outer nonce is **3**. The one authorization tuple has chain ID **56**, nonce **4**, implementation **0x63c0c19a282a1b52b07dd5a65b58948a07dae32b**, and recovered authority **B**. Full r/s/parity/digest, reconstructed signed bytes and public keys are preserved in signature_verification.json. Both outer and authorization signatures verify and recover B.

The implementation address is an exact match to the address in G008's Ethereum record. This does not independently establish identical deployed bytecode across chains or a human operator. The binary search locates this observed transition under a single-transition search assumption, then verifies adjacent block states and the actual authorization transaction. It is not a lifetime code-history proof.

At 16:44:55 B initiates a type-2 self-call, **0xf7e40d1d02ef78a0c9c898b31d466cb29918f91532eac712c88bff4c7b2afb2a**, nonce 5. Its calldata contains batch execution with token approval and a settlement pre-signature operation; the receipt records B's maximum allowance to 0xc92e8bdf79f0507f65a392b0ab4667716bfe0110. Historical delegated code immediately before this block, the self-call and its effect support delegated execution. No complete internal call trace is obtained, so exact internal authorization paths beyond the signed input/receipt remain SUPPORTED rather than trace-confirmed.

At 17:43:43 B directly approves the exact second deposit amount to the bridge spender in nonce 8; nonce 9 performs the deposit. Spending permissions and valid signatures establish technical key-authorized instructions. They do not distinguish an authorized employee from an intruder possessing the same key.

## H1/H2/H3

| Hypothesis | Consistent evidence | Counterevidence / limits | Discriminating result |
| --- | --- | --- | --- |
| H1 unauthorized extraction | First-use B activation, concentrated large funding, prompt bridge/settlement spending, valid destination delegation and the exact cross-chain A/S1 source network. | All instructions are also valid treasury/rescue operations. S1 was already an active payout source; A's second-leg funds were held before the incident. No lack-of-consent evidence or compromised ownership proof. | UNRESOLVED. The financial path is established, unauthorized status is not. |
| H2 treasury or settlement | Active S1 history, pre-existing A holdings, exact approvals, settlements and same-address bridge receipts are compatible with consolidation. | No recurring pre-incident A/S1→B settlement relationship is demonstrated. B is newly activated within the observed window. | UNRESOLVED. A new destination can be legitimate; valid signatures do not establish business purpose. |
| H3 protective relocation | Rapid movement into B and subsequent cross-chain concentration could protect assets. | Active delegated spending and shared service infrastructure do not establish cold storage, protective custody or company-directed rescue. | UNRESOLVED. No custody/incident-response execution record distinguishes this explanation. |

Independent source attribution to Gamdom remains UNRESOLVED except for clearly labeled prior third-party associations. No explorer label is used as ownership or unauthorized-activity proof.
