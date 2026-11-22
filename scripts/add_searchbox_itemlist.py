#!/usr/bin/env python3
"""Add Schema.org SearchBox (WebSite + SearchAction) and ItemList to catalog pages.

1. index.html      -> WebSite with potentialAction SearchAction (SERP search box)
2. time-zones/index.html -> ItemList of all time zones listed on the page
3. world-clock.html      -> ItemList of major cities shown in the world clock

Idempotent: skips pages that already carry the target @type.
"""
import json
import os
import re

ROOT = '/home/kaliuser/worldtime'

# ------------------------------------------------------------------ city data
CITIES = json.load(open(os.path.join(ROOT, 'cities_data.json'), encoding='utf-8'))
CITY_BY_NAME = {c['name']: c for c in CITIES}

WORLD_CLOCK_CITIES = [
    'New York', 'London', 'Tokyo', 'Los Angeles', 'Chicago', 'Dubai',
    'Singapore', 'Sydney', 'Mumbai', 'Moscow', 'Istanbul', 'Paris',
    'Berlin', 'Toronto',
]

def slugify(name):
    s = name.lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'\s+', '-', s).strip('-')
    return s

# ------------------------------------------------------------------ helpers
def has_type(html, atype):
    return f'"@type": "{atype}"' in html or f'"@type":"{atype}"' in html

def insert_before_head_tail(html, json_block, sentinel='</head>'):
    """Insert json_block right before the first </head>. Idempotent via has_type caller."""
    idx = html.find(sentinel)
    if idx < 0:
        return html
    return html[:idx] + json_block + '\n' + html[idx:]

def json_ld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False) + '\n</script>'

# ------------------------------------------------------------------ 1) SearchBox on index.html
def add_searchbox(html):
    if has_type(html, 'WebSite') and 'SearchAction' in html:
        return html, False
    website = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "World Time Sync",
        "url": "https://worldtimessync.com/",
        "description": "Free online world clock showing current local time in 700+ cities worldwide",
        "inLanguage": "en",
        "potentialAction": {
            "@type": "SearchAction",
            "target": {
                "@type": "EntryPoint",
                "urlTemplate": "https://worldtimessync.com/search?q={search_term_string}"
            },
            "query-input": "required name=search_term_string"
        }
    }
    block = json_ld(website)
    return insert_before_head_tail(html, block), True

# ------------------------------------------------------------------ 2) ItemList on time-zones/index.html
TIME_ZONES_ITEMS = [
    ("Australian Eastern Standard Time", "aest", "UTC+10"),
    ("Alaska Standard Time", "akst", "UTC-9"),
    ("Brasilia Time", "brt", "UTC-3"),
    ("Central European Time", "cet", "UTC+1"),
    ("Central Standard Time", "cst", "UTC-6"),
    ("China Standard Time", "cst-china", "UTC+8"),
    ("Eastern European Time", "eet", "UTC+2"),
    ("Eastern Standard Time", "est", "UTC-5"),
    ("Greenwich Mean Time", "gmt", "UTC+0"),
    ("Hawaii Standard Time", "hst", "UTC-10"),
    ("India Standard Time", "ist", "UTC+5:30"),
    ("Japan Standard Time", "jst", "UTC+9"),
    ("Korea Standard Time", "kst", "UTC+9"),
    ("Moscow Standard Time", "msk", "UTC+3"),
    ("Mountain Standard Time", "mst", "UTC-7"),
    ("Pacific Standard Time", "pst", "UTC-8"),
    ("Coordinated Universal Time", "utc", "UTC+0"),
]

def add_tz_itemlist(html):
    if has_type(html, 'ItemList'):
        return html, False
    elements = []
    for pos, (name, slug, offset) in enumerate(TIME_ZONES_ITEMS, 1):
        elements.append({
            "@type": "ListItem",
            "position": pos,
            "name": name,
            "url": f"https://worldtimessync.com/time-zones/{slug}",
        })
    itemlist = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "All Time Zones",
        "description": "Complete list of major time zones worldwide with current time and UTC offsets",
        "numberOfItems": len(elements),
        "itemListElement": elements,
    }
    block = json_ld(itemlist)
    return insert_before_head_tail(html, block), True

# ------------------------------------------------------------------ 3) ItemList on world-clock.html
def add_world_clock_itemlist(html):
    if has_type(html, 'ItemList'):
        return html, False
    elements = []
    for pos, name in enumerate(WORLD_CLOCK_CITIES, 1):
        c = CITY_BY_NAME.get(name)
        if not c:
            continue
        elements.append({
            "@type": "ListItem",
            "position": pos,
            "name": name,
            "url": f"https://worldtimessync.com/time/{slugify(name)}",
        })
    itemlist = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "World Clock Cities",
        "description": "Major cities in the world clock with current local time",
        "numberOfItems": len(elements),
        "itemListElement": elements,
    }
    block = json_ld(itemlist)
    return insert_before_head_tail(html, block), True

# ------------------------------------------------------------------ main
PAGES = [
    ('index.html', add_searchbox),
    ('time-zones/index.html', add_tz_itemlist),
    ('world-clock.html', add_world_clock_itemlist),
]

def main():
    total_changed = 0
    for rel, fn in PAGES:
        path = os.path.join(ROOT, rel)
        html = open(path, encoding='utf-8').read()
        new_html, changed = fn(html)
        if changed:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(new_html)
                fh.flush(); os.fsync(fh.fileno())
            total_changed += 1
            print(f'Updated {rel}')
        else:
            print(f'Skipped {rel} (already has target schema)')
    print(f'\nChanged {total_changed} of {len(PAGES)} pages')

if __name__ == '__main__':
    main()
