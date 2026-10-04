# Содержание приложения «Предлог + -ing».
# В примерах: {…} — предлог (синий), […] — форма на -ing (оранжевый).

MIXED_TOPIC = 10

# Смысл: группа | [предлог, значение, пример ([…] — -ing)]
MEANINGS = [
    {"ru": "несмотря на", "rows": [
        ["despite", "несмотря на", "despite [feeling] ill"],
        ["in spite of", "то же, но с of", "in spite of [feeling] ill"]]},
    {"ru": "вместо и без", "rows": [
        ["instead of", "вместо того чтобы", "instead of [waiting]"],
        ["without", "не делая, не сделав", "without [saying] a word"]]},
    {"ru": "за и против", "rows": [
        ["in favour of", "за, поддерживаю", "in favour of [starting] early"],
        ["against", "против", "against [operating]"]]},
    {"ru": "и ещё", "rows": [
        ["as well as", "а также, наряду с", "as well as [teaching]"],
        ["besides", "помимо, кроме того что", "besides [working] here"]]},
    {"ru": "как, почему, для чего", "rows": [
        ["by", "способ: тем, что", "by [stopping] smoking"],
        ["as a result of", "в результате того, что", "as a result of [smoking]"],
        ["for", "для чего, за что", "thanks for [coming]"],
        ["from", "не давая (prevent from)", "prevent clots from [forming]"]]},
    {"ru": "когда", "rows": [
        ["on", "как только, сразу после", "on [arriving]"]]},
    {"ru": "предложение", "rows": [
        ["how about", "как насчёт", "how about [trying]…?"],
        ["what about", "а что если", "what about [asking]…?"]]},
]

# Ловушки: неверно | верно | почему
ERRORS = [
    ["despite of the rain", "despite the rain", "of — только у in spite of"],
    ["despite he was ill", "although he was ill", "целое предложение — although"],
    ["went there for buying bread", "went there to buy bread", "цель человека — to do"],
    ["without to say", "without saying", "после предлога — -ing"],
    ["How about to go?", "How about going?", "после about — -ing"],
    ["sit besides me", "sit beside me", "рядом — beside, помимо — besides"],
]

