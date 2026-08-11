#!/usr/bin/env python3
"""Generate all 8 translations for the new time-zone-abbreviations-cheat-sheet article from translation files."""
import os
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')
BLOG_DIR = BASE / 'blog'
TRANS_DIR = BASE / 'translations'

slug = 'time-zone-abbreviations-cheat-sheet'
slug_en = slug

LANGS = {
    'es': {'home': 'Inicio', 'blog': 'Blog', 'date': '10 ago 2026', 'read': '8 min de lectura',
           'skip': 'Saltar al contenido principal', 'loading': 'Cargando la hora...'},
    'zh': {'home': '首页', 'blog': '博客', 'date': '2026年8月10日', 'read': '阅读 8 分钟',
           'skip': '跳到主要内容', 'loading': '正在加载时间...'},
    'it': {'home': 'Home', 'blog': 'Blog', 'date': '10 ago 2026', 'read': '8 min di lettura',
           'skip': 'Vai al contenuto principale', 'loading': 'Caricamento ora...'},
    'de': {'home': 'Start', 'blog': 'Blog', 'date': '10. Aug 2026', 'read': '8 Min. Lesezeit',
           'skip': 'Zum Hauptinhalt springen', 'loading': 'Zeit wird geladen...'},
    'ja': {'home': 'ホーム', 'blog': 'ブログ', 'date': '2026年8月10日', 'read': '読了 8 分',
           'skip': 'メインコンテンツへ移動', 'loading': '時刻を読み込み中...'},
    'fr': {'home': 'Accueil', 'blog': 'Blog', 'date': '10 août 2026', 'read': '8 min de lecture',
           'skip': 'Aller au contenu principal', 'loading': "Chargement de l'heure..."},
    'uk': {'home': 'Головна', 'blog': 'Блог', 'date': '10 лип 2026', 'read': '8 хв читання',
           'skip': 'Перейти до основного вмісту', 'loading': 'Завантаження часу...'},
    'ru': {'home': 'Главная', 'blog': 'Блог', 'date': '10 авг 2026', 'read': '8 мин чтения',
           'skip': 'Перейти к основному содержанию', 'loading': 'Загрузка времени...'},
}

# Read translation files
def read_translation(lang):
    path = TRANS_DIR / f'{lang}.txt'
    text = path.read_text(encoding='utf-8')
    lines = text.strip().split('\n')
    return {
        'title': lines[0].split(':', 1)[1].strip(),
        'meta_desc': lines[1].strip(),
        'keywords': lines[2].strip(),
        'h1': lines[3].strip(),
        'content': '\n'.join(lines[4:]),
    }

# Template strings using double braces for literal braces
HEAD_TEMPLATE = '''<!doctype html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <meta name="theme-color" content="#667eea">
    <meta name="google-site-verification" content="tNRYRY4K5ZdeEBPId3_g0GiclaIlooP5GhihYhXwknk">
    <title>{title} | World Time Sync</title>
    <meta name="title" content="{title} | World Time Sync">
    <meta name="description" content="{meta_desc}">
    <meta name="keywords" content="{keywords}">
    <meta name="robots" content="index, follow">
    <meta name="author" content="World Time Sync">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://worldtimessync.com/blog/{lang}-{slug}">
    <meta property="og:title" content="{title} | World Time Sync">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:image" content="https://worldtimessync.com/og-image.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title} | World Time Sync">
    <link rel="canonical" href="https://worldtimessync.com/blog/{lang}-{slug}">
    {hreflang_str}
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://cdn.worldtimessync.com" crossorigin>
    <link rel="stylesheet" href="/blog-styles.css" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="/blog-styles.css"></noscript>
    <style>
        .tz-table {{width:100%;border-collapse:collapse;margin:1.5rem 0;font-size:0.9rem}}
        .tz-table th,.tz-table td {{border:1px solid #e2e8f0;padding:0.5rem 0.75rem;text-align:left}}
        .tz-table th {{background:#f1f5f9;font-weight:600}}
        .tz-table tr:nth-child(even) {{background:#f8fafc}}
        @media (max-width:640px) {{.tz-table {{font-size:0.8rem}} .tz-table th,.tz-table td {{padding:0.35rem 0.5rem}}}}
    </style>
    <script type="application/ld+json">{{
        "@context":"https://schema.org",
        "@type":"Article",
        "headline":"{title}",
        "description":"{meta_desc}",
        "image":"https://worldtimessync.com/og-image.png",
        "author":{{"@type":"Organization","name":"World Time Sync","url":"https://worldtimessync.com"}},
        "publisher":{{"@type":"Organization","name":"World Time Sync","logo":{{"@type":"ImageObject","url":"https://worldtimessync.com/logo.png"}}}},
        "datePublished":"2026-08-10T00:00:00+00:00",
        "dateModified":"2026-08-10T00:00:00+00:00",
        "mainEntityOfPage":{{"@type":"WebPage","@id":"https://worldtimessync.com/blog/{lang}-{slug}"}}
    }}</script>
    <script type="application/ld+json">{{
        "@context":"https://schema.org",
        "@type":"BreadcrumbList",
        "itemListElement":[
            {{"@type":"ListItem","position":1,"name":"{home}","item":"https://worldtimessync.com/"}},
            {{"@type":"ListItem","position":2,"name":"{blog}","item":"https://worldtimessync.com/blog/"}},
            {{"@type":"ListItem","position":3,"name":"{title}","item":"https://worldtimessync.com/blog/{lang}-{slug}"}}
        ]
    }}</script>
</head>'''

