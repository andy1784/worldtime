#!/usr/bin/env python3
"""
Convert content/blog/<slug>-<lang>.md  ->  blog/<slug>-<lang>.html
and content/blog/<slug>.md (en)        ->  blog/<slug>.html

Using the EXACT same HTML structure as the live blog posts
(see gen_meeting_planning_article.py build_head/build_body), so we don't
break the site's scaffolding. Output is written to blog/ (the deploy dir).

Markdown is parsed manually:
  - YAML front matter (title, description, lang, slug, date) -> head meta
  - First non-meta paragraph stays as intro <p>
  - "## Heading" -> <h2>Heading</h2>
  - "- item"     -> <ul><li>item</li></ul>
  - blank line   -> paragraph break
  - other lines  -> <p>

We add hreflang links for ALL 12 site languages (en, es, de, fr, it, ja, ru,
uk, zh, pt, ar, hi). pt/ar/hi are not yet in gen_sitemap's LANGS, so the
sitemap is patched separately (see patch_sitemap_for_pt_ar_hi below / external).
"""
import os
import re
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content", "blog")
BLOG = os.path.join(ROOT, "blog")
SITE = "https://worldtimessync.com"

# All 12 languages the site ships content for (folders exist for all).
ALL_LANGS = ["en", "es", "de", "fr", "it", "ja", "ru", "uk", "zh", "pt", "ar", "hi"]

# UI strings for breadcrumb/skip, mirroring other localized posts.
UI = {
    "en": {"home": "Home", "blog": "Blog", "skip": "Skip to main content",
           "date": "August 27, 2026", "read": "5 min read", "cats": "Time Zones, Guides"},
    "es": {"home": "Inicio", "blog": "Blog", "skip": "Saltar al contenido",
           "date": "27 de agosto de 2026", "read": "5 min de lectura", "cats": "Husos horarios, Guías"},
    "de": {"home": "Start", "blog": "Blog", "skip": "Zum Inhalt springen",
           "date": "27. August 2026", "read": "5 Min. Lesezeit", "cats": "Zeitzonen, Ratgeber"},
    "fr": {"home": "Accueil", "blog": "Blog", "skip": "Aller au contenu",
           "date": "27 août 2026", "read": "5 min de lecture", "cats": "Fuseaux horaires, Guides"},
    "it": {"home": "Home", "blog": "Blog", "skip": "Vai al contenuto",
           "date": "27 agosto 2026", "read": "5 min di lettura", "cats": "Fusi orari, Guide"},
    "ja": {"home": "ホーム", "blog": "ブログ", "skip": "メインコンテンツへ",
           "date": "2026年8月27日", "read": "約5分", "cats": "タイムゾーン, ガイド"},
    "ru": {"home": "Главная", "blog": "Блог", "skip": "Перейти к содержанию",
           "date": "27 августа 2026", "read": "5 мин чтения", "cats": "Часовые пояса, Гайды"},
    "uk": {"home": "Головна", "blog": "Блог", "skip": "Перейти до вмісту",
           "date": "27 серпня 2026", "read": "5 хв читання", "cats": "Часові пояси, Гайди"},
    "zh": {"home": "首页", "blog": "博客", "skip": "跳到主要内容",
           "date": "2026年8月27日", "read": "阅读约5分钟", "cats": "时区, 指南"},
    "pt": {"home": "Início", "blog": "Blog", "skip": "Pular para o conteúdo",
           "date": "27 de agosto de 2026", "read": "5 min de leitura", "cats": "Fusos horários, Guias"},
    "ar": {"home": "الرئيسية", "blog": "المدونة", "skip": "تخطَّ إلى المحتوى",
           "date": "27 أغسطس 2026", "read": "5 دقائق قراءة", "cats": "المناطق الزمنية، أدلة"},
    "hi": {"home": "होम", "blog": "ब्लॉग", "skip": "मुख्य सामग्री पर जाएँ",
           "date": "27 अगस्त 2026", "read": "5 मिनट पढ़ें", "cats": "समय-मंडल, गाइड"},
}