TOPICS = [
    {"n": 1, "title": "После предлога — -ing",
     "rule": "Предлог перед глаголом превращает его в -ing: without saying, instead of waiting, before starting, after taking. Не to do и не голая форма. Так со всеми предлогами — и с составными: as a result of, in favour of, in spite of. Если нужно «не», оно встаёт перед -ing: sorry for not calling.",
     "ex": [
         {"en": "Wash your hands {before} [touching] the wound.", "ru": "Мойте руки, прежде чем трогать рану."},
         {"en": "Take the tablets {after} [eating].", "ru": "Принимайте таблетки после еды."},
         {"en": "What's the point {of} [doing] another scan?", "ru": "Какой смысл делать ещё одно КТ?"},
     ]},
    {"n": 2, "title": "despite и in spite of",
     "rule": "despite = in spite of — «несмотря на». После них существительное или -ing: despite the rain, despite feeling ill. of — только у in spite of: despite of — ошибка. Целое предложение с подлежащим после despite не ставят: говорят although he was ill или despite the fact that he was ill.",
     "ex": [
         {"en": "{Despite} [feeling] unwell, she finished her shift.", "ru": "Несмотря на плохое самочувствие, она доработала смену."},
         {"en": "{In spite of} the treatment, his speech didn't improve.", "ru": "Несмотря на лечение, речь у него не восстановилась."},
         {"en": "He came to work {although} he was ill.", "ru": "Он пришёл на работу, хотя был болен."},
     ]},
    {"n": 3, "title": "instead of и without",
     "rule": "instead of — «вместо того чтобы»: instead of waiting. without — «не делая, не сделав»: without asking, without saying a word. Русское деепричастие с «не» — «не посоветовавшись», «не прочитав» — по-английски without + -ing.",
     "ex": [
         {"en": "{Instead of} [waiting] for the MRI, we started treatment.", "ru": "Вместо того чтобы ждать МРТ, мы начали лечение."},
         {"en": "Don't change the dose {without} [asking] your doctor.", "ru": "Не меняйте дозу, не посоветовавшись с врачом."},
         {"en": "He left {without} [saying] goodbye.", "ru": "Он ушёл, не попрощавшись."},
     ]},
    {"n": 4, "title": "in favour of и against",
     "rule": "in favour of — «за», поддерживаю: most doctors are in favour of starting early. against — «против»: the family is against operating. После обоих — существительное или -ing. Сверх уровня: recommend against doing — «не рекомендовать».",
     "ex": [
         {"en": "Most neurologists are {in favour of} [starting] treatment early.", "ru": "Большинство неврологов — за раннее начало лечения."},
         {"en": "The family is {against} [moving] him to a care home.", "ru": "Родственники против того, чтобы переводить его в дом престарелых."},
     ]},
    {"n": 5, "title": "as well as и besides",
     "rule": "as well as — «а также, наряду с»; besides — «помимо, кроме того что». Оба добавляют ещё одно дело, и после них -ing: as well as treating patients, she teaches students. Не путай: beside без s — «рядом»: sit beside me.",
     "ex": [
         {"en": "{As well as} [treating] patients, she teaches students.", "ru": "Помимо лечения пациентов, она учит студентов."},
         {"en": "{Besides} [working] at the hospital, he runs a private clinic.", "ru": "Кроме работы в больнице, у него частная клиника."},
         {"en": "Come and sit {beside} me.", "ru": "Садись рядом со мной."},
     ]},
    {"n": 6, "title": "by и as a result of",
     "rule": "by + -ing — способ: «тем, что; путём»: you can lower your risk by stopping smoking. as a result of — «в результате того, что»: as a result of smoking for 30 years, he developed COPD. Русское деепричастие «бросив курить» часто переводится как by stopping smoking.",
     "ex": [
         {"en": "You can lower your risk {by} [stopping] smoking.", "ru": "Вы можете снизить риск, если бросите курить."},
         {"en": "{As a result of} [smoking] for 30 years, he developed COPD.", "ru": "В результате тридцати лет курения у него развилась ХОБЛ."},
     ]},
    {"n": 7, "title": "for и from",
     "rule": "for + -ing — назначение вещи или причина: a device for measuring blood pressure, thank you for coming, sorry for being late. Но цель человека — «чтобы» — через to: I came to see you, а не for seeing. from + -ing — после prevent, stop, keep: aspirin prevents clots from forming.",
     "ex": [
         {"en": "This device is {for} [measuring] blood pressure.", "ru": "Этот прибор — для измерения давления."},
         {"en": "Thank you {for} [coming] so quickly.", "ru": "Спасибо, что так быстро пришли."},
         {"en": "Aspirin prevents platelets {from} [sticking] together.", "ru": "Аспирин не даёт тромбоцитам склеиваться."},
     ]},
    {"n": 8, "title": "on + -ing: как только",
     "rule": "on + -ing — «как только, сразу после», звучит чуть официально: on arriving at the hospital = as soon as he arrived. В протоколах часто с существительным: on admission, on arrival, on discharge.",
     "ex": [
         {"en": "{On} [arriving] at the hospital, he was taken straight to CT.", "ru": "Сразу по прибытии в больницу его отвезли на КТ."},
         {"en": "{On} [hearing] the news, she burst into tears.", "ru": "Услышав новость, она расплакалась."},
     ]},
    {"n": 9, "title": "how about, what about",
     "rule": "How about…? и What about…? — «Как насчёт…? А что если…?» — предложение. Дальше -ing или существительное: How about taking a break? What about Friday? Не to do: how about to go — ошибка.",
     "ex": [
         {"en": "{How about} [taking] a short break?", "ru": "Как насчёт короткого перерыва?"},
         {"en": "{What about} [asking] the consultant?", "ru": "А что если спросить консультанта?"},
     ]},
    {"n": MIXED_TOPIC, "title": "Итог — всё вместе",
     "rule": "Пятнадцать случайных карточек из всех тем вперемешку.",
     "ex": []},
]

def F(ing, base):
    return [ing, "to " + base, base]

