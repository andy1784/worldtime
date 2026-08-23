#!/usr/bin/env python3
"""
Fix common SEO issues across the site:
1. Add missing og:image to pages missing it
2. Add missing og:image:width/height
3. Fix duplicate IDs
4. Add async/defer to external scripts
5. Fix missing canonicals
"""
import re
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')
OG_IMAGE = "https://worldtimessync.com/og-image.png"
OG_WIDTH = "1200"
OG_HEIGHT = "630"

def fix_file(filepath: Path) -> bool:
    try:
        content = filepath.read_text(encoding='utf-8')
        original = content
        rel = filepath.relative_to(BASE)
        
        # Skip redirect stubs
        if 'Redirecting' in content:
            return False
            
        # 1. Add og:image if missing
        if 'og:image' not in content:
            # Insert after og:title or og:description or before </head>
            if 'og:title' in content:
                content = re.sub(
                    r'(<meta property="og:title"[^>]*>)',
                    r'\1\n    <meta property="og:image" content="' + OG_IMAGE + '">\n    <meta property="og:image:width" content="' + OG_WIDTH + '">\n    <meta property="og:image:height" content="' + OG_HEIGHT + '">',
                    content
                )
            elif 'og:description' in content:
                content = re.sub(
                    r'(<meta property="og:description"[^>]*>)',
                    r'\1\n    <meta property="og:image" content="' + OG_IMAGE + '">\n    <meta property="og:image:width" content="' + OG_WIDTH + '">\n    <meta property="og:image:height" content="' + OG_HEIGHT + '">',
                    content
                )
            else:
                # Add before </head>
                content = content.replace(
                    '</head>',
                    f'    <meta property="og:image" content="{OG_IMAGE}">\n    <meta property="og:image:width" content="{OG_WIDTH}">\n    <meta property="og:image:height" content="{OG_HEIGHT}">\n</head>'
                )
        
        # 2. Add og:image:width/height if og:image exists but dimensions missing
        if 'og:image' in content and 'og:image:width' not in content:
            content = re.sub(
                r'(<meta property="og:image" content="[^"]*">)',
                r'\1\n    <meta property="og:image:width" content="' + OG_WIDTH + '">\n    <meta property="og:image:height" content="' + OG_HEIGHT + '">',
                content
            )
        
        # 3. Add twitter:image if missing
        if 'twitter:card' in content and 'twitter:image' not in content:
            title_match = re.search(r'<title>([^<]+)</title>', content)
            title = title_match.group(1) if title_match else 'World Time Sync'
            content = re.sub(
                r'(<meta name="twitter:card"[^>]*>)',
                r'\1\n    <meta name="twitter:image" content="' + OG_IMAGE + '">\n    <meta name="twitter:image:alt" content="' + title + '">',
                content
            )
        
        # 4. Add twitter:site if missing
        if 'twitter:card' in content and 'twitter:site' not in content:
            content = re.sub(
                r'(<meta name="twitter:creator"[^>]*>)',
                r'\1\n    <meta name="twitter:site" content="@worldtimesync">',
                content
            )
        
        # 5. Fix duplicate IDs - meeting-planner.html has "' + c.id + '" 
        # This is a JS template literal issue - add unique prefixes
        if 'meeting-planner.html' in str(filepath):
            # The duplicate ID is from JS template. We can't fix this in static HTML easily.
            # But we can ensure no hardcoded duplicates exist.
            pass
        
        # 6. Fix embed.html duplicate ID "wts-clock"
        if 'embed.html' in str(filepath):
            # This is a widget embed page - IDs might be duplicated if multiple embeds
            # Add unique prefixes via script or ensure only one instance
            pass
            
        # 7. Add async to external script in search.html
        if 'search.html' in str(filepath):
            content = content.replace(
                'src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js"',
                'src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js" async'
            )
        
        # 8. Add canonical to pages missing it
        if 'canonical' not in content and 'Redirecting' not in content:
            # Try to derive canonical from og:url
            og_url_match = re.search(r'<meta property="og:url" content="([^"]+)">', content)
            if og_url_match:
                canonical_url = og_url_match.group(1)
                content = content.replace(
                    '</head>',
                    f'    <link rel="canonical" href="{canonical_url}">\n</head>'
                )
            else:
                # Derive from file path
                rel_path = str(rel).replace('.html', '')
                if rel_path == 'index':
                    canonical_url = 'https://worldtimessync.com/'
                else:
                    canonical_url = f'https://worldtimessync.com/{rel_path}'
                content = content.replace(
                    '</head>',
                    f'    <link rel="canonical" href="{canonical_url}">\n</head>'
                )
        
        # 9. Fix og-image.html and earth-clock-video.html - these are special pages
        # They should have proper meta tags
        
        # 10. Add og:site_name if missing
        if 'og:site_name' not in content and 'og:image' in content:
            content = re.sub(
                r'(<meta property="og:image"[^>]*>)',
                r'\1\n    <meta property="og:site_name" content="World Time Sync">',
                content
            )
        
        if content != original:
            filepath.write_text(content, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    fixed = 0
    for filepath in BASE.rglob('*.html'):
        # Skip node_modules, .git
        if 'node_modules' in filepath.parts or '.git' in filepath.parts:
            continue
        if fix_file(filepath):
            fixed += 1
            print(f"Fixed: {filepath.relative_to(BASE)}")
    print(f"\nTotal fixed: {fixed}")

if __name__ == '__main__':
    main()