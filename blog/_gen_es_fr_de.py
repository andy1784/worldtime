#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Localized blog posts: ES, FR, DE translations for the 5 new posts."""
import sys
sys.path.insert(0, '/home/kaliuser/worldtime/blog')
from _gen_i18n import make_i18n_post

DATE_DISPLAY = {'es': '8 de julio de 2026', 'fr': '8 juillet 2026', 'de': '8. Juli 2026'}

# =====================================================================
# 1. time-difference-los-angeles-london
# =====================================================================
ES_1 = (
'Si trabajas entre Los Ángeles y Londres, te enfrentas a uno de los mayores desfases laborales del mundo angloparlante: 8 horas en invierno y 7 en verano. Una llamada matutina en Los Ángeles cae por la tarde en Londres, y viceversa. Veamos cómo no perderse.',
'<h2>Resumen de husos horarios</h2>',
'<h3>Los Ángeles (PST/PDT)</h3>',
'<p>Los Ángeles usa la hora del Pacífico: PST (UTC−8) en invierno y PDT (UTC−7) durante el horario de verano de EE. UU., que va del segundo domingo de marzo al primer domingo de noviembre.</p>',
'<h3>Londres (GMT/BST)</h3>',
'<p>Londres usa GMT (UTC+0) en invierno y BST (UTC+1) durante el horario de verano del Reino Unido, del último domingo de marzo al último domingo de octubre.</p>',
'<h2>Diferencia horaria</h2>',
'<p><strong>Invierno (ambos en hora estándar):</strong> Londres va 8 horas por delante de Los Ángeles.</p>',
'<p><strong>Verano (ambos en horario de verano):</strong> Londres va 7 horas por delante de Los Ángeles.</p>',
'<p><strong>Semanas conflictivas:</strong> como EE. UU. y Reino Unido cambian en domingos distintos, durante unas dos semanas en primavera y otoño la diferencia es de 7 u 8 horas según haya cambiado solo uno.</p>',
'<h2>Fórmula de conversión</h2>',
'<p><strong>Hora en Londres = Hora en Los Ángeles + 8 h (invierno) o + 7 h (verano)</strong></p>',
'<h2>Tabla rápida de conversión (LA PST → Londres GMT)</h2>',
'<table><thead><tr><th>Los Ángeles</th><th>Londres</th></tr></thead><tbody>'
'<tr><td>7:00</td><td>15:00</td></tr>'
'<tr><td>9:00</td><td>17:00</td></tr>'
'<tr><td>12:00</td><td>20:00</td></tr>'
'<tr><td>15:00</td><td>23:00</td></tr>'
'<tr><td>18:00</td><td>2:00 (día sig.)</td></tr>'
'<tr><td>21:00</td><td>5:00 (día sig.)</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>Conversor de husos horarios</h2>'
'    <div class="converter-row"><label for="from-time">Hora en Los Ángeles:</label><input type="time" id="from-time" value="09:00"></div>'
'    <div class="converter-row"><label for="dst">Estación:</label>'
'      <select id="dst"><option value="8">Invierno (PST/GMT) — Londres +8h</option><option value="7" selected>Verano (PDT/BST) — Londres +7h</option></select></div>'
'    <div class="converter-row"><label for="to-time">Hora en Londres:</label><input type="time" id="to-time" readonly></div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]+parseInt(d.value)*60; while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); d.addEventListener('change', cv); cv();});</script>",
'<h2>Cuándo sirve</h2>',
'<ul>'
'<li>Acuerdos de entretenimiento y tecnología entre Hollywood y Reino Unido</li>'
'<li>Ingenieros remotos en un equipo de Los Ángeles con interlocutores en Londres</li>'
'<li>Videollamadas familiares a través del Atlántico</li>'
'<li>Ver estrenos de series británicas o transmisiones en vivo de EE. UU.</li>'
'</ul>',
'<h2>Preguntas frecuentes</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>¿Cuál es la diferencia horaria entre Los Ángeles y Londres?</h3><p>8 horas en invierno, 7 en verano. Londres siempre va por delante.</p></div>'
'<div class="faq-item"><h3>¿Por qué cambia una hora?</h3><p>Ambos países usan horario de verano pero cambian en fechas distintas, así que la diferencia oscila entre 7 y 8 horas.</p></div>'
'<div class="faq-item"><h3>Si en Los Ángeles son las 9:00, ¿qué hora es en Londres?</h3><p>17:00 GMT (invierno) o 16:00 BST (verano).</p></div>'
'<div class="faq-item"><h3>¿Mejor momento para una reunión?</h3><p>8–10 a. m. en LA = 16–18:00 en Londres (invierno) o 15–17:00 (verano).</p></div>'
'<div class="faq-item"><h3>¿Usa Los Ángeles GMT?</h3><p>No. Los Ángeles usa hora del Pacífico, que va 8/7 horas por detrás de Londres.</p></div>'
'</div>',
'<p>Consulta la hora en vivo con nuestro <a href="/">reloj mundial</a> y planifica llamadas transatlánticas con el <a href="/meeting-planner.html">planificador de reuniones</a>.</p>'
)

FR_1 = (
'Si vous travaillez entre Los Angeles et Londres, vous affrontez l\'un des plus grands décalages professionnels du monde anglophone : 8 heures en hiver et 7 en été. Un appel matinal à Los Angeles tombe l\'après-midi à Londres, et inversement. Voyons comment ne pas vous y perdre.',
'<h2>Aperçu des fuseaux horaires</h2>',
'<h3>Los Angeles (PST/PDT)</h3>',
'<p>Los Angeles suit l\'heure du Pacifique : PST (UTC−8) en hiver et PDT (UTC−7) pendant l\'heure d\'été des États-Unis, du deuxième dimanche de mars au premier dimanche de novembre.</p>',
'<h3>Londres (GMT/BST)</h3>',
'<p>Londres utilise GMT (UTC+0) en hiver et BST (UTC+1) pendant l\'heure d\'été du Royaume-Uni, du dernier dimanche de mars au dernier dimanche d\'octobre.</p>',
'<h2>Différence horaire</h2>',
'<p><strong>Hiver (les deux à l\'heure normale) :</strong> Londres est à 8 heures devant Los Angeles.</p>',
'<p><strong>Été (les deux à l\'heure d\'été) :</strong> Londres est à 7 heures devant Los Angeles.</p>',
'<p><strong>Semaines délicates :</strong> comme les États-Unis et le Royaume-Uni changent à des dates différentes, pendant environ deux semaines au printemps et en automne, l\'écart est de 7 ou 8 heures selon qu\'une seule partie a changé.</p>',
'<h2>Formule de conversion</h2>',
'<p><strong>Heure à Londres = Heure à Los Angeles + 8 h (hiver) ou + 7 h (été)</strong></p>',
'<h2>Tableau de conversion rapide (LA PST → Londres GMT)</h2>',
'<table><thead><tr><th>Los Angeles</th><th>Londres</th></tr></thead><tbody>'
'<tr><td>7:00</td><td>15:00</td></tr>'
'<tr><td>9:00</td><td>17:00</td></tr>'
'<tr><td>12:00</td><td>20:00</td></tr>'
'<tr><td>15:00</td><td>23:00</td></tr>'
'<tr><td>18:00</td><td>2:00 (jr suiv.)</td></tr>'
'<tr><td>21:00</td><td>5:00 (jr suiv.)</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>Convertisseur de fuseaux horaires</h2>'
'    <div class="converter-row"><label for="from-time">Heure à Los Angeles :</label><input type="time" id="from-time" value="09:00"></div>'
'    <div class="converter-row"><label for="dst">Saison :</label>'
'      <select id="dst"><option value="8">Hiver (PST/GMT) — Londres +8h</option><option value="7" selected>Été (PDT/BST) — Londres +7h</option></select></div>'
'    <div class="converter-row"><label for="to-time">Heure à Londres :</label><input type="time" id="to-time" readonly></div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]+parseInt(d.value)*60; while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); d.addEventListener('change', cv); cv();});</script>",
'<h2>À quoi cela sert</h2>',
'<ul>'
'<li>Contrats dans le divertissement et la tech entre Hollywood et le Royaume-Uni</li>'
'<li>Ingénieurs à distance dans une équipe de Los Angeles avec des interlocuteurs à Londres</li>'
'<li>Appels vidéo familiaux à travers l\'Atlantique</li>'
'<li>Suivre les premières de séries britanniques ou les directs américains</li>'
'</ul>',
'<h2>Questions fréquentes</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>Quelle est la différence horaire entre Los Angeles et Londres ?</h3><p>8 heures en hiver, 7 en été. Londres est toujours en avance.</p></div>'
'<div class="faq-item"><h3>Pourquoi varie-t-elle d\'une heure ?</h3><p>Les deux pays utilisent l\'heure d\'été mais à des dates différentes, l\'écart oscille donc entre 7 et 8 heures.</p></div>'
'<div class="faq-item"><h3>S\'il est 9:00 à Los Angeles, quelle heure est-il à Londres ?</h3><p>17:00 GMT (hiver) ou 16:00 BST (été).</p></div>'
'<div class="faq-item"><h3>Le meilleur moment pour une réunion ?</h3><p>8–10 h à LA = 16–18:00 à Londres (hiver) ou 15–17:00 (été).</p></div>'
'<div class="faq-item"><h3>Los Angeles utilise-t-il GMT ?</h3><p>Non. Los Angeles utilise l\'heure du Pacifique, qui retarde de 8/7 heures par rapport à Londres.</p></div>'
'</div>',
'<p>Consultez l\'heure en direct avec notre <a href="/">horloge mondiale</a> et planifiez vos appels transatlantiques avec le <a href="/meeting-planner.html">planificateur de réunions</a>.</p>'
)

