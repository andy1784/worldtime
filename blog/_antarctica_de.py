# -*- coding: utf-8 -*-
"""DE — Antarctica time zones."""

META = {
    "title": "Zeitzonen der Antarktis: Ein Kontinent mit jedem UTC-Versatz",
    "desc": ("Die Antarktis hat keine offizielle Zeitzone. Ihre Forschungsstationen rechnen mit "
             "den Uhren ihrer jeweiligen Länder, von UTC+13 bis UTC−8. So läuft das."),
    "kw": ("zeitzone antarktis, utc antarktis, uhrzeit forschungsstation, "
           "zeit am südpol, uhrzeit troll station, amundsen-scott südpolstation"),
    "date": "1. Oktober 2026",
    "date_iso": "2026-10-01",
    "read": "7 Min. Lesezeit",
    "tags": "Zeitzonen, Fakten, Remote Work",
}

BLOCKS = [
    ("p", "Irgendwo gerade ist es Mitternacht am geografischen Südpol, Mittag im Königin-Maud-Land "
          "und Nachmittag im Rossmeer. Alles derselbe Kontinent, und alles ungefähr dieselbe "
          "Länge, weil die Antarktis den Pol vollständig umschließt."),
    ("p", "Das klingt unmöglich, bis man sich erinnert, dass es dort keine Länder gibt. Die "
          "Antarktis hat keine Bevölkerung, keine Grenzen und keine Regierung, also gibt es "
          "niemanden, der eine Amtszeit festlegen könnte. Was es stattdessen gibt, ist eine "
          "Ansammlung von Forschungsstationen, jede von einem anderen Land betrieben, jede mit "
          "ihrer eigenen Uhr. Das ist die ungewöhnlichste Zeitzonen-Situation auf der Erde."),

    ("h2", "Warum die Antarktis keine Zeitzone hat"),
    ("p", "Der Kontinent wird durch den Antarktisvertrag geregelt, unterzeichnet 1959. Der "
          "Vertrag soll Gebietsansprüche verhindern und den Kontinent für friedliche Forschung "
          "offenhalten. Über die Zeit sagt er bewusst nichts, und eine einzige antarktische "
          "Zeitzone führt er nicht ein."),
    ("p", "Damit entscheidet jedes nationale Programm selbst. Die meisten Stationen nehmen die "
          "einfachste Lösung: die Zeit des Landes, das die Station betreibt. Eine japanische "
          "Station rechnet japanisch, eine australische australisch, eine britische britisch. "
          "Das ist die am wenigsten verwirrende Regel, die es gibt, denn jeder weiß ohnehin, "
          "was seine eigene Uhr anzeigt."),

    ("h2", "Die Stationen behalten die Uhr ihres Landes"),
    ("p", "So sieht es bei den großen Stationen ungefähr aus. Betrachten Sie die Tabelle lieber "
          "als Momentaufnahme und nicht als Evangelium, denn die Zeitpläne werden manchmal "
          "geändert, teils mit kurzer Vorwarnung."),
    ("table", (
        ["Station", "Betreiber", "Üblicher Versatz"],
        [
            ["Mawson", "Australien", "UTC+5"],
            ["Davis", "Australien", "UTC+7"],
            ["Casey", "Australien", "UTC+11"],
            ["Zhongshan, Große Mauer", "China", "UTC+8"],
            ["Wostok", "Russland", "UTC+6 ganzjährig"],
            ["Syowa", "Japan", "UTC+3 ganzjährig"],
            ["SANAE IV", "Südafrika", "UTC+2"],
            ["Neumayer III, Zucchelli", "Deutschland, Italien", "UTC+1"],
            ["Troll", "Norwegen", "UTC+0 im Winter, UTC+2 im Sommer"],
            ["Palmer Station", "USA", "UTC−4"],
            ["Rothera, Halley VI", "Großbritannien", "UTC−3"],
            ["McMurdo, Scott Base", "USA, Neuseeland", "in der Praxis UTC−8"],
            ["Amundsen-Scott (Südpol)", "USA", "offiziell UTC+12, praktisch UTC−8"],
        ])),
    ("p", "In der Tabelle reicht die Spanne von UTC+11 bis UTC−8. Das sind neunzehn Stunden "
          "Unterschied, und es gibt sie einzig und allein deshalb, weil derjenige das Treibstoff "
          "liefert und derjenige das Personal hinbringt."),

    ("h2", "Die Stationen, die dem Muster widersprechen"),
    ("h3", "Troll läuft absichtlich auf UTC"),
    ("p", "Die norwegische Troll-Station liegt bei rund 72 Grad südlicher Breite, tief im "
          "Königin-Maud-Land. Sie folgt der norwegischen Zeit, also UTC+0 im Winter und UTC+2 im "
          "Sommer, wie Oslo. Im Sommer stellen die crews die Uhr einfach nicht zurück. Ein halbes "
          "Jahr auf reinem UTC zu leben ist ungewöhnlich genug, um es zu wissen, falls man "
          "dieser Station jemals eine Mail schreibt."),

    ("h3", "Wostok und Syowa stellen gar nicht um"),
    ("p", "Wostok unter russischer Leitung bleibt das ganze Jahr über auf UTC+6. Syowa unter "
          "japanischer Leitung bleibt auf UTC+3. Keine von beiden stellt um. Der Grund ist "
          "Sonnenlicht, nicht Politik. Im tiefen antarktischen Winter geht die Sonne monatelang "
          "nicht auf, eine Sommerzeitumstellung wäre also reines Rauschen. Ein fester Versatz "
          "ist einfacher, wenn die Tageslänge ohnehin zwischen Dauerlicht und Dunkelheit "
          "pendelt."),

    ("h3", "McMurdo und der Südpol ignorieren ihre eigene Amtszeit"),
    ("p", "Hier wird es für die meisten überraschend. McMurdo Station, Scott Base und die "
          "Amundsen-Scott-Station am Südpol stehen offiziell auf neuseeländischer Zeit, also "
          "UTC+12, im neuseeländischen Sommer UTC+13. In der Praxis benutzt das fast niemand. "
          "Die Gemeinschaften in McMurdo, Scott Base und am Pol rechnen mit Pazifischer Zeit, "
          "UTC−8, weil die meisten Flüge, die Fracht und die Planung von dort kommen."),
    ("p", "Der Fall am Südpol ist der auffälligste. Eine Station offiziell auf UTC+12, wo die "
          "Ortszeit 20 Stunden vor Los Angeles liegt, lebt ihren Alltag auf UTC−8. Wer Ihnen "
          "sagt, er sei am Südpol und nennt eine pazifische Zeit, hat recht."),

    ("h2", "Was am Südpol selbst passiert"),
    ("p", "Zeitzonen beruhen auf der Länge, und Länge misst man, indem man sich auf einem "
          "Meridian nach Norden oder Süden entfernt. Am Südpol ist das bedeutungslos. Jede "
          "Richtung ist Norden. Jede Richtung ist zugleich Süden, wenn man vom Nordpol aus "
          "schaut. Ost und West gibt es dort überhaupt nicht."),
    ("p", "Das geografische Argument für eine Zeitzone greift also nicht. Die Station steht am "
          "Pol, weil sie am Pol stehen will, für Atmosphären- und Geophysikforschung, und sie "
          "leiht sich ihre Uhr von einem Land 13.000 Kilometer entfernt. Das ist das deutlichste "
          "Beispiel dafür, dass eine Zeitzone eine Vereinbarung zwischen Menschen ist und keine "
          "Eigenschaft der Landschaft."),

    ("h2", "Sechs Monate Tag, sechs Monate Nacht"),
    ("p", "Was den Tag in der Antarktis tatsächlich formt, ist nicht der Versatz, sondern das "
          "Licht. Stationen an der Küste haben im Sommer Sonnenaufgang und -untergang, im Winter "
          "kaum Licht. Die crews stellen sich im Saisonverlauf oft bewusst eine Weile auf "
          "Sommerzeit, damit der Arbeitstag mit dem durchgehenden Tageslicht zusammenfällt, und "
          "stellen zurück, wenn die Sonne früher untergeht."),
    ("p", "Wenn Sie mit einem Antarktis-Programm koordinieren, ist der Versatz aus der Tabelle "
          "der kleinere Punkt. Wichtiger ist das Satellitenfenster. Die Stationen hängen "
          "größtenteils am normalen Internet, nicht an einem Backbone, deshalb muss ein "
          "Anruf oder eine Datensitzung in das Fenster fallen, in dem ein Satellit übersteht. "
          "Eine Funkverbindung um 14:00 Uhr kann der einzige verlässliche Kontakt des ganzen "
          "Tages sein. Die Uhr zählt, aber die Umlaufbahn zählt mehr."),

    ("h2", "Warum das Wissenswert ist"),
    ("p", "Selbst wenn Sie nie auf dem Eis stehen werden, ist die Antarktis ein guter Test für "
          "Ihre Annahmen über Zeitzonen. Sie bricht drei davon auf einmal."),
    ("ul", [
        "<strong>Eine Zeitzone hängt nicht an einem Land.</strong> Der Kontinent hat gar kein "
        "Land und trotzdem ein Dutzend verschiedener Uhren.",
        "<strong>Amtszeit ist nicht die Zeit, die Menschen benutzen.</strong> McMurdo, Scott Base "
        "und die Polstation ignorieren ihre eigene offizielle Zone.",
        "<strong>Sommerzeit ist nicht universal.</strong> Die Hälfte der Stationen stellt nie um, "
        "und eine stellt ein paar Monate im Jahr um.",
    ]),
    ("p", "Das ist auch eine gute Probe, wenn ein Planungstool eine seltsame Antwort liefert. "
          "Wenn ein Umrechner sagt, zwischen zwei Orten lägen 20 Stunden, prüfen Sie, ob eines "
          "davon in der Antarktis liegt und ob er die Amtszeit oder die tatsächlich benutzte "
          "Zeit nennt. Ein Blick auf unsere <a href=\"/\">Weltzeituhr</a> zeigt den aktuellen "
          "Versatz für jeden Ort und schlichtet die meisten Streitigkeiten schneller als jede "
          "Tabelle."),

    ("h2", "Fazit"),
    ("p", "Die Antarktis ist das, was einem kontrollierten Experiment in Sachen Zeit am nächsten "
          "kommt. Keine Landgrenzen, keine Staatsgewalt, keine Bevölkerung, und das Ergebnis ist "
          "ein Kontinent, übersät mit Uhren, die anderswo ausgeliehen wurden."),
    ("p", "Die praktische Fassung ist einfach: Die Tabelle oben ist ein guter Ausgangspunkt, "
          "aber für alles, was wirklich zählt, sollten Sie die Ortszeit direkt auf der Station "
          "bestätigen, statt sich auf die offizielle Bezeichnung zu verlassen. Wer Amundsen-Scott "
          "führt, weiß besser als jede Zeitzonendatenbank, was seine Wanduhr anzeigt."),
    ("p", "Und wenn Sie ein Gespräch planen, findet unser <a href=\"/meeting-planner\">Meeting-"
          "Planner</a> das passende Zeitfenster für Sie."),

    ("faq", [
        ("Hat die Antarktis eine Zeitzone?",
         "Nein. Der Antarktisvertrag führt keine ein, und der Kontinent hat weder Regierung noch "
         "ständige Bevölkerung. Jede Forschungsstation stellt ihre eigene Uhr, meist nach dem "
         "Land, das sie betreibt."),
        ("Welche Zeitzone gilt am Südpol?",
         "Die Amundsen-Scott-Station steht offiziell auf neuseeländischer Zeit, UTC+12, im "
         "neuseeländischen Sommer auf UTC+13. In der Praxis rechnet die Gemeinschaft der Station "
         "mit Pazifischer Zeit, UTC−8, weil dazu ihre Flüge und Frachten passen."),
        ("Wie spät ist es auf der McMurdo-Station?",
         "McMurdo steht offiziell auf neuseeländischer Zeit, UTC+12, aber die örtliche Gemeinschaft "
         "nutzt überwiegend Pazifische Standardzeit, UTC−8, wie Los Angeles im Winter. Es ist "
         "eine der häufigsten Überraschungen in antarktischen Zeitzonendaten."),
        ("Warum stellen manche antarktischen Stationen nicht auf Sommerzeit um?",
         "Weil sich die Sonne in diesen Breitengraden kaum bewegt. Stationen wie Wostok und Syowa "
         "behalten ganzjährig einen festen Versatz, denn eine Umstellung auf eine Stunde bringt "
         "wenig, wenn der Tag ohnehin aus 24 Stunden Licht oder 24 Stunden Dunkelheit besteht."),
        ("Kann man ein Gespräch mit einer antarktischen Station planen?",
         "Nicht zuverlässig allein nach Uhrzeit. Stationen hängen für die meiste Kommunikation "
         "an Satellitenpassagen, die Kontaktfenster richten sich also nach Umlaufbahn und nicht "
         "nach Bürozeiten. Bestätigen Sie das Fenster direkt mit der Station."),
    ]),
]
