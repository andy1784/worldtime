#!/usr/bin/env python3
"""Create the missing blog post for Dubai-London time difference"""
import os
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')
BLOG_DIR = BASE / 'blog'
TEMPLATE = BLOG_DIR / 'how-to-convert-time-zones.html'

# Read template
template_content = TEMPLATE.read_text(encoding='utf-8')

post = {
    'slug': 'time-difference-dubai-london.html',
    'title': 'Time Difference Between Dubai and London: Guide & Converter (2026)',
    'meta_desc': 'Find out the current time difference between Dubai (GST) and London (GMT/BST). Our guide includes conversion table, DST info for London, and Dubai-London time zone converter for easy time zone math.',
    'keywords': 'time difference Dubai London, Dubai to London time, GST to GMT conversion, Dubai London time zone difference',
}

# Start with template
content = template_content

# Replace title tag
content = content.replace(
    '<title>How to Convert Time Zones: The Complete Guide (2026) | World Time Sync</title>',
    f'<title>{post["title"]} | World Time Sync</title>'
)
# Replace meta title
content = content.replace(
    '<meta name="title" content="How to Convert Time Zones: The Complete Guide (2026) | World Time Sync">',
    f'<meta name="title" content="{post["title"]} | World Time Sync">'
)
# Replace meta description
content = content.replace(
    '<meta name="description" content="Learn how to convert time zones manually and with tools. Step-by-step guide with examples, DST handling, and common mistakes.">',
    f'<meta name="description" content="{post["meta_desc"]}">'
)
# Replace meta keywords
content = content.replace(
    '<meta name="keywords" content="how to convert time zones, time zone conversion, convert time, time zone calculator, time zone math">',
    f'<meta name="keywords" content="{post["keywords"]}">'
)
# Replace og:title
content = content.replace(
    '<meta property="og:title" content="How to Convert Time Zones: The Complete Guide (2026) | World Time Sync">',
    f'<meta property="og:title" content="{post["title"]} | World Time Sync">'
)
# Replace og:description
content = content.replace(
    '<meta property="og:description" content="Learn how to convert time zones manually and with tools. Step-by-step guide with examples, DST handling, and common mistakes.">',
    f'<meta property="og:description" content="{post["meta_desc"]}">'
)
# Replace twitter:title
content = content.replace(
    '<meta name="twitter:title" content="How to Convert Time Zones: The Complete Guide (2026) | World Time Sync">',
    f'<meta name="twitter:title" content="{post["title"]} | World Time Sync">'
)
# Replace canonical URL
content = content.replace(
    '<link rel="canonical" href="https://worldtimessync.com/blog/how-to-convert-time-zones.html">',
    f'<link rel="canonical" href="https://worldtimessync.com/blog/{post["slug"]}">'
)

# Replace JSON-LD BlogPosting headline and description
old_headline = '"headline": "How to Convert Time Zones: The Complete Guide (2026) | World Time Sync"'
new_headline = f'"headline": "{post["title"]} | World Time Sync"'
content = content.replace(old_headline, new_headline)

old_description = '"description": "Learn how to convert time zones manually and with tools. Step-by-step guide with examples, DST handling, and common mistakes."'
new_description = f'"description": "{post["meta_desc"]}"'
content = content.replace(old_description, new_description)

# Replace JSON-LD BreadcrumbList: third item name and item
title_part = post["title"].split("|")[0].strip()
old_breadcrumb_name = '"name": "How to Convert Time Zones"'
new_breadcrumb_name = f'"name": "{title_part}"'
content = content.replace(old_breadcrumb_name, new_breadcrumb_name)

old_breadcrumb_item = '"item": "https://worldtimessync.com/blog/how-to-convert-time-zones.html"'
new_breadcrumb_item = f'"item": "https://worldtimessync.com/blog/{post["slug"]}"'
content = content.replace(old_breadcrumb_item, new_breadcrumb_item)

# Write file
with open(BLOG_DIR / post['slug'], 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Created {post['slug']}")