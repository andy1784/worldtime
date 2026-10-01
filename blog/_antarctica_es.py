# -*- coding: utf-8 -*-
"""ES — Antarctica time zones."""

META = {
    "title": "Husos horarios de la Antártida: un continente con todos los desfases UTC",
    "desc": ("La Antártida no tiene huso horario oficial. Sus estaciones de investigación siguen "
             "los relojes de su país, de UTC+13 a UTC−8. Así funciona en la práctica."),
    "kw": ("huso horario antártida, utc antártida, hora estación de investigación, "
           "hora polo sur, hora estación troll, estación amundsen-scott"),
    "date": "1 de octubre de 2026",
    "date_iso": "2026-10-01",
    "read": "7 min de lectura",
    "tags": "Husos horarios, Datos, Trabajo remoto",
}

BLOCKS = [
    ("p", "En este mismo instante es medianoche en el polo Sur geográfico, mediodía en la Tierra "
          "de la Reina Maud y media tarde en el mar de Ross. Todo eso es el mismo continente, y "
          "casi la misma longitud, porque la Antártida rodea el polo por completo."),
    ("p", "Parece imposible hasta que te acuerdas de que allí no hay países. La Antártida no "
          "tiene población permanente, ni fronteras, ni gobierno, así que no hay nadie que "
          "decrete una hora oficial. Lo que existe en su lugar es un conjunto de estaciones de "
          "investigación, cada una a cargo de un país distinto, cada una viviendo a la hora de "
          "ese país. Es la situación de husos horarios más extraña del planeta."),

    ("h2", "Por qué la Antártida no tiene huso horario"),
    ("p", "El continente se rige por el Tratado Antártico, firmado en 1959. El tratado existe "
          "para evitar reclamaciones territoriales y para dejar el continente abierto a la "
          "investigación pacífica. Sobre el tiempo no dice absolutamente nada, y no define "
          "ningún huso horario antártico."),
    ("p", "Así que la decisión queda en manos de cada programa nacional. La mayoría de las "
          "estaciones elige lo más sencillo: la hora del país que la explota. Una estación "
          "japonesa va con la hora japonesa, una australiana con la australiana, una británica "
          "con la británica. Es la regla menos confusa posible, porque todos ya saben qué "
          "marca su propio reloj."),

    ("h2", "Las estaciones conservan el reloj de su país"),
    ("p", "Así queda más o menos la cosa en las estaciones grandes. Toma la tabla como una "
          "instantánea y no como una verdad absoluta, porque los horarios se modifican a veces, "
          "y a veces con poco aviso."),
    ("table", (
        ["Estación", "Gestionada por", "Desfase habitual"],
        [
            ["Mawson", "Australia", "UTC+5"],
            ["Davis", "Australia", "UTC+7"],
            ["Casey", "Australia", "UTC+11"],
            ["Zhongshan, Gran Muralla", "China", "UTC+8"],
            ["Vostok", "Rusia", "UTC+6 todo el año"],
            ["Syowa", "Japón", "UTC+3 todo el año"],
            ["SANAE IV", "Sudáfrica", "UTC+2"],
            ["Neumayer III, Zucchelli", "Alemania, Italia", "UTC+1"],
            ["Troll", "Noruega", "UTC+0 en invierno, UTC+2 en verano"],
            ["Palmer", "Estados Unidos", "UTC−4"],
            ["Rothera, Halley VI", "Reino Unido", "UTC−3"],
            ["McMurdo, Scott Base", "Estados Unidos, Nueva Zelanda", "UTC−8 en la práctica"],
            ["Amundsen-Scott (polo Sur)", "Estados Unidos", "oficialmente UTC+12, en la práctica UTC−8"],
        ])),
    ("p", "En esa tabla el rango va de UTC+11 a UTC−8. Son diecinueve horas de diferencia, y "
          "existen únicamente por quién lleva el combustible y quién trae al personal."),

    ("h2", "Las estaciones que rompen la norma"),
    ("h3", "Troll vive a propósito en UTC"),
    ("p", "La estación noruega Troll está a unos 72 grados de latitud sur, en el interior de la "
          "Tierra de la Reina Maud. Sigue la hora noruega, es decir UTC+0 en invierno y UTC+2 en "
          "verano, como Oslo. En verano el equipo simplemente no atrasa los relojes. Vivir en UTC "
          "puro parte del año es bastante raro como para saberlo, por si alguna vez escribes a esa "
          "estación."),

    ("h3", "Vostok y Syowa no cambian la hora nunca"),
    ("p", "Vostok, a cargo de Rusia, se queda en UTC+6 todo el año. Syowa, a cargo de Japón, se "
          "queda en UTC+3. Ninguna de las dos cambia. La razón es el sol, no la política. En "
          "pleno invierno antártico el sol no sale durante meses, así que un cambio de hora de "
          "verano sería puro ruido. Un desfase fijo resulta más sencillo cuando la duración del "
          "día ya oscila entre luz eterna y oscuridad eterna."),

    ("h3", "McMurdo y el polo Sur ignoran su hora oficial"),
    ("p", "Aquí es donde se sorprende la gente. La estación McMurdo, Scott Base y la estación "
          "Amundsen-Scott del polo Sur están oficialmente en hora neozelandesa, UTC+12, o UTC+13 "
          "cuando Nueva Zelanda está en horario de verano. En la práctica, casi nadie la usa. Las "
          "comunidades de McMurdo, Scott Base y el polo funcionan con la hora del Pacífico, "
          "UTC−8, porque de ahí vienen la mayoría de los vuelos, la carga y la planificación."),
    ("p", "El caso del polo Sur es el más llamativo. Una estación oficialmente en UTC+12, donde la "
          "hora local va 20 horas por delante de Los Ángeles, viviendo su día a día en UTC−8. Si "
          "alguien te dice que está en el polo Sur y te da una hora del Pacífico, tiene razón."),

    ("h2", "Qué ocurre en el propio polo Sur"),
    ("p", "Los husos horarios se construyen sobre la longitud, y la longitud se mide alejándose "
          "de un meridiano hacia el norte o hacia el sur. En el polo Sur eso no significa nada. "
          "Todas las direcciones son norte. Todas las direcciones son también sur, si lo miras "
          "desde el polo Norte. De este y oeste no hay absolutamente nada."),
    ("p", "Así que el argumento geográfico a favor de un huso horario no se aplica. La estación "
          "está en el polo porque quiere estar en el polo, para estudiar la atmósfera y la "
          "geofísica, y toma prestado el reloj de un país situado a 13 000 kilómetros. Es el "
          "ejemplo más claro de que un huso horario es un acuerdo entre personas y no una "
          "propiedad del paisaje."),

    ("h2", "Seis meses de día, seis meses de noche"),
    ("p", "Lo que de verdad marca un día en la Antártida no es el desfase, es la luz. Las "
          "estaciones costeras tienen amanecer y atardecer en verano, y muy poca luz en invierno. "
          "Las tripulaciones suelen pasar voluntariamente al horario de verano una parte de la "
          "temporada, para que la jornada de trabajo coincida con la luz continua, y luego "
          "regresan al horario normal cuando el sol empieza a ponerse antes."),
    ("p", "Si estás coordinando con un programa antártico, el desfase de la tabla es lo menos "
          "importante. Cuenta más la ventana satelital. Las estaciones están, en su mayor parte, "
          "fuera de la red troncal, así que una llamada o una sesión de datos tiene que coincidir "
          "con el paso de un satélite. Un enlace de radio fijado a las 14:00 puede ser el único "
          "contacto fiable del día. La hora importa, pero la órbita importa más."),

    ("h2", "Por qué conviene saberlo"),
    ("p", "Aunque nunca pises el hielo, la Antártida es un buen examen de tus ideas sobre los "
          "husos horarios. Rompe tres de golpe."),
    ("ul", [
        "<strong>Un huso horario no está atado a un país.</strong> El continente no tiene "
        "ningún país y aun así tiene una docena de relojes distintos.",
        "<strong>La hora oficial no es la hora que se usa.</strong> McMurdo, Scott Base y la "
        "estación del polo ignoran su propio huso oficial.",
        "<strong>El horario de verano no es universal.</strong> La mitad de las estaciones "
        "nunca cambian, y una sola lo hace unos meses al año.",
    ]),
    ("p", "También sirve de comprobación cuando una herramienta de citas devuelve algo raro. Si "
          "un conversor te dice que entre dos sitios hay 20 horas de diferencia, comprueba si "
          "uno de ellos está en la Antártida y si cita la hora oficial o la hora realmente en "
          "uso. Una mirada a nuestro <a href=\"/\">reloj mundial</a> te da el desfase actual "
          "de cualquier ciudad y zanja la mayoría de las discusiones más rápido que una hoja de "
          "cálculo."),

    ("h2", "En resumen"),
    ("p", "La Antártida es lo más parecido a un experimento controlado en materia de tiempo que "
          "hay en el planeta. Sin fronteras terrestres, sin autoridad estatal, sin población, y "
          "el resultado es un continente sembrado de relojes prestados por otros continentes."),
    ("p", "La versión práctica es sencilla: la tabla de arriba es un buen punto de partida, pero "
          "para todo lo que de verdad importa conviene confirmar la hora local directamente con "
          "la estación en lugar de fiarse de la denominación oficial. Quienes dirigen "
          "Amundsen-Scott saben mejor que cualquier base de datos de husos horarios qué marca su "
          "reloj de pared."),
    ("p", "Y si estás organizando una llamada, nuestro <a href=\"/meeting-planner\">planificador "
          "de reuniones</a> encuentra la franja que os viene bien."),

    ("faq", [
        ("¿Tiene huso horario la Antártida?",
         "No. El Tratado Antártico no define ninguno, y el continente no tiene gobierno ni "
         "población permanente. Cada estación pone su propio reloj, normalmente siguiendo la "
         "hora del país que la gestiona."),
        ("¿Qué huso horario se usa en el polo Sur?",
         "La estación Amundsen-Scott está oficialmente en hora neozelandesa, UTC+12, y UTC+13 en "
         "el verano neozelandés. En la práctica, la comunidad de la estación vive con la hora "
         "del Pacífico, UTC−8, porque es la que encaja con sus vuelos y su carga."),
        ("¿Qué hora es en la estación McMurdo?",
         "McMurdo está oficialmente en hora neozelandesa, UTC+12, pero la comunidad local usa "
         "sobre todo la hora estándar del Pacífico, UTC−8, igual que Los Ángeles en invierno. Es "
         "una de las sorpresas más habituales en los datos de husos horarios antárticos."),
        ("¿Por qué algunas estaciones antárticas no cambian al horario de verano?",
         "Porque el sol se mueve muy poco a esas latitudes. Estaciones como Vostok y Syowa "
         "mantienen un desfase fijo todo el año: adelantar una hora no cambia nada cuando el día "
         "ya consiste en 24 horas de luz o 24 horas de oscuridad."),
        ("¿Se puede concertar una llamada con una estación antártica?",
         "De forma fiable, no solo con la hora. Las estaciones dependen de los pasos de satélite "
         "para casi toda su comunicación, así que las ventanas de contacto las marcan las órbitas "
         "y no el horario de oficina. Confirma la ventana directamente con la estación."),
    ]),
]
