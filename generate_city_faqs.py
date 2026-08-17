#!/usr/bin/env python3
"""
Generate and inject FAQPage schema.org JSON-LD into city pages.
Adds 5-7 targeted FAQ questions per city for rich snippets.
"""
import re
import json
from pathlib import Path
from zoneinfo import ZoneInfo
from datetime import datetime

BASE = Path('/home/kaliuser/worldtime')
CITY_DIR = BASE / 'time'

def get_city_data(html: str, filepath: Path) -> dict:
    """Extract city metadata from HTML."""
    data = {}
    
    # Get city name from title
    title_match = re.search(r'<title>([^<]+)</title>', html)
    if title_match:
        title = title_match.group(1)
        # "What Time Is It in London? Current Local Time Now" -> "London"
        data['city_name'] = title.split(' in ')[-1].split('?')[0].strip()
    
    # Get timezone from data-timezone attribute
    tz_match = re.search(r'data-timezone="([^"]+)"', html)
    if tz_match:
        data['timezone'] = tz_match.group(1)
    
    # Get country from breadcrumb
    breadcrumb_match = re.search(r'<a href="/country/([^"]+)">([^<]+)</a>', html)
    if breadcrumb_match:
        data['country_slug'] = breadcrumb_match.group(1)
        data['country_name'] = breadcrumb_match.group(2)
    
    # Fallback: extract from filename
    if 'city_name' not in data:
        slug = filepath.stem
        data['city_name'] = slug.replace('-', ' ').title()
    
    # Determine UTC offset from timezone
    if 'timezone' in data:
        try:
            tz = ZoneInfo(data['timezone'])
            now = datetime.now(tz)
            offset = now.utcoffset()
            if offset is not None:
                hours = offset.total_seconds() / 3600
                if hours == int(hours):
                    data['utc_offset'] = f"UTC{int(hours):+d}"
                else:
                    data['utc_offset'] = f"UTC{hours:+g}"
            else:
                data['utc_offset'] = "UTC+0"
            
            # Check DST
            dst = now.dst()
            data['has_dst'] = dst is not None and dst.total_seconds() != 0
        except Exception:
            data['utc_offset'] = "UTC+0"
            data['has_dst'] = False
    else:
        data['utc_offset'] = "UTC+0"
        data['has_dst'] = False
    
    return data

def generate_faqs(data: dict) -> list:
    """Generate 5-7 FAQ questions for the city."""
    city = data['city_name']
    country = data.get('country_name', '')
    tz = data.get('timezone', '')
    utc = data.get('utc_offset', 'UTC+0')
    has_dst = data.get('has_dst', False)
    
    faqs = []
    
    # 1. Current time question (primary intent)
    faqs.append({
        "@type": "Question",
        "name": f"What time is it in {city}?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": f"The current time in {city} is shown in the live clock on this page. {city} follows the {tz} time zone ({utc})."
        }
    })
    
    # 2. DST question
    if has_dst:
        faqs.append({
            "@type": "Question",
            "name": f"Does {city} observe daylight saving time?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f"Yes, {city} observes daylight saving time. Clocks change according to {tz} rules."
            }
        })
    else:
        faqs.append({
            "@type": "Question",
            "name": f"Does {city} observe daylight saving time?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f"No, {city} does not observe daylight saving time. The offset stays at {utc} year-round."
            }
        })
    
    # 3. UTC offset
    faqs.append({
        "@type": "Question",
        "name": f"What is the UTC offset for {city}?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": f"{city} is on {utc}."
        }
    })
    
    # 4. Time zone converter
    faqs.append({
        "@type": "Question",
        "name": f"How do I convert {city} time to my local time?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": f"Use our free time zone converter on the homepage to convert between {city} time and your local time zone."
        }
    })
    
    # 5. Time zone name / IANA
    faqs.append({
        "@type": "Question",
        "name": f"What time zone is {city} in?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": f"{city} is in the {tz} time zone (IANA)."
        }
    })
    
    # 6. Compare with major reference cities
    reference_cities = [
        ("New York", "America/New_York"),
        ("London", "Europe/London"),
        ("Tokyo", "Asia/Tokyo"),
        ("Sydney", "Australia/Sydney"),
        ("Dubai", "Asia/Dubai"),
    ]
    
    # Pick 2 reference cities in different hemispheres
    for ref_name, ref_tz in reference_cities[:2]:
        if ref_tz != tz:  # Don't compare with itself
            try:
                ref_zone = ZoneInfo(ref_tz)
                city_zone = ZoneInfo(tz)
                now = datetime.now(city_zone)
                city_offset = now.utcoffset().total_seconds() / 3600
                ref_now = datetime.now(ref_zone)
                ref_offset = ref_now.utcoffset().total_seconds() / 3600
                diff = city_offset - ref_offset
                
                if diff == int(diff):
                    diff_str = f"{int(diff):+d} hours"
                else:
                    diff_str = f"{diff:+g} hours"
                
                faqs.append({
                    "@type": "Question",
                    "name": f"What is the time difference between {city} and {ref_name}?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f"{city} is {diff_str} ahead of {ref_name} (may vary during DST transitions)."
                    }
                })
            except Exception:
                pass
    
    # 7. DST transition dates (if applicable)
    if has_dst:
        faqs.append({
            "@type": "Question",
            "name": f"When does {city} switch to daylight saving time?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f"{city} follows {tz} DST rules. Typically clocks spring forward in March and fall back in October/November. Check the live clock for current status."
            }
        })
    
    return faqs

def inject_faq_schema(html: str, faqs: list) -> str:
    """Inject FAQPage JSON-LD into the head, replacing any existing FAQPage."""
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faqs
    }
    schema_json = json.dumps(schema, ensure_ascii=False, separators=(',', ':'))
    script_tag = f'<script type="application/ld+json">{schema_json}</script>'
    
    # Remove existing FAQPage scripts first
    html = re.sub(r'<script type="application/ld\+json">\{.*?"@type"\s*:\s*"FAQPage".*?</script>\s*', '', html, flags=re.DOTALL)
    
    # Insert before closing </head>
    if '</head>' in html:
        html = html.replace('</head>', f'{script_tag}\n</head>')
    else:
        # Fallback: insert after first script tag
        html = re.sub(r'(<script type="application/ld\+json">.*?</script>)', 
                      r'\1\n' + script_tag, html, count=1)
    
    return html

def process_city_file(filepath: Path) -> bool:
    """Process a single city HTML file."""
    try:
        html = filepath.read_text(encoding='utf-8')
        
        data = get_city_data(html, filepath)
        if not data.get('city_name'):
            print(f"  SKIP (no city name): {filepath.name}")
            return False
        
        faqs = generate_faqs(data)
        new_html = inject_faq_schema(html, faqs)
        
        if new_html != html:
            filepath.write_text(new_html, encoding='utf-8')
            print(f"  UPDATED: {filepath.name} ({data['city_name']}, {len(faqs)} FAQs)")
            return True
        else:
            print(f"  SKIP (no change): {filepath.name}")
            return False
            
    except Exception as e:
        print(f"  ERROR: {filepath.name} - {e}")
        return False

def main():
    city_files = list(CITY_DIR.glob('*.html'))
    print(f"Found {len(city_files)} city pages")
    
    updated = 0
    for f in city_files:
        if process_city_file(f):
            updated += 1
    
    print(f"\nTotal updated: {updated}/{len(city_files)}")

if __name__ == '__main__':
    main()