# Содержание приложения «in / into, on / onto».
# Пометка […] — предлог: in и on — синий (где?), into и onto — оранжевый (куда?), остальные подчёркнуты.

MIXED_TOPIC = 9

GROUPS = {
    "in": "in или into",
    "on": "on или onto",
    "more": "Транспорт и тонкости",
    "med": "В больнице",
    "mix": "Итог",
}

# Один глагол — разный смысл: [где-вариант, перевод], [куда-вариант, перевод]
CONTRAST = [
    [["We walked [in] the park.", "гуляли в парке"], ["We walked [into] the park.", "вошли в парк"]],
    [["The children swam [in] the lake.", "плавали в озере"], ["The children jumped [into] the lake.", "прыгнули в озеро"]],
    [["He's [in] the car.", "сидит в машине"], ["He got [into] the car.", "сел в машину"]],
    [["The cat is [on] the table.", "сидит на столе"], ["The cat jumped [onto] the table.", "запрыгнула на стол"]],
    [["The children ran [on] the ice.", "бегали по льду"], ["The children ran [onto] the ice.", "выбежали на лёд"]],
    [["Move the patient [on] the trolley.", "везите пациента на каталке"], ["Move the patient [onto] the trolley.", "переложите пациента на каталку"]],
]

# into — не только «внутрь»: сочетание | перевод | пример
INTO = [
    ["turn [into]", "превращаться в", "Water turns into ice."],
    ["translate [into]", "переводить на (язык)", "Translate it into English."],
    ["divide [into]", "делить на", "Divide the students into groups."],
    ["crash [into]", "врезаться в", "The car crashed into a tree."],
    ["bump [into]", "случайно встретить", "I bumped into an old friend."],
    ["look [into]", "разобраться, изучить", "We'll look into the problem."],
    ["be [into]", "увлекаться (разг.)", "My son is into football."],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["Translate it in English.", "Translate it into English.", "перевести на язык — into"],
    ["Water turns in ice.", "Water turns into ice.", "превращаться — into"],
    ["Come into, please!", "Come in, please!", "без существительного — in"],
    ["Get in the bus.", "Get on the bus.", "автобус, поезд — on"],
    ["He's sitting on the car.", "He's sitting in the car.", "машина — in; on the car — на крыше"],
    ["Divide them in groups.", "Divide them into groups.", "делить на — into"],
    ["I bumped on an old friend.", "I bumped into an old friend.", "случайно встретить — bump into"],
    ["The patient is into bed.", "The patient is in bed.", "где? — in"],
    ["We'll look in the problem.", "We'll look into the problem.", "разобраться — look into"],
    ["Let's move onto the next topic.", "Let's move on to the next topic.", "move on + to — два слова"],
]