DE_1 = (
'Wenn Sie zwischen Los Angeles und London arbeiten, haben Sie es mit einer der größten Arbeitszeitlücken der englischsprachigen Welt zu tun: 8 Stunden im Winter und 7 im Sommer. Ein Morgenanruf in Los Angeles landet am Nachmittag in London und umgekehrt. So behalten Sie den Überblick.',
'<h2>Überblick über die Zeitzonen</h2>',
'<h3>Los Angeles (PST/PDT)</h3>',
'<p>Los Angeles liegt in der pazifischen Zeit: PST (UTC−8) im Winter und PDT (UTC−7) während der US-Sommerzeit, die vom zweiten Sonntag im März bis zum ersten Sonntag im November dauert.</p>',
'<h3>London (GMT/BST)</h3>',
'<p>London verwendet GMT (UTC+0) im Winter und BST (UTC+1) während der britischen Sommerzeit, vom letzten Sonntag im März bis zum letzten Sonntag im Oktober.</p>',
'<h2>Zeitunterschied</h2>',
'<p><strong>Winter (beide Normalzeit):</strong> London liegt 8 Stunden vor Los Angeles.</p>',
'<p><strong>Sommer (beide Sommerzeit):</strong> London liegt 7 Stunden vor Los Angeles.</p>',
'<p><strong>Knifflige Wochen:</strong> Da die USA und das Vereinigte Königreich an unterschiedlichen Sonntagen umstellen, beträgt die Lücke im Frühjahr und Herbst für etwa zwei Wochen 7 oder 8 Stunden, wenn nur eine Seite gewechselt hat.</p>',
'<h2>Umrechnungsformel</h2>',
'<p><strong>Zeit in London = Zeit in Los Angeles + 8 h (Winter) oder + 7 h (Sommer)</strong></p>',
'<h2>Schnelle Umrechnungstabelle (LA PST → London GMT)</h2>',
'<table><thead><tr><th>Los Angeles</th><th>London</th></tr></thead><tbody>'
'<tr><td>7:00</td><td>15:00</td></tr>'
'<tr><td>9:00</td><td>17:00</td></tr>'
'<tr><td>12:00</td><td>20:00</td></tr>'
'<tr><td>15:00</td><td>23:00</td></tr>'
'<tr><td>18:00</td><td>2:00 (nächster Tag)</td></tr>'
'<tr><td>21:00</td><td>5:00 (nächster Tag)</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>Zeitzonen-Umrechner</h2>'
'    <div class="converter-row"><label for="from-time">Zeit in Los Angeles:</label><input type="time" id="from-time" value="09:00"></div>'
'    <div class="converter-row"><label for="dst">Jahreszeit:</label>'
'      <select id="dst"><option value="8">Winter (PST/GMT) — London +8h</option><option value="7" selected>Sommer (PDT/BST) — London +7h</option></select></div>'
'    <div class="converter-row"><label for="to-time">Zeit in London:</label><input type="time" id="to-time" readonly></div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]+parseInt(d.value)*60; while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); d.addEventListener('change', cv); cv();});</script>",
'<h2>Wann es nützlich ist</h2>',
'<ul>'
'<li>Deals in Unterhaltung und Technik zwischen Hollywood und dem Vereinigten Königreich</li>'
'<li>Remote-Entwickler in einem Team aus Los Angeles mit Ansprechpartnern in London</li>'
'<li>Familien-Videocalls über den Atlantik</li>'
'<li>Briten-Serienpremieren oder US-Livestreams verfolgen</li>'
'</ul>',
'<h2>Häufig gestellte Fragen</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>Wie groß ist der Zeitunterschied zwischen Los Angeles und London?</h3><p>8 Stunden im Winter, 7 im Sommer. London liegt immer vorne.</p></div>'
'<div class="faq-item"><h3>Warum ändert er sich um eine Stunde?</h3><p>Beide Länder haben Sommerzeit, stellen aber an unterschiedlichen Terminen um, daher schwankt die Lücke zwischen 7 und 8 Stunden.</p></div>'
'<div class="faq-item"><h3>Wenn es in Los Angeles 9:00 ist, wie spät ist es in London?</h3><p>17:00 GMT (Winter) oder 16:00 BST (Sommer).</p></div>'
'<div class="faq-item"><h3>Beste Zeit für ein Meeting?</h3><p>8–10 Uhr in LA = 16–18:00 in London (Winter) oder 15–17:00 (Sommer).</p></div>'
'<div class="faq-item"><h3>Nutzt Los Angeles GMT?</h3><p>Nein. Los Angeles nutzt die pazifische Zeit, die 8/7 Stunden hinter London liegt.</p></div>'
'</div>',
'<p>Prüfen Sie die Live-Zeit mit unserer <a href="/">Weltuhr</a> und planen Sie transatlantische Anrufe mit dem <a href="/meeting-planner.html">Meeting-Planer</a>.</p>'
)

# ----- 2. time-difference-new-york-sydney -----
ES_2 = (
'Nueva York y Sídney están casi tan lejos aislados como dos grandes ciudades de negocios pueden estar: la diferencia es de 14 a 16 horas, y como las estaciones son opuestas, sus períodos de horario de verano apenas se solapan. Eso hace que planificar sea un rompecabezas, pero solvable.',
'<h2>Resumen de husos horarios</h2>',
'<h3>Nueva York (EST/EDT)</h3>',
'<p>Nueva York usa la hora del Este: EST (UTC−5) en invierno y EDT (UTC−4) durante el horario de verano de EE. UU. (del segundo domingo de marzo al primer domingo de noviembre).</p>',
'<h3>Sídney (AEST/AEDT)</h3>',
'<p>Sídney es AEST (UTC+10) en invierno y AEDT (UTC+11) durante el horario de verano australiano (del primer domingo de octubre al primer domingo de abril).</p>',
'<h2>Diferencia horaria</h2>',
'<p><strong>Verano australiano / invierno estadounidense:</strong> Sídney va 16 horas por delante de Nueva York.</p>',
'<p><strong>Invierno australiano / verano estadounidense:</strong> Sídney va 14 horas por delante de Nueva York.</p>',
'<p><strong>Semanas de solape:</strong> durante los breves periodos en que solo uno ha cambiado, la diferencia es de 15 horas.</p>',
'<h2>Fórmula de conversión</h2>',
'<p><strong>Hora en Sídney = Hora en Nueva York + 16 h (invierno EE. UU.) o + 14 h (verano EE. UU.)</strong></p>',
'<h2>Tabla rápida de conversión (Nueva York EST → Sídney AEDT, invierno EE. UU.)</h2>',
'<table><thead><tr><th>Nueva York</th><th>Sídney</th></tr></thead><tbody>'
'<tr><td>7:00</td><td>23:00 (mismo día)</td></tr>'
'<tr><td>9:00</td><td>1:00 (día sig.)</td></tr>'
'<tr><td>12:00</td><td>4:00 (día sig.)</td></tr>'
'<tr><td>17:00</td><td>9:00 (día sig.)</td></tr>'
'<tr><td>20:00</td><td>12:00 (día sig.)</td></tr>'
'<tr><td>23:00</td><td>15:00 (día sig.)</td></tr>'
'</tbody></table>',
'<h2>Cuándo sirve</h2>',
'<ul>'
'<li>Negocios, finanzas y mudanzas entre EE. UU. y Australia</li>'
'<li>Coordinar equipos remotos a través del Pacífico</li>'
'<li>Llamadas familiares entre la Costa Este y Sídney</li>'
'<li>Seguir deportes de EE. UU. o noticias australianas a través de la línea internacional</li>'
'</ul>',
'<h2>Preguntas frecuentes</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>¿Cuál es la diferencia horaria entre Nueva York y Sídney?</h3><p>14 a 16 horas según la estación; Sídney va muy por delante.</p></div>'
'<div class="faq-item"><h3>¿Por qué es tan grande?</h3><p>Las ciudades están en lados opuestos del planeta y su horario de verano cae en mitades opuestas del año.</p></div>'
'<div class="faq-item"><h3>Si en Nueva York son las 9:00, ¿qué hora es en Sídney?</h3><p>1:00 del día siguiente (invierno EE. UU., AEDT) o 23:00 del mismo día (verano EE. UU., AEST).</p></div>'
'<div class="faq-item"><h3>¿Mejor solape para una llamada?</h3><p>7–9 a. m. en Nueva York = 23:00–1:00 en Sídney (difícil); muchos equipos simplemente se dejan notas asíncronas.</p></div>'
'<div class="faq-item"><h3>¿Sídney cambia la hora?</h3><p>Sí, AEDT en verano, pero con un calendario opuesto al de Nueva York.</p></div>'
'</div>',
'<p>Usa nuestro <a href="/">reloj mundial</a> para la hora en vivo y el <a href="/meeting-planner.html">planificador de reuniones</a> para encontrar cualquier solape real.</p>'
)

