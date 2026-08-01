#!/usr/bin/env python3
"""
add_hreflang_only_existing.py — post-processor that normalizes the hreflang
<link rel="alternate"> tags on every `blog/*.html` to a single, canonical,
duplicate-free block referencing only languages whose `<slug>-<lang>.html`
translation file actually exists on disk.

Durable fix for AGANS.md TODO #4. Run after any generation batch:

    python3 add_hreflang_only_existing.py            # rewrite in place
    python3 add_hreflang_only_existing.py --dry-run  # report only

Tag-aware (not block-aware): finds EVERY `<link rel="alternate" hreflang="XX"
href="URL">` — even stray old-format ones sitting inline on the same line as the
canonical link — collapses them into one clean block, drops duplicates and
legacy `<lang>/blog/<slug>` URLs.
"""
from __future__ import annotations
import argparse, glob, os, re, sys
from blog_hreflang_util import render_hreflang, LANG_LINK_ORDER

TAG = re.compile(
    r'<link rel="alternate" hreflang="([^"]*)"\s+href="([^"]*)">\s*',
    re.IGNORECASE,
)


def slug_from_path(path: str) -> str:
    base = os.path.basename(path)[:-len('.html')]
    for L in LANG_LINK_ORDER:
        if base.endswith(f"-{L}"):
            return base[: -(len(L) + 1)]
    return base


def relang_from_path(path: str) -> str:
    base = os.path.basename(path)[:-len('.html')]
    for L in LANG_LINK_ORDER:
        if base.endswith(f"-{L}"):
            return L
    return "en"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    rewritten = 0
    for path in sorted(glob.glob('blog/*.html')):
        lang = relang_from_path(path)
        slug = slug_from_path(path)
        text = open(path, encoding='utf-8', errors='replace').read()

        tags = TAG.findall(text)
        if not tags:
            continue

        clean_block = render_hreflang(slug, lang) + '\n    '
        state = {'done': False}

        def repl(_m, _s=state):
            if not _s['done']:
                _s['done'] = True
                return clean_block
            return ''

        new_text = TAG.sub(repl, text)
        if new_text != text:
            rewritten += 1
            print(f"  [{'DRY' if args.dry_run else 'OK '}] {path} "
                  f"(hreflang tags {len(tags)} -> 1 canonical block)")
            if not args.dry_run:
                open(path, 'w', encoding='utf-8').write(new_text)

    print(f"\n[blog_hreflang] {'DRY-RUN ' if args.dry_run else ''}rewrote "
          f"{rewritten} blog file(s)")
    return 0


if __name__ == '__main__':
    sys.exit(main())
