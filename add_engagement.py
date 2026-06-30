#!/usr/bin/env python3
"""Add engagement widgets to all city pages using .replace() not .format()"""
import re, os, json
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')

NEW_CSS = """
.minute-progress{width:100%;height:4px;background:rgba(255,255,255,0.2);border-radius:2px;margin-top:10px;overflow:hidden}
.minute-progress-bar{height:100%;background:rgba(255,255,255,0.8);border-radius:2px;transition:width 1s linear}
.copy-time-btn{display:inline-block;margin-top:10px;padding:6px 16px;background:rgba(255,255,255,0.15);color:#fff;border:1px solid rgba(255,255,255,0.3);border-radius:6px;cursor:pointer;font-size:0.85rem;transition:background 0.2s}
.copy-time-btn:hover{background:rgba(255,255,255,0.25)}
.copy-time-btn:active{background:rgba(255,255,255,0.35)}
.lsi-block{background:#fff;padding:clamp(16px,4vw,24px);border-radius:8px;margin:16px 0;box-shadow:0 1px 3px rgba(0,0,0,0.1)}
.lsi-block h2{margin-top:0;color:#16213e;font-size:clamp(1.1rem,3vw,1.3rem)}
.lsi-block p{color:#333;line-height:1.7;margin:8px 0}
.lsi-block ul{padding-left:20px;margin:8px 0}
.lsi-block li{margin:4px 0;color:#333}
.lsi-block a{color:#667eea;text-decoration:none}
.lsi-block a:hover{text-decoration:underline}
"""

COPY_LABELS = {
    'en': 'Copy time', 'es': 'Copiar hora', 'zh': '复制时间',
    'ru': 'Копировать время', 'it': 'Copia ora', 'de': 'Zeit kopieren', 'ja': '時刻をコピー',
}
COPIED_LABELS = {
    'en': 'Copied!', 'es': '¡Copiado!', 'zh': '已复制！',
    'ru': 'Скопировано!', 'it': 'Copiato!', 'de': 'Kopiert!', 'ja': 'コピー済み！',
}

