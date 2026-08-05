#!/usr/bin/env python3
"""
Update all language index.html files to add pt, ar, hi hreflang links and language switcher links.
"""

from pathlib import Path
import re

BASE = Path('/home/kaliuser/worldtime')
LANGS = ['es', 'zh', 'ru', 'it', 'de', 'ja', 'fr', 'uk', 'pt', 'ar', 'hi']

# New hreflang entries to add
NEW_HREFLANG = '''    <link rel="alternate" hreflang="pt" href="https://worldtimessync.com/pt">
    <link rel="alternate" hreflang="ar" href="https://worldtimessync.com/ar">
    <link rel="alternate" hreflang="hi" href="https://worldtimessync.com/hi">'''

# New language switcher links
NEW_LANG_LINKS = '<a href="/pt/">Português</a><a href="/ar/">العربية</a><a href="/hi/">हिन्दी</a>'

def update_index_file(lang):
    """Update a language's index.html file"""
    path = BASE / lang / 'index.html'
    if not path.exists():
        print(f"  {lang}: index.html not found")
        return False
    
    html = path.read_text(encoding='utf-8')
    modified = False
    
    # 1. Add hreflang links for pt, ar, hi
    if 'hreflang="pt"' not in html:
        # Find the last hreflang line and add after it
        pattern = r'(<link rel="alternate" hreflang="uk" href="https://worldtimessync\.com/uk"[^>]*>)'
        match = re.search(pattern, html)
        if match:
            html = html[:match.end()] + '\n' + NEW_HREFLANG + html[match.end():]
            modified = True
            print(f"  {lang}: Added hreflang links")
        else:
            # Try alternative pattern
            pattern2 = r'(<link rel="alternate" hreflang="uk" href="https://worldtimessync\.com/uk"[^>]* />)'
            match2 = re.search(pattern2, html)
            if match2:
                html = html[:match2.end()] + '\n' + NEW_HREFLANG + html[match2.end():]
                modified = True
                print(f"  {lang}: Added hreflang links (alt pattern)")
            else:
                print(f"  {lang}: Could not find hreflang insertion point")
    
    # 2. Add language switcher links
    if 'href="/pt/"' not in html:
        # Find the language switcher div
        pattern = r'(<a href="/uk/">Українська</a>)'
        match = re.search(pattern, html)
        if match:
            html = html[:match.end()] + NEW_LANG_LINKS + html[match.end():]
            modified = True
            print(f"  {lang}: Added language switcher links")
        else:
            # Try other patterns
            pattern2 = r'(<a href="/uk/">\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430</a>)'
            match2 = re.search(pattern2, html)
            if match2:
                html = html[:match2.end()] + NEW_LANG_LINKS + html[match2.end():]
                modified = True
                print(f"  {lang}: Added language switcher links (alt pattern)")
            else:
                # Try for other languages
                pattern3 = r'(<a href="/uk/">Português</a>)'
                match3 = re.search(pattern3, html)
                if match3:
                    html = html[:match3.end()] + NEW_LANG_LINKS + html[match3.end():]
                    modified = True
                    print(f"  {lang}: Added language switcher links (pt pattern)")
                else:
                    print(f"  {lang}: Could not find language switcher insertion point")
    
    if modified:
        path.write_text(html, encoding='utf-8')
        return True
    return False

def update_time_pages():
    """Add hreflang pt, ar, hi to time/ pages"""
    # This is more complex - need to process each time page
    # For now, we'll do it via a batch update script
    pass

# Update all language index pages
for lang in LANGS:
    print(f"Updating {lang}...")
    update_index_file(lang)

print("\nDone updating index pages.")