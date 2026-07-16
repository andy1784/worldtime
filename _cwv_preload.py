#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Task 4 (CWV): Add <link rel="preload" as="script" fetchpriority="high"> for the main
JS bundle in <head> of blog posts, blog indexes, and main page.
Safe: only inserts if not already present. Helps LCP by starting JS download earlier.
"""
import os, re, glob

ROOT = '/home/kaliuser/worldtime'
JS = '/assets/index-Dd7au40z.js'
PRELOAD = f'    <link rel="preload" as="script" href="{JS}" fetchpriority="high">\n'

targets = []
# blog posts (EN + localized)
targets += glob.glob(os.path.join(ROOT, 'blog', '*.html'))
# blog indexes (lang/blog/index.html)
for lang in ['', 'ru', 'es', 'zh', 'ja', 'fr', 'de', 'uk']:
    d = os.path.join(ROOT, lang, 'blog') if lang else os.path.join(ROOT, 'blog')
    if os.path.isdir(d):
        targets.append(os.path.join(d, 'index.html'))
# main page + key static pages
for f in ['index.html', 'how-it-works.html', 'privacy.html', 'about.html', 'contact.html', 'terms.html']:
    p = os.path.join(ROOT, f)
    if os.path.exists(p):
        targets.append(p)

added = 0
for path in targets:
    if not os.path.isfile(path):
        continue
    html = open(path, encoding='utf-8').read()
    if 'as="script"' in html and JS in html:
        continue  # already has JS preload
    if '</head>' not in html:
        continue
    html = html.replace('</head>', PRELOAD + '</head>', 1)
    open(path, 'w', encoding='utf-8').write(html)
    added += 1

print(f'Added JS preload to {added} files.')
