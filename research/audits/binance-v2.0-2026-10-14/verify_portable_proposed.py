"""Separate portability proposal; never replaces or writes original evidence.

Usage: python3 verify_portable_proposed.py /path/to/binance-v2.0-2026-10-14
Checks the pinned original verifier bytes, then executes its exact source with
one in-memory substitution: relative paths use as_posix() for manifest lookup.
This is a modified proposal run, not an execution of the unmodified verifier.
Python 3 standard library; no network calls. Do not run with -O.
"""
import hashlib,pathlib,sys

EXPECTED_ORIGINAL_SHA256='56ef79204924242f185463551e9f1f9c7ef3b78f9b6208332652d80b6352b60c'
if sys.flags.optimize:
 raise SystemExit('STOP: Python -O disables original verification assertions')
if len(sys.argv)!=2:
 raise SystemExit('Usage: python3 verify_portable_proposed.py EVIDENCE_DIRECTORY')
original=pathlib.Path(sys.argv[1]).resolve()/'verify.py'
raw=original.read_bytes()
if hashlib.sha256(raw).hexdigest()!=EXPECTED_ORIGINAL_SHA256:
 raise SystemExit('STOP: original verifier differs from audited commit; do not apply this proposal')
source=raw.decode('utf-8')
needle='str(p.relative_to(P))'
if source.count(needle)!=1:
 raise SystemExit('STOP: expected exactly one coverage-enumeration expression')
proposed=source.replace(needle,'p.relative_to(P).as_posix()',1)
print('PROPOSED PORTABLE RUN: exactly one in-memory path-format substitution; frozen file unchanged.',flush=True)
exec(compile(proposed,str(original)+' [portable proposal]','exec'),{'__file__':str(original),'__name__':'__main__'})
