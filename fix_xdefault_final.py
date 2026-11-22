#!/usr/bin/env python3
"""Fix x-default hreflang to point to English version for all languages."""
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')

for lang in ['zh', 'it', 'de', 'fr', 'pt', 'ru', 'ja', 'uk', 'hi', 'ar', 'es']:
    if lang == 'en':
        continue
    path = BASE / lang / 'blog' / f'check-current-time-any-city-{lang}.html'
    html = path.read_text(encoding='utf-8')
    
    # Fix x-default - should point to English version
    html = html.replace(
        f'href="https://worldtimessync.com/{lang}/blog/check-current-time-any-city-{lang}.html"',
        'href="https://worldtimessync.com/blog/check-current-time-any-city.html"',
        1  # Only first occurrence (x-default)
    )
    
    path.write_text(html, encoding='utf-8')
    print(f'Fixed x-default for {lang}')

# Also fix es
path = BASE / 'es' / 'blog' / 'check-current-time-any-city-es.html'
html = path.read_text(encoding='utf-8')
html = html.replace(
    'href="https://worldtimessync.com/es/blog/check-current-time-any-city-es.html"',
    'href="https://worldtimessync.com/blog/check-current-time-any-city.html"',
    1
)
path.write_text(html, encoding='utf-8')
print('Fixed x-default for es')

print('Done!')