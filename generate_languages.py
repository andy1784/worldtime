#!/usr/bin/env python3
"""Generate French (fr) and Ukrainian (uk) language pages from English templates."""

import os
import re
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Translation dictionaries
FR = {
    "lang_code": "fr",
    "lang_name": "Français",
    "lang_label": "FR",
    "lang_full": "French",
    # Navigation
    "nav_home": "Accueil",
    "nav_about": "À propos",
    "nav_contact": "Contact",
    "nav_privacy": "Politique de confidentialité",
    "nav_terms": "Conditions d'utilisation",
    "nav_world_clock": "Horloge mondiale",
    # Common UI
    "loading": "Chargement...",
    "copy_time": "Copier l'heure",
    "current_time_in": "Heure actuelle à",
    "what_time_is": "Quelle heure est-il à",
    "time_zone": "Fuseau horaire",
    "utc_offset": "Décalage UTC",
    "daylight_saving": "Heure d'été",
    "yes": "Oui",
    "no": "Non",
    "skip_to_content": "Aller au contenu principal",
    # City page sections
    "about": "À propos de",
    "timezone_details": "Détails du fuseau horaire",
    "iana_timezone": "Fuseau horaire IANA",
    "convert_time": "Convertir l'heure",
    "convert_desc": "Pour convertir l'heure de {city} à votre heure locale, utilisez notre convertisseur de fuseaux horaires gratuit sur la page d'accueil.",
    "frequently_asked": "Questions fréquentes",
    "popular_cities": "Villes populaires dans le même fuseau horaire",
    "nearby_timezones": "Fuseaux horaires à proximité",
    "countries_in_tz": "Pays dans ce fuseau horaire",
    "all_cities_in": "Toutes les villes en",
    "save_page": "Enregistrez cette page pour accéder rapidement à l'heure actuelle à {city}. L'horloge en direct n'a jamais besoin d'être actualisée manuellement.",
    # FAQ templates
    "faq_what_time": "Quelle heure est-il maintenant à {city} ?",
    "faq_what_time_answer": "L'heure actuelle à {city} est affichée dans l'horloge en direct ci-dessus. {city} suit le fuseau horaria {tz}.",
    "faq_dst": "{city} observe-t-il l'heure d'été ?",
    "faq_dst_yes": "Oui, {city} observe l'heure d'été. Les horloges avancent d'une heure au printemps et reculent d'une heure en automne.",
    "faq_utc_offset": "Quel est le décalage UTC de {city} ?",
    "faq_convert": "Comment convertir l'heure de {city} en mon fuseau horaire ?",
    "faq_convert_answer": "Utilisez notre convertisseur gratuit de fuseaux horaires pour convertir entre l'heure de {city} et votre heure locale.",
    "faq_difference": "Quelle est la différence horaire entre {city} et d'autres grandes villes ?",
    "faq_difference_answer": "La différence horaire dépend du fuseau horaire de l'autre ville et des règles d'heure d'été. Visitez notre horloge mondiale pour comparer {city} avec des centaines d'autres villes.",
    "faq_same_year": "L'heure de {city} est-elle la même toute l'année ?",
    "faq_same_year_answer": "Non, {city} change les horloges deux fois par an en raison de l'heure d'été.",
    # SEO content
    "seo_current_time": "Heure actuelle à {city}",
    "seo_live_desc": "Vous devez connaître l'heure locale exacte à {city} en ce moment ? L'horloge en direct ci-dessus se met à jour chaque seconde, vous montrant l'heure précise actuelle à {city}.",
    "seo_timezone_info": "L'heure à {city} suit le fuseau horaire {tz}. Comprendre le fuseau horaire local est essentiel pour éviter les erreurs de planification.",
    "quick_reference": "Référence rapide : Heure à {city}",
    "local_time": "Heure locale actuelle",
    "country": "Pays",
    # Index page
    "hero_title": "Horloge mondiale — Quelle heure est-il à {cities} ?",
    "hero_desc": "Quelle heure est-il maintenant ? Consultez l'heure locale actuelle dans plus de 700 villes du monde entier. Horloge mondiale gratuite avec convertisseur de fuseaux horaires.",
    "popular_cities_title": "Villes populaires et heures actuelles",
    "popular_cities_desc": "Consultez l'heure actuelle dans les grandes villes du monde. Cliquez sur une ville pour voir les détails.",
    "features_title": "Fonctionnalités de World Time Online",
    "features_desc": "Notre horloge mondiale offre : mises à jour en temps réel pour plus de 700 villes, convertisseur de fuseaux horaires précis, prise en charge de l'heure d'été, design responsive.",
    "understanding_title": "Comprendre les fuseaux horaires",
    "understanding_desc": "Les fuseaux horaires sont des régions de la Terre qui observent une heure standard uniforme. Le monde est divisé en 24 fuseaux horaires basés sur le UTC.",
    "what_time_title": "Quelle heure est-il maintenant ?",
    "what_time_desc": "Utilisez World Time Online pour découvrir l'heure actuelle dans l'une des plus de 700 villes prises en charge.",
    # Footer
    "footer_copyright": "© 2026 World Time Sync. Tous droits réservés.",
}

