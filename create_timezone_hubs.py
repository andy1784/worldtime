#!/usr/bin/env python3
"""Create Internal Linking Hub pages: /time-zones/europe, asia, americas"""
import os
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')

# Define countries by region (based on existing country/*.html files)
EUROPE_COUNTRIES = [
    ('albania', 'Albania'),
    ('andorra', 'Andorra'),
    ('austria', 'Austria'),
    ('belarus', 'Belarus'),
    ('belgium', 'Belgium'),
    ('bosnia-herzegovina', 'Bosnia and Herzegovina'),
    ('bulgaria', 'Bulgaria'),
    ('croatia', 'Croatia'),
    ('cyprus', 'Cyprus'),
    ('czech-republic', 'Czech Republic'),
    ('denmark', 'Denmark'),
    ('estonia', 'Estonia'),
    ('finland', 'Finland'),
    ('france', 'France'),
    ('germany', 'Germany'),
    ('greece', 'Greece'),
    ('hungary', 'Hungary'),
    ('ireland', 'Ireland'),
    ('italy', 'Italy'),
    ('latvia', 'Latvia'),
    ('lithuania', 'Lithuania'),
    ('luxembourg', 'Luxembourg'),
    ('malta', 'Malta'),
    ('moldova', 'Moldova'),
    ('monaco', 'Monaco'),
    ('montenegro', 'Montenegro'),
    ('netherlands', 'Netherlands'),
    ('north-macedonia', 'North Macedonia'),
    ('norway', 'Norway'),
    ('poland', 'Poland'),
    ('portugal', 'Portugal'),
    ('romania', 'Romania'),
    ('russia', 'Russia'),
    ('san-marino', 'San Marino'),
    ('serbia', 'Serbia'),
    ('slovakia', 'Slovakia'),
    ('slovenia', 'Slovenia'),
    ('spain', 'Spain'),
    ('sweden', 'Sweden'),
    ('switzerland', 'Switzerland'),
    ('ukraine', 'Ukraine'),
    ('united-kingdom', 'United Kingdom'),
    ('vatican-city', 'Vatican City'),
]

ASIA_COUNTRIES = [
    ('afghanistan', 'Afghanistan'),
    ('armenia', 'Armenia'),
    ('azerbaijan', 'Azerbaijan'),
    ('bahrain', 'Bahrain'),
    ('bangladesh', 'Bangladesh'),
    ('bhutan', 'Bhutan'),
    ('brunei', 'Brunei'),
    ('cambodia', 'Cambodia'),
    ('china', 'China'),
    ('cyprus', 'Cyprus'),
    ('georgia', 'Georgia'),
    ('india', 'India'),
    ('indonesia', 'Indonesia'),
    ('iran', 'Iran'),
    ('iraq', 'Iraq'),
    ('israel', 'Israel'),
    ('japan', 'Japan'),
    ('jordan', 'Jordan'),
    ('kazakhstan', 'Kazakhstan'),
    ('kuwait', 'Kuwait'),
    ('kyrgyzstan', 'Kyrgyzstan'),
    ('laos', 'Laos'),
    ('lebanon', 'Lebanon'),
    ('malaysia', 'Malaysia'),
    ('maldives', 'Maldives'),
    ('mongolia', 'Mongolia'),
    ('myanmar', 'Myanmar'),
    ('nepal', 'Nepal'),
    ('north-korea', 'North Korea'),
    ('oman', 'Oman'),
    ('pakistan', 'Pakistan'),
    ('philippines', 'Philippines'),
    ('qatar', 'Qatar'),
    ('saudi-arabia', 'Saudi Arabia'),
    ('singapore', 'Singapore'),
    ('south-korea', 'South Korea'),
    ('sri-lanka', 'Sri Lanka'),
    ('syria', 'Syria'),
    ('taiwan', 'Taiwan'),
    ('tajikistan', 'Tajikistan'),
    ('thailand', 'Thailand'),
    ('timor-leste', 'Timor-Leste'),
    ('turkey', 'Turkey'),
    ('turkmenistan', 'Turkmenistan'),
    ('united-arab-emirates', 'United Arab Emirates'),
    ('uzbekistan', 'Uzbekistan'),
    ('vietnam', 'Vietnam'),
    ('yemen', 'Yemen'),
]

