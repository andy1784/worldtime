"""
blog_hreflang_util — single source of truth for `<link rel="alternate" hreflang>`
blocks on blog posts.

Why this exists (AGENTS.md TODO #4):
  The translation generators used to hardcode an hreflang block listing ALL eight
  languages (x-default, en, es, zh, ru, it, de, ja, fr, uk) on every post,
  regardless of whether the `<slug>-<lang>.html` translation actually exists.
  That emitted ~1,372 broken (404-bound) hreflang links across 106 posts.

  The generators now call `render_hreflang(slug, lang, present_langs)` so only
  languages whose translation files exist are referenced. A companion
  post-processor `add_hreflang_only_existing.py` rewrites every committed blog
  post's header to match on-disk reality (run it after any generation batch).

A post is only ever translated to a strict subset of languages, so a missing
translation MUST be omitted from hreflang rather than left linking to a 404.
`x-default` and `en` are always emitted (an English base post always exists
when a translation exists).
"""
from __future__ import annotations
import os

SITE = "https://worldtimessync.com"
# Canonical set of non-English languages used across the translation batches.
LANG_LINK_ORDER = ("es", "zh", "ru", "it", "de", "ja", "fr", "uk")


def _file_exists(slug: str, lang: str) -> bool:
    """True iff blog/<slug>-<lang>.html exists on disk."""
    return os.path.exists(os.path.join("blog", f"{slug}-{lang}.html"))


def render_hreflang(
    slug: str,
    lang: str,
    present_langs: set | None = None,
) -> str:
    """Build the `<link rel="alternate">` header block for one blog post.

    Includes:
      * x-default and en  — always (an EN base post is implied)
      * `lang`            — the language currently being generated (always present)
      * other languages   — only if their `blog/<slug>-<lang>.html` file exists
                            on disk OR is in `present_langs` (this generation batch)

    `slug` is the English canonical slug (e.g. "world-clock-for-remote-teams").
    `lang`  is the language code of the file being generated (e.g. "zh").
    `present_langs`, if supplied, are the additional langs produced in the same
    batch run and therefore guaranteed to exist once the run completes — the
    generator passes T[slug].keys() here to avoid under-linking translations
    that are written later in the same batch.
    """
    present = set(present_langs or [])
    present.add(lang)  # the post being written always resolves to itself
    # Anything already on disk from a prior batch also resolves.
    for L in LANG_LINK_ORDER:
        if _file_exists(slug, L):
            present.add(L)

    links = [
        f'<link rel="alternate" hreflang="x-default" href="{SITE}/blog/{slug}">',
        f'<link rel="alternate" hreflang="en" href="{SITE}/blog/{slug}">',
    ]
    for L in LANG_LINK_ORDER:
        if L in present:
            links.append(f'<link rel="alternate" hreflang="{L}" href="{SITE}/blog/{slug}-{L}">')
    return "\n    ".join(links)