FR_2 = (
'New York et Sydney sont à peu près aussi éloignés que peuvent l\'être deux grandes villes d\'affaires : la différence est de 14 à 16 heures, et comme les saisons y sont inversées, leurs périodes d\'heure d\'été se chevauchent à peine. Planifier devient un casse-tête, mais résolvable.',
'<h2>Aperçu des fuseaux horaires</h2>',
'<h3>New York (EST/EDT)</h3>',
'<p>New York suit l\'heure de l\'Est : EST (UTC−5) en hiver et EDT (UTC−4) pendant l\'heure d\'été des États-Unis (du deuxième dimanche de mars au premier dimanche de novembre).</p>',
'<h3>Sydney (AEST/AEDT)</h3>',
'<p>Sydney est AEST (UTC+10) en hiver et AEDT (UTC+11) pendant l\'heure d\'été australienne (du premier dimanche d\'octobre au premier dimanche d\'avril).</p>',
'<h2>Différence horaire</h2>',
'<p><strong>Été australien / hiver américain :</strong> Sydney est à 16 heures devant New York.</p>',
'<p><strong>Hiver australien / été américain :</strong> Sydney est à 14 heures devant New York.</p>',
'<p><strong>Semaines de chevauchement :</strong> pendant les brèves périodes où une seule partie a changé, l\'écart est de 15 heures.</p>',
'<h2>Formule de conversion</h2>',
'<p><strong>Heure à Sydney = Heure à New York + 16 h (hiver US) ou + 14 h (été US)</strong></p>',
'<h2>Tableau de conversion rapide (New York EST → Sydney AEDT, hiver US)</h2>',
'<table><thead><tr><th>New York</th><th>Sydney</th></tr></thead><tbody>'
'<tr><td>7:00</td><td>23:00 (même jour)</td></tr>'
'<tr><td>9:00</td><td>1:00 (jr suiv.)</td></tr>'
'<tr><td>12:00</td><td>4:00 (jr suiv.)</td></tr>'
'<tr><td>17:00</td><td>9:00 (jr suiv.)</td></tr>'
'<tr><td>20:00</td><td>12:00 (jr suiv.)</td></tr>'
'<tr><td>23:00</td><td>15:00 (jr suiv.)</td></tr>'
'</tbody></table>',
'<h2>À quoi cela sert</h2>',
'<ul>'
'<li>Affaires, finance et expatriation entre les États-Unis et l\'Australie</li>'
'<li>Coordonner des équipes à distance à travers le Pacifique</li>'
'<li>Appels familiaux entre la côte Est et Sydney</li>'
'<li>Suivre le sport américain ou l\'actualité australienne à travers la ligne de changement de date</li>'
'</ul>',
'<h2>Questions fréquentes</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>Quelle est la différence horaire entre New York et Sydney ?</h3><p>14 à 16 heures selon la saison ; Sydney est très en avance.</p></div>'
'<div class="faq-item"><h3>Pourquoi est-elle si grande ?</h3><p>Les villes sont aux antipodes et leur heure d\'été tombe en des moitiés d\'année opposées.</p></div>'
'<div class="faq-item"><h3>S\'il est 9:00 à New York, quelle heure est-il à Sydney ?</h3><p>1:00 le lendemain (hiver US, AEDT) ou 23:00 le même jour (été US, AEST).</p></div>'
'<div class="faq-item"><h3>Meilleur chevauchement pour un appel ?</h3><p>7–9 h à New York = 23:00–1:00 à Sydney (difficile) ; beaucoup d\'équipes se contentent de notes asynchrones.</p></div>'
'<div class="faq-item"><h3>Sydney change-t-il d\'heure ?</h3><p>Oui, AEDT en été, mais selon un calendrier opposé à New York.</p></div>'
'</div>',
'<p>Utilisez notre <a href="/">horloge mondiale</a> pour l\'heure en direct et le <a href="/meeting-planner.html">planificateur de réunions</a> pour trouver un véritable chevauchement.</p>'
)

DE_2 = (
'New York und Sydney sind so weit voneinander entfernt, wie es zwei Geschäftsstädte nur sein können: Der Unterschied beträgt 14 bis 16 Stunden, und da die Jahreszeiten entgegengesetzt sind, überschneiden sich ihre Sommerzeiten kaum. Das macht die Planung zu einem Rätsel, aber einem lösbaren.',
'<h2>Überblick über die Zeitzonen</h2>',
'<h3>New York (EST/EDT)</h3>',
'<p>New York folgt der Eastern Time: EST (UTC−5) im Winter und EDT (UTC−4) während der US-Sommerzeit (vom zweiten Sonntag im März bis zum ersten Sonntag im November).</p>',
'<h3>Sydney (AEST/AEDT)</h3>',
'<p>Sydney ist AEST (UTC+10) im Winter und AEDT (UTC+11) während der australischen Sommerzeit (vom ersten Sonntag im Oktober bis zum ersten Sonntag im April).</p>',
'<h2>Zeitunterschied</h2>',
'<p><strong>Australischer Sommer / US-Winter:</strong> Sydney liegt 16 Stunden vor New York.</p>',
'<p><strong>Australischer Winter / US-Sommer:</strong> Sydney liegt 14 Stunden vor New York.</p>',
'<p><strong>Überschneidungswochen:</strong> In den kurzen Phasen, in denen nur eine Seite umgestellt hat, beträgt die Differenz 15 Stunden.</p>',
'<h2>Umrechnungsformel</h2>',
'<p><strong>Zeit in Sydney = Zeit in New York + 16 h (US-Winter) oder + 14 h (US-Sommer)</strong></p>',
'<h2>Schnelle Umrechnungstabelle (New York EST → Sydney AEDT, US-Winter)</h2>',
'<table><thead><tr><th>New York</th><th>Sydney</th></tr></thead><tbody>'
'<tr><td>7:00</td><td>23:00 (gleicher Tag)</td></tr>'
'<tr><td>9:00</td><td>1:00 (nächster Tag)</td></tr>'
'<tr><td>12:00</td><td>4:00 (nächster Tag)</td></tr>'
'<tr><td>17:00</td><td>9:00 (nächster Tag)</td></tr>'
'<tr><td>20:00</td><td>12:00 (nächster Tag)</td></tr>'
'<tr><td>23:00</td><td>15:00 (nächster Tag)</td></tr>'
'</tbody></table>',
'<h2>Wann es nützlich ist</h2>',
'<ul>'
'<li>Geschäfte, Finanzen und Umzüge zwischen den USA und Australien</li>'
'<li>Remote-Teams über den Pazifik koordinieren</li>'
'<li>Familienanrufe zwischen Ostküste und Sydney</li>'
'<li>US-Sport oder australische Nachrichten über die Datumsgrenze verfolgen</li>'
'</ul>',
'<h2>Häufig gestellte Fragen</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>Wie groß ist der Zeitunterschied zwischen New York und Sydney?</h3><p>14 bis 16 Stunden je nach Saison; Sydney liegt weit vorne.</p></div>'
'<div class="faq-item"><h3>Warum ist er so groß?</h3><p>Die Städte liegen auf entgegengesetzten Seiten des Globus, und ihre Sommerzeit fällt in gegensätzliche Jahreshälften.</p></div>'
'<div class="faq-item"><h3>Wenn es in New York 9:00 ist, wie spät ist es in Sydney?</h3><p>1:00 am nächsten Tag (US-Winter, AEDT) oder 23:00 am gleichen Tag (US-Sommer, AEST).</p></div>'
'<div class="faq-item"><h3>Bester Überlapp für einen Anruf?</h3><p>7–9 Uhr in New York = 23:00–1:00 in Sydney (schwierig); viele Teams tauschen einfach asynchrone Notizen aus.</p></div>'
'<div class="faq-item"><h3>Stellt Sydney die Uhr um?</h3><p>Ja, AEDT im Sommer, aber nach einem Zeitplan gegenläufig zu New York.</p></div>'
'</div>',
'<p>Nutzen Sie unsere <a href="/">Weltuhr</a> für die Live-Zeit und den <a href="/meeting-planner.html">Meeting-Planer</a>, um eine echte Überschneidung zu finden.</p>'
)

