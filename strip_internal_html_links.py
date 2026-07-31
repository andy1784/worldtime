#!/usr/bin/env python3
"""
strip_internal_html_links.py

Removes trailing .html from internal href URLs across all HTML files in the
worldtime repository, except for a small whitelist of paths that must keep the
extension (widget.js/embed, robots.txt-adjacent, etc.).

Why: Vercel `cleanUrls: true` already returns 308 redirect from `/foo.html` to
`/foo`. Internal links still pointing to `.html` waste crawl budget, count as
"redirect pages" in GSC Coverage, and contribute to "canonical-not-respected"
findings. Replacing them with the canonical clean URLs at the source eliminates
the redirect hop entirely and lets Google resolve every URL in one request.

Usage:
    python3 strip_internal_html_links.py [--dry-run]
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Paths that MUST keep the .html extension. Two buckets:
# 1. External-style assets (real files served as-is): widget.js etc.
# 2. Vercel routes where cleanUrls does NOT strip .html (handled separately).
KEEP_HTML = {
    "widget.html",       # documented Vercel route, accessible at /widget.html
    "widget-embed.html", # iframe-target route, must stay at .html
    # widget.js/robots.txt/sitemap.xml are NOT .html so won't match anyway.
}

# Anchor / query / fragment suffix to preserve when stripping .html
HREF_RE = re.compile(
    r'href="(?P<url>(?:https?://worldtimessync\.com)?/[^"#?]*?)\.html(?P<suffix>[#?][^"]*)?"'
)

# External hosts whose URLs must NOT be rewritten even if path ends in .html.
EXTERNAL_HOST_RE = re.compile(r'^https?://(?!worldtimessync\.com)', re.IGNORECASE)


def should_skip(url: str) -> bool:
    """Return True if this URL must keep its .html suffix."""
    # Strip leading host if present, then take the last path segment.
    path = url.split('?')[0].split('#')[0]
    last = path.rsplit('/', 1)[-1]
    return last in KEEP_HTML


def rewrite_href(match: re.Match) -> str:
    url = match.group('url')
    suffix = match.group('suffix') or ''
    if should_skip(url):
        return match.group(0)
    return f'href="{url}{suffix}"'


def process_file(path: Path) -> tuple[int, int]:
    """Return (rewrites, skips) for one HTML file."""
    text = path.read_text(encoding='utf-8', errors='replace')
    rewrites = 0
    skips = 0

    def repl(match: re.Match) -> str:
        nonlocal rewrites, skips
        url = match.group('url')
        if EXTERNAL_HOST_RE.match(url):
            skips += 1
            return match.group(0)
        if should_skip(url):
            skips += 1
            return match.group(0)
        rewrites += 1
        suffix = match.group('suffix') or ''
        return f'href="{url}{suffix}"'

    new_text = HREF_RE.sub(repl, text)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
    return rewrites, skips


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true',
                        help='Report what would change without writing files.')
    args = parser.parse_args()

    html_files = sorted(ROOT.rglob('*.html'))
    total_rewrites = 0
    total_skips = 0
    files_changed = 0
    per_file_top = Counter()

    for p in html_files:
        if args.dry_run:
            text = p.read_text(encoding='utf-8', errors='replace')
            matches = HREF_RE.findall(text)
            rewrites = sum(1 for u, _ in matches
                           if not EXTERNAL_HOST_RE.match(u)
                           and not should_skip(u))
            skips = len(matches) - rewrites
        else:
            rewrites, skips = process_file(p)
            if rewrites > 0:
                files_changed += 1
                per_file_top[p.relative_to(ROOT)] = rewrites

        total_rewrites += rewrites
        total_skips += skips

    mode = 'DRY-RUN' if args.dry_run else 'APPLIED'
    print(f'[{mode}] Scanned {len(html_files)} HTML files')
    print(f'  Rewrites planned/applied: {total_rewrites}')
    print(f'  Skipped (whitelist/external): {total_skips}')
    if not args.dry_run:
        print(f'  Files changed: {files_changed}')
        if per_file_top:
            print('  Top 10 files by rewrites:')
            for path, n in per_file_top.most_common(10):
                print(f'    {n:5d}  {path}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
