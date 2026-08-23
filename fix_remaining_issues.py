#!/usr/bin/env python3
"""
Fix remaining SEO issues:
1. Add viewport meta to country stub pages
2. Fix meeting-planner.html og:image and duplicate ID
3. Fix og-image.html, widget-embed.html, google verification file
"""
import re
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')

def fix_country_stubs():
    """Add viewport meta to country stub pages"""
    fixed = 0
    for filepath in BASE.glob('country/*.html'):
        content = filepath.read_text(encoding='utf-8')
        if 'Redirecting' in content and 'viewport' not in content:
            # Add viewport meta after charset
            content = content.replace(
                '<meta charset="UTF-8" />',
                '<meta charset="UTF-8" />\n<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">'
            )
            filepath.write_text(content, encoding='utf-8')
            fixed += 1
            print(f"Fixed viewport: {filepath.name}")
    
    # Also check language subdirectories
    for lang in ['de', 'es', 'fr', 'it', 'ja', 'ru', 'uk', 'zh', 'ar', 'hi', 'pt']:
        lang_dir = BASE / lang / 'country'
        if lang_dir.exists():
            for filepath in lang_dir.glob('*.html'):
                content = filepath.read_text(encoding='utf-8')
                if 'Redirecting' in content and 'viewport' not in content:
                    content = content.replace(
                        '<meta charset="UTF-8" />',
                        '<meta charset="UTF-8" />\n<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">'
                    )
                    filepath.write_text(content, encoding='utf-8')
                    fixed += 1
                    print(f"Fixed viewport: {filepath.relative_to(BASE)}")
    
    print(f"Total country stubs fixed: {fixed}")

def fix_meeting_planner():
    """Fix meeting-planner.html"""
    filepath = BASE / 'meeting-planner.html'
    content = filepath.read_text(encoding='utf-8')
    
    # Add og:image if missing
    if 'og:image' not in content:
        content = content.replace(
            '<meta property="og:title"',
            '<meta property="og:image" content="https://worldtimessync.com/og-image.png">\n    <meta property="og:image:width" content="1200">\n    <meta property="og:image:height" content="630">\n    <meta property="og:title"'
        )
    
    # The duplicate ID "' + c.id + '" is in a JS template string - can't easily fix in static HTML
    # This is a React template that gets compiled - the ID is a template literal
    # We'll note it but not change it since it's in JS template context
    
    filepath.write_text(content, encoding='utf-8')
    print("Fixed meeting-planner.html")

def fix_special_pages():
    """Fix og-image.html, widget-embed.html"""
    
    # og-image.html
    filepath = BASE / 'og-image.html'
    if filepath.exists():
        content = filepath.read_text(encoding='utf-8')
        # Add basic HTML structure
        if '<title>' not in content:
            new_content = f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>World Time Sync - Social Image</title>
    <link rel="canonical" href="https://worldtimessync.com/og-image.png">
    <meta property="og:image" content="https://worldtimessync.com/og-image.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
</head>
<body>
    <img src="/og-image.png" alt="World Time Sync" width="1200" height="630" />
</body>
</html>'''
            filepath.write_text(new_content, encoding='utf-8')
            print("Fixed og-image.html")
    
    # widget-embed.html
    filepath = BASE / 'widget-embed.html'
    if filepath.exists():
        content = filepath.read_text(encoding='utf-8')
        if '<title>' not in content:
            # Add minimal HTML structure
            new_content = f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <meta name="theme-color" content="#667eea">
    <title>World Time Sync Widget Embed</title>
    <meta name="description" content="Embeddable World Time Sync widget">
    <meta name="robots" content="noindex, follow">
    <link rel="canonical" href="https://worldtimessync.com/widget-embed">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://worldtimessync.com/widget-embed">
    <meta property="og:title" content="World Time Sync Widget Embed">
    <meta property="og:image" content="https://worldtimessync.com/og-image.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:description" content="Embeddable World Time Sync widget">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="World Time Sync Widget Embed">
    <meta name="twitter:image" content="https://worldtimessync.com/og-image.png">
    <meta name="twitter:creator" content="@worldtimesync">
    <meta name="twitter:site" content="@worldtimesync">
    <link rel="canonical" href="https://worldtimessync.com/widget-embed">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="preconnect" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://pagead2.googlesyndication.com">
    <link rel="dns-prefetch" href="https://www.googlesyndication.com">
</head>
<body>
{content}
</body>
</html>'''
            filepath.write_text(new_content, encoding='utf-8')
            print("Fixed widget-embed.html")
    
    # google verification file - just leave as is, it's for search console only

def fix_google_verification():
    """Google verification file should stay minimal"""
    filepath = BASE / 'google1926a28424a66c9d.html'
    if filepath.exists():
        content = filepath.read_text(encoding='utf-8')
        if '<title>' not in content:
            new_content = '''google-site-verification: google1926a28424a66c9d.html'''
            filepath.write_text(new_content, encoding='utf-8')
            print("Fixed google verification file")

def main():
    fix_country_stubs()
    fix_meeting_planner()
    fix_special_pages()
    fix_google_verification()
    print("\nDone!")

if __name__ == '__main__':
    main()