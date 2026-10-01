# -*- coding: utf-8 -*-
"""IT — Antarctica time zones."""

META = {
    "title": "Fusi orari dell'Antartide: un continente con tutti gli scostamenti UTC",
    "desc": ("L'Antartide non ha un fuso orario ufficiale. Le sue stazioni di ricerca seguono gli "
             "orologi del proprio paese, da UTC+13 a UTC−8. Ecco come funziona."),
    "kw": ("fuso orario antartide, utc antartide, ora stazione di ricerca, "
           "ora polo sud, ora stazione troll, stazione amundsen-scott"),
    "date": "1 ottobre 2026",
    "date_iso": "2026-10-01",
    "read": "7 min di lettura",
    "tags": "Fusi orari, Fatti, Lavoro da remoto",
}

BLOCKS = [
    ("p", "In questo preciso momento è mezzanotte al polo Sud geografico, mezzogiorno nella Terra "
          "della Regina Maud e primo pomeriggio nel mare di Ross. Tutto questo è lo stesso "
          "continente, e quasi la stessa longitud, perché l'Antartide avvolge completamente il polo."),
    ("p", "Sembra impossibile finché non si ricorda che lì non ci sono paesi. L'Antartide non ha "
          "popolazione permanente, né confini, né governo, quindi non c'è nessuno che dichiari "
          "un'ora ufficiale. Quello che esiste al suo posto è un insieme di stazioni di ricerca, "
          "ciascuna gestita da un paese diverso, ciascuna che vive sull'ora del proprio paese. È "
          "la situazione dei fusi orari più strana del pianeta."),

    ("h2", "Perché l'Antartide non ha un fuso orario"),
    ("p", "Il continente è regolato dal Trattato antartico, firmato nel 1959. Il trattato serve a "
          "evitare rivendicazioni territoriali e a tenere il continente aperto alla ricerca "
          "pacifica. Sull'ora dice deliberatamente niente, e non definisce alcun fuso orario "
          "antartico."),
    ("p", "La decisione resta quindi a ogni programma nazionale. La maggior parte delle stazioni "
          "sceglie la soluzione più semplice: l'ora del paese che le gestisce. Una stazione "
          "giapponese va sull'ora giapponese, una australiana su quella australiana, una "
          "britannica su quella britannica. È la regola meno confondibile possibile, perché "
          "ciascuno sa già cosa segna il proprio orologio."),

    ("h2", "Le stazioni tengono l'orologio del loro paese"),
    ("p", "Ecco all'incirca come stanno le grandi stazioni. Considera la tabella come un'istantanea "
          "e non come una verità assoluta, perché gli orari vengono a volte modificati, a volte "
          "con poco preavviso."),
    ("table", (
        ["Stazione", "Gestita da", "Scostamento abituale"],
        [
            ["Mawson", "Australia", "UTC+5"],
            ["Davis", "Australia", "UTC+7"],
            ["Casey", "Australia", "UTC+11"],
            ["Zhongshan, Grande Muraglia", "Cina", "UTC+8"],
            ["Vostok", "Russia", "UTC+6 tutto l'anno"],
            ["Syowa", "Giappone", "UTC+3 tutto l'anno"],
            ["SANAE IV", "Sudafrica", "UTC+2"],
            ["Neumayer III, Zucchelli", "Germania, Italia", "UTC+1"],
            ["Troll", "Norvegia", "UTC+0 in inverno, UTC+2 in estate"],
            ["Palmer", "Stati Uniti", "UTC−4"],
            ["Rothera, Halley VI", "Regno Unito", "UTC−3"],
            ["McMurdo, Scott Base", "Stati Uniti, Nuova Zelanda", "UTC−8 nella pratica"],
            ["Amundsen-Scott (Polo Sud)", "Stati Uniti", "ufficialmente UTC+12, in pratica UTC−8"],
        ])),
    ("p", "In quella tabella l'escursione va da UTC+11 a UTC−8. Sono diciannove ore di "
          "differenza, e ci sono unicamente perché qualcuno porta il carburante e qualcun altro "
          "porta il personale."),

    ("h2", "Le stazioni che rompono la regola"),
    ("h3", "Troll vive di proposito sull'UTC"),
    ("p", "La stazione norvegese Troll si trova a circa 72 gradi di latitudine sud, nelle "
          "interiora della Terra della Regina Maud. Segue l'ora norvegese, cioè UTC+0 in inverno e "
          "UTC+2 in estate, come Oslo. D'estate l'equipaggio semplicemente non indietroggia gli "
          "orologi. Vivere su UTC puro per una parte dell'anno è abbastanza raro da valere la "
          "penalità di saperlo, nel caso scriviate a quella stazione."),

    ("h3", "Vostok e Syowa non cambiano mai l'ora"),
    ("p", "Vostok, gestita dalla Russia, resta su UTC+6 tutto l'anno. Syowa, gestita dal Giappone, "
          "resta su UTC+3. Nessuna delle due cambia. Il motivo è il sole, non la politica. In "
          "pieno inverno antartico il sole non sorge per mesi, quindi un passaggio all'ora legale "
          "sarebbe rumore puro. Uno scostamento fisso è più semplice quando la durata del giorno "
          "oscilla comunque tra luce perenne e buio perenne."),

    ("h3", "McMurdo e il Polo Sud ignorano la propria ora ufficiale"),
    ("p", "È qui che la gente resta sorpresa. Le stazioni McMurdo, Scott Base e Amundsen-Scott al "
          "Polo Sud sono ufficialmente sull'ora neozelandese, cioè UTC+12, o UTC+13 quando la "
          "Nuova Zelanda è in ora legale. In pratica quasi nessuno la usa. Le comunità di McMurdo, "
          "Scott Base e del Polo funzionano sull'ora del Pacifico, UTC−8, perché da lì arrivano "
          "la maggior parte dei voli, del carico e della pianificazione."),
    ("p", "Il caso del Polo Sud è il più stridente. Una stazione ufficialmente su UTC+12, dove "
          "l'ora locale è 20 ore avanti rispetto a Los Angeles, che vive la sua giornata su "
          "UTC−8. Se qualcuno ti dice di essere al Polo Sud e ti dà un'ora del Pacifico, ha "
          "ragione."),

    ("h2", "Cosa succede al Polo Sud stesso"),
    ("p", "I fusi orari si costruiscono sulla longitudine, e la longitudine si misura "
          "allontanandosi da un meridiano verso nord o verso sud. Al Polo Sud questo non ha "
          "senso. Ogni direzione è nord. Ogni direzione è anche sud, se la si guarda dal punto di "
          "vista del Polo Nord. Est e ovest non esistono affatto."),
    ("p", "L'argomento geografico a favore di un fuso orario quindi non si applica. La stazione "
          "sta al polo perché vuole stare al polo, per studiare l'atmosfera e la geofisica, e "
          "prende in prestito l'orologio da un paese a 13 000 chilometri di distanza. È "
          "l'esempio più chiaro che un fuso orario è un accordo tra persone e non una proprietà "
          "del paesaggio."),

    ("h2", "Sei mesi di giorno, sei mesi di notte"),
    ("p", "Ciò che plasma davvero una giornata in Antartide non è lo scostamento, è la luce. Le "
          "stazioni costiere hanno alba e tramonto in estate e pochissima luce in inverno. Gli "
          "equipaggi passano spesso volutamente all'ora legale per una parte della stagione, così "
          "che la giornata di lavoro coincida con la luce continua, e poi tornano indietro quando "
          "il sole inizia a tramontare prima."),
    ("p", "Se stai coordinando con un programma antartico, lo scostamento della tabella è il "
          "problema minore. Conta di più la finestra satellitare. Le stazioni sono in gran parte "
          "fuori dalla dorsale internet, quindi una chiamata o una sessione di dati deve "
          "coincidere con il passaggio di un satellite. Un collegamento radio fissato alle 14:00 "
          "può essere l'unico contatto affidabile della giornata. L'ora conta, ma l'orbita conta "
          "di più."),

    ("h2", "Perché vale la pena saperlo"),
    ("p", "Anche se non metterete mai piede sul ghiaccio, l'Antartide è un buon test delle vostre "
          "idee sui fusi orari. Ne rompe tre in una volta."),
    ("ul", [
        "<strong>Un fuso orario non è legato a un paese.</strong> Il continente non ha un paese, "
        "e ha comunque una dozzina di orologi diversi.",
        "<strong>L'ora ufficiale non è l'ora che si usa.</strong> McMurdo, Scott Base e la "
        "stazione del polo ignorano il proprio fuso ufficiale.",
        "<strong>L'ora legale non è universale.</strong> Metà delle stazioni non cambia mai, e una "
        "sola cambia per qualche mese all'anno.",
    ]),
    ("p", "È anche un buon controllo quando uno strumento di pianificazione restituisce una "
          "risposta strana. Se un convertitore vi dice che tra due luoghi ci sono 20 ore di "
          "differenza, verificate se uno dei due è in Antartide e se sta citando l'ora ufficiale "
          "o quella realmente in uso. Un'occhiata al nostro <a href=\"/\">orologio mondiale</a> vi "
          "dà lo scostamento attuale di qualsiasi città e chiude la maggior parte delle "
          "discussioni più in fretta di un foglio di calcolo."),

    ("h2", "In sintesi"),
    ("p", "L'Antartide è ciò che più si avvicina a un esperimento controllato sul tempo. Nessun "
          "confine terrestre, nessuna autorità statale, nessuna popolazione, e il risultato è un "
          "continente cosparso di orologi presi in prestito da altri continenti."),
    ("p", "La versione pratica è semplice: la tabella qui sopra è un buon punto di partenza, ma per "
          "tutto ciò che conta davvero conviene confermare l'ora locale direttamente con la "
          "stazione invece di fidarsi della denominazione ufficiale. Chi gestisce Amundsen-Scott sa "
          "meglio di qualsiasi database di fusi orari cosa segna il proprio orologio a muro."),
    ("p", "E se state organizzando una chiamata, il nostro <a href=\"/meeting-planner\">pianificatore "
          "di riunioni</a> trova la fascia che vi conviene."),

    ("faq", [
        ("L'Antartide ha un fuso orario?",
         "No. Il Trattato antartico non ne definisce uno, e il continente non ha né governo né "
         "popolazione permanente. Ogni stazione regola il proprio orologio, di solito seguendo "
         "l'ora del paese che la gestisce."),
        ("Quale fuso orario si usa al Polo Sud?",
         "La stazione Amundsen-Scott è ufficialmente sull'ora neozelandese, UTC+12, e UTC+13 "
         "nell'estate neozelandese. Nella pratica la comunità della stazione vive sull'ora del "
         "Pacifico, UTC−8, perché è quella che combacia con i suoi voli e il suo carico."),
        ("Che ore sono alla stazione McMurdo?",
         "McMurdo è ufficialmente sull'ora neozelandese, UTC+12, ma la comunità locale usa "
         "soprattutto l'ora standard del Pacifico, UTC−8, come Los Angeles d'inverno. È una delle "
         "sorprese più frequenti nei dati sui fusi orari antartici."),
        ("Perché alcune stazioni antartiche non passano all'ora legale?",
         "Perché a quelle latitudini il sole si muove pochissimo. Stazioni come Vostok e Syowa "
         "mantengono uno scostamento fisso tutto l'anno: spostare l'orologio di un'ora non cambia "
         "nulla quando la giornata è già fatta di 24 ore di luce o 24 ore di buio."),
        ("Si può fissare una chiamata con una stazione antartica?",
         "In modo affidabile, no, non solo in base all'ora. Le stazioni dipendono dai passaggi "
         "dei satelliti per quasi tutta la comunicazione, quindi le finestre di contatto le "
         "dettono le orbite e non l'orario d'ufficio. Confermate la finestra direttamente con la "
         "stazione."),
    ]),
]
