# Содержание приложения «Пары слов»: 40 пар, которые путают.
# Пометка […] — слово в фокусе (оранжевый).

MIXED_TOPIC = 10

GROUPS = {
    "look": "Похожи на вид и на слух",
    "mean": "Похожи по смыслу",
    "mix": "Итог",
}

def w(word, ipa, ru): return [word, ipa, ru]

# Пары по темам: два слова (слово, транскрипция, перевод), подсказка, текст для озвучки
PAIRS = [
    # 1 · самые частые ловушки
    {"t": 1, "w": [w("accept", "/əkˈsept/", "принимать"), w("except", "/ɪkˈsept/", "кроме")],
     "tip": "except — «исключая», как exclude: оба на ex-.", "say": "Accept. Except."},
    {"t": 1, "w": [w("affect", "/əˈfekt/", "влиять (глагол)"), w("effect", "/ɪˈfekt/", "эффект, действие (сущ.)")],
     "tip": "Affect — Action, глагол. Effect — End result, существительное.", "say": "To affect. An effect."},
    {"t": 1, "w": [w("lose", "/luːz/", "терять; худеть — lose weight"), w("loose", "/luːs/", "свободный, болтается")],
     "tip": "lose потерял одну o. В loose два o — много места, свободно.", "say": "Lose. Loose."},
    {"t": 1, "w": [w("quite", "/kwaɪt/", "довольно, вполне"), w("quiet", "/ˈkwaɪət/", "тихий")],
     "tip": "quiet — два слога: qui-et, тихо. quite — один слог.", "say": "Quite. Quiet."},
    # 2 · еда и кухня
    {"t": 2, "w": [w("desert", "/ˈdezət/", "пустыня"), w("dessert", "/dɪˈzɜːt/", "десерт")],
     "tip": "В dessert две s: сладкого всегда хочется ещё.", "say": "A desert. A dessert."},
    {"t": 2, "w": [w("dairy", "/ˈdeəri/", "молочный; молочные продукты"), w("diary", "/ˈdaɪəri/", "дневник, ежедневник")],
     "tip": "diary — три слога: di-a-ry. dairy — два: dair-y.", "say": "Dairy. Diary."},
    {"t": 2, "w": [w("cousin", "/ˈkʌzn/", "двоюродный брат, сестра"), w("cuisine", "/kwɪˈziːn/", "кухня (еда)")],
     "tip": "cuisine — кухня как еда: Italian cuisine. Кухня-комната — kitchen.", "say": "Cousin. Cuisine."},
    {"t": 2, "w": [w("chief", "/tʃiːf/", "главный, начальник"), w("chef", "/ʃef/", "шеф-повар")],
     "tip": "chef — французское слово, ch читается [ʃ], как в «шеф».", "say": "Chief. Chef."},
    {"t": 2, "w": [w("cook", "/kʊk/", "повар; готовить"), w("cooker", "/ˈkʊkə/", "плита")],
     "tip": "Ложный друг: cooker — не повар, а плита. Повар — cook.", "say": "A cook. A cooker."},
    {"t": 2, "w": [w("current", "/ˈkʌrənt/", "текущий; ток, течение"), w("currant", "/ˈkʌrənt/", "смородина")],
     "tip": "Звучат одинаково. current — с e, как electric current (ток).", "say": "Current. Currant."},
    # 3 · на работе
    {"t": 3, "w": [w("principal", "/ˈprɪnsəpl/", "главный; директор школы"), w("principle", "/ˈprɪnsəpl/", "принцип")],
     "tip": "Звучат одинаково. principle — как rule, оба на -le.", "say": "Principal. Principle."},
    {"t": 3, "w": [w("stationary", "/ˈsteɪʃənri/", "неподвижный"), w("stationery", "/ˈsteɪʃənri/", "канцтовары")],
     "tip": "Звучат одинаково. stationAry — stAy, стоит. stationEry — Envelopes, бумага.", "say": "Stationary. Stationery."},
    {"t": 3, "w": [w("personal", "/ˈpɜːsənl/", "личный"), w("personnel", "/ˌpɜːsəˈnel/", "персонал")],
     "tip": "personnel — ударение в конце, как в «персонал».", "say": "Personal. Personnel."},
    {"t": 3, "w": [w("staff", "/stɑːf/", "сотрудники, персонал"), w("stuff", "/stʌf/", "вещи, штуки (разг.)")],
     "tip": "staff — люди на работе. stuff — вещи, «всякое».", "say": "Staff. Stuff."},
    # 4 · одна буква — другое слово
    {"t": 4, "w": [w("envelope", "/ˈenvələʊp/", "конверт"), w("envelop", "/ɪnˈveləp/", "окутывать")],
     "tip": "envelope — конверт, ударение в начале. envelop — глагол, ударение на -vel-.", "say": "An envelope. To envelop."},
    {"t": 4, "w": [w("device", "/dɪˈvaɪs/", "прибор, устройство"), w("devise", "/dɪˈvaɪz/", "придумать, разработать")],
     "tip": "c — существительное, s [z] — глагол. Так же advice — advise.", "say": "A device. To devise."},
    {"t": 4, "w": [w("suit", "/suːt/", "костюм; подходить"), w("suite", "/swiːt/", "номер-люкс")],
     "tip": "suite звучит как sweet — сладкая жизнь в люксе.", "say": "A suit. A suite."},
    {"t": 4, "w": [w("fair", "/feə/", "честный; ярмарка"), w("fare", "/feə/", "плата за проезд")],
     "tip": "Звучат одинаково. fare — как «фара»: всё про транспорт.", "say": "Fair. Fare."},
    {"t": 4, "w": [w("price", "/praɪs/", "цена"), w("prize", "/praɪz/", "приз")],
     "tip": "priCe — Цена, priZe — приЗ.", "say": "Price. Prize."},
    {"t": 4, "w": [w("career", "/kəˈrɪə/", "карьера"), w("carrier", "/ˈkæriə/", "носитель, перевозчик")],
     "tip": "carrier — от carry, «нести»: носитель вируса, авиаперевозчик.", "say": "Career. Carrier."},
    # 5 · маленькие, но коварные
    {"t": 5, "w": [w("beside", "/bɪˈsaɪd/", "рядом с"), w("besides", "/bɪˈsaɪdz/", "кроме того, помимо")],
     "tip": "beside — рядом (side — бок). besides — с s: «плюс ещё».", "say": "Beside. Besides."},
    {"t": 5, "w": [w("loudly", "/ˈlaʊdli/", "громко"), w("aloud", "/əˈlaʊd/", "вслух")],
     "tip": "loudly — громко, а не тихо. aloud — вслух, а не про себя.", "say": "Loudly. Aloud."},
    {"t": 5, "w": [w("alternately", "/ɔːlˈtɜːnətli/", "поочерёдно"), w("alternatively", "/ɔːlˈtɜːnətɪvli/", "или же, как вариант")],
     "tip": "alternately — то одно, то другое. alternatively — вместо этого.", "say": "Alternately. Alternatively."},
    {"t": 5, "w": [w("arise", "/əˈraɪz/", "возникать"), w("rise", "/raɪz/", "подниматься, расти")],
     "tip": "arise — проблемы, вопросы. rise — температура, цены, солнце.", "say": "Arise. Rise."},
    {"t": 5, "w": [w("conscious", "/ˈkɒnʃəs/", "в сознании; осознающий"), w("conscience", "/ˈkɒnʃəns/", "совесть")],
     "tip": "conscious — на -ous, прилагательное. conscience — на -ence, как science.", "say": "Conscious. Conscience."},
    # 6 · качество и шансы
    {"t": 6, "w": [w("effective", "/ɪˈfektɪv/", "действенный, даёт результат"), w("efficient", "/ɪˈfɪʃnt/", "продуктивный, экономный")],
     "tip": "effective — работает. efficient — работает без лишних затрат времени и сил.", "say": "Effective. Efficient."},
    {"t": 6, "w": [w("sensible", "/ˈsensəbl/", "разумный"), w("sensitive", "/ˈsensətɪv/", "чувствительный")],
     "tip": "Ложный друг: sensible — «разумный», со здравым смыслом (sense).", "say": "Sensible. Sensitive."},
    {"t": 6, "w": [w("opportunity", "/ˌɒpəˈtjuːnəti/", "шанс, удачная возможность"), w("possibility", "/ˌpɒsəˈbɪləti/", "возможность, вероятность")],
     "tip": "opportunity — шанс что-то сделать. possibility — то, что может случиться.", "say": "Opportunity. Possibility."},
    {"t": 6, "w": [w("grateful", "/ˈɡreɪtfl/", "благодарен (кому-то)"), w("thankful", "/ˈθæŋkfl/", "рад, что обошлось")],
     "tip": "grateful — кому-то за помощь: I'd be grateful if… thankful — облегчение.", "say": "Grateful. Thankful."},
    # 7 · люди и поступки
    {"t": 7, "w": [w("deny", "/dɪˈnaɪ/", "отрицать"), w("refuse", "/rɪˈfjuːz/", "отказываться")],
     "tip": "deny — «это неправда»: deny doing. refuse — «не буду»: refuse to do.", "say": "To deny. To refuse."},
    {"t": 7, "w": [w("agree", "/əˈɡriː/", "соглашаться"), w("accept", "/əkˈsept/", "принимать (предложение)")],
     "tip": "agree — с мнением: agree with you. accept — то, что дают: accept an offer.", "say": "To agree. To accept."},
    {"t": 7, "w": [w("ashamed", "/əˈʃeɪmd/", "стыдно"), w("embarrassed", "/ɪmˈbærəst/", "неловко, смущён")],
     "tip": "ashamed — стыдно за плохой поступок. embarrassed — неловкая ситуация.", "say": "Ashamed. Embarrassed."},
    {"t": 7, "w": [w("foreigner", "/ˈfɒrənə/", "иностранец"), w("stranger", "/ˈstreɪndʒə/", "незнакомец")],
     "tip": "stranger — незнакомый, даже сосед. Вместо foreigner вежливее — people from abroad.", "say": "Foreigner. Stranger."},
    # 8 · вокруг нас
    {"t": 8, "w": [w("tall", "/tɔːl/", "высокий: рост"), w("high", "/haɪ/", "высокий: над землёй, уровень")],
     "tip": "tall — люди, деревья, башни. high — горы, потолки, давление, цены.", "say": "Tall. High."},
    {"t": 8, "w": [w("city", "/ˈsɪti/", "большой город"), w("town", "/taʊn/", "небольшой город, городок")],
     "tip": "city — большой город. town — городок.", "say": "City. Town."},
    {"t": 8, "w": [w("close", "/kləʊz/", "закрывать"), w("shut", "/ʃʌt/", "закрывать (плотно)")],
     "tip": "Дверь, глаза — и так, и так. Только close: счёт, совещание. shut down — выключить.", "say": "To close. To shut."},
    {"t": 8, "w": [w("shade", "/ʃeɪd/", "тень: прохладное место"), w("shadow", "/ˈʃædəʊ/", "тень: силуэт")],
     "tip": "Сидят in the shade. Предмет отбрасывает a shadow. На рентгене — тоже shadow.", "say": "Shade. Shadow."},
    # 9 · боль, слух, политика
    {"t": 9, "w": [w("pain", "/peɪn/", "боль"), w("ache", "/eɪk/", "ноющая боль; ныть")],
     "tip": "pain — любая боль, особенно острая: chest pain. ache — ноет: headache, My back aches.", "say": "Pain. Ache."},
    {"t": 9, "w": [w("hear", "/hɪə/", "слышать"), w("listen", "/ˈlɪsn/", "слушать")],
     "tip": "hear — само, как see. listen to — стараешься, как look at.", "say": "Hear. Listen."},
    {"t": 9, "w": [w("politics", "/ˈpɒlətɪks/", "политика: власть, партии"), w("policy", "/ˈpɒləsi/", "правила, курс организации")],
     "tip": "politics — выборы, партии. policy — правила: hospital policy.", "say": "Politics. Policy."},
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["I'm agree with you.", "I agree with you.", "agree — глагол, без am"],
    ["Don't loose your keys.", "Don't lose your keys.", "терять — lose"],
    ["Stress effects sleep.", "Stress affects sleep.", "влиять — affect"],
    ["My skin is very sensible.", "My skin is very sensitive.", "чувствительный — sensitive"],
    ["The patient is conscience.", "The patient is conscious.", "в сознании — conscious"],
    ["She's a good cooker.", "She's a good cook.", "повар — cook; cooker — плита"],
    ["What's for desert?", "What's for dessert?", "десерт — две s"],
    ["His pressure is very tall.", "His pressure is very high.", "уровень — high"],
    ["Please be quite.", "Please be quiet.", "тихий — quiet"],
    ["I can't listen you.", "I can't hear you.", "слышать — hear"],
]

