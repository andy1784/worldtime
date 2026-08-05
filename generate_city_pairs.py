#!/usr/bin/env python3
"""
Generate ~1000 city-pair landing pages for "Time in A vs B" / "Time difference A B" SEO.
Targets long-tail queries: "time difference [city1] [city2]", "meeting planner [city1] [city2]"
Uses existing 682 city database + tz database.
"""

import json
import os
from pathlib import Path
from itertools import combinations

BASE = Path('/home/kaliuser/worldtime')
OUTPUT_DIR = BASE / 'time-difference'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load city data
with open(BASE / 'cities_data.json', 'r') as f:
    CITIES = json.load(f)

# Create lookup by timezone
TZ_TO_CITIES = {}
for city in CITIES:
    tz = city['timezone']
    if tz not in TZ_TO_CITIES:
        TZ_TO_CITIES[tz] = []
    TZ_TO_CITIES[tz].append(city)

# Priority city pairs (high search volume, business relevance)
PRIORITY_PAIRS = [
    # Major financial hubs
    ('New York', 'London'),
    ('New York', 'Tokyo'),
    ('London', 'Tokyo'),
    ('New York', 'Singapore'),
    ('London', 'Singapore'),
    ('Hong Kong', 'London'),
    ('Hong Kong', 'New York'),
    ('Dubai', 'London'),
    ('Dubai', 'New York'),
    ('Frankfurt', 'London'),
    ('Frankfurt', 'New York'),
    ('Paris', 'New York'),
    ('Paris', 'Tokyo'),
    ('Zurich', 'New York'),
    ('Zurich', 'London'),
    ('Shanghai', 'London'),
    ('Shanghai', 'New York'),
    ('Sydney', 'London'),
    ('Sydney', 'New York'),
    ('Toronto', 'London'),
    ('Toronto', 'New York'),

    # US cross-country
    ('New York', 'Los Angeles'),
    ('New York', 'Chicago'),
    ('New York', 'San Francisco'),
    ('Los Angeles', 'London'),
    ('San Francisco', 'London'),
    ('Chicago', 'London'),
    ('Boston', 'London'),
    ('Washington', 'London'),

    # Europe internal
    ('London', 'Paris'),
    ('London', 'Berlin'),
    ('London', 'Frankfurt'),
    ('Paris', 'Berlin'),
    ('Paris', 'Frankfurt'),
    ('Madrid', 'London'),
    ('Milan', 'London'),
    ('Amsterdam', 'London'),
    ('Stockholm', 'London'),
    ('Copenhagen', 'London'),
    ('Vienna', 'London'),
    ('Warsaw', 'London'),

    # Asia internal
    ('Tokyo', 'Shanghai'),
    ('Tokyo', 'Seoul'),
    ('Tokyo', 'Singapore'),
    ('Tokyo', 'Hong Kong'),
    ('Singapore', 'Mumbai'),
    ('Singapore', 'Sydney'),
    ('Shanghai', 'Singapore'),
    ('Shanghai', 'Hong Kong'),
    ('Mumbai', 'Dubai'),
    ('Bangkok', 'Singapore'),
    ('Jakarta', 'Singapore'),

    # Americas
    ('São Paulo', 'New York'),
    ('Mexico City', 'New York'),
    ('Buenos Aires', 'New York'),
    ('Santiago', 'New York'),
    ('Bogotá', 'New York'),
    ('Lima', 'New York'),
    ('Toronto', 'Vancouver'),
    ('Toronto', 'Los Angeles'),
    ('Vancouver', 'Tokyo'),

    # Middle East / Africa
    ('Dubai', 'Mumbai'),
    ('Dubai', 'Riyadh'),
    ('Dubai', 'Johannesburg'),
    ('Tel Aviv', 'London'),
    ('Tel Aviv', 'New York'),
    ('Cape Town', 'London'),
    ('Lagos', 'London'),

    # Australia/NZ
    ('Sydney', 'Melbourne'),
    ('Sydney', 'Auckland'),
    ('Melbourne', 'Auckland'),
    ('Perth', 'Singapore'),
]

# Build city name -> city object lookup
CITY_BY_NAME = {c['name']: c for c in CITIES}

# Generate all valid priority pairs
valid_priority_pairs = []
for city1_name, city2_name in PRIORITY_PAIRS:
    if city1_name in CITY_BY_NAME and city2_name in CITY_BY_NAME:
        c1 = CITY_BY_NAME[city1_name]
        c2 = CITY_BY_NAME[city2_name]
        if c1['timezone'] != c2['timezone']:
            valid_priority_pairs.append((c1, c2))

print(f"Valid priority pairs: {len(valid_priority_pairs)}")

# Add more pairs algorithmically: top cities by country
# Get top 3 cities per country
from collections import defaultdict
cities_by_country = defaultdict(list)
for city in CITIES:
    cities_by_country[city['country']].append(city)

# Top countries by city count
top_countries = sorted(cities_by_country.keys(), key=lambda k: len(cities_by_country[k]), reverse=True)[:25]

# Generate cross-country pairs from top cities
algorithmic_pairs = []
for i, country1 in enumerate(top_countries):
    for country2 in top_countries[i+1:]:
        top_cities_1 = cities_by_country[country1][:3]
        top_cities_2 = cities_by_country[country2][:3]
        for c1 in top_cities_1:
            for c2 in top_cities_2:
                if c1['timezone'] != c2['timezone']:
                    # Create a sortable key to avoid duplicates
                    key = tuple(sorted([c1['name'], c2['name']]))
                    algorithmic_pairs.append((key, c1, c2))

# Deduplicate algorithmic pairs
seen = set()
unique_algorithmic = []
for key, c1, c2 in algorithmic_pairs:
    if key not in seen:
        seen.add(key)
        unique_algorithmic.append((c1, c2))

print(f"Unique algorithmic pairs: {len(unique_algorithmic)}")

# Combine: priority first, then algorithmic
all_pairs = valid_priority_pairs + unique_algorithmic[:1000 - len(valid_priority_pairs)]

# Deduplicate combined
final_pairs = []
seen_final = set()
for c1, c2 in all_pairs:
    key = tuple(sorted([c1['name'], c2['name']]))
    if key not in seen_final:
        seen_final.add(key)
        final_pairs.append((c1, c2))

print(f"Final unique pairs: {len(final_pairs)}")
# Limit to ~1000
final_pairs = final_pairs[:1000]

# Save pairs list for reference
with open(BASE / 'city_pairs_generated.json', 'w') as f:
    json.dump([
        {
            'city1': c1['name'],
            'country1': c1['country'],
            'tz1': c1['timezone'],
            'city2': c2['name'],
            'country2': c2['country'],
            'tz2': c2['timezone']
        }
        for c1, c2 in final_pairs
    ], f, indent=2)

print("Saved city_pairs_generated.json")
print(f"Ready to generate {len(final_pairs)} pages")