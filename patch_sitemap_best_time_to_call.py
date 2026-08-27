#!/usr/bin/env python3
"""
Insert the 12-language best-time-to-call blog post group into sitemap.xml.

The site's gen_sitemap.py only knows 9 languages (en + de/es/fr/it/ja/ru/uk/zh)
and would NOT emit pt/ar/hi even though those blog HTML files now exist.
This script ensures a single <url> block (x-default + en + all 11 localized,
where Ukrainian uses the '-ukr' suffix to avoid colliding with the existing
"Best Time to Call the UK" country article which uses '-uk') is present, right
before </urlset>.

Idempotent + self-healing: if an older/correct block already exists it is
removed and re-inserted fresh, so re-running never duplicates or leaves a
stale (wrong -uk) entry.
"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(ROOT, "sitemap.xml")
SLUG = "best-time-to-call"
SITE = "https://worldtimessync.com"
LANGS = ["en", "es", "de", "fr", "it", "ja", "ru", "uk", "zh", "pt", "ar", "hi"]
DATE = "2026-08-27"

def url_for(lang):
    if lang == "en":
        return "%s/blog/%s" % (SITE, SLUG)
    if lang == "uk":
        # Ukrainian translation uses -ukr to avoid the UK-country -uk article
        return "%s/blog/%s-ukr" % (SITE, SLUG)
    return "%s/blog/%s-%s" % (SITE, SLUG, lang)

def build_block():
    lines = ["  <url>"]
    lines.append("    <loc>%s</loc>" % url_for("en"))
    lines.append("    <lastmod>%s</lastmod>" % DATE)
    lines.append("    <changefreq>monthly</changefreq>")
    lines.append("    <priority>0.6</priority>")
    lines.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s" />' % url_for("en"))
    for lang in LANGS:
        lines.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s" />' % (lang, url_for(lang)))
    lines.append("  </url>")
    return "\n".join(lines)

def remove_existing(xml):
    """Remove any <url>...</url> block that references this slug's EN url."""
    marker = "<loc>%s/blog/%s</loc>" % (SITE, SLUG)
    if marker not in xml:
        return xml, False
    # find the enclosing <url> ... </url>
    start = xml.rfind("<url>", 0, xml.find(marker))
    end = xml.find("</url>", xml.find(marker)) + len("</url>")
    if start == -1 or end == -1:
        return xml, False
    new_xml = xml[:start].rstrip() + "\n" + xml[end:].lstrip()
    return new_xml, True

def main():
    with open(PATH, encoding="utf-8") as f:
        xml = f.read()
    xml, removed = remove_existing(xml)
    if removed:
        print("removed existing best-time-to-call block (stale/wrong)")
    block = build_block()
    if "</urlset>" not in xml:
        raise SystemExit("no </urlset> found")
    xml = xml.replace("</urlset>", block + "\n</urlset>\n")
    with open(PATH, "w", encoding="utf-8") as f:
        f.write(xml)
    print("wrote best-time-to-call group (12 langs, uk->-ukr) to sitemap.xml")

if __name__ == "__main__":
    main()
