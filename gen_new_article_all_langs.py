#!/usr/bin/env python3
"""Generate 1 new article in all 12 languages + EN."""
import os
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')
BLOG_DIR = BASE / 'blog'
TEMPLATE = BLOG_DIR / 'how-to-convert-time-zones.html'

template = TEMPLATE.read_text(encoding='utf-8')

# breadcrumb labels per lang
CRUMB = {
    'en': ('Home', 'Blog'),
    'es': ('Inicio', 'Blog'),
    'zh': ('首页', '博客'),
    'it': ('Home', 'Blog'),
    'de': ('Start', 'Blog'),
    'fr': ('Accueil', 'Blog'),
    'pt': ('Início', 'Blog'),
    'ru': ('Главная', 'Блог'),
    'ja': ('ホーム', 'ブログ'),
    'uk': ('Головна', 'Блог'),
    'hi': ('होम', 'ब्लॉग'),
    'ar': ('الرئيسية', 'المدونة'),
}

META_DATE = {
    'en': '10 Oct 2026', 'es': '10 oct 2026', 'zh': '2026年10月10日',
    'it': '10 ott 2026', 'de': '10. Okt. 2026', 'fr': '10 oct. 2026',
    'pt': '10 out 2026', 'ru': '10 окт. 2026', 'ja': '2026年10月10日',
    'uk': '10 жовт. 2026', 'hi': '10 अक्टूबर 2026', 'ar': '10 أكتوبر 2026',
}
META_READ = {
    'en': '6 min read', 'es': '6 min de lectura', 'zh': '阅读 6 分钟',
    'it': '6 min di lettura', 'de': '6 Min. Lesezeit', 'fr': '6 min de lecture',
    'pt': '6 min de leitura', 'ru': '6 мин. чтения', 'ja': '読む時間 6 分',
    'uk': '6 хв. читання', 'hi': 'पढ़ने में 6 मिनट', 'ar': '٦ دقائق للقراءة',
}
SKIP = {
    'en': 'Skip to main content', 'es': 'Saltar al contenido principal',
    'zh': '跳到主要内容', 'it': 'Vai al contenuto principale',
    'de': 'Zum Hauptinhalt springen', 'fr': 'Aller au contenu principal',
    'pt': 'Pular para o conteúdo principal', 'ru': 'Перейти к основному контенту',
    'ja': 'メインコンテンツへスキップ', 'uk': 'Перейти до основного вмісту',
    'hi': 'मुख्य सामग्री पर जाएं', 'ar': 'تخطي إلى المحتوى الرئيسي',
}
LOADING = {
    'en': 'Loading time...', 'es': 'Cargando la hora...', 'zh': '正在加载时间...',
    'it': 'Caricamento ora...', 'de': 'Zeit wird geladen...', 'fr': 'Chargement de l\'heure...',
    'pt': 'Carregando a hora...', 'ru': 'Загрузка времени...', 'ja': '時間を読み込み中...',
    'uk': 'Завантаження часу...', 'hi': 'समय लोड हो रहा है...', 'ar': 'جاري تحميل الوقت...',
}

