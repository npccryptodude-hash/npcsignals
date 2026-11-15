#!/usr/bin/env python3
"""Read-only inventory, checksum, navigation and preservation audit.

Run from a full clone. No network access, acquisition or evidence writes.
The exit code is nonzero while known integrity/link exceptions remain.
Use --inventory FILE.csv to export the full tracked path/size/hash inventory.
"""
import argparse
import collections
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
BASELINE = '75fcb4966e4c21590cce363fcff2d94641d41257'
EDITORIAL_CHANGES = {
    'README.md', 'research/INDEX.md',
    'research/norway-welfare-infrastructure-2001-2036/README-no.md',
    'research/frogman-wallet-drain/PRIMARY_TRANSACTION_CHECKS_2026-11-12.md',
    'visual-evidence/binance-2026/audit_archive.py',
}

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inventory')
    args = parser.parse_args()
    paths = [p.decode() for p in git('ls-files', '-z').split(b'\0') if p]
    # Include newly created maintenance/navigation files before the first commit.
    extra = [p.decode() for p in git('ls-files', '--others', '--exclude-standard', '-z').split(b'\0') if p]
    paths = sorted(set(paths + extra))
    inventory = [{'path': p, 'bytes': (ROOT/p).stat().st_size, 'sha256': digest(ROOT/p)}
                 for p in paths if (ROOT/p).is_file()]
    groups = collections.defaultdict(list)
    for item in inventory:
        groups[item['sha256']].append(item['path'])
    manifests = []
    for name in paths:
        p = ROOT/name
        if p.name == 'SHA256SUMS.json':
            checks = json.loads(p.read_text())
            entries = [(p.parent/k, h) for k, h in checks.items()]
        elif name == 'research/zyrox-investigation/SOURCE_INTEGRITY.json':
            entries = [(p.parent/x['path'], x['sha256']) for x in json.loads(p.read_text())['files']]
        else:
            continue
        counts = collections.Counter()
        failures = []
        for target, expected in entries:
            state = 'missing' if not target.is_file() else 'match' if digest(target) == expected else 'mismatch'
            counts[state] += 1
            if state != 'match':
                failures.append({'path': str(target.relative_to(ROOT)), 'result': state})
        manifests.append({'manifest': name, 'counts': dict(counts), 'exceptions': failures})
    missing = []
    checked = 0
    for name in paths:
        p = ROOT/name
        if p.suffix not in ('.md', '.html'):
            continue
        text = p.read_text()
        targets = re.findall(r'!?\[[^\]\n]*\]\((<[^>\n]+>|[^\n]+?)\)', text) if p.suffix == '.md' else re.findall(r'(?:href|src)=["\']([^"\']+)', text)
        for target in targets:
            target = target.strip().split(' "')[0].strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path or '${' in target:
                continue
            checked += 1
            resolved = (ROOT if parsed.path.startswith('/') else p.parent)/unquote(parsed.path).lstrip('/')
            if not resolved.exists():
                missing.append({'document': name, 'target': target})
    original_paths = [p.decode() for p in git('ls-tree', '-r', '--name-only', '-z', BASELINE).split(b'\0') if p]
    changed = []
    removed = []
    for name in original_paths:
        p = ROOT/name
        if not p.is_file():
            removed.append(name)
        elif name not in EDITORIAL_CHANGES and p.read_bytes() != git('show', BASELINE+':'+name):
            changed.append(name)
    registry = json.loads((ROOT/'archive-maintenance/research-registry.json').read_text())
    index = (ROOT/'research/INDEX.md').read_text()
    missing_cases = [x['subject'] for x in registry if x['entry'] not in index or not (ROOT/'research'/x['entry']).is_file()]
    if args.inventory:
        with open(args.inventory, 'w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=['path', 'bytes', 'sha256'])
            writer.writeheader()
            writer.writerows(inventory)
    result = {
        'baseline': BASELINE,
        'tracked_and_new_files': len(inventory),
        'baseline_files': len(original_paths),
        'duplicate_byte_groups': sum(len(v)>1 for v in groups.values()),
        'manifests': manifests,
        'local_links_checked': checked,
        'unresolved_local_links': missing,
        'baseline_files_removed': removed,
        'unexpected_baseline_byte_changes': changed,
        'research_entries': len(registry),
        'missing_research_entries': missing_cases,
        'limits': 'local path existence and declared byte hashes; not external availability, source authenticity, full GitHub rendering or new scientific verification',
    }
    print(json.dumps(result, indent=2))
    return int(bool(missing or changed or removed or missing_cases or any(x['exceptions'] for x in manifests)))

if __name__ == '__main__':
    raise SystemExit(main())
