#!/usr/bin/env python3
"""
Fix broken hreflang alternate links on ALL blog posts (EN + localized).

Some posts emit hreflang for languages whose target file blog/<slug>-<lang>.html
does not exist -> 404 after Vercel 301. Rewrite each post's alternate block to
list only languages whose target file exists on disk.

Run: python3 fix_blog_hreflang.py
"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
BLOG = os.path.join(ROOT, "blog")
SITE = "https://worldtimessync.com"

# Match hreflang links: capture hreflang value and full URL
LINK_RE = re.compile(
    r'<link rel="alternate" hreflang="([a-z-]+)" href="(https://worldtimessync\.com/[^"]+)"\s*/?>'
)

# Map hreflang code to filename suffix
HREFLANG_TO_SUFFIX = {
    'x-default': '',
    'en': '',
    'es': '-es',
    'zh': '-zh',
    'ru': '-ru',
    'it': '-it',
    'de': '-de',
    'ja': '-ja',
    'fr': '-fr',
    'uk': '-uk',
}

def fix_file(path):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    new_lines = []
    changed = False
    for line in lines:
        m = LINK_RE.search(line)
        if not m:
            new_lines.append(line)
            continue
        hl = m.group(1)          # hreflang value (e.g. "ru")
        full_url = m.group(2)    # full URL
        
        # Determine the actual filename on disk
        suffix = HREFLANG_TO_SUFFIX.get(hl, f"-{hl}" if hl not in ('x-default', 'en') else "")
        # Extract slug from URL
        # URL format: /blog/slug.html or /lang/blog/slug.html
        slug_match = re.search(r'/blog/([^/"\']+)\.html', full_url)
        if not slug_match:
            # Fallback: extract from end of URL
            slug_match = re.search(r'/([^/"\']+)\.html', full_url)
        if slug_match:
            slug = slug_match.group(1)
            # Remove language suffix from slug if present (e.g., slug-es -> slug)
            for lang_suffix in ['-es', '-zh', '-ru', '-it', '-de', '-ja', '-fr', '-uk']:
                if slug.endswith(lang_suffix):
                    slug = slug[:-len(lang_suffix)]
                    break
            target_filename = f"{slug}{suffix}.html"
            target = os.path.join(BLOG, target_filename)
            
            if os.path.exists(target):
                new_lines.append(line)
            else:
                changed = True  # drop broken alternate
        else:
            new_lines.append(line)  # keep if can't parse
    if changed:
        open(path, "w", encoding="utf-8").write("\n".join(new_lines))
    return changed

def main():
    removed = 0
    fixed = 0
    for fn in sorted(os.listdir(BLOG)):
        if not fn.endswith(".html"):
            continue
        path = os.path.join(BLOG, fn)
        before = len(LINK_RE.findall(open(path, encoding="utf-8").read()))
        if fix_file(path):
            after = len(LINK_RE.findall(open(path, encoding="utf-8").read()))
            removed += before - after
            fixed += 1
            print(f"fixed {fn}: {before} -> {after}")
    print(f"\nDone. Fixed {fixed} files, removed {removed} broken hreflang links.")

if __name__ == "__main__":
    main()
