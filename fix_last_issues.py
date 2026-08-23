#!/usr/bin/env python3
"""
Fix remaining issues:
1. embed.html - duplicate ID in example code (just example snippets)
2. google verification file
3. meeting-planner.html og:image
4. es/meeting-planner.html viewport
5. blog/page/1/index.html viewport
"""
import re
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')

def fix_google_verification():
    """Google verification file"""
    filepath = BASE / 'google1926a28424a66c9d.html'
    if filepath.exists():
        content = '''google-site-verification: google1926a28424a66c9d.html'''
        filepath.write_text(content, encoding='utf-8')
        print("Fixed google verification file")

def fix_meeting_planner():
    """Add og:image to meeting-planner.html"""
    filepath = BASE / 'meeting-planner.html'
    content = filepath.read_text(encoding='utf-8')
    
    if 'og:image' not in content:
        content = content.replace(
            '<meta property="og:title"',
            '<meta property="og:image" content="https://worldtimessync.com/og-image.png">\n    <meta property="og:image:width" content="1200">\n    <meta property="og:image:height" content="630">\n    <meta property="og:title"'
        )
        filepath.write_text(content, encoding='utf-8')
        print("Fixed meeting-planner.html og:image")
    
    # The duplicate ID "' + c.id + '" is in JS template - can't fix in static HTML

def fix_es_meeting_planner():
    """Add viewport to es/meeting-planner.html"""
    filepath = BASE / 'es' / 'meeting-planner.html'
    if filepath.exists():
        content = filepath.read_text(encoding='utf-8')
        if 'viewport' not in content:
            content = content.replace(
                '<meta charset="UTF-8">',
                '<meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">'
            )
            filepath.write_text(content, encoding='utf-8')
            print("Fixed es/meeting-planner.html viewport")

def fix_blog_page_1():
    """Add viewport to blog/page/1/index.html"""
    filepath = BASE / 'blog' / 'page' / '1' / 'index.html'
    if filepath.exists():
        content = filepath.read_text(encoding='utf-8')
        if 'viewport' not in content:
            content = content.replace(
                '<meta charset="UTF-8">',
                '<meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">'
            )
            filepath.write_text(content, encoding='utf-8')
            print("Fixed blog/page/1/index.html viewport")

def fix_embed_html():
    """The duplicate ID in embed.html is in example code snippets showing how to use the widget.
    This is intentional example code - the same ID is shown in multiple embed examples.
    We can't really "fix" this without changing the documentation.
    We'll leave it as is - it's documentation, not actual duplicate elements on one page.
    """
    pass

def main():
    fix_google_verification()
    fix_meeting_planner()
    fix_es_meeting_planner()
    fix_blog_page_1()
    print("Done!")

if __name__ == '__main__':
    main()