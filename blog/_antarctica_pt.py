# -*- coding: utf-8 -*-
"""PT — Antarctica time zones."""

META = {
    "title": "Fusos horários da Antártida: um continente com todos os deslocamentos UTC",
    "desc": ("A Antártida não tem fuso horário oficial. Suas estações de pesquisa seguem os "
             "relógios do próprio país, de UTC+13 a UTC−8. É assim que funciona na prática."),
    "kw": ("fuso horário antártida, utc antártida, hora estação de pesquisa, "
           "hora polo sul, hora estação troll, estação amundsen-scott"),
    "date": "1 de outubro de 2026",
    "date_iso": "2026-10-01",
    "read": "7 min de leitura",
    "tags": "Fusos horários, Fatos, Trabalho remoto",
}

BLOCKS = [
    ("p", "Neste exato momento é meia-noite no polo Sul geográfico, meio-dia na Terra da Rainha "
          "Maud e metade da tarde no mar de Ross. Tudo isso é o mesmo continente, e quase a mesma "
          "longitude, porque a Antártida envolve o polo por completo."),
    ("p", "Parece impossível até lembrar que lá não existem países. A Antártida não tem "
          "população permanente, nem fronteiras, nem governo, então não há ninguém para declarar "
          "uma hora oficial. O que existe no lugar disso é um conjunto de estações de pesquisa, "
          "cada uma administrada por um país diferente, cada uma vivendo na hora desse país. É a "
          "situação de fusos horários mais estranha do planeta."),

    ("h2", "Por que a Antártida não tem fuso horário"),
    ("p", "O continente é regido pelo Tratado Antártico, assinado em 1959. O tratado existe para "
          "impedir reivindicações territoriais e manter o continente aberto à pesquisa pacífica. "
          "Sobre o horário ele deliberadamente não diz nada, e não define nenhum fuso horário "
          "antártico."),
    ("p", "Assim, a decisão fica com cada programa nacional. A maioria das estações escolhe a "
          "solução mais simples: a hora do país que a mantém. Uma estação japonesa vive na hora "
          "japonesa, uma australiana na australiana, uma britânica na britânica. É a regra menos "
          "confusa possível, porque cada um já sabe o que marca o próprio relógio."),

    ("h2", "As estações mantêm o relógio do seu país"),
    ("p", "É mais ou menos assim nas grandes estações. Considere a tabela como uma fotografia de "
          "momento, não como verdade absoluta, porque os horários às vezes mudam, e às vezes com "
          "pouco aviso."),
    ("table", (
        ["Estação", "Administração", "Deslocamento habitual"],
        [
            ["Mawson", "Austrália", "UTC+5"],
            ["Davis", "Austrália", "UTC+7"],
            ["Casey", "Austrália", "UTC+11"],
            ["Zhongshan, Grande Muralha", "China", "UTC+8"],
            ["Vostok", "Rússia", "UTC+6 o ano todo"],
            ["Syowa", "Japão", "UTC+3 o ano todo"],
            ["SANAE IV", "África do Sul", "UTC+2"],
            ["Neumayer III, Zucchelli", "Alemanha, Itália", "UTC+1"],
            ["Troll", "Noruega", "UTC+0 no inverno, UTC+2 no verão"],
            ["Palmer", "Estados Unidos", "UTC−4"],
            ["Rothera, Halley VI", "Reino Unido", "UTC−3"],
            ["McMurdo, Scott Base", "Estados Unidos, Nova Zelândia", "UTC−8 na prática"],
            ["Amundsen-Scott (polo Sul)", "Estados Unidos", "oficialmente UTC+12, na prática UTC−8"],
        ])),
    ("p", "Nessa tabela a faixa vai de UTC+11 a UTC−8. São dezenove horas de diferença, e existem "
          "apenas porque alguém traz o combustível e alguém traz o pessoal."),

    ("h2", "As estações que quebram a regra"),
    ("h3", "Troll vive de propósito em UTC"),
    ("p", "A estação norueguesa Troll fica a cerca de 72 graus de latitude sul, no interior da "
          "Terra da Rainha Maud. Segue o horário norueguês, ou seja UTC+0 no inverno e UTC+2 no "
          "verão, como Oslo. No verão a equipe simplesmente não atrasa os relógios. Viver em UTC "
          "puro parte do ano é incomum o bastante para vale a pena saber, caso você escreva para "
          "essa estação um dia."),

    ("h3", "Vostok e Syowa nunca mudam o horário"),
    ("p", "Vostok, administrada pela Rússia, fica em UTC+6 o ano inteiro. Syowa, administrada pelo "
          "Japão, fica em UTC+3. Nenhuma das duas muda. O motivo é o sol, não a política. No fundo "
          "do inverno antártico o sol não nasce por meses, então uma mudança de horário de verão "
          "seria puro ruído. Um deslocamento fixo é mais simples quando a duração do dia já "
          "oscila entre luz eterna e escuridão eterna."),

    ("h3", "McMurdo e o polo Sul ignoram a própria hora oficial"),
    ("p", "É aqui que as pessoas se surpreendem. As estações McMurdo, Scott Base e Amundsen-Scott no "
          "polo Sul estão oficialmente na hora neozelandesa, UTC+12, ou UTC+13 quando a Nova "
          "Zelândia está no horário de verão. Na prática quase ninguém a usa. As comunidades de "
          "McMurdo, Scott Base e do polo funcionam na hora do Pacífico, UTC−8, porque é de lá que "
          "vêm a maioria dos voos, das cargas e do planejamento."),
    ("p", "O caso do polo Sul é o mais chamativo. Uma estação oficialmente em UTC+12, onde a hora "
          "local está 20 horas à frente de Los Angeles, vivendo o dia a dia em UTC−8. Se alguém "
          "disser que está no polo Sul e te passar um horário do Pacífico, está certo."),

    ("h2", "O que acontece no próprio polo Sul"),
    ("p", "Fusos horários são construídos sobre a longitude, e a longitude se mede afastando-se de "
          "um meridiano para o norte ou para o sul. No polo Sul isso não faz sentido. Todas as "
          "direções são norte. Todas as direções também são sul, se você olhar do ponto de vista "
          "do polo Norte. Leste e oeste simplesmente não existem ali."),
    ("p", "Então o argumento geográfico a favor de um fuso não se aplica. A estação está no polo "
          "porque quer estar no polo, para estudar a atmosfera e a geofísica, e toma emprestado o "
          "relógio de um país a 13 000 quilômetros de distância. É o exemplo mais claro de que fuso "
          "horário é um acordo entre pessoas, e não uma propriedade da paisagem."),

    ("h2", "Seis meses de dia, seis meses de noite"),
    ("p", "O que realmente molda um dia na Antártida não é o deslocamento, é a luz. As estações "
          "costeiras têm nascer e pôr do sol no verão e pouca luz no inverno. As tripulações "
          "passam com frequência de propósito para o horário de verão durante parte da estação, "
          "para que o expediente coincida com a luz contínua, e depois voltam ao horário normal "
          "quando o sol começa a se pôr mais cedo."),
    ("p", "Se você está coordenando com um programa antártico, o deslocamento da tabela é o menor "
          "dos seus problemas. Mais importante é a janela do satélite. As estações estão em boa "
          "parte fora da espinha dorsal da internet, então uma chamada ou uma sessão de dados "
          "precisa coincidir com a passagem de um satélite. Um contato de rádio marcado para as "
          "14h pode ser o único contato confiável do dia. A hora importa, mas a órbita importa "
          "mais."),

    ("h2", "Por que vale a pena saber"),
    ("p", "Mesmo que você nunca pise no gelo, a Antártida é um bom teste das suas ideias sobre "
          "fusos horários. Ela quebra três de uma vez."),
    ("ul", [
        "<strong>Um fuso horário não está preso a um país.</strong> O continente não tem país "
        "nenhum e ainda assim tem uma dúzia de relógios diferentes.",
        "<strong>A hora oficial não é a hora usada.</strong> McMurdo, Scott Base e a estação do "
        "polo ignoram o próprio fuso oficial.",
        "<strong>Horas de verão não é universal.</strong> Metade das estações nunca muda, e uma só "
        "muda por alguns meses do ano.",
    ]),
    ("p", "Também serve de conferência quando uma ferramenta de agendamento devolve uma resposta "
          "estranha. Se um conversor disser que entre dois lugares há 20 horas de diferença, "
          "confira se um deles está na Antártida e se ele está citando a hora oficial ou a hora "
          "realmente em uso. Uma olhada no nosso <a href=\"/\">relógio mundial</a> mostra o "
          "deslocamento atual de qualquer cidade e resolve a maioria das discussões mais rápido "
          "que uma planilha."),

    ("h2", "Para resumir"),
    ("p", "A Antártida é o que mais se aproxima de um experimento controlado em matéria de tempo. "
          "Sem fronteiras terrestres, sem autoridade estatal, sem população, e o resultado é um "
          "continente coberto de relógios emprestados de outros continentes."),
    ("p", "A versão prática é simples: a tabela acima é um bom ponto de partida, mas para tudo o "
          "que realmente importa vale confirmar a hora local direto com a estação em vez de "
          "confiar no nome oficial. Quem administra Amundsen-Scott sabe melhor do que qualquer "
          "base de dados de fusos horários o que marca o relógio de parede."),
    ("p", "E se você está marcando uma chamada, nosso <a href=\"/meeting-planner\">planejador de "
          "reuniões</a> encontra a janela que funciona para vocês."),

    ("faq", [
        ("A Antártida tem fuso horário?",
         "Não. O Tratado Antártico não define nenhum, e o continente não tem governo nem população "
         "permanente. Cada estação ajusta o próprio relógio, normalmente seguindo o país que a "
         "administra."),
        ("Qual fuso horário vale no polo Sul?",
         "A estação Amundsen-Scott está oficialmente na hora neozelandesa, UTC+12, e UTC+13 no "
         "verão neozelandês. Na prática, a comunidade da estação vive na hora do Pacífico, UTC−8, "
         "porque é ela que combina com os voos e as cargas de que depende."),
        ("Que horas são na estação McMurdo?",
         "McMurdo está oficialmente na hora neozelandesa, UTC+12, mas a comunidade local usa "
         "sobretudo o horário padrão do Pacífico, UTC−8, igual a Los Angeles no inverno. É uma das "
         "surpresas mais comuns nos dados de fusos horários antárticos."),
        ("Por que algumas estações antárticas não passam para o horário de verão?",
         "Porque o sol quase não se move nessas latitudes. Estações como Vostok e Syowa mantêm um "
         "deslocamento fixo o ano inteiro: adiantar uma hora não muda nada quando o dia já é "
         "feito de 24 horas de luz ou 24 horas de escuridão."),
        ("Dá para marcar uma chamada com uma estação antártica?",
         "Com segurança, não só pelo relógio. As estações dependem das passagens dos satélites para "
         "quase toda a comunicação, então as janelas de contato são ditadas pelas órbitas e não "
         "pelo expediente. Confirme a janela diretamente com a estação."),
    ]),
]
