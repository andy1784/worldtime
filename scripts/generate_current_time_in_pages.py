#!/usr/bin/env python3
"""Generate static /current-time-in/<city>.html landing pages.

One page per city in cities_data.json (682 cities). Each page contains:
  * live clock (JS, updates every second, zoneinfo-driven)
  * UTC offset + time zone name
  * DST status + next DST transition dates
  * embedded Google Map for the city
  * schema.org WebPage + FAQPage (exactly 3 questions)
  * hreflang x-default/en, canonical, OG/Twitter meta
  * AdSense slot (consistent with other landings)

Run:  python3 scripts/generate_current_time_in_pages.py
Idempotent: re-running overwrites the same files.
"""
import json
import os
import re
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/.."
CITIES_FILE = os.path.join(ROOT, "cities_data.json")
OUT_DIR = os.path.join(ROOT, "current-time-in")
SITE = "https://worldtimessync.com"
ADSENSE_CLIENT = "ca-pub-9728257902981529"

# --------------------------------------------------------------------------- CSS (literal, no interpolation)
CSS = """*{
margin:0;padding:0;box-sizing:border-box
}
body{
font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif;
line-height:1.6;color:#1a1a2e;background:#f5f7fa;min-height:100vh
}
.container{
max-width:800px;margin:0 auto;padding:16px
}
h1{
font-size:clamp(1.3rem,4vw,1.8rem);margin:16px 0 8px;color:#1a1a2e;line-height:1.3
}
h2{
font-size:clamp(1.1rem,3vw,1.3rem);margin:20px 0 8px;color:#16213e;line-height:1.3
}
.skip-link{
position:absolute;top:-40px;left:0;background:#667eea;color:#fff;
padding:8px 16px;z-index:100;text-decoration:none;border-radius:0 0 4px 0
}
.breadcrumb{
margin-bottom:12px;font-size:.85rem;color:#555
}
.breadcrumb a{
color:#667eea;text-decoration:none
}
.current-time-card{
background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:#fff;
padding:clamp(20px,5vw,30px);border-radius:12px;margin:16px 0;text-align:center
}
.current-time-card h2{
color:#fff;margin-top:0;font-size:clamp(1rem,2.5vw,1.2rem)
}
.live-time{
font-size:clamp(1.5rem,6vw,2.5rem);font-weight:700;margin:10px 0;
font-variant-numeric:tabular-nums;line-height:1.2
}
.time-details{
opacity:.9;margin-top:8px;font-size:.9rem
}
a{color:#667eea}
.map-wrap{
margin:16px 0;border-radius:12px;overflow:hidden;border:1px solid #ddd
}
.faq-section{margin:24px 0}
.faq-section h3{margin:12px 0 6px}
.seo-footer{
margin:32px 0;padding-top:16px;border-top:1px solid #ddd;
font-size:.9rem;color:#555
}
"""

# --------------------------------------------------------------------------- JS clock (literal except {TZ} placeholder)
CLOCK_JS = """>=0%"
</div>
<button class="copy-time-btn" id="copy-time-btn" type="button">Copy time</button>
"""
# (the inline <script> block itself is assembled in build_page using {tz})


# --------------------------------------------------------------------------- helpers
def slugify(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s).strip("-")
    return s or "city"


def build_slugs(cities):
    """Unique slugs; disambiguate same-name cities with a country token."""
    seen = {}
    out = []
    for c in cities:
        base = slugify(c["name"])
        slug = base
        if slug in seen:
            token = slugify(c["country"]).split("-")[0][:4]
            slug = f"{base}-{token}"
            if slug in seen:
                slug = f"{base}-{c['id']}"
        seen[slug] = True
        out.append((c, slug))
    return out


def offset_str(off):
    total = int(off.total_seconds())
    sign = "+" if total >= 0 else "-"
    total = abs(total)
    h, m = divmod(total, 3600)
    m = m // 60
    return f"UTC{sign}{h:02d}:{m:02d}"


