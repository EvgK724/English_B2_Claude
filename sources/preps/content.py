# Содержание приложения «Предлоги: at, on, in и другие».
# Пометка […] — предлог; цвет по слову: at — синий, on — оранжевый, in — зелёный, остальные — подчёркнуты.

MIXED_TOPIC = 16

GROUPS = {
    "time": "Время: at, on, in",
    "place": "Место и направление: in, at, on, to",
    "other": "Другие значения: by, with, about, on, at",
    "mix": "Итог",
}

# Главная картинка: место и время для at, on, in
GRID = {
    "place": ["at the door", "on the table", "in the room"],
    "time": ["at 5 o'clock", "on Monday", "in May"],
    "what": ["точка", "поверхность · день", "внутри · долгий период"],
}

# В больнице и в медицине: английское (с пометками) | перевод | текст для озвучки
MED = [
    ["[on] the ward · [on] the stroke unit", "в отделении", "on the ward. on the stroke unit."],
    ["[on] call · [on] duty", "на дежурстве · на смене", "on call. on duty."],
    ["[in] hospital", "лежать в больнице (пациентом)", "in hospital."],
    ["[at] the hospital", "быть в больнице по делу, работать", "at the hospital."],
    ["admitted [to] · discharged [from]", "госпитализирован в · выписан из", "admitted to. discharged from."],
    ["[on] warfarin", "принимает варфарин", "on warfarin."],
    ["[by] mouth · [by] injection", "внутрь · в виде инъекций", "by mouth. by injection."],
    ["[at] risk [of]", "в группе риска по…", "at risk of."],
    ["allergic [to]", "аллергия на…", "allergic to."],
    ["suffer [from] · die [of]", "страдать от · умереть от", "suffer from. die of."],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["in Monday", "on Monday", "дни — on"],
    ["at the morning", "in the morning", "части дня — in (но at night)"],
    ["on next week", "next week", "с next, last, this — без предлога"],
    ["in 5 o'clock", "at 5 o'clock", "точное время — at"],
    ["I'm in work.", "I'm at work.", "at work, at home"],
    ["on the photo", "in the photo", "на фото — in"],
    ["arrive to Moscow", "arrive in Moscow", "arrive in (город) · at (здание)"],
    ["go to home", "go home", "home — без to"],
    ["with car", "by car", "транспорт — by (но on foot)"],
    ["discuss about", "discuss", "discuss — без about"],
    ["good in maths", "good at maths", "good at"],
    ["sit on the table (за столом)", "sit at the table", "за столом — at"],
]

