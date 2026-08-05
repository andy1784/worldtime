#!/usr/bin/env python3
"""
Generate seasonal content clusters for DST transitions, Ramadan, Olympics, etc.
Automated pipeline: 2 weeks before event -> publish article with template + IANA tzdb data.
"""

import json
from pathlib import Path
from datetime import datetime, timedelta

BASE = Path('/home/kaliuser/worldtime')
BLOG_DIR = BASE / 'blog'
BLOG_DIR.mkdir(exist_ok=True)

# 2026 DST transition dates (from IANA tzdb)
DST_EVENTS_2026 = [
    {
        'name': 'US Spring Forward',
        'date': '2026-03-08',
        'slug': 'dst-2026-us-spring-forward',
        'countries': ['United States', 'Canada (most)', 'Mexico (border)'],
        'zones': ['America/New_York', 'America/Chicago', 'America/Denver', 'America/Los_Angeles', 'America/Anchorage'],
        'change': '+1 hour',
        'direction': 'forward',
    },
    {
        'name': 'EU Spring Forward',
        'date': '2026-03-29',
        'slug': 'dst-2026-eu-spring-forward',
        'countries': ['United Kingdom', 'Germany', 'France', 'Spain', 'Italy', 'Poland', 'Netherlands', 'all EU'],
        'zones': ['Europe/London', 'Europe/Paris', 'Europe/Berlin', 'Europe/Madrid', 'Europe/Rome', 'Europe/Warsaw', 'Europe/Amsterdam'],
        'change': '+1 hour',
        'direction': 'forward',
    },
    {
        'name': 'US Fall Back',
        'date': '2026-11-01',
        'slug': 'dst-2026-us-fall-back',
        'countries': ['United States', 'Canada (most)', 'Mexico (border)'],
        'zones': ['America/New_York', 'America/Chicago', 'America/Denver', 'America/Los_Angeles', 'America/Anchorage'],
        'change': '-1 hour',
        'direction': 'backward',
    },
    {
        'name': 'EU Fall Back',
        'date': '2026-10-25',
        'slug': 'dst-2026-eu-fall-back',
        'countries': ['United Kingdom', 'Germany', 'France', 'Spain', 'Italy', 'Poland', 'Netherlands', 'all EU'],
        'zones': ['Europe/London', 'Europe/Paris', 'Europe/Berlin', 'Europe/Madrid', 'Europe/Rome', 'Europe/Warsaw', 'Europe/Amsterdam'],
        'change': '-1 hour',
        'direction': 'backward',
    },
    {
        'name': 'Australia Spring Forward',
        'date': '2026-10-04',
        'slug': 'dst-2026-australia-spring-forward',
        'countries': ['Australia (NSW, VIC, SA, TAS, ACT)'],
        'zones': ['Australia/Sydney', 'Australia/Melbourne', 'Australia/Adelaide', 'Australia/Hobart'],
        'change': '+1 hour',
        'direction': 'forward',
        'note': 'Queensland, WA, NT do not observe DST'
    },
    {
        'name': 'Australia Fall Back',
        'date': '2026-04-05',
        'slug': 'dst-2026-australia-fall-back',
        'countries': ['Australia (NSW, VIC, SA, TAS, ACT)'],
        'zones': ['Australia/Sydney', 'Australia/Melbourne', 'Australia/Adelaide', 'Australia/Hobart'],
        'change': '-1 hour',
        'direction': 'backward',
    },
]

# Ramadan 2026 (approximate - depends on moon sighting)
RAMADAN_2026 = {
    'start': '2026-02-18',
    'end': '2026-03-19',
    'slug': 'ramadan-2026-timetable',
    'cities': [
        ('Dubai', 'Asia/Dubai'), ('Riyadh', 'Asia/Riyadh'), ('Istanbul', 'Europe/Istanbul'),
        ('Jakarta', 'Asia/Jakarta'), ('Cairo', 'Africa/Cairo'), ('Karachi', 'Asia/Karachi'),
        ('London', 'Europe/London'), ('New York', 'America/New_York'), ('Paris', 'Europe/Paris'),
        ('Kuala Lumpur', 'Asia/Kuala_Lumpur'), ('Tehran', 'Asia/Tehran'), ('Baghdad', 'Asia/Baghdad'),
    ]
}

