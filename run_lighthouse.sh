#!/usr/bin/env bash
# Real Lighthouse runs against the live site. Outputs JSON + a summary.
set -e
mkdir -p lighthouse_reports
CHROME=/usr/bin/google-chrome-stable
URLS=("https://worldtimessync.com/" "https://worldtimessync.com/time/paris.html")
for u in "${URLS[@]}"; do
  out="lighthouse_reports/$(echo "$u" | sed 's#https://##; s#/#_#g; s#__#_#g').json"
  echo "=== Lighthouse: $u ==="
  npx lighthouse "$u" \
    --chrome-flags="--headless --no-sandbox --disable-gpu" \
    --chrome-path="$CHROME" \
    --only-categories=performance,accessibility,best-practices,seo \
    --output=json --output-path="$out" \
    --quiet
  echo "saved $out"
done
echo "=== SUMMARY ==="
python3 - <<'PY'
import json, glob, os
for f in sorted(glob.glob("lighthouse_reports/*.json")):
    d=json.load(open(f))
    cats=d["categories"]
    aud=d["audits"]
    def m(k):
        a=aud.get(k,{})
        return a.get("displayValue","n/a")
    print(f"\n## {os.path.basename(f)}")
    for c in ["performance","accessibility","best-practices","seo"]:
        print(f"  {c}: {round(cats[c]['score']*100)}")
    print(f"  LCP: {m('largest-contentful-paint')}")
    print(f"  FCP: {m('first-contentful-paint')}")
    print(f"  TBT: {m('total-blocking-time')}")
    print(f"  CLS: {m('cumulative-layout-shift')}")
    print(f"  SpeedIndex: {m('speed-index')}")
PY