UK = {
    "lang_code": "uk",
    "lang_name": "Українська",
    "lang_label": "UK",
    "lang_full": "Ukrainian",
    # Navigation
    "nav_home": "Головна",
    "nav_about": "Про нас",
    "nav_contact": "Контакти",
    "nav_privacy": "Політика конфіденційності",
    "nav_terms": "Умови використання",
    "nav_world_clock": "Світовий годинник",
    # Common UI
    "loading": "Завантаження...",
    "copy_time": "Копіювати час",
    "current_time_in": "Поточний час у",
    "what_time_is": "Котра година у",
    "time_zone": "Часовий пояс",
    "utc_offset": "Зсув UTC",
    "daylight_saving": "Літній час",
    "yes": "Так",
    "no": "Ні",
    "skip_to_content": "Перейти до вмісту",
    # City page sections
    "about": "Про",
    "timezone_details": "Деталі часового поясу",
    "iana_timezone": "Часовий пояс IANA",
    "convert_time": "Перевести час",
    "convert_desc": "Щоб перевести час {city} на ваш місцевий час, скористайтеся нашим безкоштовним конвертером часових поясів на головній сторінці.",
    "frequently_asked": "Часті запитання",
    "popular_cities": "Популярні міста в тому ж часовому поясі",
    "nearby_timezones": "Сусідні часові пояси",
    "countries_in_tz": "Країни в цьому часовому поясі",
    "all_cities_in": "Усі міста в",
    "save_page": "Збережіть цю сторінку для швидкого доступу до поточного часу в {city}. Живий годинник ніколи не потребує оновлення вручну.",
    # FAQ templates
    "faq_what_time": "Котра година зараз у {city}?",
    "faq_what_time_answer": "Поточний час у {city} відображається на живому годиннику вище. {city} використовує часовий пояс {tz}.",
    "faq_dst": "Чи {city} переходить на літній час?",
    "faq_dst_yes": "Так, {city} переходить на літній годинник. Годинники переводяться на 1 годину вперед навесні та на 1 годину назад восени.",
    "faq_utc_offset": "Який зсув UTC у {city}?",
    "faq_convert": "Як перевести час {city} на мій часовий пояс?",
    "faq_convert_answer": "Скористайтеся нашим безкоштовним конвертером часових поясів для конвертації між часом {city} та вашим місцевим часом.",
    "faq_difference": "Яка різниця в часі між {city} та іншими великими містами?",
    "faq_difference_answer": "Різниця в часі залежить від часового поясу іншого міста та правил літнього часу. Відвідайте наш світовий годинник, щоб порівняти {city} з іншими містами.",
    "faq_same_year": "Чи час у {city} однаковий протягом усього року?",
    "faq_same_year_answer": "Ні, {city} переводить годинники двічі на рік через літній час.",
    # SEO content
    "seo_current_time": "Поточний час у {city}",
    "seo_live_desc": "Потрібно знати точний місцевий час у {city} зараз? Живий годинник вище оновлюється щосекунди, показуючи точний поточний час у {city}.",
    "seo_timezone_info": "Час у {city} відповідає часовому поясу {tz}. Розуміння місцевого часового поясу необхідне для уникнення помилок планування.",
    "quick_reference": "Швидка довідка: Час у {city}",
    "local_time": "Поточний місцевий час",
    "country": "Країна",
    # Index page
    "hero_title": "Світовий годинник — Котра година у {cities}?",
    "hero_desc": "Котра година зараз? Перегляньте поточний місцевий час у понад 700 містах світу. Безкоштовний світовий годинник з конвертером часових поясів.",
    "popular_cities_title": "Популярні міста та поточний час",
    "popular_cities_desc": "Перегляньте поточний час у великих містах світу. Натисніть на місто, щоб побачити деталі.",
    "features_title": "Можливості World Time Online",
    "features_desc": "Наш світовий годинник пропонує: оновлення в реальному часі для понад 700 міст, точний конвертер часових поясів, підтримку літнього часу.",
    "understanding_title": "Розуміння часових поясів",
    "understanding_desc": "Часові пояси — це регіони Землі, які дотримуються єдиного стандартного часу. Світ поділено на 24 часових пояси на основі UTC.",
    "what_time_title": "Котра година зараз?",
    "what_time_desc": "Використовуйте World Time Online, щоб дізнатися поточний час в одному з понад 700 підтримуваних міст.",
    # Footer
    "footer_copyright": "© 2026 World Time Sync. Усі права захищені.",
}

