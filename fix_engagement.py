#!/usr/bin/env python3
"""Fix the broken city pages — reconstruct the current-time-card properly."""
import re, os, json
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')

# The correct card inner HTML structure we want
def build_card_inner(city_name, timezone, utc_label, copy_label, lang):
    """Build the correct current-time-card inner content."""
    card_h2 = 'Current Time in ' + city_name
    # For i18n pages, check lang
    lang_h2 = {
        'es': 'Hora actual en ' + city_name,
        'zh': city_name + '当前时间',
        'ru': 'Текущее время в ' + city_name,
        'it': 'Ora attuale a ' + city_name,
        'de': 'Aktuelle Zeit in ' + city_name,
        'ja': city_name + 'の現在時刻',
    }
    if lang != 'en':
        card_h2 = lang_h2.get(lang, card_h2)
    
    # Split the utc_label for display
    # e.g. "EET (UTC+2) / EEST (UTC+3)" -> prefer the full string
    parts = [
        '                <h2>' + card_h2 + '</h2>',
        '                <p class="live-time" style="min-height:2.5rem" id="live-time" data-timezone="' + timezone + '" aria-live="polite">Loading...</p>',
        '                <div class="minute-progress"><div class="minute-progress-bar" id="minute-bar" style="width:0%"></div></div>',
        '                <button class="copy-time-btn" id="copy-time-btn" type="button">' + copy_label + '</button>',
        '                <p class="time-details">',
        '                    <span>' + timezone + '</span>',
        '                    <span>' + utc_label + '</span>',
        '                </p>',
    ]
    return '\n'.join(parts)


COPY_LABELS = {
    'en': 'Copy time', 'es': 'Copiar hora', 'zh': '复制时间',
    'ru': 'Копировать время', 'it': 'Copia ora', 'de': 'Zeit kopieren', 'ja': '時刻をコピー',
}
COPIED_LABELS = {
    'en': 'Copied!', 'es': '¡Copiado!', 'zh': '已复制！',
    'ru': 'Скопировано!', 'it': 'Copiato!', 'de': 'Kopiert!', 'ja': 'コピー済み！',
}

