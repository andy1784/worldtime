#!/usr/bin/env python3
"""
Generate sitemap.xml for worldtimessync.com with proper hreflang alternate
links, by scanning the actual files on disk.

Language structure:
  - English (default):  <page>.html  and  time/<city>.html  and  blog/<slug>.html
  - Localized:          <lang>/<page>.html  <lang>/time/<city>.html  blog/<slug>-<lang>.html

We group every URL by its "base" (the English path) and emit an <url> entry
with <xhtml:link rel="alternate" hreflang="..."> for each available language,
plus x-default pointing at English.

Run from repo root:  python3 gen_sitemap.py
"""
import os
import re
from datetime import datetime, timezone
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://worldtimessync.com"
LANGS = ["en", "de", "es", "fr", "it", "ja", "ru", "uk", "zh"]
# Map folder name -> hreflang code (folder "uk" is Ukrainian, not "uk" english)
FOLDER_TO_HREFLANG = {
    "de": "de", "es": "es", "fr": "fr", "it": "it",
    "ja": "ja", "ru": "ru", "uk": "uk", "zh": "zh",
}

# Static root pages that exist as <page>.html (English) with localized <lang>/<page>.html
# (H) excludes widget.html and widget-embed.html — these are embeddable technical
# endpoints, not indexable content pages.
ROOT_PAGES = [
    "index.html", "about.html", "contact.html", "privacy.html", "terms.html",
    "api.html", "earth-clock.html", "earth-clock-video.html", "every-second.html",
    "live.html", "meeting-planner.html", "remote-team-solutions.html",
    "time-difference.html", "gmt-vs-utc.html", "dst-2026-worldwide.html",
    "dst-countdown.html", "world-clock.html", "world-time-map.html",
    "sunrise-sunset.html",
    "wordpress.html", "how-it-works.html", "event.html",
    "time/index.html",  # city directory landing page (canonical /time)
]

SKIP_DIRS = {"assets", "data", "i18n", "wp-plugin", "__pycache__", ".git", "node_modules", "tools"}
# bump dirs that are now ignored by Vercel (won't be deployed); do not list in sitemap
STUB_TITLE = "Redirecting…"  # title of redirect-stub pages (meta refresh, noindex)


def is_stub(p):
    """True if file is a noindex meta-refresh stub (canonical pointing at /country/ etc.)."""
    try:
        with open(p, encoding="utf-8", errors="ignore") as fh:
            head = fh.read(1500)
    except OSError:
        return False
    return STUB_TITLE in head or 'http-equiv="refresh" content="0; url=https://worldtimessync.com/country/"' in head


def mtime_iso(path):
    ts = os.path.getmtime(path)
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")


def strip_html(rel):
    """Convert 'time/london.html' -> 'time/london'; keep 'index.html' handled separately."""
    if rel == "index.html":
        return None  # handled at call site
    if rel.endswith("/index.html"):
        return rel[: -len("/index.html")]
    if rel.endswith(".html"):
        return rel[: -len(".html")]
    return rel


def url_for(rel_path):
    """Return canonical-style URL (no .html extension per cleanUrls:true).

    rel_path like 'time/london.html' -> 'https://worldtimessync.com/time/london'
    rel_path == 'index.html' -> 'https://worldtimessync.com/  '
    rel_path like '<lang>/index.html' -> 'https://worldtimessync.com/<lang>'
    rel_path like 'country/ukraine.html' -> 'https://worldtimessync.com/country/ukraine'
    """
    rel = rel_path.replace(os.sep, "/")
    if rel == "index.html":
        return SITE + "/"
    return SITE + "/" + strip_html(rel)