# Article data per language: title, meta_desc, keywords, h1, content
# Using slug: check-current-time-any-city
ARTICLES = {
    'en': {
        'title': 'How to Check the Current Time in Any City (2026)',
        'meta_desc': 'Quick ways to find the exact local time for any city worldwide, with or without an app. Covers browser tricks, world clocks, and command-line tools.',
        'keywords': 'check current time, what time is it in, world clock, time in any city, local time now',
        'h1': 'How to Check the Current Time in Any City',
        'content': '''<p>You need to know what time it is in Sydney right now - maybe for a call, a flight, or just curiosity. You do not need to install an app or remember UTC offsets. Here are the fastest ways to get an accurate answer in seconds.</p>

<h2>1. Type It in Your Browser Address Bar</h2>
<p>Most modern browsers answer time queries directly in the address bar. Just type:</p>
<blockquote><code>time in tokyo</code></blockquote>
<p>or</p>
<blockquote><code>what time is it in london</code></blockquote>
<p>Chrome, Edge, Firefox, and Safari all show the current local time above the search results. No click needed. This works for cities, time zone abbreviations (<code>time in est</code>), and even coordinates.</p>

<h2>2. Use a Dedicated World Clock Page</h2>
<p>When you need several cities at once, a world clock page beats repeated searches. Open our <a href="/">world clock</a>, pin the cities you care about, and they update every second. You get:</p>
<ul>
    <li>Live time for 700+ cities</li>
    <li>Day/night indicators</li>
    <li>UTC offsets and DST status</li>
    <li>Shareable links with your city set pre-selected</li>
</ul>
<p>Bookmark it once and you never search for "current time in" again.</p>

<h2>3. Voice Assistants (Phone, Watch, Smart Speaker)</h2>
<p>Siri, Google Assistant, and Alexa all answer "What time is it in [city]?" instantly. This is fastest when your hands are busy - cooking, driving, or already on a call.</p>

<h2>4. Command Line (For Developers)</h2>
<p>If you live in a terminal, <code>curl wttr.in/london</code> or <code>curl wttr.in/tokyo</code> returns a compact time card. The <code>date</code> command with <code>TZ</code> works too:</p>
<blockquote><code>TZ=America/New_York date</code></blockquote>
<p>No API keys, no rate limits for reasonable use.</</p>

<h2>5. Convert Between Your Time and Theirs</h2>
<p>Knowing "it's 14:00 in Tokyo" is only half the answer - you usually need "what is that for me?" Use our <a href="/time-zone-converter.html">time zone converter</a> to translate any time between any two cities, with automatic DST handling. Enter your city, their city, and the time - get the match instantly.</p>

<h2>Quick Reference: The Three Questions</h2>
<ul>
    <li><strong>One city, right now:</strong> browser address bar or voice assistant</li>
    <li><strong>Multiple cities, ongoing:</strong> pinned world clock page</li>
    <li><strong>Your time vs. their time:</strong> time zone converter</li>
</ul>
<p>All three are free, work on any device, and need zero setup. Next time someone asks "what time is it there?", you will have the answer before they finish the question.</p>'''
    },
    'es': {
        'title': 'Cómo consultar la hora actual en cualquier ciudad (2026)',
        'meta_desc': 'Formas rápidas de averiguar la hora local exacta para cualquier ciudad del mundo, con o sin aplicación. Trucos de navegador, relojes mundiales y herramientas de línea de comandos.',
        'keywords': 'consultar hora actual, qué hora es en, reloj mundial, hora en cualquier ciudad, hora local ahora',
        'h1': 'Cómo consultar la hora actual en cualquier ciudad',
        'content': '''<p>Necesitas saber qué hora es en Sídney ahora mismo - quizá para una llamada, un vuelo o simple curiosidad. No hace falta instalar una app ni recordar desfases UTC. Aquí tienes las formas más rápidas de obtener una respuesta exacta en segundos.</p>

<h2>1. Escríbelo en la barra de direcciones del navegador</h2>
<p>La mayoría de los navegadores modernos responden consultas de hora directamente en la barra de direcciones. Solo escribe:</p>
<blockquote><code>hora en tokyo</code></blockquote>
<p>o</p>
<blockquote><code>qué hora es en londres</code></blockquote>
<p>Chrome, Edge, Firefox y Safari muestran la hora local actual sobre los resultados de búsqueda. Sin hacer clic. Funciona para ciudades, abreviaturas de zona horaria (<code>hora en est</code>) e incluso coordenadas.</p>

<h2>2. Usa una página de reloj mundial dedicada</h2>
<p>Cuando necesitas varias ciudades a la vez, una página de reloj mundial gana a las búsquedas repetidas. Abre nuestro <a href="/es/">reloj mundial</a>, fija las ciudades que te interesan y se actualizan cada segundo. Obtienes:</p>
<ul>
    <li>Hora en vivo para 700+ ciudades</li>
    <li>Indicadores de día/noche</li>
    <li>Desfases UTC y estado de horario de verano</li>
    <li>Enlaces compartibles con tu selección de ciudades pre-fijada</li>
</ul>
<p>Añádela a favoritos una vez y nunca más buscarás "hora actual en".</p>

<h2>3. Asistentes de voz (móvil, reloj, altavoz inteligente)</h2>
<p>Siri, Google Assistant y Alexa responden "¿Qué hora es en [ciudad]?" al instante. Es lo más rápido cuando tienes las manos ocupadas - cocinando, conduciendo o ya en una llamada.</p>

<h2>4. Línea de comandos (para desarrolladores)</h2>
<p>Si vives en la terminal, <code>curl wttr.in/londres</code> o <code>curl wttr.in/tokyo</code> devuelven una ficha de hora compacta. El comando <code>date</code> con <code>TZ</code> también funciona:</p>
<blockquote><code>TZ=America/New_York date</code></blockquote>
<p>Sin claves API, sin límites de tasa para uso razonable.</</p>

<h2>5. Convierte entre tu hora y la de ellos</h2>
<p>Saber "son las 14:00 en Tokio" es solo media respuesta - normalmente necesitas "¿y eso a qué hora es para mí?". Usa nuestro <a href="/es/time-zone-converter.html">convertidor de zonas horarias</a> para traducir cualquier hora entre dos ciudades, con ajuste automático de horario de verano. Escribe tu ciudad, la suya y la hora - obtén la equivalencia al instante.</p>

<h2>Referencia rápida: Las tres preguntas</h2>
<ul>
    <li><strong>Una ciudad, ahora mismo:</strong> barra de direcciones del navegador o asistente de voz</li>
    <li><strong>Varias ciudades, de forma continua:</strong> página de reloj mundial fijada</li>
    <li><strong>Tu hora vs. la suya:</strong> convertidor de zonas horarias</li>
</ul>
<p>Las tres son gratis, funcionan en cualquier dispositivo y no necesitan configuración. La próxima vez que alguien pregunte "¿qué hora es allí?", tendrás la respuesta antes de que termine la pregunta.</p>'''
    },
    'zh': {
        'title': '如何查询任意城市的当前时间 (2026)',
        'meta_desc': '快速查找全球任意城市当地确切时间的方法，无需安装应用。涵盖浏览器技巧、世界时钟和命令行工具。',
        'keywords': '查询当前时间,几点了,世界时钟,任意城市时间,当地时间现在',
        'h1': '如何查询任意城市的当前时间',
        'content': '''<p>你需要马上知道悉尼现在几点——可能是为了开会、赶航班，或只是好奇。不必装应用、不必背 UTC 偏移。这里有几秒钟拿到准确答案的最快方法。</p>

<h2>1. 直接在浏览器地址栏输入</h2>
<p>现代浏览器都能在地址栏直接回答时间查询。只要输入：</p>
<blockquote><code>time in tokyo</code></blockquote>
<p>或者</p>
<blockquote><code>what time is it in london</code></blockquote>
<p>Chrome、Edge、Firefox、Safari 都会在搜索结果上方直接显示当地当前时间。不用点击。支持城市名、时区缩写（<code>time in est</code>）甚至坐标。</p>

<h2>2. 使用专门的世界时钟页面</h2>
<p>需要同时查多个城市时，世界时钟页面比反复搜索强。打开我们的 <a href="/zh/">世界时钟</a>，固定你关心的城市，它们每秒更新。你能得到：</p>
<ul>
    <li>700+ 城市的实时时间</li>
    <li>昼/夜指示</li>
    <li>UTC 偏移和夏令时状态</li>
    <li>可分享链接，预选好你的城市组合</li>
</ul>
<p>收藏一次，再也不用搜 "当前时间"。</p>

<h2>3. 语音助手（手机、手表、智能音箱）</h2>
<p>Siri、Google Assistant、Alexa 都能秒回 "What time is it in [city]?"。手忙脚乱时——做饭、开车、通话中——这是最快的。</p>

<h2>4. 命令行（开发者专用）</h2>
<p>如果你住在终端里，<code>curl wttr.in/london</code> 或 <code>curl wttr.in/tokyo</code> 返回紧凑的时间卡片。<code>date</code> 配合 <code>TZ</code> 也行：</p>
<blockquote><code>TZ=America/New_York date</code></blockquote>
<p>无需 API Key，合理用量下无频率限制。
</p>

<h2>5. 在你的时间和他们的时间之间换算</h2>
<p>知道"东京现在 14:00"只解决了一半问题——通常你需要"那我这边几点？"。用我们的 <a href="/zh/time-zone-converter.html">时区转换器</a> 把任意时间在任意两城市间换算，自动处理夏令时。输入你的城市、对方城市、时间——立刻得到对应时间。</p>

<h2>速查：三个问题</h2>
<ul>
    <li><strong>单一城市、当下：</strong>浏览器地址栏或语音助手</li>
    <li><strong>多城市、持续关注：</strong>固定的世界时钟页面</li>
    <li><strong>你的时间 vs 他们的时间：</strong>时区转换器</li>
</ul>
<p>三个全免费、全设备通用、零配置。下次谁问"那边几点了？"，你能在他问完前给出答案。</p>'''
    },
    'it': {
        'title': 'Come controllare l\'ora attuale in qualsiasi città (2026)',
        'meta_desc': 'Modi rapidi per trovare l\'ora locale esatta per qualsiasi città nel mondo, con o senza app. Trucchi del browser, orologi mondiali e strumenti a riga di comando.',
        'keywords': 'controllare ora attuale, che ora è in, orologio mondiale, ora in qualsiasi città, ora locale ora',
        'h1': 'Come controllare l\'ora attuale in qualsiasi città',
        'content': '''<p>Devi sapere che ora è a Sydney proprio ora - magari per una chiamata, un volo o semplice curiosità. Non serve installare un\'app o ricordare gli offset UTC. Ecco i modi più veloci per ottenere una risposta esatta in pochi secondi.</p>

<h2>1. Digita nella barra degli indirizzi del browser</h2>
<p>La maggior parte dei browser moderni risponde alle query sull'ora direttamente nella barra degli indirizzi. Basta digitare:</p>
<blockquote><code>time in tokyo</code></blockquote>
<p>o</p>
<blockquote><code>che ore sono a londra</code></blockquote>
<p>Chrome, Edge, Firefox e Safari mostrano l'ora locale attuale sopra i risultati di ricerca. Nessun clic necessario. Funziona per città, abbreviazioni di fuso orario (<code>time in est</code>) e persino coordinate.</p>

<h2>2. Usa una pagina dedicata di orologio mondiale</h2>
<p>Quando ti servono più città contemporaneamente, una pagina di orologio mondiale batte le ricerche ripetute. Apri il nostro <a href="/it/">orologio mondiale</a>, fissa le città che ti interessano e si aggiornano ogni secondo. Ottieni:</p>
<ul>
    <li>Ora live per 700+ città</li>
    <li>Indicatori giorno/notte</li>
    <li>Offset UTC e stato ora legale</li>
    <li>Link condivisibili con la tua selezione di città preimpostata</li>
</ul>
<p>Mettilo nei preferiti una volta e non cercherai più "ora attuale in".</p>

<h2>3. Assistenti vocali (telefono, orologio, smart speaker)</h2>
<p>Siri, Google Assistant e Alexa rispondono tutti a "Che ore sono a [città]?" all'istante. È il metodo più veloce quando hai le mani occupate - cucinando, guidando o già in chiamata.</p>

<h2>4. Riga di comando (per sviluppatori)</h2>
<p>Se vivi nel terminale, <code>curl wttr.in/londra</code> o <code>curl wttr.in/tokyo</code> restituisce una scheda oraria compatta. Il comando <code>date</code> con <code>TZ</code> funziona pure:</p>
<blockquote><code>TZ=America/New_York date</code></blockquote>
<p>Niente chiavi API, niente limiti di rate per uso ragionevole.
</p>

<h2>5. Converti tra la tua ora e la loro</h2>
<p>Sapere "sono le 14:00 a Tokyo" è solo metà della risposta - di solito ti serve "che ora è per me?". Usa il nostro <a href="/it/time-zone-converter.html">convertitore di fusi orari</a> per tradurre qualsiasi ora tra due città qualsiasi, con gestione automatica dell'ora legale. Inserisci la tua città, la loro città e l'ora - ottieni la corrispondenza istantaneamente.</p>

<h2>Riferimento rapido: Le tre domande</h2>
<ul>
    <li><strong>Una città, adesso:</strong> barra indirizzi browser o assistente vocale</li>
    <li><strong>Più città, continuo:</strong> pagina orologio mondiale fissata</li>
    <li><strong>La tua ora vs. la loro:</strong> convertitore di fusi orari</li>
</ul>
<p>Tutti e tre sono gratis, funzionano su qualsiasi dispositivo e non richiedono configurazione. La prossima volta che qualcuno chiede "che ore sono là?", avrai la risposta prima che finisca la domanda.</p>'''
    },
    'de': {
        'title': 'Aktuelle Uhrzeit in beliebiger Stadt prüfen (2026)',
        'meta_desc': 'Schnelle Wege, die genaue Ortszeit für jede Stadt weltweit zu finden - mit oder ohne App. Browser-Tricks, Weltuhren und Kommandozeilen-Tools.',
        'keywords': 'aktuelle uhrzeit prüfen, wie spät ist es in, weltuhr, uhrzeit in jeder stadt, ortszeit jetzt',
        'h1': 'Aktuelle Uhrzeit in beliebiger Stadt prüfen',
        'content': '''<p>Du musst wissen, wie spät es in Sydney gerade ist - vielleicht für einen Anruf, einen Flug oder aus Neugier. Du brauchst keine App zu installieren und keine UTC-Offsets auswendig zu kennen. Hier sind die schnellsten Wege, in Sekunden eine genaue Antwort zu bekommen.</p>

<h2>1. In die Adresszeile des Browsers tippen</h2>
<p>Die meisten modernen Browser beantworten Zeitabfragen direkt in der Adresszeile. Einfach eingeben:</p>
<blockquote><code>time in tokyo</code></blockquote>
<p>oder</p>
<blockquote><code>wie spät ist es in london</code></blockquote>
<p>Chrome, Edge, Firefox und Safari zeigen die aktuelle Ortszeit über den Suchergebnissen an. Kein Klick nötig. Das funktioniert für Städte, Zeitzonen-Abkürzungen (<code>time in est</code>) und sogar Koordinaten.</p>

<h2>2. Eine dedizierte Weltuhr-Seite nutzen</h2>
<p>Wenn du mehrere Städte gleichzeitig brauchst, schlägt eine Weltuhr-Seite wiederholte Suchen. Öffne unsere <a href="/de/">Weltuhr</a>, pinne die Städte, die dich interessieren, und sie aktualisieren sich jede Sekunde. Du bekommst:</p>
<ul>
    <li>Live-Uhrzeit für 700+ Städte</li>
    <li>Tag/Nacht-Indikatoren</li>
    <li>UTC-Offsets und Sommerzeit-Status</li>
    <li>Teilbare Links mit deiner Stadt-Auswahl vorbelegt</li>
</ul>
<p>Einmal als Lesezeichen speichern und du suchst nie wieder nach "aktuelle uhrzeit in".</p>

<h2>3. Sprachassistenten (Handy, Uhr, Smart Speaker)</h2>
<p>Siri, Google Assistant und Alexa beantworten alle "Wie spät ist es in [Stadt]?" sofort. Am schnellsten, wenn die Hände voll sind - kochen, fahren, schon im Gespräch.</p>

<h2>4. Kommandozeile (für Entwickler)</h2>
<p>Wenn du im Terminal lebst, liefert <code>curl wttr.in/london</code> oder <code>curl wttr.in/tokyo</code> eine kompakte Zeitkarte. Der <code>date</code>-Befehl mit <code>TZ</code> geht auch:</p>
<blockquote><code>TZ=America/New_York date</code></blockquote>
<p>Keine API-Keys, keine Rate-Limits bei vernünftiger Nutzung.
</p>

<h2>5. Zwischen deiner Zeit und ihrer umrechnen</h2>
<p>Zu wissen "es ist 14:00 in Tokio" ist nur die halbe Antwort - du brauchst meist "was ist das für mich?". Nutze unseren <a href="/de/time-zone-converter.html">Zeitzonen-Umrechner</a>, um jede Zeit zwischen je zwei Städten zu übersetzen, mit automatischer Sommerzeit-Behandlung. Deine Stadt, ihre Stadt, die Zeit eingeben - Treffer sofort.</p>

<h2>Kurzreferenz: Die drei Fragen</h2>
<ul>
    <li><strong>Eine Stadt, jetzt:</strong> Browser-Adresszeile oder Sprachassistent</li>
    <li><strong>Mehrere Städte, dauerhaft:</strong> gepinnte Weltuhr-Seite</li>
    <li><strong>Deine Zeit vs. ihre Zeit:</strong> Zeitzonen-Umrechner</li>
</ul>
<p>Alle drei sind kostenlos, funktionieren auf jedem Gerät und brauchen null Setup. Wenn das nächste Mal jemand fragt "wie spät ist es dort?", hast du die Antwort bevor er die Frage zu Ende stellt.</p>'''
    },
    'fr': {
        'title': 'Comment vérifier l\'heure actuelle dans n\'importe quelle ville (2026)',
        'meta_desc': 'Façons rapides de trouver l\'heure locale exacte pour n\'importe quelle ville dans le monde, avec ou sans application. Astuces de navigateur, horloges mondiales et outils en ligne de commande.',
        'keywords': 'vérifier heure actuelle, quelle heure est-il à, horloge mondiale, heure dans n\'importe quelle ville, heure locale maintenant',
        'h1': 'Comment vérifier l\'heure actuelle dans n\'importe quelle ville',
        'content': '''<p>Vous devez savoir quelle heure il est à Sydney en ce moment - peut-être pour un appel, un vol ou simple curiosité. Pas besoin d\'installer une appli ni de retenir les décalages UTC. Voici les moyens les plus rapides d\'obtenir une réponse exacte en quelques secondes.</p>

<h2>1. Tapez-le dans la barre d\'adresse du navigateur</h2>
<p>La plupart des navigateurs modernes répondent aux requêtes d\'heure directement dans la barre d\'adresse. Tapez simplement :</p>
<blockquote><code>time in tokyo</code></blockquote>
<p>ou</p>
<blockquote><code>quelle heure est-il à londres</code></blockquote>
<p>Chrome, Edge, Firefox et Safari affichent tous l\'heure locale actuelle au-dessus des résultats de recherche. Aucun clic nécessaire. Cela fonctionne pour les villes, les abréviations de fuseau horaire (<code>time in est</code>) et même les coordonnées.</p>

<h2>2. Utilisez une page d\'horloge mondiale dédiée</h2>
<p>Quand vous avez besoin de plusieurs villes à la fois, une page d\'horloge mondiale bat les recherches répétées. Ouvrez notre <a href="/fr/">horloge mondiale</a>, épinglez les villes qui vous intéressent, et elles se mettent à jour chaque seconde. Vous obtenez :</p>
<ul>
    <li>Heure en direct pour 700+ villes</li>
    <li>Indicateurs jour/nuit</li>
    <li>Décalages UTC et statut heure d\'été</li>
    <li>Liens partageables avec votre sélection de villes pré-sélectionnée</li>
</ul>
<p>Ajoutez-la aux favoris une fois et vous ne chercherez plus "heure actuelle dans".</p>

<h2>3. Assistants vocaux (téléphone, montre, enceinte connectée)</h2>
<p>Siri, Google Assistant et Alexa répondent tous à "Quelle heure est-il à [ville] ?" instantanément. C\'est le plus rapide quand vos mains sont occupées - cuisine, conduite, déjà en appel.</p>

<h2>4. Ligne de commande (pour développeurs)</h2>
<p>Si vous vivez dans un terminal, <code>curl wttr.in/londres</code> ou <code>curl wttr.in/tokyo</code> renvoie une fiche horaire compacte. La commande <code>date</code> avec <code>TZ</code> marche aussi :</p>
<blockquote><code>TZ=America/New_York date</code></blockquote>
<p>Pas de clés API, pas de limites de taux pour une utilisation raisonnable.
</p>

<h2>5. Convertir entre votre heure et la leur</h2>
<p>Savoir "il est 14:00 à Tokyo" n\'est que la moitié de la réponse - vous avez généralement besoin de "qu\'est-ce que ça fait pour moi ?". Utilisez notre <a href="/fr/time-zone-converter.html">convertisseur de fuseaux horaires</a> pour traduire n\'importe quelle heure entre deux villes quelconques, avec gestion automatique de l\'heure d\'été. Entrez votre ville, leur ville, l\'heure - obtenez la correspondance instantanément.</p>

<h2>Référence rapide : Les trois questions</h2>
<ul>
    <li><strong>Une ville, maintenant :</strong> barre d\'adresse navigateur ou assistant vocal</li>
    <li><strong>Plusieurs villes, en continu :</strong> page horloge mondiale épinglée</li>
    <li><strong>Votre heure vs. la leur :</strong> convertisseur de fuseaux horaires</li>
</ul>
<p>Tous les trois sont gratuits, fonctionnent sur n\'importe quel appareil et ne nécessitent aucune configuration. La prochaine fois que quelqu\'un demande "quelle heure il est là-bas ?", vous aurez la réponse avant qu\'il finisse la question.</p>'''
    },
    'pt': {
        'title': 'Como verificar a hora atual em qualquer cidade (2026)',
        'meta_desc': 'Formas rápidas de encontrar a hora local exata para qualquer cidade do mundo, com ou sem aplicativo. Truques do navegador, relógios mundiais e ferramentas de linha de comando.',
        'keywords': 'verificar hora atual, que horas são em, relógio mundial, hora em qualquer cidade, hora local agora',
        'h1': 'Como verificar a hora atual em qualquer cidade',
        'content': '''<p>Você precisa saber que horas são em Sydney agora mesmo - talvez para uma ligação, um voo ou simples curiosidade. Não precisa instalar um app nem lembrar deslocamentos UTC. Aqui estão as formas mais rápidas de obter uma resposta exata em segundos.</p>

<h2>1. Digite na barra de endereços do navegador</h2>
<p>A maioria dos navegadores modernos responde a consultas de hora diretamente na barra de endereços. Basta digitar:</p>
<blockquote><code>time in tokyo</code></blockquote>
<p>ou</p>
<blockquote><code>que horas são em londres</code></blockquote>
<p>Chrome, Edge, Firefox e Safari mostram a hora local atual acima dos resultados de busca. Sem clique necessário. Funciona para cidades, abreviações de fuso horário (<code>time in est</code>) e até coordenadas.</p>

<h2>2. Use uma página de relógio mundial dedicada</h2>
<p>Quando você precisa de várias cidades de uma vez, uma página de relógio mundial vence buscas repetidas. Abra nosso <a href="/pt/">relógio mundial</a>, fixe as cidades que importam e elas atualizam a cada segundo. Você obtém:</p>
<ul>
    <li>Hora ao vivo para 700+ cidades</li>
    <li>Indicadores dia/noite</li>
    <li>Deslocamentos UTC e status de horário de verão</li>
    <li>Links compartilháveis com sua seleção de cidades pré-definida</li>
</ul>
<p>Adicione aos favoritos uma vez e nunca mais busque "hora atual em".</p>

<h2>3. Assistentes de voz (celular, relógio, alto-falante inteligente)</h2>
<p>Siri, Google Assistant e Alexa respondem "Que horas são em [cidade]?" instantaneamente. É o mais rápido quando as mãos estão ocupadas - cozinhando, dirigindo ou já numa ligação.</p>

<h2>4. Linha de comando (para desenvolvedores)</h2>
<p>Se você vive no terminal, <code>curl wttr.in/londres</code> ou <code>curl wttr.in/tokyo</code> retorna um cartão de hora compacto. O comando <code>date</code> com <code>TZ</code> também funciona:</p>
<blockquote><code>TZ=America/New_York date</code></blockquote>
<p>Sem chaves API, sem limites de taxa para uso razoável.
</p>

<h2>5. Converta entre sua hora e a deles</h2>
<p>Saber "são 14:00 em Tóquio" é só metade da resposta - geralmente você precisa "e isso que horas dá pra mim?". Use nosso <a href="/pt/time-zone-converter.html">conversor de fusos horários</a> para traduzir qualquer hora entre quaisquer duas cidades, com ajuste automático de horário de verão. Digite sua cidade, a deles, a hora - obtenha a correspondência na hora.</p>

<h2>Referência rápida: As três perguntas</h2>
<ul>
    <li><strong>Uma cidade, agora:</strong> barra de endereços do navegador ou assistente de voz</li>
    <li><strong>Várias cidades, contínuo:</strong> página de relógio mundial fixada</li>
    <li><strong>Sua hora vs. a deles:</strong> conversor de fusos horários</li>
</ul>
<p>Todas três são grátis, funcionam em qualquer dispositivo e não precisam configuração. Da próxima vez que alguém perguntar "que horas são lá?", você terá a resposta antes de terminarem a pergunta.</p>'''
    },
    'ru': {
        'title': 'Как узнать точное время в любом городе (2026)',
        'meta_desc': 'Быстрые способы узнать точное местное время для любого города мира, с приложением или без. Хитрости браузера, мировые часы и инструменты командной строки.',
        'keywords': 'узнать точное время, сколько время в, мировые часы, время в любом городе, местное время сейчас',
        'h1': 'Как узнать точное время в любом городе',
        'content': '''<p>Вам нужно узнать, который сейчас час в Сиднее — может быть, для звонка, рейса или просто из любопытства. Не обязательно устанавливать приложение или помнить смещения UTC. Вот самые быстрые способы получить точный ответ за секунды.</p>

<h2>1. Введите в адресную строку браузера</h2>
<p>Большинство современных браузеры отвечают на запросы времени прямо в адресной строке. Просто введите:</p>
<blockquote><code>time in tokyo</code></blockquote>
<p>или</p>
<blockquote><code>сколько времени в лондоне</code></blockquote>
<p>Chrome, Edge, Firefox и Safari показывают текущее местное время над результатами поиска. Клик не нужен. Это работает для городов, аббревиатур часовых поясов (<code>time in est</code>) и даже координат.</p>

<h2>2. Используйте выделенную страницу мировых часов</h2>
<p>Когда нужно несколько городов одновременно, страница мировых часов побеждает повторные поиски. Откройте наши <a href="/ru/">мировые часы</a>, закрепите интересующие города, и они обновляются каждую секунду. Вы получаете:</p>
<ul>
    <li>Актуальное время для 700+ городов</li>
    <li>Индикаторы день/ночь</li>
    <li>Смещения UTC и статус летнего времени</li>
    <li>Ссылки для делиться с предварительно выбранными городами</li>
</ul>
<p>Добавьте в закладки один раз и больше не ищите "точное время в".</p>

<h2>3. Голосовые ассистенты (телефон, часы, умная колонка)</h2>
<p>Siri, Google Assistant и Alexa все отвечают на "Сколько времени в [город]?" мгновенно. Это быстрее всего, когда руки заняты — готовка, вождение, уже в разговоре.</p>

<h2>4. Командная строка (для разработчиков)</h2>
<p>Если вы живёте в терминале, <code>curl wttr.in/london</code> или <code>curl wttr.in/tokyo</code> вернёт компактную карточку времени. Команда <code>date</code> с <code>TZ</code> тоже работает:</p>
<blockquote><code>TZ=America/New_York date</code></blockquote>
<p>Никаких API-ключей, никаких лимитов запросов при разумном использовании.
</p>

<h2>5. Конвертируйте между вашим временем и их</h2>
<p>Знание "в Токио сейчас 14:00" — это только половина ответа. Обычно нужно "а у меня сколько?". Используйте наш <a href="/ru/time-zone-converter.html">конвертер часовых поясов</a>, чтобы перевести любое время между любыми двумя городами, с автоматическим учётом летнего времени. Введите свой город, их город, время — получите совпадение мгновенно.</p>

<h2>Краткая справка: Три вопроса</h2>
<ul>
    <li><strong>Один город, прямо сейчас:</strong> адресная строка браузера или голосовой ассистент</li>
    <li><strong>Несколько городов, постоянно:</strong> закреплённая страница мировых часов</li>
    <li><strong>Ваше время vs. их:</strong> конвертер часовых поясов</li>
</ul>
<p>Все три бесплатны, работают на любом устройстве и не требуют настройки. В следующий раз, когда кто-то спросит "который час там?", у вас будет ответ до того, как он закончит вопрос.</p>'''
    },
    'ja': {
        'title': '任意の都市の現在時刻を確認する方法 (2026)',
        'meta_desc': '世界中のあらゆる都市の正確な現地時刻を、アプリなしで素早く確認する方法。ブラウザの裏技、世界時計、コマンドラインツールを網羅。',
        'keywords': '現在時刻 確認, 何時 都市, 世界時計, 任意の都市 時刻, 現地時間 今',
        'h1': '任意の都市の現在時刻を確認する方法',
        'content': '''<p>今、シドニーが何時か知りたい——電話、フライト、単なる好奇心、理由はさまざま。アプリを入れたり UTC オフセットを覚えたりしなくても、数秒で正確な答えが得られる最速の方法を紹介します。</p>

<h2>1. ブラウザのアドレスバーに入力する</h2>
<p>最新のブラウザなら、アドレスバーで直接時刻クエリに答えてくれます。ただ入力するだけ：</p>
<blockquote><code>time in tokyo</code></blockquote>
<p>または</p>
<blockquote><code>ロンドン 何時</code></blockquote>
<p>Chrome、Edge、Firefox、Safari のすべてが検索結果の上に現在の現地時刻を表示します。クリック不要。都市名、タイムゾーン略称（<code>time in est</code>）、さらには座標でも動作します。</p>

<h2>2. 専用の世界時計ページを使う</h2>
<p>複数の都市を同時に知りたいとき、世界時計ページなら繰り返し検索する必要がありません。<a href="/ja/">世界時計</a>を開き、気になる都市をピン留めすれば、毎秒更新されます。得られるもの：</p>
<ul>
    <li>700 以上の都市のライブ時刻</li>
    <li>昼/夜インジケーター</li>
    <li>UTC オフセットと夏時間ステータス</li>
    <li>都市セットをプリセットした共有可能なリンク</li>
</ul>
<p>一度ブックマークすれば、「現在時刻」で検索することは二度となくなります。</p>

<h2>3. 音声アシスタント（スマホ、腕時計、スマートスピーカー）</h2>
<p>Siri、Google アシスタント、Alexa はすべて「[都市] は何時？」に即座に答えます。手がふさがっているとき——料理中、運転中、通話中——が最速です。</p>

<h2>4. コマンドライン（開発者向け）</h2>
<p>ターミナル暮らしなら、<code>curl wttr.in/london</code> や <code>curl wttr.in/tokyo</code> でコンパクトな時刻カードが返ってきます。<code>date</code> コマンドに <code>TZ</code> を指定しても動きます：</p>
<blockquote><code>TZ=America/New_York date</code></blockquote>
<p>API キー不要、常識的な利用ならレート制限なし。
</p>

<h2>5. 自分の時刻と相手の時刻を変換する</h2>
<p>「東京は今 14:00」が分かっても半分だけ——通常は「じゃあ自分は何時？」が知りたい。<a href="/ja/time-zone-converter.html">タイムゾーン変換</a>を使えば、任意の二都市間で任意の時刻を変換でき、夏時間も自動処理。自分の都市、相手の都市、時刻を入力するだけで即座に対応時刻が出ます。</p>

<h2>クイックリファレンス：3 つの質問</h2>
<ul>
    <li><strong>1 都市、今すぐ：</strong> ブラウザのアドレスバーまたは音声アシスタント</li>
    <li><strong>複数都市、継続的：</strong> ピン留めした世界時計ページ</li>
    <li><strong>自分の時刻 vs. 相手の時刻：</strong> タイムゾーン変換</li>
</ul>
<p>すべて無料、あらゆるデバイスで動作、セットアップゼロ。次に誰かが「あそこは今何時？」と聞いたら、相手が質問を終える前に答えられます。</p>'''
    },
    'uk': {
        'title': 'Як дізнатися точний час у будь-якому місті (2026)',
        'meta_desc': 'Швидкі способи дізнатися точний місцевий час для будь-якого міста світу, з додатком або без. Трюки браузера, світові години та інструменти командного рядка.',
        'keywords': 'дізнатися точний час, скільки час в, світові години, час у будь-якому місті, місцевий час зараз',
        'h1': 'Як дізнатися точний час у будь-якому місті',
        'content': '''<p>Вам потрібно дізнатися, котра зараз година в Сіднеї — можливо, для дзвінка, рейсу чи просто з цікавості. Не обов'язково встановлювати додаток чи пам'ятати зсуви UTC. Ось найшвидші способи отримати точну відповідь за секунди.</p>

<h2>1. Введіть у адресний рядок браузера</h2>
<p>Більшість сучасних браузерів відповідають на запити часу прямо в адресному рядку. Просто введіть:</p>
<blockquote><code>time in tokyo</code></blockquote>
<p>або</p>
<blockquote><code>скільки часу в лондоні</code></blockquote>
<p>Chrome, Edge, Firefox та Safari показують поточний місцевий час над результатами пошуку. Клік не потрібний. Це працює для міст, скорочень часових поясів (<code>time in est</code>) та навіть координат.</p>

<h2>2. Використовуйте виділену сторінку світових годин</h2>
<p>Коли потрібно кілька міст одночасно, сторінка світових годин перемагає повторні пошуки. Відкрийте наші <a href="/uk/">світові години</a>, закріпіть цікаві міста, і вони оновлюються кожну секунду. Ви отримуєте:</p>
<ul>
    <li>Актуальний час для 700+ міст</li>
    <li>Індикатори день/ніч</li>
    <li>Зсуви UTC та статус літнього часу</li>
    <li>Посилання для поділу з попередньо вибраними містами</li>
</ul>
<p>Додайте в закладки один раз і більше не шукайте "точний час у".</p>

<h2>3. Голосові асистенти (телефон, годинки, розумна колонка)</h2>
<p>Siri, Google Assistant та Alexa всі відповідають на "Скільки часу в [місто]?" миттєво. Це найшвидше, коли руки зайняті — готування, керування, вже в розмові.</p>

<h2>4. Командний рядок (для розробників)</h2>
<p>Якщо ви живете в терміналі, <code>curl wttr.in/london</code> або <code>curl wttr.in/tokyo</code> поверне компактну картку часу. Команда <code>date</code> з <code>TZ</code> теж працює:</p>
<blockquote><code>TZ=America/New_York date</code></blockquote>
<p>Жодних API-ключів, жодних лімітів запитів при розумному використанні.
</p>

<h2>5. Конвертуйте між вашим часом і їхнім</h2>
<p>Знання "в Токіо зараз 14:00" — це лише половина відповіді. Зазвичай потрібно "а у мене скільки?". Використовуйте наш <a href="/uk/time-zone-converter.html">конвертер часових поясів</a>, щоб перекласти будь-який час між будь-якими двома містами, з автоматичним урахуванням літнього часу. Введіть своє місто, їхнє місто, час — отримайте співпадіння миттєво.</p>

<h2>Коротка довідка: Три запитання</h2>
<ul>
    <li><strong>Одне місто, прямо зараз:</strong> адресний рядок браузера або голосовий асистент</li>
    <li><strong>Кілька міст, постійно:</strong> закріплена сторінка світових годин</li>
    <li><strong>Ваш час vs. їхній:</strong> конвертер часових поясів</li>
</ul>
<p>Всі три безкоштовні, працюють на будь-якому пристрої і не потребують налаштування. Наступного разу, коли хтось запитає "котра година там?", у вас буде відповідь до того, як він закінчить питання.</p>'''
    },
    'hi': {
        'title': 'किसी भी शहर का वर्तमान समय कैसे जांचें (2026)',
        'meta_desc': 'दुनिया के किसी भी शहर का सटीक स्थानीय समय जानने के तेज़ तरीके, ऐप के साथ या बिना। ब्राउज़र ट्रिक्स, विश्व घड़ियाँ और कमांड-लाइन टूल्स।',
        'keywords': 'वर्तमान समय जांचें, कितना समय है, विश्व घड़ी, किसी भी शहर में समय, स्थानीय समय अभी',
        'h1': 'किसी भी शहर का वर्तमान समय कैसे जांचें',
        'content': '''<p>आपको अभी सिडनी का समय जानना है - शायद कॉल के लिए, फ्लाइट के लिए, या सिर्फ जिज्ञासा। ऐप इंस्टॉल करने या UTC ऑफसेट याद रखने की जरूरत नहीं। यहां कुछ सेकंड में सटीक जवाब पाने के सबसे तेज़ तरीके हैं।</p>

<h2>1. ब्राउज़र के एड्रेस बार में टाइप करें</h2>
<p>अधिकांश आधुनिक ब्राउज़र एड्रेस बार में सीधे समय के प्रश्नों का उत्तर देते हैं। बस टाइप करें:</p>
<blockquote><code>time in tokyo</code></blockquote>
<p>या</p>
<blockquote><code>लंदन में कितना समय है</code></blockquote>
<p>Chrome, Edge, Firefox, और Safari सभी खोज परिणामों के ऊपर वर्तमान स्थानीय समय दिखाते हैं। किसी क्लिक की जरूरत नहीं। यह शहरों, टाइम ज़ोन संक्षिप्तीकरण (<code>time in est</code>), और यहां तक कि निर्देशांक के लिए काम करता है।</p>

<h2>2. एक समर्पित वर्ल्ड क्लॉक पेज का उपयोग करें</h2>
<p>जब आपको एक साथ कई शहरों की जरूरत हो, तो वर्ल्ड क्लॉक पेज बार-बार खोज को मात देता है। हमारा <a href="/hi/">वर्ल्ड क्लॉक</a> खोलें, जिन शहरों की परवाह है उन्हें पिन करें, और वे हर सेकंड अपडेट होते हैं। आपको मिलता है:</p>
<ul>
    <li>700+ शहरों के लिए लाइव समय</li>
    <li>दिन/रात संकेतक</li>
    <li>UTC ऑफसेट और DST स्थिति</li>
    <li>आपके शहर चयन के साथ प्री-सिलेक्टेड शेयर करने योग्य लिंक</li>
</ul>
<p>इसे एक बार बुकमार्क करें और फिर कभी "कितना समय है" खोजें नहीं।</p>

<h2>3. वॉयस असिस्टेंट (फोन, घड़ी, स्मार्ट स्पीकर)</h2>
<p>Siri, Google Assistant, और Alexa सभी "कितना समय है [शहर] में?" का तुरंत जवाब देते हैं। यह सबसे तेज़ है जब आपके हाथ व्यस्त हों - खाना बनाना, ड्राइविंग, या पहले से कॉल पर।</p>

<h2>4. कमांड लाइन (डेवलपर्स के लिए)</h2>
<p>अगर आप टर्मिनल में रहते हैं, <code>curl wttr.in/london</code> या <code>curl wttr.in/tokyo</code> एक कॉम्पैक्ट टाइम कार्ड लौटाता है। <code>date</code> कमांड <code>TZ</code> के साथ भी काम करता है:</p>
<blockquote><code>TZ=America/New_York date</code></blockquote>
<p>कोई API कीज़ नहीं, उचित उपयोग के लिए कोई रेट लिमिट नहीं।
</p>

<h2>5. अपने समय और उनके समय के बीच कनवर्ट करें</h2>
<p>यह जानना कि "टोक्यो में अभी 14:00 है" केवल आधा जवाब है - आमतौर पर आपको "मेरे लिए क्या समय है?" चाहिए। हमारे <a href="/hi/time-zone-converter.html">टाइम ज़ोन कनवर्टर</a> का उपयोग करके किन्हीं दो शहरों के बीच किसी भी समय का अनुवाद करें, स्वचालित DST हैंडलिंग के साथ। अपना शहर, उनका शहर, समय दर्ज करें - तुरंत मैच प्राप्त करें।</p>

<h2>त्वरित संदर्भ: तीन प्रश्न</h2>
<ul>
    <li><strong>एक शहर, अभी:</strong> ब्राउज़र एड्रेस बार या वॉयस असिस्टेंट</li>
    <li><strong>कई शहर, लगातार:</strong> पिन किया गया वर्ल्ड क्लॉक पेज</li>
    <li><strong>आपका समय vs. उनका:</strong> टाइम ज़ोन कनवर्टर</li>
</ul>
<p>सभी तीन मुफ़्त हैं, किसी भी डिवाइस पर काम करते हैं, और शून्य सेटअप की आवश्यकता होती है। अगली बार जब कोई पूछे "वहां कितना समय है?", आपके पास उनका सवाल खत्म होने से पहले जवाब होगा।</p>'''
    },
    'ar': {
        'title': 'كيفية معرفة الوقت الحالي في أي مدينة (2026)',
        'meta_desc': 'طرق سريعة لمعرفة الوقت المحلي الدقيق لأي مدينة في العالم، مع أو بدون تطبيق. حيل المتصفح، الساعات العالمية، وأدوات سطر الأوامر.',
        'keywords': 'معرفة الوقت الحالي, كم الساعة في, ساعة عالمية, الوقت في أي مدينة, الوقت المحلي الآن',
        'h1': 'كيفية معرفة الوقت الحالي في أي مدينة',
        'content': '''<p>تحتاج لمعرفة الوقت في سيدني الآن - ربما لمكالمة، رحلة، أو مجرد فضول. لا تحتاج لتثبيت تطبيق أو تذكر إزاحات UTC. إليك أسرع الطرق للحصول على إجابة دقيقة في ثوانٍ.</p>

<h2>1. اكتب في شريط عنوان المتصفح</h2>
<p>معظم المتصفحات الحديثة تجيب على استعلامات الوقت مباشرة في شريط العنوان. فقط اكتب:</p>
<blockquote><code>time in tokyo</code></blockquote>
<p>أو</p>
<blockquote><code>كم الساعة في لندن</code></blockquote>
<p>Chrome و Edge و Firefox و Safari جميعها تعرض الوقت المحلي الحالي فوق نتائج البحث. لا حاجة للنقر. يعمل هذا للمدن، واختصارات المناطق الزمنية (<code>time in est</code>)، وحتى الإحداثيات.</p>

<h2>2. استخدم صفحة ساعة عالمية مخصصة</h2>
<p>عندما تحتاج لعدة مدن في وقت واحد، صفحة الساعة العالمية تتفوق على البحث المتكرر. افتح <a href="/ar/">ساعتنا العالمية</a>، ثبت المدن التي تهمك، وتحديث كل ثانية. تحصل على:</p>
<ul>
    <li>وقت مباشر لـ 700+ مدينة</li>
    <li>مؤشرات نهار/ليل</li>
    <li>إزاحات UTC وحالة التوقيت الصيفي</li>
    <li>روابط قابلة للمشاركة مع تحديد مدنك مسبقاً</li>
</ul>
<p>أضفها للمفضلة مرة ولن تبحث عن "الوقت الحالي في" مجدداً.</p>

<h2>3. المساعدين الصوتيين (هاتف، ساعة، مكبر ذكي)</h2>
<p>Siri و Google Assistant و Alexa جميعًا تجيب على "كم الساعة في [المدينة]؟" فوراً. هذا الأسرع عندما يديك مشغولة - طبخ، قيادة، أو في مكالمة بالفعل.</p>

<h2>4. سطر الأوامر (للمطورين)</h2>
<p>إذا كنت تعيش في الطرفية، <code>curl wttr.in/london</code> أو <code>curl wttr.in/tokyo</code> يعيد بطاقة وقت مدمجة. أمر <code>date</code> مع <code>TZ</code> يعمل أيضاً:</p>
<blockquote><code>TZ=America/New_York date</code></blockquote>
<p>لا مفاتيح API، لا حدود معدل للاستخدام المعقول.
</p>

<h2>5. التحويل بين وقتك ووقتهم</h2>
<p>معرفة "الآن 14:00 في طوكيو" نصف الإجابة فقط - عادة تحتاج "كم الساعة بالنسبة لي؟". استخدم <a href="/ar/time-zone-converter.html">محول المناطق الزمنية</a> لترجمة أي وقت بين أي مدينتين، مع معالجة تلقائية للتوقيت الصيفي. أدخل مدينتك، مدينتهم، الوقت - احصل على التطابق فوراً.</p>

<h2>مرجع سريع: الأسئلة الثلاثة</h2>
<ul>
    <li><strong>مدينة واحدة، الآن:</strong> شريط عنوان المتصفح أو المساعد الصوتي</li>
    <li><strong>مدن متعددة، باستمرار:</strong> صفحة ساعة عالمية مثبتة</li>
    <li><strong>وقتك vs وقتهم:</strong> محول المناطق الزمنية</li>
</ul>
<p>الثلاثة مجانية، تعمل على أي جهاز، ولا تحتاج إعداد. المرة القادمة التي يسأل فيها أحد "كم الساعة هناك؟"، سيكون لديك الجواب قبل أن ينهي السؤال.</p>'''
    },
}

