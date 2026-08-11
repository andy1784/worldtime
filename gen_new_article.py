#!/usr/bin/env python3
"""Generate 1 new English blog post about time zone abbreviations."""
from pathlib import Path
import os

BASE = Path('/home/kaliuser/worldtime')
BLOG_DIR = BASE / 'blog'

NEW_POST = {
    'time-zone-abbreviations-cheat-sheet': {
        'title': 'Time Zone Abbreviations Cheat Sheet (2026)',
        'meta_desc': 'Quick reference for every major time zone abbreviation - EST, PST, CET, IST, JST and 50 more. Includes UTC offsets, DST variants, and the cities that use each one.',
        'keywords': 'time zone abbreviations, EST PST CST MST, UTC offsets cheat sheet, timezone codes list, time zone acronyms, daylight saving abbreviations',
        'content': '''<p>You see "EST" on a flight confirmation, "CET" in a meeting invite, "IST" in a log file. Every abbreviation means a specific offset from UTC, but some mean different things in summer versus winter. This cheat sheet gives you the exact offset, the major cities, and whether daylight saving shifts it.</p>

<h2>North American Time Zones</h2>
<table class="tz-table">
    <thead><tr><th>Abbr</th><th>Full Name</th><th>UTC Offset</th><th>DST Variant</th><th>Major Cities</th></tr></thead>
    <tbody>
        <tr><td>EST</td><td>Eastern Standard Time</td><td>UTC-5</td><td>EDT (UTC-4)</td><td>New York, Toronto, Miami, Atlanta</td></tr>
        <tr><td>EDT</td><td>Eastern Daylight Time</td><td>UTC-4</td><td>EST (winter)</td><td>Same cities, March-November</td></tr>
        <tr><td>CST</td><td>Central Standard Time</td><td>UTC-6</td><td>CDT (UTC-5)</td><td>Chicago, Dallas, Mexico City, Houston</td></tr>
        <tr><td>CDT</td><td>Central Daylight Time</td><td>UTC-5</td><td>CST (winter)</td><td>Same cities, March-November</td></tr>
        <tr><td>MST</td><td>Mountain Standard Time</td><td>UTC-7</td><td>MDT (UTC-6)</td><td>Denver, Phoenix*, Edmonton, El Paso</td></tr>
        <tr><td>MDT</td><td>Mountain Daylight Time</td><td>UTC-6</td><td>MST (winter)</td><td>Same cities (except Arizona)</td></tr>
        <tr><td>PST</td><td>Pacific Standard Time</td><td>UTC-8</td><td>PDT (UTC-7)</td><td>Los Angeles, Vancouver, Seattle, Tijuana</td></tr>
        <tr><td>PDT</td><td>Pacific Daylight Time</td><td>UTC-7</td><td>PST (winter)</td><td>Same cities, March-November</td></tr>
        <tr><td>AKST</td><td>Alaska Standard Time</td><td>UTC-9</td><td>AKDT (UTC-8)</td><td>Anchorage, Fairbanks, Juneau</td></tr>
        <tr><td>HST</td><td>Hawaii-Aleutian Standard Time</td><td>UTC-10</td><td>No DST</td><td>Honolulu, Hilo, Adak</td></tr>
    </tbody>
</table>
<p><small>* Arizona (except Navajo Nation) does not observe DST and stays on MST year-round.</small></p>

<h2>Atlantic & South American Time Zones</h2>
<table class="tz-table">
    <thead><tr><th>Abbr</th><th>Full Name</th><th>UTC Offset</th><th>DST Variant</th><th>Major Cities</th></tr></thead>
    <tbody>
        <tr><td>AST</td><td>Atlantic Standard Time</td><td>UTC-4</td><td>ADT (UTC-3)</td><td>Halifax, San Juan, Bermuda, Caracas</td></tr>
        <tr><td>BRT</td><td>Brasilia Time</td><td>UTC-3</td><td>No DST since 2019</td><td>São Paulo, Rio de Janeiro, Brasilia</td></tr>
        <tr><td>ART</td><td>Argentina Time</td><td>UTC-3</td><td>No DST since 2009</td><td>Buenos Aires, Córdoba, Rosario</td></tr>
        <tr><td>CLT</td><td>Chile Standard Time</td><td>UTC-4</td><td>CLST (UTC-3)</td><td>Santiago, Valparaíso, Concepción</td></tr>
    </tbody>
</table>

<h2>European & African Time Zones</h2>
<table class="tz-table">
    <thead><tr><th>Abbr</th><th>Full Name</th><th>UTC Offset</th><th>DST Variant</th><th>Major Cities</th></tr></thead>
    <tbody>
        <tr><td>GMT</td><td>Greenwich Mean Time</td><td>UTC+0</td><td>BST (UTC+1)</td><td>London, Dublin, Lisbon (winter)</td></tr>
        <tr><td>BST</td><td>British Summer Time</td><td>UTC+1</td><td>GMT (winter)</td><td>London, Dublin, Edinburgh (summer)</td></tr>
        <tr><td>WET</td><td>Western European Time</td><td>UTC+0</td><td>WEST (UTC+1)</td><td>Lisbon, Casablanca, Reykjavik</td></tr>
        <tr><td>CET</td><td>Central European Time</td><td>UTC+1</td><td>CEST (UTC+2)</td><td>Paris, Berlin, Rome, Madrid, Warsaw</td></tr>
        <tr><td>CEST</td><td>Central European Summer Time</td><td>UTC+2</td><td>CET (winter)</td><td>Same cities, March-October</td></tr>
        <tr><td>EET</td><td>Eastern European Time</td><td>UTC+2</td><td>EEST (UTC+3)</td><td>Helsinki, Kyiv, Bucharest, Cairo</td></tr>
        <tr><td>MSK</td><td>Moscow Standard Time</td><td>UTC+3</td><td>No DST since 2014</td><td>Moscow, St. Petersburg, Istanbul, Minsk</td></tr>
        <tr><td>SAST</td><td>South Africa Standard Time</td><td>UTC+2</td><td>No DST</td><td>Johannesburg, Cape Town, Durban</td></tr>
        <tr><td>WAT</td><td>West Africa Time</td><td>UTC+1</td><td>No DST</td><td>Lagos, Kinshasa, Algiers</td></tr>
    </tbody>
</table>

<h2>Middle Eastern & Central Asian Time Zones</h2>
<table class="tz-table">
    <thead><tr><th>Abbr</th><th>Full Name</th><th>UTC Offset</th><th>DST Variant</th><th>Major Cities</th></tr></thead>
    <tbody>
        <tr><td>GST</td><td>Gulf Standard Time</td><td>UTC+4</td><td>No DST</td><td>Dubai, Abu Dhabi, Muscat, Doha</td></tr>
        <tr><td>AST</td><td>Arabia Standard Time</td><td>UTC+3</td><td>No DST</td><td>Riyadh, Jeddah, Kuwait City, Manama</td></tr>
        <tr><td>IRST</td><td>Iran Standard Time</td><td>UTC+3:30</td><td>IRDT (UTC+4:30)</td><td>Tehran, Mashhad, Isfahan</td></tr>
        <tr><td>AFT</td><td>Afghanistan Time</td><td>UTC+4:30</td><td>No DST</td><td>Kabul, Herat, Mazar-i-Sharif</td></tr>
        <tr><td>PKT</td><td>Pakistan Standard Time</td><td>UTC+5</td><td>No DST</td><td>Karachi, Lahore, Islamabad</td></tr>
    </tbody>
</table>

<h2>South & Southeast Asian Time Zones</h2>
<table class="tz-table">
    <thead><tr><th>Abbr</th><th>Full Name</th><th>UTC Offset</th><th>DST Variant</th><th>Major Cities</th></tr></thead>
    <tbody>
        <tr><td>IST</td><td>India Standard Time</td><td>UTC+5:30</td><td>No DST</td><td>Mumbai, Delhi, Bangalore, Kolkata, Chennai</td></tr>
        <tr><td>NPT</td><td>Nepal Time</td><td>UTC+5:45</td><td>No DST</td><td>Kathmandu, Pokhara, Biratnagar</td></tr>
        <tr><td>BST</td><td>Bangladesh Standard Time</td><td>UTC+6</td><td>No DST</td><td>Dhaka, Chittagong, Sylhet</td></tr>
        <tr><td>MMT</td><td>Myanmar Time</td><td>UTC+6:30</td><td>No DST</td><td>Yangon, Mandalay, Naypyidaw</td></tr>
        <tr><td>ICT</td><td>Indochina Time</td><td>UTC+7</td><td>No DST</td><td>Bangkok, Hanoi, Jakarta*, Phnom Penh</td></tr>
        <tr><td>WIB</td><td>Western Indonesian Time</td><td>UTC+7</td><td>No DST</td><td>Jakarta, Bandung, Surabaya</td></tr>
        <tr><td>CST</td><td>China Standard Time</td><td>UTC+8</td><td>No DST</td><td>Beijing, Shanghai, Hong Kong, Taipei</td></tr>
        <tr><td>SGT</td><td>Singapore Time</td><td>UTC+8</td><td>No DST</td><td>Singapore, Kuala Lumpur, Manila, Perth</td></tr>
    </tbody>
</table>
<p><small>* Jakarta uses WIB (UTC+7), not ICT.</small></p>

<h2>East Asian & Pacific Time Zones</h2>
<table class="tz-table">
    <thead><tr><th>Abbr</th><th>Full Name</th><th>UTC Offset</th><th>DST Variant</th><th>Major Cities</th></tr></thead>
    <tbody>
        <tr><td>JST</td><td>Japan Standard Time</td><td>UTC+9</td><td>No DST</td><td>Tokyo, Osaka, Seoul*, Pyongyang*</td></tr>
        <tr><td>KST</td><td>Korea Standard Time</td><td>UTC+9</td><td>No DST</td><td>Seoul, Busan, Incheon</td></tr>
        <tr><td>AWST</td><td>Australian Western Standard Time</td><td>UTC+8</td><td>No DST</td><td>Perth, Broome, Karratha</td></tr>
        <tr><td>ACST</td><td>Australian Central Standard Time</td><td>UTC+9:30</td><td>ACDT (UTC+10:30)</td><td>Adelaide, Darwin, Alice Springs</td></tr>
        <tr><td>AEST</td><td>Australian Eastern Standard Time</td><td>UTC+10</td><td>AEDT (UTC+11)</td><td>Sydney, Melbourne, Brisbane*, Canberra</td></tr>
        <tr><td>NZST</td><td>New Zealand Standard Time</td><td>UTC+12</td><td>NZDT (UTC+13)</td><td>Auckland, Wellington, Christchurch</td></tr>
    </tbody>
</table>
<p><small>* Seoul and Pyongyang use KST, not JST. * Brisbane (Queensland) does not observe DST.</small></p>

<h2>Ambiguous Abbreviations — Watch Out</h2>
<p>Some abbreviations mean different zones depending on context:</p>
<ul>
    <li><strong>CST</strong> — Central Standard Time (UTC-6, North America) <em>or</em> China Standard Time (UTC+8) <em>or</em> Cuba Standard Time (UTC-5)</li>
    <li><strong>IST</strong> — India Standard Time (UTC+5:30) <em>or</em> Irish Standard Time (UTC+1, summer) <em>or</em> Israel Standard Time (UTC+2)</li>
    <li><strong>PST</strong> — Pacific Standard Time (UTC-8) <em>or</em> Philippine Standard Time (UTC+8)</li>
    <li><strong>BST</strong> — British Summer Time (UTC+1) <em>or</em> Bangladesh Standard Time (UTC+6) <em>or</em> Bougainville Standard Time (UTC+11)</li>
    <li><strong>AST</strong> — Atlantic Standard Time (UTC-4) <em>or</em> Arabia Standard Time (UTC+3) <em>or</em> Amazon Standard Time (UTC-4, Brazil)</li>
</ul>
<p>When you see an ambiguous code, check the country or city name nearby. For exact conversions, use our <a href="/time-zone-converter.html">time zone converter</a> which handles all of these correctly.</p>

<h2>Quick Reference: DST Switch Dates (Typical)</h2>
<ul>
    <li><strong>North America</strong>: 2nd Sunday March → 1st Sunday November</li>
    <li><strong>Europe</strong>: Last Sunday March → Last Sunday October</li>
    <li><strong>Australia (southeast)</strong>: 1st Sunday October → 1st Sunday April</li>
    <li><strong>New Zealand</strong>: Last Sunday September → 1st Sunday April</li>
    <li><strong>Chile</strong>: 1st Sunday September → 1st Sunday April</li>
    <li><strong>Paraguay</strong>: 1st Sunday October → Last Sunday March</li>
</ul>

<h2>Bookmark This, Use the Tool</h2>
<p>You do not need to memorize 50+ codes. Bookmark this page for the lookup table. When you need an exact conversion for a specific date — especially during DST transition weeks — use our <a href="/time-difference.html">time difference calculator</a> or <a href="/meeting-planner.html">meeting planner</a>. They use the IANA time zone database so every offset is current and correct.</p>
''',
    }
}

