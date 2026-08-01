# Project notes / TODOs

## Known limitations (require source; not in this repo)

The production JS bundle (`assets/index-Dd7au40z.js`, 442 KB minified) and CSS
(`assets/index-ufePLcBr.css`, 91 KB) are committed as static Vite artifacts —
the Vite/React **source** lives outside this repository (see `package.json`,
which only exposes `start: npx serve .`). Audits that need a rebuild cannot be
applied from here without first importing the SPA source into this repo.

## Recent work log (2026-07-31)
- `e5f35aa6` — Rewrote `<title>`/`<meta description>` on the top-10 impression
  pages (`index.html`, `time-zones/{est,pst,cst,mst}.html`,
  `country/{china,india}.html`) to target the high-impression GSC queries
  (e.g. "est time now" 129impr, "pst time now" 103impr, "cst time now" 73impr).
- `affad9fa` — Added `/time/index.html` city-directory landing (canonical,
  hreflang, JSON-LD, 696 static city links). `gen_sitemap.py` now emits `/time`;
  sitemap went 926 → 948 URLs.
- `4f61ea16` — Added `vercel.json` route `/(es|zh|ru|it|de|ja|fr|uk)/blog/(.+)\.html`
  → 301 `/blog/$2-$1` to collapse the 2-hop 308→301 redirect chain on localized
  blog posts.
- `e3a255a9` — Stripped 45,794 internal `/foo.html` hrefs → `/foo` (cleanUrls)
  across 7,631 HTML files to eliminate GSC redirect/canonical errors; kept
  `widget.html`/`widget-embed.html` (external-embed URLs).
- `affad9fa` — Removed 1,256 broken `/time/<city>` hrefs (113 nonexistent cities),
  fixed 40 suffix blog links, redirected `<lang>/time-difference`→`/time-difference`,
  `<lang>/time/`→`/time/`, `/en/` breadcrumbs→`/`.
- `f5279581` — Mobile CTR mitigation: homepage `index.html` now lazy-loads the
  442 KB React bundle (`assets/index-Dd7au40z.js`) on first user interaction
  (click/touch/keystroke) with a 4 s fallback eager load. Drops homepage TBT
  from ~3838 ms to ~0 (Lighthouse) without hurting SEO (static HTML + H1 +
  noscript city/FAQ content above `#root`). See comment block above the loader.

### TODO: real code-split (audit item #6) — mitigated, not closed
- The homepage bundle is now lazy-loaded (see `index.html` loader), so Core
  Web Vitals TBT/INP are fixed for search. The bundle is no longer auto-loaded
  on the homepage; it is created on-demand inside `loadApp()`.
- True code-splitting (manual chunks / `React.lazy` / registry chunk after LCP)
  still requires the Vite/React **source**, which lives outside this repo.
  `package.json` only exposes `start: npx serve .` — see the rebuild TODO below.
- Other pages load the bundle with `async` (12 blog pages used to load it
  blocking; fixed 2026-07-17).

### TODO: rebuild pipeline (audit item #7)
- `package.json` has only `start: npx serve .`. Add reproducible build:
  `build` (vite build), `dev` (vite), `lint` (eslint) and `typecheck`
  (tsc --noEmit) once the SPA source is back in the repo.

### Known SEO data issue (not in audit scope, recorded for visibility)
~495 HTML pages have `canonical href="https://worldtimessync.com/country/"`
pointing to the listing root instead of their own country article. That is a
canonical cannibalization bug distinct from audit items #2/#8 and is left for
the next batch.

→ 2026-07-18 update: re-checked — these 495 pages are actually `<meta http-equiv="refresh">`
**redirect stubs** with `noindex, follow` + `<title>Redirecting…</title>` pointing
to `/country/`. They are intentional consolidation pages (only 67 EN/ES country
hubs are fully translated; the other ~855 lang-country files are stubs that
keep URL consistency and redirect users to the country listing). The canonical
on `noindex` stubs is ignored by Google, so this is **not a real bug** — only
the 67 EN + 67 ES real country hubs have proper hreflang (committed).