CARDS = [
    # 1 — общее правило: форма после предлога
    {"id": "p-giving", "t": 1, "q": "Always check the patient's ID before ___ any drug.", "opts": F("giving", "give"), "a": "giving",
     "why": "before — предлог: дальше -ing."},
    {"id": "p-eating", "t": 1, "q": "Take these tablets after ___.", "opts": F("eating", "eat"), "a": "eating",
     "why": "after — предлог: after eating."},
    {"id": "p-talking", "t": 1, "q": "Don't stop the tablets without ___ to your doctor.", "opts": F("talking", "talk"), "a": "talking",
     "why": "without + -ing."},
    {"id": "p-taking", "t": 1, "q": "Instead of ___ the tablets, he threw them away.", "opts": F("taking", "take"), "a": "taking",
     "why": "instead of + -ing."},
    {"id": "p-point", "t": 1, "q": "What's the point of ___ another scan?", "opts": F("doing", "do"), "a": "doing",
     "why": "of — предлог: the point of doing."},
    {"id": "p-notcalling", "t": 1, "q": "Sorry for ___ you back yesterday.", "opts": ["not calling", "not to call", "don't call"], "a": "not calling",
     "why": "«не» встаёт перед -ing: for not calling."},

    # 2 — despite, in spite of
    {"id": "d-feeling", "t": 2, "q": "___ feeling unwell, she finished her shift.", "ru": "Несмотря на плохое самочувствие, она доработала смену.",
     "opts": ["Despite", "Instead of", "Without"], "a": "Despite", "why": "«несмотря на» — despite."},
    {"id": "d-of", "t": 2, "q": "In spite ___ the treatment, his speech didn't improve.", "opts": ["of", ""], "a": "of",
     "why": "in spite of — с of."},
    {"id": "d-despiteof", "t": 2, "q": "___ the heavy traffic, the ambulance arrived on time.", "opts": ["Despite", "Despite of"], "a": "Despite",
     "why": "despite — без of."},
    {"id": "d-although", "t": 2, "q": "___ he was ill, he came to work.", "opts": ["Although", "Despite"], "a": "Although",
     "why": "Дальше целое предложение (he was…) — although. После despite — существительное или -ing."},
    {"id": "d-being", "t": 2, "q": "Despite ___ ill, he came to work.", "opts": ["being", "he was", "to be"], "a": "being",
     "why": "despite + -ing: despite being ill."},
    {"id": "d-fact", "t": 2, "q": "Despite the fact ___ he was tired, he stayed late.", "opts": ["that", "of"], "a": "that",
     "why": "despite the fact that + предложение."},

    # 3 — instead of, without
    {"id": "iw-asking", "t": 3, "q": "Don't change the dose ___ asking your doctor.", "ru": "Не меняйте дозу, не посоветовавшись с врачом.",
     "opts": ["without", "instead of", "despite"], "a": "without", "why": "«не посоветовавшись» — without asking."},
    {"id": "iw-waiting", "t": 3, "q": "___ waiting for the MRI, we started treatment.", "ru": "Вместо того чтобы ждать МРТ, мы начали лечение.",
     "opts": ["Instead of", "Without", "Despite"], "a": "Instead of",
     "also": {"Without": "without waiting — «не дожидаясь», смысл чуть другой"},
     "why": "«вместо того чтобы» — instead of."},
    {"id": "iw-reading", "t": 3, "q": "He took the tablets ___ reading the instructions.", "ru": "Он выпил таблетки, не прочитав инструкцию.",
     "opts": ["without", "instead of", "by"], "a": "without", "why": "«не прочитав» — without reading."},
    {"id": "iw-saying", "t": 3, "q": "He left without ___ goodbye.", "opts": F("saying", "say"), "a": "saying",
     "why": "without + -ing."},

    # 4 — in favour of, against
    {"id": "fa-favour", "t": 4, "q": "The committee voted ___ extending the opening hours.", "ru": "Комитет проголосовал за продление часов работы.",
     "opts": ["in favour of", "against", "instead of"], "a": "in favour of", "why": "«за» — in favour of."},
    {"id": "fa-against", "t": 4, "q": "The family is ___ moving him to a care home.", "ru": "Родственники против переезда в дом престарелых.",
     "opts": ["against", "in favour of", "without"], "a": "against", "why": "«против» — against."},
    {"id": "fa-changing", "t": 4, "q": "I'm in favour of ___ the protocol.", "opts": F("changing", "change"), "a": "changing",
     "why": "in favour of + -ing."},
    {"id": "fa-recommend", "t": 4, "q": "The guidelines recommend ___ using this drug in pregnancy.", "ru": "Рекомендации не советуют применять этот препарат при беременности.",
     "opts": ["against", "in favour of", "without"], "a": "against", "why": "recommend against — «не рекомендовать»."},
    {"id": "fa-opening", "t": 4, "q": "Are you for or against ___ the clinic at weekends?", "opts": F("opening", "open"), "a": "opening",
     "why": "against + -ing."},

    # 5 — as well as, besides
    {"id": "ab-aswell", "t": 5, "q": "___ treating patients, Dr Orlova teaches medical students.", "ru": "Помимо лечения пациентов, доктор Орлова учит студентов.",
     "opts": ["As well as", "Instead of", "Despite"], "a": "As well as", "why": "«наряду с, помимо» — as well as."},
    {"id": "ab-besides", "t": 5, "q": "___ working at the hospital, he runs a private clinic.", "ru": "Кроме работы в больнице, у него частная клиника.",
     "opts": ["Besides", "Beside", "Instead of"], "a": "Besides", "why": "besides — помимо; beside — рядом."},
    {"id": "ab-beside", "t": 5, "q": "Come and sit ___ me.", "ru": "Садись рядом со мной.",
     "opts": ["beside", "besides"], "a": "beside", "why": "«рядом» — beside, без s."},
    {"id": "ab-doing", "t": 5, "q": "As well as ___ the ward round, I have three discharge summaries to write.", "opts": F("doing", "do"), "a": "doing",
     "why": "as well as + -ing."},
    {"id": "ab-being", "t": 5, "q": "Besides ___ a good surgeon, he's a great teacher.", "opts": F("being", "be"), "a": "being",
     "why": "besides + -ing."},

    # 6 — by, as a result of
    {"id": "br-bp", "t": 6, "q": "You can lower your stroke risk ___ controlling your blood pressure.", "ru": "Вы можете снизить риск инсульта, контролируя давление.",
     "opts": ["by", "for", "from"], "a": "by", "why": "Способ — by + -ing."},
    {"id": "br-copd", "t": 6, "q": "___ smoking for thirty years, he developed COPD.", "ru": "В результате тридцати лет курения у него развилась ХОБЛ.",
     "opts": ["As a result of", "Instead of", "In favour of"], "a": "As a result of", "why": "«в результате того, что» — as a result of."},
    {"id": "br-taking", "t": 6, "q": "We saved time by ___ the patient straight to CT.", "opts": F("taking", "take"), "a": "taking",
     "why": "by + -ing."},
    {"id": "br-films", "t": 6, "q": "She learned English ___ watching films with subtitles.", "ru": "Она выучила английский, смотря фильмы с субтитрами.",
     "opts": ["by", "for", "with"], "a": "by", "why": "Способ — by + -ing; with — ошибка."},
    {"id": "br-therapy", "t": 6, "q": "His speech improved as a result of ___ therapy every day.", "opts": F("having", "have"), "a": "having",
     "why": "as a result of + -ing."},

    # 7 — for, from
    {"id": "ff-device", "t": 7, "q": "This device is used ___ measuring blood pressure.", "ru": "Этот прибор используют для измерения давления.",
     "opts": ["for", "by", "from"], "a": "for", "why": "Назначение вещи — for + -ing."},
    {"id": "ff-thanks", "t": 7, "q": "Thank you ___ coming so quickly.", "ru": "Спасибо, что так быстро пришли.",
     "opts": ["for", "by", "on"], "a": "for", "why": "thank you for + -ing."},
    {"id": "ff-prevent", "t": 7, "q": "Aspirin prevents platelets ___ sticking together.", "ru": "Аспирин не даёт тромбоцитам склеиваться.",
     "opts": ["from", "for", "against"], "a": "from", "why": "prevent … from + -ing."},
    {"id": "ff-stop", "t": 7, "q": "Nothing could stop him ___ leaving the hospital.", "ru": "Ничто не могло помешать ему уйти из больницы.",
     "opts": ["from", "for", "of"], "a": "from", "why": "stop … from + -ing."},
    {"id": "ff-purpose", "t": 7, "q": "I went to the pharmacy ___ some aspirin.", "opts": ["to buy", "for buying"], "a": "to buy",
     "why": "Цель человека — to do. For buying — ошибка."},
    {"id": "ff-sorry", "t": 7, "q": "Sorry for ___ late.", "opts": F("being", "be"), "a": "being",
     "why": "sorry for + -ing."},

    # 8 — on
    {"id": "on-arriving", "t": 8, "q": "___ arriving at the hospital, he was taken straight to CT.", "ru": "Сразу по прибытии в больницу его отвезли на КТ.",
     "opts": ["On", "By", "For"], "a": "On", "why": "«как только, сразу после» — on + -ing."},
    {"id": "on-hearing", "t": 8, "q": "___ hearing the news, she burst into tears.", "ru": "Услышав новость, она расплакалась.",
     "opts": ["On", "Without", "Despite"], "a": "On", "why": "«как только услышала» — on hearing."},
    {"id": "on-seeing", "t": 8, "q": "On ___ the results, the consultant called the family.", "opts": F("seeing", "see"), "a": "seeing",
     "why": "on + -ing."},
    {"id": "on-admission", "t": 8, "q": "Blood glucose is checked ___ admission.", "ru": "Глюкозу проверяют при поступлении.",
     "opts": ["on", "by", "for"], "a": "on", "why": "on admission — «при поступлении»."},

    # 9 — how about, what about
    {"id": "ha-break", "t": 9, "q": "How about ___ a short break?", "opts": F("taking", "take"), "a": "taking",
     "why": "How about + -ing."},
    {"id": "ha-ask", "t": 9, "q": "What about ___ the consultant?", "opts": F("asking", "ask"), "a": "asking",
     "why": "What about + -ing."},
    {"id": "ha-friday", "t": 9, "q": "We can't meet on Monday. What ___ Friday?", "opts": ["about", "for", "on"], "a": "about",
     "why": "What about + существительное: What about Friday?"},
    {"id": "ha-coffee", "t": 9, "q": "___ a coffee before the ward round?", "ru": "Может, кофе перед обходом?",
     "opts": ["How about", "What for", "Instead of"], "a": "How about", "why": "Предложение — How about…?"},
]
