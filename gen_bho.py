# -*- coding: utf-8 -*-
"""Human-written translations for business-hours-overlap, 8 languages."""

def _faq(lang_questions):
    import json
    items = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in lang_questions]
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}, ensure_ascii=False)

POSTS_BHO = []

# ---------------- RU ----------------
POSTS_BHO.append(('ru',
 'Пересечение рабочих часов — найдите общие часы команды | World Time Sync',
 'Найдите пересечение рабочего времени между Лондоном, Нью-Йорком, Дубаем и Сингапуром.',
 'пересечение рабочих часов, время в Лондоне, время в Нью-Йорке, планировщик встреч',
 ('Главная', 'Блог', 'Пересечение рабочих часов', 'Перейти к основному контенту', 'Загрузка World Time...', 'Хлебные крошки', 'Конфиденциальность', 'О нас', 'Контакты', 'Условия'),
 '📅 10 августа 2026 &nbsp;·&nbsp; ⏱ 6 мин чтения &nbsp;·&nbsp; 🏷 Часовые пояса, Гид',
 'Пересечение рабочих часов: где команды действительно работают одновременно',
 f'''<p>Практическое пересечение двух офисов — это когда местные часы обоих находятся примерно в интервале 9:00–17:00. Для удалённых пар такое окно может длиться один час или не существовать вовсе — и тогда вы либо переносите встречи на чей-то вечер, либо переводите часть работы в асинхронный формат.</p>
<h2>Пересечение популярных пар</h2>
<table><thead><tr><th>Пара</th><th>Разница</th><th>Общие часы (9–17 у обоих)</th></tr></thead><tbody>
<tr><td>Лондон – Нью-Йорк</td><td>5 ч</td><td>14:00–17:00 Лондон / 9:00–12:00 Нью-Йорк</td></tr>
<tr><td>Лондон – Дубай</td><td>3–4 ч</td><td>12:00–17:00 лондонское время</td></tr>
<tr><td>Нью-Йорк – Сингапур</td><td>12–13 ч</td><td>Нет — нужны вечерние или ранние звонки</td></tr>
<tr><td>Лондон – Сингапур</td><td>7–8 ч</td><td>Нет стандартного — 16:00 в Лондоне = полночь в Сингапуре</td></tr>
<tr><td>Дубай – Сингапур</td><td>4 ч</td><td>13:00–17:00 Дубай / 17:00–21:00 Сингапур (на грани)</td></tr>
</tbody></table>
<h2>Лучшее время для звонка в Лондон</h2>
<p>Лондон работает с 9:00 до 17:00 по GMT/BST. Это значит:</p>
<ul>
<li>Из Нью-Йорка: 9:00–12:00 вашего времени попадает на их вторую половину дня.</li>
<li>Из Сан-Франциско: 9:00–11:30 по тихоокеанскому времени совпадает с концом лондонского дня.</li>
<li>Из Сиднея: только раннее утро (~6–8 утра) достаёт до лондонского послеполудня.</li>
</ul>
<h2>Часто задаваемые вопросы</h2>
<div class="faq-section">
<div class="faq-item"><h3>Когда лучше звонить из США в Лондон?</h3><p>Восточное побережье: 9:00–12:00 ET (14:00–17:00 в Лондоне). Западное побережье: до 11:30 PT.</p></div>
<div class="faq-item"><h3>Совпадают ли рабочие часы Лондона и Нью-Йорка?</h3><p>Да — около трёх часов: 14:00–17:00 в Лондоне соответствует 9:00–12:00 в Нью-Йорке.</p></div>
<div class="faq-item"><h3>Как сотрудничать командам без пересечения?</h3><p>Справедливо чередуйте редкие ранние или поздние звонки, фиксируйте решения письменно и используйте асинхронные статусы.</p></div>
</div>
<p>Смежное: <a href="/remote-team-solutions">решения для распределённых команд</a>.</p>''',
 _faq([('Когда лучше звонить из США в Лондон?', 'Восточное побережье: 9:00–12:00 ET (14:00–17:00 в Лондоне). Западное побережье: до 11:30 PT.'),
       ('Совпадают ли рабочие часы Лондона и Нью-Йорка?', 'Да — около трёх часов: 14:00–17:00 в Лондоне соответствует 9:00–12:00 в Нью-Йорке.'),
       ('Как сотрудничать командам без пересечения?', 'Справедливо чередуйте редкие ранние или поздние звонки, фиксируйте решения письменно и используйте асинхронные статусы.')]),
 '2026-08-10', 6))