# ----- 3. convert-cet-to-est -----
ES_3 = (
'Convertir la hora de Europa Central a la del Este de EE. UU. se usa constantemente en el negocio transatlántico, las instituciones europeas y cualquiera que llame entre ciudades como Berlín, París o Madrid y Nueva York o Washington. La diferencia es de 6 horas en invierno y 5 en verano.',
'<h2>Resumen de husos horarios</h2>',
'<h3>Hora de Europa Central (CET)</h3>',
'<p>CET es UTC+1 en invierno y CEST (UTC+2) durante la hora de verano europea, que va del último domingo de marzo al último domingo de octubre.</p>',
'<h3>Hora del Este (EST/EDT)</h3>',
'<p>La hora del Este de EE. UU. es EST (UTC−5) en invierno y EDT (UTC−4) durante la hora de verano estadounidense (del segundo domingo de marzo al primer domingo de noviembre).</p>',
'<h2>Diferencia horaria</h2>',
'<p><strong>Invierno (ambos en hora estándar):</strong> CET va 6 horas por delante de EST.</p>',
'<p><strong>Verano (ambos en horario de verano):</strong> CET va 6 horas por delante de EDT.</p>',
'<p><strong>Semanas de transición:</strong> cuando solo ha cambiado EE. UU. o solo Europa, la diferencia es de 5 o 7 horas por un breve tiempo.</p>',
'<h2>Fórmula de conversión</h2>',
'<p><strong>EST = CET − 6 horas (invierno) / CET − 6 horas (verano, ambos en horario de verano)</strong></p>',
'<p>Como ambas regiones usan horario de verano, la diferencia de 6 horas se mantiene la mayor parte del año; solo cambia en las escasas semanas en que no coinciden los cambios.</p>',
'<h2>Tabla rápida de conversión (CET → EST)</h2>',
'<table><thead><tr><th>Hora centroeuropea</th><th>Hora del Este EE. UU.</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>3:00</td></tr>'
'<tr><td>12:00</td><td>6:00</td></tr>'
'<tr><td>14:00</td><td>8:00</td></tr>'
'<tr><td>17:00</td><td>11:00</td></tr>'
'<tr><td>20:00</td><td>14:00</td></tr>'
'<tr><td>23:00</td><td>17:00</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>Conversor de husos horarios</h2>'
'    <div class="converter-row"><label for="from-time">Hora en CET/CEST:</label><input type="time" id="from-time" value="14:00"></div>'
'    <div class="converter-row"><label for="to-time">Hora en EST/EDT:</label><input type="time" id="to-time" readonly></div>'
'    <div class="converter-note">Resta 6 horas (CET→EST). Para una fecha concreta usa nuestro <a href="/meeting-planner.html">planificador de reuniones</a>.</div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]-360; while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); cv();});</script>",
'<h2>Cuándo sirve</h2>',
'<ul>'
'<li>Llamadas de negocios UE-EE. UU. (París, Berlín, Madrid y Nueva York)</li>'
'<li>Coordinar con colegas remotos europeos desde la costa este de EE. UU.</li>'
'<li>Planificar webinars a través del Atlántico</li>'
'<li>Alinear aperturas de mercados y operaciones</li>'
'</ul>',
'<h2>Preguntas frecuentes</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>¿Cuál es la diferencia horaria entre CET y EST?</h3><p>Normalmente 6 horas; CET va por delante. Brevemente baja a 5 o sube a 7 en las semanas de cambio.</p></div>'
'<div class="faq-item"><h3>¿Qué ciudades usan CET?</h3><p>París, Berlín, Madrid, Roma, Ámsterdam, Viena y la mayor parte de Europa central.</p></div>'
'<div class="faq-item"><h3>Si en París son las 14:00, ¿qué hora es en Nueva York?</h3><p>8:00 EST (invierno) o 8:00 EDT (verano): siguen siendo 6 horas.</p></div>'
'<div class="faq-item"><h3>¿Se mantiene la diferencia de 6 horas todo el año?</h3><p>Casi. Solo cambia en las semanas en que Europa y EE. UU. cambian en fechas distintas.</p></div>'
'<div class="faq-item"><h3>¿Cómo convierto EST a CET?</h3><p>Suma 6 horas a la hora del Este.</p></div>'
'</div>',
'<p>Para comparar en tiempo real, abre nuestro <a href="/">reloj mundial</a> y elige tus ciudades.</p>'
)

FR_3 = (
'Convertir l\'heure d\'Europe centrale en heure de l\'Est des États-Unis est un exercice constant pour les affaires transatlantiques, les institutions européennes et tous ceux qui appellent entre des villes comme Berlin, Paris ou Madrid et New York ou Washington. L\'écart est de 6 heures en hiver et de 5 en été.',
'<h2>Aperçu des fuseaux horaires</h2>',
'<h3>Heure d\'Europe centrale (CET)</h3>',
'<p>CET est UTC+1 en hiver et CEST (UTC+2) pendant l\'heure d\'été européenne, du dernier dimanche de mars au dernier dimanche d\'octobre.</p>',
'<h3>Heure de l\'Est (EST/EDT)</h3>',
'<p>L\'heure de l\'Est des États-Unis est EST (UTC−5) en hiver et EDT (UTC−4) pendant l\'heure d\'été américaine (du deuxième dimanche de mars au premier dimanche de novembre).</p>',
'<h2>Différence horaire</h2>',
'<p><strong>Hiver (les deux à l\'heure normale) :</strong> CET est à 6 heures devant EST.</p>',
'<p><strong>Été (les deux à l\'heure d\'été) :</strong> CET est à 6 heures devant EDT.</p>',
'<p><strong>Semaines de transition :</strong> quand seuls les États-Unis ou seule l\'Europe ont changé, l\'écart est de 5 ou 7 heures un temps court.</p>',
'<h2>Formule de conversion</h2>',
'<p><strong>EST = CET − 6 heures (hiver) / CET − 6 heures (été, les deux à l\'heure d\'été)</strong></p>',
'<p>Comme les deux régions observent l\'heure d\'été, l\'écart de 6 heures tient en fait presque toute l\'année ; il ne change que durant les rares semaines où les bascules ne coïncident pas.</p>',
'<h2>Tableau de conversion rapide (CET → EST)</h2>',
'<table><thead><tr><th>Heure d\'Europe centrale</th><th>Heure de l\'Est US</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>3:00</td></tr>'
'<tr><td>12:00</td><td>6:00</td></tr>'
'<tr><td>14:00</td><td>8:00</td></tr>'
'<tr><td>17:00</td><td>11:00</td></tr>'
'<tr><td>20:00</td><td>14:00</td></tr>'
'<tr><td>23:00</td><td>17:00</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>Convertisseur de fuseaux horaires</h2>'
'    <div class="converter-row"><label for="from-time">Heure en CET/CEST :</label><input type="time" id="from-time" value="14:00"></div>'
'    <div class="converter-row"><label for="to-time">Heure en EST/EDT :</label><input type="time" id="to-time" readonly></div>'
'    <div class="converter-note">Soustrait 6 heures (CET→EST). Pour une date précise, utilisez notre <a href="/meeting-planner.html">planificateur de réunions</a>.</div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]-360; while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); cv();});</script>",
'<h2>À quoi cela sert</h2>',
'<ul>'
'<li>Appels d\'affaires UE-États-Unis (Paris, Berlin, Madrid et New York)</li>'
'<li>Coordonner avec des collègues européens à distance depuis la côte est des États-Unis</li>'
'<li>Planifier des webinaires à travers l\'Atlantique</li>'
'<li>Aligner les ouvertures de marchés et les opérations</li>'
'</ul>',
'<h2>Questions fréquentes</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>Quelle est la différence horaire entre CET et EST ?</h3><p>En général 6 heures ; CET est en avance. Elle passe brièvement à 5 ou 7 lors des semaines de bascule.</p></div>'
'<div class="faq-item"><h3>Quelles villes utilisent CET ?</h3><p>Paris, Berlin, Madrid, Rome, Amsterdam, Vienne et la majeure partie de l\'Europe centrale.</p></div>'
'<div class="faq-item"><h3>S\'il est 14:00 à Paris, quelle heure est-il à New York ?</h3><p>8:00 EST (hiver) ou 8:00 EDT (été) : reste 6 heures.</p></div>'
'<div class="faq-item"><h3>L\'écart de 6 heures tient-il toute l\'année ?</h3><p>Presque. Il ne change que les semaines où l\'Europe et les États-Unis basculent à des dates différentes.</p></div>'
'<div class="faq-item"><h3>Comment convertir EST en CET ?</h3><p>Ajoutez 6 heures à l\'heure de l\'Est.</p></div>'
'</div>',
'<p>Pour comparer en temps réel, ouvrez notre <a href="/">horloge mondiale</a> et choisissez vos villes.</p>'
)