LSI_TEMPLATES = {
'en': '<section class="lsi-block" aria-label="Current time details">\n<h2>What\'s the Current Time in %%CITY%%, %%COUNTRY%%?</h2>\n<p>Need to know the exact local time in %%CITY%% right now? The live clock above updates every second, showing you the precise current time in %%CITY%%, %%COUNTRY%%. Whether you\'re scheduling a meeting with colleagues in %%CITY%%, planning a trip, or coordinating across time zones, this page gives you real-time information you can rely on.</p>\n<p>The time in %%CITY%% follows the <strong>%%TZ%%</strong> time zone. This means %%CITY%% is currently <strong>%%UTC%%</strong>. Understanding the local time zone is essential for avoiding scheduling mistakes and ensuring smooth communication with contacts in %%COUNTRY%%.</p>\n<h3>Quick Reference: %%CITY%% Time</h3>\n<ul>\n<li><strong>Current local time:</strong> displayed live above</li>\n<li><strong>Time zone:</strong> %%TZ%%</li>\n<li><strong>UTC offset:</strong> %%UTC%%</li>\n<li><strong>Country:</strong> %%COUNTRY%%</li>\n</ul>\n<p>Bookmark this page for quick access to the current time in %%CITY%%. The live clock never needs refreshing &mdash; it updates automatically. You can also use our <a href="/">time zone converter</a> to compare %%CITY%% time with any other city in the world, or check the <a href="/meeting-planner.html">Meeting Planner</a> to find the best time for a cross-timezone meeting.</p>\n</section>',
'es': '<section class="lsi-block" aria-label="Detalles de la hora actual">\n<h2>¿Qué hora es ahora en %%CITY%%, %%COUNTRY%%?</h2>\n<p>¿Necesitas saber la hora local exacta en %%CITY%% ahora mismo? El reloj en vivo arriba se actualiza cada segundo, mostrándote la hora precisa actual en %%CITY%%, %%COUNTRY%%. Ya sea que estés programando una reunión con colegas en %%CITY%%, planificando un viaje o coordinando entre zonas horarias, esta página te da información en tiempo real en la que puedes confiar.</p>\n<p>La hora en %%CITY%% sigue la zona horaria <strong>%%TZ%%</strong>. %%CITY%% está actualmente en <strong>%%UTC%%</strong>. Comprender la zona horaria local es esencial para evitar errores de programación y asegurar una comunicación fluida con contactos en %%COUNTRY%%.</p>\n<h3>Referencia rápida: Hora en %%CITY%%</h3>\n<ul>\n<li><strong>Hora local actual:</strong> mostrada en vivo arriba</li>\n<li><strong>Zona horaria:</strong> %%TZ%%</li>\n<li><strong>Desplazamiento UTC:</strong> %%UTC%%</li>\n<li><strong>País:</strong> %%COUNTRY%%</li>\n</ul>\n<p>Guarda esta página para acceder rápidamente a la hora actual en %%CITY%%. El reloj en vivo nunca necesita actualizarse manualmente. También puedes usar nuestro <a href="/es/">convertidor de zonas horarias</a> o el <a href="/es/meeting-planner.html">Planificador de Reuniones</a>.</p>\n</section>',
'zh': '<section class="lsi-block" aria-label="当前时间详情">\n<h2>%%CITY%%（%%COUNTRY%%）现在几点？</h2>\n<p>需要知道%%CITY%%现在的准确当地时间吗？上方的实时时钟每秒更新，显示%%CITY%%、%%COUNTRY%%的精确当前时间。无论您是与%%CITY%%的同事安排会议、计划旅行，还是跨时区协调，此页面为您提供可靠实时信息。</p>\n<p>%%CITY%%的时间遵循<strong>%%TZ%%</strong>时区。%%CITY%%目前为<strong>%%UTC%%</strong>。了解当地时区对于避免日程安排错误和确保与%%COUNTRY%%联系人顺畅沟通至关重要。</p>\n<h3>快速参考：%%CITY%%时间</h3>\n<ul>\n<li><strong>当前当地时间：</strong>上方实时显示</li>\n<li><strong>时区：</strong>%%TZ%%</li>\n<li><strong>UTC偏移：</strong>%%UTC%%</li>\n<li><strong>国家：</strong>%%COUNTRY%%</li>\n</ul>\n<p>收藏此页面以便快速查看%%CITY%%当前时间。实时时钟无需刷新即可自动更新。您还可以使用我们的<a href="/zh/">时区转换器</a>或<a href="/zh/meeting-planner.html">会议规划器</a>。</p>\n</section>',
'ru': '<section class="lsi-block" aria-label="Подробности о текущем времени">\n<h2>Сколько сейчас времени в %%CITY%%, %%COUNTRY%%?</h2>\n<p>Нужно узнать точное местное время в %%CITY%% прямо сейчас? Живые часы выше обновляются каждую секунду, показывая точное текущее время в %%CITY%%, %%COUNTRY%%. Независимо от того, назначаете ли вы встречу с коллегами в %%CITY%%, планируете поездку или координируете работу через часовые пояса, эта страница даёт вам надёжную информацию в реальном времени.</p>\n<p>Время в %%CITY%% следует часовому поясу <strong>%%TZ%%</strong>. Это означает, что %%CITY%% сейчас в <strong>%%UTC%%</strong>. Понимание местного часового пояса необходимо для предотвращения ошибок в расписании и удобного общения с контактами в %%COUNTRY%%.</p>\n<h3>Краткая справка: Время в %%CITY%%</h3>\n<ul>\n<li><strong>Текущее местное время:</strong> отображается вживую выше</li>\n<li><strong>Часовой пояс:</strong> %%TZ%%</li>\n<li><strong>Смещение UTC:</strong> %%UTC%%</li>\n<li><strong>Страна:</strong> %%COUNTRY%%</li>\n</ul>\n<p>Добавьте эту страницу в закладки для быстрого доступа к текущему времени в %%CITY%%. Живые часы обновляются автоматически без перезагрузки. Вы также можете использовать наш <a href="/ru/">конвертер часовых поясов</a> или <a href="/ru/meeting-planner.html">Планировщик встреч</a>.</p>\n</section>',
'it': '<section class="lsi-block" aria-label="Dettagli ora attuale">\n<h2>Che ore sono a %%CITY%%, %%COUNTRY%%?</h2>\n<p>Hai bisogno di sapere l\'ora locale esatta a %%CITY%% in questo momento? L\'orologio live sopra si aggiorna ogni secondo, mostrandoti l\'ora precisa attuale a %%CITY%%, %%COUNTRY%%. Che tu stia programmando una riunione con colleghi a %%CITY%%, pianificando un viaggio o coordinando tra fusi orari, questa pagina ti offre informazioni in tempo reale su cui puoi contare.</p>\n<p>L\'ora a %%CITY%% segue il fuso orario <strong>%%TZ%%</strong>. %%CITY%% è attualmente a <strong>%%UTC%%</strong>. Comprendere il fuso orario locale è essenziale per evitare errori di programmazione e garantire una comunicazione fluida con i contatti in %%COUNTRY%%.</p>\n<h3>Riferimento rapido: Ora a %%CITY%%</h3>\n<ul>\n<li><strong>Ora locale attuale:</strong> mostrata live sopra</li>\n<li><strong>Fuso orario:</strong> %%TZ%%</li>\n<li><strong>Scostamento UTC:</strong> %%UTC%%</li>\n<li><strong>Paese:</strong> %%COUNTRY%%</li>\n</ul>\n<p>Salva questa pagina per accedere rapidamente all\'ora attuale a %%CITY%%. L\'orologio live si aggiorna automaticamente. Puoi anche usare il nostro <a href="/it/">convertitore di fusi orari</a> o il <a href="/it/meeting-planner.html">Pianificatore riunioni</a>.</p>\n</section>',
'de': '<section class="lsi-block" aria-label="Aktuelle Zeit Details">\n<h2>Wie spät ist es in %%CITY%%, %%COUNTRY%%?</h2>\n<p>Möchten Sie die genaue Ortszeit in %%CITY%% jetzt wissen? Die Live-Uhr oben aktualisiert sich jede Sekunde und zeigt Ihnen die präzise aktuelle Zeit in %%CITY%%, %%COUNTRY%%. Ob Sie eine Besprechung mit Kollegen in %%CITY%% planen, eine Reise vorbereiten oder über Zeitzonen hinweg koordinieren — diese Seite bietet Ihnen verlässliche Echtzeit-Informationen.</p>\n<p>Die Zeit in %%CITY%% folgt der Zeitzone <strong>%%TZ%%</strong>. %%CITY%% ist aktuell <strong>%%UTC%%</strong>. Das Verständnis der lokalen Zeitzone ist wichtig, um Terminfehler zu vermeiden und eine reibungslose Kommunikation mit Kontakten in %%COUNTRY%% zu gewährleisten.</p>\n<h3>Kurzübersicht: Zeit in %%CITY%%</h3>\n<ul>\n<li><strong>Aktuelle Ortszeit:</strong> live oben angezeigt</li>\n<li><strong>Zeitzone:</strong> %%TZ%%</li>\n<li><strong>UTC-Verschiebung:</strong> %%UTC%%</li>\n<li><strong>Land:</strong> %%COUNTRY%%</li>\n</ul>\n<p>Lesezeichen Sie diese Seite für schnellen Zugriff auf die aktuelle Zeit in %%CITY%%. Die Live-Uhr aktualisiert sich automatisch. Sie können auch unseren <a href="/de/">Zeitzonen-Konverter</a> oder den <a href="/de/meeting-planner.html">Besprechungsplaner</a> nutzen.</p>\n</section>',
'ja': '<section class="lsi-block" aria-label="現在の時刻詳細">\n<h2>%%CITY%%（%%COUNTRY%%）の現在の時刻は？</h2>\n<p>%%CITY%%の正確な現地時間を今すぐ知る必要がありますか？上のライブクロックは毎秒更新され、%%CITY%%、%%COUNTRY%%の正確な現在の時刻を表示します。%%CITY%%の同僚との会議のスケジュール、旅行の計画、タイムゾーンをまたぐ調整など、このページは信頼できるリアルタイム情報を提供します。</p>\n<p>%%CITY%%の時刻は<strong>%%TZ%%</strong>タイムゾーンに従います。%%CITY%%は現在<strong>%%UTC%%</strong>です。現地のタイムゾーンを理解することは、スケジュールのミスを防ぎ、%%COUNTRY%%の連絡先との円滑なコミュニケーションを確保するために不可欠です。</p>\n<h3>クイックリファレンス：%%CITY%%の時刻</h3>\n<ul>\n<li><strong>現在の現地時間：</strong>上にライブ表示</li>\n<li><strong>タイムゾーン：</strong>%%TZ%%</li>\n<li><strong>UTCオフセット：</strong>%%UTC%%</li>\n<li><strong>国：</strong>%%COUNTRY%%</li>\n</ul>\n<p>このページをブックマークして、%%CITY%%の現在の時刻に素早くアクセスできます。ライブクロックは自動更新されます。<a href="/ja/">タイムゾーン変換ツール</a>や<a href="/ja/meeting-planner.html">ミーティングプランナー</a>もご利用ください。</p>\n</section>',
}