def parse_md(path):
    text = open(path, encoding="utf-8").read()
    # split front matter
    fm = {}
    body = text
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if m:
        fm_text, body = m.group(1), m.group(2)
        for line in fm_text.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                v = v.strip()
                # strip surrounding quotes if present
                if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                    v = v[1:-1]
                fm[k.strip()] = v
    # build HTML body
    html_parts = []
    in_list = False

    def close_list():
        nonlocal in_list
        if in_list:
            html_parts.append("</ul>")
            in_list = False

    for raw in body.splitlines():
        line = raw.rstrip()
        if not line.strip():
            close_list()
            continue
        if line.startswith("## "):
            close_list()
            html_parts.append("<h2>%s</h2>" % escape(line[3:].strip()))
            continue
        if line.startswith("- "):
            if not in_list:
                html_parts.append("<ul>")
                in_list = True
            html_parts.append("<li>%s</li>" % escape(line[2:].strip()))
            continue
        close_list()
        html_parts.append("<p>%s</p>" % escape(line.strip()))
    close_list()
    content_html = "\n".join(html_parts)
    return fm, content_html


def hreflang_links(slug, en_file, present):
    """present: dict lang->filename (without .html)."""
    links = []
    links.append(
        '<link rel="alternate" hreflang="x-default" href="%s/blog/%s">' % (SITE, en_file))
    for lang in ALL_LANGS:
        if lang == "en":
            links.append('<link rel="alternate" hreflang="en" href="%s/blog/%s">' % (SITE, en_file))
        else:
            f = present.get(lang)
            if f:
                links.append('<link rel="alternate" hreflang="%s" href="%s/blog/%s">' % (lang, SITE, f))
    return "\n    ".join(links)


def build_head(lang, fm, slug, href_block):
    title = fm["title"]
    desc = fm["description"]
    h1 = title
    kw = fm.get("keywords") or fm.get("title", "")
    date = fm.get("date", "2026-08-27")
    return '''<!doctype html>
<html lang="%s">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <meta name="theme-color" content="#667eea">
    <meta name="google-site-verification" content="tNRYRY4K5ZdeEBPId3_g0GiclaIlooP5GhihYhXwknk">
    <title>%s</title>
    <meta name="title" content="%s">
    <meta name="description" content="%s">
    <meta name="keywords" content="%s">
    <meta name="robots" content="index, follow">
    <meta name="author" content="World Time Sync">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://worldtimessync.com/blog/%s">
    <meta property="og:title" content="%s">
    <meta property="og:description" content="%s">
    <meta property="og:image" content="https://worldtimessync.com/og-image.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="%s">
    <meta name="twitter:description" content="%s">
    <link rel="canonical" href="https://worldtimessync.com/blog/%s">
    %s
    <link rel="preload" href="/assets/blog.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="/assets/blog.css"></noscript>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="stylesheet" href="/assets/index-ufePLcBr.css">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-LBX0CDYSSV"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-LBX0CDYSSV');
    </script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9728257902981529" crossorigin="anonymous"></script>
    <script type="application/ld+json">
    {"@context": "https://schema.org", "@type": "BlogPosting", "headline": "%s", "description": "%s", "author": {"@type": "Organization", "name": "World Time Sync", "url": "https://worldtimessync.com"}, "publisher": {"@type": "Organization", "name": "World Time Sync", "url": "https://worldtimessync.com"}, "datePublished": "%s", "dateModified": "%s", "mainEntityOfPage": {"@type": "WebPage", "id": "https://worldtimessync.com/blog/%s"}, "image": "https://worldtimessync.com/og-image.png", "inLanguage": "%s"}
    </script>
    <script type="application/ld+json">
    {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "%s", "item": "https://worldtimessync.com/"}, {"@type": "ListItem", "position": 2, "name": "%s", "item": "https://worldtimessync.com/#blog"}, {"@type": "ListItem", "position": 3, "name": "%s", "item": "https://worldtimessync.com/blog/%s"}]}
    </script>
</head>''' % (
        lang, title, title, desc, kw,
        slug + ".html", title, desc, title, desc,
        slug + ".html", href_block,
        escape(title), escape(desc), date, date, slug + ".html", lang,
        UI[lang]["home"], UI[lang]["blog"], escape(h1), slug + ".html",
    )