DE_3 = (
'Die Umrechnung von Mitteleuropäischer Zeit in die US-Ostküstenzeit wird im transatlantischen Geschäft, von europäischen Institutionen und von allen genutzt, die zwischen Städten wie Berlin, Paris oder Madrid und New York oder Washington telefonieren. Der Unterschied beträgt 6 Stunden im Winter und 5 im Sommer.',
'<h2>Überblick über die Zeitzonen</h2>',
'<h3>Mitteleuropäische Zeit (CET)</h3>',
'<p>CET ist UTC+1 im Winter und CEST (UTC+2) während der europäischen Sommerzeit, die vom letzten Sonntag im März bis zum letzten Sonntag im Oktober dauert.</p>',
'<h3>Ostzeit (EST/EDT)</h3>',
'<p>Die US-Ostzeit ist EST (UTC−5) im Winter und EDT (UTC−4) während der US-Sommerzeit (vom zweiten Sonntag im März bis zum ersten Sonntag im November).</p>',
'<h2>Zeitunterschied</h2>',
'<p><strong>Winter (beide Normalzeit):</strong> CET liegt 6 Stunden vor EST.</p>',
'<p><strong>Sommer (beide Sommerzeit):</strong> CET liegt 6 Stunden vor EDT.</p>',
'<p><strong>Übergangswochen:</strong> Wenn nur die USA oder nur Europa umgestellt haben, beträgt der Unterschied kurzzeitig 5 oder 7 Stunden.</p>',
'<h2>Umrechnungsformel</h2>',
'<p><strong>EST = CET − 6 Stunden (Winter) / CET − 6 Stunden (Sommer, beide Sommerzeit)</strong></p>',
'<p>Da beide Regionen die Sommerzeit beachten, hält sich die 6-Stunden-Lücke das ganze Jahr über; sie ändert sich nur in den wenigen Wochen, in denen die Umstellungen nicht zusammenfallen.</p>',
'<h2>Schnelle Umrechnungstabelle (CET → EST)</h2>',
'<table><thead><tr><th>Mitteleur. Zeit</th><th>US-Ostzeit</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>3:00</td></tr>'
'<tr><td>12:00</td><td>6:00</td></tr>'
'<tr><td>14:00</td><td>8:00</td></tr>'
'<tr><td>17:00</td><td>11:00</td></tr>'
'<tr><td>20:00</td><td>14:00</td></tr>'
'<tr><td>23:00</td><td>17:00</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>Zeitzonen-Umrechner</h2>'
'    <div class="converter-row"><label for="from-time">Zeit in CET/CEST:</label><input type="time" id="from-time" value="14:00"></div>'
'    <div class="converter-row"><label for="to-time">Zeit in EST/EDT:</label><input type="time" id="to-time" readonly></div>'
'    <div class="converter-note">Zieht 6 Stunden ab (CET→EST). Für ein bestimmtes Datum nutzen Sie unseren <a href="/meeting-planner.html">Meeting-Planer</a>.</div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]-360; while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); cv();});</script>",
'<h2>Wann es nützlich ist</h2>',
'<ul>'
'<li>Geschäftliche Anrufe EU-USA (Paris, Berlin, Madrid und New York)</li>'
'<li>Mit europäischen Remote-Kollegen von der US-Ostküste koordinieren</li>'
'<li>Webinare über den Atlantik planen</li>'
'<li>Marktöffnungen und Handel abstimmen</li>'
'</ul>',
'<h2>Häufig gestellte Fragen</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>Wie groß ist der Zeitunterschied zwischen CET und EST?</h3><p>Meist 6 Stunden; CET liegt vorne. In den Umstellungswochen kurz 5 oder 7 Stunden.</p></div>'
'<div class="faq-item"><h3>Welche Städte nutzen CET?</h3><p>Paris, Berlin, Madrid, Rom, Amsterdam, Wien und der Großteil Mitteleuropas.</p></div>'
'<div class="faq-item"><h3>Wenn es in Paris 14:00 ist, wie spät ist es in New York?</h3><p>8:00 EST (Winter) oder 8:00 EDT (Sommer): bleibt 6 Stunden.</p></div>'
'<div class="faq-item"><h3>Hält der 6-Stunden-Abstand das ganze Jahr?</h3><p>Fast. Er ändert sich nur in den Wochen, in denen Europa und die USA an unterschiedlichen Terminen umstellen.</p></div>'
'<div class="faq-item"><h3>Wie rechne ich EST in CET um?</h3><p>Addieren Sie 6 Stunden zur Ostzeit.</p></div>'
'</div>',
'<p>Für den Echtzeitvergleich öffnen Sie unsere <a href="/">Weltuhr</a> und wählen Sie Ihre Städte.</p>'
)

# ----- 4. time-difference-dubai-london -----
ES_4 = (
'Dubái y Londres forman un corredor de negocios popular, y es uno de los más fáciles de gestionar: la diferencia es de exactamente 4 horas y nunca cambia, porque ninguna de las dos ciudades usa horario de verano.',
'<h2>Resumen de husos horarios</h2>',
'<h3>Dubái (GST)</h3>',
'<p>Dubái usa la hora estándar del Golfo, UTC+4, todo el año. Los EAU no aplican horario de verano.</p>',
'<h3>Londres (GMT/BST)</h3>',
'<p>Londres es GMT (UTC+0) en invierno y BST (UTC+1) en verano. El Reino Unido sí usa horario de verano.</p>',
'<h2>Diferencia horaria</h2>',
'<p><strong>Invierno en Reino Unido:</strong> Dubái va 4 horas por delante de Londres.</p>',
'<p><strong>Verano en Reino Unido:</strong> Dubái va 3 horas por delante de Londres (porque Londres pasa a BST).</p>',
'<p>Nota: el propio desfase de Dubái no cambia; la diferencia solo se mueve por Londres.</p>',
'<h2>Fórmula de conversión</h2>',
'<p><strong>Hora en Dubái = Hora en Londres + 4 h (invierno) o + 3 h (verano)</strong></p>',
'<h2>Tabla rápida de conversión (Dubái GST → Londres)</h2>',
'<table><thead><tr><th>Dubái</th><th>Londres (GMT, invierno)</th><th>Londres (BST, verano)</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>5:00</td><td>6:00</td></tr>'
'<tr><td>12:00</td><td>8:00</td><td>9:00</td></tr>'
'<tr><td>15:00</td><td>11:00</td><td>12:00</td></tr>'
'<tr><td>18:00</td><td>14:00</td><td>15:00</td></tr>'
'<tr><td>21:00</td><td>17:00</td><td>18:00</td></tr>'
'<tr><td>0:00</td><td>20:00</td><td>21:00</td></tr>'
'</tbody></table>',
'<h2>Cuándo sirve</h2>',
'<ul>'
'<li>Finanzas y comercio entre EAU y Reino Unido</li>'
'<li>Planificar vuelos a través de los hub de Dubái</li>'
'<li>Equipos remotos divididos entre el Golfo y Londres</li>'
'<li>Tratos inmobiliarios en ambos mercados</li>'
'</ul>',
'<h2>Preguntas frecuentes</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>¿Cuál es la diferencia horaria entre Dubái y Londres?</h3><p>4 horas en invierno en Reino Unido, 3 en verano. Dubái no cambia.</p></div>'
'<div class="faq-item"><h3>¿Dubái usa horario de verano?</h3><p>No. Los EAU mantienen la hora estándar del Golfo (UTC+4) todo el año.</p></div>'
'<div class="faq-item"><h3>Si en Dubái son las 12:00, ¿qué hora es en Londres?</h3><p>8:00 GMT en invierno o 9:00 BST en verano.</p></div>'
'<div class="faq-item"><h3>¿Mejor ventana para reunión?</h3><p>8:00–12:00 Londres = 12:00–16:00 Dubái (invierno) o 11:00–15:00 (verano).</p></div>'
'<div class="faq-item"><h3>¿Por qué solo se mueve un lado?</h3><p>Solo el Reino Unido usa horario de verano; los EAU mantienen un desfase fijo.</p></div>'
'</div>',
'<p>Ve ambas ciudades en vivo en nuestro <a href="/">reloj mundial</a> y planifica con el <a href="/meeting-planner.html">planificador de reuniones</a>.</p>'
)

FR_4 = (
'Doubaï et Londres forment un corridor d\'affaires populaire, et l\'un des plus simples à gérer : la différence est exactement de 4 heures et ne change jamais, car aucune des deux villes n\'applique l\'heure d\'été.',
'<h2>Aperçu des fuseaux horaires</h2>',
'<h3>Doubaï (GST)</h3>',
'<p>Doubaï suit l\'heure normale du Golfe, UTC+4, toute l\'année. Les Émirats arabes unis n\'appliquent pas l\'heure d\'été.</p>',
'<h3>Londres (GMT/BST)</h3>',
'<p>Londres est GMT (UTC+0) en hiver et BST (UTC+1) en été. Le Royaume-Uni applique l\'heure d\'été.</p>',
'<h2>Différence horaire</h2>',
'<p><strong>Hiver au Royaume-Uni :</strong> Doubaï est à 4 heures devant Londres.</p>',
'<p><strong>Été au Royaume-Uni :</strong> Doubaï est à 3 heures devant Londres (car Londres passe à BST).</p>',
'<p>Note : le décalage propre de Doubaï ne change pas ; la différence ne bouge que par Londres.</p>',
'<h2>Formule de conversion</h2>',
'<p><strong>Heure à Doubaï = Heure à Londres + 4 h (hiver) ou + 3 h (été)</strong></p>',
'<h2>Tableau de conversion rapide (Doubaï GST → Londres)</h2>',
'<table><thead><tr><th>Doubaï</th><th>Londres (GMT, hiver)</th><th>Londres (BST, été)</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>5:00</td><td>6:00</td></tr>'
'<tr><td>12:00</td><td>8:00</td><td>9:00</td></tr>'
'<tr><td>15:00</td><td>11:00</td><td>12:00</td></tr>'
'<tr><td>18:00</td><td>14:00</td><td>15:00</td></tr>'
'<tr><td>21:00</td><td>17:00</td><td>18:00</td></tr>'
'<tr><td>0:00</td><td>20:00</td><td>21:00</td></tr>'
'</tbody></table>',
'<h2>À quoi cela sert</h2>',
'<ul>'
'<li>Finance et commerce entre EAU et Royaume-Uni</li>'
'<li>Planifier des vols via les hubs de Doubaï</li>'
'<li>Équipes à distance réparties entre le Golfe et Londres</li>'
'<li>Transactions immobilières sur les deux marchés</li>'
'</ul>',
'<h2>Questions fréquentes</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>Quelle est la différence horaire entre Doubaï et Londres ?</h3><p>4 heures en hiver au Royaume-Uni, 3 en été. Doubaï ne bouge pas.</p></div>'
'<div class="faq-item"><h3>Doubaï applique-t-il l\'heure d\'été ?</h3><p>Non. Les EAU gardent l\'heure normale du Golfe (UTC+4) toute l\'année.</p></div>'
'<div class="faq-item"><h3>S\'il est 12:00 à Doubaï, quelle heure est-il à Londres ?</h3><p>8:00 GMT en hiver ou 9:00 BST en été.</p></div>'
'<div class="faq-item"><h3>Meilleure fenêtre pour une réunion ?</h3><p>8:00–12:00 Londres = 12:00–16:00 Doubaï (hiver) ou 11:00–15:00 (été).</p></div>'
'<div class="faq-item"><h3>Pourquoi un seul côté bouge-t-il ?</h3><p>Seul le Royaume-Uni applique l\'heure d\'été ; les EAU gardent un décalage fixe.</p></div>'
'</div>',
'<p>Voyez les deux villes en direct avec notre <a href="/">horloge mondiale</a> et planifiez avec le <a href="/meeting-planner.html">planificateur de réunions</a>.</p>'
)

