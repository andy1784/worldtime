#!/usr/bin/env python3
"""Generate historical time-zone change pages: /time-zone-history/<city>.html.

One page per city in cities_data.json (682 cities). Each page contains:
  * "When did [City] change time zone?" headline + country
  * Table of base-UTC-offset changes (year, from, to, reason) derived from zoneinfo
  * Current local time (live JS clock) + DST status
  * Embedded Google Map for the city
  * schema.org WebPage + FAQPage (3 questions)
  * hreflang x-default/en, canonical, OG/Twitter meta, AdSense slot

Run:  python3 scripts/generate_timezone_history_pages.py
Idempotent: re-running overwrites the same files.
"""
import json
import os
import re
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/.."
CITIES_FILE = os.path.join(ROOT, "cities_data.json")
OUT_DIR = os.path.join(ROOT, "time-zone-history")
SITE = "https://worldtimessync.com"
ADSENSE_CLIENT = "ca-pub-9728257902981529"


def slugify(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s).strip("-")
    return s or "city"


def fmt_off(off):
    total = int(off.total_seconds())
    sign = "+" if total >= 0 else "-"
    total = abs(total)
    h, m = divmod(total, 3600)
    m = m // 60
    return f"UTC{sign}{h:02d}:{m:02d}"


def base_offset_history(tz_name, start_year=1900, end_year=2026):
    """List of (year, from_offset, to_offset) for base-offset changes on 1 Jan each year."""
    tz = ZoneInfo(tz_name)
    history = []
    prev_off = None
    for year in range(start_year, end_year + 1):
        dt = datetime(year, 1, 1, 12, 0, 0, tzinfo=timezone.utc).astimezone(tz)
        off = dt.utcoffset() or timedelta(0)
        if prev_off is None:
            prev_off = off
            continue
        if off != prev_off:
            history.append((year, fmt_off(prev_off), fmt_off(off)))
            prev_off = off
    return history


def reason_for(year, old_off, new_off, tz_name):
    """Best-effort human-readable reason for a base-offset change."""
    old_total = int(__import__("datetime").timedelta(0).total_seconds())  # noqa
    # parse old/new to hours
    def to_hours(s):
        sign = 1 if s.startswith("UTC+") else -1
        m = re.search(r"UTC[+-](\d{2}):(\d{2})", s)
        return sign * (int(m.group(1)) + int(m.group(2)) / 60)

    oh, nh = to_hours(old_off), to_hours(new_off)
    delta = nh - oh

    # Wartime periods
    if 1914 <= year <= 1918:
        return "Wartime time-zone change (World War I)"
    if 1939 <= year <= 1945:
        return "Wartime time-zone change (World War II)"
    # DST adoption/abolition patterns
    if abs(delta) == 1.0:
        return "Daylight saving time adopted / adjusted"
    if abs(delta) == 0.5:
        return "Half-hour time-zone adjustment"
    if abs(delta) >= 2.0:
        return "Major time-zone law change"
    if old_total == 0 and nh != 0:
        return "Standard time offset established"
    return "Time zone law / administrative change"


def current_info(tz_name):
    tz = ZoneInfo(tz_name)
    now = datetime.now(tz)
    off = now.utcoffset() or timedelta(0)
    abbr = now.tzname() or "UTC"
    is_dst = bool(now.dst() and now.dst() != timedelta(0))
    return fmt_off(off), abbr, is_dst, now


def html_escape(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;")
                   .replace(">", "&gt;").replace('"', "&quot;"))