# ---------------- ES ----------------
POSTS_BHO.append(('es',
 'Horario laboral compartido: encuentra las horas comunes de tu equipo | World Time Sync',
 'Encuentra el horario laboral compartido entre ciudades como Londres, Nueva York, Dubái y Singapur.',
 'horario laboral compartido, hora en Londres, hora en Nueva York, planificador de reuniones',
 ('Inicio', 'Blog', 'Horario laboral compartido', 'Ir al contenido principal', 'Cargando World Time...', 'Migas de pan', 'Privacidad', 'Sobre nosotros', 'Contacto', 'Términos'),
 '📅 10 de agosto de 2026 &nbsp;·&nbsp; ⏱ 6 min de lectura &nbsp;·&nbsp; 🏷 Zonas horarias, Guía',
 'Horario laboral compartido entre equipos de distintas ciudades',
 f'''<p>El solapamiento práctico entre dos oficinas es aquel en el que los relojes locales de ambas están dentro de una franja aproximada de 9 a 17 horas. Para las parejas más distantes esa ventana puede ser de una sola hora o directamente no existir — y entonces toca mover las reuniones a la tarde de alguien o pasar parte del trabajo a formato asíncrono.</p>
<h2>Solapamiento de parejas populares</h2>
<table><thead><tr><th>Pareja</th><th>Diferencia</th><th>Horas compartidas (9–17 en ambas)</th></tr></thead><tbody>
<tr><td>Londres – Nueva York</td><td>5 h</td><td>14:00–17:00 Londres / 9:00–12:00 NY</td></tr>
<tr><td>Londres – Dubái</td><td>3–4 h</td><td>12:00–17:00 lado de Londres</td></tr>
<tr><td>Nueva York – Singapur</td><td>12–13 h</td><td>Ninguna — hace falta llamadas nocturnas o muy tempranas</td></tr>
<tr><td>Londres – Singapur</td><td>7–8 h</td><td>Ninguna estándar — 16:00 Londres = medianoche en Singapur</td></tr>
<tr><td>Dubái – Singapur</td><td>4 h</td><td>13:00–17:00 Dubái / 17:00–21:00 Singapur (al límite)</td></tr>
</tbody></table>
<h2>La mejor hora para llamar a Londres</h2>
<p>Londres trabaja de 9 a 17 en GMT/BST. Eso significa:</p>
<ul>
<li>Desde Nueva York: de 9 a 12 de la mañana tu hora cae en su tarde.</li>
<li>Desde San Francisco: de 9 a 11:30 de la mañana del Pacífico coincide con el final del día londinense.</li>
<li>Desde Sídney: solo primera hora de la mañana (~6–8 AM) alcanza la tarde de Londres.</li>
</ul>
<h2>Preguntas frecuentes</h2>
<div class="faq-section">
<div class="faq-item"><h3>¿Cuál es la mejor hora para llamar a EE.&nbsp;UU. desde Londres?</h3><p>Costa este: de 9 a 12 ET (14:00–17:00 en Londres). Costa oeste: antes de las 11:30 PT.</p></div>
<div class="faq-item"><h3>¿Londres y Nueva York comparten horario laboral?</h3><p>Sí — unas tres horas: de 14:00 a 17:00 en Londres equivalen a de 9:00 a 12:00 en Nueva York.</p></div>
<div class="faq-item"><h3>¿Cómo colaboran los equipos sin solapamiento?</h3><p>Reparte con justicia las llamadas tempranas o tardías ocasionales, documenta las decisiones por escrito y usa actualizaciones asíncronas.</p></div>
</div>
<p>Relacionado: <a href="/remote-team-solutions">soluciones para equipos remotos</a>.</p>''',
 _faq([('¿Cuál es la mejor hora para llamar a EE. UU. desde Londres?', 'Costa este: de 9 a 12 ET (14:00–17:00 en Londres). Costa oeste: antes de las 11:30 PT.'),
       ('¿Londres y Nueva York comparten horario laboral?', 'Sí — unas tres horas: de 14:00 a 17:00 en Londres equivalen a de 9:00 a 12:00 en Nueva York.'),
       ('¿Cómo colaboran los equipos sin solapamiento?', 'Reparte con justicia las llamadas ocasionales, documenta las decisiones por escrito y usa actualizaciones asíncronas.')]),
 '2026-08-10', 6))