DE_4 = (
'Dubai und London bilden einen beliebten Geschäftskorridor, und einer der einfachsten zu handhaben: Die Differenz beträgt exakt 4 Stunden und ändert sich nie, da keine der beiden Städte die Sommerzeit beachtet.',
'<h2>Überblick über die Zeitzonen</h2>',
'<h3>Dubai (GST)</h3>',
'<p>Dubai folgt der Golf-Standardzeit, UTC+4, das ganze Jahr über. Die VAE wenden keine Sommerzeit an.</p>',
'<h3>London (GMT/BST)</h3>',
'<p>London ist GMT (UTC+0) im Winter und BST (UTC+1) im Sommer. Das Vereinigte Königreich wendet die Sommerzeit an.</p>',
'<h2>Zeitunterschied</h2>',
'<p><strong>Winter im Vereinigten Königreich:</strong> Dubai liegt 4 Stunden vor London.</p>',
'<p><strong>Sommer im Vereinigten Königreich:</strong> Dubai liegt 3 Stunden vor London (da London auf BST umstellt).</p>',
'<p>Hinweis: Dubais eigener Offset ändert sich nicht; die Differenz verschiebt sich nur wegen London.</p>',
'<h2>Umrechnungsformel</h2>',
'<p><strong>Zeit in Dubai = Zeit in London + 4 h (Winter) oder + 3 h (Sommer)</strong></p>',
'<h2>Schnelle Umrechnungstabelle (Dubai GST → London)</h2>',
'<table><thead><tr><th>Dubai</th><th>London (GMT, Winter)</th><th>London (BST, Sommer)</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>5:00</td><td>6:00</td></tr>'
'<tr><td>12:00</td><td>8:00</td><td>9:00</td></tr>'
'<tr><td>15:00</td><td>11:00</td><td>12:00</td></tr>'
'<tr><td>18:00</td><td>14:00</td><td>15:00</td></tr>'
'<tr><td>21:00</td><td>17:00</td><td>18:00</td></tr>'
'<tr><td>0:00</td><td>20:00</td><td>21:00</td></tr>'
'</tbody></table>',
'<h2>Wann es nützlich ist</h2>',
'<ul>'
'<li>Finanzen und Handel zwischen VAE und Vereintem Königreich</li>'
'<li>Flüge über Dubais Drehkreuze planen</li>'
'<li>Remote-Teams zwischen Golf und London</li>'
'<li>Immobilienabschlüsse auf beiden Märkten</li>'
'</ul>',
'<h2>Häufig gestellte Fragen</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>Wie groß ist der Zeitunterschied zwischen Dubai und London?</h3><p>4 Stunden im britischen Winter, 3 im Sommer. Dubai ändert sich nicht.</p></div>'
'<div class="faq-item"><h3>Beachtet Dubai die Sommerzeit?</h3><p>Nein. Die VAE halten die Golf-Standardzeit (UTC+4) das ganze Jahr.</p></div>'
'<div class="faq-item"><h3>Wenn es in Dubai 12:00 ist, wie spät ist es in London?</h3><p>8:00 GMT im Winter oder 9:00 BST im Sommer.</p></div>'
'<div class="faq-item"><h3>Beste Zeitfenster für ein Meeting?</h3><p>8:00–12:00 London = 12:00–16:00 Dubai (Winter) oder 11:00–15:00 (Sommer).</p></div>'
'<div class="faq-item"><h3>Warum verschiebt sich nur eine Seite?</h3><p>Nur das Vereinigte Königreich hat Sommerzeit; die VAE halten einen festen Offset.</p></div>'
'</div>',
'<p>Sehen Sie beide Städte live in unserer <a href="/">Weltuhr</a> und planen Sie mit dem <a href="/meeting-planner.html">Meeting-Planer</a>.</p>'
)

# ----- 5. convert-ist-to-gmt -----
ES_5 = (
'Convertir la hora estándar de la India (IST) a la hora media de Greenwich (GMT) se necesita constantemente para quienes trabajan entre la India y Europa o África. Lo clave que hay que recordar: la India usa un desfase de media hora, UTC+5:30, y nunca cambia. Esa media hora es lo que confunde a la gente.',
'<h2>Resumen de husos horarios</h2>',
'<h3>Hora estándar de la India (IST)</h3>',
'<p>IST es UTC+5:30 todo el año. La India no aplica horario de verano, así que el desfase es fijo.</p>',
'<h3>Hora media de Greenwich (GMT)</h3>',
'<p>GMT es UTC+0 en invierno. El Reino Unido pasa a BST (UTC+1) en verano, por lo que el punto de referencia se mueve.</p>',
'<h2>Diferencia horaria</h2>',
'<p><strong>Invierno en Reino Unido (GMT):</strong> la India va 5 horas 30 minutos por delante de GMT.</p>',
'<p><strong>Verano en Reino Unido (BST):</strong> la India va 4 horas 30 minutos por delante de Londres.</p>',
'<h2>Fórmula de conversión</h2>',
'<p><strong>GMT = IST − 5 h 30 m (invierno) / IST − 4 h 30 m (verano en Reino Unido)</strong></p>',
'<h2>Ejemplos de conversión</h2>',
'<p><strong>Invierno:</strong> 15:00 IST → 9:30 GMT</p>',
'<p><strong>Verano:</strong> 15:00 IST → 10:30 BST</p>',
'<p>Cuidado con la media hora. 10:00 IST son 4:30 GMT, no 5:00.</p>',
'<h2>Tabla rápida de conversión (IST → GMT)</h2>',
'<table><thead><tr><th>India (IST)</th><th>Londres (GMT, invierno)</th><th>Londres (BST, verano)</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>3:30</td><td>4:30</td></tr>'
'<tr><td>12:00</td><td>6:30</td><td>7:30</td></tr>'
'<tr><td>15:00</td><td>9:30</td><td>10:30</td></tr>'
'<tr><td>18:00</td><td>12:30</td><td>13:30</td></tr>'
'<tr><td>21:00</td><td>15:30</td><td>16:30</td></tr>'
'<tr><td>0:00</td><td>18:30</td><td>19:30</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>Conversor de husos horarios</h2>'
'    <div class="converter-row"><label for="from-time">Hora en la India:</label><input type="time" id="from-time" value="15:00"></div>'
'    <div class="converter-row"><label for="dst">Reino Unido:</label>'
'      <select id="dst"><option value="330">GMT (invierno) −5h30m</option><option value="270" selected>BST (verano) −4h30m</option></select></div>'
'    <div class="converter-row"><label for="to-time">Hora en Londres:</label><input type="time" id="to-time" readonly></div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]-parseInt(d.value); while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); d.addEventListener('change', cv); cv();});</script>",
'<h2>Cuándo sirve</h2>',
'<ul>'
'<li>Subcontratación y coordinación de equipos TI entre Reino Unido e India</li>'
'<li>Planificar llamadas entre Londres y Bangalore, Bombay o Delhi</li>'
'<li>Seguir el horario bursátil de la India desde Europa</li>'
'<li>Llamadas familiares y personales entre las regiones</li>'
'</ul>',
'<h2>Preguntas frecuentes</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>¿Cuál es la diferencia horaria entre IST y GMT?</h3><p>5 horas 30 minutos en invierno en Reino Unido, 4 horas 30 minutos en verano.</p></div>'
'<div class="faq-item"><h3>¿Por qué la media hora?</h3><p>La India usa a propósito UTC+5:30 y lo mantiene todo el año.</p></div>'
'<div class="faq-item"><h3>Si en la India son las 15:00, ¿qué hora es en Londres?</h3><p>9:30 GMT en invierno o 10:30 BST en verano.</p></div>'
'<div class="faq-item"><h3>¿La India usa horario de verano?</h3><p>No. IST es UTC+5:30 todo el año.</p></div>'
'<div class="faq-item"><h3>¿Cómo convierto GMT a IST?</h3><p>Suma 5 h 30 m en invierno o 4 h 30 m en verano en Reino Unido.</p></div>'
'</div>',
'<p>Para planificar en una fecha concreta, usa nuestro <a href="/">reloj mundial</a> y el <a href="/meeting-planner.html">planificador de reuniones</a>.</p>'
)