AMERICAS_COUNTRIES = [
    ('antigua-barbuda', 'Antigua and Barbuda'),
    ('argentina', 'Argentina'),
    ('bahamas', 'Bahamas'),
    ('barbados', 'Barbados'),
    ('belize', 'Belize'),
    ('bolivia', 'Bolivia'),
    ('brazil', 'Brazil'),
    ('canada', 'Canada'),
    ('chile', 'Chile'),
    ('colombia', 'Colombia'),
    ('costa-rica', 'Costa Rica'),
    ('cuba', 'Cuba'),
    ('dominica', 'Dominica'),
    ('dominican-republic', 'Dominican Republic'),
    ('ecuador', 'Ecuador'),
    ('el-salvador', 'El Salvador'),
    ('grenada', 'Grenada'),
    ('guatemala', 'Guatemala'),
    ('guyana', 'Guyana'),
    ('haiti', 'Haiti'),
    ('honduras', 'Honduras'),
    ('jamaica', 'Jamaica'),
    ('mexico', 'Mexico'),
    ('nicaragua', 'Nicaragua'),
    ('panama', 'Panama'),
    ('paraguay', 'Paraguay'),
    ('peru', 'Peru'),
    ('st-kitts-nevis', 'St. Kitts and Nevis'),
    ('st-lucia', 'St. Lucia'),
    ('st-vincent-grenadines', 'St. Vincent and the Grenadines'),
    ('suriname', 'Suriname'),
    ('trinidad-tobago', 'Trinidad and Tobago'),
    ('united-states', 'United States'),
    ('uruguay', 'Uruguay'),
    ('venezuela', 'Venezuela'),
]

# Also filter to only existing country files
COUNTRY_DIR = BASE / 'country'

def get_existing_countries():
    """Get list of existing country files"""
    existing = set()
    for f in COUNTRY_DIR.glob('*.html'):
        name = f.stem
        existing.add(name)
    return existing

EXISTING_COUNTRIES = get_existing_countries()

def filter_existing(countries):
    """Filter to only countries that have HTML files"""
    result = []
    for slug, name in countries:
        if slug in EXISTING_COUNTRIES:
            result.append((slug, name))
    return result

EUROPE_COUNTRIES = filter_existing(EUROPE_COUNTRIES)
ASIA_COUNTRIES = filter_existing(ASIA_COUNTRIES)
AMERICAS_COUNTRIES = filter_existing(AMERICAS_COUNTRIES)

print(f"Europe: {len(EUROPE_COUNTRIES)} countries")
print(f"Asia: {len(ASIA_COUNTRIES)} countries")
print(f"Americas: {len(AMERICAS_COUNTRIES)} countries")

# Create time-zones directory
TZ_DIR = BASE / 'time-zones'
TZ_DIR.mkdir(exist_ok=True)

