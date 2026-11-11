#!/usr/bin/env python3
"""Build the time-zone converter widget bundle.

Outputs:
  assets/converter-widget.mjs   ESM module + inlined city database (<15 KB gz target)
  converter.html                standalone page (also works inside an iframe, reads ?from=&to=)
  converter-embed.html          minimal iframe-optimized page (noindex)

Run:  python3 scripts/generate_converter_widget.py
"""
import json
import os
import re
import gzip

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/.."
CITIES_FILE = os.path.join(ROOT, "cities_data.json")
ASSETS_DIR = os.path.join(ROOT, "assets")


def slugify(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s).strip("-")
    return s or "city"


def load_cities():
    cities = json.load(open(CITIES_FILE, encoding="utf-8"))
    out = []
    seen_ids = set()
    seen_slugs = set()
    for c in cities:
        cid = c["id"]
        name = c["name"]
        country = c["country"]
        tz = c["timezone"]
        slug = slugify(name)
        if cid in seen_ids or slug in seen_slugs:
            continue
        seen_ids.add(cid)
        seen_slugs.add(slug)
        out.append({"i": cid, "n": name, "c": country, "tz": tz})
    hubs = {"nyc", "london", "tokyo", "los-angeles", "chicago", "dubai",
            "singapore", "sydney", "mumbai", "sao-paulo", "moscow", "istanbul"}
    hub_list = [c for c in out if c["i"] in hubs]
    rest = [c for c in out if c["i"] not in hubs]
    rest.sort(key=lambda c: c["n"])
    return hub_list + rest


CITIES = load_cities()
CITIES_JSON = json.dumps(CITIES, separators=(",", ":"), ensure_ascii=False)

