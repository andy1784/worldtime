#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check the Antarctica post cluster for untranslated English leaking through.

Only the visible <main> body is inspected (head, JSON-LD and nav labels stay
English by site convention). Single English function words are matched, minus
the words that are legitimately identical in the target language, which keeps
false positives down.

Usage: python3 blog/_check_antarctica.py
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATTERN = "antarctica-time-zones-every-utc-offset*.html"

# English words that must never survive into a translated paragraph.
ENGLISH = {
    "the", "and", "with", "which", "that", "this", "from", "have", "has", "are",
    "was", "were", "will", "would", "should", "could", "they", "their", "there",
    "where", "what", "when", "why", "how", "but", "you", "your", "our", "they",
    "people", "midday", "gospel", "somewhere", "anything", "something", "nothing",
    "someone", "everyone", "into", "about", "after", "before", "because", "while",
    "most", "more", "than", "then", "them", "these", "those", "been", "being",
    "does", "did", "each", "every", "other", "same", "first", "still", "also",
    "only", "very", "much", "many", "done", "here", "again", "once", "over",
    "under", "its", "it's", "their", "there", "not", "than",
}

# Words in the target language that collide with the English list above.
# Keep this short: it only needs the genuine intersections.
LANG_OK = {
    "de": {"was", "will", "also", "hat", "ist", "man", "so", "die", "das", "in",
           "an", "am", "und", "oder", "aber", "mit", "von", "für", "auf", "nicht",
           "nur", "noch", "schon", "wenn", "dann", "wie", "wo", "wer", "war",
           "waren", "werden", "kann", "muss", "soll", "mehr", "wir", "sie", "er",
           "es", "am", "zum", "zur", "im", "zum", "seit", "ohne", "durch", "über"},
    "fr": {"est", "sont", "ont", "une", "des", "les", "du", "la", "le", "au",
           "aux", "en", "sur", "pour", "par", "dans", "avec", "ne", "pas", "plus",
           "que", "qui", "son", "ses", "leur", "il", "elle", "nous", "vous",
           "ils", "elles", "est", "ont", "fait", "peut", "très", "bien", "tout",
           "tous", "cette", "même", "si", "se", "sa", "son", "ce", "de", "du"},
    "es": {"el", "la", "los", "las", "un", "una", "de", "del", "en", "por",
           "para", "con", "sin", "sobre", "entre", "es", "son", "está", "este",
           "esta", "esto", "eso", "su", "sus", "se", "lo", "al", "y", "o", "no",
           "más", "muy", "todo", "todos", "cada", "cual", "cuando", "donde",
           "porque", "pero", "si", "ya", "ha", "han", "fue", "ser", "estar"},
    "it": {"il", "lo", "la", "i", "gli", "le", "un", "una", "di", "del", "della",
           "in", "a", "da", "con", "su", "per", "tra", "è", "sono", "stato",
           "non", "più", "molto", "anche", "come", "quando", "dove", "perché",
           "ma", "se", "già", "ha", "hanno", "essere", "stare", "questo", "quella",
           "ogni", "tutto", "tutti", "c'è", "cioè", "cui", "loro", "sua", "suo"},
    "pt": {"o", "a", "os", "as", "um", "uma", "de", "do", "da", "em", "no", "na",
           "nos", "nas", "por", "para", "com", "sem", "sobre", "entre", "é", "são",
           "este", "esta", "isso", "isto", "aquele", "seu", "sua", "se", "não",
           "mais", "muito", "também", "como", "quando", "onde", "porque", "mas",
           "se", "já", "há", "foi", "ser", "estar", "todo", "todos", "cada"},
}


def main():
    files = sorted(glob.glob(os.path.join(HERE, PATTERN)))
    if not files:
        print("no files found")
        return 1
    bad = 0
    for path in files:
        name = os.path.basename(path)
        m = re.search(r"-([a-z]{2})\.html$", name)
        lang = m.group(1) if m else "en"
        if lang == "en":
            print(f"  {name} [en]: (source language, skipped)")
            continue
        html = open(path, encoding="utf-8").read()
        body = re.search(r'<main id="main-content">(.*?)</main>', html, re.S)
        body = body.group(1) if body else ""
        text = re.sub(r"<[^>]+>", " ", body)

        ok = LANG_OK.get(lang, set())
        found = set()
        for w in re.findall(r"[A-Za-z][a-z']+", text):
            if w.lower() in ENGLISH and w.lower() not in ok and w not in ok:
                found.add(w)
        if found:
            bad += 1
            print(f"  {name} [{lang}]: LEAK -> {sorted(found)}")
        else:
            print(f"  {name} [{lang}]: clean")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