def build_body(lang, fm, content_html):
    ui = UI[lang]
    h1 = fm["title"]
    return '''<body>
    <a href="#main-content" class="skip-link">%s</a>
    <div id="root" role="application" aria-label="World Time Online Application">
        <div class="app-loading" aria-busy="true" aria-live="polite">
            <div class="app-loading-spinner" role="status" aria-label="Loading application"></div>
            <p class="app-loading-text">Loading World Time...</p>
        </div>
    </div>
    <main id="main-content">
        <article class="blog-wrap">
            <nav class="blog-breadcrumb" aria-label="Breadcrumb">
                <a href="/">%s</a> &#8250; <a href="/#blog">%s</a> &#8250; <span aria-current="page">%s</span>
            </nav>
            <h1>%s</h1>
            <div class="blog-meta">&#128197; %s &nbsp;&middot;&nbsp; &#9201; %s &nbsp;&middot;&nbsp; &#127991; %s</div>
%s
        </article>
    </main>
    <script type="module" src="/assets/index-Dd7au40z.js" async></script>
    <script>
      document.addEventListener('DOMContentLoaded', function() {
        var seo = document.querySelector('.blog-wrap');
        if (seo) seo.style.display = 'none';
      });
    </script>
    <script>
      window.addEventListener('load',function(){
        var ahrefs=document.createElement('script');
        ahrefs.async=true;
        ahrefs.src='https://analytics.ahrefs.com/analytics.js';
        ahrefs.setAttribute('data-key','hB1VYWuwb1i/f1d8re7P2A');
        document.head.appendChild(ahrefs);
      });
    </script>
  </body>
</html>''' % (
        ui["skip"], ui["home"], ui["blog"], h1, h1,
        ui["date"], ui["read"], ui["cats"], content_html,
    )


def main():
    os.makedirs(BLOG, exist_ok=True)
    # discover slugs
    slugs = {}
    for fn in os.listdir(CONTENT):
        if not fn.endswith(".md"):
            continue
        stem = fn[:-3]  # strip .md
        if stem.endswith("-en"):
            slug = stem[:-3]
            slugs.setdefault(slug, {})["en"] = fn
        elif "-" in stem:
            slug, lang = stem.rsplit("-", 1)
            if lang in ALL_LANGS:
                slugs.setdefault(slug, {})[lang] = fn
        else:
            slugs.setdefault(stem, {})["en"] = fn

    written = 0
    for slug, files in slugs.items():
        if "en" not in files:
            print("SKIP slug %s: no EN source" % slug)
            continue
        present = {}
        # en file name
        en_fn = slug if files["en"] == (slug + ".md") else (slug + ".html")
        present["en"] = slug + ".html"
        for lang in ALL_LANGS:
            if lang == "en":
                continue
            if lang in files:
                # Special case: '-uk' collides with the existing "Best Time to
                # Call the UK" country article (which uses -uk suffix). To avoid
                # overwriting it, the Ukrainian translation of THIS article uses
                # the '-ukr' suffix instead.
                suffix = "ukr" if lang == "uk" else lang
                present[lang] = "%s-%s.html" % (slug, suffix)
        href_block = hreflang_links(slug, slug + ".html", present)
        for lang, mdfile in files.items():
            fm, content = parse_md(os.path.join(CONTENT, mdfile))
            fm["title"] = fm.get("title", slug)
            fm["description"] = fm.get("description", "")
            if lang == "en":
                out_name = slug + ".html"
            elif lang == "uk":
                out_name = slug + "-ukr.html"
            else:
                out_name = "%s-%s.html" % (slug, lang)
            html = build_head(lang, fm, slug, href_block) + "\n" + build_body(lang, fm, content)
            with open(os.path.join(BLOG, out_name), "w", encoding="utf-8") as f:
                f.write(html)
            written += 1
            print("wrote blog/%s" % out_name)
    print("done: %d files" % written)


if __name__ == "__main__":
    main()