FR_5 = (
'Convertir l\'heure normale de l\'Inde (IST) en heure moyenne de Greenwich (GMT) est nécessaire en permanence pour ceux qui travaillent entre l\'Inde et l\'Europe ou l\'Afrique. Le point clé à retenir : l\'Inde utilise un décalage de trente minutes, UTC+5:30, qui ne change jamais. C\'est cette demi-heure qui perd les gens.</p>',
'<h2>Aperçu des fuseaux horaires</h2>',
'<h3>Heure normale de l\'Inde (IST)</h3>',
'<p>IST est UTC+5:30 toute l\'année. L\'Inde n\'applique pas l\'heure d\'été, le décalage est donc fixe.</p>',
'<h3>Heure moyenne de Greenwich (GMT)</h3>',
'<p>GMT est UTC+0 en hiver. Le Royaume-Uni passe à BST (UTC+1) en été, le point de référence bouge donc.</p>',
'<h2>Différence horaire</h2>',
'<p><strong>Hiver au Royaume-Uni (GMT) :</strong> l\'Inde est à 5 heures 30 minutes devant GMT.</p>',
'<p><strong>Été au Royaume-Uni (BST) :</strong> l\'Inde est à 4 heures 30 minutes devant Londres.</p>',
'<h2>Formule de conversion</h2>',
'<p><strong>GMT = IST − 5 h 30 m (hiver) / IST − 4 h 30 m (été au Royaume-Uni)</strong></p>',
'<h2>Exemples de conversion</h2>',
'<p><strong>Hiver :</strong> 15:00 IST → 9:30 GMT</p>',
'<p><strong>Été :</strong> 15:00 IST → 10:30 BST</p>',
'<p>Attention à la demi-heure. 10:00 IST font 4:30 GMT, pas 5:00.</p>',
'<h2>Tableau de conversion rapide (IST → GMT)</h2>',
'<table><thead><tr><th>Inde (IST)</th><th>Londres (GMT, hiver)</th><th>Londres (BST, été)</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>3:30</td><td>4:30</td></tr>'
'<tr><td>12:00</td><td>6:30</td><td>7:30</td></tr>'
'<tr><td>15:00</td><td>9:30</td><td>10:30</td></tr>'
'<tr><td>18:00</td><td>12:30</td><td>13:30</td></tr>'
'<tr><td>21:00</td><td>15:30</td><td>16:30</td></tr>'
'<tr><td>0:00</td><td>18:30</td><td>19:30</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>Convertisseur de fuseaux horaires</h2>'
'    <div class="converter-row"><label for="from-time">Heure en Inde :</label><input type="time" id="from-time" value="15:00"></div>'
'    <div class="converter-row"><label for="dst">Royaume-Uni :</label>'
'      <select id="dst"><option value="330">GMT (hiver) −5h30m</option><option value="270" selected>BST (été) −4h30m</option></select></div>'
'    <div class="converter-row"><label for="to-time">Heure à Londres :</label><input type="time" id="to-time" readonly></div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]-parseInt(d.value); while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); d.addEventListener('change', cv); cv();});</script>",
'<h2>À quoi cela sert</h2>',
'<ul>'
'<li>Sous-traitance et coordination d\'équipes IT entre Royaume-Uni et Inde</li>'
'<li>Planifier des appels entre Londres et Bangalore, Bombay ou Delhi</li>'
'<li>Suivre les heures de bourse indiennes depuis l\'Europe</li>'
'<li>Appels familiaux et personnels entre les régions</li>'
'</ul>',
'<h2>Questions fréquentes</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>Quelle est la différence horaire entre IST et GMT ?</h3><p>5 heures 30 minutes en hiver au Royaume-Uni, 4 heures 30 minutes en été.</p></div>'
'<div class="faq-item"><h3>Pourquoi la demi-heure ?</h3><p>L\'Inde utilise volontairement UTC+5:30 et le garde toute l\'année.</p></div>'
'<div class="faq-item"><h3>S\'il est 15:00 en Inde, quelle heure est-il à Londres ?</h3><p>9:30 GMT en hiver ou 10:30 BST en été.</p></div>'
'<div class="faq-item"><h3>L\'Inde applique-t-elle l\'heure d\'été ?</h3><p>Non. IST est UTC+5:30 toute l\'année.</p></div>'
'<div class="faq-item"><h3>Comment convertir GMT en IST ?</h3><p>Ajoutez 5 h 30 m en hiver ou 4 h 30 m en été au Royaume-Uni.</p></div>'
'</div>',
'<p>Pour planifier à une date précise, utilisez notre <a href="/">horloge mondiale</a> et le <a href="/meeting-planner.html">planificateur de réunions</a>.</p>'
)

DE_5 = (
'Die Umrechnung von Indischer Standardzeit (IST) in Greenwich Mean Time (GMT) wird ständig von allen gebraucht, die zwischen Indien und Europa oder Afrika arbeiten. Das Wichtigste: Indien verwendet einen Halbstunden-Offset, UTC+5:30, der sich nie ändert. Eben diese halbe Stunde verwirrt die Leute.',
'<h2>Überblick über die Zeitzonen</h2>',
'<h3>Indische Standardzeit (IST)</h3>',
'<p>IST ist UTC+5:30 das ganze Jahr. Indien beobachtet keine Sommerzeit, der Offset ist also fest.</p>',
'<h3>Greenwich Mean Time (GMT)</h3>',
'<p>GMT ist UTC+0 im Winter. Das Vereinigte Königreich stellt im Sommer auf BST (UTC+1) um, der Bezugspunkt verschiebt sich also.</p>',
'<h2>Zeitunterschied</h2>',
'<p><strong>Winter im Vereinigten Königreich (GMT):</strong> Indien liegt 5 Stunden 30 Minuten vor GMT.</p>',
'<p><strong>Sommer im Vereinigten Königreich (BST):</strong> Indien liegt 4 Stunden 30 Minuten vor London.</p>',
'<h2>Umrechnungsformel</h2>',
'<p><strong>GMT = IST − 5 h 30 m (Winter) / IST − 4 h 30 m (Sommer im Vereinigten Königreich)</strong></p>',
'<h2>Umrechnungsbeispiele</h2>',
'<p><strong>Winter:</strong> 15:00 IST → 9:30 GMT</p>',
'<p><strong>Sommer:</strong> 15:00 IST → 10:30 BST</p>',
'<p>Achten Sie auf die halbe Stunde. 10:00 IST sind 4:30 GMT, nicht 5:00.</p>',
'<h2>Schnelle Umrechnungstabelle (IST → GMT)</h2>',
'<table><thead><tr><th>Indien (IST)</th><th>London (GMT, Winter)</th><th>London (BST, Sommer)</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>3:30</td><td>4:30</td></tr>'
'<tr><td>12:00</td><td>6:30</td><td>7:30</td></tr>'
'<tr><td>15:00</td><td>9:30</td><td>10:30</td></tr>'
'<tr><td>18:00</td><td>12:30</td><td>13:30</td></tr>'
'<tr><td>21:00</td><td>15:30</td><td>16:30</td></tr>'
'<tr><td>0:00</td><td>18:30</td><td>19:30</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>Zeitzonen-Umrechner</h2>'
'    <div class="converter-row"><label for="from-time">Zeit in Indien:</label><input type="time" id="from-time" value="15:00"></div>'
'    <div class="converter-row"><label for="dst">Vereinigtes Königreich:</label>'
'      <select id="dst"><option value="330">GMT (Winter) −5h30m</option><option value="270" selected>BST (Sommer) −4h30m</option></select></div>'
'    <div class="converter-row"><label for="to-time">Zeit in London:</label><input type="time" id="to-time" readonly></div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]-parseInt(d.value); while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); d.addEventListener('change', cv); cv();});</script>",
'<h2>Wann es nützlich ist</h2>',
'<ul>'
'<li>Outsourcing und Koordination von IT-Teams zwischen UK und Indien</li>'
'<li>Anrufe zwischen London und Bangalore, Mumbai oder Delhi planen</li>'
'<li>Indische Börsenzeiten aus Europa verfolgen</li>'
'<li>Familien- und Privatgespräche zwischen den Regionen</li>'
'</ul>',
'<h2>Häufig gestellte Fragen</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>Wie groß ist der Zeitunterschied zwischen IST und GMT?</h3><p>5 Stunden 30 Minuten im britischen Winter, 4 Stunden 30 Minuten im Sommer.</p></div>'
'<div class="faq-item"><h3>Warum die halbe Stunde?</h3><p>Indien verwendet bewusst UTC+5:30 und hält das das ganze Jahr.</p></div>'
'<div class="faq-item"><h3>Wenn es in Indien 15:00 ist, wie spät ist es in London?</h3><p>9:30 GMT im Winter oder 10:30 BST im Sommer.</p></div>'
'<div class="faq-item"><h3>Beobachtet Indien die Sommerzeit?</h3><p>Nein. IST ist UTC+5:30 das ganze Jahr.</p></div>'
'<div class="faq-item"><h3>Wie rechne ich GMT in IST um?</h3><p>Addieren Sie 5 h 30 m im Winter oder 4 h 30 m im britischen Sommer.</p></div>'
'</div>',
'<p>Für die Planung an einem bestimmten Datum nutzen Sie unsere <a href="/">Weltuhr</a> und den <a href="/meeting-planner.html">Meeting-Planer</a>.</p>'
)