# ---------------- DE ----------------
POSTS_BHO.append(('de',
 'Überschneidende Geschäftszeiten: Gemeinsame Stunden des Teams finden | World Time Sync',
 'Finden Sie überschneidende Geschäftszeiten zwischen Städten wie London, New York, Dubai und Singapur.',
 'überschneidende Geschäftszeiten, Zeit in London, Zeit in New York, Meetingplaner',
 ('Startseite', 'Blog', 'Überschneidende Geschäftszeiten', 'Zum Hauptinhalt springen', 'World Time wird geladen...', 'Brotkrumen', 'Datenschutz', 'Über uns', 'Kontakt', 'Nutzungsbedingungen'),
 '📅 10. August 2026 &nbsp;·&nbsp; ⏱ 6 Min. Lesezeit &nbsp;·&nbsp; 🏷 Zeitzonen, Leitfaden',
 'Überschneidende Geschäftszeiten: Wann Teams wirklich gleichzeitig arbeiten',
 f'''<p>Eine praktische Überschneidung zwischen zwei Standorten liegt vor, wenn die örtlichen Uhren beider Seiten grob zwischen 9 und 17 Uhr stehen. Bei sehr weit entfernten Paaren kann dieses Fenster nur eine Stunde betragen oder ganz fehlen — dann verlegt man Meetings in den Abend einer Seite oder verlagert einen Teil der Arbeit in asynchrone Abstimmung.</p>
<h2>Überschneidung beliebter Paare</h2>
<table><thead><tr><th>Paar</th><th>Abstand</th><th>Gemeinsame Stunden (9–17 bei beiden)</th></tr></thead><tbody>
<tr><td>London – New York</td><td>5 Std.</td><td>14:00–17:00 London / 9:00–12:00 New York</td></tr>
<tr><td>London – Dubai</td><td>3–4 Std.</td><td>12:00–17:00 Londoner Seite</td></tr>
<tr><td>New York – Singapur</td><td>12–13 Std.</td><td>Keine — Abend- oder Frühtermine nötig</td></tr>
<tr><td>London – Singapur</td><td>7–8 Std.</td><td>Keine reguläre — 16:00 London = Mitternacht in Singapur</td></tr>
<tr><td>Dubai – Singapur</td><td>4 Std.</td><td>13:00–17:00 Dubai / 17:00–21:00 Singapur (Grenzfälle)</td></tr>
</tbody></table>
<h2>Beste Anrufzeit für London</h2>
<p>In London wird von 9 bis 17 Uhr nach GMT/BST gearbeitet. Das bedeutet:</p>
<ul>
<li>Von New York aus: 9–12 Uhr Ihrer Zeit trifft deren Nachmittag.</li>
<li>Von San Francisco aus: 9–11:30 Uhr Pazifik überlappen mit dem späten Londoner Tag.</li>
<li>Von Sydney aus: nur frühester Morgen (~6–8 Uhr) erreicht den Londoner Nachmittag.</li>
</ul>
<h2>Häufige Fragen</h2>
<div class="faq-section">
<div class="faq-item"><h3>Wann ruft man am besten von den USA nach London an?</h3><p>Ostküste: 9–12 Uhr ET (14:00–17:00 in London). Westküste: vor 11:30 Uhr PT.</p></div>
<div class="faq-item"><h3>Haben London und New York gemeinsame Geschäftszeiten?</h3><p>Ja — rund drei Stunden: 14:00–17:00 in London entsprechen 9:00–12:00 in New York.</p></div>
<div class="faq-item"><h3>Wie arbeiten Teams ohne Überschneidung zusammen?</h3><p>Verteilen Sie gelegentliche frühe oder späte Calls fair, halten Sie Entscheidungen schriftlich fest und nutzen Sie asynchrone Status-Updates.</p></div>
</div>
<p>Verwandt: <a href="/remote-team-solutions">Lösungen für verteilte Teams</a>.</p>''',
 _faq([('Wann ruft man am besten von den USA nach London an?', 'Ostküste: 9–12 Uhr ET (14:00–17:00 in London). Westküste: vor 11:30 Uhr PT.'),
       ('Haben London und New York gemeinsame Geschäftszeiten?', 'Ja — rund drei Stunden: 14:00–17:00 in London entsprechen 9:00–12:00 in New York.'),
       ('Wie arbeiten Teams ohne Überschneidung zusammen?', 'Frühe oder späte Calls fair verteilen, Entscheidungen schriftlich festhalten und asynchrone Updates nutzen.')]),
 '2026-08-10', 6))

