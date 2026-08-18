#!/usr/bin/env python3
"""
Generate search index (search-index.json) for Fuse.js client-side search.
Extracts title, description, URL, and tags from all pages.
"""
import re
import json
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')

# Pages to index
INCLUDE_DIRS = ['time', 'country', 'time-zones', 'blog']
INCLUDE_FILES = ['index.html', 'world-clock.html', 'time-difference.html', 'meeting-planner.html', 'search.html']

EXCLUDE_PATTERNS = [
    r'.*-[a-z]{2}\.html$',  # Localized versions
    r'^[a-z]{2}-.*\.html$',  # Prefix localized
    r'index-[a-z]{2}\.html$',
    r'page/\d+/',
]

def should_index(filepath: Path) -> bool:
    """Check if file should be indexed."""
    rel = str(filepath.relative_to(BASE))
    
    # Check exclude patterns
    for pattern in EXCLUDE_PATTERNS:
        if re.search(pattern, rel):
            return False
    
    # Must be in included dirs or files
    for d in INCLUDE_DIRS:
        if rel.startswith(d + '/'):
            return True
    for f in INCLUDE_FILES:
        if rel == f:
            return True
    
    return False

def extract_metadata(filepath: Path) -> dict:
    """Extract title, description, tags from HTML file."""
    try:
        html = filepath.read_text(encoding='utf-8')
    except:
        return None
    
    # Extract title
    title_match = re.search(r'<title>([^<]+)</title>', html)
    title = title_match.group(1) if title_match else filepath.stem
    
    # Extract description
    desc_match = re.search(r'<meta name="description" content="([^"]+)">', html)
    if not desc_match:
        desc_match = re.search(r'<meta property="og:description" content="([^"]+)">', html)
    description = desc_match.group(1) if desc_match else ""
    
    # Extract keywords
    kw_match = re.search(r'<meta name="keywords" content="([^"]+)">', html)
    keywords = kw_match.group(1) if kw_match else ""
    
    # Extract og:type
    og_type_match = re.search(r'<meta property="og:type" content="([^"]+)">', html)
    og_type = og_type_match.group(1) if og_type_match else "website"
    
    # Build URL
    rel = str(filepath.relative_to(BASE))
    if rel == 'index.html':
        url = '/'
    elif rel.endswith('.html'):
        url = '/' + rel[:-5]
    else:
        url = '/' + rel
    
    # Build tags
    tags = []
    if og_type == 'article':
        tags.append('blog')
    elif 'time/' in rel:
        tags.append('city')
    elif 'country/' in rel:
        tags.append('country')
    elif 'time-zones/' in rel:
        tags.append('timezone')
    elif 'blog/' in rel:
        tags.append('blog')
    elif rel in ['world-clock.html', 'time-difference.html', 'meeting-planner.html']:
        tags.append('tool')
    
    if keywords:
        tags.extend([k.strip() for k in keywords.split(',') if k.strip()])
    
    # Add city/country names from URL
    if 'time/' in rel:
        city = rel.split('/')[-1].replace('.html', '').replace('-', ' ').title()
        tags.append(city)
    elif 'country/' in rel:
        country = rel.split('/')[-1].replace('.html', '').replace('-', ' ').title()
        tags.append(country)
    elif 'time-zones/' in rel:
        tz = rel.split('/')[-1].replace('.html', '').upper()
        tags.append(tz)
    
    # Deduplicate tags
    tags = list(dict.fromkeys(tags))
    
    return {
        'title': title,
        'description': description,
        'url': url,
        'tags': tags,
        'type': og_type,
    }

def main():
    items = []
    
    for filepath in BASE.rglob('*.html'):
        if not should_index(filepath):
            continue
        
        meta = extract_metadata(filepath)
        if meta:
            items.append(meta)
    
    print(f"Indexed {len(items)} pages")
    
    # Write search index
    output = BASE / 'search-index.json'
    output.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Created {output}")
    
    # Show sample
    if items:
        print("\nSample entry:")
        print(json.dumps(items[0], ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()