#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate ALL missing EN posts into a target language via MyMemory (free).
Builds localized files via blog/_gen_i18n.make_i18n_post.
SEO+FAQ only (body stays EN with notice) to fit quota.
Cache in /tmp/translate_cache.json survives quota limits.
Usage: python3 _translate_all.py <lang>   (lang in ru es zh ja fr de uk)
"""
import sys, re, json, time, urllib.parse, urllib.request, os, glob
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

LANG_CODE = {'ru':'ru','es':'es','zh':'zh','ja':'ja','fr':'fr','de':'de','uk':'uk','it':'it'}
NOTICE = {
 'ru':'<p><em>Полный текст статьи доступен на английском языке ниже.</em></p>',
 'es':'<p><em>El texto completo del artículo está disponible en inglés a continuación.</em></p>',
 'zh':'<p><em>本文完整内容以下方英文版本提供。</em></p>',
 'ja':'<p><em>この記事の全文は以下の英語版でご覧いただけます。</em></p>',
 'fr':'<p><em>Le texte complet de l\'article est disponible en anglais ci-dessous.</em></p>',
 'de':'<p><em>Der vollständige Artikeltext ist unten auf Englisch verfügbar.</em></p>',
 'uk':'<p><em>Повний текст статті доступний англійською мовою нижче.</em></p>',
 'it':'<p><em>Il testo completo dell\'articolo è disponibile in inglese di seguito.</em></p>',
}

def get_all_en_slugs():
    slugs = []
    for f in sorted(glob.glob('/home/kaliuser/worldtime/blog/*.html')):
        base = os.path.basename(f)
        if re.search(r'-(ru|es|zh|ja|fr|de|uk|it)\.html$', base):
            continue
        slug = base.replace('.html', '')
        if slug in ('index', 'blog', 'blog-index'):  # skip index/list pages
            continue
        slugs.append(slug)
    return slugs

def extract(slug):
    html = open(f'/home/kaliuser/worldtime/blog/{slug}.html', encoding='utf-8').read()
    title = re.search(r'<title>(.*?)\s*\| World Time Sync</title>', html)
    title = title.group(1).strip() if title else ''
    meta = re.search(r'<meta name="description" content="([^"]*)"', html)
    meta = meta.group(1) if meta else ''
    kw = re.search(r'<meta name="keywords" content="([^"]*)"', html)
    kw = kw.group(1) if kw else ''
    h1 = re.search(r'<h1>(.*?)</h1>', html, re.S)
    h1 = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else ''
    body = re.search(r'</h1>\s*(.*?)(?:<script>|</article>|<!--)', html, re.S)
    content = body.group(1).strip() if body else ''
    faqs = re.findall(r'<div class="faq-item"><h3>(.*?)</h3><p>(.*?)</p></div>', html, re.S)
    faqs = [(re.sub(r'<[^>]+>','',q).strip(), re.sub(r'<[^>]+>','',a).strip()) for q,a in faqs]
    bc = slug.replace('-', ' ').title()
    return {'title':title,'meta':meta,'kw':kw,'h1':h1,'content':content,'faqs':faqs,'bc':bc}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 _translate_all.py <lang>"); sys.exit(1)
    lang = sys.argv[1]
    if lang not in LANG_CODE:
        print("Bad lang", lang); sys.exit(1)
    slugs = get_all_en_slugs()
    done = 0
    print(f'=== Translating ALL missing to {lang} ({len(slugs)} EN posts) ===')
    for slug in slugs:
        # skip if already localized
        if os.path.exists(f'/home/kaliuser/worldtime/blog/{slug}-{lang}.html'):
            continue
        en = extract(slug)
        title = translate(en['title'], lang)
        if title is None:
            print(f'  QUOTA on {slug} title — skipping to next post.'); continue
        h1 = translate(en['h1'], lang)
        if h1 is None:
            print(f'  QUOTA on {slug} h1 — skipping to next post.'); continue
        meta = translate(en['meta'], lang)
        if meta is None:
            print(f'  QUOTA on {slug} meta — skipping to next post.'); continue
        kw = translate(en['kw'], lang)
        if kw is None:
            print(f'  QUOTA on {slug} kw — skipping to next post.'); continue
        bc = translate(en['bc'], lang)
        if bc is None:
            print(f'  QUOTA on {slug} bc — skipping to next post.'); continue
        faq_tr = []
        quota_on_faq = False
        for q, a in en['faqs']:
            qt = translate(q, lang); at = translate(a, lang)
            if qt is None or at is None:
                print(f'  QUOTA on {slug} FAQ — skipping to next post.')
                quota_on_faq = True
                break
            faq_tr.append((qt, at))
        if quota_on_faq:
            continue
        faq_html = '<div class="faq-section">' + ''.join(
            f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in faq_tr) + '</div>'
        localized_content = NOTICE[lang] + '\n' + en['content'] + '\n' + faq_html
        make_i18n_post(
            slug, lang, LANG_CODE[lang],
            title=title, h1=h1, meta_desc=meta, keywords=kw,
            breadcrumb=bc, display_date='July 16, 2026', read_time='6',
            tags='time zones', content=localized_content, faq_list=[]
        )
        done += 1
    print(f'Finished/stopped. Translated {done} posts to {lang}. Cache saved.')
