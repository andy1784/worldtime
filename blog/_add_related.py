#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add 'Related Articles' block to the 11 new EN posts that lack it.
Picks 3-4 related posts by keyword matching from the full EN post list.
Inserts before </article>.
"""
import re, os, glob

BLOG = '/home/kaliuser/worldtime/blog'

# All EN posts (exclude localized)
all_posts = []
for f in glob.glob(os.path.join(BLOG, '*.html')):
    base = os.path.basename(f)
    if re.search(r'-(ru|es|zh|ja|fr|de|uk)\.html$', base):
        continue
    all_posts.append(base.replace('.html', ''))

# Keyword groups for similarity
GROUPS = {
    'time-difference': ['time-difference'],
    'convert': ['convert-'],
    'meeting': ['meeting', 'schedule', 'remote', 'etiquette', 'call'],
    'dst': ['daylight', 'dst'],
    'general': ['time-zone', 'time', 'clock'],
}

def keywords_of(slug):
    kws = []
    for g, terms in GROUPS.items():
        for t in terms:
            if t in slug:
                kws.append(g)
                break
    return kws or ['general']

def related_to(slug, n=4):
    sk = set(keywords_of(slug))
    scored = []
    for other in all_posts:
        if other == slug:
            continue
        ok = set(keywords_of(other))
        score = len(sk & ok)
        if score > 0:
            scored.append((score, other))
    scored.sort(key=lambda x: (-x[0], x[1]))
    # fallback: if too few, add recent/general ones
    if len(scored) < n:
        for other in all_posts:
            if other != slug and other not in [s[1] for s in scored]:
                scored.append((0, other))
            if len(scored) >= n:
                break
    return [s[1] for s in scored[:n]]

# Manual override for best relevance
OVERRIDE = {
 'time-difference-tokyo-london': ['time-difference-singapore-london','time-difference-tokyo-sydney','time-difference-london-tokyo','convert-gmt-to-est'],
 'time-difference-singapore-london': ['time-difference-tokyo-london','time-difference-london-tokyo','convert-gmt-to-ist','best-time-to-call-usa-from-europe'],
 'time-difference-tokyo-sydney': ['time-difference-tokyo-london','time-difference-singapore-london','best-time-to-call-japan','best-time-to-call-australia'],
 'convert-gmt-to-ist': ['convert-ist-to-gmt','convert-utc-to-est','convert-est-to-gmt','time-difference-singapore-london'],
 'convert-utc-to-est': ['convert-est-to-gmt','convert-pst-to-gmt','convert-gmt-to-ist','best-time-to-schedule-meeting-across-time-zones'],
 'best-time-to-call-usa-from-europe': ['best-time-to-call-usa','best-time-to-call-uk','how-daylight-saving-affects-meetings','best-time-to-schedule-meeting-across-time-zones'],
 'how-daylight-saving-affects-meetings': ['daylight-saving-time-explained','best-time-to-call-usa-from-europe','time-zone-meeting-etiquette-remote-teams','daylight-saving-2026-prep'],
 'best-time-to-schedule-meeting-across-time-zones': ['time-zone-meeting-etiquette-remote-teams','best-time-to-call-usa-from-europe','best-meeting-times-remote-teams','how-daylight-saving-affects-meetings'],
 'time-zone-meeting-etiquette-remote-teams': ['best-time-to-schedule-meeting-across-time-zones','best-meeting-times-remote-teams','how-daylight-saving-affects-meetings','best-time-to-call-internationally'],
 'convert-est-to-gmt': ['convert-gmt-to-est','convert-pst-to-gmt','convert-utc-to-est','time-difference-singapore-london'],
 'convert-pst-to-gmt': ['convert-est-to-gmt','convert-gmt-to-est','convert-utc-to-est','best-time-to-call-usa'],
}

TARGETS = list(OVERRIDE.keys())

for slug in TARGETS:
    path = os.path.join(BLOG, slug + '.html')
    if not os.path.exists(path):
        print('SKIP (missing):', slug); continue
    html = open(path, encoding='utf-8').read()
    if 'Related Articles' in html or 'related-posts' in html:
        print('SKIP (already has):', slug); continue
    rel = OVERRIDE[slug]
    items = ''
    for r in rel:
        rpath = os.path.join(BLOG, r + '.html')
        rtitle = r.replace('-', ' ').title()
        if os.path.exists(rpath):
            rm = re.search(r'<title>(.*?)\s*\| World Time Sync</title>', open(rpath, encoding='utf-8').read())
            if rm:
                rtitle = rm.group(1).strip()
        items += f'        <li><a href="/blog/{r}.html">{rtitle}</a></li>\n'
    block = f'''
    <section class="related-articles" aria-label="Related articles">
        <h2>Related Articles</h2>
        <ul>
{items}        </ul>
    </section>
'''
    # insert before </article>
    if '</article>' in html:
        html = html.replace('</article>', block + '</article>', 1)
        open(path, 'w', encoding='utf-8').write(html)
        print('ADDED related to:', slug)
    else:
        print('WARN no </article> in', slug)

print('Done.')
