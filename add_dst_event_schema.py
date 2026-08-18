#!/usr/bin/env python3
"""
Generate Event schema for DST transitions on country and time-zone pages.
Optimized version using known DST rules.
"""
import re
import json
from pathlib import Path
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

BASE = Path('/home/kaliuser/worldtime')

# Known DST transition rules (month, week, weekday) for major timezones
# week: 1=first, 2=second, 3=third, 4=fourth, -1=last
# weekday: 0=Monday, 6=Sunday
DST_RULES = {
    # Northern Hemisphere (spring forward, fall back)
    'America/New_York': {'spring': (3, 2, 6), 'fall': (11, 1, 6)},  # 2nd Sun Mar, 1st Sun Nov
    'America/Chicago': {'spring': (3, 2, 6), 'fall': (11, 1, 6)},
    'America/Denver': {'spring': (3, 2, 6), 'fall': (11, 1, 6)},
    'America/Los_Angeles': {'spring': (3, 2, 6), 'fall': (11, 1, 6)},
    'America/Anchorage': {'spring': (3, 2, 6), 'fall': (11, 1, 6)},
    'America/Toronto': {'spring': (3, 2, 6), 'fall': (11, 1, 6)},
    'America/Vancouver': {'spring': (3, 2, 6), 'fall': (11, 1, 6)},
    'Europe/London': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},  # Last Sun Mar, Last Sun Oct
    'Europe/Paris': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Berlin': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Rome': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Madrid': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Amsterdam': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Brussels': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Vienna': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Zurich': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Stockholm': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Oslo': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Copenhagen': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Helsinki': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Warsaw': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Prague': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Budapest': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Bucharest': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Sofia': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Athens': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Dublin': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Lisbon': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Moscow': {},  # No DST since 2014
    'Europe/Kyiv': {'spring': (3, -1, 6), 'fall': (10, -1, 6)},
    'Europe/Minsk': {},  # No DST
    'Europe/Istanbul': {},  # No DST since 2016
    'Asia/Beirut': {'spring': (3, -1, 5), 'fall': (10, -1, 5)},  # Last Fri Mar, Last Fri Oct
    'Asia/Amman': {'spring': (3, -1, 4), 'fall': (10, -1, 4)},  # Last Thu Mar, Last Thu Oct
    'Asia/Jerusalem': {'spring': (3, -1, 5), 'fall': (10, -1, 5)},  # Complex rules
    'Asia/Damascus': {'spring': (3, -1, 5), 'fall': (10, -1, 5)},
    'Asia/Tehran': {'spring': (3, -1, 5), 'fall': (9, -1, 5)},  # Complex, approx
    'Asia/Baghdad': {},  # No DST
    'Asia/Riyadh': {},  # No DST
    'Asia/Dubai': {},  # No DST
    'Asia/Kuwait': {},  # No DST
    'Asia/Qatar': {},  # No DST
    'Asia/Bahrain': {},  # No DST
    'Asia/Muscat': {},  # No DST
    'Asia/Karachi': {},  # No DST
    'Asia/Kolkata': {},  # No DST
    'Asia/Kathmandu': {},  # No DST
    'Asia/Dhaka': {},  # No DST
    'Asia/Colombo': {},  # No DST
    'Asia/Yangon': {},  # No DST
    'Asia/Bangkok': {},  # No DST
    'Asia/Ho_Chi_Minh': {},  # No DST
    'Asia/Jakarta': {},  # No DST
    'Asia/Kuala_Lumpur': {},  # No DST
    'Asia/Singapore': {},  # No DST
    'Asia/Manila': {},  # No DST
    'Asia/Shanghai': {},  # No DST
    'Asia/Tokyo': {},  # No DST
    'Asia/Seoul': {},  # No DST
    'Asia/Hong_Kong': {},  # No DST
    'Asia/Taipei': {},  # No DST
    # Southern Hemisphere (fall forward, spring back)
    'Australia/Sydney': {'spring': (10, 1, 6), 'fall': (4, 1, 6)},  # 1st Sun Oct, 1st Sun Apr
    'Australia/Melbourne': {'spring': (10, 1, 6), 'fall': (4, 1, 6)},
    'Australia/Brisbane': {},  # No DST
    'Australia/Perth': {},  # No DST
    'Australia/Adelaide': {'spring': (10, 1, 6), 'fall': (4, 1, 6)},
    'Australia/Darwin': {},  # No DST
    'Pacific/Auckland': {'spring': (9, -1, 6), 'fall': (4, 1, 6)},  # Last Sun Sep, 1st Sun Apr
    'Pacific/Fiji': {'spring': (11, 1, 6), 'fall': (1, 2, 6)},  # Approx
    'America/Sao_Paulo': {},  # No DST currently
    'America/Santiago': {'spring': (9, 1, 6), 'fall': (4, 1, 6)},  # Approx
    'America/Argentina/Buenos_Aires': {},  # No DST
    'America/Bogota': {},  # No DST
    'America/Lima': {},  # No DST
    'America/Caracas': {},  # No DST
    'America/Mexico_City': {'spring': (4, 1, 6), 'fall': (10, -1, 6)},  # 1st Sun Apr, Last Sun Oct
    'America/Cancun': {},  # No DST
    'America/Asuncion': {'spring': (10, 1, 6), 'fall': (3, -1, 6)},  # Approx
    'Africa/Johannesburg': {},  # No DST
    'Africa/Cairo': {'spring': (4, -1, 4), 'fall': (10, -1, 4)},  # Last Thu Apr, Last Thu Oct
    'Africa/Lagos': {},  # No DST
    'Africa/Nairobi': {},  # No DST
    'Africa/Casablanca': {'spring': (3, -1, 0), 'fall': (10, -1, 0)},  # Complex, Ramadan-dependent
    'America/St_Johns': {'spring': (3, 2, 6), 'fall': (11, 1, 6)},  # Newfoundland
    'America/Halifax': {'spring': (3, 2, 6), 'fall': (11, 1, 6)},
    'America/Winnipeg': {'spring': (3, 2, 6), 'fall': (11, 1, 6)},
    'America/Regina': {},  # No DST
    'America/Edmonton': {'spring': (3, 2, 6), 'fall': (11, 1, 6)},
    'America/Yellowknife': {'spring': (3, 2, 6), 'fall': (11, 1, 6)},
    'America/Whitehorse': {},  # No DST
}

