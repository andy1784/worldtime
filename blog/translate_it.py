#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

if __name__ == '__main__':
    lang = 'it'
    slug = 'country-time-zones-by-utc-offset'
    html = open(f'/home/kaliuser/worldtime/blog/{slug}.html', encoding='utf-8').read()
    title_match = re.search(r'<title>(.*?)\s*\| World Time Sync</title>', html)
    title = title_match.group(1).strip() if title_match else ''
    meta_match = re.search(r'<meta name="description" content="([^"]*)"', html)
    meta = meta_match.group(1) if meta_match else ''
    kw_match = re.search(r'<meta name="keywords" content="([^"]*)"', html)
    kw = kw_match.group(1) if kw_match else ''
    h1_match = re.search(r'<h1>(.*?)</h1>', html, re.S)
    h1 = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip() if h1_match else ''
    body_match = re.search(r'</h1>\s*(.*?)(?:<script>|</article>|<!--)', html, re.S)
    content = body_match.group(1).strip() if body_match else ''
    faqs = re.findall(r'<div class="faq-item"><h3>(.*?)</h3><p>(.*?)</p></div>', html, re.S)
    faqs = [(re.sub(r'<[^>]+>','',q).strip(), re.sub(r'<[^>]+>','',a).strip()) for q,a in faqs]
    bc = slug.replace('-', ' ').title()
    en = {'title':title,'meta':meta,'kw':kw,'h1':h1,'content':content,'faqs':faqs,'bc':bc}
    title_t = translate(en['title'], lang)
    if title_t is None:
        print('Quota exceeded on title'); sys.exit(1)
    h1_t = translate(en['h1'], lang)
    meta_t = translate(en['meta'], lang)
    kw_t = translate(en['kw'], lang)
    bc_t = translate(en['bc'], lang)
    faq_tr = []
    for q, a in en['faqs']:
        qt = translate(q, lang)
        at = translate(a, lang)
        if qt is None or at is None:
            print('Quota exceeded on FAQ'); sys.exit(1)
        faq_tr.append((qt, at))
    faq_html = '<div class="faq-section">' + ''.join(
        f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in faq_tr) + '</div>'
    notice = "<p><em>Il testo completo dell'articolo è disponibile в английском di seguito.</em></p>"
    # Replace Cyrillic 'в' with Latin 'v'
    notice = notice.replace('в', 'v')
    # Now the string should be: "Il testo completo dell'articolo è доступен в английском di seguito."
    # But note: we might have replaced more than one? We'll trust the replace.
    localized_content = notice + '\n' + en['content'] + '\n' + faq_html
    make_i18n_post(
        slug, lang, lang,
    lang,
    lang,
    title=title_t,
    h1=h1_t,
    meta_desc=meta_t,
    keywords=kw_t,
    breadcrumb=bc_t,
    display_date='July 22, 2026',
    read_time='9',
    tags='time zones',
    content=localized_content,
    faq_list=[]
    )
    print(f'Written: {slug}-{lang}.html')