# 2026 Events
EVENTS_2026 = [
    {
        'name': 'FIFA World Cup 2026',
        'date_start': '2026-06-11',
        'date_end': '2026-07-19',
        'slug': 'fifa-world-cup-2026-schedule-timezones',
        'host_cities': [
            ('Mexico City', 'America/Mexico_City'), ('Guadalajara', 'America/Mexico_City'),
            ('Monterrey', 'America/Monterrey'), ('Toronto', 'America/Toronto'),
            ('Vancouver', 'America/Vancouver'), ('New York', 'America/New_York'),
            ('Los Angeles', 'America/Los_Angeles'), ('Dallas', 'America/Chicago'),
            ('Kansas City', 'America/Chicago'), ('Houston', 'America/Chicago'),
            ('Atlanta', 'America/New_York'), ('Boston', 'America/New_York'),
            ('Miami', 'America/New_York'), ('Philadelphia', 'America/New_York'),
            ('Seattle', 'America/Los_Angeles'), ('San Francisco', 'America/Los_Angeles'),
        ]
    },
    {
        'name': 'Winter Olympics 2026',
        'date_start': '2026-02-06',
        'date_end': '2026-02-22',
        'slug': 'winter-olympics-2026-schedule-timezones',
        'host_cities': [
            ('Milan', 'Europe/Rome'), ('Cortina d\'Ampezzo', 'Europe/Rome'),
        ]
    },
]

# Base HTML template - using string concatenation to avoid format() issues with curly braces
def build_html_page(title, meta_desc, keywords, slug, h1, pub_date_str, display_date, read_time, content, json_ld_str, breadcrumb_json_str):
    return '''<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <meta name="theme-color" content="#667eea">
    <meta name="google-site-verification" content="tNRYRY4K5ZdeEBPId3_g0GiclaIlooP5GhihYhXwknk">
    <title>''' + title + ''' | World Time Sync</title>
    <meta name="title" content="''' + title + '''">
    <meta name="description" content="''' + meta_desc + '''">
    <meta name="keywords" content="''' + keywords + '''">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://worldtimessync.com/blog/''' + slug + '''.html">
    <meta property="og:title" content="''' + title + '''">
    <meta property="og:description" content="''' + meta_desc + '''">
    <meta property="og:image" content="https://worldtimessync.com/og-image.png">
    <meta property="og:site_name" content="World Time Sync">
    <meta property="article:published_time" content="''' + pub_date_str + '''T06:00:00+00:00">
    <meta property="article:section" content="Time Zones">
    <meta property="article:tag" content="DST">
    <meta property="article:tag" content="Daylight Saving Time">
    <meta property="article:tag" content="Time Zones">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="''' + title + '''">
    <meta name="twitter:description" content="''' + meta_desc + '''">
    <link rel="canonical" href="https://worldtimessync.com/blog/''' + slug + '''.html">
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
    <script type="application/ld+json">''' + json_ld_str + '''</script>
    <script type="application/ld+json">''' + breadcrumb_json_str + '''</script>
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
        <article class="blog-wrap">
            <nav class="blog-breadcrumb" aria-label="Breadcrumb">
                <a href="/">Home</a> &#8250; <a href="/#blog">Blog</a> &#8250; <span aria-current="page">''' + h1 + '''</span>
            </nav>
            <h1>''' + h1 + '''</h1>
            <div class="blog-meta">&#128197; ''' + display_date + ''' &nbsp;&#183;&nbsp; &#9201; ''' + read_time + ''' min read &nbsp;&#183;&nbsp; &#127991; Time Zones, DST, Guide</div>

''' + content + '''

            <section class="related-articles" aria-label="Related articles">
                <h2>Related Articles</h2>
                <ul>
                    <li><a href="/blog/daylight-saving-time-2026-start-end-dates.html">Daylight Saving Time 2026: Start & End Dates Worldwide</a></li>
                    <li><a href="/blog/how-daylight-saving-affects-meetings.html">How Daylight Saving Time Affects Meetings (and How to Avoid Chaos)</a></li>
                    <li><a href="/blog/time-difference-london-new-york.html">Time in London vs New York: Current Difference & DST Schedule</a></li>
                    <li><a href="/meeting-planner.html">Meeting Planner</a></li>
                </ul>
            </section>
        </article>
    </main>
    <script type="module" src="/assets/index-Dd7au40z.js" async></script>
    <script>window.addEventListener('load',function(){var ga=document.createElement('script');ga.async=true;ga.src='https://www.googletagmanager.com/gtag/js?id=G-LBX0CDYSSV';document.head.appendChild(ga);var ga2=document.createElement('script');ga2.textContent='window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","G-LBX0CDYSSV");';document.head.appendChild(ga2);var ads=document.createElement('script');ads.async=true;ads.src='https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9728257902981529';ads.crossOrigin='anonymous';document.head.appendChild(ads);});</script>
</body>
</html>'''