def nth_weekday(year: int, month: int, week: int, weekday: int) -> datetime:
    """Get the nth weekday of a month. week=-1 means last."""
    if week > 0:
        # First day of month
        d = datetime(year, month, 1)
        # Add days to reach target weekday
        days_ahead = (weekday - d.weekday() + 7) % 7
        d += timedelta(days=days_ahead)
        # Add weeks
        d += timedelta(weeks=week - 1)
        return d
    else:
        # Last weekday: start from last day of month
        if month == 12:
            d = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            d = datetime(year, month + 1, 1) - timedelta(days=1)
        # Go back to target weekday
        days_back = (d.weekday() - weekday + 7) % 7
        d -= timedelta(days=days_back)
        return d

def get_next_dst_event(timezone_str: str) -> dict:
    """Get the next upcoming DST transition as an Event schema."""
    try:
        tz = ZoneInfo(timezone_str)
        now = datetime.now(tz)
        today = now.date()
        current_year = now.year
        
        rules = DST_RULES.get(timezone_str, {})
        if not rules:
            return None
        
        events = []
        
        # Check spring transition
        if 'spring' in rules:
            month, week, weekday = rules['spring']
            for year in [current_year, current_year + 1]:
                dt = nth_weekday(year, month, week, weekday)
                # DST transitions typically happen at 2 AM local time
                dt = dt.replace(hour=2, minute=0, second=0, microsecond=0, tzinfo=tz)
                if dt.date() >= today:
                    is_dst_start = True  # Spring = DST starts (clocks forward)
                    events.append((dt, is_dst_start))
                    break
        
        # Check fall transition
        if 'fall' in rules:
            month, week, weekday = rules['fall']
            for year in [current_year, current_year + 1]:
                dt = nth_weekday(year, month, week, weekday)
                dt = dt.replace(hour=2, minute=0, second=0, microsecond=0, tzinfo=tz)
                if dt.date() >= today:
                    is_dst_start = False  # Fall = DST ends (clocks back)
                    events.append((dt, is_dst_start))
                    break
        
        if not events:
            return None
        
        # Get the nearest event
        events.sort(key=lambda x: x[0])
        next_dt, is_dst_start = events[0]
        
        event_date = next_dt.date().isoformat()
        
        if is_dst_start:
            name = f"Daylight Saving Time Starts ({timezone_str})"
            description = f"Clocks move forward 1 hour at 2:00 AM local time on {next_dt.strftime('%B %d, %Y')}. {timezone_str} switches to Daylight Saving Time."
        else:
            name = f"Daylight Saving Time Ends ({timezone_str})"
            description = f"Clocks move back 1 hour at 2:00 AM local time on {next_dt.strftime('%B %d, %Y')}. {timezone_str} returns to Standard Time."
        
        return {
            "@context": "https://schema.org",
            "@type": "Event",
            "name": name,
            "description": description,
            "startDate": event_date,
            "endDate": event_date,
            "eventStatus": "https://schema.org/EventScheduled",
            "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
            "location": {
                "@type": "VirtualLocation",
                "url": f"https://worldtimessync.com/time-zones/{timezone_str.lower().replace('/', '-')}"
            },
            "organizer": {
                "@type": "Organization",
                "name": "World Time Sync",
                "url": "https://worldtimessync.com"
            }
        }
    except Exception as e:
        print(f"Error getting next DST event for {timezone_str}: {e}")
        return None

