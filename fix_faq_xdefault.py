#!/usr/bin/env python3
"""Fix remaining issues: x-default hreflang, FAQ schema translations, and any remaining URL issues."""
from pathlib import Path
import json

BASE = Path('/home/kaliuser/worldtime')

FAQ_TRANSLATIONS = {
    'zh': {
        'q1': '如何快速查询任意城市的时间？',
        'a1': '在浏览器地址栏输入 "time in [城市]"，使用世界时钟页面，询问语音助手，或使用命令行工具如 curl wttr.in/[城市]。',
        'q2': '同时查询多个城市的最佳方式是什么？',
        'a2': '使用专门的世界时钟页面，如 worldtimessync.com/zh/，你可以固定多个城市，它们每秒自动更新。',
    },
    'it': {
        'q1': 'Come posso controllare rapidamente l\'ora in qualsiasi città?',
        'a1': 'Digita "time in [città]" nella barra degli indirizzi del browser, usa una pagina di orologio mondiale, chiedi a un assistente vocale, o usa strumenti da riga di comando come curl wttr.in/[città].',
        'q2': 'Qual è il modo migliore per controllare più città contemporaneamente?',
        'a2': 'Usa una pagina dedicata di orologio mondiale come worldtimessync.com/it/ dove puoi fissare più città e si aggiornano ogni secondo.',
    },
    'de': {
        'q1': 'Wie kann ich die Uhrzeit in einer beliebigen Stadt schnell prüfen?',
        'a1': 'Tippe "time in [Stadt]" in die Browser-Adresszeile, nutze eine Weltuhr-Seite, frage einen Sprachassistenten oder nutze Kommandozeilen-Tools wie curl wttr.in/[Stadt].',
        'q2': 'Was ist der beste Weg, mehrere Städte gleichzeitig zu prüfen?',
        'a2': 'Nutze eine dedizierte Weltuhr-Seite wie worldtimessync.com/de/, wo du mehrere Städte pinnen kannst und sie sich jede Sekunde aktualisieren.',
    },
    'fr': {
        'q1': 'Comment puis-je vérifier rapidement l\'heure dans n\'importe quelle ville ?',
        'a1': 'Tapez "time in [ville]" dans la barre d\'adresse du navigateur, utilisez une page d\'horloge mondiale, demandez à un assistant vocal, ou utilisez des outils en ligne de commande comme curl wttr.in/[ville].',
        'q2': 'Quelle est la meilleure façon de vérifier plusieurs villes à la fois ?',
        'a2': 'Utilisez une page d\'horloge mondiale dédiée comme worldtimessync.com/fr/ où vous pouvez épingler plusieurs villes et elles se mettent à jour chaque seconde.',
    },
    'pt': {
        'q1': 'Como posso verificar rapidamente a hora em qualquer cidade?',
        'a1': 'Digite "time in [cidade]" na barra de endereços do navegador, use uma página de relógio mundial, pergunte a um assistente de voz, ou use ferramentas de linha de comando como curl wttr.in/[cidade].',
        'q2': 'Qual a melhor forma de verificar várias cidades de uma vez?',
        'a2': 'Use uma página de relógio mundial dedicada como worldtimessync.com/pt/ onde você pode fixar várias cidades e elas atualizam a cada segundo.',
    },
    'ru': {
        'q1': 'Как быстро узнать время в любом городе?',
        'a1': 'Введите "time in [город]" в адресной строке браузера, используйте страницу мировых часов, спросите голосового ассистента или используйте инструменты командной строки вроде curl wttr.in/[город].',
        'q2': 'Какой лучший способ узнать время в нескольких городах сразу?',
        'a2': 'Используйте выделенную страницу мировых часов, как worldtimessync.com/ru/, где можно закрепить несколько городов и они обновляются каждую секунду.',
    },
    'ja': {
        'q1': '任意の都市の現在時刻を素早く確認する方法は？',
        'a1': 'ブラウザのアドレスバーに "time in [都市]" と入力する、世界時計ページを使う、音声アシスタントに尋ねる、または curl wttr.in/[都市] などのコマンドラインツールを使う。',
        'q2': '複数の都市を同時に確認する最善の方法は？',
        'a2': 'worldtimessync.com/ja/ のような専用の世界時計ページを使う。複数の都市をピン留めでき、毎秒自動更新される。',
    },
    'uk': {
        'q1': 'Як швидко дізнатися час у будь-якому місті?',
        'a1': 'Введіть "time in [місто]" у адресному рядку браузера, скористайтеся сторінкою світових годин, запитайте голосового асистента або скористайтеся інструментами командного рядка на кшталт curl wttr.in/[місто].',
        'q2': 'Як найкраще дізнатися час у кількох містах одночасно?',
        'a2': 'Скористайтеся виділеною сторінкою світових годин, як worldtimessync.com/uk/, де можна закріпити кілька міст і вони оновлюються кожну секунду.',
    },
    'hi': {
        'q1': 'किसी भी शहर का वर्तमान समय जल्दी कैसे जांचें?',
        'a1': 'ब्राउज़र के एड्रेस बार में "time in [शहर]" टाइप करें, वर्ल्ड क्लॉक पेज का उपयोग करें, वॉयस असिस्टेंट से पूछें, या curl wttr.in/[शहर] जैसे कमांड-लाइन टूल्स का उपयोग करें।',
        'q2': 'एक साथ कई शहरों का समय जांचने का सबसे अच्छा तरीका क्या है?',
        'a2': 'worldtimessync.com/hi/ जैसे समर्पित वर्ल्ड क्लॉक पेज का उपयोग करें जहां आप कई शहरों को पिन कर सकते हैं और वे हर सेकंड अपडेट होते हैं।',
    },
    'ar': {
        'q1': 'كيف يمكنني معرفة الوقت في أي مدينة بسرعة؟',
        'a1': 'اكتب "time in [المدينة]" في شريط عنوان المتصفح، استخدم صفحة ساعة عالمية، اسأل المساعد الصوتي، أو استخدم أدوات سطر الأوامر مثل curl wttr.in/[المدينة].',
        'q2': 'ما هي أفضل طريقة لمعرفة الوقت في عدة مدن في وقت واحد؟',
        'a2': 'استخدم صفحة ساعة عالمية مخصصة مثل worldtimessync.com/ar/ حيث يمكنك تثبيت عدة مدن وتحديثها كل ثانية.',
    },
}