META = {
 'time-difference-los-angeles-london': {
   'es': ('Diferencia horaria Los Ángeles — Londres: guía y conversor (2026) | World Time Sync',
     'Los Ángeles — Londres: entendiendo el desfase de 7–8 horas',
     'Conoce la diferencia de 7–8 horas entre Los Ángeles y Londres: tablas de conversión, horario de verano y conversor en vivo.',
     'diferencia horaria Los Ángeles Londres, conversión LA Londres, PST a GMT',
     'Diferencia horaria Los Ángeles — Londres', 'Husos horarios, Conversión, Guía'),
   'fr': ('Différence horaire Los Angeles — Londres : guide et convertisseur (2026) | World Time Sync',
     'Los Angeles — Londres : comprendre le décalage de 7–8 heures',
     'Découvrez le décalage de 7–8 heures entre Los Angeles et Londres : tableaux de conversion, heure d\'été et convertisseur en direct.',
     'différence horaire Los Angeles Londres, conversion LA Londres, PST en GMT',
     'Différence horaire Los Angeles — Londres', 'Fuseaux horaires, Conversion, Guide'),
   'de': ('Zeitunterschied Los Angeles — London: Leitfaden und Umrechner (2026) | World Time Sync',
     'Los Angeles — London: den 7–8-Stunden-Unterschied verstehen',
     'Erfahren Sie den 7–8-Stunden-Unterschied zwischen Los Angeles und London: Umrechnungstabellen, Sommerzeit und Live-Umrechner.',
     'Zeitunterschied Los Angeles London, Umrechnung LA London, PST nach GMT',
     'Zeitunterschied Los Angeles — London', 'Zeitzonen, Umrechnung, Leitfaden'),
 },
 'time-difference-new-york-sydney': {
   'es': ('Diferencia horaria Nueva York — Sídney: guía y conversor (2026) | World Time Sync',
     'Nueva York — Sídney: el desfase del Pacífico de 14–16 horas',
     'Comprende la diferencia de 14–16 horas entre Nueva York y Sídney: tablas, horario de verano y consejos de planificación.',
     'diferencia horaria Nueva York Sídney, conversión NY Sídney, EST a AEDT',
     'Diferencia horaria Nueva York — Sídney', 'Husos horarios, Conversión, Guía'),
   'fr': ('Différence horaire New York — Sydney : guide et convertisseur (2026) | World Time Sync',
     'New York — Sydney : le décalage du Pacifique de 14–16 heures',
     'Comprenez la différence de 14–16 heures entre New York et Sydney : tableaux, heure d\'été et conseils de planification.',
     'différence horaire New York Sydney, conversion NY Sydney, EST en AEDT',
     'Différence horaire New York — Sydney', 'Fuseaux horaires, Conversion, Guide'),
   'de': ('Zeitunterschied New York — Sydney: Leitfaden und Umrechner (2026) | World Time Sync',
     'New York — Sydney: die 14–16-Stunden-Pazifiklücke',
     'Verstehen Sie den 14–16-Stunden-Unterschied zwischen New York und Sydney: Tabellen, Sommerzeit und Planungstipps.',
     'Zeitunterschied New York Sydney, Umrechnung NY Sydney, EST nach AEDT',
     'Zeitunterschied New York — Sydney', 'Zeitzonen, Umrechnung, Leitfaden'),
 },
 'convert-cet-to-est': {
   'es': ('Convertir CET a EST: diferencia horaria y guía (2026) | World Time Sync',
     'Convertir CET a EST: el estable desfase transatlántico de 6 horas',
     'Convierte la hora de Europa Central a la del Este de EE. UU. con nuestra guía, tablas y conversor en vivo.',
     'convertir CET a EST, diferencia horaria CET EST, Europa Central a Este',
     'Convertir CET a EST', 'Husos horarios, Conversión, Guía'),
   'fr': ('Convertir CET en EST : différence horaire et guide (2026) | World Time Sync',
     'Convertir CET en EST : le décalage transatlantique stable de 6 heures',
     'Convertissez l\'heure d\'Europe centrale en heure de l\'Est des États-Unis avec notre guide, tableaux et convertisseur en direct.',
     'convertir CET en EST, différence horaire CET EST, Europe centrale à Est',
     'Convertir CET en EST', 'Fuseaux horaires, Conversion, Guide'),
   'de': ('CET in EST umrechnen: Zeitunterschied und Leitfaden (2026) | World Time Sync',
     'CET in EST umrechnen: die stabile 6-Stunden-Transatlantiklücke',
     'Rechnen Sie Mitteleuropäische Zeit in US-Ostzeit um mit unserem Leitfaden, Tabellen und Live-Umrechner.',
     'CET in EST umrechnen, Zeitunterschied CET EST, Mitteleuropa nach Ost',
     'CET in EST umrechnen', 'Zeitzonen, Umrechnung, Leitfaden'),
 },
 'time-difference-dubai-london': {
   'es': ('Diferencia horaria Dubái — Londres: guía y conversor (2026) | World Time Sync',
     'Dubái — Londres: un desfase limpio de 3–4 horas',
     'La diferencia entre Dubái y Londres es de exactas 3–4 horas y no se mueve del lado de Dubái. Tablas, horario de verano y conversor.',
     'diferencia horaria Dubái Londres, conversión Dubái Londres, GST a GMT',
     'Diferencia horaria Dubái — Londres', 'Husos horarios, Conversión, Guía'),
   'fr': ('Différence horaire Doubaï — Londres : guide et convertisseur (2026) | World Time Sync',
     'Doubaï — Londres : un décalage net de 3–4 heures',
     'L\'écart entre Doubaï et Londres est de 3–4 heures nettes et ne bouge pas du côté de Doubaï. Tableaux, heure d\'été et convertisseur.',
     'différence horaire Doubaï Londres, conversion Doubaï Londres, GST en GMT',
     'Différence horaire Doubaï — Londres', 'Fuseaux horaires, Conversion, Guide'),
   'de': ('Zeitunterschied Dubai — London: Leitfaden und Umrechner (2026) | World Time Sync',
     'Dubai — London: eine saubere 3–4-Stunden-Lücke',
     'Der Unterschied zwischen Dubai und London beträgt glatte 3–4 Stunden und verschiebt sich nicht auf Dubais Seite. Tabellen, Sommerzeit und Umrechner.',
     'Zeitunterschied Dubai London, Umrechnung Dubai London, GST nach GMT',
     'Zeitunterschied Dubai — London', 'Zeitzonen, Umrechnung, Leitfaden'),
 },
 'convert-ist-to-gmt': {
   'es': ('Convertir IST a GMT: diferencia horaria y guía (2026) | World Time Sync',
     'Convertir IST a GMT: no olvides la media hora',
     'Convierte la hora estándar de la India a GMT con nuestra guía. La India es UTC+5:30 todo el año, así que cuida la media hora.',
     'convertir IST a GMT, diferencia horaria India GMT, conversión IST GMT',
     'Convertir IST a GMT', 'Husos horarios, Conversión, Guía'),
   'fr': ('Convertir IST en GMT : différence horaire et guide (2026) | World Time Sync',
     'Convertir IST en GMT : ne négligez pas la demi-heure',
     'Convertissez l\'heure normale de l\'Inde en GMT avec notre guide. L\'Inde est UTC+5:30 toute l\'année, donc attention à la demi-heure.',
     'convertir IST en GMT, différence horaire Inde GMT, conversion IST GMT',
     'Convertir IST en GMT', 'Fuseaux horaires, Conversion, Guide'),
   'de': ('IST in GMT umrechnen: Zeitunterschied und Leitfaden (2026) | World Time Sync',
     'IST in GMT umrechnen: die halbe Stunde nicht vergessen',
     'Rechnen Sie Indische Standardzeit in GMT um mit unserem Leitfaden. Indien ist UTC+5:30 das ganze Jahr, beachten Sie die halbe Stunde.',
     'IST in GMT umrechnen, Zeitunterschied Indien GMT, IST GMT Umrechnung',
     'IST in GMT umrechnen', 'Zeitzonen, Umrechnung, Leitfaden'),
 },
}

CONTENT = {
 'time-difference-los-angeles-london': {'es': ES_1, 'fr': FR_1, 'de': DE_1},
 'time-difference-new-york-sydney': {'es': ES_2, 'fr': FR_2, 'de': DE_2},
 'convert-cet-to-est': {'es': ES_3, 'fr': FR_3, 'de': DE_3},
 'time-difference-dubai-london': {'es': ES_4, 'fr': FR_4, 'de': DE_4},
 'convert-ist-to-gmt': {'es': ES_5, 'fr': FR_5, 'de': DE_5},
}

for slug, langs in CONTENT.items():
    for lang in ('es', 'fr', 'de'):
        parts = langs[lang]
        content = ''.join(parts)
        title, h1, desc, kw, bc, tags = META[slug][lang]
        make_i18n_post(slug, lang, lang, title, h1, desc, kw, bc, DATE_DISPLAY[lang], 6, tags, content, [])

print('\nES + FR + DE localized posts generated.')
