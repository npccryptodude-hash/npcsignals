#!/usr/bin/env python3
"""read-only archive path, reference and checksum audit; standard library only."""
import argparse, hashlib, json, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
LINK = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
SKIP = ('http:', 'https:', 'mailto:', '#', 'data:')
def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True)
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output', default='research/archive_audit_report.json')
    a=p.parse_args()
    tracked=git('ls-files', '-z').split('\0')
    tracked=[x for x in tracked if x]
    missing=[]; links=[]; sha={}
    for name in tracked:
        f=ROOT/name
        if not f.is_file():
            missing.append(name); continue
        if name.startswith('research/'):
            sha[name]=hashlib.sha256(f.read_bytes()).hexdigest()
        if f.suffix.lower() not in ('.md','.markdown'):
            continue
        text=f.read_text(encoding='utf-8',errors='replace')
        for raw in LINK.findall(text):
            dest=raw.strip().split('#')[0].split('?')[0]
            if not dest or dest.startswith(SKIP): continue
            target=(f.parent/dest).resolve()
            try: target.relative_to(ROOT.resolve())
            except ValueError:
                links.append({'source':name,'target':dest,'status':'outside repository'});continue
            links.append({'source':name,'target':dest,'status':'exists' if target.exists() else 'missing'})
    protected=['research/gamdom-incident-2026-10/','research/evidence/binance-v2.0-2026-10-14/','research/zyrox-investigation/','research/frogman-wallet-drain/']
    result={'tracked_files':len(tracked),'research_sha256':sha,'missing_tracked_files':missing,'markdown_links':links,'missing_relative_links':[x for x in links if x['status']!='exists'],'protected_paths_for_manual_integrity_review':protected,'notes':['sha256 inventory is a file fingerprint, not a pass of project-specific verify.py scripts','remote website and medium inbound links are not covered','no source file is modified']}
    target=ROOT/a.output;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('tracked:',len(tracked),'links:',len(links),'missing:',len(result['missing_relative_links']),'output:',target)
    return 1 if missing or result['missing_relative_links'] else 0
if __name__=='__main__':sys.exit(main())