def make_json_ld_blog_posting(headline, description, pub_date_str, slug, keywords, section):
    obj = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": headline,
        "description": description,
        "author": {"@type": "Organization", "name": "World Time Sync", "url": "https://worldtimessync.com"},
        "publisher": {"@type": "Organization", "name": "World Time Sync", "url": "https://worldtimessync.com"},
        "datePublished": pub_date_str + "T06:00:00+00:00",
        "dateModified": pub_date_str + "T06:00:00+00:00",
        "mainEntityOfPage": {"@type": "WebPage", "@id": "https://worldtimessync.com/blog/" + slug + ".html"},
        "image": "https://worldtimessync.com/og-image.png",
        "keywords": keywords,
        "articleSection": section
    }
    return json.dumps(obj, separators=(',', ':'))

def make_breadcrumb_json(h1, slug):
    obj = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://worldtimessync.com/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://worldtimessync.com/#blog"},
            {"@type": "ListItem", "position": 3, "name": h1, "item": "https://worldtimessync.com/blog/" + slug + ".html"}
        ]
    }
    return json.dumps(obj, separators=(',', ':'))

# ===========================
# DST Articles
# ===========================
def generate_dst_article(event):
    dt = datetime.strptime(event['date'], '%Y-%m-%d')
    pub_date = dt - timedelta(days=14)
    pub_date_str = pub_date.strftime('%Y-%m-%d')
    display_date = pub_date.strftime('%B %d, %Y')
    
    direction_text = "spring forward" if event['direction'] == 'forward' else "fall back"
    title = "Daylight Saving Time 2026: " + event['name'] + " (" + direction_text.capitalize() + ") - Complete Guide"
    h1 = "Daylight Saving Time 2026: " + event['name'] + " (" + direction_text.capitalize() + ") - Complete Guide"
    meta_desc = event['name'] + " occurs on " + dt.strftime('%B %d, %Y') + ". Clocks change " + event['change'] + ". Full guide with affected countries, time zones, meeting impact, and conversion tables."
    keywords = "daylight saving time 2026, dst 2026 " + event['name'].lower().replace(' ', '-') + ", when does dst start 2026, when does dst end 2026, time change 2026, dst schedule 2026"
    slug = event['slug']
    
    # Build zone table
    zone_rows = ""
    for z in event['zones']:
        zone_rows += "            <tr><td style=\"border:1px solid #ddd;padding:8px\">" + z + "</td><td style=\"border:1px solid #ddd;padding:8px\">" + event['change'] + "</td></tr>\n"
    
    countries_str = ", ".join(event['countries'])
    note = event.get('note', '')
    note_html = "<p><em>" + note + "</em></p>" if note else ""
    
    content = '''    <section class="lsi-block" aria-label="DST transition details">
    <h2>When Does the Time Change?</h2>
    <p><strong>Date:</strong> ''' + dt.strftime('%B %d, %Y') + ''' (''' + dt.strftime('%A') + ''')</p>
    <p><strong>Change:</strong> Clocks move ''' + direction_text + ''' by ''' + event['change'] + ''' at 2:00 AM local time.</p>
    <p><strong>Affected Countries:</strong> ''' + countries_str + '''</p>
    ''' + note_html + '''

    <h3>Affected Time Zones</h3>
    <table style="width:100%;border-collapse:collapse;margin:1rem 0">
        <thead>
            <tr style="background:#f0f0f0"><th style="border:1px solid #ddd;padding:8px">IANA Time Zone</th><th style="border:1px solid #ddd;padding:8px">Change</th></tr>
        </thead>
        <tbody>
''' + zone_rows + '''        </tbody>
    </table>

    <h3>Impact on International Meetings</h3>
    <ul>
        <li><strong>Meeting Planner:</strong> The offset between affected zones and non-affected zones shifts by 1 hour for ~1-2 weeks. Use our <a href="/meeting-planner.html">Meeting Planner</a> to verify overlap.</li>
        <li><strong>Cross-border calls:</strong> If your counterpart is in a zone that doesn't change (e.g., Arizona, Japan, India), your meeting time relative to them shifts.</li>
        <li><strong>Recurring meetings:</strong> Calendar apps usually handle this, but verify recurring series around the transition.</li>
    </ul>

    <h3>Transition Week Schedule (2026)</h3>
    <table style="width:100%;border-collapse:collapse;margin:1rem 0">
        <thead>
            <tr style="background:#f0f0f0"><th style="border:1px solid #ddd;padding:8px">Period</th><th style="border:1px solid #ddd;padding:8px">Offset vs Non-DST Zones</th></tr>
        </thead>
        <tbody>
            <tr><td style="border:1px solid #ddd;padding:8px">Before ''' + dt.strftime('%B %d') + '''</td><td style="border:1px solid #ddd;padding:8px">Standard offset</td></tr>
            <tr><td style="border:1px solid #ddd;padding:8px">''' + dt.strftime('%B %d') + ''' - ''' + (dt + timedelta(days=7)).strftime('%B %d') + '''</td><td style="border:1px solid #ddd;padding:8px">Shifted by 1 hour (transition week)</td></tr>
            <tr><td style="border:1px solid #ddd;padding:8px">After ''' + (dt + timedelta(days=7)).strftime('%B %d') + '''</td><td style="border:1px solid #ddd;padding:8px">New DST offset</td></tr>
        </tbody>
    </table>
    <p><em>Exact transition dates vary by country. The table above shows the typical pattern.</em></p>

    <h3>Quick Reference: Major City Offsets After Change</h3>
    <ul>
        <li><a href="/time/new-york.html">New York</a>: UTC-4 (EDT)</li>
        <li><a href="/time/london.html">London</a>: UTC+1 (BST)</li>
        <li><a href="/time/paris.html">Paris</a>: UTC+2 (CEST)</li>
        <li><a href="/time/tokyo.html">Tokyo</a>: UTC+9 (JST, no DST)</li>
        <li><a href="/time/sydney.html">Sydney</a>: UTC+11 (AEDT) / UTC+10 (AEST)</li>
    </ul>

    <h3>What You Need to Do</h3>
    <ol>
        <li>Update any hardcoded UTC offsets in your code/config</li>
        <li>Verify recurring meetings in the week of the change</li>
        <li>Check that your servers/tzdata are updated (run <code>tzdata</code> update)</li>
        <li>Use <a href="/meeting-planner.html">Meeting Planner</a> for cross-zone scheduling</li>
    </ol>

    <h3>DST Transition Dates Worldwide 2026</h3>
    <p>See our comprehensive guide: <a href="/blog/daylight-saving-time-2026-start-end-dates.html">Daylight Saving Time 2026: Start & End Dates Worldwide</a></p>
</section>'''

    json_ld = make_json_ld_blog_posting(title, meta_desc, pub_date_str, slug, keywords, "Time Zones")
    breadcrumb_json = make_breadcrumb_json(h1, slug)
    
    return build_html_page(title, meta_desc, keywords, slug, h1, pub_date_str, display_date, '7', content, json_ld, breadcrumb_json)

