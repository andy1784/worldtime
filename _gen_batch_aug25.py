#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate human-quality localized posts for two slugs x 8 languages."""
import os

BLOG = '/home/kaliuser/worldtime/blog'

def hreflang(slug, lang):
    en = f'https://worldtimessync.com/blog/{slug}'
    lines = [f'<link rel="alternate" hreflang="x-default" href="{en}">',
             f'<link rel="alternate" hreflang="en" href="{en}">']
    for l in ['es','zh','ru','it','de','ja','fr','uk']:
        lines.append(f'<link rel="alternate" hreflang="{l}" href="{en}-{l}">')
    return '\n    '.join(lines)

def build_post(slug, lang, title, desc, kw, breadcrumb, meta_line, h1, body_html, faq, date_iso, read_time):
    faq_json = faq.replace('\n', ' ')
    html = f'''<!doctype html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <meta name="theme-color" content="#667eea">
    <meta name="google-site-verification" content="tNRYRY4K5ZdeEBPId3_g0GiclaIlooP5GhihYhXwknk">
    <title>{title}</title>
    <meta name="title" content="{title}">
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{kw}">
    <meta name="robots" content="index, follow">
    <meta name="author" content="World Time Sync">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://worldtimessync.com/blog/{slug}-{lang}.html">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="article:published_time" content="{date_iso}">
    <meta property="article:modified_time" content="{date_iso}">
    <meta property="article:author" content="https://worldtimessync.com/">
    <meta property="article:publisher" content="https://worldtimessync.com/">
    <meta property="og:image" content="https://worldtimessync.com/og-image.png">
    <meta property="og:site_name" content="World Time Sync">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://worldtimessync.com/og-image.png">
    <meta name="twitter:title" content="{title}">
    <link rel="canonical" href="https://worldtimessync.com/blog/{slug}-{lang}.html">
    {hreflang(slug, lang)}
    <link rel="preload" href="/assets/blog.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="/assets/blog.css"></noscript>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="stylesheet" href="/assets/index-ufePLcBr.css">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-LBX0CDYSSV"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-LBX0CDYSSV');
    </script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9728257902981529" crossorigin="anonymous"></script>
    <script type="application/ld+json">
    {{"@context": "https://schema.org", "@type": "BlogPosting", "headline": "{title}", "description": "{desc}", "author": {{"@type": "Organization", "name": "World Time Sync", "url": "https://worldtimessync.com"}}, "publisher": {{"@type": "Organization", "name": "World Time Sync", "url": "https://worldtimessync.com"}}, "datePublished": "{date_iso}", "dateModified": "{date_iso}", "mainEntityOfPage": {{"@type": "WebPage", "@id": "https://worldtimessync.com/blog/{slug}-{lang}.html"}}, "image": "https://worldtimessync.com/og-image.png"}}
    </script>
    <script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "{breadcrumb[0]}", "item": "https://worldtimessync.com/"}}, {{"@type": "ListItem", "position": 2, "name": "{breadcrumb[1]}", "item": "https://worldtimessync.com/"}}, {{"@type": "ListItem", "position": 3, "name": "{breadcrumb[2]}", "item": "https://worldtimessync.com/blog/{slug}-{lang}.html"}}]}}</script>
    <script type="application/ld+json">
    {faq_json}
    </script>
    <link rel="preload" as="script" href="/assets/index-Dd7au40z.js" fetchpriority="high">
</head>
<body>
    <a href="#main-content" class="skip-link">{breadcrumb[3]}</a>
    <div id="root" role="application" aria-label="World Time Online Application">
        <div class="app-loading" aria-busy="true" aria-live="polite">
            <div class="app-loading-spinner" role="status" aria-label="{breadcrumb[4]}"></div>
            <p class="app-loading-text">{breadcrumb[4]}</p>
        </div>
    </div>
    <main id="main-content">
        <article class="blog-wrap">
            <nav class="blog-breadcrumb" aria-label="{breadcrumb[5]}">
                <a href="/">{breadcrumb[0]}</a> › <a href="/#blog">{breadcrumb[1]}</a> › <span aria-current="page">{breadcrumb[2]}</span>
            </nav>
            <h1>{h1}</h1>
            <div class="blog-meta">{meta_line}</div>
{body_html}
        </article>
        <footer class="blog-footer">
            <a href="/privacy">{breadcrumb[6]}</a>
            <a href="/about">{breadcrumb[7]}</a>
            <a href="/contact">{breadcrumb[8]}</a>
            <a href="/terms">{breadcrumb[9]}</a>
            <p style="margin-top:8px;color:#444;font-size:0.75rem">&copy; 2026 World Time Sync</p>
        </footer>
    </main>
    <script type="module" src="/assets/index-Dd7au40z.js" async></script>
    <script>
      document.addEventListener('DOMContentLoaded', function() {{
        var seo = document.querySelector('.blog-wrap');
        if (seo) seo.style.display = "none";
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
</html>'''
    path = os.path.join(BLOG, f'{slug}-{lang}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('written', path, len(html))

from gen_bho import POSTS_BHO
from gen_bho2 import POSTS_BHO2
POSTS_BHO = POSTS_BHO + POSTS_BHO2
from gen_au import POSTS_AU
from gen_au2 import POSTS_AU2
from gen_au3 import POSTS_AU3
POSTS_AU = POSTS_AU + POSTS_AU2 + POSTS_AU3

for slug, posts, fix_h1 in (('business-hours-overlap', POSTS_BHO, False),
                            ('daylight-saving-time-australia-how-it-works', POSTS_AU, True)):
    for p in posts:
        if fix_h1:
            p = list(p); p.insert(6, p[5][2]); p = tuple(p)
        build_post(slug, *p)
print('DONE')
