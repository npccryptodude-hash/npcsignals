#!/usr/bin/env python3
"""Run frozen verifiers in disposable historical layouts, without editing evidence.

Requires a full git clone, Python 3, rlp, eth-keys and eth-hash[pycryptodome].
No acquisition scripts are run. --row-order-proposal is a separately labelled
G009 verifier proposal; it is never presented as an unmodified verifier pass.
"""
import argparse
import csv
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

REPO = Path(__file__).resolve().parents[2]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--row-order-proposal', action='store_true')
    args = parser.parse_args()
    if sys.flags.optimize:
        raise SystemExit('verification requires assertions: do not use python -O')
    results = []
    checkpoints = sorted(p for p in (REPO / 'research/gamdom').iterdir() if p.is_dir())
    for checkpoint in checkpoints:
        # Each verifier gets fresh copies: G009 regenerates files as part of its test.
        with tempfile.TemporaryDirectory(prefix='npc-gamdom-verify-') as tmp:
            root = Path(tmp)
            (root / '.git').symlink_to(REPO / '.git', target_is_directory=True)
            research = root / 'research'
            research.mkdir()
            for entry in (REPO / 'research').iterdir():
                if entry.name != 'gamdom':
                    (research / entry.name).symlink_to(entry, target_is_directory=entry.is_dir())
            for original in checkpoints:
                old = 'gamdom-incident-2026-10' + ('' if original.name == 'g005' else '-' + original.name)
                shutil.copytree(original, research / old)
            old = 'gamdom-incident-2026-10' + ('' if checkpoint.name == 'g005' else '-' + checkpoint.name)
            script = research / old / 'verify.py'
            command = [sys.executable, str(script)]
            mode = 'unmodified verifier in historical layout'
            if args.row_order_proposal and checkpoint.name == 'g009':
                # Only unordered table row presentation is relaxed. Hash checks,
                # every other output byte and all downstream assertions remain.
                original = script.read_text()
                needle = "assert prior=={n:(R/n).read_bytes() for n in generated}"
                if original.count(needle) != 1:
                    raise SystemExit('unexpected G009 verifier source; proposal not applicable')
                replacement = '''after={n:(R/n).read_bytes() for n in generated}
    for n in generated:
        if n == 'upstream_routes.csv':
            def canonical(b):
                return sorted(json.dumps(row,sort_keys=True) for row in csv.DictReader(__import__('io').StringIO(b.decode())))
            assert canonical(prior[n]) == canonical(after[n]), n
        else:
            assert prior[n] == after[n], n'''
                proposal = root / 'proposal.py'
                proposal.write_text('source=' + repr(original.replace(needle, replacement)) + '\n' +
                                    'exec(compile(source,' + repr(str(script)) + ',"exec"), {"__file__":' +
                                    repr(str(script)) + ',"__name__":"__main__"})\n')
                command = [sys.executable, str(proposal)]
                # imports are resolved against the untouched historical script directory
                env_path = str(script.parent)
                mode = 'proposed verifier: CSV row-order-only comparison for G009'
            else:
                env_path = str(script.parent)
            proc = subprocess.run(command, cwd=script.parent, capture_output=True, text=True,
                                  timeout=120, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1', 'PYTHONPATH': env_path})
            results.append({'checkpoint': checkpoint.name, 'mode': mode, 'exit_code': proc.returncode,
                            'stdout': proc.stdout, 'stderr': proc.stderr.replace(str(root), '<temporary-root>')})
    print(json.dumps(results, indent=2))
    return int(any(x['exit_code'] for x in results))

if __name__ == '__main__':
    sys.exit(main())
