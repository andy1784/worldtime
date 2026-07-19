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

LINK_RE = re.compile(
    r'<link rel="alternate" hreflang="([a-z-]+)" href="(https://worldtimessync\.com/blog/([^"/]+)\.html)"\s*/?>'
)

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
        hl = m.group(1)
        slug = m.group(3)  # e.g. "best-time-to-call-usa" or "best-time-to-call-usa-de"
        target = os.path.join(BLOG, f"{slug}.html")
        if os.path.exists(target):
            new_lines.append(line)
        else:
            changed = True  # drop broken alternate
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
