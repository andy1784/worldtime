#!/usr/bin/env python3
"""
Add Article + BreadcrumbList schema to localized blog posts missing it.
"""
import re
import json
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')
BLOG_DIR = BASE / 'blog'

# Posts that need localized schema added
localized_posts = [
    'best-meeting-times-remote-teams',
    'daylight-saving-2026-prep',
    'schedule-online-classes-time-zones',
    'utc-everything-guide',
    'world-clock-desk-setup',
]

langs = ['de', 'es', 'fr', 'it', 'ja', 'ru', 'uk', 'zh']

# Title mapping for each post (from English version)
post_titles = {
    'best-meeting-times-remote-teams': 'Finding the Best Meeting Time for Remote Teams (2026) | World Time Sync',
    'daylight-saving-2026-prep': 'Daylight Saving Time 2026: Dates, Changes & Preparation Guide | World Time Sync',
    'schedule-online-classes-time-zones': 'How to Schedule Online Classes Across Time Zones | World Time Sync',
    'utc-everything-guide': 'UTC Time: Everything You Need to Know | World Time Sync',
    'world-clock-desk-setup': 'World Clock Desk Setup: Stay on Time Across Time Zones | World Time Sync',
}

# Description mapping
post_descriptions = {
    'best-meeting-times-remote-teams': 'A practical method for picking meeting times that a distributed team across several time zones can actually attend, without burning out one region.',
    'daylight-saving-2026-prep': 'Complete guide to DST 2026: when clocks change, which countries observe it, and how to prepare your schedule and devices.',
    'schedule-online-classes-time-zones': 'Step-by-step guide for educators to schedule live online classes that work for students across multiple time zones.',
    'utc-everything-guide': 'Comprehensive guide to UTC (Coordinated Universal Time): history, usage, conversion, and why it matters for global coordination.',
    'world-clock-desk-setup': 'How to set up a world clock on your desk for tracking multiple time zones — hardware, software, and workflow tips.',
}

# Keywords mapping
post_keywords = {
    'best-meeting-times-remote-teams': 'best meeting time remote team, distributed team meeting schedule, global team standup time, fair meeting times, time zone overlap',
    'daylight-saving-2026-prep': 'daylight saving time 2026, dst 2026 dates, when do clocks change 2026, dst preparation, time change 2026',
    'schedule-online-classes-time-zones': 'schedule online classes time zones, teach across time zones, global classroom scheduling, virtual class time zones',
    'utc-everything-guide': 'utc time, coordinated universal time, utc conversion, utc vs gmt, world time standard',
    'world-clock-desk-setup': 'world clock desk setup, multiple time zones desk, time zone clock hardware, global time tracking',
}

# Article section mapping
post_sections = {
    'best-meeting-times-remote-teams': 'Time Zones',
    'daylight-saving-2026-prep': 'Time Zones',
    'schedule-online-classes-time-zones': 'Education',
    'utc-everything-guide': 'Time Zones',
    'world-clock-desk-setup': 'Productivity',
}

# Time required mapping
post_time = {
    'best-meeting-times-remote-teams': 'PT6M',
    'daylight-saving-2026-prep': 'PT8M',
    'schedule-online-classes-time-zones': 'PT7M',
    'utc-everything-guide': 'PT10M',
    'world-clock-desk-setup': 'PT6M',
}

# Word count mapping (approximate)
post_wordcount = {
    'best-meeting-times-remote-teams': 486,
    'daylight-saving-2026-prep': 623,
    'schedule-online-classes-time-zones': 534,
    'utc-everything-guide': 789,
    'world-clock-desk-setup': 445,
}

# Language-specific names
lang_names = {
    'de': 'Deutsch',
    'es': 'Español',
    'fr': 'Français',
    'it': 'Italiano',
    'ja': '日本語',
    'ru': 'Русский',
    'uk': 'Українська',
    'zh': '中文',
}

