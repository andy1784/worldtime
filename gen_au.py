# -*- coding: utf-8 -*-
"""Human-written translations for daylight-saving-time-australia-how-it-works, 8 languages."""
import json as _json

def _faq(qa):
    items = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]
    return _json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}, ensure_ascii=False)

POSTS_AU = []

# ---------------- RU ----------------
POSTS_AU.append(('ru',
 'Как работает летнее время в Австралии — гид по штатам',
 'Летнее время в Австралии зависит от штата. Одни переводят часы, другие нет, а разница во времени меняется четыре раза в год.',
 'летнее время Австралия, часовые пояса Австралии, время в Сиднее, время в Перте',
 ('Главная', 'Блог', 'Летнее время в Австралии', 'Перейти к основному контенту', 'Загрузка World Time...', 'Хлебные крошки', 'Конфиденциальность', 'О нас', 'Контакты', 'Условия'),
 '📅 27 июня 2026 &nbsp;·&nbsp; ⏱ 8 мин чтения &nbsp;·&nbsp; 🏷 Австралия',
 f'''<h2>Как работает летнее время в Австралии</h2>
<p>Австралия — одна из самых запутанных стран мира, когда речь идёт о летнем времени. Единого общенационального правила здесь нет: каждый штат и территория решает вопрос самостоятельно. В итоге получается лоскутное одеяло, где разница между Сиднеем и Брисбеном меняется дважды в год, а разница между Сиднеем и Пертом сдвигается дважды в год по совершенно другому расписанию.</p>
<h2>Штаты, которые переводят часы</h2>
<p>Новый Южный Уэльс, Виктория, Южная Австралия, Тасмания и столичная территория Канберры переходят на летнее время в первое воскресенье октября и возвращаются обратно в первое воскресенье апреля. На период летнего времени эти штаты сдвигают часы на час вперёд.</p>
<h2>Штаты без летнего времени</h2>
<p>Квинсленд, Западная Австралия и Северная территория круглый год живут по стандартному времени. Квинсленд выносил вопрос на референдум в 1992 году — и отклонил его. Западная Австралия проводила пробный период с 2006 по 2009 год, после чего референдум 2009 года также сказал «нет».</p>
<h2>«Разница во времени»: сезонная перестановка</h2>
<p>Обычно Сидней (Новый Южный Уэльс) и Брисбен (Квинсленд) оба живут по UTC+10 — разницы нет. Но когда в октябре начинается летнее время, Сидней переходит на UTC+11, а Брисбен остаётся на UTC+10. Полгода два крупнейших города восточного побережья разделены одним часом.</p>
<p>Перт (Западная Австралия) обычно отстаёт от Сиднея на два часа (UTC+8 против UTC+10). Во время летнего времени отставание вырастает до трёх часов (UTC+8 против UTC+11). Для компаний, работающих по всей стране, это постоянная головная боль.</p>
<h2>Исключение: остров Лорд-Хау</h2>
<p>Остров Лорд-Хау, относящийся к Новому Южному Уэльсу, довёл идею до предела: он сдвигает часы не на привычные 60 минут, а всего на 30. Это самый маленький переход на летнее время в мире — летом остров перемещается с UTC+10:30 на UTC+11:00.</p>
<h2>Почему Австралия так устроена?</h2>
<p>Короткий ответ — федерализм и география. Северные штаты у экватора почти не видят разницы в длине светового дня в течение года, поэтому летнее время даёт им мало. Южным штатам вроде Тасмании зимой достаются очень короткие дни, там эта идея популярнее. Федеральное правительство отказалось вводить единое правило, оставив решение штатам.</p>
<p>Если вы планируете встречи между австралийскими штатами, всегда проверяйте актуальное смещение. Откройте <a href="/">World Time Sync</a>, чтобы увидеть живые часы Сиднея, Мельбурна, Брисбена, Перта и Аделаиды.</p>
<h2>Часто задаваемые вопросы</h2>
<div class="faq-section">
<div class="faq-item"><h3>Все ли штаты Австралии переводят часы?</h3><p>Нет. Юго-восток (Новый Южный Уэльс, Виктория, Южная Австралия, Тасмания, ACT) переходит на летнее время; Квинсленд, Западная Австралия и Северная территория — нет.</p></div>
<div class="faq-item"><h3>Когда именно начинается и заканчивается летнее время в Австралии?</h3><p>Начало — первое воскресенье октября, конец — первое воскресенье апреля. Обратите внимание: это наоборот по отношению к северному полушарию.</p></div>
<div class="faq-item"><h3>Какая разница между Сиднеем и Пертом летом?</h3><p>Три часа: Сидней живёт по UTC+11, Перт — по UTC+8.</p></div>
</div>''',
 _faq([('Все ли штаты Австралии переводят часы?', 'Нет. Юго-восток переходит на летнее время; Квинсленд, Западная Австралия и Северная территория — нет.'),
       ('Когда начинается и заканчивается летнее время в Австралии?', 'Начало — первое воскресенье октября, конец — первое воскресенье апреля.'),
       ('Какая разница между Сиднеем и Пертом летом?', 'Три часа: UTC+11 против UTC+8.')]),
 '2026-06-27', 8))

