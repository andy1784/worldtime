#!/usr/bin/env python3
"""Prune hreflang link block on every blog/*.html file so it ONLY lists
languages whose target file actually exists on disk.

Without this, the static translator generator emits hreflang entries that 404
because vercel.json redirects /<lang>/blog/<slug>.html to /blog/<slug>-<lang>.html
and the latter does not exist when the post was translated to fewer than 8
languages.

Run this after each batch of new translations:
    python3 _fix_hreflang.py

Idempotent — running it twice is safe.
"""
import os, re, glob, sys

BLOG_DIR = '/home/kaliuser/worldtime/blog'
LANGS = ['en', 'ru', 'es', 'zh', 'ja', 'fr', 'de', 'uk']


def en_url_from_file(html_path: str) -> str:
    """Return the canonical EN URL stored in the <link rel="canonical"> of html_path.
    Falls back to synthesising from the filename."""
    txt = open(html_path, encoding='utf-8').read()
    m = re.search(r'<link rel="canonical" href="([^"]+)"', txt)
    if m:
        return m.group(1)
    base = os.path.basename(html_path).replace('.html', '')
    if base.endswith(('-e\u0440', '-ru')):  # noqa
        pass
    slug = base
    if any(base.endswith('-' + l) for l in LANGS if l != 'en'):
        slug = base.rsplit('-', 1)[0]
    return f'https://worldtimessync.com/blog/{slug}.html'


def target_url_from_en(en_url: str, lang: str) -> str:
    """Derive the hreflang-tagged URL for lang from the EN canonical's slug.

    EN stays as the same EN URL. Other langs use the redirected URL form
    /<lang>/blog/<slug>.html (which Vercel 301s to /blog/<slug>-<lang>.html)."""
    m = re.search(r'https://worldtimessync\.com/blog/([^.]+)\.html$', en_url)
    slug = m.group(1) if m else ''
    if lang == 'en' or not slug:
        return en_url
    return f'https://worldtimessync.com/{lang}/blog/{slug}.html'


def expected_filename(slug: str, lang: str) -> str:
    if lang == 'en':
        return f'{slug}.html'
    return f'{slug}-{lang}.html'


def fix_file(html_path: str, stats: dict) -> None:
    txt = open(html_path, encoding='utf-8').read()

    # Locate the hreflang block (consecutive <link rel="alternate" hreflang=...> lines)
    pattern = re.compile(
        r'(?:\s*<link rel="alternate" hreflang="[^"]+" href="[^"]+">)+',
        re.S
    )
    block_match = pattern.search(txt)
    if not block_match:
        return

    en_url = en_url_from_file(html_path)
    # Determine slug from the canonical url referenced inside the block
    inner = block_match.group(0)
    m = re.search(r'hreflang="(?:x-default|en)" href="([^"]+)"', inner)
    en_block_url = m.group(1) if m else en_url
    slug_match = re.search(r'/blog/([^.]+)\.html$', en_block_url)
    slug = slug_match.group(1) if slug_match else ''

    # New block — only the langs whose file actually exists
    new_lines = []
    for l in LANGS:
        target = os.path.join(BLOG_DIR, expected_filename(slug, l))
        if not os.path.exists(target):
            continue
        url = target_url_from_en(en_block_url, l)
        if l == 'en':
            new_lines.append(f'    <link rel="alternate" hreflang="en" href="{url}">')
        else:
            new_lines.append(f'    <link rel="alternate" hreflang="{l}" href="{url}">')
    # Always include x-default (x-default = EN page) even if we somehow don't have EN; here EN always exists.
    new_lines.append(f'    <link rel="alternate" hreflang="x-default" href="{en_block_url}">')

    new_block = '\n'.join(new_lines)

    new_txt = txt[:block_match.start()] + '\n' + new_block + txt[block_match.end():]
    if new_txt != txt:
        with open(html_path, 'w', encoding='utf-8') as fh:
            fh.write(new_txt)
        stats['fixed'] += 1

    # Count entries before/after for log
    before = len(re.findall(r'hreflang="', inner))
    after = len(re.findall(r'hreflang="', new_block))
    stats['entries_before'] += before
    stats['entries_after'] += after


def main() -> int:
    stats = {'processed': 0, 'fixed': 0, 'entries_before': 0, 'entries_after': 0}
    for fname in sorted(os.listdir(BLOG_DIR)):
        if not fname.endswith('.html'):
            continue
        path = os.path.join(BLOG_DIR, fname)
        if os.path.isdir(path):
            continue
        stats['processed'] += 1
        fix_file(path, stats)

    saved = stats['entries_before'] - stats['entries_after']
    print(f'Processed: {stats["processed"]} files; rewrote: {stats["fixed"]}')
    print(f'hreflang entries: {stats["entries_before"]} -> {stats["entries_after"]} (removed {saved})')
    return 0


if __name__ == '__main__':
    sys.exit(main())