# ---------------- FR ----------------
POSTS_BHO.append(('fr',
 'Heures de travail communes : trouvez les heures partagées de votre équipe | World Time Sync',
 'Trouvez les heures de travail communes entre Londres, New York, Dubaï et Singapour.',
 'heures de travail communes, heure à Londres, heure à New York, planificateur de réunions',
 ('Accueil', 'Blog', 'Heures de travail communes', 'Aller au contenu principal', 'Chargement de World Time...', 'Fil d\u2019Ariane', 'Confidentialité', 'À propos', 'Contact', 'Conditions'),
 '📅 10 août 2026 &nbsp;·&nbsp; ⏱ 6 min de lecture &nbsp;·&nbsp; 🏷 Fuseaux horaires, Guide',
 'Heures de travail communes : quand les équipes travaillent vraiment ensemble',
 f'''<p>Le chevauchement pratique entre deux bureaux correspond aux moments où les horloges locales des deux sites se situent grosso modo entre 9 h et 17 h. Pour les paires très éloignées, cette fenêtre peut durer une heure ou ne pas exister du tout — il faut alors décaler les réunions vers la soirée de quelqu\u2019un ou passer une partie du travail en mode asynchrone.</p>
<h2>Chevauchement des paires populaires</h2>
<table><thead><tr><th>Paire</th><th>Écart</th><th>Heures communes (9 h–17 h des deux côtés)</th></tr></thead><tbody>
<tr><td>Londres – New York</td><td>5 h</td><td>14h00–17h00 Londres / 9h00–12h00 NY</td></tr>
<tr><td>Londres – Dubaï</td><td>3–4 h</td><td>12h00–17h00 côté Londres</td></tr>
<tr><td>New York – Singapour</td><td>12–13 h</td><td>Aucun — appels en soirée ou très tôt nécessaires</td></tr>
<tr><td>Londres – Singapour</td><td>7–8 h</td><td>Aucun standard — 16 h à Londres = minuit à Singapour</td></tr>
<tr><td>Dubaï – Singapour</td><td>4 h</td><td>13h00–17h00 Dubaï / 17h00–21h00 Singapour (en limite)</td></tr>
</tbody></table>
<h2>Meilleure heure pour appeler Londres</h2>
<p>Londres travaille de 9 h à 17 h en GMT/BST. Cela signifie :</p>
<ul>
<li>Depuis New York : de 9 h à midi chez vous tombe pendant leur après-midi.</li>
<li>Depuis San Francisco : de 9 h à 11 h 30 du Pacifique coïncide avec la fin de journée londonienne.</li>
<li>Depuis Sydney : seul le tout début de matinée (~6 h–8 h) atteint l\u2019après-midi londonien.</li>
</ul>
<h2>Questions fréquentes</h2>
<div class="faq-section">
<div class="faq-item"><h3>Quelle est la meilleure heure pour appeler les États-Unis depuis Londres ?</h3><p>Côte Est : de 9 h à midi ET (14h–17h à Londres). Côte Ouest : avant 11 h 30 PT.</p></div>
<div class="faq-item"><h3>Londres et New York partagent-elles des heures de travail ?</h3><p>Oui — environ trois heures : 14h–17h à Londres correspondent à 9h–12h à New York.</p></div>
<div class="faq-item"><h3>Comment collaborer sans aucun chevauchement ?</h3><p>Répartissez équitablement les rares appels matinaux ou nocturnes, consignez les décisions par écrit et utilisez des points d\u2019avancement asynchrones.</p></div>
</div>
<p>À lire aussi : <a href="/remote-team-solutions">solutions pour équipes distribuées</a>.</p>''',
 _faq([('Quelle est la meilleure heure pour appeler les États-Unis depuis Londres ?', 'Côte Est : de 9 h à midi ET (14h–17h à Londres). Côte Ouest : avant 11 h 30 PT.'),
       ('Londres et New York partagent-elles des heures de travail ?', 'Oui — environ trois heures : 14h–17h à Londres correspondent à 9h–12h à New York.'),
       ('Comment collaborer sans aucun chevauchement ?', 'Répartir équitablement les appels rares, consigner les décisions par écrit et travailler de façon asynchrone.')]),
 '2026-08-10', 6))

