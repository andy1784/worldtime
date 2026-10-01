#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shared renderer for the "Antarctica time zones" post cluster (12 languages).

Why not reuse gen_blog_from_md.py:
  - it has no FAQPage schema
  - it emits og:url/canonical with ".html" while hreflang is extensionless
  - it has no RTL support for Arabic
  - its UI dict hardcodes one date/read-time for every post
  - it rewrites the "-uk" suffix to "-ukr" to dodge a slug collision that does
    not apply to this article
So this module renders one clean, self-consistent cluster and touches nothing else.

Import from blog/_gen_antarctica.py.  Output: blog/antarctica-time-zones-every-utc-offset[-<lang>].html
"""
import json
import re

SITE = "https://worldtimessync.com"
SLUG = "antarctica-time-zones-every-utc-offset"

# en first, then the 11 localized site languages
LANGS = ["en", "es", "de", "fr", "it", "ja", "ru", "uk", "zh", "pt", "ar", "hi"]
RTL = {"ar"}

UI = {
    "en": ("Home", "Blog", "Skip to main content"),
    "es": ("Inicio", "Inicio", "Saltar al contenido"),
    "de": ("Start", "Blog", "Zum Inhalt springen"),
    "fr": ("Accueil", "Blog", "Aller au contenu"),
    "it": ("Home", "Blog", "Vai al contenuto"),
    "ja": ("ホーム", "ブログ", "メインコンテンツへ"),
    "ru": ("Главная", "Блог", "Перейти к содержанию"),
    "uk": ("Головна", "Блог", "Перейти до вмісту"),
    "zh": ("首页", "博客", "跳到主要内容"),
    "pt": ("Início", "Blog", "Pular para o conteúdo"),
    "ar": ("الرئيسية", "المدونة", "تخطَّ إلى المحتوى"),
    "hi": ("होम", "ब्लॉग", "मुख्य सामग्री पर जाएँ"),
}

# Breadcrumb label for "Blog" per language (UI[1] is the site root, UI[2] is skip)
BLOG_LABEL = {
    "en": "Blog", "es": "Blog", "de": "Blog", "fr": "Blog", "it": "Blog",
    "ja": "ブログ", "ru": "Блог", "uk": "Блог", "zh": "博客", "pt": "Blog",
    "ar": "المدونة", "hi": "ब्लॉग",
}


def url_for(lang):
    """Public, extensionless URL for a language in this cluster."""
    return f"{SITE}/blog/{SLUG}" if lang == "en" else f"{SITE}/blog/{SLUG}-{lang}"


def file_for(lang):
    return f"{SLUG}.html" if lang == "en" else f"{SLUG}-{lang}.html"


def hreflang_block():
    """x-default + en + all 11 localized. Every href is the real file location."""
    lines = [f'    <link rel="alternate" hreflang="x-default" href="{url_for("en")}">']
    for lang in LANGS:
        lines.append(f'    <link rel="alternate" hreflang="{lang}" href="{url_for(lang)}">')
    return "\n".join(lines)


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


_TAG_RE = re.compile(r'</?(?:strong|em|code|a)(\s[^>]*)?>')


def _inline(s):
    """Escape text, but pass through the handful of tags we author by hand.

    Stash real tags behind sentinels first, otherwise the closing tag
    `</strong>` survives escaping as `&lt;/strong&gt;`."""
    kept = []

    def stash(m):
        kept.append(m.group(0))
        return f"\x00{len(kept) - 1}\x00"

    s = _TAG_RE.sub(stash, s)
    s = esc(s)
    return re.sub(r"\x00(\d+)\x00", lambda m: kept[int(m.group(1))], s)


def render_blocks(blocks):
    out = []
    for kind, payload in blocks:
        if kind == "p":
            out.append(f"            <p>{_inline(payload)}</p>")
        elif kind == "h2":
            out.append(f"            <h2>{esc(payload)}</h2>")
        elif kind == "h3":
            out.append(f"            <h3>{esc(payload)}</h3>")
        elif kind == "ul":
            out.append("            <ul>\n" + "\n".join(
                f"                <li>{_inline(i)}</li>" for i in payload
            ) + "\n            </ul>")
        elif kind == "quote":
            out.append(f"            <blockquote>{_inline(payload)}</blockquote>")
        elif kind == "table":
            head, rows = payload
            th = "\n".join(f"                    <th>{esc(h)}</th>" for h in head)
            body = "\n".join(
                "                    <tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>"
                for r in rows)
            out.append("            <table>\n"
                       "                <thead>\n                    <tr>\n"
                       + th + "\n                    </tr>\n                </thead>\n"
                       "                <tbody>\n" + body + "\n                </tbody>\n"
                       "            </table>")
        elif kind == "faq":
            out.append('            <div class="faq-section">')
            for q, a in payload:
                out.append(f'                <div class="faq-item"><h3>{esc(q)}</h3>'
                           f"<p>{_inline(a)}</p></div>")
            out.append("            </div>")
        elif kind == "tags":
            out.append('            <div class="post-tags">' + " ".join(
                f'<span class="tag">{esc(t)}</span>' for t in payload) + "</div>")
        else:
            raise ValueError(f"unknown block kind: {kind}")
    return "\n".join(out)


def word_count(blocks):
    text = " ".join(
        (p if isinstance(p, str) else " ".join(map(str, p)))
        for _, p in blocks
    )
    text = re.sub(r"<[^>]+>", " ", text)
    # CJK text is not whitespace-delimited, so a naive split undercounts badly
    # (a 1400-character Japanese article came out as ~160 "words"). Count each
    # CJK character as a word instead, which is the usual approximation.
    cjk = re.findall(r"[\u3040-\u30ff\u3400-\u9fff]", text)
    rest = re.sub(r"[\u3040-\u30ff\u3400-\u9fff]", " ", text)
    words = [w for w in re.split(r"\s+", rest) if w.strip()]
    return len(words) + len(cjk)


def faq_pairs(blocks):
    for kind, payload in blocks:
        if kind == "faq":
            return payload
    return []


def build(lang, meta, blocks):
    """meta: dict with title, desc, kw, date, date_iso, read, tags, short_h1"""
    home, blog, skip = UI[lang]
    rtl = ' dir="rtl"' if lang in RTL else ""
    url = url_for(lang)
    canonical = f"{SITE}/blog/{file_for(lang)}"
    title = meta["title"]
    full_title = f"{title} | World Time Sync"
    desc = meta["desc"]
    kw = meta["kw"]
    d = meta["date_iso"]
    read = meta["read"]
    cats = meta["tags"]
    words = word_count(blocks)

    faq = faq_pairs(blocks)
    faq_schema = json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq],
    }, ensure_ascii=False)

    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Organization", "name": "World Time Sync", "url": f"{SITE}/",
             "logo": {"@type": "ImageObject", "url": f"{SITE}/logo.png",
                      "width": 512, "height": 512}},
            {"@type": "WebPage", "@id": f"{url}#webpage", "url": url, "name": title,
             "inLanguage": lang, "datePublished": d, "dateModified": d},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": home, "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": BLOG_LABEL[lang],
                 "item": f"{SITE}/blog/"},
                {"@type": "ListItem", "position": 3, "name": title, "item": url},
            ]},
            {"@type": "BlogPosting", "headline": title, "description": desc,
             "inLanguage": lang, "datePublished": d, "dateModified": d,
             "wordCount": words, "timeRequired": f"PT{read}M",
             "articleSection": cats,
             "keywords": kw,
             "image": f"{SITE}/og-image.png",
             "author": {"@type": "Organization", "name": "World Time Sync", "url": f"{SITE}/"},
             "publisher": {"@type": "Organization", "name": "World Time Sync", "url": f"{SITE}/"},
             "mainEntityOfPage": {"@type": "WebPage", "@id": f"{url}#webpage"}},
        ],
    }

    body = render_blocks(blocks)
    return f"""<!doctype html>
