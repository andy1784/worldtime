#!/usr/bin/env python3
"""
Copy city pages to pt, ar, hi language directories
and add hreflang links for pt, ar, hi to all city pages.
"""

import os
import re
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')

# Source: English city pages
EN_TIME_DIR = BASE / 'time'

# Target language directories
TARGET_LANGS = ['pt', 'ar', 'hi']

def copy_city_pages():
    """Copy English city pages to pt, ar, hi directories"""
    en_files = list(EN_TIME_DIR.glob('*.html'))
    print(f"Found {len(en_files)} English city pages")
    
    for lang in TARGET_LANGS:
        target_dir = BASE / lang / 'time'
        target_dir.mkdir(parents=True, exist_ok=True)
        
        copied = 0
        for en_file in en_files:
            target_file = target_dir / en_file.name
            if not target_file.exists():
                target_file.write_bytes(en_file.read_bytes())
                copied += 1
        
        print(f"  {lang}: Copied {copied} new city pages")

def add_hreflang_to_city_pages():
    """Add pt, ar, hi hreflang links to all city pages"""
    # All language directories
    lang_dirs = ['en', 'es', 'zh', 'ru', 'it', 'de', 'ja', 'fr', 'uk', 'pt', 'ar', 'hi']
    
    for lang in lang_dirs:
        if lang == 'en':
            time_dir = BASE / 'time'
        else:
            time_dir = BASE / lang / 'time'
        
        if not time_dir.exists():
            print(f"  {lang}: time directory not found")
            continue
        
        files = list(time_dir.glob('*.html'))
        updated = 0
        
        for f in files:
            html = f.read_text(encoding='utf-8')
            
            # Check if pt, ar, hi hreflangs already present
            if 'hreflang="pt"' in html and 'hreflang="ar"' in html and 'hreflang="hi"' in html:
                continue
            
            # Find the hreflang block and add pt, ar, hi
            # Pattern: <link rel="alternate" hreflang="uk" ...>
            pattern = r'(<link rel="alternate" hreflang="uk" href="https://worldtimessync\.com/[^"]+">)'
            match = re.search(pattern, html)
            if match:
                insert_after = match.end()
                new_links = '\n    <link rel="alternate" hreflang="pt" href="https://worldtimessync.com/pt/time/{slug}">\n    <link rel="alternate" hreflang="ar" href="https://worldtimessync.com/ar/time/{slug}">\n    <link rel="alternate" hreflang="hi" href="https://worldtimessync.com/hi/time/{slug}">'.format(
                    slug=f.stem
                )
                html = html[:insert_after] + '\n' + new_links + html[insert_after:]
                f.write_text(html, encoding='utf-8')
                updated += 1
            else:
                # Try alternative pattern
                pattern2 = r'(<link rel="alternate" hreflang="uk" href="https://worldtimessync\.com/[^"]+"/>'
                match2 = re.search(pattern2, html)
                if match2:
                    insert_after = match2.end()
                    new_links = '\n    <link rel="alternate" hreflang="pt" href="https://worldtimessync.com/pt/time/{slug}"/>\n    <link rel="alternate" hreflang="ar" href="https://worldtimessync.com/ar/time/{slug}"/>\n    <link rel="alternate" hreflang="hi" href="https://worldtimessync.com/hi/time/{slug}"/>'.format(
                        slug=f.stem
                    )
                    html = html[:insert_after] + '\n' + new_links + html[insert_after:]
                    f.write_text(html, encoding='utf-8')
                    updated += 1
        
        print(f"  {lang}: Updated {updated} city pages")

if __name__ == '__main__':
    print("Copying city pages to pt, ar, hi...")
    copy_city_pages()
    
    print("\nAdding hreflang links to all city pages...")
    add_hreflang_to_city_pages()
    
    print("\nDone!")