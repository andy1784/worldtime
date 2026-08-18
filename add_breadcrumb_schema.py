#!/usr/bin/env python3
"""
Add BreadcrumbList schema to localized blog posts missing it.
"""
import re
import json
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')
BLOG_DIR = BASE / 'blog'

# Posts that need localized schema added
localized_posts = [
    'best-meeting-times-remote-teams',
    'daylight-saving-2026-prep',
    'schedule-online-classes-time-zones',
    'utc-everything-guide',
    'world-clock-desk-setup',
]

langs = ['de', 'es', 'fr', 'it', 'ja', 'ru', 'uk', 'zh']

# Title mapping for each post (from English version)
post_titles = {
    'best-meeting-times-remote-teams': 'Finding the Best Meeting Time for Remote Teams (2026) | World Time Sync',
    'daylight-saving-2026-prep': 'Daylight Saving Time 2026: Dates, Changes & Preparation Guide | World Time Sync',
    'schedule-online-classes-time-zones': 'How to Schedule Online Classes Across Time Zones | World Time Sync',
    'utc-everything-guide': 'UTC Time: Everything You Need to Know | World Time Sync',
    'world-clock-desk-setup': 'World Clock Desk Setup: Stay on Time Across Time Zones | World Time Sync',
}

# Language-specific names
lang_names = {
    'de': 'Deutsch',
    'es': 'Español',
    'fr': 'Français',
    'it': 'Italiano',
    'ja': '日本語',
    'ru': 'Русский',
    'uk': 'Українська',
    'zh': '中文',
}

# Localized titles (extracted from existing pages)
localized_titles = {
    'de': {
        'best-meeting-times-remote-teams': 'Die beste Besprechungszeit für Remote-Teams finden (2026)',
        'daylight-saving-2026-prep': 'Sommerzeit 2026: Daten, Änderungen & Vorbereitungsguide',
        'schedule-online-classes-time-zones': 'Online-Kurse über Zeitzonen hinweg planen',
        'utc-everything-guide': 'UTC-Zeit: Alles, was Sie wissen müssen',
        'world-clock-desk-setup': 'Weltzeituhr-Schreibtisch-Setup: Über Zeitzonen hinweg pünktlich bleiben',
    },
    'es': {
        'best-meeting-times-remote-teams': 'Encontrar la mejor hora de reunión para equipos remotos (2026)',
        'daylight-saving-2026-prep': 'Horario de verano 2026: Fechas, cambios y guía de preparación',
        'schedule-online-classes-time-zones': 'Cómo programar clases en línea entre zonas horarias',
        'utc-everything-guide': 'Hora UTC: Todo lo que necesitas saber',
        'world-clock-desk-setup': 'Configuración de reloj mundial en el escritorio: Mantente a tiempo entre zonas horarias',
    },
    'fr': {
        'best-meeting-times-remote-teams': 'Trouver le meilleur horaire de réunion pour les équipes distantes (2026)',
        'daylight-saving-2026-prep': 'Heure d\'été 2026 : Dates, changements et guide de préparation',
        'schedule-online-classes-time-zones': 'Comment planifier des cours en ligne à travers les fuseaux horaires',
        'utc-everything-guide': 'Heure UTC : Tout ce que vous devez savoir',
        'world-clock-desk-setup': 'Configuration d\'horloge mondiale au bureau : Restez à l\'heure à travers les fuseaux horaires',
    },
    'it': {
        'best-meeting-times-remote-teams': 'Trovare il miglior orario di riunione per team remoti (2026)',
        'daylight-saving-2026-prep': 'Ora legale 2026: Date, modifiche e guida di preparazione',
        'schedule-online-classes-time-zones': 'Come programmare lezioni online tra fusi orari',
        'utc-everything-guide': 'Ora UTC: Tutto ciò che devi sapere',
        'world-clock-desk-setup': 'Configurazione orologio mondiale sulla scrivania: Resta in orario tra i fusi orari',
    },
    'ja': {
        'best-meeting-times-remote-teams': 'リモートチームの最適な会議時間を見つける (2026)',
        'daylight-saving-2026-prep': '2026年夏時間: 日程、変更、準備ガイド',
        'schedule-online-classes-time-zones': 'タイムゾーンをまたいでオンラインクラスをスケジュールする方法',
        'utc-everything-guide': 'UTC時間: 知っておくべきすべて',
        'world-clock-desk-setup': '世界時計デスクセットアップ: タイムゾーンをまたいで時間を守る',
    },
    'ru': {
        'best-meeting-times-remote-teams': 'Поиск лучшего времени встречи для удаленных команд (2026)',
        'daylight-saving-2026-prep': 'Летнее время 2026: Даты, изменения и руководство по подготовке',
        'schedule-online-classes-time-zones': 'Как планировать онлайн-уроки через часовые пояса',
        'utc-everything-guide': 'Время UTC: Все, что вам нужно знать',
        'world-clock-desk-setup': 'Мировые часы на рабочем столе: Будьте вовремя в разных часовых поясах',
    },
    'uk': {
        'best-meeting-times-remote-teams': 'Знайти найкращий час наради для віддалених команд (2026)',
        'daylight-saving-2026-prep': 'Літній час 2026: Дати, зміни та посібник із підготовки',
        'schedule-online-classes-time-zones': 'Як планувати онлайн-уроки через часові пояси',
        'utc-everything-guide': 'Час UTC: Все, що потрібно знати',
        'world-clock-desk-setup': 'Налаштування світових годинників на робочому столі: Залишайтеся вчасно в різних часових поясах',
    },
    'zh': {
        'best-meeting-times-remote-teams': '为远程团队寻找最佳会议时间 (2026)',
        'daylight-saving-2026-prep': '2026年夏令时间: 日期、变更和准备指南',
        'schedule-online-classes-time-zones': '如何跨时区安排在线课程',
        'utc-everything-guide': 'UTC时间: 您需要知道的一切',
        'world-clock-desk-setup': '世界时钟桌面设置: 跨时区保持准时',
    },
}