<html lang="{lang}"{rtl}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <meta name="theme-color" content="#667eea">
    <meta name="google-site-verification" content="tNRYRY4K5ZdeEBPId3_g0GiclaIlooP5GhihYhXwknk">
    <title>{esc(full_title)}</title>
    <meta name="title" content="{esc(full_title)}">
    <meta name="description" content="{esc(desc)}">
    <meta name="keywords" content="{esc(kw)}">
    <meta name="robots" content="index, follow">
    <meta name="author" content="World Time Sync">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{esc(full_title)}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="article:published_time" content="{d}">
    <meta property="article:modified_time" content="{d}">
    <meta property="article:author" content="{SITE}/">
    <meta property="article:publisher" content="{SITE}/">
    <meta property="og:image" content="{SITE}/og-image.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:site_name" content="World Time Sync">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{esc(full_title)}">
    <meta name="twitter:description" content="{esc(desc)}">
    <meta name="twitter:image" content="{SITE}/og-image.png">
    <meta name="twitter:image:alt" content="{esc(full_title)}">
    <meta name="twitter:creator" content="World Time Sync">
    <link rel="canonical" href="{url}">
{hreflang_block()}
    <link rel="preload" href="/assets/blog.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="/assets/blog.css"></noscript>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="stylesheet" href="/assets/index-ufePLcBr.css">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-LBX0CDYSSV"></script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XCBTT7YSSY"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-LBX0CDYSSV'); gtag('config', 'G-XCBTT7YSSY');
    </script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9728257902981529" crossorigin="anonymous"></script>
    <script type="application/ld+json">
{json.dumps(graph, ensure_ascii=False, indent=2)}
    </script>
    <script type="application/ld+json">
{faq_schema}
    </script>
</head>
<body>
    <a href="#main-content" class="skip-link">{esc(skip)}</a>
    <div id="root" role="application" aria-label="World Time Online Application">
        <div class="app-loading" aria-busy="true" aria-live="polite">
            <div class="app-loading-spinner" role="status" aria-label="Loading application"></div>
            <p class="app-loading-text">Loading World Time...</p>
        </div>
    </div>
    <main id="main-content">
        <article class="blog-wrap">
            <nav class="blog-breadcrumb" aria-label="Breadcrumb">
                <a href="/">{esc(home)}</a> &#8250; <a href="/blog/">{esc(BLOG_LABEL[lang])}</a> &#8250; <span aria-current="page">{esc(title)}</span>
            </nav>
            <h1>{esc(title)}</h1>
            <div class="blog-meta">&#128197; {esc(meta["date"])} &nbsp;&middot;&nbsp; &#9201; {esc(read)} &nbsp;&middot;&nbsp; &#127991; {esc(cats)}</div>
{body}
        </article>
    </main>
    <script type="module" src="/assets/index-Dd7au40z.js" async></script>
    <script>
      document.addEventListener('DOMContentLoaded', function() {{
        var seo = document.querySelector('.blog-wrap');
        if (seo) seo.style.display = 'none';
      }});
    </script>
    <script>
      window.addEventListener('load',function(){{
        var ahrefs=document.createElement('script');
        ahrefs.async=true;
        ahrefs.src='https://analytics.ahrefs.com/analytics.js';
        ahrefs.setAttribute('data-key','hB1VYWuwb1i/f1d8re7P2A');
        document.head.appendChild(ahrefs);
      }});
    </script>
</body>
</html>"""
