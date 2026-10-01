#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Strict validator for the Antarctica post cluster.

For every non-English file it lists every Latin-script word appearing in the
visible article body that is not on the allowlist. That catches English leaks
in ANY script (Chinese, Japanese, Arabic, Hindi, Cyrillic) and also catches
truncated / garbled sections, which show up as stray tokens.

Usage: python3 blog/_validate_antarctica.py
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATTERN = "antarctica-time-zones-every-utc-offset*.html"

# Proper nouns, unit prefixes and roman numerals that legitimately stay Latin.
ALLOW = {
    # UTC / units
    "UTC", "PT", "M", "DST", "III", "IV", "VI", "II", "I", "V", "N", "S", "E", "W",
    # station names
    "Mawson", "Davis", "Casey", "Zhongshan", "Vostok", "Syowa", "SANAE", "Neumayer",
    "Zucchelli", "Troll", "Palmer", "Rothera", "Halley", "McMurdo", "Scott", "Base",
    "Amundsen", "Amundsen-Scott", "Mc", "Merdo", "Ro",
    # countries / places
    "Australia", "China", "Russia", "Japan", "South", "Africa", "Germany", "Italy",
    "Norway", "United", "States", "Kingdom", "New", "Zealand", "Great", "Wall",
    "Queen", "Maud", "Ross", "Antarctic", "Pole", "Los", "Angeles", "Oslo",
    "Arctic",
}


# Latin-script languages are handled by _check_antarctica.py (English-stopword
# heuristic). For these the strict "any Latin word is suspicious" rule does not
# apply, because the body is written in Latin script to begin with.
NON_LATIN = {"zh", "ja", "ru", "uk", "ar", "hi"}


def body_text(path):
    html = open(path, encoding="utf-8").read()
    m = re.search(r'<main id="main-content">(.*?)</main>', html, re.S)
    body = m.group(1) if m else ""
    body = re.sub(r"<[^>]+>", " ", body)
    # drop HTML entities (&nbsp; &middot; ...) so they are not tokenised
    body = re.sub(r"&[a-zA-Z]+;|&#\d+;", " ", body)
    return body


def main():
    files = sorted(glob.glob(os.path.join(HERE, PATTERN)))
    rc = 0
    for path in files:
        name = os.path.basename(path)
        m = re.search(r"-([a-z]{2})\.html$", name)
        lang = m.group(1) if m else "en"
        if lang not in NON_LATIN:
            continue
        text = body_text(path)
        bad = []
        for w in re.findall(r"[A-Za-z][A-Za-z'\-]*", text):
            if w in ALLOW:
                continue
            if any(part in ALLOW for part in w.split("-") if part):
                continue
            bad.append(w)
        # the replacement char is a classic sign of a mangled write
        repl = text.count("�")

        # Script check: Japanese prose is always mixed with kana; a long run of
        # kanji-only text is almost always untranslated Chinese pasted in, and
        # the mirror case (kana inside the Chinese file) is just as wrong.
        kana = re.findall(r"[\u3040-\u30ff]", text)
        han = re.findall(r"[\u4e00-\u9fff]", text)
        script = []
        if lang == "ja" and len(han) > 60 and len(kana) < 10:
            script.append("no kana but lots of han -> looks like untranslated Chinese")
        if lang == "zh" and len(kana) > 5:
            script.append("kana present in the Chinese file")

        if bad or repl or script:
            rc = 1
            print(f"  {name} [{lang}]: {sorted(set(bad))}"
                  + (f"  (+{repl} replacement chars)" if repl else "")
                  + ("  SCRIPT: " + "; ".join(script) if script else ""))
        else:
            print(f"  {name} [{lang}]: clean")
    return rc


if __name__ == "__main__":
    sys.exit(main())