# Timezone mapping for country pages (representative major city)
COUNTRY_TIMEZONES = {
    'united-states': 'America/New_York',
    'united-kingdom': 'Europe/London',
    'canada': 'America/Toronto',
    'australia': 'Australia/Sydney',
    'germany': 'Europe/Berlin',
    'france': 'Europe/Paris',
    'italy': 'Europe/Rome',
    'spain': 'Europe/Madrid',
    'russia': 'Europe/Moscow',
    'brazil': 'America/Sao_Paulo',
    'mexico': 'America/Mexico_City',
    'india': 'Asia/Kolkata',
    'china': 'Asia/Shanghai',
    'japan': 'Asia/Tokyo',
    'south-korea': 'Asia/Seoul',
    'indonesia': 'Asia/Jakarta',
    'turkey': 'Europe/Istanbul',
    'saudi-arabia': 'Asia/Riyadh',
    'south-africa': 'Africa/Johannesburg',
    'egypt': 'Africa/Cairo',
    'nigeria': 'Africa/Lagos',
    'kenya': 'Africa/Nairobi',
    'morocco': 'Africa/Casablanca',
    'argentina': 'America/Argentina/Buenos_Aires',
    'chile': 'America/Santiago',
    'colombia': 'America/Bogota',
    'peru': 'America/Lima',
    'venezuela': 'America/Caracas',
    'iran': 'Asia/Tehran',
    'iraq': 'Asia/Baghdad',
    'israel': 'Asia/Jerusalem',
    'pakistan': 'Asia/Karachi',
    'bangladesh': 'Asia/Dhaka',
    'thailand': 'Asia/Bangkok',
    'vietnam': 'Asia/Ho_Chi_Minh',
    'philippines': 'Asia/Manila',
    'malaysia': 'Asia/Kuala_Lumpur',
    'singapore': 'Asia/Singapore',
    'new-zealand': 'Pacific/Auckland',
    'fiji': 'Pacific/Fiji',
    'united-arab-emirates': 'Asia/Dubai',
    'qatar': 'Asia/Qatar',
    'kuwait': 'Asia/Kuwait',
    'bahrain': 'Asia/Bahrain',
    'oman': 'Asia/Muscat',
    'jordan': 'Asia/Amman',
    'lebanon': 'Asia/Beirut',
    'syria': 'Asia/Damascus',
    'ukraine': 'Europe/Kyiv',
    'belarus': 'Europe/Minsk',
    'kazakhstan': 'Asia/Almaty',
    'uzbekistan': 'Asia/Tashkent',
    'turkmenistan': 'Asia/Ashgabat',
    'kyrgyzstan': 'Asia/Bishkek',
    'tajikistan': 'Asia/Dushanbe',
    'afghanistan': 'Asia/Kabul',
    'nepal': 'Asia/Kathmandu',
    'sri-lanka': 'Asia/Colombo',
    'myanmar': 'Asia/Yangon',
    'cambodia': 'Asia/Phnom_Penh',
    'laos': 'Asia/Vientiane',
    'mongolia': 'Asia/Ulaanbaatar',
    'north-korea': 'Asia/Pyongyang',
    'taiwan': 'Asia/Taipei',
    'hong-kong': 'Asia/Hong_Kong',
    'macau': 'Asia/Macau',
    'austria': 'Europe/Vienna',
    'belgium': 'Europe/Brussels',
    'netherlands': 'Europe/Amsterdam',
    'switzerland': 'Europe/Zurich',
    'sweden': 'Europe/Stockholm',
    'norway': 'Europe/Oslo',
    'denmark': 'Europe/Copenhagen',
    'finland': 'Europe/Helsinki',
    'poland': 'Europe/Warsaw',
    'czech-republic': 'Europe/Prague',
    'hungary': 'Europe/Budapest',
    'romania': 'Europe/Bucharest',
    'bulgaria': 'Europe/Sofia',
    'greece': 'Europe/Athens',
    'ireland': 'Europe/Dublin',
    'portugal': 'Europe/Lisbon',
}

