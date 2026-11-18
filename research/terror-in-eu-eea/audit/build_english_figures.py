"""Rebuild and verify English SVG copies without changing geometry or numeric labels."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "phase23" / "figures"
TARGET = ROOT / "phase25" / "figures"
MANIFEST = ROOT / "phase25" / "figure_translations.json"
TAG = re.compile(r"<(title|desc|text)([^>]*)>([^<]*)</\\1>")
NUMBER = re.compile(r"(?<![A-Za-z])\\d+(?:[.,]\\d+)?")

def convert(source, pairs):
    replacements = dict(pairs)
    seen = set()
    def change(match):
        original = match.group(3)
        translated = replacements.get(original, original)
        if original in replacements:
            seen.add(original)
            if NUMBER.findall(original) != NUMBER.findall(translated):
                raise ValueError(f"numeric token changed: {original!r}")
        return f"<{match.group(1)}{match.group(2)}>{translated}</{match.group(1)}>"
    output = TAG.sub(change, source)
    missing = set(replacements) - seen
    if missing:
        raise ValueError(f"unused translation entries: {missing}")
    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify committed SVG bytes")
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for name, pairs in manifest.items():
        original = (SOURCE / f"{name}.svg").read_text(encoding="utf-8")
        expected = convert(original, pairs)
        destination = TARGET / f"{name}_en.svg"
        if args.check:
            actual = destination.read_text(encoding="utf-8")
            if actual != expected:
                raise SystemExit(f"FAIL: {destination}")
        else:
            destination.write_text(expected, encoding="utf-8")
        print(f"PASS: {name}")
    if args.check:
        print("PASS: all English SVGs reproduce byte-for-byte from originals and translation manifest")

if __name__ == "__main__":
    main()