# LSI block templates using %%PLACEHOLDER%% to avoid format issues
LSI_TEMPLATES = {
'en': '''<section class="lsi-block" aria-label="Current time details">
<h2>What's the Current Time in %%CITY%%, %%COUNTRY%%?</h2>
<p>Need to know the exact local time in %%CITY%% right now? The live clock above updates every second, showing you the precise current time in %%CITY%%, %%COUNTRY%%. Whether you're scheduling a meeting with colleagues in %%CITY%%, planning a trip, or coordinating across time zones, this page gives you real-time information you can rely on.</p>
<p>The time in %%CITY%% follows the <strong>%%TZ%%</strong> time zone. This means %%CITY%% is currently <strong>%%UTC%%</strong>. Understanding the local time zone is essential for avoiding scheduling mistakes and ensuring smooth communication with contacts in %%COUNTRY%%.</p>
<h3>Quick Reference: %%CITY%% Time</h3>
<ul>
<li><strong>Current local time:</strong> displayed live above</li>
<li><strong>Time zone:</strong> %%TZ%%</li>
<li><strong>UTC offset:</strong> %%UTC%%</li>
<li><strong>Country:</strong> %%COUNTRY%%</li>
</ul>
<p>Bookmark this page for quick access to the current time in %%CITY%%. The live clock never needs refreshing — it updates automatically. You can also use our <a href="/">time zone converter</a> to compare %%CITY%% time with any other city in the world, or check the <a href="/meeting-planner.html">Meeting Planner</a> to find the best time for a cross-timezone meeting.</p>
</section>''',

'es': '''<section class="lsi-block" aria-label="Detalles de la hora actual">
<h2>¿Qué hora es ahora en %%CITY%%, %%COUNTRY%%?</h2>
<p>¿Necesitas saber la hora local exacta en %%CITY%% ahora mismo? El reloj en vivo arriba se actualiza cada segundo, mostrándote la hora precisa actual en %%CITY%%, %%COUNTRY%%. Ya sea que estés programando una reunión con colegas en %%CITY%%, planificando un viaje o coordinando entre zonas horarias, esta página te da información en tiempo real en la que puedes confiar.</p>
<p>La hora en %%CITY%% sigue la zona horaria <strong>%%TZ%%</strong>. %%CITY%% está actualmente en <strong>%%UTC%%</strong>. Comprender la zona horaria local es esencial para evitar errores de programación y asegurar una comunicación fluida con contactos en %%COUNTRY%%.</p>
<h3>Referencia rápida: Hora en %%CITY%%</h3>
<ul>
<li><strong>Hora local actual:</strong> mostrada en vivo arriba</li>
<li><strong>Zona horaria:</strong> %%TZ%%</li>
<li><strong>Desplazamiento UTC:</strong> %%UTC%%</li>
<li><strong>País:</strong> %%COUNTRY%%</li>
</ul>
<p>Guarda esta página para acceder rápidamente a la hora actual en %%CITY%%. El reloj en vivo nunca necesita actualizarse manualmente. También puedes usar nuestro <a href="/es/">convertidor de zonas horarias</a> o el <a href="/es/meeting-planner.html">Planificador de Reuniones</a>.</p>
</section>''',

'zh': '''<section class="lsi-block" aria-label="当前时间详情">
<h2>%%CITY%%（%%COUNTRY%%）现在几点？</h2>
<p>需要知道%%CITY%%现在的准确当地时间吗？上方的实时时钟每秒更新，显示%%CITY%%、%%COUNTRY%%的精确当前时间。无论您是与%%CITY%%的同事安排会议、计划旅行，还是跨时区协调，此页面为您提供可靠实时信息。</p>
<p>%%CITY%%的时间遵循<strong>%%TZ%%</strong>时区。%%CITY%%目前为<strong>%%UTC%%</strong>。了解当地时区对于避免日程安排错误和确保与%%COUNTRY%%联系人顺畅沟通至关重要。</p>
<h3>快速参考：%%CITY%%时间</h3>
<ul>
<li><strong>当前当地时间：</strong>上方实时显示</li>
<li><strong>时区：</strong>%%TZ%%</li>
<li><strong>UTC偏移：</strong>%%UTC%%</li>
<li><strong>国家：</strong>%%COUNTRY%%</li>
</ul>
<p>收藏此页面以便快速查看%%CITY%%当前时间。实时时钟无需刷新即可自动更新。您还可以使用我们的<a href="/zh/">时区转换器</a>或<a href="/zh/meeting-planner.html">会议规划器</a>。</p>
</section>''',

'ru': '''<section class="lsi-block" aria-label="Подробности о текущем времени">
<h2>Сколько сейчас времени в %%CITY%%, %%COUNTRY%%?</h2>
<p>Нужно узнать точное местное время в %%CITY%% прямо сейчас? Живые часы выше обновляются каждую секунду, показывая точное текущее время в %%CITY%%, %%COUNTRY%%. Независимо от того, назначаете ли вы встречу с коллегами в %%CITY%%, планируете поездку или координируете работу через часовые пояса, эта страница даёт вам надёжную информацию в реальном времени.</p>
<p>Время в %%CITY%% следует часовому поясу <strong>%%TZ%%</strong>. Это означает, что %%CITY%% сейчас в <strong>%%UTC%%</strong>. Понимание местного часового пояса необходимо для предотвращения ошибок в расписании и удобного общения с контактами в %%COUNTRY%%.</p>
<h3>Краткая справка: Время в %%CITY%%</h3>
<ul>
<li><strong>Текущее местное время:</strong> отображается вживую выше</li>
<li><strong>Часовой пояс:</strong> %%TZ%%</li>
<li><strong>Смещение UTC:</strong> %%UTC%%</li>
<li><strong>Страна:</strong> %%COUNTRY%%</li>
</ul>
<p>Добавьте эту страницу в закладки для быстрого доступа к текущему времени в %%CITY%%. Живые часы обновляются автоматически без перезагрузки. Вы также можете использовать наш <a href="/ru/">конвертер часовых поясов</a> или <a href="/ru/meeting-planner.html">Планировщик встреч</a>.</p>
</section>''',

'it': '''<section class="lsi-block" aria-label="Dettagli ora attuale">
<h2>Che ore sono a %%CITY%%, %%COUNTRY%%?</h2>
<p>Hai bisogno di sapere l\'ora locale esatta a %%CITY%% in questo momento? L\'orologio live sopra si aggiorna ogni secondo, mostrandoti l\'ora precisa attuale a %%CITY%%, %%COUNTRY%%. Che tu stia programmando una riunione con colleghi a %%CITY%%, pianificando un viaggio o coordinando tra fusi orari, questa pagina ti offre informazioni in tempo reale su cui puoi contare.</p>
<p>L\'ora a %%CITY%% segue il fuso orario <strong>%%TZ%%</strong>. %%CITY%% è attualmente a <strong>%%UTC%%</strong>. Comprendere il fuso orario locale è essenziale per evitare errori di programmazione e garantire una comunicazione fluida con i contatti in %%COUNTRY%%.</p>
<h3>Riferimento rapido: Ora a %%CITY%%</h3>
<ul>
<li><strong>Ora locale attuale:</strong> mostrata live sopra</li>
<li><strong>Fuso orario:</strong> %%TZ%%</li>
<li><strong>Scostamento UTC:</strong> %%UTC%%</li>
<li><strong>Paese:</strong> %%COUNTRY%%</li>
</ul>
<p>Salva questa pagina per accedere rapidamente all\'ora attuale a %%CITY%%. L\'orologio live si aggiorna automaticamente. Puoi anche usare il nostro <a href="/it/">convertitore di fusi orari</a> o il <a href="/it/meeting-planner.html">Pianificatore riunioni</a>.</p>
</section>''',

'de': '''<section class="lsi-block" aria-label="Aktuelle Zeit Details">
<h2>Wie spät ist es in %%CITY%%, %%COUNTRY%%?</h2>
<p>Möchten Sie die genaue Ortszeit in %%CITY%% jetzt wissen? Die Live-Uhr oben aktualisiert sich jede Sekunde und zeigt Ihnen die präzise aktuelle Zeit in %%CITY%%, %%COUNTRY%%. Ob Sie eine Besprechung mit Kollegen in %%CITY%% planen, eine Reise vorbereiten oder über Zeitzonen hinweg koordinieren — diese Seite bietet Ihnen verlässliche Echtzeit-Informationen.</p>
<p>Die Zeit in %%CITY%% folgt der Zeitzone <strong>%%TZ%%</strong>. %%CITY%% ist aktuell <strong>%%UTC%%</strong>. Das Verständnis der lokalen Zeitzone ist wichtig, um Terminfehler zu vermeiden und eine reibungslose Kommunikation mit Kontakten in %%COUNTRY%% zu gewährleisten.</p>
<h3>Kurzübersicht: Zeit in %%CITY%%</h3>
<ul>
<li><strong>Aktuelle Ortszeit:</strong> live oben angezeigt</li>
<li><strong>Zeitzone:</strong> %%TZ%%</li>
<li><strong>UTC-Verschiebung:</strong> %%UTC%%</li>
<li><strong>Land:</strong> %%COUNTRY%%</li>
</ul>
<p>Lesezeichen Sie diese Seite für schnellen Zugriff auf die aktuelle Zeit in %%CITY%%. Die Live-Uhr aktualisiert sich automatisch. Sie können auch unseren <a href="/de/">Zeitzonen-Konverter</a> oder den <a href="/de/meeting-planner.html">Besprechungsplaner</a> nutzen.</p>
</section>''',

'ja': '''<section class="lsi-block" aria-label="現在の時刻詳細">
<h2>%%CITY%%（%%COUNTRY%%）の現在の時刻は？</h2>
<p>%%CITY%%の正確な現地時間を今すぐ知る必要がありますか？上のライブクロックは毎秒更新され、%%CITY%%、%%COUNTRY%%の正確な現在の時刻を表示します。%%CITY%%の同僚との会議のスケジュール、旅行の計画、タイムゾーンをまたぐ調整など、このページは信頼できるリアルタイム情報を提供します。</p>
<p>%%CITY%%の時刻は<strong>%%TZ%%</strong>タイムゾーンに従います。%%CITY%%は現在<strong>%%UTC%%</strong>です。現地のタイムゾーンを理解することは、スケジュールのミスを防ぎ、%%COUNTRY%%の連絡先との円滑なコミュニケーションを確保するために不可欠です。</p>
<h3>クイックリファレンス：%%CITY%%の時刻</h3>
<ul>
<li><strong>現在の現地時間：</strong>上にライブ表示</li>
<li><strong>タイムゾーン：</strong>%%TZ%%</li>
<li><strong>UTCオフセット：</strong>%%UTC%%</li>
<li><strong>国：</strong>%%COUNTRY%%</li>
</ul>
<p>このページをブックマークして、%%CITY%%の現在の時刻に素早くアクセスできます。ライブクロックは自動更新されます。<a href="/ja/">タイムゾーン変換ツール</a>や<a href="/ja/meeting-planner.html">ミーティングプランナー</a>もご利用ください。</p>
</section>''',
}