BASE = Path('/home/kaliuser/worldtime')

for lang in ['zh', 'it', 'de', 'fr', 'pt', 'ru', 'ja', 'uk', 'hi', 'ar']:
    path = BASE / lang / 'blog' / f'check-current-time-any-city-{lang}.html'
    html = path.read_text(encoding='utf-8')
    
    # Fix x-default hreflang - should point to English version
    html = html.replace(
        f'href="https://worldtimessync.com/{lang}/blog/check-current-time-any-city-{lang}.html"',
        'href="https://worldtimessync.com/blog/check-current-time-any-city.html"',
        1  # Only replace the first occurrence (x-default)
    )
    
    # Fix FAQ schema - translate answers
    ft = FAQ_TRANSLATIONS.get(lang, {})
    if ft:
        # Find and replace the FAQ schema
        old_faq = '"@type": "FAQPage"'
        # Find the FAQPage block and replace it
        import re
        faq_pattern = r'({\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\".*?})'
        match = re.search(faq_pattern, html)
        if match:
            old_faq_block = match.group(1)
            # Build new FAQ block with translated content
            new_faq = f'''{{
    \"@context\": \"https://schema.org\",
    \"@type\": \"FAQPage\",
    \"mainEntity\": [
        {{
            \"@type\": \"Question\",
            \"name\": \"{ft['q1']}\",
            \"acceptedAnswer\": {{
                \"@type\": \"Answer\",
                \"text\": \"{ft['a1']}\"
            }}
        }},
        {{
            \"@type\": \"Question\",
            \"name\": \"{ft['q2']}\",
            \"acceptedAnswer\": {{
                \"@type\": \"Answer\",
                \"text\": \"{ft['a2']}\"
            }}
        }}
    ]
}}'''
            html = html.replace(old_faq_block, new_faq)
    
    path.write_text(html, encoding='utf-8')
    print(f'Fixed FAQ and x-default for {lang}')

print('Done!')