def build_page(city, slug=None):
    name = city["name"]
    country = city["country"]
    tz_name = city["timezone"]
    if slug is None:
        slug = slugify(name)
    offset, abbr, is_dst, now = current_info(tz_name)

    title = f"When Did {name} Change Time Zone? {tz_name} History"
    desc = (f"History of time zone changes for {name}, {country}. "
            f"UTC offset changes, DST adoption, and time zone law changes for {tz_name}.")
    canon = f"{SITE}/time-zone-history/{slug}"

    webpage = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": desc,
        "url": canon,
    }

    faq_q1 = f"When did {name} last change its time zone?"
    faq_a1 = (f"{name} follows the {tz_name} time zone. The most recent base-offset "
              f"change is shown in the table above; the city currently observes {offset}.")
    faq_q2 = f"Does {name} observe daylight saving time?"
    faq_a2 = (f"Yes, {name} currently observes daylight saving time ({abbr}). "
              f"Clocks move forward by 1 hour in spring and back by 1 hour in autumn." if is_dst else
              f"No, {name} does not currently observe daylight saving time. It stays on {abbr} ({offset}) year-round.")
    faq_q3 = f"What is the current UTC offset for {name}?"
    faq_a3 = f"{name} is on {offset} right now (time zone: {tz_name})."

    faqpage = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": faq_q1,
             "acceptedAnswer": {"@type": "Answer", "text": faq_a1}},
            {"@type": "Question", "name": faq_q2,
             "acceptedAnswer": {"@type": "Answer", "text": faq_a2}},
            {"@type": "Question", "name": faq_q3,
             "acceptedAnswer": {"@type": "Answer", "text": faq_a3}},
        ],
    }

    webpage_json = json.dumps(webpage, ensure_ascii=False)
    faq_json = json.dumps(faqpage, ensure_ascii=False)

    # --- change table ---
    history = base_offset_history(tz_name)
    rows = ""
    for year, old, new in history:
        reason = reason_for(year, old, new, tz_name)
        rows += (f"<tr><td>{year}</td><td>{html_escape(old)}</td>"
                 f"<td>{html_escape(new)}</td><td>{html_escape(reason)}</td></tr>")
    if not rows:
        rows = ("<tr><td colspan=\"4\">No base-offset time-zone changes recorded for "
                f"{tz_name} between 1900 and 2026.</td></tr>")

    map_url = ("https://www.google.com/maps?q=" +
               html_escape(f"{name}, {country}") + "&output=embed")

    dst_label = "Yes" if is_dst else "No"

    clock_js = (
        "<script>(function(){var tz=\"" + tz_name + "\";"
        "var el=document.getElementById(\"live-time\");"
        "function update(){try{var now=new Date();"
        "var timeStr=new Intl.DateTimeFormat(\"en-US\",{"
        "timeZone:tz,hour:\"2-digit\",minute:\"2-digit\",second:\"2-digit\","
        "hour12:true,weekday:\"long\",year:\"numeric\",month:\"long\",day:\"numeric\""
        "}).format(now);el.textContent=timeStr}catch(e){el.textContent=\"Time zone not supported\"}"
        "}update();setInterval(update,1000)})();</script>"
    )

    ga_ads_js = (
        "<script>window.addEventListener('load',function(){"
        "var s=document.createElement('script');s.async=true;"
        "s.src='https://pagead2.googlesyndication.com/pagead/js/"
        "adsbygoogle.js?client=" + ADSENSE_CLIENT + "';"
        "s.crossOrigin='anonymous';document.head.appendChild(s);"
        "var g=document.createElement('script');g.async=true;"
        "g.src='https://www.googletagmanager.com/gtag/js?id=G-LBX0CDYSSV';"
        "document.head.appendChild(g);"
        "var g2=document.createElement('script');"
        "g2.textContent='window.dataLayer=window.dataLayer||[];"
        "function gtag(){dataLayer.push(arguments);};"
        "gtag(\"js\",new Date());gtag(\"config\",\"G-LBX0CDYSSV\");"
        "gtag(\"config\",\"G-XCBTT7YSPY\");';"
        "document.head.appendChild(g2)});</script>"
    )

    html = f"""<!doctype html>
<html lang="en">
<head>
<style>*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif;line-height:1.6;color:#1a1a2e;background:#f5f7fa;min-height:100vh}}.container{{max-width:800px;margin:0 auto;padding:16px}}h1{{font-size:clamp(1.3rem,4vw,1.8rem);margin:16px 0 8px;color:#1a1a2e;line-height:1.3}}h2{{font-size:clamp(1.1rem,3vw,1.3rem);margin:20px 0 8px;color:#16213e;line-height:1.3}}.skip-link{{position:absolute;top:-40px;left:0;background:#667eea;color:#fff;padding:8px 16px;z-index:100;text-decoration:none;border-radius:0 0 4px 0}}.breadcrumb{{margin-bottom:12px;font-size:.85rem;color:#555}}.breadcrumb a{{color:#667eea;text-decoration:none}}.current-time-card{{background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:#fff;padding:clamp(20px,5vw,30px);border-radius:12px;margin:16px 0;text-align:center}}.live-time{{font-size:clamp(1.5rem,6vw,2.5rem);font-weight:700;margin:10px 0;font-variant-numeric:tabular-nums;line-height:1.2}}.time-details{{opacity:.9;margin-top:8px;font-size:.9rem}}a{{color:#667eea}}table{{width:100%;border-collapse:collapse;margin:16px 0;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.06)}}.map-wrap{{margin:16px 0;border-radius:12px;overflow:hidden;border:1px solid #ddd}}th,td{{padding:12px;text-align:left;border-bottom:1px solid #e5e7ea}}th{{background:#f3f4f6;font-weight:600;color:#16213e}}tr:last-child td{{border-bottom:none}}tr:hover{{background:#f9fafb}}.faq-section{{margin:24px 0}}.faq-section h3{{margin:12px 0 6px}}.seo-footer{{margin:32px 0;padding-top:16px;border-top:1px solid #ddd;font-size:.9rem;color:#555}}</style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <meta name="theme-color" content="#667eea">
    <meta name="google-site-verification" content="tNRYRY4K5ZdeEBPId3_g0GiclaIlooP5GhihYhXwknk">
    <title>{html_escape(title)}</title>
    <meta name="title" content="{html_escape(title)}">
    <meta name="description" content="{html_escape(desc)}">
    <meta name="keywords" content="{html_escape(name)} time zone history, {html_escape(name)} time zone change, {html_escape(country)} time zone, {tz_name} history, UTC offset changes">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canon}">
    <meta property="og:title" content="{html_escape(title)}">
    <meta property="og:image" content="{SITE}/og-image.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:description" content="{html_escape(desc)}">
    <meta property="og:site_name" content="World Time Sync">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{html_escape(title)}">
    <meta name="twitter:url" content="{canon}">
    <meta name="twitter:description" content="{html_escape(desc)}">
    <meta name="twitter:image" content="{SITE}/og-image.png">
    <meta name="twitter:image:alt" content="{html_escape(title)}">
    <meta name="twitter:creator" content="@worldtimesync">
    <meta name="twitter:site" content="@worldtimesync">
    <link rel="canonical" href="{canon}">
    <link rel="icon" type="image/svg+xml" href="{SITE}/favicon.svg">
    <link rel="preconnect" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://pagead.googlesyndication.com">
    <link rel="dns-prefetch" href="https://www.googlesyndication.com">
    <script type="application/ld+json">{webpage_json}</script>
    <script type="application/ld+json">{faq_json}</script>
    <link rel="alternate" hreflang="x-default" href="{canon}">
    <link rel="alternate" hreflang="en" href="{canon}">
</head>
<body>
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <main id="main-content">
        <div class="container">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="/">Home</a> &gt;
                <a href="/time-zones">Time Zones</a> &gt;
                <span aria-current="page">{html_escape(name)}</span>
            </nav>
            <h1>When Did {html_escape(name)} Change Time Zone?</h1>
            <div class="current-time-card" role="region" aria-label="Live clock for {html_escape(name)}">
                <h2>Current Time in {html_escape(name)}, {html_escape(country)}</h2>
                <p class="live-time" style="min-height:2.5rem" id="live-time" data-timezone="{html_escape(tz_name)}" aria-live="polite">Loading...</p>
                <p class="time-details">
                    <span>{html_escape(tz_name)}</span>
                    <span>{abbr} ({offset})</span>
                </p>
            </div>
            <section class="city-info" aria-label="About {html_escape(name)}">
                <h2>About {html_escape(name)}</h2>
                <ul>
                    <li><strong>City:</strong> {html_escape(name)}, {html_escape(country)}</li>
                    <li><strong>Time zone:</strong> {html_escape(tz_name)}</li>
                    <li><strong>Current offset:</strong> {offset}</li>
                    <li><strong>Time zone abbreviation:</strong> {abbr}</li>
                    <li><strong>Daylight saving time:</strong> {dst_label}</li>
                </ul>
                <p>This page shows the history of base UTC-offset changes for {html_escape(name)}. Changes in 1 January offset are recorded; annual daylight-saving transitions are not listed as separate changes.</p>
            </section>
            <section aria-label="Time zone change history">
                <h2>Time Zone Change History for {html_escape(name)}</h2>
                <table>
                    <thead>
                        <tr><th>Year</th><th>Previous offset</th><th>New offset</th><th>Reason</th></tr>
                    </thead>
                    <tbody>
                        {rows}
                    </tbody>
                </table>
                <p class="time-details" style="font-size:.85rem;color:#6b7280">Source: IANA time zone database ({html_escape(tz_name)}). Reasons are best-effort interpretations of offset-change patterns.</p>
            </section>
            <section class="map-wrap" aria-label="Map of {html_escape(name)}">
                <h2>Where Is {html_escape(name)}?</h2>
                <iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{map_url}" style="border:0;width:100%;height:300px;" allowfullscreen="" aria-label="Map of {html_escape(name)}, {html_escape(country)}"></iframe>
            </section>
            <section class="faq-section" aria-label="Frequently asked questions">
                <h2>Frequently Asked Questions</h2>
                <h3>{html_escape(faq_q1)}</h3>
                <p>{html_escape(faq_a1)}</p>
                <h3>{html_escape(faq_q2)}</h3>
                <p>{html_escape(faq_a2)}</p>
                <h3>{html_escape(faq_q3)}</h3>
                <p>{html_escape(faq_a3)}</p>
            </section>
            <p>Bookmark this page to track the time-zone history of {html_escape(name)}. You can also use our <a href="/">time zone converter</a> to compare {html_escape(name)} time with any other city in the world.</p>
        </div>
        <footer class="seo-footer">
            <nav aria-label="Footer navigation">
                <a href="/privacy">Privacy Policy</a> |
                <a href="/about">About Us</a> |
                <a href="/">World Time Sync</a>
            </nav>
            <p>&copy; 2026 World Time Sync. All rights reserved.</p>
        </footer>
        {clock_js}
        {ga_ads_js}
    </body>
</html>
"""
    return html


def main():
    cities = json.load(open(CITIES_FILE, encoding="utf-8"))
    os.makedirs(OUT_DIR, exist_ok=True)
    # Build unique slugs (disambiguate same-name cities with country token)
    seen = {}
    pairs = []
    for c in cities:
        base = slugify(c["name"])
        slug = base
        if slug in seen:
            token = slugify(c["country"]).split("-")[0][:4]
            slug = f"{base}-{token}"
            if slug in seen:
                slug = f"{base}-{c['id']}"
        seen[slug] = True
        pairs.append((c, slug))
    written = 0
    for city, slug in pairs:
        path = os.path.join(OUT_DIR, slug + ".html")
        html = build_page(city, slug)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
            fh.flush(); os.fsync(fh.fileno())
        written += 1
    print(f"Wrote {written} pages to {OUT_DIR}")
    renames = [(c["name"], s) for c, s in pairs if s != slugify(c["name"])]
    if renames:
        print("Disambiguated slugs (name collision):")
        for name, s in renames:
            print(f"  {name} -> {s}")


if __name__ == "__main__":
    main()
