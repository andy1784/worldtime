#!/usr/bin/env python3
"""Add hreflang blocks to English landing pages and fix JSON-LD @context."""
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')
PAGES = ['world-clock.html', 'time-zone-converter.html']
LANGS = ['de', 'es', 'fr', 'it', 'ja', 'ru', 'uk', 'zh', 'hi', 'ar', 'pt']

def add_hreflang(html, page_slug):
    base_slug = page_slug.replace('.html', '')
    base_url = f"https://worldtimessync.com/{base_slug}"
    links = [
        f'<link rel="alternate" hreflang="x-default" href="{base_url}" />',
        f'<link rel="alternate" hreflang="en" href="{base_url}" />',
    ]
    for lang in LANGS:
        links.append(f'<link rel="alternate" hreflang="{lang}" href="https://worldtimessync.com/{lang}/{base_slug}" />')
    
    hreflang_html = '\n    '.join(links) + '\n'
    html = html.replace('</head>', f'    {hreflang_html}</head>')
    return html

def fix_jsonld_context(html):
    # Pattern: "@context":"https://***@type":" -> "@context":"https://schema.org","@type":
    html = html.replace('"@context":"https://***@type":"', '"@context":"https://schema.org","@type":"')
    return html

def main():
    for page in PAGES:
        path = BASE / page
        html = path.read_text(encoding='utf-8')
        html = fix_jsonld_context(html)
        html = add_hreflang(html, page)
        path.write_text(html, encoding='utf-8')
        print(f"Updated {page}")

if __name__ == '__main__':
    main()