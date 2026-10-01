#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGLISH source post + writer for the "Antarctica time zones" cluster.

Run:  python3 blog/_gen_antarctica.py            # writes all available languages
      python3 blog/_gen_antarctica.py en ru      # writes only those languages

Each localized language lives in its own module next to this file
(_antarctica_es.py, _antarctica_ru.py, ...) exposing:
    META = dict(title=, desc=, kw=, date=, date_iso=, read=, tags=)
    BLOCKS = [ (kind, payload), ... ]
"""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import _antarctica_render as R

BLOG = os.path.dirname(os.path.abspath(__file__))  # .../worldtime/blog

# ---------------------------------------------------------------- English ---

META = {
    "title": "Antarctica Time Zones: The Continent With Every UTC Offset",
    "desc": ("Antarctica has no official time zone. Its research stations run on their home "
             "countries' clocks, from UTC+13 down to UTC-8. Here is how it actually works."),
    "kw": ("antarctica time zone, antarctica utc offset, research station time, "
           "south pole time zone, troll station time, amundsen-scott south pole station, "
           "vostok station time"),
    "date": "October 1, 2026",
    "date_iso": "2026-10-01",
    "read": "7 min read",
    "tags": "Time Zones, Facts, Global Work",
}

BLOCKS = [
    ("p", "Somewhere right now it is midnight at the geographic South Pole, lunchtime in "
          "Queen Maud Land, and the middle of the afternoon in the Ross Sea. All of it is "
          "the same continent, and all of it is roughly the same longitude, because "
          "Antarctica wraps all the way around the pole."),
    ("p", "That sounds impossible until you remember there are no countries down there. "
          "Antarctica has no permanent population, no borders, and no government, so there "
          "is nobody to declare an official time. What exists instead is a loose collection "
          "of research stations, each staffed and supplied by a different country, each "
          "keeping its own clock. It is the most unusual time zone situation anywhere on Earth."),

    ("h2", "Why Antarctica Has No Time Zone"),
    ("p", "The continent is governed by the Antarctic Treaty, signed in 1959. The Treaty "
          "exists to stop territorial claims and to keep the place open for peaceful "
          "research. It deliberately says nothing about time, and it does not define a "
          "single Antarctic time zone."),
    ("p", "That leaves each national programme to make its own decision. Most stations "
          "settle on something simple: use the time of the country that runs the station. "
          "A Japanese station keeps Japanese time, an Australian station keeps Australian "
          "time, a British station keeps British time. It is the least confusing rule "
          "available, because everyone already knows what their own clock says."),

    ("h2", "Stations Keep Their Home Country's Clock"),
    ("p", "Here is roughly what the big stations run on. Treat this as a snapshot rather "
          "than gospel, because station schedules do get adjusted, sometimes on short notice."),
    ("table", (
        ["Station", "Operated by", "Usual offset"],
        [
            ["Mawson", "Australia", "UTC+5"],
            ["Davis", "Australia", "UTC+7"],
            ["Casey", "Australia", "UTC+11"],
            ["Zhongshan, Great Wall", "China", "UTC+8"],
            ["Vostok", "Russia", "UTC+6 all year"],
            ["Syowa", "Japan", "UTC+3 all year"],
            ["SANAE IV", "South Africa", "UTC+2"],
            ["Neumayer III, Zucchelli", "Germany, Italy", "UTC+1"],
            ["Troll", "Norway", "UTC+0 winter, UTC+2 summer"],
            ["Palmer Station", "United States", "UTC-4"],
            ["Rothera, Halley VI", "United Kingdom", "UTC-3"],
            ["McMurdo, Scott Base", "United States, New Zealand", "UTC-8 in practice"],
            ["Amundsen-Scott (South Pole)", "United States", "UTC+12 official, UTC-8 in practice"],
        ])),
    ("p", "Read that table and you will notice the range runs from UTC+11 down to UTC-8. "
          "That is a nineteen hour spread, and it exists purely because of who supplies the "
          "fuel and who flies the staff in."),

    ("h2", "The Stations That Break the Pattern"),
    ("h3", "Troll runs on UTC, on purpose"),
    ("p", "Norway's Troll Station sits at roughly 72 degrees south, deep in Queen Maud Land. "
          "It follows Norwegian time, which means UTC+0 in winter and UTC+2 in summer, same "
          "as Oslo. In summer the crew simply does not set their clocks back. Living on pure "
          "UTC for part of the year is unusual enough that it is worth knowing about if you "
          "ever end up emailing that station."),

    ("h3", "Vostok and Syowa ignore daylight saving entirely"),
    ("p", "Vostok, run by Russia, stays on UTC+6 the whole year. Syowa, run by Japan, stays "
          "on UTC+3. Neither switches. The reason is sunlight, not politics. In the deep "
          "Antarctic winter the sun does not rise for months, so a summer time adjustment "
          "would be pure noise. Keeping a single fixed offset is simpler when the day length "
          "is swinging between endless daylight and endless dark anyway."),

    ("h3", "McMurdo and the South Pole ignore their official time"),
    ("p", "This is the one that catches people. McMurdo Station, Scott Base, and the "
          "Amundsen-Scott station at the South Pole are all officially on New Zealand time, "
          "which is UTC+12, or UTC+13 when New Zealand is in summer. In practice, almost "
          "nobody uses it. The communities at McMurdo, Scott Base, and the pole run on Pacific "
          "time, UTC-8, because that is where most of the flights, the cargo, and the "
          "scheduling come from."),
    ("p", "The South Pole case is the most striking. A station officially on UTC+12, where "
          "the local time is 20 hours ahead of Los Angeles, operating its daily life on "
          "UTC-8. If somebody tells you they are at the South Pole and quotes you a Pacific "
          "time, they are right."),

    ("h2", "What Happens at the South Pole Itself"),
    ("p", "Time zones are built on longitude, and longitude is measured by walking away from "
          "a meridian in a north or south direction. At the South Pole that is meaningless. "
          "Every direction you walk is north. Every direction is also south, from the "
          "perspective of the North Pole. There is no east and no west at all."),
    ("p", "So the geographic argument for a time zone simply does not apply. The station sits "
          "at the pole because it wants to be at the pole, for atmospheric and geophysical "
          "research, and it borrows its clock from a country 13,000 kilometres away instead. "
          "It is the clearest example on the planet that time zones are an agreement between "
          "people, not a property of the landscape."),

    ("h2", "Six Months of Day, Six Months of Night"),
    ("p", "The thing that actually shapes a day in Antarctica is not the offset, it is the "
          "light. Stations near the coast see sunrise and sunset in the summer and very "
          "little light in the winter. Crews often deliberately run on summer time for part "
          "of the season so that the working day lines up with continuous daylight, then "
          "change the clock when the sun starts setting earlier."),
    ("p", "If you are coordinating with an Antarctic programme, the offset in the table above "
          "is the least of it. What matters more is the satellite window. Stations are mostly "
          "off the internet backbone, so a phone call or a data session has to happen when a "
          "satellite is overhead. A radio contact scheduled for 14:00 might be the only "
          "reliable contact of the day. The clock matters, but the orbit matters more."),

    ("h2", "Why This Is Worth Knowing"),
    ("p", "Even if you will never set foot on the ice, Antarctica is a useful test of your "
          "time zone assumptions. It breaks three of them at once."),
    ("ul", [
        "<strong>A time zone is not tied to a country.</strong> The continent has no country, "
        "and still has a dozen different clocks.",
        "<strong>Official time is not the time people use.</strong> McMurdo, Scott Base, and "
        "the South Pole station all ignore their own official zone.",
        "<strong>DST is not universal.</strong> Half the stations never shift at all, and one "
        "shifts for a few months of the year.",
    ]),
    ("p", "It is also a good sanity check when a scheduling tool gives you a strange answer. "
          "If a converter tells you that two places are 20 hours apart, check whether one of "
          "them is in Antarctica and whether it is quoting official time or the time actually "
          "in use. A quick look at our <a href=\"/\">world clock</a> will show you the current "
          "offset for any city, which settles most arguments faster than a spreadsheet does."),

    ("h2", "The Bottom Line"),
    ("p", "Antarctica is the closest thing the planet has to a controlled experiment in time. "
          "No land rules, no national authority, no population to please, and the result is a "
          "continent covered in clocks borrowed from other continents."),
    ("p", "If you want the practical version: the offset table above is a good starting point, "
          "but for anything that matters, confirm the local time with the station rather than "
          "relying on the official designation. The people running Amundsen-Scott know better "
          "than any time zone database what their wall clock says."),
    ("p", "And if you are scheduling a call with someone, our <a href=\"/meeting-planner\">"
          "meeting planner</a> finds the overlap for you, so you do not have to do this by hand."),

    ("faq", [
        ("Does Antarctica have a time zone?",
         "No. The Antarctic Treaty does not define one, and the continent has no government or "
         "permanent population. Each research station sets its own clock, usually following the "
         "country that operates it."),
        ("What time zone does the South Pole use?",
         "Amundsen-Scott South Pole Station is officially on New Zealand time, UTC+12, or UTC+13 "
         "in New Zealand summer. In practice the station community runs on Pacific time, UTC-8, "
         "because that matches the flights and cargo it depends on."),
        ("What time is it at McMurdo Station?",
         "McMurdo is officially on New Zealand time, UTC+12, but the local community largely uses "
         "Pacific standard time, UTC-8, the same as Los Angeles in winter. It is one of the most "
         "common surprises in Antarctic time zone data."),
        ("Why do some Antarctic stations not use daylight saving time?",
         "Because the sun barely moves at those latitudes. Stations such as Vostok and Syowa keep a "
         "single fixed offset all year, since a summer time shift would make little sense when the "
         "day is already 24 hours of light or 24 hours of dark."),
        ("Can I schedule a call with an Antarctic research station?",
         "Not reliably by clock time alone. Stations depend on satellite passes for most "
         "communication, so contact windows are set by orbital passes rather than office hours. "
         "Confirm the window with the station directly."),
    ]),
]


def write(lang, meta, blocks):
    html = R.build(lang, meta, blocks)
    path = os.path.join(BLOG, R.file_for(lang))
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path, len(html)


if __name__ == "__main__":
    wanted = sys.argv[1:] or R.LANGS
    for lang in wanted:
        if lang == "en":
            meta, blocks = META, BLOCKS
        else:
            mod = importlib.import_module(f"_antarctica_{lang}")
            meta, blocks = mod.META, mod.BLOCKS
        p, n = write(lang, meta, blocks)
        print(f"wrote {os.path.relpath(p, BLOG)}  ({n:,} bytes, "
              f"{R.word_count(blocks)} words)")