def fill_tpl(template, city, country, tz, utc):
    return template.replace('%%CITY%%', city).replace('%%COUNTRY%%', country).replace('%%TZ%%', tz).replace('%%UTC%%', utc)


def process_file(filepath, lang='en'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract data
    tz_match = re.search(r'data-timezone="([^"]+)"', html)
    if not tz_match:
        return False
    timezone = tz_match.group(1)
    
    utc_match = re.search(r'<span>([A-Z]{2,5}\s*\(UTC[+-]\d+(?:\/[A-Z]{2,5}\s*\(UTC[+-]\d+)?\))', html)
    utc_label = utc_match.group(1) if utc_match else ''
    
    # Try longer UTC label pattern with / separator
    if not utc_label:
        utc_match2 = re.search(r'<span>([^<]+UTC[^<]*)</span>', html)
        if utc_match2:
            utc_label = utc_match2.group(1)
    
    crumb_match = re.findall(r'<a href="/[^"]*country/[^"]+">([^<]+)</a>', html)
    country = crumb_match[-1] if crumb_match else ''
    
    page_match = re.search(r'<span aria-current="page">([^<]+)</span>', html)
    city = page_match.group(1) if page_match else ''
    
    if not city or not timezone:
        return False
    
    # Find the current-time-card section and replace it entirely
    card_start = html.find('<div class="current-time-card"')
    if card_start == -1:
        return False
    
    # Find the matching closing </div> — count nesting
    pos = html.find('>', card_start) + 1
    depth = 1
    while depth > 0 and pos < len(html):
        next_open = html.find('<div', pos)
        next_close = html.find('</div>', pos)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                card_end = next_close + 6  # after </div>
                break
            pos = next_close + 6
    
    # Build new card
    copy_label = COPY_LABELS.get(lang, 'Copy time')
    card_inner = build_card_inner(city, timezone, utc_label, copy_label, lang)
    
    # For finding the old UTC label (may have both standard/summer)
    # We need the full string like "EET (UTC+2) / EEST (UTC+3)"
    full_utc = ''
    time_details_match = re.search(r'<p class="time-details">\s*<span>[^<]*</span>\s*<span>([^<]+)</span>', html)
    if time_details_match:
        full_utc = time_details_match.group(1)
    else:
        full_utc = utc_label
    
    new_card = '<div class="current-time-card" role="region" aria-label="Live clock for ' + city + '">\n' + card_inner + '\n            </div>'
    
    # Build LSI block
    lsi_template = LSI_TEMPLATES.get(lang, LSI_TEMPLATES['en'])
    lsi_html = '\n            ' + fill_tpl(lsi_template, city, country, timezone, full_utc)
    
    # Replace card + anything between card and city-info with new card + LSI
    # Find next section after the broken card
    next_section = html.find('<section class="city-info"', card_end)
    if next_section == -1:
        next_section = html.find('<section class="faq-section"', card_end)
    
    if next_section == -1:
        return False
    
    html = html[:card_start] + new_card + lsi_html + '\n            ' + html[next_section:]
    
    # Also fix the old script — replace with enhanced version
    script_match = re.search(r'<script>\(function\(\)\{var tz="[^"]+";var el=document\.getElementById\("live-time"\);.*?\}\)\(\)</script>', html, re.DOTALL)
    
    if script_match:
        copied_label = COPIED_LABELS.get(lang, 'Copied!')
        tz_json = json.dumps(timezone)
        copy_json = json.dumps(copy_label)
        copied_json = json.dumps(copied_label)
        
        new_script = '<script>(function(){var tz=' + tz_json + ';var el=document.getElementById("live-time");var bar=document.getElementById("minute-bar");var copyBtn=document.getElementById("copy-time-btn");function update(){try{var now=new Date();var timeStr=new Intl.DateTimeFormat("en-US",{timeZone:tz,hour:"2-digit",minute:"2-digit",second:"2-digit",hour12:true,weekday:"long",year:"numeric",month:"long",day:"numeric"}).format(now);el.textContent=timeStr;if(bar){var sec=now.getSeconds();bar.style.width=((sec/60)*100)+"%"}}catch(e){el.textContent="Time zone not supported"}}update();setInterval(update,1000);if(copyBtn){copyBtn.addEventListener("click",function(){var text=el.textContent;navigator.clipboard.writeText(text).then(function(){copyBtn.textContent=' + copied_json + ';setTimeout(function(){copyBtn.textContent=' + copy_json + '},2000)}).catch(function(){var ta=document.createElement("textarea");ta.value=text;document.body.appendChild(ta);ta.select();document.execCommand("copy");document.body.removeChild(ta);copyBtn.textContent=' + copied_json + ';setTimeout(function(){copyBtn.textContent=' + copy_json + '},2000)})}})})();</script>'
        
        html = html[:script_match.start()] + new_script + html[script_match.end():]
    
    # Fix the width:0%% to width:0%
    html = html.replace('width:0%%"', 'width:0%"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return True


def main():
    count = 0
    errors = 0
    
    time_dir = BASE / 'time'
    for fp in sorted(time_dir.glob('*.html')):
        try:
            if process_file(fp, 'en'):
                count += 1
                if count % 100 == 0:
                    print("  Fixed " + str(count) + " en pages...")
            else:
                errors += 1
        except Exception as e:
            print("  ERROR en/" + fp.name + ": " + str(e))
            errors += 1
    
    print("EN: " + str(count) + " fixed, " + str(errors) + " skipped")
    
    for lang in ['es', 'zh', 'ru', 'it', 'de', 'ja']:
        lang_dir = BASE / lang / 'time'
        if not lang_dir.exists():
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
        print(lang.upper() + ": " + str(lang_count) + " fixed, " + str(lang_errors) + " skipped")
        count += lang_count
    
    print("\nTOTAL: " + str(count) + " pages fixed")


if __name__ == '__main__':
    main()
