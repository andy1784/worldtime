#!/usr/bin/env python3
"""Fix og:url and other issues in blog posts"""
import re
from pathlib import Path

BLOG_DIR = Path('/home/kaliuser/worldtime/blog')

POSTS = [
    'convert-est-to-pst.html',
    'convert-pst-to-est.html',
    'time-difference-london-tokyo.html',
    'time-difference-new-york-london.html',
    'time-difference-sydney-london.html',
    'convert-gmt-to-est.html',
    'convert-cst-to-est.html',
    'time-difference-los-angeles-sydney.html',
    'convert-ist-to-est.html',
    'time-difference-dubai-london.html',
]

for slug in POSTS:
    filepath = BLOG_DIR / slug
    if not filepath.exists():
        continue
    
    content = filepath.read_text(encoding='utf-8')
    
    # Fix og:url
    correct_url = f"https://worldtimessync.com/blog/{slug}"
    
    # Replace og:url
    content = re.sub(
        r'<meta property="og:url" content="[^"]+">',
        f'<meta property="og:url" content="{correct_url}">',
        content
    )
    
    # Fix breadcrumb - it still has the template article title
    # Find the article block and fix the breadcrumb
    # This is harder, let's just regenerate properly
    # For now just fix the og:url
    
    filepath.write_text(content, encoding='utf-8')
    print(f"Fixed {slug}")

print("Done!")