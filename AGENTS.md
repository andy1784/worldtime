# Project notes / TODOs

## Known limitations (require source; not in this repo)

The production JS bundle (`assets/index-Dd7au40z.js`, 442 KB minified) and CSS
(`assets/index-ufePLcBr.css`, 91 KB) are committed as static Vite artifacts —
the Vite/React **source** lives outside this repository (see `package.json`,
which only exposes `start: npx serve .`). Audits that need a rebuild cannot be
applied from here without first importing the SPA source into this repo.

### TODO: real code-split (audit item #6)
- Re-import the Vite/React source for the world-clock SPA, expose `build` /
  `typecheck` / `lint` scripts in `package.json`, and Ship a `vite.config.ts`
  with manual chunks (`React.lazy` for the city registry,
  `react-dom/client` production build, time-zone registry as a separate chunk
  loaded after LCP). This is not possible against the committed artifacts.
- Until then, the main bundle is loaded with `async` everywhere (no `defer`
  because Vite ESM modules already defer by default; `async` lets the bundle
  download in parallel and not block HTML parsing/initial paint).
- Make sure every page loads the bundle with `async` (12 blog pages used to load
  it blocking; fixed on 2026-07-17).

### TODO: rebuild pipeline (audit item #7)
- `package.json` has only `start: npx serve .`. Add reproducible build:
  `build` (vite build), `dev` (vite), `lint` (eslint) and `typecheck`
  (tsc --noEmit) once the SPA source is back in the repo.

### Known SEO data issue (not in audit scope, recorded for visibility)
~495 HTML pages have `canonical href="https://worldtimessync.com/country/"`
pointing to the listing root instead of their own country article. That is a
canonical cannibalization bug distinct from audit items #2/#8 and is left for
the next batch.

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