# Common HTML template
def make_page(region_name, region_slug, countries, description, keywords):
    # Build country cards HTML
    cards_html = ''
    for slug, name in countries:
        cards_html += f'''                <div class="country-card">
                    <a href="/country/{slug}.html" class="country-link">
                        <h3>{name}</h3>
                        <p>View time zones & cities</p>
                    </a>
                </div>
'''
    
    # Build JSON-LD BreadcrumbList
    breadcrumb_json = f'''    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://worldtimessync.com/"}},
        {{"@type": "ListItem", "position": 2, "name": "Time Zones by Region", "item": "https://worldtimessync.com/time-zones"}},
        {{"@type": "ListItem", "position": 3, "name": "{region_name} Time Zones", "item": "https://worldtimessync.com/time-zones/{region_slug}.html"}}
      ]
    }}
    </script>'''
    
    # Build JSON-LD ItemList for countries
    country_list = '[' + ','.join([
        f'{{"@type": "ListItem", "position": {i+1}, "name": "{name}", "item": "https://worldtimessync.com/country/{slug}.html"}}'
        for i, (slug, name) in enumerate(countries)
    ]) + ']'
    
    itemlist_json = f'''    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "ItemList",
      "itemListElement": {country_list}
    }}
    </script>'''
    
    html = f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <meta name="theme-color" content="#667eea">
    <meta name="google-site-verification" content="tNRYRY4K5ZdeEBPId3_g0GiclaIlooP5GhihYhXwknk">
    <title>Time Zones in {region_name} — Complete List & City Times | World Time Sync</title>
    <meta name="title" content="Time Zones in {region_name} — Complete List & City Times">
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://worldtimessync.com/time-zones/{region_slug}.html">
    <meta property="og:title" content="Time Zones in {region_name} — Complete List & City Times">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="https://worldtimessync.com/og-image.png">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="canonical" href="https://worldtimessync.com/time-zones/{region_slug}.html">
    <link rel="preload" href="/assets/country.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="/assets/country.css"></noscript>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="preconnect" href="https://www.googlesyndication.com">
    <link rel="dns-prefetch" href="https://www.googlesyndication.com">
    
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "Time Zones in {region_name}",
      "description": "{description}",
      "url": "https://worldtimessync.com/time-zones/{region_slug}.html"
    }}
    </script>
{breadcrumb_json}
{itemlist_json}
</head>
<body>
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <main id="main-content">
        <div class="container">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="/">Home</a> >
                <a href="/time-zones">Time Zones by Region</a> >
                <span aria-current="page">{region_name} Time Zones</span>
            </nav>
            <h1>🌍 Time Zones in {region_name}</h1>
            <p>{description}</p>
            
            <h2>Countries in {region_name}</h2>
            <p>Click any country to see its time zones, major cities, and current local times:</p>
            
            <div class="country-grid">
{cards_html}            </div>
            
            <div class="info-card">
                <h2>Quick Facts</h2>
                <ul>
                    <li><strong>Number of countries:</strong> {len(countries)}</li>
                    <li><strong>Total cities covered:</strong> 695+</li>
                </ul>
            </div>
            
            <h2>Related Pages</h2>
            <ul class="city-list">
                <li><a href="/">World Clock — All Cities</a></li>
                <li><a href="/meeting-planner.html">Meeting Planner — Find Best Time</a></li>
                <li><a href="/blog/how-to-convert-time-zones.html">How to Convert Time Zones</a></li>
                <li><a href="/blog/time-zone-converter-guide.html">Time Zone Converter Guide</a></li>
            </ul>
        </div>
        <footer class="seo-footer">
            <nav aria-label="Footer navigation">
                <a href="/privacy.html">Privacy Policy</a>
                <a href="/about.html">About Us</a>
                <a href="/">World Time Sync</a>
            </nav>
            <p>&copy; 2026 World Time Sync. All rights reserved.</p>
        </footer>
    </main>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-LBX0CDYSSV"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-LBX0CDYSSV');
    </script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9728257902981529" crossorigin="anonymous"></script>
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
</html>
'''
    return html

# Generate the three pages
pages = [
    {
        'slug': 'europe',
        'name': 'Europe',
        'countries': EUROPE_COUNTRIES,
        'description': 'Complete guide to time zones across Europe. Current local times, UTC offsets, DST schedules, and major cities for all European countries.',
        'keywords': 'Europe time zones, European time zones, time in Europe, European countries time'
    },
    {
        'slug': 'asia',
        'name': 'Asia',
        'countries': ASIA_COUNTRIES,
        'description': 'Complete guide to time zones across Asia. Current local times, UTC offsets, DST schedules, and major cities for all Asian countries.',
        'keywords': 'Asia time zones, Asian time zones, time in Asia, Asian countries time'
    },
    {
        'slug': 'americas',
        'name': 'Americas',
        'countries': AMERICAS_COUNTRIES,
        'description': 'Complete guide to time zones across the Americas. Current local times, UTC offsets, DST schedules, and major cities for all North and South American countries.',
        'keywords': 'Americas time zones, North America time zones, South America time zones, time in Americas'
    },
]

for page in pages:
    filepath = TZ_DIR / f"{page['slug']}.html"
    content = make_page(page['name'], page['slug'], page['countries'], page['description'], page['keywords'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filepath}")

print("\nDone! Three time-zone hub pages created.")