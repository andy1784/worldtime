#!/usr/bin/env python3
"""Generate all 8 translations for the new time-zone-abbreviations-cheat-sheet article."""
import os
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')
BLOG_DIR = BASE / 'blog'

slug = 'time-zone-abbreviations-cheat-sheet'
slug_en = slug

LANGS = {
    'es': {'home': 'Inicio', 'blog': 'Blog', 'date': '10 ago 2026', 'read': '8 min de lectura',
           'skip': 'Saltar al contenido principal', 'loading': 'Cargando la hora...'},
    'zh': {'home': '首页', 'blog': '博客', 'date': '2026年8月10日', 'read': '阅读 8 分钟',
           'skip': '跳到主要内容', 'loading': '正在加载时间...'},
    'it': {'home': 'Home', 'blog': 'Blog', 'date': '10 ago 2026', 'read': '8 min di lettura',
           'skip': 'Vai al contenuto principale', 'loading': 'Caricamento ora...'},
    'de': {'home': 'Start', 'blog': 'Blog', 'date': '10. Aug 2026', 'read': '8 Min. Lesezeit',
           'skip': 'Zum Hauptinhalt springen', 'loading': 'Zeit wird geladen...'},
    'ja': {'home': 'ホーム', 'blog': 'ブログ', 'date': '2026年8月10日', 'read': '読了 8 分',
           'skip': 'メインコンテンツへ移動', 'loading': '時刻を読み込み中...'},
    'fr': {'home': 'Accueil', 'blog': 'Blog', 'date': '10 août 2026', 'read': '8 min de lecture',
           'skip': 'Aller au contenu principal', 'loading': "Chargement de l'heure..."},
    'uk': {'home': 'Головна', 'blog': 'Блог', 'date': '10 лип 2026', 'read': '8 хв читання',
           'skip': 'Перейти до основного вмісту', 'loading': 'Завантаження часу...'},
    'ru': {'home': 'Главная', 'blog': 'Блог', 'date': '10 авг 2026', 'read': '8 мин чтения',
           'skip': 'Перейти к основному содержанию', 'loading': 'Загрузка времени...'},
}

