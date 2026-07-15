#!/usr/bin/env python3
"""Create redirect stubs for country pages referenced in navigation but missing from disk.
Redirects to /country/ (the country index). Canonical on en country index to avoid dup content.
Also creates the missing ROOT country stubs so even en links resolve.
"""
import re, glob
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')
LANGS = ['de', 'es', 'fr', 'it', 'ja', 'ru', 'uk', 'zh']

def stub(name: str, lang: str) -> str:
    target = f"https://worldtimessync.com/country/{name}.html"
    index = "https://worldtimessync.com/country/"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="UTF-8" />
<link rel="canonical" href="{index}" />
<meta http-equiv="refresh" content="0; url={index}" />
<meta name="robots" content="noindex, follow" />
<title>Redirecting…</title>
</head>
<body>
<p>Redirecting to <a href="{index}">country index</a>…</p>
</body>
</html>
"""

def main():
    missing = set()
    # collect all /(lang/)?country/NAME links that are missing on disk
    for lang in [''] + LANGS:
        prefix = f"{lang}/" if lang else ""
        pattern = f"{prefix}time/*.html" if lang else "time/*.html"
        for f in glob.glob(pattern):
            h = open(f, encoding='utf-8').read()
            pat = r'href="(/(?:%s)?country/([^"]+))"' % (lang) if lang else r'href="(/country/([^"]+))"'
            for full, name in re.findall(pat, h):
                name = name.split('#')[0].split('?')[0]
                if name.endswith('.html'):
                    name = name[:-5]
                p = BASE / (full.lstrip('/'))
                if not p.exists() and not Path(str(p) + '.html').exists():
                    missing.add((lang, name))
    made = 0
    for lang, name in missing:
        if lang:
            target = BASE / f"{lang}/country/{name}.html"
        else:
            target = BASE / f"country/{name}.html"
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(stub(name, lang or 'en'), encoding='utf-8')
            made += 1
    print(f"country stubs created: {made}")

if __name__ == '__main__':
    main()
