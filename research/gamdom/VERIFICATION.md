# verifying the moved gamdom archive

[case overview](README.md) · [checkpoint guide](CHECKPOINTS.md)

## what changed when the folders moved

all ten checkpoint folders are now under `research/gamdom/`. their files and local checksum manifests remain unchanged in this quality audit. several original scripts still refer to sibling folders with names beginning `gamdom-incident-2026-10`, and calculate the repository root using the previous depth.

running those scripts directly in the new location is therefore not a reliable portability check. replacing their paths in place would invalidate the frozen manifests.

## reproducible offline check

from a full git clone, using python 3 with `rlp`, `eth-keys` and `eth-hash[pycryptodome]` available:

```sh
python archive-maintenance/tools/verify_gamdom.py
```

the [compatibility runner](../../archive-maintenance/tools/verify_gamdom.py) creates a fresh temporary historical layout for each checkpoint. it runs the unchanged original verifier there, then discards the copy. acquisition scripts are not executed. the public evidence tree is not rewritten.

**observed result: nine of ten unchanged verifiers pass in the reconstructed layout.** the remaining original verifier, G009, checks regenerated table bytes. its receipt-file iteration is not explicitly sorted, so the `upstream_routes.csv` row sequence can differ between filesystems even when its records are identical.

## separately labelled proposal

```sh
python archive-maintenance/tools/verify_gamdom.py --row-order-proposal
```

this mode changes one verification assertion in memory for G009: compare complete csv row records independently of order for `upstream_routes.csv` only. original input hashes, every other generated file’s bytes and subsequent assertions are still checked. no original script or saved table is altered.

**observed result: all ten pass, with G009 explicitly identified as a proposed verifier run.** this is not reported as ten unchanged-verifier passes and is not a new blockchain verification. signatures, accounting and ownership conclusions retain their original stated scope.

individual checkpoint scripts remain historical originals. use this adapter from the repository root; do not run collection or packaging scripts to repair an integrity failure.