# ---------------- ES ----------------
POSTS_AU.append(('es',
 'Cómo funciona el horario de verano en Australia — guía por estados',
 'El horario de verano en Australia varía según el estado. Algunos lo observan, otros no, y las diferencias de hora cambian cuatro veces al año.',
 'horario de verano Australia, zonas horarias Australia, hora Sídney, hora Perth',
 ('Inicio', 'Blog', 'Horario de verano en Australia', 'Ir al contenido principal', 'Cargando World Time...', 'Migas de pan', 'Privacidad', 'Sobre nosotros', 'Contacto', 'Términos'),
 '📅 27 de junio de 2026 &nbsp;·&nbsp; ⏱ 8 min de lectura &nbsp;·&nbsp; 🏷 Australia',
 f'''<h2>Cómo funciona el horario de verano en Australia</h2>
<p>Australia es uno de los países más liosos del mundo en cuanto al horario de verano. No existe una regla nacional única: cada estado y territorio decide por su cuenta. El resultado es un mosaico en el que la diferencia entre Sídney y Brisbane cambia dos veces al año, y la diferencia entre Sídney y Perth se desplaza dos veces al año siguiendo un calendario completamente distinto.</p>
<h2>Estados que cambian el reloj</h2>
<p>Nueva Gales del Sur, Victoria, Australia Meridional, Tasmania y el Territorio de la Capital Australiana pasan al horario de verano el primer domingo de octubre y vuelven atrás el primer domingo de abril. Durante ese periodo adelantan sus relojes una hora.</p>
<h2>Estados que no lo observan</h2>
<p>Queensland, Australia Occidental y el Territorio del Norte viven todo el año en hora estándar. Queensland sometió la cuestión a referéndum en 1992 y la rechazó. Australia Occidental hizo una prueba entre 2006 y 2009, y el referéndum de 2009 también dijo que no.</p>
<h2>El baile de diferencias horarias</h2>
<p>Normalmente Sídney (Nueva Gales del Sur) y Brisbane (Queensland) están ambas en UTC+10: sin diferencia. Pero cuando empieza el horario de verano en octubre, Sídney pasa a UTC+11 mientras Brisbane se queda en UTC+10. Durante seis meses, las dos mayores ciudades de la costa este quedan separadas por una hora.</p>
<p>Perth (Australia Occidental) suele ir dos horas por detrás de Sídney (UTC+8 frente a UTC+10). Con el horario de verano, el retraso sube a tres horas (UTC+8 frente a UTC+11). Para las empresas nacionales es un dolor de cabeza permanente.</p>
<h2>La excepción: isla Lord Howe</h2>
<p>La isla Lord Howe, perteneciente a Nueva Gales del Sur, lleva la idea al extremo: solo mueve el reloj 30 minutos en lugar de los habituales 60. Es el cambio de horario de verano más pequeño del mundo: en verano la isla pasa de UTC+10:30 a UTC+11:00.</p>
<h2>¿Por qué Australia funciona así?</h2>
<p>Respuesta corta: federalismo y geografía. Los estados del norte, cerca del ecuador, apenas notan cambios en la duración del día a lo largo del año, así que el horario de verano les aporta poco. A los estados del sur como Tasmania les tocan inviernos muy cortos de luz, y allí la idea es más popular. El Gobierno federal ha preferido no imponer una norma nacional y dejar la decisión en manos de cada estado.</p>
<p>Si planificas reuniones entre estados australianos, comprueba siempre el desfase actual. Abre <a href="/">World Time Sync</a> para ver los relojes en vivo de Sídney, Melbourne, Brisbane, Perth y Adelaida.</p>
<h2>Preguntas frecuentes</h2>
<div class="faq-section">
<div class="faq-item"><h3>¿Todos los estados de Australia cambian el reloj?</h3><p>No. El sureste (Nueva Gales del Sur, Victoria, Australia Meridional, Tasmania y ACT) observa el horario de verano; Queensland, Australia Occidental y el Territorio del Norte, no.</p></div>
<div class="faq-item"><h3>¿Cuándo empieza y termina el horario de verano en Australia?</h3><p>Empieza el primer domingo de octubre y termina el primer domingo de abril. Fíjate: al revés que en el hemisferio norte.</p></div>
<div class="faq-item"><h3>¿Qué diferencia hay entre Sídney y Perth en verano?</h3><p>Tres horas: Sídney en UTC+11 y Perth en UTC+8.</p></div>
</div>''',
 _faq([('¿Todos los estados de Australia cambian el reloj?', 'No. El sureste sí; Queensland, Australia Occidental y el Territorio del Norte, no.'),
       ('¿Cuándo empieza y termina el horario de verano en Australia?', 'Primer domingo de octubre hasta el primer domingo de abril.'),
       ('¿Qué diferencia hay entre Sídney y Perth en verano?', 'Tres horas: UTC+11 frente a UTC+8.')]),
 '2026-06-27', 8))

