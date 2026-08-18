#!/usr/bin/env python3
"""
Generate RSS 2.0, Atom 1.0, and JSON Feed 1.1 for the blog.
Outputs to /feed.rss, /feed.atom, /feed.json
"""
import re
import json
from pathlib import Path
from datetime import datetime
from email.utils import formatdate

BASE = Path('/home/kaliuser/worldtime')
BLOG_DIR = BASE / 'blog'

SITE_URL = "https://worldtimessync.com"
SITE_TITLE = "World Time Sync"
SITE_DESCRIPTION = "Current time, time zones, and world clock tools. Blog covers time zone conversions, DST, scheduling across time zones, and global time coordination."
OG_IMAGE_URL = "https://worldtimessync.com/og-image.png"
AUTHOR_NAME = "World Time Sync"
AUTHOR_URL = "https://worldtimessync.com/"

def parse_blog_post(filepath: Path) -> dict:
    """Extract metadata from a blog post HTML file."""
    try:
        html = filepath.read_text(encoding='utf-8')
        
        # Extract title
        title_match = re.search(r'<title>([^<]+)</title>', html)
        title = title_match.group(1) if title_match else filepath.stem
        
        # Extract description
        desc_match = re.search(r'<meta name="description" content="([^"]+)">', html)
        description = desc_match.group(1) if desc_match else ""
        
        # Extract og:image
        og_image_match = re.search(r'<meta property="og:image" content="([^"]+)">', html)
        og_image = og_image_match.group(1) if og_image_match else OG_IMAGE_URL
        
        # Extract date from Article schema
        date_published = "2026-06-28"
        date_modified = "2026-06-28"
        
        schema_match = re.search(r'"datePublished"\s*:\s*"([^"]+)"', html)
        if schema_match:
            date_published = schema_match.group(1)
        
        schema_match = re.search(r'"dateModified"\s*:\s*"([^"]+)"', html)
        if schema_match:
            date_modified = schema_match.group(1)
        
        # Extract keywords
        keywords_match = re.search(r'<meta name="keywords" content="([^"]+)">', html)
        keywords = keywords_match.group(1) if keywords_match else ""
        
        # Extract article section
        section_match = re.search(r'"articleSection"\s*:\s*"([^"]+)"', html)
        section = section_match.group(1) if section_match else "Time Zones"
        
        # Build URL
        slug = filepath.stem
        url = f"{SITE_URL}/blog/{slug}.html"
        
        # Generate GUID
        guid = url
        
        # Parse date for RFC 822 format
        try:
            pub_date = datetime.fromisoformat(date_published)
            pub_date_rfc822 = formatdate(pub_date.timestamp(), usegmt=True)
        except:
            pub_date_rfc822 = formatdate(datetime.now().timestamp(), usegmt=True)
        
        try:
            mod_date = datetime.fromisoformat(date_modified)
            mod_date_rfc3339 = mod_date.isoformat() + 'Z'
        except:
            mod_date_rfc3339 = datetime.now().isoformat() + 'Z'
        
        return {
            'title': title,
            'description': description,
            'url': url,
            'guid': guid,
            'date_published': date_published,
            'date_modified': date_modified,
            'pub_date_rfc822': pub_date_rfc822,
            'mod_date_rfc3339': mod_date_rfc3339,
            'og_image': og_image,
            'keywords': keywords,
            'section': section,
            'slug': slug,
        }
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None

def get_blog_posts():
    """Get all English blog posts (non-localized)."""
    posts = []
    for filepath in BLOG_DIR.glob('*.html'):
        # Skip localized versions (those with -xx.html suffix or xx- prefix)
        if re.match(r'.+-[a-z]{2}\.html$', filepath.name):
            continue
        if re.match(r'^[a-z]{2}-.+\.html$', filepath.name):
            continue
        # Skip paginated index pages
        if filepath.name.startswith('page') or filepath.name == 'index.html':
            continue
        # Skip language-specific index files
        if re.match(r'index-[a-z]{2}\.html$', filepath.name):
            continue
            
        post = parse_blog_post(filepath)
        if post:
            posts.append(post)
    
    # Sort by date published descending
    posts.sort(key=lambda x: x['date_published'], reverse=True)
    return posts

def generate_rss(posts):
    """Generate RSS 2.0 feed."""
    rss_items = []
    for post in posts:
        item = f'''    <item>
      <title><![CDATA[{post['title']}]]></title>
      <link>{post['url']}</link>
      <guid isPermaLink="true">{post['guid']}</guid>
      <pubDate>{post['pub_date_rfc822']}</pubDate>
      <description><![CDATA[{post['description']}]]></description>
      <category>{post['section']}</category>
      <enclosure url="{post['og_image']}" type="image/png" length="0"/>
    </item>'''
        rss_items.append(item)
    
    rss = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:media="http://search.yahoo.com/mrss/">
  <channel>
    <title><![CDATA[{SITE_TITLE} Blog]]></title>
    <link>{SITE_URL}/blog</link>
    <description><![CDATA[{SITE_DESCRIPTION}]]></description>
    <language>en</language>
    <lastBuildDate>{formatdate(datetime.now().timestamp(), usegmt=True)}</lastBuildDate>
    <atom:link href="{SITE_URL}/feed.rss" rel="self" type="application/rss+xml"/>
    <image>
      <url>{OG_IMAGE_URL}</url>
      <title><![CDATA[{SITE_TITLE}]]></title>
      <link>{SITE_URL}</link>
      <width>1200</width>
      <height>630</height>
    </image>
    <managingEditor>{AUTHOR_NAME} ({AUTHOR_URL})</managingEditor>
    <webMaster>{AUTHOR_NAME} ({AUTHOR_URL})</webMaster>
    <copyright>Copyright {datetime.now().year} {SITE_TITLE}. All rights reserved.</copyright>
    <ttl>60</ttl>
{''.join(rss_items)}
  </channel>