# Language switcher templates
LANG_BAR_FR = '<div class="lang-bar"><span>🌐</span><a href="/fr/">EN</a><a href="/es/">ES</a><a href="/zh/">中文</a><a href="/ru/">RU</a><a href="/it/">IT</a><a href="/de/">DE</a><a href="/ja/">日本語</a><a href="/fr/" class="active">FR</a><a href="/uk/">UA</a></div>'
LANG_BAR_UK = '<div class="lang-bar"><span>🌐</span><a href="/uk/">EN</a><a href="/es/">ES</a><a href="/zh/">中文</a><a href="/ru/">RU</a><a href="/it/">IT</a><a href="/de/">DE</a><a href="/ja/">日本語</a><a href="/fr/">FR</a><a href="/uk/" class="active">UA</a></div>'

# Hreflang tags
HREFLANG_FR = '    <link rel="alternate" hreflang="fr" href="https://worldtimessync.com/fr/{path}" />\n'
HREFLANG_UK = '    <link rel="alternate" hreflang="uk" href="https://worldtimessync.com/uk/{path}" />\n'


def translate_city_page(en_content, lang_dict, lang_code):
    """Translate an English city page to target language."""
    t = lang_dict
    content = en_content

    # Replace lang attribute
    content = content.replace('<html lang="en">', f'<html lang="{t["lang_code"]}">')

    # Replace skip link
    content = content.replace('Skip to main content', t["skip_to_content"])

    # Replace copy time button
    content = content.replace('Copy time', t["copy_time"])

    # Replace "Loading..." in live-time element
    content = content.replace('>Loading...</p', f'>{t["loading"]}</p')

    # Replace breadcrumb "Home"
    content = re.sub(
        r'<a href="/">Home</a> &gt;',
        f'<a href="/{t["lang_code"]}/">{t["nav_home"]}</a> &gt;',
        content
    )

    # Replace breadcrumb on city pages (English uses /time/ prefix)
    content = re.sub(
        r'<a href="/time/[^"]*">Home</a>',
        f'<a href="/{t["lang_code"]}/">{t["nav_home"]}</a>',
        content
    )

    # Replace "Frequently Asked Questions"
    content = content.replace('Frequently Asked Questions', t["frequently_asked"])
    content = content.replace('Frequently asked questions', t["frequently_asked"])

    # Replace "Popular Cities in the Same Time Zone"
    content = content.replace('Popular Cities in the Same Time Zone', t["popular_cities"])

    # Replace "Nearby Time Zones"
    content = content.replace('Nearby Time Zones', t["nearby_timezones"])

    # Replace "Countries in This Time Zone"
    content = content.replace('Countries in This Time Zone', t["countries_in_tz"])

    # Replace footer links
    content = content.replace('Privacy Policy', t["nav_privacy"])
    content = content.replace('About', t["nav_about"])
    content = content.replace('>Home<', f'>{t["nav_home"]}<')
    content = content.replace('All rights reserved.', 'Tous droits réservés.' if lang_code == 'fr' else 'Усі права захищені.')

    # Replace copyright
    content = re.sub(
        r'© 2026 World Time Sync\. All rights reserved\.',
        t["footer_copyright"],
        content
    )

    # Replace Intl.DateTimeFormat locale
    content = content.replace('Intl.DateTimeFormat("en"', f'Intl.DateTimeFormat("{t["lang_code"]}"')

    # Replace internal links from /time/ to /{lang}/time/
    content = re.sub(r'href="/time/', f'href="/{t["lang_code"]}/time/', content)
    content = re.sub(r"href='/time/", f"href='/{t['lang_code']}/time/", content)

    # Replace internal links from / to /{lang}/
    content = re.sub(r'href="/"', f'href="/{t["lang_code"]}/"', content)

    # Replace "Loading..." in script fallback
    content = content.replace('"Loading..."', f'"{t["loading"]}"')
    content = content.replace("'Loading...'", f"'{t['loading']}'")

    # Replace "About {city}" section headers
    content = re.sub(
        r'<h2>About ([^<]+)</h2>',
        f'<h2>{t["about"]} \\1</h2>',
        content
    )

    # Replace "Time Zone Details"
    content = content.replace('Time Zone Details', t["timezone_details"])
    content = content.replace('IANA Time Zone', t["iana_timezone"])
    content = content.replace('UTC Offset', t["utc_offset"])
    content = content.replace('Daylight Saving', t["daylight_saving"])

    # Replace "Convert Time" section
    content = content.replace('Convert Time', t["convert_time"])

    # Replace "Quick Reference"
    content = content.replace('Quick Reference', t["quick_reference"])
    content = content.replace('Current Local Time', t["local_time"])

    # Replace FAQ questions
    content = re.sub(
        r'What time is it in ([^?]+)\?',
        lambda m: t["faq_what_time"].replace("{city}", m.group(1)),
        content
    )
    content = re.sub(
        r'Does ([^?]+) observe daylight saving\?',
        lambda m: t["faq_dst"].replace("{city}", m.group(1)),
        content
    )
    content = re.sub(
        r'What is the UTC offset for ([^?]+)\?',
        lambda m: t["faq_utc_offset"].replace("{city}", m.group(1)),
        content
    )
    content = re.sub(
        r'How do I convert ([^?]+) time to my time zone\?',
        lambda m: t["faq_convert"].replace("{city}", m.group(1)),
        content
    )
    content = re.sub(
        r'What is the time difference between ([^?]+) and other major cities\?',
        lambda m: t["faq_difference"].replace("{city}", m.group(1)),
        content
    )
    content = re.sub(
        r'Is ([^?]+) time the same all year round\?',
        lambda m: t["faq_same_year"].replace("{city}", m.group(1)),
        content
    )

    # Replace SEO headings
    content = re.sub(
        r'What time is it now in ([^,?]+)',
        lambda m: t["what_time_is"] + " " + m.group(1),
        content
    )

    # Replace meta title and description patterns
    content = re.sub(
        r'<title>([^<]+) — What Time Is It\?</title>',
        lambda m: f'<title>{m.group(1)} — {"Quelle heure est-il?" if lang_code == "fr" else "Котра година?"} | World Time Sync</title>',
        content
    )

    # Replace "Country" label
    content = content.replace('>Country<', f'>{t["country"]}<')

    # Replace "All Cities in" for country links
    content = re.sub(
        r'<h2><a href="/[^/]+/country/([^"]+)">All Cities in ([^<]+)</a></h2>',
        lambda m: f'<h2><a href="/{t["lang_code"]}/country/{m.group(1)}">{t["all_cities_in"]} {m.group(2)}</a></h2>',
        content
    )

    return content