BODY_TEMPLATE = '''<body>
    <a href="#main" class="skip-link">{skip}</a>
    <header class="site-header">
        <div class="container">
            <a href="/" class="logo" aria-label="World Time Sync — Home">
                <svg width="32" height="32" viewBox="0 0 32 32" fill="none" aria-hidden="true"><circle cx="16" cy="16" r="14" stroke="#667eea" stroke-width="3"/><path d="M16 6v10l6 6" stroke="#667eea" stroke-width="3" stroke-linecap="round"/></svg>
                <span>World Time Sync</span>
            </a>
            <nav class="lang-nav" aria-label="Language selection">
                <select id="lang-select" onchange="window.location.href=this.value">
                    <option value="/" {en_selected}>English</option>
                    <option value="/es/" {es_selected}>Español</option>
                    <option value="/zh/" {zh_selected}>中文</option>
                    <option value="/ru/" {ru_selected}>Русский</option>
                    <option value="/de/" {de_selected}>Deutsch</option>
                    <option value="/ja/" {ja_selected}>日本語</option>
                    <option value="/fr/" {fr_selected}>Français</option>
                    <option value="/it/" {it_selected}>Italiano</option>
                    <option value="/uk/" {uk_selected}>Українська</option>
                </select>
            </nav>
        </div>
    </header>
    <main id="main" class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
            <ol>
                <li><a href="/">{home}</a></li>
                <li><a href="/blog/">Blog</a></li>
                <li aria-current="page">{h1}</li>
            </ol>
        </nav>
        <article class="blog-post">
            <header class="post-header">
                <h1>{h1}</h1>
                <div class="post-meta">
                    <time datetime="2026-08-10">{meta_date}</time>
                    <span class="read-time">{meta_read}</span>
                </div>
            </header>
            <div class="post-content">
                {content}
            </div>
        </article>
        <footer class="site-footer">
            <div class="container">
                <p>© 2026 World Time Sync. All rights reserved.</p>
                <nav aria-label="Footer navigation">
                    <a href="/privacy.html">Privacy</a> · <a href="/about.html">About</a> · <a href="/contact.html">Contact</a>
                </nav>
            </div>
        </footer>
    </main>
    <script>
        const lang = '{lang}';
        const loadingText = '{loading}';
        const urlParams = new URLSearchParams(window.location.search);
        const city = urlParams.get('city');
        if (city) {{
            const params = new URLSearchParams();
            params.set('city', city);
            ['date','tz1','tz2','tz3'].forEach(k => {{ if (urlParams.get(k)) params.set(k, urlParams.get(k)); }});
            window.location.href = '/time-zone-converter.html?' + params.toString();
        }}
        document.getElementById('lang-select').value = '/' + lang + '/';
    </script>
</body>
</html>'''

def main():
    present_langs = ['es', 'zh', 'it', 'de', 'ja', 'fr', 'uk', 'ru']
    created = 0
    for lang in present_langs:
        t = read_translation(lang)
        l = LANGS[lang]
        
        # Build hreflang
        hreflangs = []
        hreflangs.append('<link rel="alternate" hreflang="x-default" href="https://worldtimessync.com/blog/{slug_en}">'.format(slug_en=slug_en))
        hreflangs.append('<link rel="alternate" hreflang="en" href="https://worldtimessync.com/blog/{slug_en}">'.format(slug_en=slug_en))
        for pl in present_langs:
            if pl == 'en':
                continue
            hreflangs.append('<link rel="alternate" hreflang="{pl}" href="https://worldtimessync.com/blog/{slug}-{pl}">'.format(pl=pl, slug=slug))
        hreflang_str = '\n    '.join(hreflangs)
        
        # Language select options
        def sel(current, target):
            return 'selected' if current == target else ''
        
        head = HEAD_TEMPLATE.format(
            lang=lang,
            title=t['title'],
            meta_desc=t['meta_desc'],
            keywords=t['keywords'],
            slug=slug,
            slug_en=slug_en,
            home=l['home'],
            blog=l['blog'],
            hreflang_str=hreflang_str,
        )
        
        body = BODY_TEMPLATE.format(
            lang=lang,
            skip=l['skip'],
            home=l['home'],
            h1=t['h1'],
            meta_date=l['date'],
            meta_read=l['read'],
            content=t['content'],
            loading=l['loading'],
            en_selected=sel(lang, 'en'),
            es_selected=sel(lang, 'es'),
            zh_selected=sel(lang, 'zh'),
            ru_selected=sel(lang, 'ru'),
            de_selected=sel(lang, 'de'),
            ja_selected=sel(lang, 'ja'),
            fr_selected=sel(lang, 'fr'),
            it_selected=sel(lang, 'it'),
            uk_selected=sel(lang, 'uk'),
        )
        
        html = head + '\n' + body
        out_path = BLOG_DIR / f'{slug}-{lang}.html'
        out_path.write_text(html, encoding='utf-8')
        print(f'Created {out_path.name} ({len(html)} bytes)')
        created += 1
    print(f'\nDone. {created} translation files created.')

if __name__ == '__main__':
    main()