def generate_breadcrumb_schema(post_slug, lang):
    """Generate BreadcrumbList JSON-LD for a localized post."""
    base_slug = post_slug.replace(f'-{lang}', '')
    
    # Get localized title if available, fallback to English
    if lang in localized_titles and base_slug in localized_titles[lang]:
        title = localized_titles[lang][base_slug]
    else:
        title = post_titles.get(base_slug, 'Blog Post')
    
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://worldtimessync.com/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Blog",
                "item": "https://worldtimessync.com/#blog"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": title,
                "item": f"https://worldtimessync.com/blog/{post_slug}.html"
            }
        ]
    }
    return json.dumps(schema, ensure_ascii=False, separators=(',', ':'))

def process_file(filepath: Path) -> bool:
    """Add BreadcrumbList schema to a localized blog post."""
    try:
        html = filepath.read_text(encoding='utf-8')
        
        # Check if already has BreadcrumbList schema
        if '"@type": "BreadcrumbList"' in html:
            print(f"  SKIP (has BreadcrumbList): {filepath.name}")
            return False
        
        # Extract post slug from filename
        post_slug = filepath.stem
        
        # Extract lang from filename
        lang = post_slug.split('-')[-1]
        
        # Generate schema
        breadcrumb_json = generate_breadcrumb_schema(post_slug, lang)
        
        # Build script tag
        breadcrumb_script = f'<script type="application/ld+json">{breadcrumb_json}</script>'
        
        # Insert after existing JSON-LD scripts (before </head>)
        insert_point = '</head>'
        new_scripts = f'\n    {breadcrumb_script}\n'
        
        if insert_point in html:
            new_html = html.replace(insert_point, new_scripts + insert_point)
        else:
            print(f"  ERROR: No </head> found in {filepath.name}")
            return False
        
        if new_html != html:
            filepath.write_text(new_html, encoding='utf-8')
            print(f"  UPDATED: {filepath.name}")
            return True
        else:
            print(f"  SKIP (no change): {filepath.name}")
            return False
            
    except Exception as e:
        print(f"  ERROR: {filepath.name} - {e}")
        return False

def main():
    updated = 0
    for post in localized_posts:
        for lang in langs:
            filename = f'{post}-{lang}.html'
            filepath = BLOG_DIR / filename
            if filepath.exists():
                if process_file(filepath):
                    updated += 1
            else:
                print(f"  NOT FOUND: {filename}")
    
    print(f"\nTotal updated: {updated}")

if __name__ == '__main__':
    main()