# ---------------- DE ----------------
POSTS_AU.append(('de',
 'Wie die Sommerzeit in Australien funktioniert — ein Guide nach Bundesstaaten',
 'Die Sommerzeit in Australien ist je nach Bundesstaat unterschiedlich. Manche stellen um, andere nicht — und die Zeitunterschiede ändern sich viermal im Jahr.',
 'Sommerzeit Australien, Zeitzonen Australien, Uhrzeit Sydney, Uhrzeit Perth',
 ('Startseite', 'Blog', 'Sommerzeit in Australien', 'Zum Hauptinhalt springen', 'World Time wird geladen...', 'Brotkrumen', 'Datenschutz', 'Über uns', 'Kontakt', 'Nutzungsbedingungen'),
 '📅 27. Juni 2026 &nbsp;·&nbsp; ⏱ 8 Min. Lesezeit &nbsp;·&nbsp; 🏷 Australien',
 f'''<h2>Wie die Sommerzeit in Australien funktioniert</h2>
<p>Australien ist eines der verwirrendsten Länder der Welt, wenn es um die Sommerzeit geht. Es gibt keine landesweite Regel — jeder Bundesstaat und jedes Territorium entscheidet selbst. Das Ergebnis ist ein Flickenteppich, bei dem sich der Unterschied zwischen Sydney und Brisbane zweimal jährlich ändert, während der Unterschied zwischen Sydney und Perth zweimal jährlich nach einem völlig anderen Muster springt.</p>
<h2>Bundesstaaten mit Sommerzeit</h2>
<p>New South Wales, Victoria, South Australia, Tasmanien und das Australian Capital Territory wechseln am ersten Sonntag im Oktober auf Sommerzeit und am ersten Sonntag im April zurück. Während dieser Zeit stellen sie ihre Uhren eine Stunde vor.</p>
<h2>Bundesstaaten ohne Sommerzeit</h2>
<p>Queensland, Western Australia und das Northern Territory bleiben das ganze Jahr über auf Standardzeit. Queensland hatte 1992 ein Referendum dazu abgehalten — und abgelehnt. Western Australia testete die Sommerzeit von 2006 bis 2009; das Referendum 2009 lehnte sie ebenfalls ab.</p>
<h2>Das Verschiebe-Karussell der Zeitunterschiede</h2>
<p>NORMAL stehen Sydney (New South Wales) und Brisbane (Queensland) beide auf UTC+10 — kein Unterschied. Beginnt im Oktober aber die Sommerzeit, geht Sydney auf UTC+11, während Brisbane bei UTC+10 bleibt. Sechs Monate lang liegen die beiden größten Ostküstenstädte eine Stunde auseinander.</p>
<p>Perth (Western Australia) liegt normalerweise zwei Stunden hinter Sydney (UTC+8 gegenüber UTC+10). Zur Sommerzeit werden es drei Stunden (UTC+8 gegenüber UTC+11). Für landesweit tätige Unternehmen ein rollendes Ärgernis.</p>
<h2>Die Ausnahme: Lord-Howe-Insel</h2>
<p>Die zu New South Wales gehörende Lord-Howe-Insel treibt es auf die Spitze: Sie verschiebt die Uhr nur um 30 statt der üblichen 60 Minuten — die kleinste Sommerzeit-Umstellung der Welt. Im Sommer wandert die Insel von UTC+10:30 auf UTC+11:00.</p>
<h2>Warum macht Australien das so?</h2>
<p>Kurze Antwort: Föderalismus und Geografie. Die nördlichen Staaten nahe dem Äquator erleben kaum Schwankungen bei der Tageslänge — Sommerzeit bringt dort wenig. Südstaaten wie Tasmanien bekommen sehr kurze Wintertage, dort ist die Idee beliebter. Die Bundesregierung hat es abgelehnt, eine nationale Regel zu erzwingen, und lässt den Staaten die Entscheidung.</p>
<p>Wer Termine über australische Bundesstaaten hinweg plant, sollte stets den aktuellen Versatz prüfen. Mit <a href="/">World Time Sync</a> sehen Sie Live-Uhren für Sydney, Melbourne, Brisbane, Perth und Adelaide.</p>
<h2>Häufige Fragen</h2>
<div class="faq-section">
<div class="faq-item"><h3>Stellen alle Bundesstaaten Australiens die Uhren um?</h3><p>Nein. Der Südosten (New South Wales, Victoria, South Australia, Tasmanien, ACT) befolgt die Sommerzeit; Queensland, Western Australia und das Northern Territory nicht.</p></div>
<div class="faq-item"><h3>Wann beginnt und endet die Sommerzeit in Australien?</h3><p>Beginn am ersten Sonntag im Oktober, Ende am ersten Sonntag im April — also umgekehrt zur Nordhalbkugel.</p></div>
<div class="faq-item"><h3>Wie groß ist der Unterschied zwischen Sydney und Perth im Sommer?</h3><p>Drei Stunden: Sydney UTC+11, Perth UTC+8.</p></div>
</div>''',
 _faq([('Stellen alle Bundesstaaten Australiens die Uhren um?', 'Nein. Der Südosten ja; Queensland, Western Australia und das Northern Territory nicht.'),
       ('Wann beginnt und endet die Sommerzeit in Australien?', 'Erster Sonntag im Oktober bis erster Sonntag im April.'),
       ('Unterschied zwischen Sydney und Perth im Sommer?', 'Drei Stunden: UTC+11 gegenüber UTC+8.')]),
 '2026-06-27', 8))