def translate_index_page(en_content, lang_dict):
    """Translate the English index page to target language."""
    t = lang_dict
    content = en_content

    # Replace lang
    content = content.replace('<html lang="en">', f'<html lang="{t["lang_code"]}">')

    # Replace title
    content = re.sub(
        r'<title>[^<]+</title>',
        f'<title>{"Horloge mondiale — Quelle heure est-il?" if t["lang_code"] == "fr" else "Світовий годинник — Котра година?"} | World Time Sync</title>',
        content
    )

    # Replace skip link
    content = content.replace('Skip to main content', t["skip_to_content"])

    # Replace breadcrumb
    content = content.replace('>Home</a> &gt; World Clock', f'>{t["nav_home"]}</a> &gt; {t["nav_world_clock"]}')

    # Replace h1
    content = re.sub(
        r'<h1>[^<]+</h1>',
        f'<h1>{"Horloge mondiale — gratuit pour plus de 700 villes" if t["lang_code"] == "fr" else "Світовий годинник — безкоштовно для понад 700 міст"}</h1>',
        content,
        count=1
    )

    # Replace FAQ heading
    content = content.replace('Frequently Asked Questions', t["frequently_asked"])

    # Replace footer
    content = re.sub(
        r'© 2026 World Time Sync\. All rights reserved\.',
        t["footer_copyright"],
        content
    )

    # Replace Intl locale
    content = content.replace('Intl.DateTimeFormat("en"', f'Intl.DateTimeFormat("{t["lang_code"]}"')

    # Replace internal links
    content = re.sub(r'href="/time/', f'href="/{t["lang_code"]}/time/', content)
    content = re.sub(r'href="/"', f'href="/{t["lang_code"]}/"', content)
    content = re.sub(r'href="/meeting-planner.html"', f'href="/{t["lang_code"]}/meeting-planner.html"', content)

    return content