# ---------------- IT ----------------
POSTS_BHO.append(('it',
 'Orari di lavoro sovrapposti: trova le ore condivise del team | World Time Sync',
 'Trova le ore di lavoro sovrapposte tra città come Londra, New York, Dubai e Singapore.',
 'orari di lavoro sovrapposti, ora a Londra, ora a New York, pianificatore riunioni',
 ('Home', 'Blog', 'Orari di lavoro sovrapposti', 'Vai al contenuto principale', 'Caricamento di World Time...', 'Briciole di pane', 'Privacy', 'Chi siamo', 'Contatti', 'Termini'),
 '📅 10 agosto 2026 &nbsp;·&nbsp; ⏱ 6 min di lettura &nbsp;·&nbsp; 🏷 Fusi orari, Guida',
 'Orari di lavoro sovrapposti: quando i team lavorano davvero insieme',
 f'''<p>La sovrapposizione pratica tra due uffici è quella in cui gli orologi locali di entrambi cadono grossomodo nella fascia 9–17. Per le coppie più distanti questa finestra può durare un\u2019ora o non esistere affatto — e allora bisogna spostare le riunioni nella serata di qualcuno oppure trasferire parte del lavoro in modalità asincrona.</p>
<h2>Sovrapposizione delle coppie più comuni</h2>
<table><thead><tr><th>Coppia</th><th>Scarto</th><th>Ore condivise (9–17 per entrambe)</th></tr></thead><tbody>
<tr><td>Londra – New York</td><td>5 h</td><td>14:00–17:00 Londra / 9:00–12:00 New York</td></tr>
<tr><td>Londra – Dubai</td><td>3–4 h</td><td>12:00–17:00 lato Londra</td></tr>
<tr><td>New York – Singapore</td><td>12–13 h</td><td>Nessuna — servono chiamate serali o mattutine</td></tr>
<tr><td>Londra – Singapore</td><td>7–8 h</td><td>Nessuna standard — le 16:00 di Londra sono mezzanotte a Singapore</td></tr>
<tr><td>Dubai – Singapore</td><td>4 h</td><td>13:00–17:00 Dubai / 17:00–21:00 Singapore (al limite)</td></tr>
</tbody></table>
<h2>Migliore ora per chiamare Londra</h2>
<p>A Londra si lavora dalle 9 alle 17 GMT/BST. Questo significa:</p>
<ul>
<li>Da New York: dalle 9 alle 12 del tuo tempo cade nel loro pomeriggio.</li>
<li>Da San Francisco: dalle 9 alle 11:30 della costa ovest coincide con la fine della giornata londinese.</li>
<li>Da Sydney: solo al primo mattino (~6–8) si raggiunge il pomeriggio di Londra.</li>
</ul>
<h2>Domande frequenti</h2>
<div class="faq-section">
<div class="faq-item"><h3>Qual è l\u2019ora migliore per chiamare gli Stati Uniti da Londra?</h3><p>Costa orientale: dalle 9 alle 12 ET (14:00–17:00 a Londra). Costа occidentale: prima delle 11:30 PT.</p></div>
<div class="faq-item"><h3>Londra e New York condividono orari di lavoro?</h3><p>Sì — circa tre ore: le 14:00–17:00 di Londra corrispondono alle 9:00–12:00 di New York.</p></div>
<div class="faq-item"><h3>Come collaborano i team senza sovrapposizione?</h3><p>Alterna con equità le rare chiamate anticipate o serali, documenta le decisioni per iscritto e usa aggiornamenti asincroni sullo stato dei lavori.</p></div>
</div>
<p>Approfondimento: <a href="/remote-team-solutions">soluzioni per team distribuiti</a>.</p>''',
 _faq([('Qual è l\'ora migliore per chiamare gli Stati Uniti da Londra?', 'Costa orientale: dalle 9 alle 12 ET (14:00–17:00 a Londra). Costa occidentale: prima delle 11:30 PT.'),
       ('Londra e New York condividono orari di lavoro?', 'Sì — circa tre ore: le 14:00–17:00 di Londra corrispondono alle 9:00–12:00 di New York.'),
       ('Come collaborano i team senza sovrapposizione?', 'Alternare equamente le chiamate rare, documentare per iscritto e usare aggiornamenti asincroni.')]),
 '2026-08-10', 6))