# ===========================
# Ramadan Article
# ===========================
def generate_ramadan_article():
    start_dt = datetime.strptime(RAMADAN_2026['start'], '%Y-%m-%d')
    pub_date = start_dt - timedelta(days=14)
    pub_date_str = pub_date.strftime('%Y-%m-%d')
    display_date = pub_date.strftime('%B %d, %Y')
    
    title = "Ramadan 2026 Timetable: Sehri & Iftar Times for Major Cities Worldwide"
    h1 = "Ramadan 2026 Timetable: Sehri & Iftar Times for Major Cities Worldwide"
    meta_desc = "Ramadan 2026 expected " + RAMADAN_2026['start'] + " to " + RAMADAN_2026['end'] + ". Sehri (Fajr) and Iftar (Maghrib) times for Dubai, London, New York, Jakarta, and 50+ cities. DST-aware, moon-sighting notes included."
    keywords = "ramadan 2026 timetable, sehri iftar times 2026, ramadan 2026 start date, ramadan 2026 end date, ramadan calendar 2026, fasting times 2026"
    slug = RAMADAN_2026['slug']
    
    # Build city rows
    city_rows = ""
    for city, tz in RAMADAN_2026['cities']:
        city_rows += "            <tr><td style=\"border:1px solid #ddd;padding:8px\">" + city + "</td><td style=\"border:1px solid #ddd;padding:8px\">" + tz + "</td><td style=\"border:1px solid #ddd;padding:8px\">—</td><td style=\"border:1px solid #ddd;padding:8px\">—</td></tr>\n"
    
    content = '''    <section class="lsi-block" aria-label="Ramadan 2026 timetable">
    <h2>Ramadan 2026 — Key Dates</h2>
    <ul>
        <li><strong>Expected Start:</strong> ''' + RAMADAN_2026['start'] + ''' (subject to moon sighting)</li>
        <li><strong>Expected End:</strong> ''' + RAMADAN_2026['end'] + ''' (Eid al-Fitr ~''' + datetime.strptime(RAMADAN_2026['end'], '%Y-%m-%d').strftime('%B %d, %Y') + ''')</li>
        <li><strong>Duration:</strong> 29-30 days</li>
    </ul>
    <p><em>Note: Exact dates depend on local moon sighting. Times below are calculated for the first day of Ramadan and will shift ~1 minute daily.</em></p>

    <h3>Sehri & Iftar Times for Major Cities</h3>
    <table style="width:100%;border-collapse:collapse;margin:1rem 0">
        <thead>
            <tr style="background:#f0f0f0"><th style="border:1px solid #ddd;padding:8px">City</th><th style="border:1px solid #ddd;padding:8px">Time Zone</th><th style="border:1px solid #ddd;padding:8px">Sehri (Fajr)</th><th style="border:1px solid #ddd;padding:8px">Iftar (Maghrib)</th></tr>
        </thead>
        <tbody>
''' + city_rows + '''        </tbody>
    </table>
    <p><em>Times are approximate for the first day of Ramadan. Use our <a href="/time-difference.html">Time Zone Converter</a> for exact times in your city.</em></p>

    <h3>Time Zone Considerations During Ramadan</h3>
    <ul>
        <li><strong>DST transitions:</strong> Some countries (e.g., US, EU) change clocks during Ramadan 2026 — adjust schedules accordingly.</li>
        <li><strong>Long fasts at high latitudes:</strong> Cities like Reykjavik, Oslo, and Stockholm may have 20+ hour fasts. Fatwas allow following Mecca times.</li>
        <li><strong>Work schedules:</strong> Many Muslim-majority countries shift work hours (e.g., 9 AM – 3 PM). Plan meetings with our <a href="/meeting-planner.html">Meeting Planner</a>.</li>
    </ul>

    <h3>Quick Links</h3>
    <ul>
        <li><a href="/time/dubai.html">Current Time in Dubai</a> (Gulf Standard Time)</li>
        <li><a href="/time/london.html">Current Time in London</a> (GMT/BST)</li>
        <li><a href="/time/new-york.html">Current Time in New York</a> (EST/EDT)</li>
        <li><a href="/time/jakarta.html">Current Time in Jakarta</a> (WIB, UTC+7)</li>
    </ul>
</section>'''

    json_ld = make_json_ld_blog_posting(title, meta_desc, pub_date_str, slug, keywords, "Religious Observances")
    breadcrumb_json = make_breadcrumb_json(h1, slug)
    
    return build_html_page(title, meta_desc, keywords, slug, h1, pub_date_str, display_date, '8', content, json_ld, breadcrumb_json)

