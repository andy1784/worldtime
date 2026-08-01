#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate localized blog index pages: <lang>/blog/index.html for 7 languages.
hreflang on each points to all language variants + x-default/en.
Mirrors the EN blog/index.html structure but with localized UI strings.
"""
import os, json

ROOT = '/home/kaliuser/worldtime'
posts = json.load(open('/tmp/blog_posts_list.json', encoding='utf-8'))

# Localized UI strings: (html_lang, title, description, h1, subtitle, read_more, footer_blog_label)
L10N = {
 'ru': ('ru',
   'Блог World Time — гайды по часовым поясам, советы по конвертации и удалённой работе | World Time Sync',
   'Практические гайды по часовым поясам, расчёту разницы во времени, переходу на летнее время и координации встреч по всему миру. Статьи для удалённых команд, путешественников и бизнеса.',
   'Блог World Time',
   'Практические, написанные человеком гайды по часовым поясам, математике разницы во времени, летнему времени и координации встреч по всему миру.',
   'Читать статью →', 'Блог', 'Как это работает'),
 'es': ('es',
   'Blog de World Time — guías de zonas horarias, consejos de conversión y teletrabajo | World Time Sync',
   'Guías prácticas sobre zonas horarias, cálculo de diferencias horarias, horario de verano y coordinación de reuniones en todo el mundo. Artículos para equipos remotos, viajeros y empresas.',
   'Blog de World Time',
   'Guías prácticas escritas por humanos sobre zonas horarias, cálculo de diferencias horarias, horario de verano y coordinación de reuniones globales.',
   'Leer artículo →', 'Blog', 'Cómo funciona'),
 'zh': ('zh',
   'World Time 博客 — 时区指南、换算技巧与远程工作建议 | World Time Sync',
   '关于时区、时差计算、夏令时以及全球会议协调的实用指南。面向远程团队、旅行者和企业的文章。',
   'World Time 博客',
   '由真人撰写的实用指南，涵盖时区、时差计算、夏令时以及全球会议协调。',
   '阅读全文 →', '博客', '工作原理'),
 'ja': ('ja',
   'World Time ブログ — タイムゾーンガイド、変換のヒント、リモートワーク | World Time Sync',
   'タイムゾーン、時差計算、夏時間、世界中での会議調整に関する実践的なガイド。リモートチーム、旅行者、企業向けの記事。',
   'World Time ブログ',
   'タイムゾーン、時差計算、夏時間、グローバルな会議調整について、人間が書いた実践的なガイド。',
   '記事を読む →', 'ブログ', 'しくみ'),
 'fr': ('fr',
   'Blog World Time — guides de fuseaux horaires, conseils de conversion et télétravail | World Time Sync',
   'Guides pratiques sur les fuseaux horaires, le calcul de décalage, l\'heure d\'été et la coordination de réunions dans le monde. Articles pour équipes distantes, voyageurs et entreprises.',
   'Blog World Time',
   'Des guides pratiques écrits par des humains sur les fuseaux horaires, le calcul de décalage, l\'heure d\'été et la coordination de réunions mondiales.',
   'Lire l\'article →', 'Blog', 'Comment ça marche'),
 'de': ('de',
   'World Time Blog — Zeitzonen-Guides, Umrechnungstipps & Remote Work | World Time Sync',
   'Praktische Guides zu Zeitzonen, Zeitdifferenz-Berechnung, Sommerzeit und Meeting-Koordinierung weltweit. Artikel für Remote-Teams, Reisende und Unternehmen.',
   'World Time Blog',
   'Praktische, von Menschen geschriebene Guides zu Zeitzonen, Zeitdifferenz-Mathematik, Sommerzeit und globaler Meeting-Koordinierung.',
   'Artikel lesen →', 'Blog', 'So funktioniert\'s'),
 'uk': ('uk',
   'Блог World Time — гайди по часових поясах, поради з конвертації та віддаленої роботи | World Time Sync',
   'Практичні гайди по часових поясах, розрахунку різниці в часі, літньому часу та координації зустрічей по всьому світу. Статті для віддалених команд, мандрівників і бізнесу.',
   'Блог World Time',
   'Практичні, написані людиною гайди по часових поясах, математиці різниці в часі, літньому часу та координації зустрічей у світі.',
   'Читати статтю →', 'Блог', 'Як це працює'),
}

LANGS_ORDER = ['ru','es','zh','ja','fr','de','uk']
ALL_LANGS_HREF = ['x-default','en'] + LANGS_ORDER

def hreflang_block(lang):
    lines = [f'      <link rel="canonical" href="https://worldtimessync.com/{lang}/blog/" />']
    for l in ALL_LANGS_HREF:
        if l == 'x-default':
            lines.append(f'      <link rel="alternate" hreflang="x-default" href="https://worldtimessync.com/blog/" />')
        elif l == 'en':
            lines.append(f'      <link rel="alternate" hreflang="en" href="https://worldtimessync.com/blog/" />')
        else:
            lines.append(f'      <link rel="alternate" hreflang="{l}" href="https://worldtimessync.com/{l}/blog/" />')
    return '\n'.join(lines)

def lang_bar(active):
    items = [('', 'English'), ('es/', 'Español'), ('zh/', '中文'), ('ru/', 'Русский'),
             ('it/', 'Italiano'), ('de/', 'Deutsch'), ('ja/', '日本語'), ('fr/', 'Français'), ('uk/', 'Українська')]
    out = []
    for code, label in items:
        cls = ' class="active"' if code == active else ''
        out.append(f'<a href="/{code}"{cls}>{label}</a>')
    return '<div class="lang-bar" role="navigation" aria-label="Language selection"><span class="lang-globe">🌐</span>' + ''.join(out) + '</div>'

def footer_links(lang, blog_label, how_label):
    return f'''  <footer>
    <p>© 2026 World Time Sync · <a href="/{lang}/">World Clock</a> · <a href="/{lang}/blog/">{blog_label}</a> · <a href="/{lang}/how-it-works.html">{how_label}</a> · <a href="/{lang}/privacy.html">Privacy Policy</a> · <a href="/{lang}/contact.html">Contact</a></p>
  </footer>'''

CSS = '''      *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
      html{font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.5}
      body{background-color:#000;color:#fff;min-height:100vh}
      .lang-bar{position:fixed;top:0;right:0;z-index:9999;display:flex;align-items:center;gap:2px;padding:6px 12px;background:rgba(0,0,0,0.85);backdrop-filter:blur(8px);border-radius:0 0 0 10px;font-size:0.8rem}
      .lang-bar .lang-globe{margin-right:4px;font-size:0.9rem}
      .lang-bar a{color:#888;text-decoration:none;padding:3px 7px;border-radius:4px;transition:all 0.15s}
      .lang-bar a:hover{color:#fff;background:rgba(255,255,255,0.1)}
      .lang-bar a.active{color:#60a5fa;font-weight:600}
      .container{max-width:1100px;margin:0 auto;padding:5rem 1.5rem 3rem}
      .breadcrumb{margin-bottom:1.5rem;color:#888;font-size:0.85rem}
      .breadcrumb a{color:#60a5fa;text-decoration:none}
      h1{font-size:2.2rem;margin-bottom:0.75rem;color:#fff}
      .subtitle{color:#aaa;font-size:1.05rem;margin-bottom:2.5rem;max-width:700px}
      .blog-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem}
      .blog-card{background:#0a0a0a;border:1px solid #222;border-radius:10px;padding:1.5rem;display:flex;flex-direction:column;transition:border-color 0.2s,transform 0.2s}
      .blog-card:hover{border-color:#60a5fa;transform:translateY(-2px)}
      .blog-card h3{font-size:1.1rem;margin-bottom:0.6rem;line-height:1.35}
      .blog-card h3 a{color:#e0e0e0;text-decoration:none}
      .blog-card h3 a:hover{color:#60a5fa}
      .blog-card p{color:#999;font-size:0.9rem;line-height:1.6;flex-grow:1;margin-bottom:1rem}
      .read-more{color:#60a5fa;text-decoration:none;font-size:0.9rem;font-weight:500}
      .read-more:hover{text-decoration:underline}
      footer{border-top:1px solid #222;margin-top:3rem;padding-top:2rem;color:#666;font-size:0.85rem;text-align:center}
      footer a{color:#60a5fa;text-decoration:none}
      @media(max-width:600px){.blog-grid{grid-template-columns:1fr}.container{padding-top:4rem}}'''

for lang in LANGS_ORDER:
    html_lang, title, desc, h1, subtitle, read_more, blog_label, how_label = L10N[lang]
    cards = []
    for p in posts:
        slug = p['file'].replace('.html','')
        # link to localized post if exists, else EN
        loc_file = f"{slug}-{lang}.html"
        loc_path = os.path.join(ROOT, 'blog', loc_file)
        if os.path.exists(loc_path):
            href = f"/blog/{loc_file}"
            card_title = p['title'] or p['h1']
        else:
            href = f"/blog/{p['file']}"
            card_title = p['title'] or p['h1']
        cards.append(f'''      <article class="blog-card">
        <h3><a href="{href}">{card_title}</a></h3>
        <p>{p['desc']}</p>
        <a class="read-more" href="{href}">{read_more}</a>
      </article>''')
    cards_html = '\n'.join(cards)
    html = f'''<!doctype html><html lang="{html_lang}"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0" /><meta name="google-site-verification" content="tNRYRY4K5ZdeEBPId3_g0GiclaIlooP5GhihYhXwknk" /><title>{title}</title><meta name="description" content="{desc}" /><meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" /><meta name="theme-color" content="#000000" /><meta property="og:type" content="website" /><meta property="og:url" content="https://worldtimessync.com/{lang}/blog/" /><meta property="og:title" content="{h1}" /><meta property="og:description" content="{desc}" /><meta property="og:image" content="https://worldtimessync.com/og-image.png" /><meta property="og:site_name" content="World Time Sync" /><meta name="twitter:card" content="summary_large_image" />
{hreflang_block(lang)}
    <style>{CSS}</style></head><body>{lang_bar(lang+'/')}
<main class="container">
  <nav class="breadcrumb"><a href="/{lang}/">Home</a> &gt; {blog_label}</nav>
  <h1>{h1}</h1>
  <p class="subtitle">{subtitle}</p>
  <div class="blog-grid">
{cards_html}
  </div>
{footer_links(lang, blog_label, how_label)}
</main>
</body></html>'''
    out_dir = os.path.join(ROOT, lang, 'blog')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'index.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Wrote {out_path} ({len(html)} bytes)")