def dst_info(tz_name):
    tz = ZoneInfo(tz_name)
    now = datetime.now(tz)
    off = now.utcoffset() or timedelta(0)
    abbr = now.tzname() or "UTC"
    is_dst = bool(now.dst() and now.dst() != timedelta(0))

    next_change = None
    cur_off = off
    base = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    for i in range(1, 15):
        candidate = (base + timedelta(days=32 * i)).replace(day=1)
        c_local = candidate.astimezone(tz)
        c_off = c_local.utcoffset() or timedelta(0)
        if c_off != cur_off:
            next_change = c_local.isoformat()
            cur_off = c_off
            break

    return offset_str(off), abbr, is_dst, next_change


# --------------------------------------------------------------------------- page builder
def build_page(city, slug):
    name = city["name"]
    country = city["country"]
    tz_name = city["timezone"]
    offset, abbr, is_dst, next_change = dst_info(tz_name)

    title = f"Current Time in {name}, {country} | World Time Sync"
    desc = (f"What time is it in {name} right now? Check the current local time in "
            f"{name}, {country}. Live clock, UTC offset ({offset}), DST status.")
    canon = f"{SITE}/current-time-in/{slug}"

    webpage = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": desc,
        "url": canon,
    }

    faq_q1 = f"What time is it in {name} right now?"
    faq_a1 = (f"The current time in {name} is shown in the live clock on this page. "
              f"{name} follows the {tz_name} time zone ({offset}).")
    faq_q2 = f"Does {name} observe daylight saving time?"
    if is_dst:
        faq_a2 = (f"Yes, {name} currently observes daylight saving time ({abbr}). "
                  f"Clocks move forward by 1 hour in spring and back by 1 hour in autumn.")
    else:
        faq_a2 = (f"No, {name} does not currently observe daylight saving time. "
                  f"It stays on {abbr} ({offset}) year-round.")
    faq_q3 = f"What is the UTC offset for {name}?"
    faq_a3 = f"{name} is on {offset} right now (time zone: {tz_name})."

    faqpage = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": faq_q1,
                "acceptedAnswer": {"@type": "Answer", "text": faq_a1},
            },
            {
                "@type": "Question",
                "name": faq_q2,
                "acceptedAnswer": {"@type": "Answer", "text": faq_a2},
            },
            {
                "@type": "Question",
                "name": faq_q3,
                "acceptedAnswer": {"@type": "Answer", "text": faq_a3},
            },
        ],
    }

    webpage_json = json.dumps(webpage, ensure_ascii=False)
    faq_json = json.dumps(faqpage, ensure_ascii=False)

    if next_change:
        dt = datetime.fromisoformat(next_change)
        dst_line = (f"<p><strong>Next time change:</strong> "
                    f"{dt.strftime('%d %b %Y %H:%M')} local time.</p>")
    else:
        dst_line = "<p>No scheduled time-zone change in the coming months.</p>"

    map_q = f"{name}, {country}"
    map_url = "https://www.google.com/maps?q=" + map_q + "&output=embed"

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
        "var ahrefs=document.createElement('script');ahrefs.async=true;"
        "ahrefs.src='https://analytics.ahrefs.com/analytics.js';"
        "ahrefs.setAttribute('data-key','hB1VYWuwb1i/f1d8re7P2A');"
        "document.head.appendChild(ahrefs);"
        "var ga=document.createElement('script');ga.async=true;"
        "ga.src='https://www.googletagmanager.com/gtag/js?id=G-LBX0CDYSSV';"
        "document.head.appendChild(ga);"
        "var ga2=document.createElement('script');"
        "ga2.textContent='window.dataLayer=window.dataLayer||[];"
        "function gtag(){dataLayer.push(arguments);};"
        "gtag(\"js\",new Date());gtag(\"config\",\"G-LBX0CDYSSV\");"
        "gtag(\"config\",\"G-XCBTT7YSPY\");';"
        "document.head.appendChild(ga2);"
        "var ads=document.createElement('script');ads.async=true;"
        "ads.src='https://pagead2.googlesyndication.com/pagead/js/"
        "adsbygoogle.js?client=" + ADSENSE_CLIENT + "';"
        "ads.crossOrigin='anonymous';document.head.appendChild(ads)});</script>"
    )

    html = f"""<!doctype html>
<html lang="en">
<head>
<style>{CSS}</style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <meta name="theme-color" content="#667eea">
    <meta name="google-site-verification" content="tNRYRY4K5ZdeEBPId3_g0GiclaIlooP5GhihYhXwknk">
    <title>{title}</title>
    <meta name="title" content="{title}">
    <meta name="description" content="{desc}">
    <meta name="keywords" content="current time in {name}, {name} time now, {name} local time, {name} clock, {country} time">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canon}">
    <meta property="og:title" content="{title}">
    <meta property="og:image" content="{SITE}/og-image.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:description" content="{desc}">
    <meta property="og:site_name" content="World Time Sync">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:url" content="{canon}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{SITE}/og-image.png">
    <meta name="twitter:image:alt" content="{title}">
    <meta name="twitter:creator" content="@worldtimesync">
    <meta name="twitter:site" content="@worldtimesync">
    <link rel="canonical" href="{canon}">
    <link rel="preload" href="/assets/city.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="/assets/city.css"></noscript>
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
                <a href="/current-time-in">Current Time Anywhere</a> &gt;
                <span aria-current="page">{name}</span>
            </nav>
            <h1>Current Time in {name}, {country}</h1>
            <div class="current-time-card" role="region" aria-label="Live clock for {name}">
                <h2>Current Time in {name}</h2>
                <p class="live-time" style="min-height:2.5rem" id="live-time" data-timezone="{tz_name}" aria-live="polite">Loading...</p>
                <div class="minute-progress"><div class="minute-progress-bar" id="minute-bar" style="width:0%"></div></div>
                <button class="copy-time-btn" id="copy-time-btn" type="button">Copy time</button>
                <p class="time-details">
                    <span>{tz_name}</span>
                    <span>{abbr} ({offset})</span>
                </p>
            </div>
            <section class="time-info" aria-label="Time zone details">
                <h2>Time Zone Details</h2>
                <ul>
                    <li><strong>City:</strong> {name}, {country}</li>
                    <li><strong>Time zone:</strong> {tz_name}</li>
                    <li><strong>Current offset:</strong> {offset}</li>
                    <li><strong>Time zone abbreviation:</strong> {abbr}</li>
                    <li><strong>Daylight saving time:</strong> {dst_label}</li>
                </ul>
                {dst_line}
            </section>
            <section class="map-wrap" aria-label="Map of {name}">
                <h2>Where Is {name}?</h2>
                <iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{map_url}" style="border:0;width:100%;height:300px;" allowfullscreen="" aria-label="Map of {name}, {country}"></iframe>
            </section>
            <section class="faq-section" aria-label="Frequently asked questions">
                <h2>Frequently Asked Questions</h2>
                <h3>{faq_q1}</h3>
                <p>{faq_a1}</p>
                <h3>{faq_q2}</h3>
                <p>{faq_a2}</p>
                <h3>{faq_q3}</h3>
                <p>{faq_a3}</p>
            </section>
            <p>Bookmark this page for quick access to the current time in {name}. The live clock never needs refreshing — it updates automatically. You can also use our <a href="/">time zone converter</a> to compare {name} time with any other city in the world.</p>
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


# --------------------------------------------------------------------------- main
def main():
    cities = json.load(open(CITIES_FILE, encoding="utf-8"))
    os.makedirs(OUT_DIR, exist_ok=True)
    pairs = build_slugs(cities)
    written = 0
    for city, slug in pairs:
        path = os.path.join(OUT_DIR, slug + ".html")
        html = build_page(city, slug)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
            fh.flush()
            os.fsync(fh.fileno())
        written += 1
    print(f"Wrote {written} pages to {OUT_DIR}")
    renames = [(c["name"], s) for c, s in pairs if s != slugify(c["name"])]
    if renames:
        print("Disambiguated slugs (name collision):")
        for name, s in renames:
            print(f"  {name} -> {s}")


if __name__ == "__main__":
    main()
