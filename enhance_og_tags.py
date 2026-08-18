#!/usr/bin/env python3
"""
Enhance OG/Twitter meta tags across all page types:
- Add og:image:width/height (1200x630)
- Add article:published_time/article:modified_time for blog posts
- Add article:author for blog posts
- Add twitter:image:alt, twitter:site
"""
import re
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')

OG_IMAGE_URL = "https://worldtimessync.com/og-image.png"
OG_IMAGE_WIDTH = "1200"
OG_IMAGE_HEIGHT = "630"
TWITTER_SITE = "@worldtimesync"
TWITTER_CREATOR = "@worldtimesync"
AUTHOR_URL = "https://worldtimessync.com/"

def enhance_city_page(html: str, filepath: Path) -> str:
    """Enhance city/time pages."""
    # Add og:image:width/height after og:image
    if 'og:image:width' not in html:
        html = re.sub(
            r'(<meta property="og:image" content="[^"]+">)',
            r'\1\n    <meta property="og:image:width" content="' + OG_IMAGE_WIDTH + '">\n    <meta property="og:image:height" content="' + OG_IMAGE_HEIGHT + '">',
            html
        )
    
    # Add twitter:image:alt after twitter:image
    if 'twitter:image:alt' not in html:
        # Extract title for alt text
        title_match = re.search(r'<title>([^<]+)</title>', html)
        alt_text = title_match.group(1) if title_match else "World Time Sync"
        html = re.sub(
            r'(<meta name="twitter:image" content="[^"]+">)',
            r'\1\n    <meta name="twitter:image:alt" content="' + alt_text + '">',
            html
        )
    
    # Add twitter:site if missing
    if 'twitter:site' not in html:
        html = re.sub(
            r'(<meta name="twitter:creator" content="[^"]+">)',
            r'\1\n    <meta name="twitter:site" content="' + TWITTER_SITE + '">',
            html
        )
    
    return html

def enhance_blog_page(html: str, filepath: Path) -> str:
    """Enhance blog pages with article meta."""
    # Add og:image:width/height
    if 'og:image:width' not in html:
        html = re.sub(
            r'(<meta property="og:image" content="[^"]+">)',
            r'\1\n    <meta property="og:image:width" content="' + OG_IMAGE_WIDTH + '">\n    <meta property="og:image:height" content="' + OG_IMAGE_HEIGHT + '">',
            html
        )
    
    # Add twitter:image:alt
    if 'twitter:image:alt' not in html:
        title_match = re.search(r'<title>([^<]+)</title>', html)
        alt_text = title_match.group(1) if title_match else "World Time Sync Blog"
        html = re.sub(
            r'(<meta name="twitter:image" content="[^"]+">)',
            r'\1\n    <meta name="twitter:image:alt" content="' + alt_text + '">',
            html
        )
    
    # Add twitter:site
    if 'twitter:site' not in html:
        html = re.sub(
            r'(<meta name="twitter:creator" content="[^"]+">)',
            r'\1\n    <meta name="twitter:site" content="' + TWITTER_SITE + '">',
            html
        )
    
    # Add article meta tags (published_time, modified_time, author)
    # Extract date from Article schema if present
    published = "2026-06-28"
    modified = "2026-06-28"
    
    schema_match = re.search(r'"datePublished"\s*:\s*"([^"]+)"', html)
    if schema_match:
        published = schema_match.group(1)
    
    schema_match = re.search(r'"dateModified"\s*:\s*"([^"]+)"', html)
    if schema_match:
        modified = schema_match.group(1)
    
    article_meta = f'''    <meta property="article:published_time" content="{published}">
    <meta property="article:modified_time" content="{modified}">
    <meta property="article:author" content="{AUTHOR_URL}">
    <meta property="article:publisher" content="{AUTHOR_URL}">'''
    
    if 'article:published_time' not in html:
        # Insert after og:site_name or og:description
        if 'og:site_name' in html:
            html = re.sub(
                r'(<meta property="og:site_name" content="[^"]+">)',
                r'\1\n' + article_meta,
                html
            )
        elif 'og:description' in html:
            html = re.sub(
                r'(<meta property="og:description" content="[^"]+">)',
                r'\1\n' + article_meta,
                html
            )
        else:
            # Fallback: insert before </head>
            html = re.sub(
                r'(</head>)',
                article_meta + '\n' + r'\1',
                html
            )
    
    return html

def enhance_country_page(html: str, filepath: Path) -> str:
    """Enhance country pages."""
    return enhance_city_page(html, filepath)  # Same treatment as city pages

def enhance_timezone_page(html: str, filepath: Path) -> str:
    """Enhance time-zone pages."""
    return enhance_city_page(html, filepath)

def enhance_world_clock_page(html: str, filepath: Path) -> str:
    """Enhance world-clock page."""
    return enhance_city_page(html, filepath)

def enhance_homepage(html: str, filepath: Path) -> str:
    """Enhance homepage."""
    # Add og:image:width/height
    if 'og:image:width' not in html:
        html = re.sub(
            r'(<meta property="og:image" content="[^"]+">)',
            r'\1\n    <meta property="og:image:width" content="' + OG_IMAGE_WIDTH + '">\n    <meta property="og:image:height" content="' + OG_IMAGE_HEIGHT + '">',
            html
        )
    
    # Add twitter:image:alt
    if 'twitter:image:alt' not in html:
        html = re.sub(
            r'(<meta name="twitter:image" content="[^"]+">)',
            r'\1\n    <meta name="twitter:image:alt" content="World Time Sync - Current Time Worldwide">',
            html
        )
    
    # Add twitter:site
    if 'twitter:site' not in html:
        html = re.sub(
            r'(<meta name="twitter:creator" content="[^"]+">)',
            r'\1\n    <meta name="twitter:site" content="' + TWITTER_SITE + '">',
            html
        )
    
    return html

def process_file(filepath: Path) -> bool:
    """Process a single HTML file based on its type."""
    try:
        html = filepath.read_text(encoding='utf-8')
        original = html
        
        rel_path = filepath.relative_to(BASE)
        path_str = str(rel_path)
        
        if path_str == 'index.html':
            html = enhance_homepage(html, filepath)
        elif path_str.startswith('time/') and path_str.endswith('.html'):
            html = enhance_city_page(html, filepath)
        elif path_str.startswith('blog/') and path_str.endswith('.html'):
            html = enhance_blog_page(html, filepath)
        elif path_str.startswith('country/') and path_str.endswith('.html'):
            html = enhance_country_page(html, filepath)
        elif path_str.startswith('time-zones/') and path_str.endswith('.html'):
            html = enhance_timezone_page(html, filepath)
        elif path_str == 'world-clock.html':
            html = enhance_world_clock_page(html, filepath)
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
    
    # Process all HTML files
    for filepath in BASE.rglob('*.html'):
        # Skip language subdirectories for now (they'll be handled separately if needed)
        if any(part in ['de', 'es', 'fr', 'it', 'ja', 'ru', 'uk', 'zh', 'ar', 'hi', 'pt'] for part in filepath.parts if part != 'blog'):
            continue
        if 'node_modules' in filepath.parts or '.git' in filepath.parts:
            continue
            
        if process_file(filepath):
            updated += 1
    
    print(f"\nTotal updated: {updated}")

if __name__ == '__main__':
    main()