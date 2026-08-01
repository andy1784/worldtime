#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate blog/index.html - the blog landing/index page listing all EN posts."""
import re, os, glob, json

ROOT = '/home/kaliuser/worldtime'
blog_dir = os.path.join(ROOT, 'blog')
posts = json.load(open('/tmp/blog_posts_list.json', encoding='utf-8'))

# Build cards
cards = []
for p in posts:
    slug = p['file'].replace('.html', '')
    title = p['title'] or p['h1']
    desc = p['desc']
    cards.append(f'''      <article class="blog-card">
        <h3><a href="/blog/{p['file']}">{title}</a></h3>
        <p>{desc}</p>
        <a class="read-more" href="/blog/{p['file']}">Read article →</a>
      </article>''')

cards_html = '\n'.join(cards)

html = f'''<!doctype html><html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0" /><meta name="google-site-verification" content="tNRYRY4K5ZdeEBPId3_g0GiclaIlooP5GhihYhXwknk" /><title>World Time Blog — Time Zone Guides, Conversion Tips & Remote Work Advice | World Time Sync</title><meta name="description" content="Practical guides on time zones, time difference calculations, daylight saving time, and coordinating meetings across the globe. {len(posts)} articles for remote teams, travelers, and businesses." /><meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" /><meta name="theme-color" content="#000000" /><meta property="og:type" content="website" /><meta property="og:url" content="https://worldtimessync.com/blog/" /><meta property="og:title" content="World Time Blog — Time Zone Guides & Remote Work Advice" /><meta property="og:description" content="Practical guides on time zones, time difference calculations, DST, and coordinating global meetings. {len(posts)} articles." /><meta property="og:image" content="https://worldtimessync.com/og-image.png" /><meta property="og:site_name" content="World Time Sync" /><meta name="twitter:card" content="summary_large_image" /><link rel="canonical" href="https://worldtimessync.com/blog/" /><link rel="alternate" hreflang="x-default" href="https://worldtimessync.com/blog/" /><link rel="alternate" hreflang="en" href="https://worldtimessync.com/blog/" /><link rel="alternate" hreflang="es" href="https://worldtimessync.com/es/blog/" /><link rel="alternate" hreflang="zh" href="https://worldtimessync.com/zh/blog/" /><link rel="alternate" hreflang="ru" href="https://worldtimessync.com/ru/blog/" /><link rel="alternate" hreflang="it" href="https://worldtimessync.com/it/blog/" /><link rel="alternate" hreflang="de" href="https://worldtimessync.com/de/blog/" /><link rel="alternate" hreflang="ja" href="https://worldtimessync.com/ja/blog/" /><link rel="alternate" hreflang="fr" href="https://worldtimessync.com/fr/blog/" /><link rel="alternate" hreflang="uk" href="https://worldtimessync.com/uk/blog/" /><style>
      *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
      html{{font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.5}}
      body{{background-color:#000;color:#fff;min-height:100vh}}
      .lang-bar{{position:fixed;top:0;right:0;z-index:9999;display:flex;align-items:center;gap:2px;padding:6px 12px;background:rgba(0,0,0,0.85);backdrop-filter:blur(8px);border-radius:0 0 0 10px;font-size:0.8rem}}
      .lang-bar .lang-globe{{margin-right:4px;font-size:0.9rem}}
      .lang-bar a{{color:#888;text-decoration:none;padding:3px 7px;border-radius:4px;transition:all 0.15s}}
      .lang-bar a:hover{{color:#fff;background:rgba(255,255,255,0.1)}}
      .lang-bar a.active{{color:#60a5fa;font-weight:600}}
      .container{{max-width:1100px;margin:0 auto;padding:5rem 1.5rem 3rem}}
      .breadcrumb{{margin-bottom:1.5rem;color:#888;font-size:0.85rem}}
      .breadcrumb a{{color:#60a5fa;text-decoration:none}}
      h1{{font-size:2.2rem;margin-bottom:0.75rem;color:#fff}}
      .subtitle{{color:#aaa;font-size:1.05rem;margin-bottom:2.5rem;max-width:700px}}
      .blog-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem}}
      .blog-card{{background:#0a0a0a;border:1px solid #222;border-radius:10px;padding:1.5rem;display:flex;flex-direction:column;transition:border-color 0.2s,transform 0.2s}}
      .blog-card:hover{{border-color:#60a5fa;transform:translateY(-2px)}}
      .blog-card h3{{font-size:1.1rem;margin-bottom:0.6rem;line-height:1.35}}
      .blog-card h3 a{{color:#e0e0e0;text-decoration:none}}
      .blog-card h3 a:hover{{color:#60a5fa}}
      .blog-card p{{color:#999;font-size:0.9rem;line-height:1.6;flex-grow:1;margin-bottom:1rem}}
      .read-more{{color:#60a5fa;text-decoration:none;font-size:0.9rem;font-weight:500}}
      .read-more:hover{{text-decoration:underline}}
      footer{{border-top:1px solid #222;margin-top:3rem;padding-top:2rem;color:#666;font-size:0.85rem;text-align:center}}
      footer a{{color:#60a5fa;text-decoration:none}}
      @media(max-width:600px){{.blog-grid{{grid-template-columns:1fr}}.container{{padding-top:4rem}}}}
    </style></head><body><div class="lang-bar" role="navigation" aria-label="Language selection"><span class="lang-globe">🌐</span><a href="/" >English</a><a href="/es/">Español</a><a href="/zh/">中文</a><a href="/ru/">Русский</a><a href="/it/">Italiano</a><a href="/de/">Deutsch</a><a href="/ja/">日本語</a><a href="/fr/">Français</a><a href="/uk/">Українська</a></div>
<main class="container">
  <nav class="breadcrumb"><a href="/">Home</a> &gt; Blog</nav>
  <h1>World Time Blog</h1>
  <p class="subtitle">Practical, human-written guides on time zones, time-difference math, daylight saving time, and coordinating meetings across the globe. Built for remote teams, travelers, and anyone scheduling across borders.</p>
  <div class="blog-grid">
{cards_html}
  </div>
  <footer>
    <p>© 2026 World Time Sync · <a href="/">World Clock</a> · <a href="/privacy.html">Privacy Policy</a> · <a href="/meeting-planner.html">Meeting Planner</a></p>
  </footer>
</main>
</body></html>'''

out = os.path.join(blog_dir, 'index.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Wrote {out} ({len(html)} bytes, {len(posts)} cards)")