# ---------------- FR ----------------
POSTS_AU.append(('fr',
 'Comment fonctionne l\u2019heure d\u2019été en Australie — guide état par état',
 'L\u2019heure d\u2019été en Australie varie selon les États. Certains la suivent, d\u2019autres non, et les écarts d\u2019horaire changent quatre fois par an.',
 'heure d\u2019été Australie, fuseaux horaires Australie, heure Sydney, heure Perth',
 ('Accueil', 'Blog', 'Heure d\u2019été en Australie', 'Aller au contenu principal', 'Chargement de World Time...', 'Fil d\u2019Ariane', 'Confidentialité', 'À propos', 'Contact', 'Conditions'),
 '📅 27 juin 2026 &nbsp;·&nbsp; ⏱ 8 min de lecture &nbsp;·&nbsp; 🏷 Australie',
 f'''<h2>Comment fonctionne l\u2019heure d\u2019été en Australie</h2>
<p>L\u2019Australie est l\u2019un des pays les plus déroutants au monde en matière d\u2019heure d\u2019été. Il n\u2019existe pas de règle nationale unique : chaque État et territoire décide seul. Résultat, une mosaïque où l\u2019écart entre Sydney et Brisbane change deux fois par an, tandis que celui entre Sydney et Perth se décale deux fois par an selon un tout autre calendrier.</p>
<h2>Les États qui changent d\u2019heure</h2>
<p>Nouvelle-Galles du Sud, Victoria, Australie-Méridionale, Tasmanie et le Territoire de la capitale australienne passent à l\u2019heure d\u2019été le premier dimanche d\u2019octobre et reviennent en arrière le premier dimanche d\u2019avril. Pendant cette période, ils avancent leurs horloges d\u2019une heure.</p>
<h2>Les États qui ne la pratiquent pas</h2>
<p>Le Queensland, l\u2019Australie-Occidentale et le Territoire du Nord vivent toute l\u2019année à l\u2019heure standard. Le Queensland a soumis la question à un référendum en 1992 — et l\u2019a rejetée. L\u2019Australie-Occidentale a mené une période d\u2019essai de 2006 à 2009 ; le référendum de 2009 a également dit non.</p>
<h2>Le grand écart des différences horaires</h2>
<p>Normalement, Sydney (Nouvelle-Galles du Sud) et Brisbane (Queensland) sont toutes deux sur UTC+10 : aucun décalage. Mais quand l\u2019heure d\u2019été commence en octobre, Sydney passe à UTC+11 pendant que Brisbane reste à UTC+10. Pendant six mois, les deux plus grandes villes de la côte est sont séparées d\u2019une heure.</p>
<p>Perth (Australie-Occidentale) a normalement deux heures de retard sur Sydney (UTC+8 contre UTC+10). Pendant l\u2019heure d\u2019été, ce retard passe à trois heures (UTC+8 contre UTC+11). Pour les entreprises nationales, c\u2019est un casse-tête permanent.</p>
<h2>L\u2019exception : l\u2019île Lord Howe</h2>
<p>L\u2019île Lord Howe, rattachée à la Nouvelle-Galles du Sud, pousse l\u2019idée à l\u2019extrême : elle ne décale son horloge que de 30 minutes au lieu des 60 habituelles. C\u2019est le plus petit changement d\u2019heure d\u2019été au monde — en été, l\u2019île passe d\u2019UTC+10:30 à UTC+11:00.</p>
<h2>Pourquoi l\u2019Australie fonctionne-t-elle ainsi ?</h2>
<p>Réponse courte : fédéralisme et géographie. Les États du nord, proches de l\u2019équateur, voient peu varier la durée du jour au fil de l\u2019année, donc l\u2019heure d\u2019été leur apporte peu. Les États du sud comme la Tasmanie connaissent des hivers très courts en lumière, et l\u2019idée y est plus populaire. Le gouvernement fédéral a renoncé à imposer une règle nationale, laissant chaque État décider.</p>
<p>Si vous planifiez des réunions entre États australiens, vérifiez toujours le décalage actuel. Ouvrez <a href="/">World Time Sync</a> pour voir les horloges en direct de Sydney, Melbourne, Brisbane, Perth et Adélaïde.</p>
<h2>Questions fréquentes</h2>
<div class="faq-section">
<div class="faq-item"><h3>Tous les États australiens changent-ils d\u2019heure ?</h3><p>Non. Le sud-est (Nouvelle-Galles du Sud, Victoria, Australie-Méridionale, Tasmanie, ACT) suit l\u2019heure d\u2019été ; le Queensland, l\u2019Australie-Occidentale et le Territoire du Nord non.</p></div>
<div class="faq-item"><h3>Quand commence et finit l\u2019heure d\u2019été en Australie ?</h3><p>Début le premier dimanche d\u2019octobre, fin le premier dimanche d\u2019avril — donc à l\u2019inverse de l\u2019hémisphère nord.</p></div>
<div class="faq-item"><h3>Quel écart entre Sydney et Perth en été ?</h3><p>Trois heures : Sydney sur UTC+11, Perth sur UTC+8.</p></div>
</div>''',
 _faq([('Tous les États australiens changent-ils d\'heure ?', 'Non. Le sud-est oui ; Queensland, Australie-Occidentale et Territoire du Nord non.'),
       ('Quand commence et finit l\'heure d\'été en Australie ?', 'Premier dimanche d\'octobre jusqu\'au premier dimanche d\'avril.'),
       ('Quel écart entre Sydney et Perth en été ?', 'Trois heures : UTC+11 contre UTC+8.')]),
 '2026-06-27', 8))
