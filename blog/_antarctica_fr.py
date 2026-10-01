# -*- coding: utf-8 -*-
"""FR — Antarctica time zones."""

META = {
    "title": "Fuseaux horaires de l'Antarctique : un continent, tous les décalages UTC",
    "desc": ("L'Antarctique n'a pas de fuseau horaire officiel. Ses stations de recherche suivent "
             "les horloges de leur pays, de UTC+13 à UTC−8. Voici comment ça marche."),
    "kw": ("fuseau horaire antarctique, utc antarctique, heure station de recherche, "
           "heure pole sud, heure station troll, station amundsen-scott"),
    "date": "1 octobre 2026",
    "date_iso": "2026-10-01",
    "read": "7 min de lecture",
    "tags": "Fuseaux horaires, Faits, Travail à distance",
}

BLOCKS = [
    ("p", "En ce moment même, il est minuit au pôle Sud géographique, midi dans la Terre de "
          "la Reine-Maud et le milieu de l'après-midi dans la mer de Ross. Tout cela est le même "
          "continent, et presque la même longitude, parce que l'Antarctique fait le tour du pôle."),
    ("p", "Cela paraît impossible jusqu'à ce qu'on rappelle qu'il n'y a pas de pays là-bas. "
          "L'Antarctique n'a ni population permanente, ni frontières, ni gouvernement, donc "
          "personne pour décréter une heure officielle. Ce qui existe à la place, c'est un "
          "ensemble de stations de recherche, chacune gérée par un pays différent, chacune "
          "vivant à l'heure de son pays. C'est la situation de fuseaux horaires la plus "
          "étrange de la planète."),

    ("h2", "Pourquoi l'Antarctique n'a pas de fuseau horaire"),
    ("p", "Le continent est régi par le traité sur l'Antarctique, signé en 1959. Ce traité "
          "empêche les revendications territoriales et garde le continent ouvert à la recherche "
          "pacifique. Il ne dit volontairement rien de l'heure, et il ne définit aucun fuseau "
          "horaire antarctique."),
    ("p", "La décision revient donc à chaque programme national. La plupart des stations choisissent "
          "la solution la plus simple : l'heure du pays qui les exploite. Une station japonaise "
          "vit à l'heure japonaise, une station australienne à l'heure australienne, une station "
          "britannique à l'heure britannique. C'est la règle la moins déroutante possible, "
          "puisque chacun sait déjà ce qu'indique sa propre montre."),

    ("h2", "Les stations gardent l'heure de leur pays"),
    ("p", "Voici à peu près ce que donnent les grandes stations. Prenez ce tableau pour un "
          "instantané et non pour une vérité absolue : les horaires sont parfois modifiés, "
          "parfois sans préavis."),
    ("table", (
        ["Station", "Gestionnaire", "Décalage habituel"],
        [
            ["Mawson", "Australie", "UTC+5"],
            ["Davis", "Australie", "UTC+7"],
            ["Casey", "Australie", "UTC+11"],
            ["Zhongshan, Grande Muraille", "Chine", "UTC+8"],
            ["Vostok", "Russie", "UTC+6 toute l'année"],
            ["Syowa", "Japon", "UTC+3 toute l'année"],
            ["SANAE IV", "Afrique du Sud", "UTC+2"],
            ["Neumayer III, Zucchelli", "Allemagne, Italie", "UTC+1"],
            ["Troll", "Norvège", "UTC+0 en hiver, UTC+2 en été"],
            ["Palmer", "États-Unis", "UTC−4"],
            ["Rothera, Halley VI", "Royaume-Uni", "UTC−3"],
            ["McMurdo, Scott Base", "États-Unis, Nouvelle-Zélande", "UTC−8 dans la pratique"],
            ["Amundsen-Scott (pôle Sud)", "États-Unis", "officiellement UTC+12, en pratique UTC−8"],
        ])),
    ("p", "Dans ce tableau, l'amplitude va de UTC+11 à UTC−8. Cela fait dix-neuf heures "
          "d'écart, et cela tient uniquement à qui fournit le carburant et qui amène le personnel."),

    ("h2", "Les stations qui dérogent à la règle"),
    ("h3", "Troll vit volontairement à l'heure UTC"),
    ("p", "La station norvégienne Troll se trouve vers 72 degrés de latitude sud, au cœur de la "
          "Terre de la Reine-Maud. Elle suit l'heure norvégienne, donc UTC+0 en hiver et UTC+2 "
          "en été, comme Oslo. En été, l'équipe ne recule tout simplement pas ses montres. "
          "Vivre en UTC pur une partie de l'année est assez rare pour qu'on le sache, au cas où "
          "vous écririez un jour à cette station."),

    ("h3", "Vostok et Syowa ne changent jamais l'heure"),
    ("p", "Vostok, gérée par la Russie, reste à UTC+6 toute l'année. Syowa, gérée par le Japon, "
          "reste à UTC+3. Aucune des deux ne bascule. La raison est solaire, pas politique. Au "
          "cœur de l'hiver antarctique, le soleil ne se lève pas pendant des mois : un décalage "
          "d'heure d'été n'aurait aucun sens. Un décalage fixe est plus simple quand la durée "
          "du jour bascule déjà entre lumière permanente et nuit permanente."),

    ("h3", "McMurdo et le pôle Sud ignorent leur heure officielle"),
    ("p", "C'est là que ça surprend. La station McMurdo, Scott Base et la station Amundsen-Scott "
          "au pôle Sud sont officiellement à l'heure néo-zélandaise, soit UTC+12, ou UTC+13 quand "
          "la Nouvelle-Zélande est en heure d'été. En pratique, presque personne ne s'en sert. "
          "Les communautés de McMurdo, Scott Base et du pôle vivent à l'heure du Pacifique, "
          "UTC−8, parce que c'est de là que viennent l'essentiel des vols, du fret et de la "
          "planification."),
    ("p", "Le cas du pôle Sud est le plus frappant. Une station officiellement à UTC+12, où "
          "l'heure locale a 20 heures d'avance sur Los Angeles, qui organise sa vie quotidienne "
          "sur UTC−8. Si quelqu'un vous dit être au pôle Sud et vous donne une heure du "
          "Pacifique, il a raison."),

    ("h2", "Ce qui se passe au pôle Sud lui-même"),
    ("p", "Les fuseaux horaires reposent sur la longitude, et la longitude se mesure en "
          "s'éloignant d'un méridien vers le nord ou vers le sud. Au pôle Sud, cela n'a aucun "
          "sens. Toutes les directions mènent au nord. Toutes les directions mènent aussi au "
          "sud, si l'on se place du point de vue du pôle Nord. Il n'y a ni est ni ouest du tout."),
    ("p", "L'argument géographique pour un fuseau horaire ne s'applique donc pas. La station est "
          "au pôle parce qu'elle veut être au pôle, pour l'étude de l'atmosphère et de la "
          "géophysique, et elle emprunte son horloge à un pays situé à 13 000 kilomètres. C'est "
          "l'exemple le plus net qu'un fuseau horaire est un accord entre les gens, pas une "
          "propriété du paysage."),

    ("h2", "Six mois de jour, six mois de nuit"),
    ("p", "Ce qui façonne réellement une journée en Antarctique, ce n'est pas le décalage, c'est "
          "la lumière. Les stations côtières ont lever et coucher de soleil en été, et très peu "
          "de lumière en hiver. Les équipes passent souvent volontairement à l'heure d'été une "
          "partie de la saison, pour que la journée de travail coïncide avec une lumière "
          "continue, puis reviennent à l'heure normale quand le soleil se couche plus tôt."),
    ("p", "Si vous coordonnez avec un programme antarctique, le décalage du tableau est le "
          "moindre de vos soucis. Ce qui compte davantage, c'est la fenêtre satellite. Les "
          "stations sont pour l'essentiel hors du réseau dorsal, donc un appel ou une session "
          "de données doit coïncider avec le passage d'un satellite. Une liaison radio fixée à "
          "14 h peut être le seul contact fiable de la journée. L'heure compte, mais l'orbite "
          "compte davantage."),

    ("h2", "Pourquoi c'est utile à savoir"),
    ("p", "Même si vous ne mettrez jamais les pieds sur la glace, l'Antarctique est un bon test de "
          "vos idées sur les fuseaux horaires. Elle en casse trois d'un coup."),
    ("ul", [
        "<strong>Un fuseau horaire n'est pas lié à un pays.</strong> Le continent n'a pas de pays "
        "du tout, et possède quand même une douzaine d'horloges différentes.",
        "<strong>L'heure officielle n'est pas l'heure utilisée.</strong> McMurdo, Scott Base et "
        "la station du pôle ignorent leur propre fuseau officiel.",
        "<strong>L'heure d'été n'est pas universelle.</strong> La moitié des stations ne changent "
        "jamais, et une seule le fait pendant quelques mois de l'année.",
    ]),
    ("p", "C'est aussi un bon contrôle quand un outil de planification renvoie une réponse "
          "étrange. Si un convertisseur vous dit que deux endroits ont 20 heures d'écart, "
          "vérifiez si l'un des deux est en Antarctique et s'il cite l'heure officielle ou "
          "l'heure réellement en usage. Un coup d'œil à notre <a href=\"/\">horloge mondiale</a> "
          "vous donnera le décalage actuel de n'importe quelle ville et règle la plupart des "
          "débats plus vite qu'un tableur."),

    ("h2", "En résumé"),
    ("p", "L'Antarctique est ce qui se rapproche le plus d'une expérience contrôlée en matière "
          "de temps. Pas de frontières terrestres, pas d'autorité publique, pas de population, "
          "et pour résultat un continent couvert d'horloges empruntées à d'autres continents."),
    ("p", "La version pratique est simple : le tableau ci-dessus est un bon point de départ, mais "
          "pour tout ce qui compte vraiment, confirmez l'heure locale directement auprès de la "
          "station plutôt que de vous fier à l'appellation officielle. Ceux qui dirigent "
          "Amundsen-Scott en savent plus long que n'importe quelle base de fuseaux horaires sur "
          "ce qu'indique leur horloge murale."),
    ("p", "Et si vous planifiez un appel, notre <a href=\"/meeting-planner\">planificateur de "
          "réunions</a> trouve le créneau qui vous convient."),

    ("faq", [
        ("L'Antarctique a-t-il un fuseau horaire ?",
         "Non. Le traité sur l'Antarctique n'en définit aucun, et le continent n'a ni "
         "gouvernement ni population permanente. Chaque station règle sa propre horloge, en "
         "général sur l'heure du pays qui l'exploite."),
        ("Quel fuseau horaire au pôle Sud ?",
         "La station Amundsen-Scott est officiellement à l'heure néo-zélandaise, UTC+12, et "
         "UTC+13 pendant l'été néo-zélandais. En pratique, la communauté de la station vit à "
         "l'heure du Pacifique, UTC−8, parce que c'est celle qui colle à ses vols et à son fret."),
        ("Quelle heure est-il à la station McMurdo ?",
         "McMurdo est officiellement à l'heure néo-zélandaise, UTC+12, mais la communauté locale "
         "utilise surtout l'heure standard du Pacifique, UTC−8, comme Los Angeles en hiver. "
         "C'est l'une des surprises les plus fréquentes dans les données de fuseaux horaires "
         "antarctiques."),
        ("Pourquoi certaines stations antarctiques ne passent-elles pas en heure d'été ?",
         "Parce que le soleil bouge très peu à ces latitudes. Des stations comme Vostok et Syowa "
         "gardent un décalage fixe toute l'année : décaler d'une heure ne changerait rien quand "
         "la journée compte déjà 24 heures de lumière ou 24 heures d'obscurité."),
        ("Peut-on planifier un appel avec une station antarctique ?",
         "Pas de façon fiable sur la seule base de l'heure. Les stations dépendent des passages "
         "de satellites pour l'essentiel de leurs communications : les fenêtres de contact sont "
         "dictées par les orbites, pas par les horaires de bureau. Confirmez la fenêtre "
         "directement avec la station."),
    ]),
]
