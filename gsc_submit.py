#!/usr/bin/env python3
"""Submit worldtimessync.com sitemap + inspect 45 new blog URLs via GSC API using a service-account JSON."""
import sys, time, json
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SITE = "https://worldtimessync.com/"
SCOPES = ["https://www.googleapis.com/auth/webmasters"]

SLUGS = [
    "schedule-online-classes-time-zones",
    "best-meeting-times-remote-teams",
    "world-clock-desk-setup",
    "daylight-saving-2026-prep",
    "utc-everything-guide",
]
LANGS = ["", "es", "zh", "ru", "it", "de", "ja", "fr", "uk"]

def all_urls():
    out = []
    for s in SLUGS:
        for l in LANGS:
            if l == "":
                out.append(f"https://worldtimessync.com/blog/{s}")
            else:
                out.append(f"https://worldtimessync.com/blog/{l}-{s}")
    return out

def main():
    if len(sys.argv) < 2:
        print("USAGE: gsc_submit.py <service-account.json>")
        sys.exit(1)
    sa_path = sys.argv[1]
    creds = service_account.Credentials.from_service_account_file(sa_path, scopes=SCOPES)
    sc = build("searchconsole", "v1", credentials=creds)

    # 1) Submit sitemap
    print("=== Submitting sitemap ===")
    try:
        sc.sitemaps().submit(siteUrl=SITE, feedpath="https://worldtimessync.com/sitemap.xml").execute()
        print("sitemap submitted OK")
    except HttpError as e:
        print("sitemap submit error:", e)

    # 2) Inspect each URL (rate-limited)
    print(f"=== Inspecting {len(all_urls())} URLs ===")
    ok = 0
    indexed = 0
    not_indexed = 0
    errors = 0
    for i, url in enumerate(all_urls(), 1):
        try:
            res = sc.urlTestingTools().inspect(method="URL_INSPECTION", body={
                "inspectionUrl": url,
                "siteUrl": SITE,
                "languageCode": "en",
            }).execute()
            verdict = res.get("inspectionResult", {}).get("indexStatusResult", {}).get("verdict", "?")
            if verdict == "INDEXED":
                indexed += 1
            else:
                not_indexed += 1
            print(f"[{i:2}] {verdict:9} {url}")
            ok += 1
        except HttpError as e:
            errors += 1
            print(f"[{i:2}] ERROR {url}: {e}")
        time.sleep(1.2)  # GSC inspection rate limit

    print(f"\n=== SUMMARY ===\ninspected={ok} indexed={indexed} not_indexed={not_indexed} errors={errors}")

if __name__ == "__main__":
    main()