ARTICLE_TEMPLATE = '''        <article class="blog-wrap">
            <nav class="blog-breadcrumb" aria-label="Breadcrumb">
                <a href="/">Home</a> &#8250; <a href="/#blog">Blog</a> &#8250; <span aria-current="page">{h1}</span>
            </nav>
            <h1>{h1}</h1>
            <div class="blog-meta">&#128197; August 10, 2026 &nbsp;&middot;&nbsp; &#9201; 8 min read &nbsp;&middot;&nbsp; &#127991; Time Zones, Reference, Guides</div>
{content}
        </article>'''

def build_head(title, meta_desc, keywords, slug):
    return '''<!doctype html>
<html lang="en">
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
    <meta property="og:url" content="https://worldtimessync.com/blog/{slug}">
    <meta property="og:title" content="{title} | World Time Sync">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:image" content="https://worldtimessync.com/og-image.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title} | World Time Sync">
    <link rel="canonical" href="https://worldtimessync.com/blog/{slug}">
    <link rel="alternate" hreflang="x-default" href="https://worldtimessync.com/blog/{slug}">
    <link rel="alternate" hreflang="en" href="https://worldtimessync.com/blog/{slug}">
    <link rel="alternate" hreflang="es" href="https://worldtimessync.com/blog/{slug}-es">
    <link rel="alternate" hreflang="zh" href="https://worldtimessync.com/blog/{slug}-zh">
    <link rel="alternate" hreflang="ru" href="https://worldtimessync.com/blog/{slug}-ru">
    <link rel="alternate" hreflang="it" href="https://worldtimessync.com/blog/{slug}-it">
    <link rel="alternate" hreflang="de" href="https://worldtimessync.com/blog/{slug}-de">
    <link rel="alternate" hreflang="ja" href="https://worldtimessync.com/blog/{slug}-ja">
    <link rel="alternate" hreflang="fr" href="https://worldtimessync.com/blog/{slug}-fr">
    <link rel="alternate" hreflang="uk" href="https://worldtimessync.com/blog/{slug}-uk">
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
    {{"@context": "https://schema.org", "@type": "BlogPosting", "headline": "{title} | World Time Sync", "description": "{meta_desc}", "author": {{"@type": "Organization", "name": "World Time Sync", "url": "https://worldtimessync.com"}}, "publisher": {{"@type": "Organization", "name": "World Time Sync", "url": "https://worldtimessync.com"}}, "datePublished": "2026-08-10", "dateModified": "2026-08-10", "mainEntityOfPage": {{"@type": "WebPage", "@id": "https://worldtimessync.com/blog/{slug}"}}, "image": "https://worldtimessync.com/og-image.png", "inLanguage": "en"}}
    </script>
    <script type="application/ld+json">
    {{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://worldtimessync.com/"}}, {{"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://worldtimessync.com/#blog"}}, {{"@type": "ListItem", "position": 3, "name": "{title}", "item": "https://worldtimessync.com/blog/{slug}"}}]}}
    </script>
</head>
<body>
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <div id="root" role="application" aria-label="World Time Online Application">
        <div class="app-loading" aria-busy="true" aria-live="polite">
            <div class="app-loading-spinner" role="status" aria-label="Loading application"></div>
            <p class="app-loading-text">Loading World Time...</p>
        </div>
    </div>
    <main id="main-content">
'''.format(title=title, meta_desc=meta_desc, keywords=keywords, slug=slug)

TAIL = '''    </main>
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
</html>'''

created = 0
for slug, p in NEW_POST.items():
    slug_html = slug + '.html'
    h1 = p['title'].split(' (2026)')[0]
    head = build_head(p['title'], p['meta_desc'], p['keywords'], slug_html)
    article = ARTICLE_TEMPLATE.format(h1=h1, content=p['content'])
    full = head + article + TAIL
    fp = BLOG_DIR / slug_html
    with open(fp, 'w', encoding='utf-8') as fh:
        fh.write(full)
        fh.flush()
        os.fsync(fh.fileno())
    created += 1
    print('Wrote', slug_html, os.path.getsize(fp), 'bytes')

print(f'Done. {created} EN post created.')