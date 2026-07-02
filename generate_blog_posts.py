#!/usr/bin/env python3
"""Generate 10 SEO blog posts for time zone conversion cluster by replacing template"""
import os
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')
BLOG_DIR = BASE / 'blog'
TEMPLATE = BLOG_DIR / 'how-to-convert-time-zones.html'

# Read template
try:
    template_content = TEMPLATE.read_text(encoding='utf-8')
except Exception as e:
    print(f"Error reading template: {e}")
    exit(1)

# Posts to create
POSTS = [
    {
        'slug': 'convert-est-to-pst.html',
        'title': 'Convert EST to PST: Time Difference & Conversion Guide (2026)',
        'meta_desc': 'Learn how to convert Eastern Standard Time (EST) to Pacific Standard Time (PST) with our step-by-step guide. Includes time difference chart, DST handling, and conversion formula.',
        'keywords': 'convert EST to PST, EST to PST time difference, Eastern to Pacific time, time zone converter EST PST',
    },
    {
        'slug': 'convert-pst-to-est.html',
        'title': 'Convert PST to EST: Time Difference & Conversion Guide (2026)',
        'meta_desc': 'Learn how to convert Pacific Standard Time (PST) to Eastern Standard Time (EST) with our step-by-step guide. Includes time difference chart, DST handling, and conversion formula.',
        'keywords': 'convert PST to EST, PST to EST time difference, Pacific to Eastern time, time zone converter PST EST',
    },
    {
        'slug': 'time-difference-london-tokyo.html',
        'title': 'Time Difference Between London and Tokyo: Current Offset & Guide (2026)',
        'meta_desc': 'Discover the current time difference between London (GMT/BST) and Tokyo (JST). Our guide includes conversion table, DST info, and interactive converter for London-Tokyo time zone conversion.',
        'keywords': 'time difference London Tokyo, London to Tokyo time, GMT to JST conversion, London Tokyo time zone difference',
    },
    {
        'slug': 'time-difference-new-york-london.html',
        'title': 'Time Difference Between New York and London: Guide & Converter (2026)',
        'meta_desc': 'Learn the current time difference between New York (EST/EDT) and London (GMT/BST). Includes conversion chart, DST schedules, and easy conversion formula for NY-London time zone math.',
        'keywords': 'time difference New York London, NY to London time, EST to GMT conversion, New York London time zone',
    },
    {
        'slug': 'time-difference-sydney-london.html',
        'title': 'Time Difference Between Sydney and London: Guide & Converter (2026)',
        'meta_desc': 'Find out the current time difference between Sydney (AEST/AEDT) and London (GMT/BST). Our guide includes conversion table, DST info for both hemispheres, and Sydney-London time zone converter.',
        'keywords': 'time difference Sydney London, Sydney to London time, AEST to GMT conversion, Sydney London time zone difference',
    },
    {
        'slug': 'convert-gmt-to-est.html',
        'title': 'Convert GMT to EST: Time Difference & Conversion Guide (2026)',
        'meta_desc': 'Learn how to convert Greenwich Mean Time (GMT) to Eastern Standard Time (EST) with our step-by-step guide. Includes time difference chart, DST handling, and conversion formula for GMT-EST time zone math.',
        'keywords': 'convert GMT to EST, GMT to EST time difference, Greenwich to Eastern time, GMT EST converter',
    },
    {
        'slug': 'convert-cst-to-est.html',
        'title': 'Convert CST to EST: Time Difference & Conversion Guide (2026)',
        'meta_desc': 'Learn how to convert Central Standard Time (CST) to Eastern Standard Time (EST) with our step-by-step guide. Includes time difference chart, DST handling, and conversion formula for CST-EST time zone math.',
        'keywords': 'convert CST to EST, CST to EST time difference, Central to Eastern time, CST EST converter',
    },
    {
        'slug': 'time-difference-los-angeles-sydney.html',
        'title': 'Time Difference Between Los Angeles and Sydney: Guide & Converter (2026)',
        'meta_desc': 'Discover the current time difference between Los Angeles (PST/PDT) and Sydney (AEST/AEDT). Our guide includes conversion table, DST schedules, and easy conversion formula for LA-Sydney time zone math.',
        'keywords': 'time difference Los Angeles Sydney, LA to Sydney time, PST to AEST conversion, Los Angeles Sydney time zone',
    },
    {
        'slug': 'convert-ist-to-est.html',
        'title': 'Convert IST to EST: Time Difference & Conversion Guide (2026)',
        'meta_desc': 'Learn how to convert Indian Standard Time (IST) to Eastern Standard Time (EST) with our step-by-step guide. Includes time difference chart (IST is UTC+5:35:30), DST handling, and conversion formula for IST-EST time zone math.',
        'keywords': 'convert IST to EST, IST to EST time difference, India to Eastern time, IST EST converter',
    },
    {
        'slug': 'time-difference-dot-5), DST handling, and conversion formula for IST-EST time zone math.',
        'keywords': 'convert IST to EST, IST to EST time difference, India to Eastern time, IST EST converter',
    },
    {
        'slug': 'time-difference-dubai-london.html',
        'title': 'Time Difference Between Dubai and London: Guide & Converter (2026)',
        'meta_desc': 'Find out the current time difference between Dubai (GST) and London (GMT/BST). Our guide includes conversion table, DST info for London, and Dubai-London time zone converter for easy time zone math.',
        'keywords': 'time difference Dubai London, Dubai to London time, GST to GMT conversion, Dubai London time zone difference',
    },
]

def escape_for_replace(text):
    # We are doing simple string replacement, so we just need to make sure we don't have overlapping patterns.
    # We'll assume the template has unique enough strings.
    return text

def main():
    created = 0
    for post in POSTS:
        filepath = BLOG_DIR / post['slug']
        if filepath.exists():
            print(f"  Skipping {post['slug']} - already exists")
            continue
        
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
        # We assume the title does not have a pipe, but if it does, we take the first part.
        # In our titles, we have a pipe before "| World Time Sync", so we split by "|" and take the first part.
        title_part = post["title"].split("|")[0].strip()
        old_breadcrumb_name = '"name": "How to Convert Time Zones"'
        new_breadcrumb_name = f'"name": "{title_part}"'
        content = content.replace(old_breadcrumb_name, new_breadcrumb_name)
        
        old_breadcrumb_item = '"item": "https://worldtimessync.com/blog/how-to-convert-time-zones.html"'
        new_breadcrumb_item = f'"item": "https://worldtimessync.com/blog/{post["slug"]}"'
        content = content.replace(old_breadcrumb_item, new_breadcrumb_item)
        
        # Write file
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Created {post['slug']}")
            created += 1
        except Exception as e:
            print(f"  Error writing {post['slug']}: {e}")
    
    print(f"\nCreated {created} new blog posts")

if __name__ == '__main__':
    main()