TOPICS = [
    {"n": 1, "group": "look", "title": "Самые частые ловушки", "sub": "accept · affect · lose · quite",
     "rule": "accept — принимать, except — кроме. affect — влиять (глагол), effect — эффект (существительное): Stress affects sleep. It has a strong effect. lose — терять, loose — свободный. quite — довольно, quiet — тихий.",
     "ex": [
         {"en": "Please [accept] my apologies.", "ru": "Пожалуйста, примите мои извинения."},
         {"en": "Stress can [affect] your sleep.", "ru": "Стресс может влиять на сон."},
         {"en": "Please be [quiet].", "ru": "Тише, пожалуйста."},
     ]},
    {"n": 2, "group": "look", "title": "Еда и кухня", "sub": "dessert · dairy · cuisine · chef · cooker · currant",
     "rule": "dessert — десерт, desert — пустыня. dairy — молочный, diary — дневник. cuisine — кухня как еда, cousin — двоюродный брат. chef — шеф-повар, chief — главный. cook — повар, cooker — плита. current — текущий, currant — смородина.",
     "ex": [
         {"en": "What's for [dessert]?", "ru": "Что на десерт?"},
         {"en": "Keep a headache [diary].", "ru": "Ведите дневник головной боли."},
         {"en": "Turn off the [cooker].", "ru": "Выключи плиту."},
     ]},
    {"n": 3, "group": "look", "title": "На работе", "sub": "principal · stationery · personnel · staff",
     "rule": "principal — главный; директор школы, principle — принцип. stationary — неподвижный, stationery — канцтовары. personal — личный, personnel — персонал. staff — сотрудники, stuff — вещи.",
     "ex": [
         {"en": "It's against my [principles].", "ru": "Это против моих принципов."},
         {"en": "Medical [personnel] only.", "ru": "Только для медицинского персонала."},
         {"en": "All [staff] must wear badges.", "ru": "Все сотрудники должны носить бейджи."},
     ]},
    {"n": 4, "group": "look", "title": "Одна буква — другое слово", "sub": "envelope · device · suite · fare · prize · carrier",
     "rule": "envelope — конверт, envelop — окутывать. device — прибор, devise — придумать. suit — костюм; подходить, suite — номер-люкс. fair — честный, fare — плата за проезд. price — цена, prize — приз. career — карьера, carrier — носитель.",
     "ex": [
         {"en": "Put it in an [envelope].", "ru": "Положи это в конверт."},
         {"en": "Does Friday [suit] you?", "ru": "Вам подходит пятница?"},
         {"en": "He's a [carrier] of the virus.", "ru": "Он носитель вируса."},
     ]},
    {"n": 5, "group": "look", "title": "Маленькие, но коварные", "sub": "besides · aloud · alternatively · arise · conscious",
     "rule": "beside — рядом с, besides — кроме того. loudly — громко, aloud — вслух. alternately — поочерёдно, alternatively — или же. arise — возникать (проблемы), rise — подниматься (температура, цены). conscious — в сознании, conscience — совесть.",
     "ex": [
         {"en": "Sit [beside] me.", "ru": "Сядь рядом со мной."},
         {"en": "Call me if problems [arise].", "ru": "Звоните, если возникнут проблемы."},
         {"en": "The patient is [conscious].", "ru": "Пациент в сознании."},
     ]},
    {"n": 6, "group": "mean", "title": "Качество и шансы", "sub": "effective · sensible · opportunity · grateful",
     "rule": "effective — даёт результат, efficient — без лишних затрат. sensible — разумный, sensitive — чувствительный. opportunity — шанс что-то сделать, possibility — то, что может случиться. grateful — благодарен кому-то, thankful — рад, что обошлось.",
     "ex": [
         {"en": "The drug is very [effective].", "ru": "Препарат очень эффективен."},
         {"en": "That's a [sensible] idea.", "ru": "Это разумная мысль."},
         {"en": "I'd be [grateful] for your help.", "ru": "Буду благодарен за помощь."},
     ]},
    {"n": 7, "group": "mean", "title": "Люди и поступки", "sub": "deny · agree · ashamed · stranger",
     "rule": "deny — отрицать: deny doing. refuse — отказаться: refuse to do. agree — соглашаться с мнением: agree with you. accept — принять предложение: accept an offer. ashamed — стыдно, embarrassed — неловко. foreigner — иностранец, stranger — незнакомец.",
     "ex": [
         {"en": "He [refused] to take the tablets.", "ru": "Он отказался пить таблетки."},
         {"en": "I [agree] with you.", "ru": "Я с вами согласен."},
         {"en": "I felt so [embarrassed].", "ru": "Мне было так неловко."},
     ]},
    {"n": 8, "group": "mean", "title": "Вокруг нас", "sub": "tall · town · shut · shadow",
     "rule": "tall — рост: a tall man, a tall tree. high — над землёй и уровни: a high mountain, high blood pressure. city — большой город, town — городок. close и shut — закрыть дверь или глаза; только close — счёт, совещание; shut down — выключить. shade — тень-прохлада, shadow — тень-силуэт.",
     "ex": [
         {"en": "His temperature is [high].", "ru": "У него высокая температура."},
         {"en": "Let's sit in the [shade].", "ru": "Давай сядем в тени."},
         {"en": "[Shut] down the computer.", "ru": "Выключи компьютер."},
     ]},
    {"n": 9, "group": "mean", "title": "Боль, слух, политика", "sub": "ache · listen · policy",
     "rule": "pain — боль, особенно острая: chest pain. ache — ноющая боль: headache; и глагол: My back aches. hear — слышать, listen to — слушать. politics — власть, партии, выборы; policy — правила: hospital policy.",
     "ex": [
         {"en": "Where is the [pain]?", "ru": "Где болит?"},
         {"en": "I can't [hear] you.", "ru": "Я вас не слышу."},
         {"en": "It's hospital [policy].", "ru": "Таковы правила больницы."},
     ]},
    {"n": 10, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · самые частые ловушки
    c("ae-accept", 1, "Please ___ my apologies.", "Пожалуйста, примите мои извинения.", ["accept", "except"], "accept", "Принимать — accept."),
    c("ae-except", 1, "Everyone came ___ Dr Petrov.", "Пришли все, кроме доктора Петрова.", ["except", "accept"], "except", "Кроме — except."),
    c("af-affect", 1, "Stress can ___ your blood pressure.", "Стресс может влиять на давление.", ["affect", "effect"], "affect", "Влиять (глагол) — affect."),
    c("af-effect", 1, "The main side ___ of this drug is headache.", "Главный побочный эффект этого препарата — головная боль.", ["effect", "affect"], "effect",
      "Эффект (существительное) — effect: a side effect."),
    c("lo-lose", 1, "I want to ___ five kilos before summer.", "Хочу похудеть на пять килограммов к лету.", ["lose", "loose"], "lose", "Терять, сбросить вес — lose [luːz]."),
    c("lo-loose", 1, "These trousers are too ___ — I need a smaller size.", "Эти брюки слишком свободные — мне нужен размер поменьше.", ["loose", "lose"], "loose",
      "Свободный — loose [luːs]."),
    c("qu-quiet", 1, "Please be ___ — the patient is asleep.", "Тише, пожалуйста, — пациент спит.", ["quiet", "quite"], "quiet", "Тихий — quiet, два слога: qui-et."),
    c("qu-quite", 1, "The results are ___ good.", "Результаты довольно хорошие.", ["quite", "quiet"], "quite", "Довольно, вполне — quite, один слог."),

    # 2 · еда и кухня
    c("de-dessert", 2, "What would you like for ___? — Ice cream, please.", "Что хотите на десерт? — Мороженое, пожалуйста.", ["dessert", "desert"], "dessert",
      "Десерт — dessert, две s."),
    c("de-desert", 2, "The Sahara is the largest hot ___ in the world.", "Сахара — самая большая жаркая пустыня в мире.", ["desert", "dessert"], "desert",
      "Пустыня — desert, одна s, ударение в начале."),
    c("da-dairy", 2, "Don't take this antibiotic with ___ products.", "Не принимайте этот антибиотик с молочными продуктами.", ["dairy", "diary"], "dairy",
      "Молочный — dairy."),
    c("da-diary", 2, "Keep a headache ___ for two weeks.", "Ведите дневник головной боли две недели.", ["diary", "dairy"], "diary", "Дневник — diary."),
    c("cu-cuisine", 2, "I love Italian ___.", "Я обожаю итальянскую кухню.", ["cuisine", "cousin"], "cuisine", "Кухня как еда — cuisine. Кухня-комната — kitchen."),
    c("cu-cousin", 2, "My ___ is a surgeon in Moscow.", "Мой двоюродный брат — хирург в Москве.", ["cousin", "cuisine"], "cousin", "Двоюродный брат, сестра — cousin."),
    c("ch-chef", 2, "The ___ prepared a special dinner for us.", "Шеф-повар приготовил для нас особый ужин.", ["chef", "chief"], "chef", "Шеф-повар — chef [ʃef]."),
    c("ch-chief", 2, "What's the patient's ___ complaint?", "Какая у пациента основная жалоба?", ["chief", "chef"], "chief",
      "Главный, основной — chief [tʃiːf]: chief complaint."),
    c("co-cook", 2, "My dad is a great ___.", "Мой папа отлично готовит.", ["cook", "cooker"], "cook", "Тот, кто готовит, — cook."),
    c("co-cooker", 2, "Don't forget to turn off the ___.", "Не забудь выключить плиту.", ["cooker", "cook"], "cooker",
      "Плита — cooker (в американском — stove). Повар — cook."),
    c("cr-current", 2, "What is his ___ medication?", "Какие препараты он сейчас принимает?", ["current", "currant"], "current", "Текущий — current."),
    c("cr-currant", 2, "My grandmother grew ___ in her garden.", "Бабушка выращивала смородину в саду.", ["currants", "currents"], "currants",
      "Смородина — currant, с a."),

    # 3 · на работе
    c("pp-principle", 3, "It's against my ___.", "Это против моих принципов.", ["principles", "principals"], "principles", "Принцип — principle, как rule — на -le."),
    c("pp-principal", 3, "The ___ cause of death was pneumonia.", "Основной причиной смерти стала пневмония.", ["principal", "principle"], "principal",
      "Главный, основной — principal."),
    c("st-stationary", 3, "The car was ___ when the bus hit it.", "Машина стояла на месте, когда в неё врезался автобус.", ["stationary", "stationery"], "stationary",
      "Неподвижный — stationary: a — stay, стоит."),
    c("st-stationery", 3, "Pens and paper are in the ___ cupboard.", "Ручки и бумага — в шкафу с канцтоварами.", ["stationery", "stationary"], "stationery",
      "Канцтовары — stationery: e — envelopes, бумага."),
    c("pe-personnel", 3, "Medical ___ only.", "Только для медицинского персонала.", ["personnel", "personal"], "personnel", "Персонал — personnel, ударение в конце."),
    c("pe-personal", 3, "Can I ask you a ___ question?", "Можно задать вам личный вопрос?", ["personal", "personnel"], "personal", "Личный — personal."),
    c("sf-staff", 3, "All ___ must wear ID badges.", "Все сотрудники должны носить бейджи.", ["staff", "stuff"], "staff", "Сотрудники — staff."),
    c("sf-stuff", 3, "Put your ___ in the locker.", "Положи свои вещи в шкафчик.", ["stuff", "staff"], "stuff", "Вещи (разговорное) — stuff."),

    # 4 · одна буква — другое слово
    c("en-envelope", 4, "Put the letter in an ___.", "Положи письмо в конверт.", ["envelope", "envelop"], "envelope", "Конверт — envelope, с e на конце."),
    c("en-envelop", 4, "Thick fog began to ___ the city.", "Густой туман начал окутывать город.", ["envelop", "envelope"], "envelop",
      "Окутывать (глагол) — envelop, ударение на -vel-."),
    c("dv-device", 4, "This ___ measures oxygen in the blood.", "Этот прибор измеряет кислород в крови.", ["device", "devise"], "device",
      "Прибор (существительное) — device, с c."),
    c("dv-devise", 4, "We need to ___ a new treatment plan.", "Нам нужно разработать новый план лечения.", ["devise", "device"], "devise",
      "Придумать, разработать (глагол) — devise, с s."),
    c("su-suit", 4, "Does Friday ___ you?", "Вам подходит пятница?", ["suit", "suite"], "suit", "Подходить, устраивать — suit. Ещё suit — костюм."),
    c("su-suite", 4, "They stayed in a luxury ___.", "Они жили в номере-люкс.", ["suite", "suit"], "suite", "Номер-люкс — suite [swiːt], звучит как sweet."),
    c("fa-fare", 4, "The bus ___ has gone up again.", "Проезд в автобусе опять подорожал.", ["fare", "fair"], "fare", "Плата за проезд — fare."),
    c("fa-fair", 4, "That's not ___!", "Это нечестно!", ["fair", "fare"], "fair", "Честный, справедливый — fair."),
    c("pz-price", 4, "The ___ of this drug has doubled.", "Цена этого препарата выросла вдвое.", ["price", "prize"], "price", "priCe — Цена."),
    c("pz-prize", 4, "She won first ___ in the competition.", "Она получила первый приз на конкурсе.", ["prize", "price"], "prize", "priZe — приЗ."),
    c("ca-career", 4, "She's had a long ___ in medicine.", "У неё долгая карьера в медицине.", ["career", "carrier"], "career", "Карьера — career."),
    c("ca-carrier", 4, "He's a ___ of hepatitis B.", "Он носитель гепатита B.", ["carrier", "career"], "carrier", "Носитель — carrier, от carry — «нести»."),

    # 5 · маленькие, но коварные
    c("bs-beside", 5, "Come and sit ___ me.", "Иди сядь рядом со мной.", ["beside", "besides"], "beside", "Рядом с — beside."),
    c("bs-besides", 5, "___ neurology, she's interested in cardiology.", "Помимо неврологии, она интересуется кардиологией.", ["Besides", "Beside"], "Besides",
      "Кроме, помимо — besides, с s."),
    c("la-aloud", 5, "Sorry, I was just thinking ___.", "Извини, я просто думал вслух.", ["aloud", "loudly"], "aloud", "Вслух — aloud."),
    c("la-loudly", 5, "The music next door was playing very ___.", "У соседей очень громко играла музыка.", ["loudly", "aloud"], "loudly", "Громко — loudly."),
    c("al-alternatively", 5, "You can take the bus. ___, you can walk.", "Можно поехать на автобусе. Или же можно пройтись пешком.",
      ["Alternatively", "Alternately"], "Alternatively", "Или же, как вариант — alternatively."),
    c("al-alternately", 5, "Apply ice and heat ___.", "Прикладывайте лёд и тепло поочерёдно.", ["alternately", "alternatively"], "alternately", "Поочерёдно — alternately."),
    c("ar-arise", 5, "Call me if any problems ___.", "Звоните, если возникнут проблемы.", ["arise", "rise"], "arise", "Возникать — arise: problems arise."),
    c("ar-rise", 5, "His temperature began to ___ again.", "У него снова начала подниматься температура.", ["rise", "arise"], "rise", "Подниматься, расти — rise."),
    c("cn-conscious", 5, "The patient is ___ and breathing.", "Пациент в сознании и дышит.", ["conscious", "conscience"], "conscious",
      "В сознании — conscious, на -ous: прилагательное."),
    c("cn-conscience", 5, "I have a clear ___.", "У меня чистая совесть.", ["conscience", "conscious"], "conscience", "Совесть — conscience, на -ence: существительное."),

    # 6 · качество и шансы
    c("ef-effective", 6, "This drug is very ___ against migraine.", "Этот препарат очень эффективен против мигрени.", ["effective", "efficient"], "effective",
      "Действенный, даёт результат — effective."),
    c("ef-efficient", 6, "She's very ___ — she never wastes a minute.", "Она очень продуктивная — никогда не теряет ни минуты.", ["efficient", "effective"], "efficient",
      "Без лишних затрат времени и сил — efficient."),
    c("se-sensible", 6, "That's a very ___ decision.", "Это очень разумное решение.", ["sensible", "sensitive"], "sensible", "Разумный — sensible. Ложный друг!"),
    c("se-sensitive", 6, "My teeth are ___ to cold.", "Мои зубы чувствительны к холоду.", ["sensitive", "sensible"], "sensitive", "Чувствительный — sensitive."),
    c("op-opportunity", 6, "This course is a great ___ to improve my English.", "Этот курс — отличная возможность подтянуть английский.",
      ["opportunity", "possibility"], "opportunity", "Шанс что-то сделать — opportunity to do."),
    c("op-possibility", 6, "We can't rule out the ___ of a second stroke.", "Нельзя исключить возможность повторного инсульта.", ["possibility", "opportunity"], "possibility",
      "То, что может случиться, — possibility of."),
    c("gr-grateful", 6, "I'd be ___ if you could send me the results.", "Буду благодарен, если пришлёте мне результаты.", ["grateful", "thankful"], "grateful",
      "Вежливая просьба — I'd be grateful if…"),
    c("gr-thankful", 6, "We're ___ that nobody was hurt.", "Мы рады, что никто не пострадал.", ["thankful", "grateful"], "thankful",
      "Рад, что обошлось, — thankful.", also={"grateful": "так говорят, но «хорошо, что обошлось» чаще — thankful"}),

    # 7 · люди и поступки
    c("dr-refused", 7, "He ___ to take the medication.", "Он отказался принимать лекарство.", ["refused", "denied"], "refused", "Отказаться что-то делать — refuse to do."),
    c("dr-denied", 7, "She ___ taking the money.", "Она отрицала, что взяла деньги.", ["denied", "refused"], "denied", "Отрицать — deny doing."),
    c("aa-agree", 7, "I completely ___ with you.", "Я полностью с вами согласен.", ["agree", "accept"], "agree", "Соглашаться с кем-то — agree with. I'm agree — ошибка."),
    c("aa-accepted", 7, "She ___ the job offer.", "Она приняла предложение о работе.", ["accepted", "agreed"], "accepted", "Принять то, что предлагают, — accept an offer."),
    c("as-embarrassed", 7, "I was so ___ when I forgot her name.", "Мне было так неловко, когда я забыл её имя.", ["embarrassed", "ashamed"], "embarrassed",
      "Неловко, неудобно — embarrassed."),
    c("as-ashamed", 7, "You lied to her — you should be ___ of yourself!", "Ты ей солгал — как тебе не стыдно!", ["ashamed", "embarrassed"], "ashamed",
      "Стыдно за плохой поступок — ashamed."),
    c("fs-strangers", 7, "Children shouldn't talk to ___.", "Детям не стоит разговаривать с незнакомцами.", ["strangers", "foreigners"], "strangers", "Незнакомец — stranger."),
    c("fs-foreigner", 7, "He's a ___ — he doesn't speak Russian.", "Он иностранец — не говорит по-русски.", ["foreigner", "stranger"], "foreigner",
      "Иностранец — foreigner. Вежливее — someone from abroad."),

    # 8 · вокруг нас
    c("th-high", 8, "His blood pressure is too ___.", "У него слишком высокое давление.", ["high", "tall"], "high", "Уровень — high: high pressure, high temperature."),
    c("th-tall", 8, "He's very ___ — almost two metres.", "Он очень высокий — почти два метра.", ["tall", "high"], "tall", "Рост человека — tall."),
    c("ct-city", 8, "Moscow is the largest ___ in Russia.", "Москва — крупнейший город России.", ["city", "town"], "city", "Большой город — city."),
    c("ct-town", 8, "He grew up in a small ___ near Yekaterinburg.", "Он вырос в небольшом городке под Екатеринбургом.", ["town", "city"], "town",
      "Небольшой город — town."),
    c("cs-close", 8, "I'd like to ___ my bank account.", "Я хочу закрыть банковский счёт.", ["close", "shut"], "close", "Счёт, совещание — только close."),
    c("cs-shut", 8, "Please ___ down your computer before you leave.", "Пожалуйста, выключите компьютер перед уходом.", ["shut", "close"], "shut",
      "Выключить — shut down."),
    c("sh-shade", 8, "Let's sit in the ___ — it's too hot.", "Давай сядем в тень — слишком жарко.", ["shade", "shadow"], "shade", "Тень как прохладное место — shade."),
    c("sh-shadow", 8, "The tree cast a long ___ on the grass.", "Дерево отбрасывало длинную тень на траву.", ["shadow", "shade"], "shadow",
      "Тень-силуэт от предмета — shadow."),

    # 9 · боль, слух, политика
    c("ap-pain", 9, "Chest ___ can be a sign of a heart attack.", "Боль в груди может быть признаком инфаркта.", ["pain", "ache"], "pain",
      "Боль, особенно острая, — pain: chest pain."),
    c("ap-ache", 9, "My legs ___ after yesterday's run.", "После вчерашней пробежки у меня ноют ноги.", ["ache", "pain"], "ache", "Ныть (глагол) — ache: My back aches."),
    c("hl-hear", 9, "Can you ___ me? — Yes, loud and clear.", "Вы меня слышите? — Да, отлично.", ["hear", "listen"], "hear", "Слышать — hear, без to."),
    c("hl-listen", 9, "Let me ___ to your chest.", "Давайте я послушаю ваши лёгкие.", ["listen", "hear"], "listen", "Слушать специально — listen to."),
    c("pc-politics", 9, "He's not interested in ___.", "Он не интересуется политикой.", ["politics", "policy"], "politics", "Политика: власть, партии — politics."),
    c("pc-policy", 9, "Hospital ___ doesn't allow visitors after 8 pm.", "По правилам больницы посещения после 20:00 запрещены.", ["policy", "politics"], "policy",
      "Правила организации — policy."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
    for alt in k.get("also", {}): assert alt in k["opts"] and alt != k["a"], k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert len(PAIRS) == 40 and {p["t"] for p in PAIRS} == set(range(1, MIXED_TOPIC))
# у каждой пары по две карточки, и в них встречаются оба слова пары
low = lambda s: s.lower()
for p in PAIRS:
    words = {low(p["w"][0][0]), low(p["w"][1][0])}
    hits = [k for k in CARDS if k["t"] == p["t"] and {low(o) for o in k["opts"]} & {x + e for x in words for e in ("", "s", "d", "ed")}]
    assert len(hits) >= 2, (p["w"][0][0], len(hits))

if __name__ == "__main__":
    from collections import Counter
    print(len(PAIRS), "pairs;", len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