</rss>'''
    return rss

def generate_atom(posts):
    """Generate Atom 1.0 feed."""
    atom_entries = []
    for post in posts:
        entry = f'''    <entry>
      <title type="html"><![CDATA[{post['title']}]]></title>
      <link href="{post['url']}" rel="alternate" type="text/html"/>
      <id>{post['guid']}</id>
      <updated>{post['mod_date_rfc3339']}</updated>
      <published>{post['date_published']}T00:00:00Z</published>
      <summary type="html"><![CDATA[{post['description']}]]></summary>
      <category term="{post['section']}"/>
      <author>
        <name>{AUTHOR_NAME}</name>
        <uri>{AUTHOR_URL}</uri>
      </author>
      <content type="html"><![CDATA[{post['description']}]]></content>
      <link href="{post['og_image']}" rel="enclosure" type="image/png" length="0"/>
    </entry>'''
        atom_entries.append(entry)
    
    atom = f'''<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title type="html"><![CDATA[{SITE_TITLE} Blog]]></title>
  <link href="{SITE_URL}/blog" rel="alternate" type="text/html"/>
  <link href="{SITE_URL}/feed.atom" rel="self" type="application/atom+xml"/>
  <id>{SITE_URL}/blog</id>
  <updated>{datetime.now().isoformat()}Z</updated>
  <subtitle type="html"><![CDATA[{SITE_DESCRIPTION}]]></subtitle>
  <rights>Copyright {datetime.now().year} {SITE_TITLE}. All rights reserved.</rights>
  <author>
    <name>{AUTHOR_NAME}</name>
    <uri>{AUTHOR_URL}</uri>
  </author>
  <logo>{OG_IMAGE_URL}</logo>
  <icon>{SITE_URL}/favicon.svg</icon>
{''.join(atom_entries)}
</feed>'''
    return atom

def generate_json_feed(posts):
    """Generate JSON Feed 1.1."""
    items = []
    for post in posts:
        item = {
            "id": post['guid'],
            "url": post['url'],
            "title": post['title'],
            "content_html": f"<p>{post['description']}</p>",
            "summary": post['description'],
            "date_published": post['date_published'] + "T00:00:00Z",
            "date_modified": post['mod_date_rfc3339'],
            "authors": [{"name": AUTHOR_NAME, "url": AUTHOR_URL}],
            "tags": [post['section']] + [k.strip() for k in post['keywords'].split(',') if k.strip()],
            "image": post['og_image'],
            "_meta": {
                "section": post['section'],
                "slug": post['slug']
            }
        }
        items.append(item)
    
    feed = {
        "version": "https://jsonfeed.org/version/1.1",
        "title": f"{SITE_TITLE} Blog",
        "home_page_url": f"{SITE_URL}/blog",
        "feed_url": f"{SITE_URL}/feed.json",
        "description": SITE_DESCRIPTION,
        "language": "en",
        "icon": f"{SITE_URL}/favicon.svg",
        "favicon": f"{SITE_URL}/favicon.svg",
        "authors": [{"name": AUTHOR_NAME, "url": AUTHOR_URL}],
        "items": items
    }
    
    return json.dumps(feed, indent=2, ensure_ascii=False)

def main():
    posts = get_blog_posts()
    print(f"Found {len(posts)} blog posts")
    
    # Generate feeds
    rss = generate_rss(posts)
    atom = generate_atom(posts)
    json_feed = generate_json_feed(posts)
    
    # Write files
    (BASE / 'feed.rss').write_text(rss, encoding='utf-8')
    print("Created feed.rss")
    
    (BASE / 'feed.atom').write_text(atom, encoding='utf-8')
    print("Created feed.atom")
    
    (BASE / 'feed.json').write_text(json_feed, encoding='utf-8')
    print("Created feed.json")
    
    # Also add feed links to index.html if not present
    index_path = BASE / 'index.html'
    if index_path.exists():
        html = index_path.read_text(encoding='utf-8')
        if 'feed.rss' not in html:
            # Add feed links in head
            feed_links = '''    <link rel="alternate" type="application/rss+xml" title="World Time Sync Blog RSS" href="/feed.rss">
    <link rel="alternate" type="application/atom+xml" title="World Time Sync Blog Atom" href="/feed.atom">
    <link rel="alternate" type="application/json" title="World Time Sync Blog JSON Feed" href="/feed.json">'''
            html = html.replace('</head>', f'{feed_links}\n</head>')
            index_path.write_text(html, encoding='utf-8')
            print("Added feed links to index.html")
    
    print("\nDone! Feeds available at:")
    print(f"  RSS: {SITE_URL}/feed.rss")
    print(f"  Atom: {SITE_URL}/feed.atom")
    print(f"  JSON: {SITE_URL}/feed.json")

if __name__ == '__main__':
    main()