# ------------------------------------------------------------------ ESM module (NOT an f-string: literal braces are JS code)
MODULE = r"""// World Time Sync — Time Zone Converter Widget (ESM)
// Drop-in: <script type="module" src="/assets/converter-widget.mjs"></script>
//   <div data-wts-converter data-from="nyc" data-to="london"></div>
// Programmatic: import {WTSConverter} from '/assets/converter-widget.mjs'
const CITIES = __CITIES__;

function esc(t){return String(t).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}

function findCity(q){
  if(!q)return null;
  const s=String(q).trim().toLowerCase();
  for(const c of CITIES){if(c.i===s||c.n.toLowerCase()===s)return c;}
  for(const c of CITIES){if(c.n.toLowerCase().includes(s))return c;}
  return null;
}

function offsetMs(tz,instantMs){
  const f=new Intl.DateTimeFormat("en-US",{timeZone:tz,year:"numeric",month:"2-digit",day:"2-digit",hour:"2-digit",minute:"2-digit",second:"2-digit",hour12:false});
  const p={};
  for(const x of f.formatToParts(new Date(instantMs))){if(x.type!=="literal")p[x.type]=+x.value;}
  const localAsUTC=new Date(Date.UTC(p.year,p.month-1,p.day,p.hour,p.minute,p.second||0));
  return localAsUTC-instantMs;
}

// wall-clock (y,mo,d,hh,mm) in tz -> UTC instant (DST-safe probe)
function wallToUtc(y,mo,d,hh,mm,tz){
  let g=new Date(Date.UTC(y,mo-1,d,hh,mm,0));
  for(let i=0;i<10;i++){
    const f=new Intl.DateTimeFormat("en-US",{timeZone:tz,year:"numeric",month:"2-digit",day:"2-digit",hour:"2-digit",minute:"2-digit",hour12:false});
    const p={};
    for(const x of f.formatToParts(g)){if(x.type!=="literal"){p[x.type]=+x.value;}}
    const err=(p.hour*60+p.minute)-(hh*60+mm);
    if(err===0&&p.year===y&&p.month===mo&&p.day===d)break;
    g=new Date(g.getTime()-err*60000);
  }
  return g.getTime();
}

function fmtTime(instantMs,tz,h12){
  const f=new Intl.DateTimeFormat("en-US",{timeZone:tz,weekday:"short",month:"short",day:"numeric",hour:"2-digit",minute:"2-digit",hour12:h12!==false});
  return f.format(new Date(instantMs));
}

function fmtDiff(ms){
  const abs=Math.abs(ms);const h=Math.floor(abs/3600000);const m=Math.floor((abs%3600000)/60000);
  const sign=ms<0?"-":ms>0?"+":"";
  return sign+(h?h+"h ":"")+(m?m+"m":"")||"0m";
}

const CSS=`.wts-conv{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#1a1a2e;max-width:700px;margin:0 auto;padding:16px}
.wts-conv.wts-embed{padding:8px;max-width:none}
.wts-conv *{box-sizing:border-box}
.wts-card{background:#fff;border:1px solid #e5e7ea;border-radius:14px;padding:20px;box-shadow:0 4px 16px rgba(0,0,0,0.06)}
.wts-embed .wts-card{box-shadow:none;border:none;padding:0}
.wts-head{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px}
.wts-head h2{font-size:1.15rem;margin:0;letter-spacing:-0.2px}
.wts-pair{display:flex;gap:14px;align-items:flex-end}
.wts-embed .wts-pair{flex-direction:column;align-items:stretch}
.wts-side{flex:1;display:flex;flex-direction:column;gap:8px}
.wts-embed .wts-side{min-width:0}
.wts-lab{font-size:0.78rem;text-transform:uppercase;letter-spacing:0.6px;color:#6b7280}
.wts-sel{width:100%;height:44px;padding:0 12px;border:1px solid #d1d5db;border-radius:10px;background:#fff;font-size:0.95rem;color:#111}
.wts-sel:focus{border-color:#667eea;outline:none}
.wts-clock{font-size:1.75rem;font-weight:700;font-variant-numeric:tabular-nums;margin:6px 0 2px;line-height:1.2}
.wts-embed .wts-clock{font-size:1.5rem}
.wts-tz{font-size:0.85rem;color:#6b7280}
.wts-arrow{align-self:center;font-size:1.25rem;color:#667eea}
.wts-embed .wts-arrow{align-self:center;margin:6px 0}
.wts-result{margin-top:14px;padding:12px;background:#f3f4f6;border-radius:10px;text-align:center}
.wts-embed .wts-result{margin-top:10px}
.wts-diff{font-size:1.1rem;font-weight:700;color:#16213e}
.wts-diff .sign{color:#047857}
.wts-time{font-size:0.95rem;color:#4b5563;margin-top:4px}
.wts-note{font-size:0.8rem;color:#9ca3af;margin-top:6px}
.wts-actions{margin-top:14px;display:flex;gap:8px;flex-wrap:wrap}
.wts-btn{border:none;border-radius:10px;padding:8px 14px;font-size:0.88rem;font-weight:600;cursor:pointer}
.wts-btn.copy{background:#667eea;color:#fff}
.wts-btn.copy.ok{background:#047857}
.wts-btn.embed{background:#f3f4f6;color:#111}
.wts-embed .wts-actions{display:none}
.wts-embed{display:none}
.wts-code{margin-top:10px}
.wts-code textarea{width:100%;height:64px;padding:8px;border:1px solid #d1d5db;border-radius:8px;font:0.8rem ui-monospace,SFMono-Regular,Menlo,monospace;resize:vertical}
.wts-embed .wts-code{display:none}
@media(max-width:520px){.wts-pair{flex-direction:column;align-items:stretch}.wts-arrow{align-self:center;margin:8px 0}}
`;

class WTSConverter{
  constructor(root,opts={}){
    this.root=root;
    this.fromCity=opts.from?findCity(opts.from):null;
    this.toCity=opts.to?findCity(opts.to):null;
    if(!this.fromCity)this.fromCity=CITIES[0];
    if(!this.toCity||this.toCity.i===this.fromCity.i){this.toCity=CITIES.find(c=>c.i!==this.fromCity.i)||CITIES[1];}
    this.instantMs=Date.now();
    this.timer=null;
    this.embedMode=typeof window!=="undefined"&&window.self!==window.top;
    this.root.classList.add("wts-conv");
    if(this.embedMode)this.root.classList.add("wts-embed");
    this.render();
    this.start();
  }
  render(){
    const f=this.fromCity,t=this.toCity;
    const ft=fmtTime(this.instantMs,f.tz,true);
    const tt=fmtTime(this.instantMs,t.tz,true);
    const off=offsetMs(t.tz,this.instantMs)-offsetMs(f.tz,this.instantMs);
    const link="https://worldtimessync.com/converter?from="+esc(f.i)+"&to="+esc(t.i);
    const embed='<iframe src="https://worldtimessync.com/converter?from='+esc(f.i)+'&to='+esc(t.i)+'" style="border:0;width:100%;height:320px;border-radius:10px" loading="lazy" allow="clipboard-write"></iframe>';
    var fromOpts="",toOpts="";
    for(const c of CITIES){fromOpts+='<option value="'+esc(c.i)+'"'+(c.i===f.i?" selected":"")+'>'+esc(c.n)+" ("+esc(c.c)+")</option>";}
    for(const c of CITIES){toOpts+='<option value="'+esc(c.i)+'"'+(c.i===t.i?" selected":"")+'>'+esc(c.n)+" ("+esc(c.c)+")</option>";}
    const html='<style>'+CSS+'</style>'+
      '<div class="wts-card">'+
        '<div class="wts-head"><h2>Time Zone Converter</h2><span class="wts-note">World Time Sync</span></div>'+
        '<div class="wts-pair">'+
          '<div class="wts-side">'+
            '<div class="wts-lab">From</div>'+
            '<select class="wts-sel" id="wts-from">'+fromOpts+'</select>'+
            '<div class="wts-clock" id="wts-clock-from">'+ft+'</div>'+
            '<div class="wts-tz" id="wts-tz-from">'+esc(f.n+", "+f.c)+" • "+esc(f.tz)+'</div>'+
          '</div>'+
          '<div class="wts-arrow">&#8594;</div>'+
          '<div class="wts-side">'+
            '<div class="wts-lab">To</div>'+
            '<select class="wts-sel" id="wts-to">'+toOpts+'</select>'+
            '<div class="wts-clock" id="wts-clock-to">'+tt+'</div>'+
            '<div class="wts-tz" id="wts-tz-to">'+esc(t.n+", "+t.c)+" • "+esc(t.tz)+'</div>'+
          '</div>'+
        '</div>'+
        '<div class="wts-result">'+
          '<div class="wts-diff"><span class="sign">'+(off>=0?"+":"")+fmtDiff(off)+'</span> vs '+esc(f.n)+'</div>'+
          '<div class="wts-time" id="wts-diff-time">'+tt+'</div>'+
          '<div class="wts-note">Updates live • DST handled automatically</div>'+
        '</div>'+
        '<div class="wts-actions">'+
          '<button class="wts-btn copy" id="wts-copy">Copy link</button>'+
          '<button class="wts-btn embed" id="wts-embed">Embed code</button>'+
        '</div>'+
        '<div class="wts-code" id="wts-code">'+
          '<textarea readonly>&lt;iframe src="'+esc(embed)+'"&gt;&lt;/iframe&gt;</textarea>'+
        '</div>'+
      '</div>';
    this.root.innerHTML=html;
    var self=this;
    this.root.querySelector("#wts-from").addEventListener("change",function(e){self.setFrom(e.target.value);});
    this.root.querySelector("#wts-to").addEventListener("change",function(e){self.setTo(e.target.value);});
    this.root.querySelector("#wts-copy").addEventListener("click",function(){self.copy(link);});
    this.root.querySelector("#wts-embed").addEventListener("click",function(){
      var ta=self.root.querySelector("#wts-code textarea");
      ta.style.display=ta.style.display==="none"?"block":"none";
    });
  }
  setFrom(val){var c=findCity(val);if(c&&c.i!==this.toCity.i){this.fromCity=c;this.render();this.start();}}
  setTo(val){var c=findCity(val);if(c&&c.i!==this.fromCity.i){this.toCity=c;this.render();this.start();}}
  start(){if(this.timer)clearInterval(this.timer);var self=this;this.timer=setInterval(function(){self.instantMs=Date.now();self.render();},1000);}
  copy(link){if(!navigator.clipboard)return;navigator.clipboard.writeText(link).then(function(){
    var b=document.getElementById("wts-copy");if(!b)return;var old=b.textContent;b.textContent="Copied!";b.classList.add("ok");
    setTimeout(function(){b.textContent=old;b.classList.remove("ok");},1800);});
  }
}

if(typeof document!=="undefined"){
  var init=function(){
    document.querySelectorAll("[data-wts-converter]").forEach(function(el){
      if(el.dataset.wtsInit)return;el.dataset.wtsInit="1";
      new WTSConverter(el,{from:el.dataset.from,to:el.dataset.to});
    });
  };
  if(document.readyState==="loading"){document.addEventListener("DOMContentLoaded",init);}else{init();}
}

export {WTSConverter,CITIES,findCity};
"""
MODULE = MODULE.replace("__CITIES__", CITIES_JSON)

