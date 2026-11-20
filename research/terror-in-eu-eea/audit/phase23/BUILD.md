# build and validation

Starting reference `d1f675eb785db712655c6952e43f3a57dd31f66c` on the existing research branch. Run from the repository root with Python 3.10+ and POSIX tools. No external packages or online requests are needed for the builds.

```sh
set -eu
root=research/terror-in-eu-eea
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
python3 "$root/audit/recalculate.py" > "$tmp/recalculated.csv"
cmp "$tmp/recalculated.csv" "$root/audit/recalculated.csv"
python3 -B "$root/audit/build_phase22.py" > "$tmp/annual.csv"
cmp "$tmp/annual.csv" "$root/data/phase22_annual_analysis.csv"
python3 "$root/audit/phase23/build_figures.py" --output "$tmp/figures"
diff -r "$tmp/figures" "$root/audit/phase23/figures"
python3 -B "$root/audit/phase23/verify_package.py"
```

Expected Phase 18 audit SHA-256 `fc351da07034e81754741f8fc3963855d62627747c84e366f634f9fcb5a6ab9f`. Expected Phase 22 analytical dataset SHA-256 `d88bbcae61083b791dc253f834d754767618f96e90c3d960ac41fa23ef02507d`. [Figure captions](FIGURES.md) identify exact data fields and sources and remain part of any reviewable export.
