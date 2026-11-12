# research link and evidence-preservation audit

**audit date:** 12 november 2026  
**branch:** `chore/research-archive-restructure-2026-11`  
**scope:** links in `research/README.md` and selected checkpoint readmes  
**method:** individually request the exact `README.md` or named document through the connected github repository interface. a successful file retrieval confirms the document path exists; it does **not** validate every relative link inside that document. directory-only links are not automatically verified by this method.

## confirmed document targets

| archive entry | exact document checked | outcome |
| --- | --- | --- |
| frogman wallet drain | `frogman-wallet-drain/README.md` | confirmed |
| zyrox token investigation | `zyrox-investigation/README.md` | confirmed |
| gamdom checkpoints | `gamdom-case-index/README.md` | confirmed on working branch |
| binance evidence | `evidence/binance-v2.0-2026-10-14/README.md` | confirmed |
| democratic representation | `democratic-representation-stress-test-2026/README.md` | confirmed |
| presidential claims | `presidential-claim-stress-test-2025-2026/README.md` | confirmed |
| netanyahu un address | `netanyahu-unga-2026-claim-stress-test/README.md` | confirmed |
| demographic change and elections | `ddr-01/DDR01_ARCHIVE_SUMMARY_v1.2.md` | confirmed |
| tennessee execution protocol | `tennessee-execution-protocol-stress-test-2026/README.md` | confirmed |
| gen z protests | `gen-z-movements-evidence-archive/README.md` | confirmed |
| norway welfare infrastructure | `norway-welfare-infrastructure-2001-2036/README.md` | confirmed |
| ai performance narrative | `ai-performance-narrative-audit-2026/README.md` | confirmed |
| ibrahim traoré narrative | `traore-narrative-audit-2026/README.md` | confirmed |
| gamdom g005, g006, g008–g015 | each case `README.md` | confirmed individually |

## directory-only targets needing further investigation

| entry | result | action |
| --- | --- | --- |
| `zyrox-investigation-post-freeze/` | `README.md` not found; directory content not enumerated | retain directory link; inspect tree before renaming or creating an index |
| `glitch-investigation/` | `README.md` not found; directory content not enumerated | inspect tree and identify authoritative entry document |
| `authority-handover/` | `README.md` not found; topic and contents unverified | do not invent a description beyond the path label |
| `gcr-01/` | `README.md` not found; topic and contents unverified | inspect tree before assigning a readable topic name |

a missing `README.md` is **not** evidence that the directory is missing or empty. the connected file endpoint did not return a parseable directory listing, so these four entries remain **unverified**, not broken.

## source-backed descriptions and corrections

- `ddr-01`: demographic change and electoral competition across 15 selected countries; source is the v1.2 archive summary.
- `ai-performance-narrative-audit-2026`: evidence audit behind **distribution depth is not evidence depth**, including an online narrative about an autonomous grok trading claim. a generic ai benchmark description would be misleading.
- `traore-narrative-audit-2026`: claims about burkina faso under ibrahim traoré, compared against documented developments.
- `norway-welfare-infrastructure-2001-2036`: ten-year restoration of education, hospital and elderly-care infrastructure; not simply a general welfare review.
- `tennessee-execution-protocol-stress-test-2026`: specific christa pike case and execution-protocol evidence; do not generalize its scope.
- `presidential-claim-stress-test-2025-2026`: falsifiable presidential claims and their supporting or contradicting evidence.
- `democratic-representation-stress-test-2026`: political voice, governing power, institutions, information integrity and representation; not a single democracy ranking.

## do not move without verified integrity and link dependencies

| source | evidence preservation concern |
| --- | --- |
| `gamdom-incident-2026-10/` (g005) | g006 source explicitly states g005 integrity verification covers all descendants; avoid adding files inside frozen tree |
| `gamdom-incident-2026-10-g006/` | frozen sibling checkpoint with historical references |
| `gamdom-incident-2026-10-g008/` through `-g015/` | versioned checkpoints explicitly depend on prior preserved directories; g012 says 196 earlier files unchanged |
| `evidence/binance-v2.0-2026-10-14/` | archived evidence package with offline verification and preserved transport objects |
| `zyrox-investigation/` | frozen technical basis and linked post-freeze record |
| `frogman-wallet-drain/` | dated verified checkpoint and publicly referenced evidence path |
| `gen-z-movements-evidence-archive/` | public research archive, likely externally linked; check before moving |
| `norway-welfare-infrastructure-2001-2036/` | frozen research package; preserve provenance and publication links |

**rule:** freeze status alone does not prove moving changes file hashes; however path-sensitive scripts, manifest coverage, cross-checkpoint relative references, and public permalinks can fail. treat these paths as protected until tests establish a safe migration.

## outstanding checks

1. obtain a complete recursive git tree listing and record file hashes.
2. identify exact files in gcr-01, authority-handover, glitch and zyrox post-freeze.
3. scan all markdown links and scripts for path dependencies and published inbound references.
4. verify every link in the navigation index, including directory-only targets.
5. execute offline integrity checks before and after any proposed move.
6. review a path-by-path migration diff; do not change main without approval.

**audit status: partial, source-checked; not a complete repository-wide link audit.**