def extract_city_data(html):
    tz_match = re.search(r'data-timezone="([^"]+)"', html)
    timezone = tz_match.group(1) if tz_match else ''
    
    utc_match = re.search(r'<span>([A-Z]{2,5}\s*\(UTC[+-]\d+(?:\/[A-Z]{2,5}\s*\(UTC[+-]\d+)?\))', html)
    utc_label = utc_match.group(1) if utc_match else ''
    
    crumb_match = re.findall(r'<a href="/country/[^"]+">([^<]+)</a>', html)
    country = crumb_match[-1] if crumb_match else ''
    
    page_match = re.search(r'<span aria-current="page">([^<]+)</span>', html)
    city = page_match.group(1) if page_match else ''
    
    return city, country, timezone, utc_label


def fill_template(template, city, country, tz, utc):
    return template.replace('%%CITY%%', city).replace('%%COUNTRY%%', country).replace('%%TZ%%', tz).replace('%%UTC%%', utc)


def process_file(filepath, lang='en'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if 'minute-progress-bar' in html:
        return False
    
    city, country, timezone, utc_label = extract_city_data(html)
    if not timezone or not city:
        return False
    
    # 1. Add CSS before </style>
    style_end = html.find('</style>')
    if style_end == -1:
        return False
    html = html[:style_end] + NEW_CSS + html[style_end:]
    
    # 2. Add progress bar and copy button after time-details </p>
    time_details_idx = html.find('</p>', html.find('time-details'))
    if time_details_idx == -1:
        return False
    insert_pos = time_details_idx + 4
    
    copy_label = COPY_LABELS.get(lang, 'Copy time')
    extra_html = '\n                <div class="minute-progress"><div class="minute-progress-bar" id="minute-bar" style="width:0%%"></div></div>\n                <button class="copy-time-btn" id="copy-time-btn" type="button">' + copy_label + '</button>'
    html = html[:insert_pos] + extra_html + html[insert_pos:]
    
    # 3. Replace old live clock script with enhanced one
    script_match = re.search(r'<script>\(function\(\)\{var tz="[^"]+";var el=document\.getElementById\("live-time"\);.*?\}\)\(\)</script>', html, re.DOTALL)
    
    if script_match:
        copied_label = COPIED_LABELS.get(lang, 'Copied!')
        tz_json = json.dumps(timezone)
        copy_json = json.dumps(copy_label)
        copied_json = json.dumps(copied_label)
        
        new_script = '<script>(function(){var tz=' + tz_json + ';var el=document.getElementById("live-time");var bar=document.getElementById("minute-bar");var copyBtn=document.getElementById("copy-time-btn");function update(){try{var now=new Date();var timeStr=new Intl.DateTimeFormat("en-US",{timeZone:tz,hour:"2-digit",minute:"2-digit",second:"2-digit",hour12:true,weekday:"long",year:"numeric",month:"long",day:"numeric"}).format(now);el.textContent=timeStr;if(bar){var sec=now.getSeconds();bar.style.width=((sec/60)*100)+"%"}}catch(e){el.textContent="Time zone not supported"}}update();setInterval(update,1000);if(copyBtn){copyBtn.addEventListener("click",function(){var text=el.textContent;navigator.clipboard.writeText(text).then(function(){copyBtn.textContent=' + copied_json + ';setTimeout(function(){copyBtn.textContent=' + copy_json + '},2000)}).catch(function(){var ta=document.createElement("textarea");ta.value=text;document.body.appendChild(ta);ta.select();document.execCommand("copy");document.body.removeChild(ta);copyBtn.textContent=' + copied_json + ';setTimeout(function(){copyBtn.textContent=' + copy_json + '},2000)})}})})();</script>'
        
        html = html[:script_match.start()] + new_script + html[script_match.end():]
    
    # 4. Add LSI block after current-time-card closing </div>
    card_close = html.find('</div>', html.find('copy-time-btn'))
    if card_close == -1:
        return False
    
    lsi_template = LSI_TEMPLATES.get(lang, LSI_TEMPLATES['en'])
    lsi_html = '\n            ' + fill_template(lsi_template, city, country, timezone, utc_label)
    
    html = html[:card_close+6] + lsi_html + html[card_close+6:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return True


def main():
    count = 0
    errors = 0
    
    # Process English pages
    time_dir = BASE / 'time'
    for fp in sorted(time_dir.glob('*.html')):
        try:
            if process_file(fp, 'en'):
                count += 1
                if count % 100 == 0:
                    print("  Processed " + str(count) + " en pages...")
            else:
                errors += 1
        except Exception as e:
            print("  ERROR en/" + fp.name + ": " + str(e))
            errors += 1
    
    print("EN: " + str(count) + " updated, " + str(errors) + " skipped")
    
    # Process i18n pages
    for lang in ['es', 'zh', 'ru', 'it', 'de', 'ja']:
        lang_dir = BASE / lang / 'time'
        if not lang_dir.exists():
            print(lang + ": dir not found")
            continue
        
        lang_count = 0
        lang_errors = 0
        for fp in sorted(lang_dir.glob('*.html')):
            try:
                if process_file(fp, lang):
                    lang_count += 1
                else:
                    lang_errors += 1
            except Exception as e:
                print("  ERROR " + lang + "/" + fp.name + ": " + str(e))
                lang_errors += 1
        
        print(lang.upper() + ": " + str(lang_count) + " updated, " + str(lang_errors) + " skipped")
        count += lang_count
    
    print("\nTOTAL: " + str(count) + " pages updated")


if __name__ == '__main__':
    main()