### TODO #4 blog hreflang block on 106 pages (2026-07-18 GSC Coverage finding) — RESOLVED
Translation generator `gen_new_blog_translations_*.py` statically emits an
hreflang link for all 8 languages on every blog post (e.g. `hreflang="ru"` on
`blog/<slug>-zh.html`), regardless of whether a `blog/<slug>-<lang>.html`
actually exists. This produced **483 broken (404-bound) hreflang links across
106 files** because:

1. The hreflang URL is `worldtimessync.com/<lang>/blog/<slug>.html`.
2. Vercel 301-redirects that to `/blog/<slug>-<lang>.html`
   (see `vercel.json` route added in commit 28c426df / SEO-F).
3. If `blog/<slug>-<lang>.html` doesn't exist (post is only translated to some
   languages), the URL ultimately 404s.

Resolution (committed `eab1b879`):
- `add_hreflang_only_existing.py` + `blog_hreflang_util.py` form a durable,
  idempotent post-processor. `render_hreflang(slug, lang, present_langs)` emits
  x-default + en + ONLY languages whose `blog/<slug>-<lang>.html` exists on disk.
  Run `python3 add_hreflang_only_existing.py` after any generation batch.
- Applied once over all committed `blog/*.html`: 8827 hreflang links verified,
  0 broken targets, 0 duplicate langs, 0 old-format `<lang>/blog/` URLs.

Deferred (do NOT edit blind):
- Hardening the generator *source* (`gen_new_blog_translations_*.py`,
  `gen_batch2.py`, `gen_batch3.py`) to call `render_hreflang` at write time is
  NOT done. These scripts are stale/inconsistent with the committed output
  (they pass `slug_html = slug + '.html'` — including the lang suffix — into
  `build_head`, which would corrupt canonical hreflang URLs if run as-is).
  Editing them risks breaking regeneration without a verified baseline. **Fix:
  run the post-processor after re-generating instead of hand-patching these
  stale scripts.** Re-visit once the active generator path is confirmed.

### TODO: corrupt localized title/description on fr/uk toulouse page
Resolved 2026-07-18 (commit a12f1136) — `Touloutilise-t-il` / `Touloвикористовує`
replaced with `Toulouse` on `fr/time/toulouse.html` + `uk/time/toulouse.html`.
Other pages from the same translation generator batch should be scanned for
similar garbage (e.g. `/blog/...-fr.html` had `futilise-t-ilau` substring — see
commit history). Worth running `rg -i 'utilise-t-il|використовує' blog/ fr/ uk/`.

## Verified deploy config (post-artifact audit fixes committed 2026-07-17)
- `vercel.json` — widget-embed served with `X-Frame-Options: ALLOWALL` /
  per-page CSP `frame-ancestors *`; HSTS `includeSubDomains; preload`;
  Ahrefs allowed in `script-src`/`connect-src`; route-404 for `*.py`/`*.sh`
  and internal `*.md` and backup directories.
- `.vercelignore` — strips `*.py`, `*.sh`, `__pycache__/`, `tools/`,
  `README*_*.md` internals and `blog_hreflang_backup_*/` from the upload.
- Lang index pages (`/index.html`, `/es`, `/ru`, ...) — canonical / hreflang /
  og:url / JSON-LD `url` all without trailing slash (cleanUrls +
  trailingSlash:false); fixed fr/uk canonical pointing to wrong root and
  duplicate hreflang entries.
- `api/meeting-planner/world-time-map` — main CSS loaded async via print/onload
  swap + `<noscript>` fallback to spare ~91KB blocking CSS.
- `robots.txt` — blocks `GPTBot`/`CCBot`/`ClaudeBot`/`Bytespider`/`PerplexityBot`.
- PWA `manifest.json` — proper 192/512 PNG icons (maskable).
