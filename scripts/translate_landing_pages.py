#!/usr/bin/env python3
"""Translate world-clock.html and time-zone-converter.html to 11 languages."""
import json, sys, os, re, time, urllib.request, urllib.error
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')
auth = json.load(open('/home/kaliuser/.hermes/auth.json'))
TOK = None
for t in auth['credential_pool'].get('alibaba', []):
    if t.get('access_token','').startswith('sk-or'):
        TOK = t['access_token']; break
assert TOK, "no openrouter token"
MODEL = "meta-llama/llama-3.2-3b-instruct:free"

LANGS = {
    'es': 'Spanish', 'zh': 'Chinese (Simplified)', 'ru': 'Russian',
    'it': 'Italian', 'de': 'German', 'ja': 'Japanese', 'fr': 'French', 'uk': 'Ukrainian',
    'hi': 'Hindi', 'ar': 'Arabic', 'pt': 'Portuguese',
}

RTL_LANGS = {'ar', 'he'}

SOURCE_PAGES = ['world-clock.html', 'time-zone-converter.html']

def translate_html(html, target_lang_name):
    system = (
        f"You are a professional translator. Translate all visible/user-facing text in the "
        f"following HTML document into {target_lang_name}. Rules: (1) Keep ALL HTML tags, "
        f"attributes, href/lang values, JSON-LD blocks, and CSS exactly as-is. "
        f"(2) Translate only human-readable text inside tags and attributes like title/alt/aria-label/description/keywords/content. "
        f"(3) Do NOT translate URLs, city/feature names that are proper nouns unless a natural localized form exists, "
        f"UTC offsets, IANA timezone IDs, or code. (4) Output ONLY the full translated HTML, no commentary, no markdown fences."
    )
    body = {
        "model": MODEL,
        "messages": [
            {"role":"system","content": system},
            {"role":"user","content": html},
        ],
        "temperature": 0.15,
        "max_tokens": 8000,
    }
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Authorization":f"Bearer {TOK}","Content-Type":"application/json"})
    backoff = 8
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                resp = json.load(r)
            return resp['choices'][0]['message']['content']
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(backoff); backoff = min(backoff*2, 60); continue
            if e.code == 402:
                raise RuntimeError("OpenRouter credits exhausted (402 Payment Required)")
            raise
        except Exception:
            time.sleep(backoff); backoff = min(backoff*2, 60)
    raise RuntimeError("translate failed after retries")

def localize_urls(html, lang, src_rel, dst_rel):
    """Update internal URLs to point to localized versions."""
    html = re.sub(r'https?://worldtimessync\\.com/' + re.escape(src_rel),
                  'https://worldtimessync.com/' + dst_rel, html)
    html = re.sub(r'<html lang="en">', f'<html lang="{lang}">', html)
    if lang in RTL_LANGS:
        html = re.sub(r'<html lang="[^"]*">', f'<html lang="{lang}" dir="rtl">', html)
    return html

def fix_jsonld_context(html):
    """Fix the @context placeholder bug in JSON-LD."""
    return html.replace('https://***@type', 'https://schema.org\",\"@type')

def add_hreflang_block(html, lang, page_slug):
    """Add hreflang alternate links before </head>."""
    # Build hreflang links
    base_url = f"https://worldtimessync.com/{page_slug}"
    links = [
        f'<link rel="alternate" hreflang="x-default" href="{base_url}" />',
        f'<link rel="alternate" hreflang="en" href="{base_url}" />',
    ]
    for lcode, lname in LANGS.items():
        if lcode == 'en': continue
        links.append(f'<link rel="alternate" hreflang="{lcode}" href="https://worldtimessync.com/{lcode}/{page_slug}" />')
    # Also add hi, ar, pt which are in LANGS but not in the old LANGS dict
    for lcode in ['hi', 'ar', 'pt']:
        if lcode not in LANGS: continue
        links.append(f'<link rel="alternate" hreflang="{lcode}" href="https://worldtimessync.com/{lcode}/{page_slug}" />')
    
    hreflang_html = '\n    '.join(links) + '\n'
    # Insert before </head>
    html = html.replace('</head>', f'    {hreflang_html}</head>')
    return html

def translate_page(page_name, lang, workers=3):
    src = BASE / page_name
    dst_dir = BASE / lang
    dst = dst_dir / page_name
    
    if dst.exists():
        return f"skip {page_name} ({lang})"
    
    html = src.read_text(encoding='utf-8')
    src_rel = page_name
    dst_rel = f"{lang}/{page_name}"
    
    html = localize_urls(html, lang, src_rel, dst_rel)
    html = fix_jsonld_context(html)
    
    # Translate
    out = translate_html(html, LANGS[lang])
    
    # Fix any context issues introduced by translation
    out = fix_jsonld_context(out)
    
    # Add hreflang block
    out = add_hreflang_block(out, lang, page_name)
    
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst.write_text(out, encoding='utf-8')
    return f"ok {page_name} ({lang})"

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('lang', nargs='?', help='Single language to process')
    parser.add_argument('--workers', type=int, default=3)
    parser.add_argument('--all', action='store_true', help='Process all languages')
    args = parser.parse_args()
    
    if args.lang:
        langs = [args.lang]
    elif args.all:
        langs = list(LANGS.keys())
    else:
        print("Usage: python3 translate_landing_pages.py <lang> [--workers N]  OR  --all")
        sys.exit(1)
    
    for lang in langs:
        if lang not in LANGS:
            print(f"Unknown lang: {lang}")
            continue
        print(f"\n=== Processing {lang} ({LANGS[lang]}) ===")
        for page in SOURCE_PAGES:
            try:
                result = translate_page(page, lang, workers=args.workers)
                print(f"  {result}")
            except Exception as e:
                import traceback
                open('/tmp/gen_fail.log','a').write(f"[{lang}] {page}: {repr(e)}\n{traceback.format_exc()}\n")
                print(f"  FAIL {page} ({lang}): {e}")

if __name__ == '__main__':
    main()