def add_hreflang(content, lang_code):
    """Add fr and uk hreflang tags to a page."""
    # Find the last hreflang tag and add after it
    last_hreflang = re.search(r'(<link rel="alternate" hreflang="ja"[^>]*>)', content)
    if last_hreflang:
        insert_pos = last_hreflang.end()
        new_tags = f'\n{HREFLANG_FR.format(path="")}\n{HREFLANG_UK.format(path="")}'
        if lang_code == 'fr':
            new_tags = f'\n{HREFLANG_UK.format(path="")}'
        elif lang_code == 'uk':
            new_tags = f'\n{HREFLANG_FR.format(path="")}'
        content = content[:insert_pos] + new_tags + content[insert_pos:]
    return content


def add_lang_bar_links(content, lang_code):
    """Add fr and uk links to existing lang-bar."""
    # Find the lang-bar and add new links before closing </div>
    # For existing language pages, add fr and uk links
    if lang_code in ('es', 'zh', 'ru', 'it', 'de', 'ja'):
        # Add FR and UK links to the lang-bar
        # Find the last </a> before </div> in lang-bar
        match = re.search(
            r'(<div class="lang-bar">.*?)(</div>)',
            content,
            re.DOTALL
        )
        if match:
            lang_bar = match.group(1)
            if '/fr/' not in lang_bar:
                lang_bar += f'<a href="/fr/">FR</a><a href="/uk/">UA</a>'
            content = content[:match.start()] + lang_bar + match.group(2) + content[match.end():]
    elif lang_code == 'en':
        # Add to English root page
        match = re.search(
            r'(<div class="lang-bar">.*?)(</div>)',
            content,
            re.DOTALL
        )
        if match:
            lang_bar = match.group(1)
            if '/fr/' not in lang_bar:
                lang_bar += f'<a href="/fr/">Français</a><a href="/uk/">Українська</a>'
            content = content[:match.start()] + lang_bar + match.group(2) + content[match.end():]
    return content


def generate_city_pages(lang_dict, lang_code):
    """Generate all city pages for a language."""
    en_time_dir = os.path.join(BASE_DIR, 'time')
    out_dir = os.path.join(BASE_DIR, lang_code, 'time')
    os.makedirs(out_dir, exist_ok=True)

    count = 0
    for filename in sorted(os.listdir(en_time_dir)):
        if not filename.endswith('.html'):
            continue
        en_path = os.path.join(en_time_dir, filename)
        out_path = os.path.join(out_dir, filename)

        with open(en_path, 'r', encoding='utf-8') as f:
            en_content = f.read()

        translated = translate_city_page(en_content, lang_dict, lang_code)

        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(translated)

        count += 1
        if count % 100 == 0:
            print(f"  Generated {count} city pages...")

    print(f"  Total: {count} city pages generated in /{lang_code}/time/")
    return count