def enhance_country_page(html: str, filepath: Path) -> str:
    """Add DST Event schema to country page."""
    slug = filepath.stem
    tz = COUNTRY_TIMEZONES.get(slug)
    
    if not tz:
        return html
    
    event = get_next_dst_event(tz)
    if not event:
        return html
    
    event_json = json.dumps(event, ensure_ascii=False, separators=(',', ':'))
    event_script = f'<script type="application/ld+json">{event_json}</script>'
    
    # Insert before </head>
    if '</head>' in html and 'schema.org/Event' not in html:
        html = html.replace('</head>', f'{event_script}\n</head>')
    
    return html

def enhance_timezone_page(html: str, filepath: Path) -> str:
    """Add DST Event schema to time-zone page."""
    slug = filepath.stem
    
    tz_map = {
        'est': 'America/New_York',
        'edt': 'America/New_York',
        'cst': 'America/Chicago',
        'cdt': 'America/Chicago',
        'mst': 'America/Denver',
        'mdt': 'America/Denver',
        'pst': 'America/Los_Angeles',
        'pdt': 'America/Los_Angeles',
        'gmt': 'Europe/London',
        'utc': 'UTC',
        'cet': 'Europe/Paris',
        'cest': 'Europe/Paris',
        'eet': 'Europe/Helsinki',
        'eest': 'Europe/Helsinki',
        'msk': 'Europe/Moscow',
        'ist': 'Asia/Kolkata',
        'jst': 'Asia/Tokyo',
        'kst': 'Asia/Seoul',
        'cst-china': 'Asia/Shanghai',
        'aest': 'Australia/Sydney',
        'aedt': 'Australia/Sydney',
        'acst': 'Australia/Adelaide',
        'acdt': 'Australia/Adelaide',
        'awst': 'Australia/Perth',
        'nzst': 'Pacific/Auckland',
        'nzdt': 'Pacific/Auckland',
        'brt': 'America/Sao_Paulo',
        'brst': 'America/Sao_Paulo',
        'art': 'America/Argentina/Buenos_Aires',
        'clst': 'America/Santiago',
        'clt': 'America/Santiago',
        'cot': 'America/Bogota',
        'pyt': 'America/Asuncion',
        'pyst': 'America/Asuncion',
        'est-brazil': 'America/Fortaleza',
        'akt': 'America/Anchorage',
        'akdt': 'America/Anchorage',
        'hst': 'Pacific/Honolulu',
        'hdt': 'Pacific/Honolulu',
        'sst': 'Pacific/Pago_Pago',
        'chast': 'Pacific/Chatham',
        'chadt': 'Pacific/Chatham',
        'wib': 'Asia/Jakarta',
        'wita': 'Asia/Makassar',
        'wit': 'Asia/Jayapura',
        'ict': 'Asia/Bangkok',
        'myt': 'Asia/Kuala_Lumpur',
        'sgt': 'Asia/Singapore',
        'pht': 'Asia/Manila',
        'cxt': 'Indian/Christmas',
        'mut': 'Indian/Mauritius',
        'syt': 'Asia/Srednekolymsk',
        'vost': 'Antarctica/Vostok',
    }
    
    tz = tz_map.get(slug.lower())
    
    if not tz:
        return html
    
    event = get_next_dst_event(tz)
    if not event:
        return html
    
    event_json = json.dumps(event, ensure_ascii=False, separators=(',', ':'))
    event_script = f'<script type="application/ld+json">{event_json}</script>'
    
    # Insert before </head>
    if '</head>' in html and 'schema.org/Event' not in html:
        html = html.replace('</head>', f'{event_script}\n</head>')
    
    return html

def process_file(filepath: Path) -> bool:
    """Process a single HTML file."""
    try:
        html = filepath.read_text(encoding='utf-8')
        original = html
        
        rel_path = filepath.relative_to(BASE)
        path_str = str(rel_path)
        
        # Skip redirect stubs
        if 'Redirecting' in html:
            return False
        
        if path_str.startswith('country/') and path_str.endswith('.html'):
            html = enhance_country_page(html, filepath)
        elif path_str.startswith('time-zones/') and path_str.endswith('.html'):
            html = enhance_timezone_page(html, filepath)
        else:
            return False
        
        if html != original:
            filepath.write_text(html, encoding='utf-8')
            print(f"  UPDATED: {path_str}")
            return True
        else:
            return False
            
    except Exception as e:
        print(f"  ERROR: {filepath} - {e}")
        return False

def main():
    updated = 0
    
    # Process country pages
    for filepath in (BASE / 'country').glob('*.html'):
        if process_file(filepath):
            updated += 1
    
    # Process time-zone pages
    for filepath in (BASE / 'time-zones').glob('*.html'):
        if process_file(filepath):
            updated += 1
    
    print(f"\nTotal updated: {updated}")

if __name__ == '__main__':
    main()