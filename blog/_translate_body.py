#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Full body translation for already-localized posts (replace EN body with translated).
Translates text inside HTML tags (p, h2, h3, li, td, th, strong, em) keeping structure.
Usage: python3 _translate_body.py <lang> <slug1> <slug2> ...
"""
import sys, re, json, time, urllib.parse, urllib.request, os
sys.path.insert(0, '/home/kaliuser/worldtime/blog')
from _gen_i18n import make_i18n_post

CACHE = '/tmp/translate_cache.json'
try:
    cache = json.load(open(CACHE, encoding='utf-8'))
except Exception:
    cache = {}

def translate(text, target):
    if not text or not text.strip():
        return text
    key = f'{target}:{text}'
    if key in cache:
        return cache[key]
    q = urllib.parse.quote(text)
    url = f'https://api.mymemory.translated.net/get?q={q}&langpair=en|{target}'
    for _ in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            resp = urllib.request.urlopen(req, timeout=20).read().decode('utf-8')
            data = json.loads(resp)
            t = data.get('responseData', {}).get('translatedText', '')
            if t and t != text:
                cache[key] = t
                json.dump(cache, open(CACHE, 'w'), ensure_ascii=False)
                return t
            if data.get('quotaFinished'):
                return None
        except Exception:
            time.sleep(2)
    return None

LANG_CODE = {'ru':'ru','es':'es','zh':'zh','ja':'ja','fr':'fr','de':'de','uk':'uk'}

def translate_html_content(html, lang):
    """Translate visible text inside block tags, keep tags."""
    # pattern: opening tag + text + closing tag for common block elements
    def repl(m):
        tag = m.group(1)
        inner = re.sub(r'<[^>]+>', '', m.group(0))
        if not inner.strip():
            return m.group(0)
        tr = translate(inner, lang)
        if tr is None:
            raise RuntimeError('QUOTA')
        # rebuild: opening tag + translated text + closing tag
        # extract opening tag string
        open_tag = m.group(0)[:m.group(0).find('>')+1]
        close_tag = m.group(0)[m.group(0).rfind('<'):]
        return open_tag + tr + close_tag
    # translate p, h2, h3, li, td, th, strong, em, a (text only)
    out = re.sub(r'<(p|h2|h3|li|td|th|strong|em)[^>]*>.*?</\1>', repl, html, flags=re.S)
    return out

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 _translate_body.py <lang> <slug> ..."); sys.exit(1)
    lang = sys.argv[1]
    if lang not in LANG_CODE:
        print("Bad lang"); sys.exit(1)
    slugs = sys.argv[2:]
    for slug in slugs:
        path = f'/home/kaliuser/worldtime/blog/{slug}-{lang}.html'
        if not os.path.exists(path):
            print(f'SKIP (no {lang} file): {slug}'); continue
        html = open(path, encoding='utf-8').read()
        # extract current localized meta
        title = re.search(r'<title>(.*?)</title>', html)
        title = title.group(1) if title else ''
        meta = re.search(r'<meta name="description" content="([^"]*)"', html)
        meta = meta.group(1) if meta else ''
        kw = re.search(r'<meta name="keywords" content="([^"]*)"', html)
        kw = kw.group(1) if kw else ''
        h1 = re.search(r'<h1>(.*?)</h1>', html, re.S)
        h1 = re.sub(r'<[^>]+>','',h1.group(1)).strip() if h1 else ''
        bc = re.search(r'"@type": "ListItem".*?"name": "(.*?)"', html)
        bc = bc.group(1) if bc else slug.replace('-',' ').title()
        # extract existing localized content (between h1 and footer/script)
        body = re.search(r'</h1>\s*(.*?)(?:<footer|</article>|<script)', html, re.S)
        content = body.group(1).strip() if body else ''
        # remove the "notice" paragraph (EN notice) before translating
        content = re.sub(r'<p><em>[^<]*</em></p>\s*', '', content)
        try:
            translated = translate_html_content(content, lang)
        except RuntimeError:
            print(f'  QUOTA on {slug} body — stop.'); break
        make_i18n_post(
            slug, lang, LANG_CODE[lang],
            title=title, h1=h1, meta_desc=meta, keywords=kw,
            breadcrumb=bc, display_date='July 16, 2026', read_time='6',
            tags='time zones', content=translated, faq_list=[]
        )
        print(f'  body translated: {slug}-{lang}')
    print('Done.')
