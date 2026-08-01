#!/usr/bin/env python3
"""
find_broken_links.py — improved

Finds TRUE 404s among internal same-origin href links across all .html files.

Ignores:
  * href="/"  (resolves to index.html)
  * href="/<lang>/blog/<slug>.html"  (Vercel 301 rule -> /blog/<slug>-<lang>)
  * href="/<lang>/blog/index.html"  (Vercel rewrite -> index)
  * href="..." without a path  e.g. href="foo" (relative, site uses absolute)

For each href that does NOT resolve to an existing local file AND is not covered
by a known Vercel route rewrite, record it as broken.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent
LANGS = r"(?:es|zh|ru|it|de|ja|fr|uk)"

HREFS = re.compile(r'href="([^"#?]+)')
SKIP = re.compile(r'^(https?:|//|mailto:|tel:|javascript:|#|data:|"$)')

# Patterns that are valid redirects (handled by Vercel), not true 404s
REDIRECT_OK = [
    re.compile(rf'^/{LANGS}/blog/.+\.html(?:$|\?|#)'),
    re.compile(rf'^/{LANGS}/blog/index\.html'),
    re.compile(r'^/about\.html$'),
    re.compile(r'^/api\.html$'),
    re.compile(r'^/contact\.html$'),
    re.compile(r'^/privacy\.html$'),
    re.compile(r'^/terms\.html$'),
    # /<lang>/<page>.html → clean via cleanUrls is NOT a redirect (200). These are real pages.
]


def resolve_local(url: str) -> bool:
    """Resolve a clean internal URL against local files, emulating Vercel
    cleanUrls: `/foo` -> `/foo.html`; `/foo/` -> `/foo/index.html`."""
    path = unquote(url)
    # Root -> index.html
    if path == '/':
        return (ROOT / 'index.html').exists()
    p = path.lstrip('/')
    # Language-prefixed root dirs e.g. /es -> /es/index.html
    if re.fullmatch(rf'{LANGS}(?:/|$)', p):
        p = p + 'index.html' if p.endswith('/') else p + 'index.html'
    candidates = [
        ROOT / p,                                    # direct file /foo.html or /foo/index.html
        ROOT / (p + '.html'),                        # clean -> .html  (cleanUrls mapping)
        ROOT / (p + '/index.html'),                  # /foo -> /foo/index.html
    ]
    return any(c.is_file() for c in candidates if c.exists())


def is_redirect_handled(url: str) -> bool:
    return any(r.match(url) for r in REDIRECT_OK)


def main() -> int:
    broken = [[] for _ in range(1000)]  # not used, replaced below
    broken: dict[str, str] = {}  # href -> first source_file
    checked = 0
    files_scanned = 0

    # Pre-compiled regex to drop <script>...</script> blocks: runtime JS can
    # build href strings (e.g. '<a href="/time/'+c+"'>") that look like broken
    # links to a static resolver. Googlebot doesn't treat those as crawlable
    # static anchors, so we exclude script bodies from link validation.
    STRIP_SCRIPT = re.compile(r'<script\b[^>]*>.*?</script>', re.IGNORECASE | re.DOTALL)
    for f in sorted(ROOT.rglob('*.html')):
        files_scanned += 1
        text = STRIP_SCRIPT.sub('', f.read_text(encoding='utf-8', errors='replace'))
        rel = str(f.relative_to(ROOT))
        for m in HREFS.finditer(text):
            url = m.group(1).strip()
            if SKIP.match(url) or not url.startswith('/'):
                continue
            checked += 1

            # Skip root and known Vercel redirect destinations
            if url == '/':
                continue
            if is_redirect_handled(url):
                continue

            if not resolve_local(url):
                # Store only unique hrefs, keep first source file
                if url not in broken:
                    broken[url] = rel

    print(f'Files scanned: {files_scanned}, internal hrefs checked: {checked}')
    print(f'True 404-causing hrefs: {len(broken)}')
    print()
    # Group by path-prefix for readability
    from collections import Counter
    prefix_counter = Counter()
    for href in broken:
        pfx = href.split('/')[1] if href.startswith('/') else 'ROOT'
        prefix_counter[pfx] += 1

    print('Breakdown by path prefix:')
    for pfx, n in prefix_counter.most_common():
        print(f'  /{pfx}/: {n} broken hrefs')
    print()
    print('First 30 broken hrefs (unique):')
    for i, (href, src) in enumerate(sorted(broken.items())[:30]):
        print(f'  {i+1:2d}. {href:55s}  (first seen in {src})')

    return 0


if __name__ == '__main__':
    sys.exit(main())