TOPICS = [
    # ——— Время
    {"n": 1, "group": "time", "title": "at — точное время", "sub": "at 5 o'clock · at night",
     "rule": "at — точный момент: at 5 o'clock, at noon, at midnight, at lunchtime. А ещё: at night, at the weekend (брит.), at Christmas, at the moment, at the age of 60.",
     "ex": [
         {"en": "The meeting starts [at] 9.", "ru": "Совещание начинается в 9."},
         {"en": "I often work [at] night.", "ru": "Я часто работаю ночью."},
         {"en": "He had his first stroke [at] the age of 60.", "ru": "Первый инсульт у него случился в 60 лет."},
     ]},
    {"n": 2, "group": "time", "title": "on — дни и даты", "sub": "on Monday · on 3 May",
     "rule": "on — день или дата: on Monday, on 3 May, on my birthday, on Christmas Day. День + часть дня — тоже on: on Friday evening.",
     "ex": [
         {"en": "The clinic is closed [on] Sundays.", "ru": "По воскресеньям поликлиника закрыта."},
         {"en": "He was admitted [on] 3 May.", "ru": "Его госпитализировали 3 мая."},
         {"en": "See you [on] Monday morning.", "ru": "Увидимся в понедельник утром."},
     ]},
    {"n": 3, "group": "time", "title": "in — месяцы, годы, части дня", "sub": "in May · in 2019 · in the morning",
     "rule": "in — долгий период: in May, in 2019, in winter, in the 1990s. Части дня: in the morning, in the afternoon, in the evening (но at night). И in = «через»: in two weeks — через две недели.",
     "ex": [
         {"en": "He was born [in] 1958.", "ru": "Он родился в 1958 году."},
         {"en": "The pain is worse [in] the morning.", "ru": "Утром боль сильнее."},
         {"en": "Come back [in] two weeks.", "ru": "Приходите через две недели."},
     ]},
    {"n": 4, "group": "time", "title": "Без предлога", "sub": "next week · last Monday · this morning",
     "rule": "Перед this, next, last, every, а также с today, tomorrow, yesterday предлог не нужен: next Monday, last week, this morning, every day, tomorrow afternoon.",
     "ex": [
         {"en": "I saw him last Monday.", "ru": "Я видел его в прошлый понедельник."},
         {"en": "Take it every morning.", "ru": "Принимайте каждое утро."},
         {"en": "The results will be ready tomorrow afternoon.", "ru": "Результаты будут готовы завтра днём."},
     ]},
    {"n": 5, "group": "time", "title": "Шаг к B2: on time, in time, by", "sub": "вовремя · успеть · к сроку", "late": 0.25,
     "rule": "on time — точно по графику; in time — успеть, пока не поздно. at the end of — в конце чего-то; in the end — в итоге. by Friday — к пятнице, не позже; until Friday — до пятницы, всё это время. during — во время чего: during the night.",
     "ex": [
         {"en": "The ambulance arrived [on] time.", "ru": "Скорая приехала точно вовремя."},
         {"en": "We got him to hospital [in] time.", "ru": "Мы успели довезти его до больницы."},
         {"en": "Send it [by] Friday.", "ru": "Пришлите к пятнице."},
         {"en": "[In] the end, he agreed.", "ru": "В итоге он согласился."},
     ]},
    # ——— Место и направление
    {"n": 6, "group": "place", "title": "in — внутри", "sub": "in the room · in bed · in Moscow",
     "rule": "in — внутри пространства: in the room, in the car, in the box. Город и страна — in: in Moscow, in Russia. Устойчивые: in bed, in hospital (лежать пациентом), in the photo, in the newspaper, in a queue.",
     "ex": [
         {"en": "The patient is [in] bed.", "ru": "Пациент в постели."},
         {"en": "She lives [in] Moscow.", "ru": "Она живёт в Москве."},
         {"en": "Who's that [in] the photo?", "ru": "Кто это на фото? — по-русски «на», по-английски in"},
     ]},
    {"n": 7, "group": "place", "title": "at — точка, место встречи", "sub": "at the door · at work · at home",
     "rule": "at — точка или место, где что-то происходит: at the door, at the bus stop, at the top. Места, где мы чем-то заняты: at work, at home, at school, at university, at the doctor's, at a conference.",
     "ex": [
         {"en": "There's someone [at] the door.", "ru": "Кто-то стоит у двери."},
         {"en": "I'm still [at] work.", "ru": "Я ещё на работе."},
         {"en": "We met [at] a conference.", "ru": "Мы познакомились на конференции."},
     ]},
    {"n": 8, "group": "place", "title": "on — поверхность, этаж, транспорт", "sub": "on the table · on the bus · on the ward",
     "rule": "on — на поверхности: on the table, on the wall, on the floor. Этаж — on: on the first floor. Стороны — on the left, on the right. Транспорт, где можно ходить, — on: on the bus, on the train, on the plane (но in a car, in a taxi). В больнице: on the ward, on the stroke unit.",
     "ex": [
         {"en": "The results are [on] your desk.", "ru": "Результаты у тебя на столе."},
         {"en": "Radiology is [on] the first floor.", "ru": "Рентгенология на втором этаже. — в британском first floor = наш второй"},
         {"en": "He's [on] the stroke unit.", "ru": "Он лежит в инсультном отделении."},
     ]},
    {"n": 9, "group": "place", "title": "to — направление", "sub": "go to work · send to the lab",
     "rule": "to — движение куда-то: go to work, come to the hospital, send it to the lab, from … to. Внутрь — into. Без to: go home, go there, go abroad. Arrive — не to, а in (город) или at (здание).",
     "ex": [
         {"en": "He was taken [to] hospital.", "ru": "Его отвезли в больницу."},
         {"en": "I go [to] work by bus.", "ru": "Я езжу на работу на автобусе."},
         {"en": "We arrived [at] the hospital at six.", "ru": "Мы приехали в больницу в шесть."},
     ]},
    {"n": 10, "group": "place", "title": "at, in или to?", "sub": "быть — at · идти — to",
     "rule": "Где? — at или in: I'm at the hospital, he's in the operating theatre. Куда? — to: I'm going to the hospital. Одно и то же место: быть — at, идти — to. За столом — at the table, а on the table — «на столе».",
     "ex": [
         {"en": "I'm [at] the hospital.", "ru": "Я в больнице (по делу, на работе)."},
         {"en": "I'm going [to] the hospital.", "ru": "Я еду в больницу."},
         {"en": "She was sitting [at] the table.", "ru": "Она сидела за столом."},
     ]},
    # ——— Другие значения
    {"n": 11, "group": "other", "title": "by — способ, автор, к сроку", "sub": "by car · by email · by Friday",
     "rule": "by — способ и транспорт: by car, by bus, by email, by phone (но on foot). Кто сделал: written by, caused by. К сроку: by Friday. Рядом: by the window. Устойчивые: by mistake, by chance, by heart (наизусть).",
     "ex": [
         {"en": "I usually come [by] bus.", "ru": "Обычно я приезжаю на автобусе."},
         {"en": "Send it [by] email.", "ru": "Пришлите по электронной почте."},
         {"en": "The stroke was caused [by] a clot.", "ru": "Инсульт был вызван тромбом."},
     ]},
    {"n": 12, "group": "other", "title": "with — с кем и чем", "sub": "with a friend · with a scalpel",
     "rule": "with — с кем: with a friend, with the family. Чем, каким инструментом или средством: with a scalpel, with saline. С каким признаком: a patient with diabetes. Транспорт — не with, а by: by car.",
     "ex": [
         {"en": "He came [with] his wife.", "ru": "Он пришёл с женой."},
         {"en": "Clean the wound [with] saline.", "ru": "Промойте рану физраствором."},
         {"en": "a patient [with] diabetes", "ru": "пациент с диабетом"},
     ]},
    {"n": 13, "group": "other", "title": "about — о чём", "sub": "talk about · worried about",
     "rule": "about — о чём: talk about, think about, a book about, worried about, ask about. How about…? и What about…? — «как насчёт…?». About + число — «примерно»: about fifty. Но discuss — без about.",
     "ex": [
         {"en": "We talked [about] his treatment.", "ru": "Мы поговорили о его лечении."},
         {"en": "She's worried [about] the results.", "ru": "Она волнуется из-за результатов."},
         {"en": "There were [about] fifty people.", "ru": "Было около пятидесяти человек."},
     ]},
    {"n": 14, "group": "other", "title": "on — тема, связь, лекарство", "sub": "a lecture on stroke · on the phone",
     "rule": "on — научная тема: a lecture on stroke, a book on neurology. Связь и экран: on the phone, on TV, on the radio, on the internet. В медицине: on call, on duty, on warfarin — «принимает варфарин». Ещё: on foot, on holiday, on purpose (нарочно).",
     "ex": [
         {"en": "She gave a lecture [on] stroke.", "ru": "Она прочитала лекцию об инсульте."},
         {"en": "He's [on] the phone.", "ru": "Он говорит по телефону."},
         {"en": "Is he [on] warfarin?", "ru": "Он принимает варфарин?"},
     ]},
    {"n": 15, "group": "other", "title": "at — ещё значения", "sub": "good at · at risk · at least",
     "rule": "at — после good, bad, better: good at languages. Устойчивые: at risk (в группе риска), at least (по крайней мере), at first (сначала), at last (наконец), at once (сразу), at 80 km/h (скорость).",
     "ex": [
         {"en": "She's good [at] languages.", "ru": "Ей хорошо даются языки."},
         {"en": "Smokers are [at] higher risk.", "ru": "Курильщики — в группе повышенного риска."},
         {"en": "Drink [at] least two litres a day.", "ru": "Пейте не меньше двух литров в день."},
     ]},
    {"n": 16, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

AOI = ["at", "on", "in"]
def c(id, t, q, ru, a, why, opts=None, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts or AOI, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · at — точное время
    c("ti-at8", 1, "The ward round starts ___ 8 o'clock.", "Обход начинается в 8 часов.", "at", "Точное время — at."),
    c("ti-night", 1, "I often work ___ night.", "Я часто работаю ночью.", "at", "at night — «ночью». Но in the morning, in the evening."),
    c("ti-weekend", 1, "What are you doing ___ the weekend?", "Что делаешь на выходных?", "at",
      "at the weekend — британский вариант.", also={"on": "так говорят в американском"}),
    c("ti-christmas", 1, "We usually visit my parents ___ Christmas.", "На Рождество мы обычно ездим к родителям.", "at",
      "Праздник в целом — at: at Christmas, at Easter. Но сам день — on Christmas Day.",
      also={"on": "в американском on Christmas — это сам день Рождества"}),
    c("ti-age", 1, "He retired ___ the age of 65.", "Он вышел на пенсию в 65 лет.", "at", "at the age of … — «в возрасте …»."),
    c("ti-moment", 1, "She's busy ___ the moment.", "Она сейчас занята.", "at", "at the moment — «сейчас»."),

    # 2 · on — дни и даты
    c("on-sundays", 2, "The clinic is closed ___ Sundays.", "По воскресеньям поликлиника закрыта.", "on", "Дни недели — on."),
    c("on-date", 2, "He was admitted ___ 3 May.", "Его госпитализировали 3 мая.", "on", "Дата — on."),
    c("on-birthday", 2, "She called me ___ my birthday.", "Она позвонила мне в день рождения.", "on", "Конкретный день — on: on my birthday."),
    c("on-morning", 2, "I'll see you ___ Monday morning.", "Увидимся в понедельник утром.", "on",
      "День + часть дня — on: on Monday morning. Но просто in the morning."),
    c("on-xmasday", 2, "The unit is open even ___ Christmas Day.", "Отделение работает даже в сам день Рождества.", "on",
      "Конкретный день праздника — on Christmas Day. Праздник в целом — at Christmas."),
    c("on-weekdays", 2, "I go to the gym ___ weekdays.", "Я хожу в спортзал по будням.", "on", "on weekdays — «по будням»."),

    # 3 · in — месяцы, годы, части дня
    c("in-year", 3, "He had a heart attack ___ 2019.", "У него был инфаркт в 2019 году.", "in", "Год — in."),
    c("in-month", 3, "The conference is ___ October.", "Конференция в октябре.", "in", "Месяц — in."),
    c("in-morning", 3, "The headaches are worse ___ the morning.", "Головные боли сильнее по утрам.", "in",
      "Части дня — in the morning. Но at night."),
    c("in-minutes", 3, "I'll be back ___ ten minutes.", "Я вернусь через десять минут.", "in", "in = «через»: in ten minutes."),
    c("in-winter", 3, "Flu is more common ___ winter.", "Зимой грипп встречается чаще.", "in", "Времена года — in."),
    c("in-decade", 3, "This method was developed ___ the 1990s.", "Этот метод разработали в 1990-х.", "in", "Десятилетия и века — in: in the 1990s."),

    # 4 · без предлога
    c("np-next", 4, "The operation is ___ next Monday.", "Операция в следующий понедельник.", "", "С next — без предлога: next Monday.",
      opts=["", "on", "in"]),
    c("np-last", 4, "I saw him ___ last week.", "Я видел его на прошлой неделе.", "", "С last — без предлога.", opts=["", "in", "at"]),
    c("np-this", 4, "He was discharged ___ this morning.", "Его выписали сегодня утром.", "",
      "this morning — без предлога. Но in the morning.", opts=["", "in", "on"]),
    c("np-every", 4, "Take one tablet ___ every evening.", "Принимайте по таблетке каждый вечер.", "", "С every — без предлога.",
      opts=["", "in", "at"]),
    c("np-tomorrow", 4, "The results will be ready ___ tomorrow.", "Результаты будут готовы завтра.", "",
      "tomorrow, today, yesterday — без предлога.", opts=["", "on", "in"]),

    # 5 · шаг к B2
    c("b2-ontime", 5, "The ambulance arrived exactly ___ time.", "Скорая приехала точно вовремя.", "on", "Точно по графику — on time."),
    c("b2-intime", 5, "We started the treatment just ___ time.", "Мы начали лечение как раз вовремя — успели.", "in",
      "Успеть, пока не поздно, — in time: just in time.", opts=["in", "on", "at"]),
    c("b2-intheend", 5, "___ the end, he agreed to the operation.", "В итоге он согласился на операцию.", "In",
      "«В итоге» — in the end. At the end of — «в конце чего-то».", opts=["In", "At", "On"]),
    c("b2-endof", 5, "Please pay ___ the end of the month.", "Пожалуйста, оплатите в конце месяца.", "at", "«В конце чего-то» — at the end of."),
    c("b2-by", 5, "Please send me the report ___ Friday.", "Пожалуйста, пришлите отчёт к пятнице.", "by",
      "«К сроку, не позже» — by. Until — «до, всё это время».", opts=["by", "until"]),
    c("b2-until", 5, "He has to stay in bed ___ Friday.", "Ему нужно лежать до пятницы.", "until",
      "«До, всё это время» — until. By — «к сроку».", opts=["until", "by"]),
    c("b2-during", 5, "He woke up twice ___ the night.", "Ночью он дважды просыпался.", "during",
      "«Во время чего» — during. For — сколько длится: for two hours.", opts=["during", "for", "while"]),

    # 6 · in — внутри
    c("pl-room", 6, "The patient is waiting ___ the examination room.", "Пациент ждёт в смотровой.", "in", "Внутри помещения — in."),
    c("pl-city", 6, "She lives ___ Moscow.", "Она живёт в Москве.", "in", "Город, страна — in."),
    c("pl-bed", 6, "He's still ___ bed.", "Он всё ещё в постели.", "in", "in bed — «в постели», без the."),
    c("pl-hospital", 6, "My father is ___ hospital with pneumonia.", "Мой отец лежит в больнице с пневмонией.", "in",
      "in hospital (брит.) — лежать в больнице пациентом. At the hospital — быть там по делу."),
    c("pl-car", 6, "Get ___ the car, please.", "Садитесь, пожалуйста, в машину.", "in",
      "Машина, такси — in: там не встать в полный рост. Автобус, поезд — on."),
    c("pl-photo", 6, "Who's that ___ the photo?", "Кто это на фотографии?", "in", "На фото, на картинке — in: in the photo."),

    # 7 · at — точка
    c("at-door", 7, "There's someone ___ the door.", "Кто-то стоит у двери.", "at", "Точка — at: at the door."),
    c("at-work", 7, "I'm still ___ work.", "Я ещё на работе.", "at", "at work — «на работе»."),
    c("at-home", 7, "She's ___ home today.", "Она сегодня дома.", "at", "at home — «дома». А go home — без предлога."),
    c("at-conference", 7, "We met ___ a conference in Berlin.", "Мы познакомились на конференции в Берлине.", "at",
      "Мероприятие — at: at a conference, at a meeting."),
    c("at-busstop", 7, "I'll wait for you ___ the bus stop.", "Подожду тебя на остановке.", "at",
      "Точка — at: at the bus stop. По-русски «на», а по-английски at."),
    c("at-corridor", 7, "Turn left ___ the end of the corridor.", "В конце коридора поверните налево.", "at",
      "at the end of — «в конце чего-то»: at the end of the corridor."),

    # 8 · on — поверхность, этаж, транспорт
    c("on-desk", 8, "Your results are ___ my desk.", "Ваши результаты у меня на столе.", "on", "На поверхности — on."),
    c("on-floor", 8, "Radiology is ___ the first floor.", "Рентгенология на втором этаже.", "on",
      "Этаж — on. В британском first floor — это наш второй этаж, а наш первый — ground floor."),
    c("on-bus", 8, "I read ___ the bus to work.", "По дороге на работу я читаю в автобусе.", "on",
      "Автобус, поезд, самолёт — on. Машина, такси — in."),
    c("on-ward", 8, "He's ___ the stroke unit.", "Он лежит в инсультном отделении.", "on",
      "Отделение больницы — on: on the ward, on the stroke unit.", also={"in": "так говорят, но у врачей обычнее on the ward"}),
    c("on-left", 8, "The lift is ___ the left.", "Лифт слева.", "on", "on the left, on the right — «слева», «справа»."),
    c("on-wall", 8, "There's a clock ___ the wall.", "На стене висят часы.", "on", "На стене — on: поверхность."),

    # 9 · to — направление
    c("to-work", 9, "I go ___ work by bus.", "Я езжу на работу на автобусе.", "to",
      "Движение куда — to: go to work. А быть на работе — at work.", opts=["to", "in", "at"]),
    c("to-hospital", 9, "He was taken ___ hospital by ambulance.", "Его отвезли в больницу на скорой.", "to", "Куда — to hospital.",
      opts=["to", "in", "at"]),
    c("to-home", 9, "Let's go ___ home.", "Пойдём домой.", "", "home — без to: go home.", opts=["", "to", "at"]),
    c("to-arrive", 9, "We arrived ___ the hospital at six.", "Мы приехали в больницу в шесть.", "at",
      "arrive at (здание) или in (город). Arrive to — ошибка.", opts=["at", "to", "in"]),
    c("to-arrivecity", 9, "They arrived ___ London last night.", "Они прилетели в Лондон вчера вечером.", "in",
      "arrive in + город или страна.", opts=["in", "to", "at"]),
    c("to-into", 9, "He walked ___ the room.", "Он вошёл в палату.", "into", "Движение внутрь — into.", opts=["into", "to", "at"]),

    # 10 · at, in или to?
    c("ia-at", 10, "I'm ___ the hospital — I'll call you later.", "Я в больнице — перезвоню позже.", "at", "Где? — at the hospital.",
      opts=["at", "to", "on"]),
    c("ia-to", 10, "I'm on my way ___ the hospital.", "Я еду в больницу.", "to", "Куда? — to.", opts=["to", "at", "in"]),
    c("ia-in", 10, "The surgeon is still ___ the operating theatre.", "Хирург ещё в операционной.", "in", "Внутри помещения — in.",
      opts=["in", "at", "to"]),
    c("ia-entrance", 10, "I'll meet you ___ the main entrance.", "Встречу тебя у главного входа.", "at", "Точка встречи — at.", opts=["at", "in", "to"]),
    c("ia-sent", 10, "The sample was sent ___ the lab.", "Образец отправили в лабораторию.", "to", "Куда? — to.", opts=["to", "in", "at"]),
    c("ia-table", 10, "She was sitting ___ the table.", "Она сидела за столом.", "at",
      "За столом — at the table. On the table — «на столе», сверху."),

    # 11 · by
    c("by-bus", 11, "I usually come to work ___ bus.", "Обычно я езжу на работу на автобусе.", "by",
      "Транспорт как способ — by bus, без артикля. On the bus — «в автобусе».", opts=["by", "on", "with"]),
    c("by-foot", 11, "I usually come to work ___ foot.", "Обычно я хожу на работу пешком.", "on",
      "Пешком — on foot. Остальной транспорт — by.", opts=["on", "by", "with"]),
    c("by-email", 11, "Please send the results ___ email.", "Пожалуйста, пришлите результаты по почте.", "by",
      "Способ — by: by email, by phone, by post.", opts=["by", "on", "with"]),
    c("by-caused", 11, "The stroke was caused ___ a blood clot.", "Инсульт был вызван тромбом.", "by",
      "Кто или что это сделало (в пассиве) — by.", opts=["by", "with", "from"]),
    c("by-deadline", 11, "The report must be ready ___ Monday.", "Отчёт должен быть готов к понедельнику.", "by",
      "«К сроку» — by.", opts=["by", "until"]),
    c("by-mistake", 11, "I took his notes ___ mistake.", "Я по ошибке взял его записи.", "by",
      "by mistake — «по ошибке». Ещё: by chance, by heart.", opts=["by", "on", "with"]),

    # 12 · with
    c("wi-wife", 12, "He came ___ his wife.", "Он пришёл с женой.", "with", "С кем — with.", opts=["with", "by", "and"]),
    c("wi-saline", 12, "Clean the wound ___ saline.", "Промойте рану физраствором.", "with", "Чем, каким средством — with.",
      opts=["with", "by", "in"]),
    c("wi-diabetes", 12, "We have three patients ___ diabetes on the ward.", "В отделении три пациента с диабетом.", "with",
      "С каким заболеванием, признаком — with: a patient with diabetes.", opts=["with", "of", "by"]),
    c("wi-scalpel", 12, "The surgeon made a cut ___ a scalpel.", "Хирург сделал разрез скальпелем.", "with",
      "Инструмент — with.", opts=["with", "by", "from"]),
    c("wi-agree", 12, "I agree ___ you.", "Я с тобой согласен.", "with",
      "agree with — «согласен с кем-то». Agree to — «согласиться на что-то».", opts=["with", "to", "by"]),
    c("wi-car", 12, "She came to the clinic ___ car.", "Она приехала в поликлинику на машине.", "by",
      "Транспорт — by car, а не with car.", opts=["by", "with", "on"]),

    # 13 · about
    c("ab-talk", 13, "Can we talk ___ your test results?", "Можно поговорить о ваших анализах?", "about", "Говорить о чём — talk about.",
      opts=["about", "on", "of"]),
    c("ab-worried", 13, "She's worried ___ her husband.", "Она волнуется за мужа.", "about", "Волноваться о ком-то — worried about.",
      opts=["about", "for", "of"], also={"for": "бывает и так — «боится за него»; обычнее worried about"}),
    c("ab-think", 13, "I'll think ___ it.", "Я подумаю об этом.", "about",
      "«Обдумать» — think about. Think of — «придумать, вспомнить».", opts=["about", "on", "of"]),
    c("ab-approx", 13, "There were ___ fifty people at the lecture.", "На лекции было около пятидесяти человек.", "about",
      "about + число — «примерно».", opts=["about", "on", "by"]),
    c("ab-howabout", 13, "How ___ a coffee break?", "Как насчёт перерыва на кофе?", "about", "How about…? — «как насчёт…?»",
      opts=["about", "on", "for"]),
    c("ab-discuss", 13, "We discussed ___ the plan.", "Мы обсудили план.", "", "discuss — без about. А talk about — с about.",
      opts=["", "about", "on"]),

    # 14 · on — тема, связь, лекарство
    c("ot-lecture", 14, "She gave a lecture ___ stroke prevention.", "Она прочитала лекцию о профилактике инсульта.", "on",
      "Научная тема — on: a lecture on…", opts=["on", "about", "of"], also={"about": "так можно; on — научнее и официальнее"}),
    c("ot-phone", 14, "Dr Smith is ___ the phone.", "Доктор Смит говорит по телефону.", "on",
      "Говорить по телефону — on the phone. Связаться по телефону как способ — by phone.", opts=["on", "at", "by"]),
    c("ot-warfarin", 14, "Is he ___ any anticoagulants?", "Он принимает какие-нибудь антикоагулянты?", "on",
      "Принимать лекарство курсом — be on: on warfarin, on anticoagulants.", opts=["on", "with", "at"]),
    c("ot-call", 14, "I'm ___ call this weekend.", "В эти выходные я дежурю.", "on",
      "on call — «на дежурстве по вызову»; on duty — «на смене».", opts=["on", "at", "in"]),
    c("ot-purpose", 14, "He didn't do it ___ purpose.", "Он сделал это не нарочно.", "on",
      "on purpose — «нарочно». Случайно — by accident, by mistake.", opts=["on", "by", "with"]),
    c("ot-tv", 14, "I saw it ___ TV.", "Я видел это по телевизору.", "on", "По телевизору, по радио — on TV, on the radio.",
      opts=["on", "in", "by"]),

    # 15 · at — ещё значения
    c("at-good", 15, "He's very good ___ explaining things.", "Он очень хорошо умеет объяснять.", "at",
      "good at — «хорошо умеет». Good in — ошибка.", opts=["at", "in", "on"]),
    c("at-risk", 15, "Smokers are ___ higher risk of stroke.", "У курильщиков выше риск инсульта.", "at",
      "at risk — «в группе риска»: at high risk of…", opts=["at", "in", "on"]),
    c("at-least", 15, "Drink ___ least two litres of water a day.", "Пейте не меньше двух литров воды в день.", "at",
      "at least — «по крайней мере, не меньше».", opts=["at", "in", "for"]),
    c("at-first", 15, "___ first, he refused the treatment.", "Сначала он отказался от лечения.", "At", "at first — «сначала, поначалу».",
      opts=["At", "In", "On"]),
    c("at-once", 15, "Call the doctor ___ once!", "Немедленно позовите врача!", "at", "at once — «сразу, немедленно».",
      opts=["at", "in", "on"]),
    c("at-speed", 15, "He was driving ___ 120 kilometres an hour.", "Он ехал со скоростью 120 км/ч.", "at", "Скорость — at: at 120 km/h.",
      opts=["at", "with", "by"]),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
