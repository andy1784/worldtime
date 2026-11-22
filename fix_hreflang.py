#!/usr/bin/env python3
"""Fix hreflang URLs and html lang in generated articles."""
from pathlib import Path
import re

BASE = Path('/home/kaliuser/worldtime')

LANGS = ['zh', 'it', 'de', 'fr', 'pt', 'ru', 'ja', 'uk', 'hi', 'ar']

for lang in LANGS:
    path = BASE / lang / 'blog' / f'check-current-time-any-city-{lang}.html'
    html = path.read_text(encoding='utf-8')
    
    # Fix html lang
    html = html.replace('<html lang="en">', f'<html lang="{lang}">')
    
    # Fix hreflang URLs - each should point to its own language version
    # The pattern is: <link rel="alternate" hreflang="xx" href="https://worldtimessync.com/zh/blog/...">
    # Should be: <link rel="alternate" hreflang="xx" href="https://worldtimessync.com/xx/blog/...">
    
    # Fix x-default
    html = html.replace(
        f'https://worldtimessync.com/zh/blog/check-current-time-any-city-zh.html',
        f'https://worldtimessync.com/{lang}/blog/check-current-time-any-city-{lang}.html'
    )
    
    # Fix each hreflang
    for other_lang in ['en', 'es', 'zh', 'it', 'de', 'fr', 'pt', 'ru', 'ja', 'uk', 'hi', 'ar']:
        if other_lang == lang:
            # self-referencing - should use own URL
            old = f'hreflang="{other_lang}" href="https://worldtimessync.com/zh/blog/check-current-time-any-city-zh.html"'
            new = f'hreflang="{other_lang}" href="https://worldtimessync.com/{lang}/blog/check-current-time-any-city-{lang}.html"'
            html = html.replace(old, new)
        else:
            # other languages - should point to their own versions
            old = f'hreflang="{other_lang}" href="https://worldtimessync.com/zh/blog/check-current-time-any-city-zh.html"'
            if other_lang == 'en':
                new = f'hreflang="{other_lang}" href="https://worldtimessync.com/blog/check-current-time-any-city.html"'
            else:
                new = f'hreflang="{other_lang}" href="https://worldtimessync.com/{other_lang}/blog/check-current-time-any-city-{other_lang}.html"'
            html = html.replace(old, new)
    
    # Fix BreadcrumbList - position 2 should be the language's blog index
    html = html.replace(
        '"item": "https://worldtimessync.com/blog/"',
        f'"item": "https://worldtimessync.com/{lang}/blog/"'
    )
    
    # Fix hreflang in BreadcrumbList position 3
    html = html.replace(
        f'"item": "https://worldtimessync.com/zh/blog/check-current-time-any-city-zh.html"',
        f'"item": "https://worldtimessync.com/{lang}/blog/check-current-time-any-city-{lang}.html"'
    )
    
    # Fix the blog link in breadcrumb (position 2) - should be /{lang}/blog/
    html = html.replace(
        '<a href="/blog/">博客</a>',
        f'<a href="/{lang}/blog/">博客</a>'
    ).replace(
        '<a href="/blog/">Blog</a>',
        f'<a href="/{lang}/blog/">Blog</a>'
    ).replace(
        '<a href="/blog/">Blog</a>',
        f'<a href="/{lang}/blog/">Blog</a>'
    )
    
    # Fix home link in breadcrumb
    html = html.replace(
        '<a href="/">Home</a>',
        f'<a href="/{lang}/">Home</a>'
    ).replace(
        '<a href="/">首页</a>',
        f'<a href="/{lang}/">首页</a>'
    ).replace(
        '<a href="/">Главная</a>',
        f'<a href="/{lang}/">Главная</a>'
    ).replace(
        '<a href="/">ホーム</a>',
        f'<a href="/{lang}/">ホーム</a>'
    ).replace(
        '<a href="/">Головна</a>',
        f'<a href="/{lang}/">Головна</a>'
    ).replace(
        '<a href="/">होम</a>',
        f'<a href="/{lang}/">होम</a>'
    ).replace(
        '<a href="/">الرئيسية</a>',
        f'<a href="/{lang}/">الرئيسية</a>'
    ).replace(
        '<a href="/">Inicio</a>',
        f'<a href="/{lang}/">Inicio</a>'
    ).replace(
        '<a href="/">Accueil</a>',
        f'<a href="/{lang}/">Accueil</a>'
    ).replace(
        '<a href="/">Início</a>',
        f'<a href="/{lang}/">Início</a>'
    ).replace(
        '<a href="/">Start</a>',
        f'<a href="/{lang}/">Start</a>'
    )
    
    path.write_text(html, encoding='utf-8')
    print(f'Fixed {path}')

print('Done!')