def generate_core_pages(lang_dict, lang_code):
    """Generate core pages (index, about, contact, privacy, terms)."""
    # Copy and translate from English templates
    pages = {
        'index.html': 'index.html',
        'about.html': 'about.html',
        'contact.html': 'contact.html',
        'privacy.html': 'privacy.html',
        'terms.html': 'terms.html',
    }

    os.makedirs(os.path.join(BASE_DIR, lang_code), exist_ok=True)

    for en_name, out_name in pages.items():
        en_path = os.path.join(BASE_DIR, en_name)
        if not os.path.exists(en_path):
            print(f"  Warning: {en_name} not found, skipping")
            continue

        with open(en_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Basic translations for core pages
        content = content.replace('<html lang="en">', f'<html lang="{lang_code}">')
        content = content.replace('Skip to main content', lang_dict["skip_to_content"])
        content = content.replace('Frequently Asked Questions', lang_dict["frequently_asked"])

        # Replace hreflang - add fr and uk
        content = add_hreflang(content, lang_code)

        # Add lang-bar links for fr and uk
        if lang_code == 'fr':
            content = content.replace(
                '</head>',
                '    <link rel="alternate" hreflang="uk" href="https://worldtimessync.com/uk/' + ('' if out_name == 'index.html' else out_name) + '" />\n</head>'
            )
        elif lang_code == 'uk':
            content = content.replace(
                '</head>',
                '    <link rel="alternate" hreflang="fr" href="https://worldtimessync.com/fr/' + ('' if out_name == 'index.html' else out_name) + '" />\n</head>'
            )

        out_path = os.path.join(BASE_DIR, lang_code, out_name)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  Generated: /{lang_code}/{out_name}")


def update_existing_pages():
    """Update all existing pages with fr/uk hreflang and lang-bar links."""
    print("\nUpdating existing pages with fr/uk links...")

    # Hreflang tags to add
    fr_hreflang = '    <link rel="alternate" hreflang="fr" href="https://worldtimessync.com/fr/{path}" />\n'
    uk_hreflang = '    <link rel="alternate" hreflang="uk" href="https://worldtimessync.com/uk/{path}" />\n'

    # Lang-bar links to add
    fr_uk_links = '<a href="/fr/">Français</a><a href="/uk/">Українська</a>'
    fr_uk_links_short = '<a href="/fr/">FR</a><a href="/uk/">UA</a>'

    count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip the new fr/ and uk/ directories
        rel = os.path.relpath(root, BASE_DIR)
        if rel.startswith('fr') or rel.startswith('uk'):
            continue
        # Skip hidden dirs and node_modules
        if any(d.startswith('.') or d == 'node_modules' for d in rel.split(os.sep)):
            continue

        for filename in files:
            if not filename.endswith('.html'):
                continue

            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue

            modified = False

            # Add hreflang tags if not present
            if 'hreflang="fr"' not in content:
                # Find last hreflang tag
                match = re.search(r'(<link rel="alternate" hreflang="ja"[^>]*>)', content)
                if match:
                    pos = match.end()
                    # Determine the path for this page
                    rel_path = os.path.relpath(filepath, BASE_DIR)
                    if rel_path == 'index.html':
                        page_path = ''
                    else:
                        page_path = rel_path.replace('.html', '')

                    new_tags = fr_hreflang.format(path=page_path) + uk_hreflang.format(path=page_path)
                    content = content[:pos] + '\n' + new_tags + content[pos:]
                    modified = True

            # Add lang-bar links if not present
            if '/fr/' not in content and 'lang-bar' in content:
                # Determine which lang-bar format to use
                is_root = os.path.relpath(filepath, BASE_DIR) in ('index.html',)
                is_lang_dir = any(
                    os.path.relpath(filepath, BASE_DIR).startswith(d + '/')
                    for d in ('es', 'zh', 'ru', 'it', 'de', 'ja')
                )

                if is_root:
                    # Root English page - add full names
                    links_to_add = fr_uk_links
                elif is_lang_dir:
                    # Language subdirectory page - add short labels
                    links_to_add = fr_uk_links_short
                else:
                    continue

                # Find the lang-bar and add links
                match = re.search(
                    r'(<div[^>]*class="lang-bar"[^>]*>.*?)(</div>)',
                    content,
                    re.DOTALL
                )
                if match:
                    lang_bar = match.group(1)
                    if links_to_add not in lang_bar:
                        lang_bar += links_to_add
                        content = content[:match.start()] + lang_bar + match.group(2) + content[match.end():]
                        modified = True

            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1

    print(f"  Updated {count} existing pages")


def main():
    print("=" * 60)
    print("Generating French (fr) and Ukrainian (uk) pages")
    print("=" * 60)

    # Generate French pages
    print("\n--- French (fr) ---")
    generate_core_pages(FR, 'fr')
    generate_city_pages(FR, 'fr')

    # Generate Ukrainian pages
    print("\n--- Ukrainian (uk) ---")
    generate_core_pages(UK, 'uk')
    generate_city_pages(UK, 'uk')

    # Update all existing pages
    update_existing_pages()

    print("\n" + "=" * 60)
    print("Done! Generated fr/ and uk/ directories")
    print("=" * 60)


if __name__ == '__main__':
    main()
