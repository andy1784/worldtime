#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re, json, time, urllib.parse, urllib.request, os
sys.path.insert(0, '/home/kaliuser/worldtime/blog')
from _gen_i18n import make_i18n_post

def translate_text(text, target):
    if not text or not text.strip():
        return text
    key = f'{target}:{text}'
    url = f'https://api.mymemory.translated.net/get?q={urllib.parse.quote(text)}&langpair=en|{target}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        data = json.loads(resp)
        t = data.get('responseData', {}).get('translatedText', '')
        if t and t != text:
            return t
        if data.get('quotaFinished'):
            return None
    except Exception as e:
        print(f'Translation error: {e}')
    return None

if __name__ == '__main__':
    lang = 'it'
    slug = 'country-time-zones-by-utc-offset'
    html = open(f'/home/kaliuser/worldtime/blog/{slug}.html', encoding='utf-8').read()
    # Extract title
    title_match = re.search(r'<title>(.*?)\s*\| World Time Sync</title>', html)
    title = title_match.group(1).strip() if title_match else ''
    # Extract meta description
    meta_match = re.search(r'<meta name="description" content="([^"]*)"', html)
    meta = meta_match.group(1) if meta_match else ''
    # Extract keywords
    kw_match = re.search(r'<meta name="keywords" content="([^"]*)"', html)
    kw = kw_match.group(1) if kw_match else ''
    # Extract h1
    h1_match = re.search(r'<h1>(.*?)</h1>', html, re.S)
    h1 = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip() if h1_match else ''
    # Extract content (from after h1 until <script> or </article> or <!--)
    body_match = re.search(r'</h1>\s*(.*?)(?:<script>|</article>|<!--)', html, re.S)
    content = body_match.group(1).strip() if body_match else ''
    # Extract FAQs
    faqs = re.findall(r'<div class="faq-item"><h3>(.*?)</h3><p>(.*?)</p></div>', html, re.S)
    faqs = [(re.sub(r'<[^>]+>','',q).strip(), re.sub(r'<[^>]+>','',a).strip()) for q,a in faqs]
    # Breadcrumb
    bc = slug.replace('-', ' ').title()
    print(f'English title: {title}')
    print(f'English meta: {meta}')
    print(f'English h1: {h1}')
    print(f'English kw: {kw}')
    print(f'English bc: {bc}')
    print(f'Number of FAQs: {len(faqs)}')
    # Translate each component
    title_it = translate_text(title, lang)
    if title_it is None:
        print('Failed to translate title (quota?)'); sys.exit(1)
    meta_it = translate_text(meta, lang)
    if meta_it is None:
        print('Failed to translate meta (quota?)'); sys.exit(1)
    kw_it = translate_text(kw, lang)
    if kw_it is None:
        print('Failed to translate keywords (quota?)'); sys.exit(1)
    h1_it = translate_text(h1, lang)
    if h1_it is None:
        print('Failed to translate h1 (quota?)'); sys.exit(1)
    bc_it = translate_text(bc, lang)
    if bc_it is None:
        print('Failed to translate breadcrumb (quota?)'); sys.exit(1)
    faqs_it = []
    for q, a in faqs:
        qt = translate_text(q, lang)
        at = translate_text(a, lang)
        if qt is None or at is None:
            print('Failed to translate FAQ (quota?)'); sys.exit(1)
        faqs_it.append((qt, at))
    # Build notice in Italian
    notice = '<p><em>Il testo completo dell\'articolo è disponibile in inglese di seguito.</em></p>'
    # Build FAQ HTML
    faq_html = '<div class="faq-section">' + ''.join(
        f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in faqs_it) + '</div>'
    # Combine content: notice + original English content + faq_html
    # Note: The original content is in English, as per the design (body stays in English with notice)
    localized_content = notice + '\n' + content + '\n' + faq_html
    # Generate the localized file
    make_i18n_post(
        slug, lang, lang,
        title=title_it, h1=h1_it, meta_desc=meta_it, keywords=kw_it,
        breadcrumb=bc_it, display_date='July 22, 2026', read_time='9',
        tags='time zones', content=localized_content, faq_list=[]
    )
    print(f'Successfully created {slug}-{lang}.html')
