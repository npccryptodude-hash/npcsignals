# Verification report — G005

Input review: both G001–G003 and G004 ZIPs read. Repository main baseline ac740cbac38273aef293ba4f88939c1ced1fc56e reviewed; filename search found no Gamdom research. No AGENTS.md found in checkout.

Evidence review completed:
- Original vxdb tally, provenance reply, two diagrams and THORChain image inspected in browser.
- Official company and founder original posts read; UTC timestamps taken from DOM datetime attributes rather than UI timezone. Company 2026-10-14 03:36:58 UTC; founder 16:43:53 UTC; vxdb tally 22:37:37 UTC; provenance reply 22:38:27 UTC. The US-Pacific UI displayed October 13 for the company post; earlier Norwegian screenshot date October 14 is consistent with UTC metadata.
- Six successful transaction receipts inspected on PolygonScan/Etherscan, including initial raw Transfer values and bridge payload/log amounts. Two payload hashes matched at both ends and checked against Axelarscan GMP mappings.
- Direct JSON-RPC retrieval unavailable; do not describe offline checks as independent chain re-execution.
- No historical USD valuation performed. No entire-network or complete-wallet audit claimed.

Offline validation: run `python3 verify.py`. It verifies complete manifest coverage (manifest excludes itself), SHA-256 hashes, CSV shape, unique transaction IDs, integer/decimal conversion, bridge pair membership/payload structure and no second counting of bridge hops in principal totals.

Publication policy: validated research checkpoint may be published; **article HOLD**. Confirm remote branch SHA and byte-equivalent checkpoint after push. Local validation does not itself prove remote publication.