TRANSLATIONS = {
    'es': {
        'title': 'Hoja de referencia de abreviaturas de zonas horarias (2026)',
        'meta_desc': 'Referencia rápida para todas las abreviaturas principales de zonas horarias: EST, PST, CET, IST, JST y 50 más. Incluye desfases UTC, variantes de horario de verano y las ciudades que usan cada una.',
        'keywords': 'abreviaturas de zonas horarias, EST PST CST MST, hoja de trucos desfases UTC, lista de códigos de zona horaria, acrónimos de zona horaria, abreviaturas de horario de verano',
        'h1': 'Hoja de referencia de abreviaturas de zonas horarias',
        'content': '''<p>Ves "EST" en una confirmación de vuelo, "CET" en una invitación de reunión, "IST" en un archivo de log. Cada abreviatura significa un desfase específico de UTC, pero algunas significan cosas distintas en verano versus invierno. Esta hoja de referencia te da el desfase exacto, las ciudades principales y si el horario de verano lo cambia.</p>
<h2>Zonas Horarias de Norteamérica</h2>
<table class="tz-table"><thead><tr><th>Abr</th><th>Nombre Completo</th><th>Desfase UTC</th><th>Variante Horario de Verano</th><th>Ciudades Principales</th></tr></thead>
<tbody><tr><td>EST</td><td>Eastern Standard Time</td><td>UTC-5</td><td>EDT (UTC-4)</td><td>Nueva York, Toronto, Miami, Atlanta</td></tr>
<tr><td>EDT</td><td>Eastern Daylight Time</td><td>UTC-4</td><td>EST (invierno)</td><td>Mismas ciudades, marzo-noviembre</td></tr>
<tr><td>CST</td><td>Central Standard Time</td><td>UTC-6</td><td>CDT (UTC-5)</td><td>Chicago, Dallas, Ciudad de México, Houston</td></tr>
<tr><td>CDT</td><td>Central Daylight Time</td><td>UTC-5</td><td>CST (invierno)</td><td>Mismas ciudades, marzo-noviembre</td></tr>
<tr><td>MST</td><td>Mountain Standard Time</td><td>UTC-7</td><td>MDT (UTC-6)</td><td>Denver, Phoenix*, Edmonton, El Paso</td></tr>
<tr><td>MDT</td><td>Mountain Daylight Time</td><td>UTC-6</td><td>MST (invierno)</td><td>Mismas ciudades (excepto Arizona)</td></tr>
<tr><td>PST</td><td>Pacific Standard Time</td><td>UTC-8</td><td>PDT (UTC-7)</td><td>Los Ángeles, Vancouver, Seattle, Tijuana</td></tr>
<tr><td>PDT</td><td>Pacific Daylight Time</td><td>UTC-7</td><td>PST (invierno)</td><td>Mismas ciudades, marzo-noviembre</td></tr>
<tr><td>AKST</td><td>Alaska Standard Time</td><td>UTC-9</td><td>AKDT (UTC-8)</td><td>Anchorage, Fairbanks, Juneau</td></tr>
<tr><td>HST</td><td>Hawaii-Aleutian Standard Time</td><td>UTC-10</td><td>Sin horario de verano</td><td>Honolulu, Hilo, Adak</td></tr></tbody></table>
<p><small>* Arizona (excepto la Nación Navajo) no observa horario de verano y se queda en MST todo el año.</small></p>
<h2>Zonas Horarias del Atlántico y Sudamérica</h2>
<table class="tz-table"><thead><tr><th>Abr</th><th>Nombre Completo</th><th>Desfase UTC</th><th>Variante Horario de Verano</th><th>Ciudades Principales</th></tr></thead>
<tbody><tr><td>AST</td><td>Atlantic Standard Time</td><td>UTC-4</td><td>ADT (UTC-3)</td><td>Halifax, San Juan, Bermudas, Caracas</td></tr>
<tr><td>BRT</td><td>Brasilia Time</td><td>UTC-3</td><td>Sin horario de verano desde 2019</td><td>São Paulo, Río de Janeiro, Brasilia</td></tr>
<tr><td>ART</td><td>Argentina Time</td><td>UTC-3</td><td>Sin horario de verano desde 2009</td><td>Buenos Aires, Córdoba, Rosario</td></tr>
<tr><td>CLT</td><td>Chile Standard Time</td><td>UTC-4</td><td>CLST (UTC-3)</td><td>Santiago, Valparaíso, Concepción</td></tr></tbody></table>
<h2>Zonas Horarias Europeas y Africanas</h2>
<table class="tz-table"><thead><tr><th>Abr</th><th>Nombre Completo</th><th>Desfase UTC</th><th>Variante Horario de Verano</th><th>Ciudades Principales</th></tr></thead>
<tbody><tr><td>GMT</td><td>Greenwich Mean Time</td><td>UTC+0</td><td>BST (UTC+1)</td><td>Londres, Dublín, Lisboa (invierno)</td></tr>
<tr><td>BST</td><td>British Summer Time</td><td>UTC+1</td><td>GMT (invierno)</td><td>Londres, Dublín, Edimburgo (verano)</td></tr>
<tr><td>WET</td><td>Western European Time</td><td>UTC+0</td><td>WEST (UTC+1)</td><td>Lisboa, Casablanca, Reikiavik</td></tr>
<tr><td>CET</td><td>Central European Time</td><td>UTC+1</td><td>CEST (UTC+2)</td><td>París, Berlín, Roma, Madrid, Varsovia</td></tr>
<tr><td>CEST</td><td>Central European Summer Time</td><td>UTC+2</td><td>CET (invierno)</td><td>Mismas ciudades, marzo-octubre</td></tr>
<tr><td>EET</td><td>Eastern European Time</td><td>UTC+2</td><td>EEST (UTC+3)</td><td>Helsinki, Kiev, Bucarest, El Cairo</td></tr>
<tr><td>MSK</td><td>Moscow Standard Time</td><td>UTC+3</td><td>Sin horario de verano desde 2014</td><td>Moscú, San Petersburgo, Estambul, Minsk</td></tr>
<tr><td>SAST</td><td>South Africa Standard Time</td><td>UTC+2</td><td>Sin horario de verano</td><td>Johannesburgo, Ciudad del Cabo, Durban</td></tr>
<tr><td>WAT</td><td>West Africa Time</td><td>UTC+1</td><td>Sin horario de verano</td><td>Lagos, Kinshasa, Argel</td></tr></tbody></table>
<h2>Zonas Horarias del Medio Oriente y Asia Central</h2>
<table class="tz-table"><thead><tr><th>Abr</th><th>Nombre Completo</th><th>Desfase UTC</th><th>Variante Horario de Verano</th><th>Ciudades Principales</th></tr></thead>
<tbody><tr><td>GST</td><td>Gulf Standard Time</td><td>UTC+4</td><td>Sin horario de verano</td><td>Dubái, Abu Dabi, Mascate, Doha</td></tr>
<tr><td>AST</td><td>Arabia Standard Time</td><td>UTC+3</td><td>Sin horario de verano</td><td>Riad, Yeda, Ciudad de Kuwait, Manama</td></tr>
<tr><td>IRST</td><td>Iran Standard Time</td><td>UTC+3:30</td><td>IRDT (UTC+4:30)</td><td>Teherán, Mashhad, Isfahán</td></tr>
<tr><td>AFT</td><td>Afghanistan Time</td><td>UTC+4:30</td><td>Sin horario de verano</td><td>Kabul, Herat, Mazar-i-Sharif</td></tr>
<tr><td>PKT</td><td>Pakistan Standard Time</td><td>UTC+5</td><td>Sin horario de verano</td><td>Karachi, Lahore, Islamabad</td></tr></tbody></table>
<h2>Zonas Horarias del Sur y Sudeste Asiático</h2>
<table class="tz-table"><thead><tr><th>Abr</th><th>Nombre Completo</th><th>Desfase UTC</th><th>Variante Horario de Verano</th><th>Ciudades Principales</th></tr></thead>
<tbody><tr><td>IST</td><td>India Standard Time</td><td>UTC+5:30</td><td>Sin horario de verano</td><td>Mumbai, Delhi, Bangalore, Kolkata, Chennai</td></tr>
<tr><td>NPT</td><td>Nepal Time</td><td>UTC+5:45</td><td>Sin horario de verano</td><td>Katmandú, Pokhara, Biratnagar</td></tr>
<tr><td>BST</td><td>Bangladesh Standard Time</td><td>UTC+6</td><td>Sin horario de verano</td><td>Daca, Chittagong, Sylhet</td></tr>
<tr><td>MMT</td><td>Myanmar Time</td><td>UTC+6:30</td><td>Sin horario de verano</td><td>Yangon, Mandalay, Naypyidaw</td></tr>
<tr><td>ICT</td><td>Indochina Time</td><td>UTC+7</td><td>Sin horario de verano</td><td>Bangkok, Hanói, Yakarta*, Phnom Penh</td></tr>
<tr><td>WIB</td><td>Western Indonesian Time</td><td>UTC+7</td><td>Sin horario de verano</td><td>Yakarta, Bandung, Surabaya</td></tr>
<tr><td>CST</td><td>China Standard Time</td><td>UTC+8</td><td>Sin horario de verano</td><td>Pekín, Shanghái, Hong Kong, Taipéi</td></tr>
<tr><td>SGT</td><td>Singapore Time</td><td>UTC+8</td><td>Sin horario de verano</td><td>Singapur, Kuala Lumpur, Manila, Perth</td></tr></tbody></table>
<p><small>* Yakarta usa WIB (UTC+7), no ICT.</small></p>
<h2>Zonas Horarias de Asia Oriental y el Pacífico</h2>
<table class="tz-table"><thead><tr><th>Abr</th><th>Nombre Completo</th><th>Desfase UTC</th><th>Variante Horario de Verano</th><th>Ciudades Principales</th></tr></thead>
<tbody><tr><td>JST</td><td>Japan Standard Time</td><td>UTC+9</td><td>Sin horario de verano</td><td>Tokio, Osaka, Seúl*, Pionyang*</td></tr>
<tr><td>KST</td><td>Korea Standard Time</td><td>UTC+9</td><td>Sin horario de verano</td><td>Seúl, Busán, Incheon</td></tr>
<tr><td>AWST</td><td>Australian Western Standard Time</td><td>UTC+8</td><td>Sin horario de verano</td><td>Perth, Broome, Karratha</td></tr>
<tr><td>ACST</td><td>Australian Central Standard Time</td><td>UTC+9:30</td><td>ACDT (UTC+10:30)</td><td>Adelaida, Darwin, Alice Springs</td></tr>
<tr><td>AEST</td><td>Australian Eastern Standard Time</td><td>UTC+10</td><td>AEDT (UTC+11)</td><td>Sídney, Melbourne, Brisbane*, Canberra</td></tr>
<tr><td>NZST</td><td>New Zealand Standard Time</td><td>UTC+12</td><td>NZDT (UTC+13)</td><td>Auckland, Wellington, Christchurch</td></tr></tbody></table>
<p><small>* Seúl y Pionyang usan KST, no JST. * Brisbane (Queensland) no observa horario de verano.</small></p>
<h2>Abreviaturas Ambiguas — Cuidado</h2>
<p>Algunas abreviaturas significan zonas distintas según el contexto:</p>
<ul><li><strong>CST</strong> — Central Standard Time (UTC-6, Norteamérica) <em>o</em> China Standard Time (UTC+8) <em>o</em> Cuba Standard Time (UTC-5)</li>
<li><strong>IST</strong> — India Standard Time (UTC+5:30) <em>o</em> Irish Standard Time (UTC+1, verano) <em>o</em> Israel Standard Time (UTC+2)</li>
<li><strong>PST</strong> — Pacific Standard Time (UTC-8) <em>o</em> Philippine Standard Time (UTC+8)</li>
<li><strong>BST</strong> — British Summer Time (UTC+1) <em>o</em> Bangladesh Standard Time (UTC+6) <em>o</em> Bougainville Standard Time (UTC+11)</li>
<li><strong>AST</strong> — Atlantic Standard Time (UTC-4) <em>o</em> Arabia Standard Time (UTC+3) <em>o</em> Amazon Standard Time (UTC-4, Brasil)</li></ul>
<p>Cuando ves un código ambiguo, mira el país o ciudad cercana. Para conversiones exactas, usa nuestro <a href="/es/time-zone-converter.html">convertidor de zonas horarias</a> que maneja todos estos correctamente.</p>
<h2>Referencia Rápida: Fechas de Cambio de Horario de Verano (Típicas)</h2>
<ul><li><strong>Norteamérica</strong>: 2.º domingo de marzo → 1.er domingo de noviembre</li>
<li><strong>Europa</strong>: último domingo de marzo → último domingo de octubre</li>
<li><strong>Australia (sureste)</strong>: 1.er domingo de octubre → 1.er domingo de abril</li>
<li><strong>Nueva Zelanda</strong>: último domingo de septiembre → 1.er domingo de abril</li>
<li><strong>Chile</strong>: 1.er domingo de septiembre → 1.er domingo de abril</li>
<li><strong>Paraguay</strong>: 1.er domingo de octubre → último domingo de marzo</li></ul>
<h2>Guarda Esta Página, Usa la Herramienta</h2>
<p>No necesitas memorizar 50+ códigos. Guarda esta página para la tabla de consulta. Cuando necesites una conversión exacta para una fecha específica — especialmente durante las semanas de transición de horario de verano — usa nuestra <a href="/es/time-difference.html">calculadora de diferencia horaria</a> o <a href="/es/meeting-planner.html">planificador de reuniones</a>. Usan la base de datos IANA de zonas horarias así que cada desfase está actualizado y es correcto.</p>''',
    },
    'zh': {
        'title': '时区缩写速查表 (2026)',
        'meta_desc': '主要时区缩写的快速参考——EST、PST、CET、IST、JST 及 50 多个其他。包含 UTC 偏移、夏令时变体及使用各缩写的城市。',
        'keywords': '时区缩写,EST PST CST MST,UTC 偏移速查表,时区代码列表,时区首字母缩写,夏令时缩写',
        'h1': '时区缩写速查表',
        'content': '''<p>你在航班确认单上看到"EST",会议邀请里看到"CET",日志文件里看到"IST"。每个缩写都代表一个具体的 UTC 偏移,但有些在夏冬季意义不同。这张速查表给你确切偏移、主要城市,以及夏令时是否会改变它。</p>
<h2>北美时区</h2>
<table class="tz-table"><thead><tr><th>缩写</th><th>全称</th><th>UTC 偏移</th><th>夏令时变体</th><th>主要城市</th></tr></thead>
<tbody><tr><td>EST</td><td>Eastern Standard Time</td><td>UTC-5</td><td>EDT (UTC-4)</td><td>纽约、多伦多、迈阿密、亚特兰大</td></tr>
<tr><td>EDT</td><td>Eastern Daylight Time</td><td>UTC-4</td><td>EST (冬季)</td><td>相同城市,3-11月</td></tr>
<tr><td>CST</td><td>Central Standard Time</td><td>UTC-6</td><td>CDT (UTC-5)</td><td>芝加哥、达拉斯、墨西哥城、休斯顿</td></tr>
<tr><td>CDT</td><td>Central Daylight Time</td><td>UTC-5</td><td>CST (冬季)</td><td>相同城市,3-11月</td></tr>
<tr><td>MST</td><td>Mountain Standard Time</td><td>UTC-7</td><td>MDT (UTC-6)</td><td>丹佛、凤凰城*、埃德蒙顿、埃尔帕索</td></tr>
<tr><td>MDT</td><td>Mountain Daylight Time</td><td>UTC-6</td><td>MST (冬季)</td><td>相同城市(除亚利桑那)</td></tr>
<tr><td>PST</td><td>Pacific Standard Time</td><td>UTC-8</td><td>PDT (UTC-7)</td><td>洛杉矶、温哥华、西雅图、蒂华纳</td></tr>
<tr><td>PDT</td><td>Pacific Daylight Time</td><td>UTC-7</td><td>PST (冬季)</td><td>相同城市,3-11月</td></tr>
<tr><td>AKST</td><td>Alaska Standard Time</td><td>UTC-9</td><td>AKDT (UTC-8)</td><td>安克雷奇、费尔班克斯、朱诺</td></tr>
<tr><td>HST</td><td>Hawaii-Aleutian Standard Time</td><td>UTC-10</td><td>无夏令时</td><td>檀香山、希洛、阿达克</td></tr></tbody></table>
<p><small>* 亚利桑那州(纳瓦霍族保留地除外)不实行夏令时,全年使用 MST。</small></p>
<h2>大西洋和南美时区</h2>
<table class="tz-table"><thead><tr><th>缩写</th><th>全称</th><th>UTC 偏移</th><th>夏令时变体</th><th>主要城市</th></tr></thead>
<tbody><tr><td>AST</td><td>Atlantic Standard Time</td><td>UTC-4</td><td>ADT (UTC-3)</td><td>哈利法克斯、圣胡安、百慕大、加拉加斯</td></tr>
<tr><td>BRT</td><td>Brasilia Time</td><td>UTC-3</td><td>2019年后无夏令时</td><td>圣保罗、里约热内卢、巴西利亚</td></tr>
<tr><td>ART</td><td>Argentina Time</td><td>UTC-3</td><td>2009年后无夏令时</td><td>布宜诺斯艾利斯、科尔多瓦、罗萨里奥</td></tr>
<tr><td>CLT</td><td>Chile Standard Time</td><td>UTC-4</td><td>CLST (UTC-3)</td><td>圣地亚哥、瓦尔帕莱索、康塞普西翁</td></tr></tbody></table>
<h2>欧洲和非洲时区</h2>
<table class="tz-table"><thead><tr><th>缩写</th><th>全称</th><th>UTC 偏移</th><th>夏令时变体</th><th>主要城市</th></tr></thead>
<tbody><tr><td>GMT</td><td>Greenwich Mean Time</td><td>UTC+0</td><td>BST (UTC+1)</td><td>伦敦、都柏林、里斯本(冬季)</td></tr>
<tr><td>BST</td><td>British Summer Time</td><td>UTC+1</td><td>GMT (冬季)</td><td>伦敦、都柏林、爱丁堡(夏季)</td></tr>
<tr><td>WET</td><td>Western European Time</td><td>UTC+0</td><td>WEST (UTC+1)</td><td>里斯本、卡萨布兰卡、雷克雅未克</td></tr>
<tr><td>CET</td><td>Central European Time</td><td>UTC+1</td><td>CEST (UTC+2)</td><td>巴黎、柏林、罗马、马德里、华沙</td></tr>
<tr><td>CEST</td><td>Central European Summer Time</td><td>UTC+2</td><td>CET (冬季)</td><td>相同城市,3-10月</td></tr>
<tr><td>EET</td><td>Eastern European Time</td><td>UTC+2</td><td>EEST (UTC+3)</td><td>赫尔辛基、基辅、布加勒斯特、开罗</td></tr>
<tr><td>MSK</td><td>Moscow Standard Time</td><td>UTC+3</td><td>2014年后无夏令时</td><td>莫斯科、圣彼得堡、伊斯坦布尔、明斯克</td></tr>
<tr><td>SAST</td><td>South Africa Standard Time</td><td>UTC+2</td><td>无夏令时</td><td>约翰内斯堡、开普敦、德班</td></tr>
<tr><td>WAT</td><td>West Africa Time</td><td>UTC+1</td><td>无夏令时</td><td>拉各斯、金沙萨、阿尔及尔</td></tr></tbody></table>
<h2>中东和中亚时区</h2>
<table class="tz-table"><thead><tr><th>缩写</th><th>全称</th><th>UTC 偏移</th><th>夏令时变体</th><th>主要城市</th></tr></thead>
<tbody><tr><td>GST</td><td>Gulf Standard Time</td><td>UTC+4</td><td>无夏令时</td><td>迪拜、阿布扎比、马斯喀特、多哈</td></tr>
<tr><td>AST</td><td>Arabia Standard Time</td><td>UTC+3</td><td>无夏令时</td><td>利雅得、吉达、科威特城、马纳马</td></tr>
<tr><td>IRST</td><td>Iran Standard Time</td><td>UTC+3:30</td><td>IRDT (UTC+4:30)</td><td>德黑兰、马什哈德、伊斯法罕</td></tr>
<tr><td>AFT</td><td>Afghanistan Time</td><td>UTC+4:30</td><td>无夏令时</td><td>喀布尔、赫拉特、马扎里沙里夫</td></tr>
<tr><td>PKT</td><td>Pakistan Standard Time</td><td>UTC+5</td><td>无夏令时</td><td>卡拉奇、拉合尔、伊斯兰堡</td></tr></tbody></table>
<h2>南亚和东南亚时区</h2>
<table class="tz-table"><thead><tr><th>缩写</th><th>全称</th><th>UTC 偏移</th><th>夏令时变体</th><th>主要城市</th></tr></thead>
<tbody><tr><td>IST</td><td>India Standard Time</td><td>UTC+5:30</td><td>无夏令时</td><td>孟买、德里、班加罗尔、加尔各答、金奈</td></tr>
<tr><td>NPT</td><td>Nepal Time</td><td>UTC+5:45</td><td>无夏令时</td><td>加德满都、博卡拉、比拉特纳加尔</td></tr>
<tr><td>BST</td><td>Bangladesh Standard Time</td><td>UTC+6</td><td>无夏令时</td><td>达卡、吉大港、锡尔赫特</td></tr>
<tr><td>MMT</td><td>Myanmar Time</td><td>UTC+6:30</td><td>无夏令时</td><td>仰光、曼德勒、内比都</td></tr>
<tr><td>ICT</td><td>Indochina Time</td><td>UTC+7</td><td>无夏令时</td><td>曼谷、河内、雅加达*、金边</td></tr>
<tr><td>WIB</td><td>Western Indonesian Time</td><td>UTC+7</td><td>无夏令时</td><td>雅加达、万隆、泗水</td></tr>
<tr><td>CST</td><td>China Standard Time</td><td>UTC+8</td><td>无夏令时</td><td>北京、上海、香港、台北</td></tr>
<tr><td>SGT</td><td>Singapore Time</td><td>UTC+8</td><td>无夏令时</td><td>新加坡、吉隆坡、马尼拉、珀斯</td></tr></tbody></table>
<p><small>* 雅加达使用 WIB (UTC+7),而非 ICT。</small></p>
<h2>东亚和太平洋时区</h2>
<table class="tz-table"><thead><tr><th>缩写</th><th>全称</th><th>UTC 偏移</th><th>夏令时变体</th><th>主要城市</th></tr></thead>
<tbody><tr><td>JST</td><td>Japan Standard Time</td><td>UTC+9</td><td>无夏令时</td><td>东京、大阪、首尔*、平壤*</td></tr>
<tr><td>KST</td><td>Korea Standard Time</td><td>UTC+9</td><td>无夏令时</td><td>首尔、釜山、仁川</td></tr>
<tr><td>AWST</td><td>Australian Western Standard Time</td><td>UTC+8</td><td>无夏令时</td><td>珀斯、布鲁姆、卡拉萨</td></tr>
<tr><td>ACST</td><td>Australian Central Standard Time</td><td>UTC+9:30</td><td>ACDT (UTC+10:30)</td><td>阿德莱德、达尔文、爱丽丝泉</td></tr>
<tr><td>AEST</td><td>Australian Eastern Standard Time</td><td>UTC+10</td><td>AEDT (UTC+11)</td><td>悉尼、墨尔本、布里斯班*、堪培拉</td></tr>
<tr><td>NZST</td><td>New Zealand Standard Time</td><td>UTC+12</td><td>NZDT (UTC+13)</td><td>奥克兰、惠灵顿、克赖斯特彻奇</td></tr></tbody></table>
<p><small>* 首尔和用平壤使用 KST,而非 JST。* 布里斯班(昆士兰)不实行夏令时。</small></p>
<h2>歧义缩写 — 请注意</h2>
<p>有些缩写根据上下文代表不同的时区:</p>
<ul><li><strong>CST</strong> — Central Standard Time (UTC-6,北美) <em>或</em> China Standard Time (UTC+8) <em>或</em> Cuba Standard Time (UTC-5)</li>
<li><strong>IST</strong> — India Standard Time (UTC+5:30) <em>或</em> Irish Standard Time (UTC+1,夏季) <em>或</em> Israel Standard Time (UTC+2)</li>
<li><strong>PST</strong> — Pacific Standard Time (UTC-8) <em>或</em> Philippine Standard Time (UTC+8)</li>
<li><strong>BST</strong> — British Summer Time (UTC+1) <em>或</em> Bangladesh Standard Time (UTC+6) <em>或</em> Bougainville Standard Time (UTC+11)</li>
<li><strong>AST</strong> — Atlantic Standard Time (UTC-4) <em>或</em> Arabia Standard Time (UTC+3) <em>或</em> Amazon Standard Time (UTC-4,巴西)</li></ul>
<p>看到歧义代码时,查看旁边的国家或城市名。要精确换算,请用我们的 <a href="/zh/time-zone-converter.html">时区转换器</a>,它能正确处理所有这些情况。</p>
<h2>快速参考:夏令时切换日期(典型)</h2>
<ul><li><strong>北美</strong>:3月第2个周日→11月第1个周日</li>
<li><strong>欧洲</strong>:3月最后一个周日→10月最后一个周日</li>
<li><strong>澳大利亚(东南部)</strong>:10月第1个周日→4月第1个周日</li>
<li><strong>新西兰</strong>:9月最后一个周日→4月第1个周日</li>
<li><strong>智利</strong>:9月第1个周日→4月第1个周日</li>
<li><strong>巴拉圭</strong>:10月第1个周日→3月最后一个周日</li></ul>
<h2>收藏此页,使用工具</h2>
<p>你不需要背下 50 多个代码。收藏此页做查阅表。当你需要特定日期的精确换算——尤其是夏令时过渡周——请用我们的 <a href="/zh/time-difference.html">时差计算器</a> 或 <a href="/zh/meeting-planner.html">会议规划器</a>。它们使用 IANA 时区数据库,每个偏移都是最新且正确的。</p>''',
    },
    'it': {
        'title': 'Scheda di riferimento per le abbreviazioni dei fusi orari (2026)',
        'meta_desc': 'Riferimento rapido per tutte le principali abbreviazioni dei fusi orari - EST, PST, CET, IST, JST e 50 altre. Include offset UTC, varianti ora legale e le città che usano ciascuna.',
        'keywords': 'abbreviazioni fusi orari, EST PST CST MST, foglio trucco offset UTC, lista codici fuso orario, acronimi fuso orario, abbreviazioni ora legale',
        'h1': 'Scheda di riferimento per le abbreviazioni dei fusi orari',
        'content': '''<p>Vedi "EST" su una conferma di volo, "CET" in un invito a una riunione, "IST" in un file di log. Ogni abbreviazione significa un offset specifico da UTC, ma alcune significano cose diverse d'estate versus d'inverno. Questa scheda ti dà l'offset esatto, le città principali e se l'ora legale lo sposta.</p>
<h2>Fusi Orari Nordamericani</h2>
<table class="tz-table"><thead><tr><th>ABBREV</th><th>Nome Completo</th><th>Offset UTC</th><th>Variante Ora Legale</th><th>Città Principali</th></tr></thead>
<tbody><tr><td>EST</td><td>Eastern Standard Time</td><td>UTC-5</td><td>EDT (UTC-4)</td><td>New York, Toronto, Miami, Atlanta</td></tr>
<tr><td>EDT</td><td>Eastern Daylight Time</td><td>UTC-4</td><td>EST (inverno)</td><td>Stesse città, marzo-novembre</td></tr>
<tr><td>CST</td><td>Central Standard Time</td><td>UTC-6</td><td>CDT (UTC-5)</td><td>Chicago, Dallas, Città del Messico, Houston</td></tr>
<tr><td>CDT</td><td>Central Daylight Time</td><td>UTC-5</td><td>CST (inverno)</td><td>Stesse città, marzo-novembre</td></tr>
<tr><td>MST</td><td>Mountain Standard Time</td><td>UTC-7</td><td>MDT (UTC-6)</td><td>Denver, Phoenix*, Edmonton, El Paso</td></tr>
<tr><td>MDT</td><td>Mountain Daylight Time</td><td>UTC-6</td><td>MST (inverno)</td><td>Stesse città (eccetto Arizona)</td></tr>
<tr><td>PST</td><td>Pacific Standard Time</td><td>UTC-8</td><td>PDT (UTC-7)</td><td>Los Angeles, Vancouver, Seattle, Tijuana</td></tr>
<tr><td>PDT</td><td>Pacific Daylight Time</td><td>UTC-7</td><td>PST (inverno)</td><td>Stesse città, marzo-novembre</td></tr>
<tr><td>AKST</td><td>Alaska Standard Time</td><td>UTC-9</td><td>AKDT (UTC-8)</td><td>Anchorage, Fairbanks, Juneau</td></tr>
<tr><td>HST</td><td>Hawaii-Aleutian Standard Time</td><td>UTC-10</td><td>Nessuna ora legale</td><td>Honolulu, Hilo, Adak</td></tr></tbody></table>
<p><small>* Arizona (eccetto Nazione Navajo) non osserva l'ora legale e resta su MST tutto l'anno.</small></p>
<h2>Fusi Orari dell'Atlantico e Sudamericani</h2>
<table class="tz-table"><thead><tr><th>ABBREV</th><th>Nome Completo</th><th>Offset UTC</th><th>Variante Ora Legale</th><th>Città Principali</th></tr></thead>
<tbody><tr><td>AST</td><td>Atlantic Standard Time</td><td>UTC-4</td><td>ADT (UTC-3)</td><td>Halifax, San Juan, Bermuda, Caracas</td></tr>
<tr><td>BRT</td><td>Brasilia Time</td><td>UTC-3</td><td>Nessuna ora legale dal 2019</td><td>São Paulo, Rio de Janeiro, Brasilia</td></tr>
<tr><td>ART</td><td>Argentina Time</td><td>UTC-3</td><td>Nessuna ora legale dal 2009</td><td>Buenos Aires, Córdoba, Rosario</td></tr>
<tr><td>CLT</td><td>Chile Standard Time</td><td>UTC-4</td><td>CLST (UTC-3)</td><td>Santiago, Valparaíso, Concepción</td></tr></tbody></table>
<h2>Fusi Orari Europei e Africani</h2>
<table class="tz-table"><thead><tr><th>ABBREV</th><th>Nome Completo</th><th>Offset UTC</th><th>Variante Ora Legale</th><th>Città Principali</th></tr></thead>
<tbody><tr><td>GMT</td><td>Greenwich Mean Time</td><td>UTC+0</td><td>BST (UTC+1)</td><td>Londra, Dublino, Lisbona (inverno)</td></tr>
<tr><td>BST</td><td>British Summer Time</td><td>UTC+1</td><td>GMT (inverno)</td><td>Londra, Dublino, Edimburgo (estate)</td></tr>
<tr><td>WET</td><td>Western European Time</td><td>UTC+0</td><td>WEST (UTC+1)</td><td>Lisbona, Casablanca, Reykjavik</td></tr>
<tr><td>CET</td><td>Central European Time</td><td>UTC+1</td><td>CEST (UTC+2)</td><td>Parigi, Berlino, Roma, Madrid, Varsavia</td></tr>
<tr><td>CEST</td><td>Central European Summer Time</td><td>UTC+2</td><td>CET (inverno)</td><td>Stesse città, marzo-ottobre</td></tr>
<tr><td>EET</td><td>Eastern European Time</td><td>UTC+2</td><td>EEST (UTC+3)</td><td>Helsinki, Kiev, Bucarest, Il Cairo</td></tr>
<tr><td>MSK</td><td>Moscow Standard Time</td><td>UTC+3</td><td>Nessuna ora legale dal 2014</td><td>Mosca, San Pietroburgo, Istanbul, Minsk</td></tr>
<tr><td>SAST</td><td>South Africa Standard Time</td><td>UTC+2</td><td>Nessuna ora legale</td><td>Johannesburg, Città del Capo, Durban</td></tr>
<tr><td>WAT</td><td>West Africa Time</td><td>UTC+1</td><td>Nessuna ora legale</td><td>Lagos, Kinshasa, Algeri</td></tr></tbody></table>
<h2>Fusi Orari del Medio Oriente e Asia Centrale</h2>
<table class="tz-table"><thead><tr><th>ABBREV</th><th>Nome Completo</th><th>Offset UTC</th><th>Variante Ora Legale</th><th>Città Principali</th></tr></thead>
<tbody><tr><td>GST</td><td>Gulf Standard Time</td><td>UTC+4</td><td>Nessuna ora legale</td><td>Dubai, Abu Dhabi, Muscat, Doha</td></tr>
<tr><td>AST</td><td>Arabia Standard Time</td><td>UTC+3</td><td>Nessuna ora legale</td><td>Riyadh, Gedda, Città del Kuwait, Manama</td></tr>
<tr><td>IRST</td><td>Iran Standard Time</td><td>UTC+3:30</td><td>IRDT (UTC+4:30)</td><td>Tehran, Mashhad, Isfahan</td></tr>
<tr><td>AFT</td><td>Afghanistan Time</td><td>UTC+4:30</td><td>Nessuna ora legale</td><td>Kabul, Herat, Mazar-i-Sharif</td></tr>
<tr><td>PKT</td><td>Pakistan Standard Time</td><td>UTC+5</td><td>Nessuna ora legale</td><td>Karachi, Lahore, Islamabad</td></tr></tbody></table>
<h2>Fusi Orari dell'Asia Meridionale e Sudorientale</h2>
<table class="tz-table"><thead><tr><th>ABBREV</th><th>Nome Completo</th><th>Offset UTC</th><th>Variante Ora Legale</th><th>Città Principali</th></tr></thead>
<tbody><tr><td>IST</td><td>India Standard Time</td><td>UTC+5:30</td><td>Nessuna ora legale</td><td>Mumbai, Delhi, Bangalore, Kolkata, Chennai</td></tr>
<tr><td>NPT</td><td>Nepal Time</td><td>UTC+5:45</td><td>Nessuna ora legale</td><td>Kathmandu, Pokhara, Biratnagar</td></tr>
<tr><td>BST</td><td>Bangladesh Standard Time</td><td>UTC+6</td><td>Nessuna ora legale</td><td>Dacca, Chittagong, Sylhet</td></tr>
<tr><td>MMT</td><td>Myanmar Time</td><td>UTC+6:30</td><td>Nessuna ora legale</td><td>Yangon, Mandalay, Naypyidaw</td></tr>
<tr><td>ICT</td><td>Indochina Time</td><td>UTC+7</td><td>Nessuna ora legale</td><td>Bangkok, Hanoi, Giacarta*, Phnom Penh</td></tr>
<tr><td>WIB</td><td>Western Indonesian Time</td><td>UTC+7</td><td>Nessuna ora legale</td><td>Giacarta, Bandung, Surabaya</td></tr>
<tr><td>CST</td><td>China Standard Time</td><td>UTC+8</td><td>Nessuna ora legale</td><td>Pechino, Shanghai, Hong Kong, Taipei</td></tr>
<tr><td>SGT</td><td>Singapore Time</td><td>UTC+8</td><td>Nessuna ora legale</td><td>Singapore, Kuala Lumpur, Manila, Perth</td></tr></tbody></table>
<p><small>* Giacarta usa WIB (UTC+7), non ICT.</small></p>
<h2>Fusi Orari dell'Asia Orientale e del Pacifico</h2>
<table class="tz-table"><thead><tr><th>ABBREV</th><th>Nome Completo</th><th>Offset UTC</th><th>Variante Ora Legale</th><th>Città Principali</th></tr></thead>
<tbody><tr><td>JST</td><td>Japan Standard Time</td><td>UTC+9</td><td>Nessuna ora legale</td><td>Tokyo, Osaka, Seul*, Pyongyang*</td></tr>
<tr><td>KST</td><td>Korea Standard Time</td><td>UTC+9</td><td>Nessuna ora legale</td><td>Seul, Busan, Incheon</td></tr>
<tr><td>AWST</td><td>Australian Western Standard Time</td><td>UTC+8</td><td>Nessuna ora legale</td><td>Perth, Broome, Karratha</td></tr>
<tr><td>ACST</td><td>Australian Central Standard Time</td><td>UTC+9:30</td><td>ACDT (UTC+10:30)</td><td>Adelaide, Darwin, Alice Springs</td></tr>
<tr><td>AEST</td><td>Australian Eastern Standard Time</td><td>UTC+10</td><td>AEDT (UTC+11)</td><td>Sydney, Melbourne, Brisbane*, Canberra</td></tr>
<tr><td>NZST</td><td>New Zealand Standard Time</td><td>UTC+12</td><td>NZDT (UTC+13)</td><td>Auckland, Wellington, Christchurch</td></tr></tbody></table>
<p><small>* Seul e Pyongyang usano KST, non JST. * Brisbane (Queensland) non osserva l'ora legale.</small></p>
<h2>Abbreviazioni Ambigue — Attenzione</h2>
<p>Alcune abbreviazioni significano zone diverse a seconda del contesto:</p>
<ul><li><strong>CST</strong> — Central Standard Time (UTC-6, Nord America) <em>o</em> China Standard Time (UTC+8) <em>o</em> Cuba Standard Time (UTC-5)</li>
<li><strong>IST</strong> — India Standard Time (UTC+5:30) <em>o</em> Irish Standard Time (UTC+1, estate) <em>o</em> Israel Standard Time (UTC+2)</li>
<li><strong>PST</strong> — Pacific Standard Time (UTC-8) <em>o</em> Philippine Standard Time (UTC+8)</li>
<li><strong>BST</strong> — British Summer Time (UTC+1) <em>o</em> Bangladesh Standard Time (UTC+6) <em>o</em> Bougainville Standard Time (UTC+11)</li>
<li><strong>AST</strong> — Atlantic Standard Time (UTC-4) <em>o</em> Arabia Standard Time (UTC+3) <em>o</em> Amazon Standard Time (UTC-4, Brasile)</li></ul>
<p>Quando vedi un codice ambiguo, controlla il paese o la città vicina. Per conversioni esatte, usa il nostro <a href="/it/time-zone-converter.html">convertitore di fusi orari</a> che gestisce correttamente tutti questi casi.</p>
<h2>Riferimento Rapido: Date Cambio Ora Legale (Tipiche)</h2>
<ul><li><strong>Nord America</strong>: 2ª domenica di marzo → 1ª domenica di novembre</li>
<li><strong>Europa</strong>: ultima domenica di marzo → ultima domenica di ottobre</li>
<li><strong>Australia (sudest)</strong>: 1ª domenica di ottobre → 1ª domenica di aprile</li>
<li><strong>Nuova Zelanda</strong>: ultima domenica di settembre → 1ª domenica di aprile</li>
<li><strong>Cile</strong>: 1ª domenica di settembre → 1ª domenica di aprile</li>
<li><strong>Paraguay</strong>: 1ª domenica di ottobre → ultima domenica di marzo</li></ul>
<h2>Salva Questa Pagina, Usa lo Strumento</h2>
<p>Non devi memorizzare 50+ codici. Salva questa pagina per la tabella di consultazione. Quando ti serve una conversione esatta per una data specifica — soprattutto durante le settimane di transizione dell'ora legale — usa il nostro <a href="/it/time-difference.html">calcolatore di differenza oraria</a> o <a href="/it/meeting-planner.html">pianificatore di riunioni</a>. Usano il database IANA dei fusi orari quindi ogni offset è aggiornato e corretto.</p>''',
    },
    'de': {
        'title': 'Zeitzone-Abkürzungen Spickzettel (2026)',
        'meta_desc': 'Schnellreferenz für alle wichtigen Zeitzonen-Abkürzungen — EST, PST, CET, IST, JST und 50 mehr. Enthält UTC-Offsets, Sommerzeit-Varianten und die Städte, die jede nutzen.',
        'keywords': 'zeitzonen-abkürzungen, EST PST CST MST, UTC-offsets spickzettel, zeitzonen-codes liste, zeitzonen-akronyme, sommerzeit-abkürzungen',
        'h1': 'Zeitzone-Abkürzungen Spickzettel',
        'content': '''<p>Du siehst "EST" auf einer Flugbestätigung, "CET" in einer Meeting-Einladung, "IST" in einer Log-Datei. Jede Abkürzung steht für einen spezifischen Offset zu UTC, aber manche bedeuten im Sommer etwas anderes als im Winter. Dieser Spickzettel gibt dir den exakten Offset, die Hauptstädte und ob die Sommerzeit ihn verschiebt.</p>
<h2>Nordamerikanische Zeitzonen</h2>
<table class="tz-table"><thead><tr><th>Abk.</th><th>Vollständiger Name</th><th>UTC-Offset</th><th>Sommerzeit-Variante</th><th>Hauptstädte</th></tr></thead>
<tbody><tr><td>EST</td><td>Eastern Standard Time</td><td>UTC-5</td><td>EDT (UTC-4)</td><td>New York, Toronto, Miami, Atlanta</td></tr>
<tr><td>EDT</td><td>Eastern Daylight Time</td><td>UTC-4</td><td>EST (Winter)</td><td>Gleiche Städte, März-November</td></tr>
<tr><td>CST</td><td>Central Standard Time</td><td>UTC-6</td><td>CDT (UTC-5)</td><td>Chicago, Dallas, Mexiko-Stadt, Houston</td></tr>
<tr><td>CDT</td><td>Central Daylight Time</td><td>UTC-5</td><td>CST (Winter)</td><td>Gleiche Städte, März-November</td></tr>
<tr><td>MST</td><td>Mountain Standard Time</td><td>UTC-7</td><td>MDT (UTC-6)</td><td>Denver, Phoenix*, Edmonton, El Paso</td></tr>
<tr><td>MDT</td><td>Mountain Daylight Time</td><td>UTC-6</td><td>MST (Winter)</td><td>Gleiche Städte (außer Arizona)</td></tr>
<tr><td>PST</td><td>Pacific Standard Time</td><td>UTC-8</td><td>PDT (UTC-7)</td><td>Los Angeles, Vancouver, Seattle, Tijuana</td></tr>
<tr><td>PDT</td><td>Pacific Daylight Time</td><td>UTC-7</td><td>PST (Winter)</td><td>Gleiche Städte, März-November</td></tr>
<tr><td>AKST</td><td>Alaska Standard Time</td><td>UTC-9</td><td>AKDT (UTC-8)</td><td>Anchorage, Fairbanks, Juneau</td></tr>
<tr><td>HST</td><td>Hawaii-Aleutian Standard Time</td><td>UTC-10</td><td>Keine Sommerzeit</td><td>Honolulu, Hilo, Adak</td></tr></tbody></table>
<p><small>* Arizona (außer Navajo-Reservat) stellt nicht auf Sommerzeit um und bleibt ganzjährig auf MST.</small></p>
<h2>Atlantik & Südamerikanische Zeitzonen</h2>
<table class="tz-table"><thead><tr><th>Abk.</th><th>Vollständiger Name</th><th>UTC-Offset</th><th>Sommerzeit-Variante</th><th>Hauptstädte</th></tr></thead>
<tbody><tr><td>AST</td><td>Atlantic Standard Time</td><td>UTC-4</td><td>ADT (UTC-3)</td><td>Halifax, San Juan, Bermuda, Caracas</td></tr>
<tr><td>BRT</td><td>Brasilia Time</td><td>UTC-3</td><td>Keine Sommerzeit seit 2019</td><td>São Paulo, Rio de Janeiro, Brasilia</td></tr>
<tr><td>ART</td><td>Argentina Time</td><td>UTC-3</td><td>Keine Sommerzeit seit 2009</td><td>Buenos Aires, Córdoba, Rosario</td></tr>
<tr><td>CLT</td><td>Chile Standard Time</td><td>UTC-4</td><td>CLST (UTC-3)</td><td>Santiago, Valparaíso, Concepción</td></tr></tbody></table>
<h2>Europäische & Afrikanische Zeitzonen</h2>
<table class="tz-table"><thead><tr><th>Abk.</th><th>Vollständiger Name</th><th>UTC-Offset</th><th>Sommerzeit-Variante</th><th>Hauptstädte</th></tr></thead>
<tbody><tr><td>GMT</td><td>Greenwich Mean Time</td><td>UTC+0</td><td>BST (UTC+1)</td><td>London, Dublin, Lissabon (Winter)</td></tr>
<tr><td>BST</td><td>British Summer Time</td><td>UTC+1</td><td>GMT (Winter)</td><td>London, Dublin, Edinburgh (Sommer)</td></tr>
<tr><td>WET</td><td>Western European Time</td><td>UTC+0</td><td>WEST (UTC+1)</td><td>Lissabon, Casablanca, Reykjavik</td></tr>
<tr><td>CET</td><td>Central European Time</td><td>UTC+1</td><td>CEST (UTC+2)</td><td>Paris, Berlin, Rom, Madrid, Warschau</td></tr>
<tr><td>CEST</td><td>Central European Summer Time</td><td>UTC+2</td><td>CET (Winter)</td><td>Gleiche Städte, März-Oktober</td></tr>
<tr><td>EET</td><td>Eastern European Time</td><td>UTC+2</td><td>EEST (UTC+3)</td><td>Helsinki, Kiew, Bukarest, Kairo</td></tr>
<tr><td>MSK</td><td>Moscow Standard Time</td><td>UTC+3</td><td>Keine Sommerzeit seit 2014</td><td>Moskau, St. Petersburg, Istanbul, Minsk</td></tr>
<tr><td>SAST</td><td>South Africa Standard Time</td><td>UTC+2</td><td>Keine Sommerzeit</td><td>Johannesburg, Kapstadt, Durban</td></tr>
<tr><td>WAT</td><td>West Africa Time</td><td>UTC+1</td><td>Keine Sommerzeit</td><td>Lagos, Kinshasa, Algier</td></tr></tbody></table>
<h2>Nahöstliche & Zentralasiatische Zeitzonen</h2>
<table class="tz-table"><thead><tr><th>Abk.</th><th>Vollständiger Name</th><th>UTC-Offset</th><th>Sommerzeit-Variante</th><th>Hauptstädte</th></tr></thead>
<tbody><tr><td>GST</td><td>Gulf Standard Time</td><td>UTC+4</td><td>Keine Sommerzeit</td><td>Dubai, Abu Dhabi, Maskat, Doha</td></tr>
<tr><td>AST</td><td>Arabia Standard Time</td><td>UTC+3</td><td>Keine Sommerzeit</td><td>Riad, Dschidda, Kuwait-Stadt, Manama</td></tr>
<tr><td>IRST</td><td>Iran Standard Time</td><td>UTC+3:30</td><td>IRDT (UTC+4:30)</td><td>Teheran, Mashhad, Isfahan</td></tr>
<tr><td>AFT</td><td>Afghanistan Time</td><td>UTC+4:30</td><td>Keine Sommerzeit</td><td>Kabul, Herat, Mazar-i-Sharif</td></tr>
<tr><td>PKT</td><td>Pakistan Standard Time</td><td>UTC+5</td><td>Keine Sommerzeit</td><td>Karachi, Lahore, Islamabad</td></tr></tbody></table>
<h2>Süd- & Südostasiatische Zeitzonen</h2>
<table class="tz-table"><thead><tr><th>Abk.</th><th>Vollständiger Name</th><th>UTC-Offset</th><th>Sommerzeit-Variante</th><th>Hauptstädte</th></tr></thead>
<tbody><tr><td>IST</td><td>India Standard Time</td><td>UTC+5:30</td><td>Keine Sommerzeit</td><td>Mumbai, Delhi, Bangalore, Kolkata, Chennai</td></tr>
<tr><td>NPT</td><td>Nepal Time</td><td>UTC+5:45</td><td>Keine Sommerzeit</td><td>Kathmandu, Pokhara, Biratnagar</td></tr>
<tr><td>BST</td><td>Bangladesh Standard Time</td><td>UTC+6</td><td>Keine Sommerzeit</td><td>Dhaka, Chittagong, Sylhet</td></tr>
<tr><td>MMT</td><td>Myanmar Time</td><td>UTC+6:30</td><td>Keine Sommerzeit</td><td>Yangon, Mandalay, Naypyidaw</td></tr>
<tr><td>ICT</td><td>Indochina Time</td><td>UTC+7</td><td>Keine Sommerzeit</td><td>Bangkok, Hanoi, Jakarta*, Phnom Penh</td></tr>
<tr><td>WIB</td><td>Western Indonesian Time</td><td>UTC+7</td><td>Keine Sommerzeit</td><td>Jakarta, Bandung, Surabaya</td></tr>
<tr><td>CST</td><td>China Standard Time</td><td>UTC+8</td><td>Keine Sommerzeit</td><td>Peking, Shanghai, Hongkong, Taipeh</td></tr>
<tr><td>SGT</td><td>Singapore Time</td><td>UTC+8</td><td>Keine Sommerzeit</td><td>Singapur, Kuala Lumpur, Manila, Perth</td></tr></tbody></table>
<p><small>* Jakarta nutzt WIB (UTC+7), nicht ICT.</small></p>
<h2>Ostasiatische & Pazifische Zeitzonen</h2>
<table class="tz-table"><thead><tr><th>Abk.</th><th>Vollständiger Name</th><th>UTC-Offset</th><th>Sommerzeit-Variante</th><th>Hauptstädte</th></tr></thead>
<tbody><tr><td>JST</td><td>Japan Standard Time</td><td>UTC+9</td><td>Keine Sommerzeit</td><td>Tokio, Osaka, Seoul*, Pjöngjang*</td></tr>
<tr><td>KST</td><td>Korea Standard Time</td><td>UTC+9</td><td>Keine Sommerzeit</td><td>Seoul, Busan, Incheon</td></tr>
<tr><td>AWST</td><td>Australian Western Standard Time</td><td>UTC+8</td><td>Keine Sommerzeit</td><td>Perth, Broome, Karratha</td></tr>
<tr><td>ACST</td><td>Australian Central Standard Time</td><td>UTC+9:30</td><td>ACDT (UTC+10:30)</td><td>Adelaide, Darwin, Alice Springs</td></tr>
<tr><td>AEST</td><td>Australian Eastern Standard Time</td><td>UTC+10</td><td>AEDT (UTC+11)</td><td>Sydney, Melbourne, Brisbane*, Canberra</td></tr>
<tr><td>NZST</td><td>New Zealand Standard Time</td><td>UTC+12</td><td>NZDT (UTC+13)</td><td>Auckland, Wellington, Christchurch</td></tr></tbody></table>
<p><small>* Seoul und Pjöngjang nutzen KST, nicht JST. * Brisbane (Queensland) stellt nicht auf Sommerzeit um.</small></p>
<h2>Mehrdeutige Abkürzungen — Vorsicht</h2>
<p>Einige Abkürzungen bedeuten je nach Kontext verschiedene Zonen:</p>
<ul><li><strong>CST</strong> — Central Standard Time (UTC-6, Nordamerika) <em>oder</em> China Standard Time (UTC+8) <em>oder</em> Cuba Standard Time (UTC-5)</li>
<li><strong>IST</strong> — India Standard Time (UTC+5:30) <em>oder</em> Irish Standard Time (UTC+1, Sommer) <em>oder</em> Israel Standard Time (UTC+2)</li>
<li><strong>PST</strong> — Pacific Standard Time (UTC-8) <em>oder</em> Philippine Standard Time (UTC+8)</li>
<li><strong>BST</strong> — British Summer Time (UTC+1) <em>oder</em> Bangladesh Standard Time (UTC+6) <em>oder</em> Bougainville Standard Time (UTC+11)</li>
<li><strong>AST</strong> — Atlantic Standard Time (UTC-4) <em>oder</em> Arabia Standard Time (UTC+3) <em>oder</em> Amazon Standard Time (UTC-4, Brasilien)</li></ul>
<p>Wenn du einen mehrdeutigen Code siehst, prüfe den Ländernamen oder die Stadt in der Nähe. Für exakte Umrechnungen nutze unseren <a href="/de/time-zone-converter.html">Zeitzonen-Konverter</a>, der alle diese korrekt handhabt.</p>
<h2>Schnellreferenz: Sommerzeit-Umschaltdaten (Typisch)</h2>
<ul><li><strong>Nordamerika</strong>: 2. Sonntag März → 1. Sonntag November</li>
<li><strong>Europa</strong>: Letzter Sonntag März → Letzter Sonntag Oktober</li>
<li><strong>Australien (Südost)</strong>: 1. Sonntag Oktober → 1. Sonntag April</li>
<li><strong>Neuseeland</strong>: Letzter Sonntag September → 1. Sonntag April</li>
<li><strong>Chile</strong>: 1. Sonntag September → 1. Sonntag April</li>
<li><strong>Paraguay</strong>: 1. Sonntag Oktober → Letzter Sonntag März</li></ul>
<h2>Diese Seite Merken, Tool Nutzen</h2>
<p>Du musst dir nicht 50+ Codes merken. Merke dir diese Seite für die Nachschlagetabelle. Wenn du eine exakte Umrechnung für ein bestimmtes Datum brauchst — besonders in den Sommerzeit-Übergangswochen — nutze unseren <a href="/de/time-difference.html">Zeitdifferenz-Rechner</a> oder <a href="/de/meeting-planner.html">Terminplaner</a>. Sie nutzen die IANA-Zeitzonen-Datenbank, sodass jeder Offset aktuell und korrekt ist.</p>''',
    },
    'ja': {
        'title': 'タイムゾーン略語チートシート (2026)',
        'meta_desc': '主要なタイムゾーン略語のクイックリファレンス——EST、PST、CET、IST、JST およびその他 50 以上。UTC オフセット、夏時間バリエーション、各略語を使用する都市を含む。',
        'keywords': 'タイムゾーン略語,EST PST CST MST,UTC オフセット チートシート,タイムゾーンコード リスト,タイムゾーン頭字語,夏時間略語',
        'h1': 'タイムゾーン略語チートシート',
        'content': '''<p>フライトの確認で "EST"、会議の招待で "CET"、ログファイルで "IST" を見かける。各略語は UTC からの特定のオフセットを意味するが、夏と冬で異なるものもある。このチートシートでは正確なオフセット、主要都市、夏時間で変わるかどうかを示す。</p>
<h2>北米のタイムゾーン</h2>
<table class="tz-table"><thead><tr><th>略語</th><th>正式名称</th><th>UTC オフセット</th><th>夏時間バリエーション</th><th>主要都市</th></tr></thead>
<tbody><tr><td>EST</td><td>Eastern Standard Time</td><td>UTC-5</td><td>EDT (UTC-4)</td><td>ニューヨーク、トロント、マイアミ、アトランタ</td></tr>
<tr><td>EDT</td><td>Eastern Daylight Time</td><td>UTC-4</td><td>EST (冬)</td><td>同じ都市、3-11月</td></tr>
<tr><td>CST</td><td>Central Standard Time</td><td>UTC-6</td><td>CDT (UTC-5)</td><td>シカゴ、ダラス、メキシコシティ、ヒューストン</td></tr>
<tr><td>CDT</td><td>Central Daylight Time</td><td>UTC-5</td><td>CST (冬)</td