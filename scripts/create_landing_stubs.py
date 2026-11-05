#!/usr/bin/env python3
"""Create redirect stubs for localized landing pages when translation is unavailable."""
import os
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')
LANGS = ['de', 'es', 'fr', 'it', 'ja', 'ru', 'uk', 'zh', 'hi', 'ar', 'pt']

SOURCE_PAGES = ['world-clock.html', 'time-zone-converter.html']

STUB_TEMPLATE = '''<!doctype html>
<html lang="{lang}"{dir_attr}>
<head>
<meta charset="UTF-8" />
<link rel="canonical" href="https://worldtimessync.com/{page}" />
<meta http-equiv="refresh" content="0; url=https://worldtimessync.com/{page}" />
<meta name="robots" content="noindex, follow" />
<title>Redirecting…</title>
</head>
<body>
<p>Redirecting to <a href="https://worldtimessync.com/{page}">{page}</a></p>
</body>
</html>
'''

def main():
    for page in SOURCE_PAGES:
        print(f"\n=== Creating stubs for {page} ===")
        for lang in LANGS:
            dir_attr = ' dir="rtl"' if lang in ('ar', 'he') else ''
            stub_dir = BASE / lang
            stub_dir.mkdir(parents=True, exist_ok=True)
            stub_path = stub_dir / page
            
            if stub_path.exists():
                print(f"  {lang}/{page}: exists, skipping")
                continue
            
            content = STUB_TEMPLATE.format(lang=lang, dir_attr=dir_attr, page=page)
            stub_path.write_text(content, encoding='utf-8')
            print(f"  {lang}/{page}: created")
    
    print("\nDone. Regenerate sitemap to include these URLs.")

if __name__ == '__main__':
    main()