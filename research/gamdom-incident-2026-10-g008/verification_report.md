# Verification report

## Completed verification
- Five new Polygon token-transfer receipts were inspected on primary explorer overview and decoded Transfer logs. This is receipt verification, not independent node verification.
- One existing delegation transaction gained new cryptographic verification: saved 979-byte raw signed envelope; hash matches the anchor identifier; strict RLP; one authorization tuple; low-s authorization signature; recovered B authorization address; recovered B outer sender; ABI batch decoded independently.
- Saved receipt Approval and PreSignature observations agree with decoded signed input. The explorer's advanced internal table shows the corresponding two calls.
- Exact integer sums, decimal conversion, unique hashes, timestamp/block ordering and preserved frozen files are validated by verify.py. The output is saved in verification_results.txt.

## Reproduction
Install the pinned requirements in an isolated environment, then run `python3 verify_authorization.py` and `python3 verify.py` from this directory. The second script expects the repository Git object for starting commit bc834822f0e4956fc78c1746eb958fecb290ef39. Python creates __pycache__; it is excluded from manifest enumeration and must not be published.

The SHA-256 manifest covers every published file except itself. It protects integrity, not chain inclusion or authorization legitimacy. No raw node receipt, proof or complete historical export is implied. Source observations are curated transcriptions, clearly distinguished from raw signed bytes.

## Resume inventory
At resumption GitHub main remained bc834822f0e4956fc78c1746eb958fecb290ef39. Local G008 contained only authorization_raw.hex. The successful earlier cryptographic output and five completed funding-receipt observations were preserved into the package, then reproduced offline. No G005–G007 investigation was restarted. Historical code and later traces are incomplete and are retained as explicit blockers.

## Publication checks
Publish only research/gamdom-incident-2026-10-g008/. After updating the remote branch, fetch it, compare every package byte against the published commit, confirm the diff adds only G008, and read back the README and cryptographic result using the GitHub connector. The final response must supply the verified remote SHA; this pre-publication report does not itself assert a successful push.
