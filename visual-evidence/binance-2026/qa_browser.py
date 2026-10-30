#!/usr/bin/env python3
"""Read-only, reproducible NPCsignals Binance archive browser and ledger QA.

Run in this directory: python3 -B qa_browser.py
Requires: python3 -m pip install playwright ; python3 -m playwright install chromium
No network requests from the pages. Output: qa-output/ (screenshots + report).
"""
from __future__ import annotations
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "qa-output"
RESULTS = []

def check(label, condition, detail=""):
    RESULTS.append({"test": label, "pass": bool(condition), "detail": str(detail)})
    print(("PASS " if condition else "FAIL ") + label + ((": " + str(detail)) if detail else ""))

def main():
    OUT.mkdir(exist_ok=True)
    audit = subprocess.run([sys.executable, "-B", str(ROOT / "audit_archive.py")],
        cwd=ROOT, capture_output=True, text=True, timeout=50)
    check("offline audit runs", audit.returncode == 0,
          (audit.stdout + audit.stderr)[-1500:])
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        check("playwright installed", False,
              "pip install playwright && python -m playwright install chromium")
        return 1
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            for width, height, mode in [(390, 844, "mobile"), (768, 1024, "tablet"),
                                        (1440, 900, "desktop")]:
                page = browser.new_page(viewport={"width": width, "height": height},
                                        device_scale_factor=1)
                errors = []
                page.on("pageerror", lambda e: errors.append(str(e)))
                for filename in ("index.html", "flow.html"):
                    path = ROOT / filename
                    check(f"{mode} {filename} exists", path.is_file())
                    if not path.is_file():
                        continue
                    page.goto(path.as_uri(), wait_until="load", timeout=20000)
                    page.wait_for_timeout(200)
                    check(f"{mode} {filename} title", bool(page.title()))
                    check(f"{mode} {filename} main", page.locator("main").count() == 1)
                    check(f"{mode} {filename} no horizontal overflow",
                          page.evaluate("document.documentElement.scrollWidth <= innerWidth + 2"),
                          f"scrollWidth={page.evaluate('document.documentElement.scrollWidth')}, viewport={width}")
                    check(f"{mode} {filename} no JS exceptions", not errors, "; ".join(errors))
                    check(f"{mode} {filename} no missing local links",
                          page.evaluate("""() => [...document.querySelectorAll('a[href]')]
                          .filter(a => !/^(https?:|mailto:|#)/.test(a.getAttribute('href')))
                          .every(a => {
                            const url = new URL(a.getAttribute('href'), location.href);
                            return url.protocol === 'file:'; })"""))
                    page.screenshot(path=str(OUT / f"{mode}-{filename}.png"), full_page=True)
                    if filename == "flow.html":
                        for route in ("175", "80", "200"):
                            button = page.locator(f'button[data-route="{route}"]')
                            check(f"{mode} flow route {route} exists", button.count() == 1)
                            if button.count():
                                button.click()
                                check(f"{mode} flow route {route} pressed",
                                      button.get_attribute("aria-pressed") == "true")
                                check(f"{mode} flow route {route} populated",
                                      page.locator("#map-steps .step").count() >= 3)
                        page.screenshot(path=str(OUT / f"{mode}-flow-selected-200.png"), full_page=True)
                    if filename == "index.html":
                        buttons = page.locator("#eventbuttons button")
                        check(f"{mode} timeline controls", buttons.count() >= 5)
                        if buttons.count() >= 5:
                            buttons.nth(3).click()
                            check(f"{mode} timeline selection changes",
                                  buttons.nth(3).get_attribute("aria-pressed") == "true")
                    page.keyboard.press("Tab")
                    check(f"{mode} keyboard focus available",
                          page.evaluate("document.activeElement !== document.body"))
                page.close()
        finally:
            browser.close()
    failed = [r for r in RESULTS if not r["pass"]]
    report = {"test": "npcsignals binance archive full local browser QA",
              "timestamp_utc": datetime.now(timezone.utc).isoformat(),
              "status": "PASS" if not failed else "FAIL",
              "total": len(RESULTS), "passed": len(RESULTS)-len(failed),
              "failed": len(failed), "checks": RESULTS,
              "limitations": ["No live blockchain verification.",
                  "External HTTP links must be separately checked at publication.",
                  "Screenshot files need a human visual inspection."]}
    (OUT / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"RESULT: {report['status']}: {report['passed']}/{report['total']} checks. See qa-output/report.json")
    return 0 if not failed else 1

if __name__ == "__main__":
    raise SystemExit(main())