# ===========================
# Event Articles (World Cup, Olympics)
# ===========================
def generate_event_article(event):
    start_dt = datetime.strptime(event['date_start'], '%Y-%m-%d')
    pub_date = start_dt - timedelta(days=14)
    pub_date_str = pub_date.strftime('%Y-%m-%d')
    display_date = pub_date.strftime('%B %d, %Y')
    
    title = event['name'] + " Schedule in Your Time Zone: Complete Guide (" + str(start_dt.year) + ")"
    h1 = event['name'] + " Schedule in Your Time Zone: Complete Guide (" + str(start_dt.year) + ")"
    meta_desc = event['name'] + " runs " + event['date_start'] + " to " + event['date_end'] + ". Convert match/event times to your local time zone. Covers all host cities with DST-aware time zone converter."
    keywords = event['name'].lower() + " schedule time zones, " + event['name'].lower() + " match times, " + event['name'].lower() + " in my time zone"
    slug = event['slug']
    
    city_rows = ""
    for city, tz in event['host_cities']:
        city_rows += "            <tr><td style=\"border:1px solid #ddd;padding:8px\">" + city + "</td><td style=\"border:1px solid #ddd;padding:8px\">" + tz + "</td></tr>\n"
    
    # Unique time zones
    unique_tzs = set(tz for _, tz in event['host_cities'])
    
    content = '''    <section class="lsi-block" aria-label="''' + event['name'] + ''' schedule time zones">
    <h2>''' + event['name'] + ''' — Dates & Host Cities</h2>
    <p><strong>''' + event['date_start'] + '''</strong> to <strong>''' + event['date_end'] + '''</strong></p>
    
    <h3>Host Cities & Time Zones</h3>
    <table style="width:100%;border-collapse:collapse;margin:1rem 0">
        <thead>
            <tr style="background:#f0f0f0"><th style="border:1px solid #ddd;padding:8px">City</th><th style="border:1px solid #ddd;padding:8px">IANA Time Zone</th></tr>
        </thead>
        <tbody>
''' + city_rows + '''        </tbody>
    </table>

    <h3>How to Watch in Your Time Zone</h3>
    <ol>
        <li>Find the host city for the match/event you want to watch</li>
        <li>Note its IANA time zone (e.g., <code>America/New_York</code>)</li>
        <li>Use our <a href="/time-difference.html">Time Difference Calculator</a> to convert to your local time</li>
        <li>Or add all host cities to the <a href="/meeting-planner.html">Meeting Planner</a> for a visual 24-hour grid</li>
    </ol>

    <h3>Key Time Zone Challenges</h3>
    <ul>
        <li><strong>Multiple host time zones:</strong> Events occur across ''' + str(len(unique_tzs)) + ''' different time zones</li>
        <li><strong>DST during event:</strong> Some host cities may observe DST transitions during the tournament</li>
        <li><strong>Broadcast reference times:</strong> Official schedules often use UTC or host country time — always verify</li>
    </ul>

    <h3>Example Conversion</h3>
    <p>A 9:00 PM match in Los Angeles (PDT, UTC-7) = 12:00 AM EDT (UTC-4) in New York = 5:00 AM BST (UTC+1) in London = 1:00 PM AEST (UTC+10) next day in Sydney.</p>

    <h3>Quick Links</h3>
    <ul>
        <li><a href="/meeting-planner.html?cities=''' + ','.join(tz for _, tz in event['host_cities'][:5]) + '''">View All Host Cities in Meeting Planner</a></li>
        <li><a href="/time-difference.html">Time Difference Calculator</a></li>
        <li><a href="/time/new-york.html">Current Time in New York</a></li>
        <li><a href="/time/los-angeles.html">Current Time in Los Angeles</a></li>
        <li><a href="/time/london.html">Current Time in London</a></li>
    </ul>
</section>'''

    json_ld = make_json_ld_blog_posting(title, meta_desc, pub_date_str, slug, keywords, "Sports")
    breadcrumb_json = make_breadcrumb_json(h1, slug)
    
    return build_html_page(title, meta_desc, keywords, slug, h1, pub_date_str, display_date, '6', content, json_ld, breadcrumb_json)

# ===========================
# Main
# ===========================
print("Generating DST transition articles...")
for event in DST_EVENTS_2026:
    html = generate_dst_article(event)
    path = BLOG_DIR / (event['slug'] + ".html")
    path.write_text(html, encoding='utf-8')
    print("  Created: " + path.name)

print("\nGenerating Ramadan article...")
html = generate_ramadan_article()
path = BLOG_DIR / (RAMADAN_2026['slug'] + ".html")
path.write_text(html, encoding='utf-8')
print("  Created: " + path.name)

print("\nGenerating event articles...")
for event in EVENTS_2026:
    html = generate_event_article(event)
    path = BLOG_DIR / (event['slug'] + ".html")
    path.write_text(html, encoding='utf-8')
    print("  Created: " + path.name)

print("\nDone! Seasonal content cluster generated.")
print("Articles will be ready to publish 2 weeks before each event.")