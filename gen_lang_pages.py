#!/usr/bin/env python3
"""Generate language-localized pages (country/time/blog/meeting-planner) via LLM translation.
Parallel + resume. Usage: python3 gen_lang_pages.py <lang> [--workers N]
"""
import json, sys, os, re, time, urllib.request, urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = Path('/home/kaliuser/worldtime')
auth = json.load(open('/home/kaliuser/.hermes/auth.json'))
TOK = None
for t in auth['credential_pool'].get('alibaba', []):
    if t.get('access_token','').startswith('sk-or'):
        TOK = t['access_token']; break
assert TOK, "no openrouter token"
MODEL = "nvidia/nemotron-3-super-120b-a12b:free"
LANGS = {
    'es': 'Spanish', 'zh': 'Chinese (Simplified)', 'ru': 'Russian',
    'it': 'Italian', 'de': 'German', 'ja': 'Japanese', 'fr': 'French', 'uk': 'Ukrainian',
}

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
            raise
        except Exception:
            time.sleep(backoff); backoff = min(backoff*2, 60)
    raise RuntimeError("translate failed after retries")

def localize_urls(html, lang, src_rel, dst_rel):
    html = re.sub(r'https?://worldtimessync\.com/' + re.escape(src_rel),
                  'https://worldtimessync.com/' + dst_rel, html)
    html = re.sub(r'<html lang="en">', f'<html lang="{lang}">', html)
    return html

def job(lang, src_dir, dst_dir, sf):
    rel = sf.stem
    df = dst_dir / sf.name
    if df.exists():
        return f"skip {sf.name}"
    html = sf.read_text(encoding='utf-8')
    src_rel = f"{src_dir.name}/{rel}"
    dst_rel = f"{lang}/{src_dir.name}/{rel}"
    html = localize_urls(html, lang, src_rel, dst_rel)
    out = translate_html(html, LANGS[lang])
    # basic structural guard: if hreflang present in source but missing in output, re-inject
    if 'rel="alternate" hreflang' in html and 'rel="alternate" hreflang' not in out:
        # extract hreflang block from source and inject before </head>
        m = re.search(r'(<link rel="alternate" hreflang.*?/>\s*)+', html, re.S)
        if m:
            out = out.replace('</head>', m.group(0) + '\n</head>', 1)
    df.write_text(out, encoding='utf-8')
    return f"ok {sf.name}"

def process(lang, workers=5):
    tname = LANGS[lang]
    targets = [
        (BASE/'country', BASE/f'{lang}/country'),
        (BASE/'time', BASE/f'{lang}/time'),
        (BASE/'blog', BASE/f'{lang}/blog'),
    ]
    tasks = []
    for src_dir, dst_dir in targets:
        if not src_dir.exists(): continue
        dst_dir.mkdir(parents=True, exist_ok=True)
        for sf in sorted(src_dir.glob('*.html')):
            tasks.append((src_dir, dst_dir, sf))
    # meeting-planner
    mp = BASE/'meeting-planner.html'
    if mp.exists():
        dmp = BASE/f'{lang}/meeting-planner.html'
        if not dmp.exists():
            tasks.append(('mp', BASE/f'{lang}', mp))
    total = len(tasks)
    print(f"[{lang}] {total} tasks queued (workers={workers})")
    ok = skip = fail = 0
    def run(t):
        if t[0] == 'mp':
            sf = t[2]; df = t[1]/sf.name
            if df.exists(): return "skip mp"
            html = sf.read_text(encoding='utf-8')
            html = localize_urls(html, lang, 'meeting-planner', f'{lang}/meeting-planner')
            out = translate_html(html, tname)
            df.write_text(out, encoding='utf-8')
            return "ok mp"
        return job(lang, t[0], t[1], t[2])
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(run, t) for t in tasks]
        for i, fu in enumerate(as_completed(futs), 1):
            try:
                r = fu.result()
            except Exception as e:
                import traceback
                open('/tmp/gen_fail.log','a').write(f"[{lang}] {repr(e)}\n{traceback.format_exc()}\n")
                r = f"FAIL {e}"
            if r.startswith('ok'): ok += 1
            elif r.startswith('skip'): skip += 1
            else: fail += 1
            if i % 25 == 0:
                print(f"[{lang}] {i}/{total} ok={ok} skip={skip} fail={fail}")
    print(f"[{lang}] DONE ok={ok} skip={skip} fail={fail}")

if __name__ == '__main__':
    lang = sys.argv[1] if len(sys.argv)>1 else 'es'
    workers = 5
    args = sys.argv[2:]
    i = 0
    while i < len(args):
        a = args[i]
        if a.startswith('--workers'):
            if '=' in a:
                workers = int(a.split('=')[1])
            else:
                i += 1
                workers = int(args[i])
        i += 1
    if lang not in LANGS:
        print("unknown lang", lang); sys.exit(1)
    process(lang, workers=workers)
