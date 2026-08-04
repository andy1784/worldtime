#!/usr/bin/env python3
"""
remove_broken_time_links.py

Removes all internal <a href="/time/<broken-slug>">...</a> links from HTML
files across the repo, where <broken-slug> is a /time/ city slug that has no
corresponding time/<slug>.html file on disk (these pages 404).

Approach: rather than surgically deleting the <a> tag (which can break
sentences), we *unwrap* the anchor — keep its inner text, drop the href — so
the prose stays readable and the city name is preserved as informational text,
just not clickable. This avoids 404s without harming UX / i18n content.

Example:
  <a href="/time/bali">Bali, Indonesia (WIB)</a>
  ->  Bali, Indonesia (WIB)      (no link)

Whitelist (never touched):
  /time/new-york, /time/london, etc.  — only slugs WITHOUT a file are removed.
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Collect slugs that exist on disk
EXISTING_SLUGS = {
    p.name[:-5]        # strip .html
    for p in (ROOT / 'time').glob('*.html')
}
print(f'Existing /time/ pages: {len(EXISTING_SLUGS)}')

# Build broken-slug set from all hrefs referencing /time/<x>
HREF_TIME = re.compile(r'href="(/time/[a-z0-9-]+)"', re.I)
broken_slugs = set()
for f in ROOT.rglob('*.html'):
    text = f.read_text(encoding='utf-8', errors='replace')
    for m in HREF_TIME.finditer(text):
        href = m.group(1)  # /time/bali
        slug = href.split('/time/', 1)[1]
        if slug not in EXISTING_SLUGS:
            broken_slugs.add(slug)

print(f'Broken /time/ slugs (no file): {len(broken_slugs)}')


# Unwrap anchors with broken hrefs
ANCHOR_RE = re.compile(
    r'<a\s[^>]*href="(/time/[a-z0-9-]+)"[^>]*>(.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)

def unwrap(match: re.Match) -> str:
    href = match.group(1)
    inner = match.group(2)
    slug = href.split('/time/', 1)[1]
    if slug not in broken_slugs:
        return match.group(0)   # keep existing links
    return inner.strip()        # drop the <a>, keep text


def main() -> int:
    files_changed = 0
    total_unwrapped = 0
    for f in sorted(ROOT.rglob('*.html')):
        text = f.read_text(encoding='utf-8', errors='replace')
        # Count before
        n_before = len(ANCHOR_RE.findall(text))
        new_text, n = ANCHOR_RE.subn(unwrap, text)
        n_changed = sum(1 for m in ANCHOR_RE.finditer(text)
                        if m.group(1).split('/time/',1)[1] in broken_slugs)
        if new_text != text:
            f.write_text(new_text, encoding='utf-8')
            files_changed += 1
            total_unwrapped += n
    print(f'Files modified: {files_changed}')
    print(f'Total broken anchors unwrapped: {total_unwrapped}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