LANG_DIRS = {
    'en': BASE,
    'es': BASE / 'es',
    'zh': BASE / 'zh',
    'it': BASE / 'it',
    'de': BASE / 'de',
    'fr': BASE / 'fr',
    'pt': BASE / 'pt',
    'ru': BASE / 'ru',
    'ja': BASE / 'ja',
    'uk': BASE / 'uk',
    'hi': BASE / 'hi',
    'ar': BASE / 'ar',
}

def build_article(slug, lang, art):
    lang_dir = LANG_DIRS[lang]
    blog_dir = lang_dir / 'blog'
    blog_dir.mkdir(parents=True, exist_ok=True)
    
    fname = f'{slug}-{lang}.html' if lang != 'en' else f'{slug}.html'
    out_path = blog_dir / fname
    
    crumb_home, crumb_blog = CRUMB[lang]
    
    # Read template and replace placeholders
    html = template
    html = html.replace('{{TITLE}}', art['title'])
    html = html.replace('{{META_DESC}}', art['meta_desc'])
    html = html.replace('{{KEYWORDS}}', art['keywords'])
    html = html.replace('{{H1}}', art['h1'])
    html = html.replace('{{CONTENT}}', art['content'])
    html = html.replace('{{CRUMB_HOME}}', crumb_home)
    html = html.replace('{{CRUMB_BLOG}}', crumb_blog)
    html = html.replace('{{META_DATE}}', META_DATE[lang])
    html = html.replace('{{META_READ}}', META_READ[lang])
    html = html.replace('{{SKIP}}', SKIP[lang])
    html = html.replace('{{LOADING}}', LOADING[lang])
    html = html.replace('{{LANG_CODE}}', lang)
    html = html.replace('{{CANONICAL}}', f'https://worldtimessync.com/{lang}/blog/{slug}.html' if lang != 'en' else f'https://worldtimessync.com/blog/{slug}.html')
    html = html.replace('{{OG_URL}}', f'https://worldtimessync.com/{lang}/blog/{slug}.html' if lang != 'en' else f'https://worldtimessync.com/blog/{slug}.html')
    html = html.replace('{{OG_TITLE}}', art['title'])
    html = html.replace('{{OG_DESC}}', art['meta_desc'])
    html = html.replace('{{BLOG_URL}}', f'/{lang}/blog/' if lang != 'en' else '/blog/')
    
    out_path.write_text(html, encoding='utf-8')
    print(f'Created {out_path}')

if __name__ == '__main__':
    slug = 'check-current-time-any-city'
    for lang, art in ARTICLES.items():
        build_article(slug, lang, art)
    print('Done!')