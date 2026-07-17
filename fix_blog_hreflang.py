#!/usr/bin/env python3
"""Fix blog hreflang/alternate links: /lang/blog/slug -> /blog/slug-lang.

The blog translation files physically live at /blog/slug-lang.html, but the
generator wrote alternate/hreflang links as /lang/blog/slug.html (404).
Google indexes those 404s. This rewrites them in place for all blog/*.html.
City/country pages are NOT touched (their /lang/... structure is correct).
"""
import re
import glob
import os
import shutil
from datetime import datetime

BLOG_DIR = "/home/kaliuser/worldtime/blog"
BACKUP_DIR = f"/home/kaliuser/worldtime/blog_hreflang_backup_{datetime.now():%Y%m%d_%H%M%S}"

LANGS = ["es", "zh", "ru", "it", "de", "ja", "fr", "uk"]
# Match: https://worldtimessync.com/<lang>/blog/<slug>.html
PAT = re.compile(
    r"https://worldtimessync\.com/(" + "|".join(LANGS) + r")/blog/([a-z0-9-]+)\.html"
)


def fix():
    files = sorted(glob.glob(os.path.join(BLOG_DIR, "*.html")))
    total_files = 0
    total_subs = 0
    os.makedirs(BACKUP_DIR, exist_ok=True)
    for fp in files:
        with open(fp, encoding="utf-8") as fh:
            s = fh.read()
        n = len(PAT.findall(s))
        if not n:
            continue

        def repl(m):
            lang, slug = m.group(1), m.group(2)
            return f"https://worldtimessync.com/blog/{slug}-{lang}.html"

        new = PAT.sub(repl, s)
        if new != s:
            # backup original
            rel = os.path.basename(fp)
            shutil.copy2(fp, os.path.join(BACKUP_DIR, rel))
            with open(fp, "w", encoding="utf-8") as fh:
                fh.write(new)
            total_files += 1
            total_subs += n
    print(f"Backup dir: {BACKUP_DIR}")
    print(f"Files changed: {total_files}")
    print(f"Links rewritten: {total_subs}")


if __name__ == "__main__":
    fix()
