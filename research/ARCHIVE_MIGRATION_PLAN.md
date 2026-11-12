# archive restructuring — migration plan

**status:** planning / non-destructive working branch  
**scope:** public npcsignals repository only; private sentinel repository excluded  
**baseline:** `main`; changes are not approved for merge

## verified observations

- `research/README.md` now provides a consolidated navigation layer.
- `research/gamdom-case-index/README.md` links the existing gamdom case directories without moving evidence.
- `research/frogman-wallet-drain/README.md` preserves a dated frozen checkpoint and distinguishes independently verified records from later external comparison.
- `research/zyrox-investigation/README.md` references a separate post-freeze archive and integrity manifest.
- root `README.md` contains historical research links. these must be tested before modifying paths.
- a complete recursive tree inventory and full external-link audit have **not** yet been completed.

## proposed destination taxonomy

```text
research/
  01-crypto-investigations/
    binance/
    frogman/
    gamdom/
      cases/
    glitch/
    zyrox/
  02-politics-and-power/
  03-society-and-institutions/
  04-methodology-and-audits/
  05-visual-evidence/
  99-archive/
  README.md
```

this is a proposed logical structure, not a claim that these directories already exist.

## migration controls

1. inventory every tracked path, its blob hash, size and relative references.
2. enumerate inbound links from markdown, manifests, website and published medium articles.
3. preserve all frozen checkpoints, original evidence and source identifiers.
4. produce a complete old-path → new-path map, including the gamdom g006–g015 case series and binance root-level evidence documents.
5. check whether each old directory needs a compatibility index; note that git cannot preserve a directory-level redirect automatically.
6. make moves on this branch only, in small, reviewable commits.
7. validate path existence, internal links, referenced manifests, hashes and evidence totals after each move.
8. obtain explicit approval before merging into `main`.

## migration register — provisional

| current path | proposed destination | status |
| --- | --- | --- |
| `research/gamdom-incident-2026-10-g006/` | `research/01-crypto-investigations/gamdom/cases/g006/` | pending dependency audit |
| `research/gamdom-incident-2026-10-g008/` through `-g015/` | corresponding `gamdom/cases/g###/` | pending dependency audit |
| `research/gamdom-incident-2026-10/` | `research/01-crypto-investigations/gamdom/` | pending collision and dependency audit |
| `research/frogman-wallet-drain/` | `research/01-crypto-investigations/frogman/` | pending published-link audit |
| `research/zyrox-investigation/` and `research/zyrox-investigation-post-freeze/` | `research/01-crypto-investigations/zyrox/` with separate checkpoint sections | pending manifest and link audit |
| `research/evidence/binance-v2.0-2026-10-14/` and root-level binance/exchange documents | `research/01-crypto-investigations/binance/` | pending complete file inventory |
| `research/gen-z-movements-evidence-archive/` | `research/03-society-and-institutions/gen-z/` | pending published-link audit |
| `research/norway-welfare-infrastructure-2001-2036/` | `research/03-society-and-institutions/norway-welfare/` | pending published-link audit |

## release gate

**no-go for physical moves** until the recursive inventory, old-path mapping and inbound-reference checks are complete. navigation-only changes are permitted because they do not remove existing source paths.

## editorial policy

new editorial content uses lowercase. maintain evidence-first language. do not convert third-party claims into confirmed findings or alter conclusions during structural work.