TOPICS = [
    {"n": 1, "group": "in", "title": "in — где?", "sub": "внутри, уже на месте",
     "rule": "in — где? Внутри, в пределах чего-то: in the room, in my bag, in London, in bed, in the car. Движения нет — человек или предмет уже там: The keys are in my bag. We walked in the park — гуляли в парке, по его территории.",
     "ex": [
         {"en": "The keys are [in] my bag.", "ru": "Ключи у меня в сумке."},
         {"en": "The patient is [in] bed.", "ru": "Пациент в постели."},
         {"en": "We walked [in] the park.", "ru": "Мы гуляли в парке."},
     ]},
    {"n": 2, "group": "in", "title": "into — куда?", "sub": "движение внутрь",
     "rule": "into — куда? Движение снаружи внутрь: walk into the room, move into a new flat, run into the house. Сравни: We walked in the park — гуляли в парке; We walked into the park — вошли в парк. После put, throw, jump, fall в разговоре годится и in: Put it in the box.",
     "ex": [
         {"en": "She walked [into] the room.", "ru": "Она вошла в комнату."},
         {"en": "We walked [into] the park.", "ru": "Мы вошли в парк."},
         {"en": "They moved [into] a new flat.", "ru": "Они переехали в новую квартиру."},
     ]},
    {"n": 3, "group": "in", "title": "into — не только «внутрь»", "sub": "превращение · встреча · интерес",
     "rule": "into — ещё и превращение, деление: turn into ice, translate into English, divide into groups. Столкновение: crash into a tree. Случайная встреча: bump into, run into an old friend. Разобраться: look into a problem. Увлекаться (разг.): I'm into jazz.",
     "ex": [
         {"en": "Translate it [into] English.", "ru": "Переведи это на английский."},
         {"en": "Water turns [into] ice.", "ru": "Вода превращается в лёд."},
         {"en": "I bumped [into] an old friend.", "ru": "Я случайно встретил старого друга."},
     ]},
    {"n": 4, "group": "on", "title": "on — где?", "sub": "на поверхности",
     "rule": "on — где? На поверхности: on the table, on the wall, on the floor, on the screen, on the roof. Движения нет: The results are on your desk. The cat is on the table.",
     "ex": [
         {"en": "The results are [on] your desk.", "ru": "Результаты у вас на столе."},
         {"en": "There's a clock [on] the wall.", "ru": "На стене висят часы."},
         {"en": "The cat is [on] the table.", "ru": "Кошка сидит на столе."},
     ]},
    {"n": 5, "group": "on", "title": "onto — куда?", "sub": "движение на поверхность",
     "rule": "onto — куда? Движение на поверхность: jump onto the table, move the patient onto the trolley, roll onto the road. Иногда без onto меняется смысл: run on the ice — бегать по льду, run onto the ice — выбежать на лёд. В разговоре часто говорят и on: jump on the table. После put обычно просто on: Put it on the table.",
     "ex": [
         {"en": "The cat jumped [onto] the table.", "ru": "Кошка запрыгнула на стол."},
         {"en": "Move the patient [onto] the trolley.", "ru": "Переложите пациента на каталку."},
         {"en": "The ball rolled [onto] the road.", "ru": "Мяч выкатился на дорогу."},
     ]},
    {"n": 6, "group": "more", "title": "Транспорт: in или on", "sub": "in the car · on the bus",
     "rule": "Машина, такси — сидишь внутри и встать нельзя: in the car, get in(to) the car, get out of the car. Автобус, поезд, самолёт — можно ходить внутри: on the bus, get on the bus, get off the bus. Велосипед, мотоцикл — сидишь сверху: on a bike. Осторожно: on the car — «на крыше машины».",
     "ex": [
         {"en": "She's [in] the car.", "ru": "Она в машине."},
         {"en": "We got [on] the bus.", "ru": "Мы сели в автобус."},
         {"en": "Get [off] at the next stop.", "ru": "Выходите на следующей остановке."},
     ]},
    {"n": 7, "group": "more", "title": "Тонкости", "sub": "Come in! · Hold on! · move on to",
     "rule": "Если после предлога нет существительного — только in или on: Come in! Get in! Hold on! Into и onto всегда требуют существительного: come into the room. Когда on — часть глагола, а to — отдельный предлог, пишут раздельно: move on to the next topic.",
     "ex": [
         {"en": "Come [in]!", "ru": "Входите!"},
         {"en": "Hold [on]!", "ru": "Подождите!"},
         {"en": "Let's move [on to] the next topic.", "ru": "Переходим к следующей теме."},
     ]},
    {"n": 8, "group": "med", "title": "В больнице", "sub": "in intensive care · on a drip · onto his side",
     "rule": "in: in hospital (брит.), in intensive care, in bed. on: on a drip — под капельницей, on medication — на лекарствах. into: inject into a vein, insert into. onto: move onto the trolley, roll onto his side.",
     "ex": [
         {"en": "He's [in] intensive care.", "ru": "Он в реанимации."},
         {"en": "She's [on] a drip.", "ru": "Она под капельницей."},
         {"en": "Roll him [onto] his side.", "ru": "Поверните его на бок."},
     ]},
    {"n": 9, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · in — где?
    c("i1-bag", 1, "The keys are ___ my bag.", "Ключи у меня в сумке.", ["in", "into"], "in", "Где? — in. Движения нет."),
    c("i1-bed", 1, "The patient is still ___ bed.", "Пациент ещё в постели.", ["in", "into"], "in", "Где? — in: in bed."),
    c("i1-flat", 1, "She lives ___ a small flat near the hospital.", "Она живёт в маленькой квартире рядом с больницей.", ["in", "into"], "in",
      "Где живёт? — in."),
    c("i1-car", 1, "He's waiting ___ the car.", "Он ждёт в машине.", ["in", "into"], "in", "Где ждёт? — in."),
    c("i1-park", 1, "We walked ___ the park for an hour.", "Мы целый час гуляли в парке.", ["in", "into"], "in",
      "Гулять в парке (где?) — in. Walk into the park — «войти в парк»."),
    c("i1-swim", 1, "The children are swimming ___ the pool.", "Дети плавают в бассейне.", ["in", "into"], "in",
      "Плавать в бассейне (где?) — in. Прыгнуть в бассейн — into."),

    # 2 · into — куда?
    c("i2-room", 2, "She walked ___ the room and sat down.", "Она вошла в комнату и села.", ["into", "in"], "into", "Куда? Движение внутрь — into."),
    c("i2-ward", 2, "A nurse came ___ the ward with the results.", "В палату вошла медсестра с результатами.", ["into", "in"], "into", "Вошла куда? — into."),
    c("i2-blood", 2, "The drug is injected directly ___ the bloodstream.", "Препарат вводят прямо в кровоток.", ["into", "in"], "into",
      "Ввести внутрь — into: inject into."),
    c("i2-hide", 2, "The boy ran ___ the house to hide.", "Мальчик забежал в дом, чтобы спрятаться.", ["into", "in"], "into",
      "Забежать внутрь — into. Run in the house — «бегать по дому»."),
    c("i2-gate", 2, "We walked ___ the park through the main gate.", "Мы вошли в парк через главные ворота.", ["into", "in"], "into",
      "Войти в парк — into. Гулять в парке — in."),
    c("i2-flat", 2, "They moved ___ a new flat last month.", "В прошлом месяце они переехали в новую квартиру.", ["into", "in"], "into",
      "Въехать куда? — move into."),

    # 3 · into — не только «внутрь»
    c("i3-translate", 3, "Can you translate this letter ___ English?", "Можете перевести это письмо на английский?", ["into", "in", "on"], "into",
      "Перевести на язык — translate into."),
    c("i3-ice", 3, "Water turns ___ ice at 0 °C.", "При 0 °C вода превращается в лёд.", ["into", "in", "on"], "into", "Превращаться — turn into."),
    c("i3-groups", 3, "The teacher divided the students ___ three groups.", "Преподаватель разделил студентов на три группы.", ["into", "in", "on"], "into",
      "Делить на — divide into."),
    c("i3-bump", 3, "I bumped ___ an old classmate at the supermarket.", "В супермаркете я случайно встретил бывшего одноклассника.", ["into", "in", "on"], "into",
      "Случайно встретить — bump into."),
    c("i3-look", 3, "We'll look ___ the problem and call you back.", "Мы разберёмся с проблемой и перезвоним вам.", ["into", "in", "on"], "into",
      "Разобраться, изучить — look into."),
    c("i3-crash", 3, "The car crashed ___ a tree.", "Машина врезалась в дерево.", ["into", "in", "on"], "into", "Врезаться — crash into."),
    c("i3-fan", 3, "My son is really ___ football at the moment.", "Мой сын сейчас очень увлекается футболом.", ["into", "in", "on"], "into",
      "Увлекаться (разг.) — be into."),

    # 4 · on — где?
    c("o4-desk", 4, "The results are ___ your desk.", "Результаты у вас на столе.", ["on", "onto"], "on", "Где? На поверхности — on."),
    c("o4-wall", 4, "There's a clock ___ the wall.", "На стене висят часы.", ["on", "onto"], "on", "Где? — on the wall."),
    c("o4-floor", 4, "The patient was lying ___ the floor when we arrived.", "Когда мы приехали, пациент лежал на полу.", ["on", "onto"], "on",
      "Где лежал? — on."),
    c("o4-screen", 4, "Look at the image ___ the screen.", "Посмотрите на изображение на экране.", ["on", "onto"], "on", "На экране — on the screen."),
    c("o4-roof", 4, "The cat is sitting ___ the roof.", "Кошка сидит на крыше.", ["on", "onto"], "on", "Где сидит? — on."),

    # 5 · onto — куда?
    c("o5-trolley", 5, "Let's move the patient ___ the trolley — one, two, three!", "Перекладываем пациента на каталку — раз, два, три!", ["onto", "on"], "onto",
      "Переложить на — onto. Move him on the trolley — «везти его на каталке»."),
    c("o5-road", 5, "The ball rolled ___ the road.", "Мяч выкатился на дорогу.", ["onto", "on"], "onto",
      "Выкатиться на — onto. Roll on the road — «катиться по дороге»."),
    c("o5-ice", 5, "The children ran ___ the ice.", "Дети выбежали на лёд.", ["onto", "on"], "onto", "Выбежать на — onto. Run on the ice — «бегать по льду»."),
    c("o5-cat", 5, "The cat jumped ___ the table.", "Кошка запрыгнула на стол.", ["onto", "on", "into"], "onto", "Движение на поверхность — onto.",
      also={"on": "в разговоре так говорят, но движение на поверхность точнее — onto"}),

    # 6 · транспорт
    c("t6-bus", 6, "We got ___ the bus at the railway station.", "Мы сели в автобус у вокзала.", ["on", "in", "into"], "on", "Автобус, поезд, самолёт — get on."),
    c("t6-car", 6, "She's sitting ___ the car, waiting for you.", "Она сидит в машине и ждёт тебя.", ["in", "on"], "in",
      "Машина — in. On the car — «на крыше машины»."),
    c("t6-taxi", 6, "He got ___ a taxi and went to the airport.", "Он сел в такси и поехал в аэропорт.", ["into", "on", "onto"], "into",
      "Такси, машина — get into (или get in)."),
    c("t6-plane", 6, "There were 200 passengers ___ the plane.", "В самолёте было 200 пассажиров.", ["on", "in"], "on", "Самолёт, поезд, автобус — on."),
    c("t6-bike", 6, "My son goes to school ___ his bike.", "Мой сын ездит в школу на велосипеде.", ["on", "in", "by"], "on",
      "На своём велосипеде — on his bike (или by bike, без his)."),
    c("t6-out", 6, "Get ___ of the car, please.", "Выйдите из машины, пожалуйста.", ["out", "off"], "out", "Из машины — get out of. Из автобуса — get off."),
    c("t6-off", 6, "We need to get ___ at the next stop.", "Нам выходить на следующей остановке.", ["off", "out"], "off", "Из автобуса — get off."),

    # 7 · тонкости
    c("t7-comein", 7, "Come ___, please — the door is open.", "Входите, пожалуйста, — дверь открыта.", ["in", "into"], "in",
      "После предлога нет существительного — только in: Come in!"),
    c("t7-getin", 7, "Get ___ — I'll drive you home.", "Садись — я отвезу тебя домой.", ["in", "into"], "in", "Без существительного — in: Get in!"),
    c("t7-hold", 7, "Hold ___! I'm coming.", "Подожди! Я иду.", ["on", "onto"], "on", "Без существительного — on: Hold on!"),
    c("t7-moveon", 7, "Let's move ___ the next patient.", "Переходим к следующему пациенту.", ["on to", "onto"], "on to",
      "move on (продолжать) + to — два слова. Onto здесь значило бы «залезть на пациента»."),

    # 8 · в больнице
    c("h8-hospital", 8, "My father has been ___ hospital for a week.", "Отец уже неделю в больнице.", ["in", "into"], "in", "Где? — in hospital (британский вариант)."),
    c("h8-icu", 8, "He's ___ intensive care.", "Он в реанимации.", ["in", "on", "into"], "in", "В реанимации — in intensive care."),
    c("h8-drip", 8, "The patient is ___ a drip.", "Пациент под капельницей.", ["on", "in"], "on", "Под капельницей — on a drip."),
    c("h8-meds", 8, "She's ___ medication for high blood pressure.", "Она принимает препараты от давления.", ["on", "in"], "on",
      "Принимать лекарства — be on medication."),
    c("h8-vein", 8, "The contrast is injected ___ a vein in the arm.", "Контраст вводят в вену на руке.", ["into", "onto"], "into", "Ввести в вену — inject into."),
    c("h8-side", 8, "Roll the patient ___ his side.", "Поверните пациента на бок.", ["onto", "into"], "onto", "Повернуть на бок — onto: на поверхность, а не внутрь."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