def generate_article_schema(post_slug, lang):
    """Generate Article JSON-LD for a localized post."""
    base_slug = post_slug.replace(f'-{lang}', '')
    title = post_titles.get(base_slug, 'World Time Sync Blog Post')
    desc = post_descriptions.get(base_slug, '')
    keywords = post_keywords.get(base_slug, '')
    section = post_sections.get(base_slug, 'Time Zones')
    time_req = post_time.get(base_slug, 'PT6M')
    wordcount = post_wordcount.get(base_slug, 500)
    
    # Localized title
    if lang != 'en':
        title = f'{title} ({lang_names.get(lang, lang.upper())})'
    
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "articleSection": section,
        "keywords": keywords,
        "wordCount": wordcount,
        "timeRequired": time_req,
        "inLanguage": lang,
        "author": {
            "@type": "Organization",
            "name": "World Time Sync",
            "url": "https://worldtimessync.com"
        },
        "publisher": {
            "@type": "Organization",
            "name": "World Time Sync",
            "url": "https://worldtimessync.com",
            "logo": {
                "@type": "ImageObject",
                "url": "https://worldtimessync.com/logo.png",
                "width": 512,
                "height": 512
            }
        },
        "datePublished": "2026-06-28",
        "dateModified": "2026-06-28",
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"https://worldtimessync.com/blog/{post_slug}.html"
        },
        "image": "https://worldtimessync.com/og-image.png"
    }
    return json.dumps(schema, ensure_ascii=False, separators=(',', ':'))

def generate_breadcrumb_schema(post_slug, lang):
    """Generate BreadcrumbList JSON-LD for a localized post."""
    base_slug = post_slug.replace(f'-{lang}', '')
    title = post_titles.get(base_slug, 'Blog Post')
    
    if lang != 'en':
        title = f'{title} ({lang_names.get(lang, lang.upper())})'
    
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://worldtimessync.com/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Blog",
                "item": "https://worldtimessync.com/#blog"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": title,
                "item": f"https://worldtimessync.com/blog/{post_slug}.html"
            }
        ]
    }
    return json.dumps(schema, ensure_ascii=False, separators=(',', ':'))

def process_file(filepath: Path) -> bool:
    """Add schema to a localized blog post."""
    try:
        html = filepath.read_text(encoding='utf-8')
        
        # Check if already has Article schema
        if '"@type": "Article"' in html:
            print(f"  SKIP (has Article): {filepath.name}")
            return False
        
        # Extract post slug from filename
        post_slug = filepath.stem
        
        # Generate schemas
        article_json = generate_article_schema(post_slug, filepath.stem.split('-')[-1] if '-' in filepath.stem else 'en')
        breadcrumb_json = generate_breadcrumb_schema(post_slug, filepath.stem.split('-')[-1] if '-' in filepath.stem else 'en')
        
        # Build script tags
        article_script = f'<script type="application/ld+json">{article_json}</script>'
        breadcrumb_script = f'<script type="application/ld+json">{breadcrumb_json}</script>'
        
        # Insert after existing JSON-LD scripts (before </head>)
        insert_point = '</head>'
        new_scripts = f'\n    {article_script}\n    {breadcrumb_script}\n'
        
        if insert_point in html:
            new_html = html.replace(insert_point, new_scripts + insert_point)
        else:
            print(f"  ERROR: No </head> found in {filepath.name}")
            return False
        
        if new_html != html:
            filepath.write_text(new_html, encoding='utf-8')
            print(f"  UPDATED: {filepath.name}")
            return True
        else:
            print(f"  SKIP (no change): {filepath.name}")
            return False
            
    except Exception as e:
        print(f"  ERROR: {filepath.name} - {e}")
        return False

def main():
    updated = 0
    for post in localized_posts:
        for lang in langs:
            filename = f'{post}-{lang}.html'
            filepath = BLOG_DIR / filename
            if filepath.exists():
                if process_file(filepath):
                    updated += 1
            else:
                print(f"  NOT FOUND: {filename}")
    
    print(f"\nTotal updated: {updated}")

if __name__ == '__main__':
    main()