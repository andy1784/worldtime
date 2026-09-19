#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate /abbreviations/ glossary: hub + one card per time-zone abbreviation.
Cards link to /time-zones/* hubs and related cities. Schema: DefinedTermSet on hub,
DefinedTerm + FAQPage + BreadcrumbList on each card."""
import os, json

ROOT = '/home/kaliuser/worldtime'
OUT = os.path.join(ROOT, 'abbreviations')
os.makedirs(OUT, exist_ok=True)

SITE = 'https://worldtimessync.com'

ANALYTICS = '''    <script async src="https://www.googletagmanager.com/gtag/js?id=G-LBX0CDYSSV"></script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XCBTT7YSPY"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-LBX0CDYSSV');
      gtag('config', 'G-XCBTT7YSPY');
    </script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9728257902981529" crossorigin="anonymous"></script>'''

def head(title, desc, kw, canonical_path, schema_blocks):
    return f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#667eea">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{kw}">
    <meta name="robots" content="index, follow">
    <meta name="author" content="World Time Sync">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{SITE}{canonical_path}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="{SITE}/og-image.png">
    <meta property="og:site_name" content="World Time Sync">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="{SITE}/og-image.png">
    <link rel="canonical" href="{SITE}{canonical_path}">
    <link rel="alternate" hreflang="x-default" href="{SITE}{canonical_path}">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="stylesheet" href="/assets/index-ufePLcBr.css">
{ANALYTICS}
{schema_blocks}
</head>
<body>
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <main id="main-content" style="max-width:860px;margin:0 auto;padding:24px 16px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.65;color:#222;">
'''

FOOTER = '''
        <nav class="blog-breadcrumb" aria-label="Breadcrumb" style="margin-top:32px;font-size:.85rem;">
            <a href="/">Home</a> › <a href="/#tools">Tools</a> › Time Zone Abbreviations Glossary
        </nav>
        <footer class="blog-footer" style="border-top:1px solid #eee;padding-top:12px;margin-top:12px;">
            <a href="/privacy">Privacy</a> <a href="/about">About</a> <a href="/contact">Contact</a> <a href="/terms">Terms</a>
            <p style="color:#666;font-size:.75rem">&copy; 2026 World Time Sync</p>
        </footer>
    </main>
</body>
</html>'''

# ---------------- DATA ----------------
ABBR = [
 dict(abbr='EST', full='Eastern Standard Time', offset='UTC−5', dst='EDT (UTC−4), March–November',
      regions='US East Coast (New York, Washington DC, Miami), Ontario, Quebec, Colombia, Peru, Ecuador, Jamaica, Panama',
      hub='/time-zones/est', cities=[('New York','new-york'),('Washington, D.C.','washington-d-c'),('Miami','miami'),('Toronto','toronto')],
      note='EST is the most-searched time-zone abbreviation in the world. It covers roughly 47% of the US population. In everyday speech people say "EST" year-round, but from March to November the zone technically switches to EDT.',
      faq=[('What does EST stand for?','EST stands for Eastern Standard Time, UTC−5. It is used on the US East Coast and in parts of Canada, South America and the Caribbean.'),
           ('Is New York currently EST or EDT?','From early November to mid-March New York is on EST (UTC−5). From March to November it observes daylight saving as EDT (UTC−4).'),
           ('What is the difference between EST and EDT?','EDT is Eastern Daylight Time — the same zone shifted one hour forward for daylight saving. EST is UTC−5; EDT is UTC−4.')]),
 dict(abbr='PST', full='Pacific Standard Time', offset='UTC−8', dst='PDT (UTC−7), March–November',
      regions='US West Coast (Los Angeles, San Francisco, Seattle), British Columbia, Nevada',
      hub='/time-zones/pst', cities=[('Los Angeles','los-angeles'),('San Francisco','san-francisco'),('Seattle','seattle'),('Las Vegas','las-vegas')],
      note='PST governs Silicon Valley and Hollywood, so it became the de-facto clock of the tech industry. Server logs, release notes and "PT" timestamps in software usually mean this zone.',
      faq=[('What does PST stand for?','PST stands for Pacific Standard Time, UTC−8, observed on the US West Coast and western Canada during winter months.'),
           ('What is PT vs PST?','PT (Pacific Time) is the umbrella label. In winter it equals PST (UTC−8); in summer it becomes PDT (UTC−7).'),
           ('What is the difference between PST and EST?','EST is 3 hours ahead of PST. When it is 9 AM in Los Angeles it is already noon in New York.')]),
 dict(abbr='CST', full='Central Standard Time', offset='UTC−6', dst='CDT (UTC−5), March–November',
      regions='US Midwest and South (Chicago, Dallas, Houston, New Orleans), Mexico (as Tiempo del Centro), Central America',
      hub='/time-zones/cst', cities=[('Chicago','chicago'),('Dallas','dallas'),('Houston','houston'),('Mexico City','mexico-city')],
      note='CST has a rare double meaning: in Asia the same letters stand for China Standard Time (UTC+8). Context matters — a meeting "at 10 CST" means two different moments depending on which side of the Pacific you are on.',
      faq=[('What does CST stand for?','In North America CST stands for Central Standard Time (UTC−6). The same abbreviation is also used for China Standard Time (UTC+8), which causes frequent confusion.'),
           ('Is Chicago always on CST?','No. From March to November Chicago follows CDT (UTC−5) because of daylight saving.'),
           ('How far is CST from EST?','One hour behind. When it is noon EST it is 11 AM CST.')]),
 dict(abbr='MST', full='Mountain Standard Time', offset='UTC−7', dst='MDT (UTC−6), March–November (except Arizona)',
      regions='US Mountain states (Denver, Phoenix, Salt Lake City), Alberta, parts of Idaho and Montana',
      hub='/time-zones/mst', cities=[('Denver','denver'),('Phoenix','phoenix'),('Salt Lake City','salt-lake-city')],
      note='Arizona is the famous exception: it stays on MST all year without daylight saving, so in summer Arizona shares a clock with Pacific daylight time while Denver moves ahead.',
      faq=[('What does MST stand for?','MST stands for Mountain Standard Time, UTC−7, used in the Rocky Mountain region of North America.'),
           ('Does Arizona use MST year-round?','Yes. Most of Arizona does not observe daylight saving and stays on MST (UTC−7) all year.'),
           ('What is the MST to EST conversion?','EST is 2 hours ahead of MST.')]),
 dict(abbr='GMT', full='Greenwich Mean Time', offset='UTC+0', dst='BST (UTC+1), late March–late October',
      regions='UK and Ireland in winter; Ghana, Senegal, Iceland year-round; nautical and aviation reference',
      hub='/time-zones/gmt', cities=[('London','london'),('Dublin','dublin'),('Accra','accra'),('Reykjavik','reykjavik')],
      note='GMT was set by the astronomical observations at the Royal Observatory in Greenwich. Since 1972 UTC has replaced it as the scientific standard, but GMT survives in everyday British usage and aviation.',
      faq=[('What does GMT stand for?','GMT stands for Greenwich Mean Time — mean solar time at the Royal Observatory in Greenwich, London. It equals UTC+0.'),
           ('Is GMT the same as UTC?','For practical purposes yes, both are UTC+0. Technically GMT is an astronomical time standard while UTC is kept by atomic clocks with leap-second corrections.'),
           ('Is London always on GMT?','No. From late March to late October London uses BST (UTC+1).')]),
 dict(abbr='UTC', full='Coordinated Universal Time', offset='UTC±0', dst=None,
      regions='Global standard: aviation, computing, GPS, weather services; no local population lives on UTC proper',
      hub='/time-zones/utc', cities=[('London','london'),('Accra','accra'),('Dakar','dakar')],
      note='UTC is not a time zone you can live in — it is the reference every other offset is measured against. The odd abbreviation comes from a compromise between English (CUT) and French (TUC): both sides got the same letters.',
      faq=[('What does UTC stand for?','UTC stands for Coordinated Universal Time (in English) or Temps Universel Coordonné (in French). The mixed abbreviation satisfies both languages.'),
           ('Is UTC a time zone?','Not exactly. It is the global reference standard; local zones are expressed as offsets like UTC+3 or UTC−7.'),
           ('Why do servers log in UTC?','Because UTC never shifts for daylight saving, server timestamps stay unambiguous across seasons and countries.')]),
 dict(abbr='CET', full='Central European Time', offset='UTC+1', dst='CEST (UTC+2), late March–late October',
      regions='Germany, France, Italy, Spain, Poland, Netherlands, Belgium, Austria, Switzerland, Sweden, Norway',
      hub='/time-zones/cet', cities=[('Berlin','berlin'),('Paris','paris'),('Rome','rome'),('Madrid','madrid')],
      note='CET covers around 500 million people, more than any other single UTC+1 adoption. Spain is geographically aligned with GMT but politically sits in CET — a legacy decision attributed to Franco-era alignment with Berlin.',
      faq=[('What does CET stand for?','CET stands for Central European Time, UTC+1, used by most of continental Europe including Germany, France, Italy and Spain.'),
           ('What is CEST?','Central European Summer Time — the same zone at UTC+2 during daylight-saving months, from late March to late October.'),
           ('What is the CET to GMT difference?','CET is one hour ahead of GMT in winter, and CEST is two hours ahead of GMT in summer.')]),
 dict(abbr='IST', full='India Standard Time', offset='UTC+5:30', dst=None,
      regions='India (all states); same offset used by Sri Lanka since 2006',
      hub='/time-zones/ist', cities=[('Delhi','delhi'),('Mumbai','mumbai'),('Bengaluru','bengaluru'),('Kolkata','kolkata')],
      note='India stretches almost 30 degrees of longitude yet uses a single offset chosen as a compromise between Mumbai and Kolkata. Note that IST also means Irish Standard Time and Israel Standard Time — another abbreviation collision.',
      faq=[('What does IST stand for?','Most commonly India Standard Time, UTC+5:30. The same abbreviation also refers to Irish Standard Time and Israel Standard Time, so context matters.'),
           ('Why is India 5:30 hours off UTC?','The half-hour offset splits the difference between the country\u2019s eastern and western extremes, keeping sunrise times reasonable nationwide.'),
           ('Does India have daylight saving?','No. India has stayed on IST year-round since 1962.')]),
 dict(abbr='JST', full='Japan Standard Time', offset='UTC+9', dst=None,
      regions='Japan only (all 47 prefectures)',
      hub='/time-zones/jst', cities=[('Tokyo','tokyo'),('Osaka','osaka'),('Kyoto','kyoto')],
      note='Japan tried daylight saving during the US occupation (1948–1951) and dropped it. JST has been fixed at UTC+9 ever since, which keeps scheduling with Tokyo pleasantly predictable.',
      faq=[('What does JST stand for?','JST stands for Japan Standard Time, UTC+9. Japan does not observe daylight saving.'),
           ('What is the JST to PST difference?','JST is 17 hours ahead of PST in winter and 16 hours ahead of PDT in summer.'),
           ('Has Japan ever used DST?','Briefly, during the American occupation between 1948 and 1951. It was abolished afterwards and never returned.')]),
 dict(abbr='AEST', full='Australian Eastern Standard Time', offset='UTC+10', dst='AEDT (UTC+11), October–April (NSW, VIC, SA, TAS only)',
      regions='Queensland year-round; NSW, Victoria, Tasmania, ACT in winter months',
      hub='/time-zones/aest', cities=[('Sydney','sydney'),('Melbourne','melbourne'),('Brisbane','brisbane')],
      note='Australia runs its daylight saving backwards relative to the northern hemisphere: clocks go forward in October and back in April. Queensland skips it entirely, so Sydney–Brisbane gain a phantom hour half the year.',
      faq=[('What does AEST stand for?','AEST stands for Australian Eastern Standard Time, UTC+10, covering Queensland year-round and the southeastern states outside daylight-saving months.'),
           ('What is AEDT?','Australian Eastern Daylight Time, UTC+11 — AEST shifted forward from October to April.'),
           ('Do Sydney and Brisbane always share a clock?','No. During Australian summer Sydney is on AEDT while Brisbane stays on AEST, creating a one-hour gap.')]),
 dict(abbr='EET', full='Eastern European Time', offset='UTC+2', dst='EEST (UTC+3), late March–late October',
      regions='Greece, Finland, Romania, Bulgaria, Ukraine, Baltics, Egypt, Israel (as IDT variant)',
      hub='/time-zones/eet', cities=[('Athens','athens'),('Helsinki','helsinki'),('Kyiv','kyiv'),('Bucharest','bucharest')],
      note='Ukraine switched to EET-aligned permanent policy debates after 2022, while Egypt returned to daylight saving in 2023 after eight years of abolition — EET-region rules keep shifting, so live checks matter here more than anywhere else.',
      faq=[('What does EET stand for?','EET stands for Eastern European Time, UTC+2, observed in Greece, Finland, Ukraine, the Baltic states and several others.'),
           ('What is EEST?','Eastern European Summer Time, UTC+3 — the daylight-saving variant used from late March to late October.'),
           ('What is the EET to CET difference?','One hour. Athens is always one hour ahead of Rome or Berlin.')]),
 dict(abbr='MSK', full='Moscow Time', offset='UTC+3', dst=None,
      regions='Moscow, Saint Petersburg, most of European Russia; also Belarus and Crimea administratively',
      hub='/time-zones/msk', cities=[('Moscow','moscow'),('Saint Petersburg','saint-petersburg'),('Minsk','minsk')],
      note='Russia spans 11 time zones, but MSK is the political anchor: federal schedules, TV broadcasting and even railway tickets are published against Moscow Time regardless of where you physically are.',
      faq=[('What does MSK stand for?','MSK stands for Moscow Time, UTC+3, the reference zone used across European Russia, Belarus and much of the former USSR infrastructure.'),
           ('Does Russia use daylight saving?','No. Russia cancelled permanent seasonal clock changes in 2011 and settled on fixed offsets per zone.'),
           ('How many zones does Russia have?','Eleven, from Kaliningrad (UTC+2) to Kamchatka (UTC+12).')]),
 dict(abbr='KST', full='Korea Standard Time', offset='UTC+9', dst=None,
      regions='South Korea and North Korea (both use UTC+9 despite separate names)',
      hub='/time-zones/kst', cities=[('Seoul','seoul'),('Busan','busan')],
      note='North Korea briefly created its own Pyongyang Time (UTC+8:30) in 2015 as a symbolic break from Japan, then quietly rejoined UTC+9 in 2018 — a rare case of a national offset used as diplomacy.',
      faq=[('What does KST stand for?','KST stands for Korea Standard Time, UTC+9. Both Korean states effectively share this offset today.'),
           ('Did North Korea ever change its time zone?','Yes — it introduced UTC+8:30 in 2015 and reverted to UTC+9 in May 2018.'),
           ('Is KST the same as JST?','Yes, both are UTC+9, so Seoul and Tokyo always share the same wall-clock time.')]),
 dict(abbr='HST', full='Hawaii Standard Time', offset='UTC−10', dst=None,
      regions='Hawaii year-round; also Tahiti and Cook Islands (as separate zone names)',
      hub='/time-zones/hst', cities=[('Honolulu','honolulu')],
      note='Hawaii skipped daylight saving partly because day length barely changes near the tropics — sunrise varies by under an hour and a half across the whole year, making DST pointless there.',
      faq=[('What does HST stand for?','HST stands for Hawaii Standard Time, UTC−10. Hawaii does not observe daylight saving.'),
           ('What is the HST to EST difference?','Five hours. When it is 9 AM in New York it is 4 AM in Honolulu.'),
           ('Does Hawaii ever change clocks?','Never — Hawaii and most of Arizona are the only US states that skip daylight saving entirely.')]),
 dict(abbr='AKST', full='Alaska Standard Time', offset='UTC−9', dst='AKDT (UTC−8), March–November',
      regions='State of Alaska (most of it)',
      hub='/time-zones/akst', cities=[('Anchorage','anchorage'),('Juneau','juneau')],
      note='Alaska moved to UTC−9 in 1983, merging four old zones into one. Because of extreme northern latitude, Anchorage gets over 19 hours of daylight in June — DST barely registers against that swing.',
      faq=[('What does AKST stand for?','AKST stands for Alaska Standard Time, UTC−9, used across most of Alaska.'),
           ('What is AKDT?','Alaska Daylight Time, UTC−8 — the summer variant.'),
           ('Why is Alaska only one hour behind Pacific Time?','Congress consolidated Alaska into a single zone in 1983; before that the state stretched across four different offsets.')]),
 dict(abbr='BRT', full='Brasília Time', offset='UTC−3', dst='Abolished in 2019',
      regions='Brazil southeast (São Paulo, Rio de Janeiro), south and northeast regions',
      hub='/time-zones/brt', cities=[('São Paulo','sao-paulo'),('Rio de Janeiro','rio-de-janeiro'),('Brasília','brasilia')],
      note='Brazil spans four offsets, but BRT carries the country\u2019s business rhythm. Brazil scrapped national daylight saving in 2019 after studies showed negligible savings — one of the largest recent countries to do so.',
      faq=[('What does BRT stand for?','BRT stands for Brasília Time, UTC−3, the main Brazilian offset used by São Paulo, Rio de Janeiro and Brasília.'),
           ('Does Brazil have daylight saving now?','No. Brazil abolished daylight saving nationally in 2019.'),
           ('How many time zones does Brazil span?','Four, from UTC−2 (Atlantic islands) to UTC−5 (western Acre).')]),
]

WIKI_NOTE = 'Note on military time: the NATO phonetic letter Z ("Zulu") denotes UTC+0. Pilots and militaries say "1200 Zulu" instead of "noon UTC" to avoid any ambiguity.'

# ---------------- CARD BUILDER ----------------
def card(d):
    slug = d['abbr'].lower()
    url = f'{SITE}/abbreviations/{slug}'
    city_links = ' '.join(f'<li><a href="/time/{c[1]}">Current time in {c[0]}</a></li>' for c in d['cities'])
    dst_html = f'<li><strong>Daylight saving:</strong> {d["dst"]}</li>' if d['dst'] else '<li><strong>Daylight saving:</strong> none</li>'
    faq_json = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d['faq']]}, ensure_ascii=False)
    defined_term = json.dumps({"@context": "https://schema.org", "@type": "DefinedTerm", "name": d['abbr'],
                               "alternateName": d['full'], "description": d['note'][:280], "url": url,
                               "inDefinedTermSet": {"@type": "DefinedTermSet", "name": "Time Zone Abbreviations", "url": f"{SITE}/abbreviations"}}, ensure_ascii=False)
    crumb = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": "Time Zone Abbreviations", "item": f"{SITE}/abbreviations"},
        {"@type": "ListItem", "position": 3, "name": d['abbr'], "item": url}]}, ensure_ascii=False)
    title = f'What Does {d["abbr"]} Stand For? {d["full"]} ({d["offset"]}) | World Time Sync'
    desc = f'{d["abbr"]} = {d["full"]} ({d["offset"]}). Regions, daylight-saving rules, conversions and current time in major {d["abbr"]} cities.'
    body = f'''        <nav class="blog-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/abbreviations">Abbreviations</a> › <span aria-current="page">{d['abbr']}</span></nav>
        <h1>{d['abbr']} — {d['full']} ({d['offset']})</h1>
        <div class="blog-meta">🏷 Time zone abbreviations · Glossary entry</div>

        <div class="converter-widget" style="background:#f7f8ff;border:1px solid #e3e6ff;border-radius:12px;padding:18px;margin:18px 0;">
            <h2 style="margin-top:0">{d['abbr']} right now</h2>
            <p style="font-size:1.6rem;font-weight:700;margin:.2em 0" id="live-clock">Loading…</p>
            <p style="margin:.2em 0;color:#555">Offset: <strong>{d['offset']}</strong> · DST: {d['dst'] or 'none'}</p>
            <p><a href="/time-zones/{slug}" style="font-weight:600">Open the full {d['abbr']} time-zone page →</a></p>
        </div>

        <p>{d['note']}</p>

        <h2>{d['abbr']} quick facts</h2>
        <ul>
            <li><strong>Full name:</strong> {d['full']}</li>
            <li><strong>Standard offset:</strong> {d['offset']}</li>
            {dst_html}
            <li><strong>Where it applies:</strong> {d['regions']}</li>
        </ul>

        <h2>Major cities on {d['abbr']}</h2>
        <ul>{city_links}</ul>

        <h2>Frequently asked questions about {d['abbr']}</h2>
        <div class="faq-section">
'''
    for q, a in d['faq']:
        body += f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>\n'
    body += '''        </div>
        <p>Related: <a href="/abbreviations">all time-zone abbreviations</a> · <a href="/meeting-planner">Meeting Planner</a> · <a href="/world-clock">World Clock</a></p>'''
    schemas = f'''    <script type="application/ld+json">
    {defined_term}
    </script>
    <script type="application/ld+json">
    {crumb}
    </script>
    <script type="application/ld+json">
    {faq_json}
    </script>'''
    html = head(title, desc, f'{d["abbr"]} time zone, what does {d["abbr"]} stand for, {d["full"]}', f'/abbreviations/{slug}', schemas) + body + FOOTER
    path = os.path.join(OUT, f'{slug}.html')
    open(path, 'w', encoding='utf-8').write(html)
    print('written', path)

# ---------------- HUB BUILDER ----------------
def hub():
    url = f'{SITE}/abbreviations'
    rows = '\n'.join(
        f'<tr><td><a href="/abbreviations/{d["abbr"].lower()}"><strong>{d["abbr"]}</strong></a></td>'
        f'<td>{d["full"]}</td><td>{d["offset"]}</td>'
        f'<td>{"Yes — "+d["dst"].split("(")[0].strip() if d["dst"] else "No"}</td></tr>'
        for d in ABBR)
    terms = json.dumps([{"@type": "DefinedTerm", "name": d['abbr'], "alternateName": d['full'],
                         "url": f"{SITE}/abbreviations/{d['abbr'].lower()}"} for d in ABBR], ensure_ascii=False)
    dts = json.dumps({"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Time Zone Abbreviations Glossary",
                      "description": "Every common time-zone abbreviation explained: EST, PST, CST, GMT, UTC, CET, IST and more.",
                      "url": url, "hasDefinedTerm": json.loads(terms)}, ensure_ascii=False)
    faq_json = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": "What does EST stand for?", "acceptedAnswer": {"@type": "Answer", "text": "EST stands for Eastern Standard Time, UTC−5, used on the US East Coast and in eastern Canada."}},
        {"@type": "Question", "name": "Is GMT the same as UTC?", "acceptedAnswer": {"@type": "Answer", "text": "Practically yes — both equal UTC+0. GMT is the older astronomical standard; UTC is the modern atomic-clock standard."}},
        {"@type": "Question", "name": "Why does CST mean two different things?", "acceptedAnswer": {"@type": "Answer", "text": "In North America CST is Central Standard Time (UTC−6); in Asia it commonly means China Standard Time (UTC+8). Always check the context."}},
        {"@type": "Question", "name": "What is Zulu time?", "acceptedAnswer": {"@type": "Answer", "text": "Zulu (Z) is military and aviation shorthand for UTC+0. \"1200 Zulu\" means noon UTC."}}],
        }, ensure_ascii=False)
    title = 'Time Zone Abbreviations Explained: EST, PST, GMT, UTC, IST & More'
    desc = 'Complete glossary of time-zone abbreviations — what each acronym means, its UTC offset, DST rules and the regions that use it.'
    body = f'''        <nav class="blog-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> › <span aria-current="page">Abbreviations</span></nav>
        <h1>Time Zone Abbreviations — Complete Glossary</h1>
        <div class="blog-meta">🏷 Reference · Updated 2026 · {len(ABBR)} entries</div>

        <p>EST, CST, IST, GMT… time-zone acronyms collide constantly — the same three letters can describe zones twelve hours apart on opposite sides of the planet. This glossary gives each abbreviation its full name, UTC offset, daylight-saving behaviour and links to live pages.</p>

        <h2>All abbreviations at a glance</h2>
        <table style="width:100%;border-collapse:collapse">
            <thead><tr style="text-align:left;border-bottom:2px solid #e3e6ff"><th>Abbr.</th><th>Full name</th><th>Offset</th><th>DST?</th></tr></thead>
            <tbody>{rows}</tbody>
        </table>

        <h2>The confusing ones</h2>
        <p><strong>CST</strong> is the worst offender: North American Central Standard Time (UTC−6) versus China Standard Time (UTC+8). <strong>IST</strong> triples up — India, Ireland and Israel all claim it. <strong>CET</strong> occasionally collides with Cuba Standard Time in older documents. When precision matters, prefer explicit offsets or IANA names like <code>America/New_York</code>.</p>
        <p>{WIKI_NOTE}</p>

        <h2>Quick answers</h2>
        <div class="faq-section">
            <div class="faq-item"><h3>What does EST stand for?</h3><p>Eastern Standard Time, UTC−5 — the US East Coast and eastern Canada.</p></div>
            <div class="faq-item"><h3>Is GMT the same as UTC?</h3><p>Practically yes, both are UTC+0. GMT is the historical astronomical standard; UTC is maintained by atomic clocks.</p></div>
            <div class="faq-item"><h3>Why does CST mean two different things?</h3><p>North America uses CST for UTC−6; Asia often uses it for China Standard Time, UTC+8.</p></div>
            <div class="faq-item"><h3>What is Zulu time?</h3><p>Zulu (Z) is military/aviation shorthand for UTC+0. “1200 Zulu” means noon UTC.</p></div>
        </div>

        <p>Need to convert rather than decode? Jump straight to the <a href="/world-clock">World Clock</a>, the <a href="/time-zone-converter">Time Zone Converter</a>, or plan across zones in the <a href="/meeting-planner">Meeting Planner</a>. Zone deep-dives live under <a href="/time-zones">Time Zones</a>.</p>'''
    schemas = f'''    <script type="application/ld+json">
    {dts}
    </script>
    <script type="application/ld+json">
    {faq_json}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE}/"}},{{"@type":"ListItem","position":2,"name":"Time Zone Abbreviations","item":"{url}"}}]}}
    </script>'''
    html = head(title, desc, 'time zone abbreviations, what does est stand for, gmt utc difference, ist cst pst meaning', '/abbreviations', schemas) + body + FOOTER
    open(os.path.join(ROOT, 'abbreviations.html'), 'w', encoding='utf-8').write(html)
    print('written hub')

if __name__ == '__main__':
    hub()
    for d in ABBR:
        card(d)
    print(f'DONE: hub + {len(ABBR)} cards')
