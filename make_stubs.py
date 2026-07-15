#!/usr/bin/env python3
"""Create redirect-stub pages for missing language sections (country/blog/meeting-planner).
Stub redirects to the English equivalent with canonical=en, so no 404 and no duplicate-content penalty.
Real translated content can later overwrite these stubs.
Usage: python3 make_stubs.py
"""
from pathlib import Path
import re

BASE = Path('/home/kaliuser/worldtime')
LANGS = ['de', 'es', 'fr', 'it', 'ja', 'ru', 'uk', 'zh']

def stub_html(en_path: str, lang: str) -> str:
    en_url = f"https://worldtimessync.com/{en_path}"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="UTF-8" />
<link rel="canonical" href="{en_url}" />
<meta http-equiv="refresh" content="0; url={en_url}" />
<meta name="robots" content="noindex, follow" />
<title>Redirecting…</title>
</head>
<body>
<p>Redirecting to <a href="{en_url}">{en_url}</a>…</p>
</body>
</html>
"""

def main():
    made = 0
    # meeting-planner per lang (except en)
    for lang in LANGS:
        target = BASE / f"{lang}/meeting-planner.html"
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(stub_html("meeting-planner.html", lang), encoding='utf-8')
            made += 1
    # country + blog per lang: mirror english structure
    for section in ['country', 'blog']:
        src = BASE / section
        if not src.exists():
            continue
        for sf in src.glob('*.html'):
            en_rel = f"{section}/{sf.name}"
            for lang in LANGS:
                target = BASE / f"{lang}/{section}/{sf.name}"
                if not target.exists():
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text(stub_html(en_rel, lang), encoding='utf-8')
                    made += 1
    print(f"stubs created: {made}")

if __name__ == '__main__':
    main()
