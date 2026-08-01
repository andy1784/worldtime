#!/usr/bin/env python3
"""
add_hreflang_only_existing.py — post-processor for blog hreflang blocks.

After any generation batch, run this to guarantee every `blog/*.html` lists
ONLY languages whose `<slug>-<lang>.html` translation file actually exists on
disk (plus always-on x-default + en). This is the durable counterpart to
blog_hreflang_util.render_hreflang(): the generators call the helper at write
time (so newly generated headers are clean), and this script fixes up any
already-committed files that may have been produced by an older generator.

Usage:
    python3 add_hreflang_only_existing.py            # rewrite in place
    python3 add_hreflang_only_existing.py --dry-run  # report only
"""
from __future__ import annotations
import argparse, glob, re, sys
from blog_hreflang_util import render_hreflang, SITE, LANG_LINK_ORDER

# Match an entire contiguous hreflang <link> block (any whitespace/newlines).
HREFLANG_BLOCK = re.compile(
    r' *<link rel="alternate" hreflang="x-default"[^>]*>\s*\n'
    r'(?: *<link rel="alternate" hreflang="[^"]*"[^>]*>\s*\n)+',
)


def slug_from_path(path: str) -> str:
    """blog/world-clock-for-remote-teams-zh.html -> world-clock-for-remote-teams"""
    base = path.rsplit('/', 1)[-1]            # world-clock-for-remote-teams-zh.html
    base = base[:-len('.html')]               # world-clock-for-remote-teams-zh
    for L in LANG_LINK_ORDER:                 # strip a trailing -lang suffix
        if base.endswith(f"-{L}"):
            base = base[: -(len(L) + 1)]
            break
    return base


def relang_from_path(path: str) -> str:
    base = path.rsplit('/', 1)[-1][:-len('.html')]
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
        m = HREFLANG_BLOCK.search(text)
        if not m:
            continue
        # Normalize to a sorted set of link lines so formatting differences don't
        # cause needless churn. Only rewrite when the *set* of referenced languages
        # actually changes.
        old_links = sorted(ln.strip() for ln in m.group(0).splitlines()
                           if ln.strip().startswith('<link rel="alternate"'))
        new_block = render_hreflang(slug, lang).rstrip()
        new_links = sorted(ln.strip() for ln in new_block.splitlines()
                           if ln.strip().startswith('<link rel="alternate"'))
        if old_links == new_links:
            continue  # already correct for this post's translations

        lead = m.group(0)[: len(m.group(0)) - len(m.group(0).lstrip())]
        indent = ' ' * len(lead)
        replacement = '\n'.join(
            lead + ln if i == 0 else indent + ln for i, ln in enumerate(new_block.splitlines())
        )
        new_text = text[: m.start()] + replacement + text[m.end():]
        rewritten += 1
        if not args.dry_run:
            open(path, 'w', encoding='utf-8').write(new_text)
        print(f"  [{'DRY' if args.dry_run else 'OK '}] {path} "
              f"(synced {len(new_links)} hreflang links, was {len(old_links)})")
    print(f"\n[blog_hreflang] {'DRY-RUN ' if args.dry_run else ''}rewrote {rewritten} blog file(s)")
    return 0


if __name__ == '__main__':
    sys.exit(main())