def collect_groups():
    """
    Returns dict: base_key -> { 'en': relpath_or_None, '<lang>': relpath_or_None, 'type': ... }
    base_key is the english relative path (e.g. 'time/london.html').
    """
    groups = {}

    # 1) Root static pages
    for page in ROOT_PAGES:
        key = page
        g = {"en": page, "type": "page"}
        for lang in FOLDER_TO_HREFLANG:
            lp = os.path.join(ROOT, lang, page)
            g[lang] = lang + "/" + page if os.path.exists(lp) else None
        groups[key] = g

    # 2) City pages: time/<city>.html + <lang>/time/<city>.html
    time_dir = os.path.join(ROOT, "time")
    if os.path.isdir(time_dir):
        for fn in os.listdir(time_dir):
            if not fn.endswith(".html") or fn == "index.html":
                continue
            p = os.path.join(time_dir, fn)
            if is_stub(p):
                continue
            base = "time/" + fn
            g = {"en": base, "type": "city"}
            for lang in FOLDER_TO_HREFLANG:
                lp = os.path.join(ROOT, lang, "time", fn)
                if os.path.exists(lp) and not is_stub(lp):
                    g[lang] = lang + "/time/" + fn
                else:
                    g[lang] = None
            groups[base] = g

    # 2b) Country hubs: country/<slug>.html + <lang>/country/<slug>.html (real pages only, skip stubs)
    country_dir = os.path.join(ROOT, "country")
    if os.path.isdir(country_dir):
        for fn in os.listdir(country_dir):
            if not fn.endswith(".html"):
                continue
            p = os.path.join(country_dir, fn)
            if is_stub(p):
                continue
            base = "country/" + fn
            g = {"en": base, "type": "country"}
            for lang in FOLDER_TO_HREFLANG:
                lp = os.path.join(ROOT, lang, "country", fn)
                if os.path.exists(lp) and not is_stub(lp):
                    g[lang] = lang + "/country/" + fn
                else:
                    g[lang] = None
            groups[base] = g

    # 3) Blog posts: blog/<slug>.html + blog/<slug>-<lang>.html
    blog_dir = os.path.join(ROOT, "blog")
    if os.path.isdir(blog_dir):
        en_posts = {}
        for fn in os.listdir(blog_dir):
            if not fn.endswith(".html"):
                continue
            stem = fn[:-5]
            # localized?
            matched = None
            for lang in FOLDER_TO_HREFLANG:
                if stem.endswith("-" + lang):
                    matched = lang
                    break
            if matched:
                # base = strip -lang
                base_slug = stem[: -(len(matched) + 1)]
                key = "blog/" + base_slug + ".html"
                p = os.path.join(blog_dir, fn)
                if is_stub(p):
                    continue
                groups.setdefault(key, {"en": None, "type": "blog"})
                groups[key][matched] = "blog/" + fn
            else:
                key = "blog/" + fn
                p = os.path.join(blog_dir, fn)
                if is_stub(p):
                    continue
                g = groups.setdefault(key, {"en": "blog/" + fn, "type": "blog"})
                if g.get("en") is None:
                    g["en"] = "blog/" + fn
                for lang in FOLDER_TO_HREFLANG:
                    if g.get(lang) is None:
                        g[lang] = None

    return groups


def hreflang_block(g):
    """Return list of (hreflang, url) tuples including x-default."""
    links = []
    # english url
    en_rel = g.get("en")
    if not en_rel:
        # pick first available as default
        for lang in FOLDER_TO_HREFLANG:
            if g.get(lang):
                en_rel = g[lang]
                break
    if not en_rel:
        return links
    en_url = url_for(en_rel)
    # x-default -> english
    links.append(("x-default", en_url))
    links.append(("en", en_url))
    for lang in FOLDER_TO_HREFLANG:
        rel = g.get(lang)
        if rel:
            links.append((FOLDER_TO_HREFLANG[lang], url_for(rel)))
    return links


def priority_for(g):
    t = g.get("type")
    if t == "page":
        return "0.9"
    if t == "city":
        return "0.8"
    if t == "country":
        return "0.7"
    if t == "blog":
        return "0.6"
    return "0.5"


def changefreq_for(g):
    t = g.get("type")
    if t == "city":
        return "daily"
    if t == "country":
        return "weekly"
    if t == "page":
        return "monthly"
    return "monthly"


def main():
    groups = collect_groups()
    # Build url entries
    entries = []
    for key, g in groups.items():
        links = hreflang_block(g)
        if not links:
            continue
        # lastmod: newest mtime among existing files
        mtimes = []
        for lang in ["en"] + list(FOLDER_TO_HREFLANG):
            rel = g.get(lang)
            if rel and os.path.exists(os.path.join(ROOT, rel)):
                mtimes.append(mtime_iso(os.path.join(ROOT, rel)))
        lastmod = max(mtimes) if mtimes else "2026-07-17"
        en_rel = g.get("en") or next((g[l] for l in FOLDER_TO_HREFLANG if g.get(l)), None)
        loc = url_for(en_rel)
        block = '  <url>\n'
        block += f'    <loc>{escape(loc)}</loc>\n'
        block += f'    <lastmod>{lastmod}</lastmod>\n'
        block += f'    <changefreq>{changefreq_for(g)}</changefreq>\n'
        block += f'    <priority>{priority_for(g)}</priority>\n'
        for hl, hlurl in links:
            block += f'    <xhtml:link rel="alternate" hreflang="{hl}" href="{escape(hlurl)}" />\n'
        block += '  </url>\n'
        entries.append(block)

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    xml += '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n\n'
    xml += "".join(entries)
    xml += '</urlset>\n'

    out = os.path.join(ROOT, "sitemap.xml")
    with open(out, "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Wrote {out}: {len(entries)} url entries")


if __name__ == "__main__":
    main()