# ------------------------------------------------------------------ pages (placeholder tokens, NOT f-strings)
SCHEMA_WEBPAGE = json.dumps({"@context":"https://schema.org","@type":"WebPage"}, ensure_ascii=False)
SCHEMA_APP = json.dumps({"@context":"https://schema.org","@type":"SoftwareApplication"}, ensure_ascii=False)

CONVERTER_HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#667eea">
<meta name="google-site-verification" content="tNRYRY4K5ZdeEBPId3_g0GiclaIlooP5GhihYhXwknk">
<title>__TITLE__</title>
<meta name="title" content="__TITLE__">
<meta name="description" content="__DESC__">
<meta name="keywords" content="time zone converter, convert time zones, time difference, world clock converter, time converter">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta property="og:type" content="website">
<meta property="og:url" content="__CANON__">
<meta property="og:title" content="__TITLE__">
<meta property="og:image" content="https://worldtimessync.com/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:description" content="__DESC__">
<meta property="og:site_name" content="World Time Sync">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="__TITLE__">
<meta name="twitter:url" content="__CANON__">
<meta name="twitter:description" content="__DESC__">
<meta name="twitter:image" content="https://worldtimessync.com/og-image.png">
<meta name="twitter:image:alt" content="__TITLE__">
<meta name="twitter:creator" content="@worldtimesync">
<meta name="twitter:site" content="@worldtimesync">
<link rel="canonical" href="__CANON__">
<link rel="icon" type="image/svg+xml" href="https://worldtimessync.com/favicon.svg">
<link rel="preconnect" href="https://www.googletagmanager.com">
<link rel="preconnect" href="https://pagead.googlesyndication.com">
<link rel="dns-prefetch" href="https://www.googlesyndication.com">
<script type="application/ld+json">__SCHEMA_WEBPAGE_FULL__</script>
<script type="application/ld+json">__SCHEMA_APP_FULL__</script>
<link rel="alternate" hreflang="x-default" href="__CANON__">
<link rel="alternate" hreflang="en" href="__CANON__">
</head>
<body>
<a href="#main-content" class="skip-link">Skip to main content</a>
<main id="main-content" style="font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;max-width:700px;margin:0 auto;padding:16px">
  <header style="display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px">
    <h1 style="font-size:1.2rem;margin:0">Time Zone Converter</h1>
    <a href="/" style="font-size:0.85rem;color:#667eea">World Time Sync</a>
  </header>
  <div id="wts-converter"></div>
  <script type="module">
    import {WTSConverter} from "/assets/converter-widget.mjs";
    function getParam(n){const m=new URLSearchParams(location.search).get(n);return m||null;}
    new WTSConverter(document.getElementById("wts-converter"),{from:getParam("from"),to:getParam("to")});
  </script>
  <p style="font-size:0.85rem;color:#6b7280;margin-top:10px">Share: <code id="wts-share-url" style="word-break:break-all"></code></p>
  <footer style="margin:24px 0 8px;padding-top:14px;border-top:1px solid #e5e7ea;font-size:0.85rem;color:#6b7280">
    <a href="/privacy" style="color:#667eea;margin-right:10px">Privacy</a>
    <a href="/about" style="color:#667eea;margin-right:10px">About</a>
    <a href="/" style="color:#667eea">World Time Sync</a>
    <span style="float:right">&copy; 2026 World Time Sync</span>
  </footer>
  <script>document.getElementById("wts-share-url").textContent=location.href;</script>
  <script>window.addEventListener("load",function(){var s=document.createElement("script");s.async=true;s.src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9728257902981529";s.crossOrigin="anonymous";document.head.appendChild(s);var g=document.createElement("script");g.async=true;g.src="https://www.googletagmanager.com/gtag/js?id=G-LBX0CDYSSV";document.head.appendChild(g);var g2=document.createElement("script");g2.textContent="window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);};gtag(\"js\",new Date());gtag(\"config\",\"G-LBX0CDYSSV\");gtag(\"config\",\"G-XCBTT7YSPY\");";document.head.appendChild(g2);});</script>
</main>
</body>
</html>"""

CONVERTER_EMBED_HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, follow">
<title>__TITLE__</title>
<link rel="canonical" href="__CANON__">
<link rel="icon" type="image/svg+xml" href="https://worldtimessync.com/favicon.svg">
</head>
<body>
<div id="wts-embed"></div>
<script type="module">
  import {WTSConverter} from "/assets/converter-widget.mjs";
  function getParam(n){const m=new URLSearchParams(location.search).get(n);return m||null;}
  new WTSConverter(document.getElementById("wts-embed"),{from:getParam("from"),to:getParam("to")});
</script>
</body>
</html>"""


def fill(tpl, title, desc, canon, schema_webpage, schema_app):
    return (tpl
        .replace("__TITLE__", title)
        .replace("__DESC__", desc)
        .replace("__CANON__", canon)
        .replace("__SCHEMA_WEBPAGE_FULL__", schema_webpage)
        .replace("__SCHEMA_APP_FULL__", schema_app))


def main():
    os.makedirs(ASSETS_DIR, exist_ok=True)
    mjs_path = os.path.join(ASSETS_DIR, "converter-widget.mjs")
    with open(mjs_path, "w", encoding="utf-8") as fh:
        fh.write(MODULE)
        fh.flush(); os.fsync(fh.fileno())
    raw = len(MODULE.encode("utf-8"))
    gz = len(gzip.compress(MODULE.encode("utf-8")))
    print("Wrote %s: %d bytes raw, %d bytes gzipped (target <15360)" % (mjs_path, raw, gz))

    schema_webpage = json.dumps({"@context":"https://schema.org","@type":"WebPage","name":"Time Zone Converter — Convert Between Any Two Cities","description":"Free time zone converter: pick two cities, see the instant time difference with DST handling. Share via link or embed as an iframe.","url":"https://worldtimessync.com/converter"}, ensure_ascii=False)
    schema_app = json.dumps({"@context":"https://schema.org","@type":"SoftwareApplication","name":"World Time Sync Time Zone Converter","description":"Free online time zone converter for cities worldwide with automatic DST handling.","url":"https://worldtimessync.com/converter","applicationCategory":"UtilityApplication","operatingSystem":"Any (Web-based)","offers":{"@type":"Offer","price":"0","priceCurrency":"USD","availability":"https://schema.org/InStock"}}, ensure_ascii=False)

    title = "Time Zone Converter — Convert Between Any Two Cities"
    desc = "Free time zone converter: pick two cities, see the instant time difference with DST handling. Share via link or embed as an iframe."
    canon = "https://worldtimessync.com/converter"

    html = fill(CONVERTER_HTML, title, desc, canon, schema_webpage, schema_app)
    with open(os.path.join(ROOT, "converter.html"), "w", encoding="utf-8") as fh:
        fh.write(html); fh.flush(); os.fsync(fh.fileno())
    print("Wrote converter.html")

    embed_title = "World Time Sync Converter Embed"
    embed_canon = "https://worldtimessync.com/converter-embed"
    embed_html = fill(CONVERTER_EMBED_HTML, embed_title, "", embed_canon, "", "")
    with open(os.path.join(ROOT, "converter-embed.html"), "w", encoding="utf-8") as fh:
        fh.write(embed_html); fh.flush(); os.fsync(fh.fileno())
    print("Wrote converter-embed.html")
    print("Cities in module:", len(CITIES))

if __name__ == "__main__":
    main()
