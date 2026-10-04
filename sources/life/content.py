# Содержание приложения «life / live»: life, live [lɪv], live [laɪv], alive, living, lively.
# Пометка […] — слово в фокусе (оранжевый).

MIXED_TOPIC = 7

GROUPS = {
    "life": "Жизнь и жить: life, live",
    "alive": "Живой: alive, live, living, lively",
    "med": "В больнице",
    "mix": "Итог",
}

# Как звучит: слово | транскрипция | значение | пример | озвучка (у омографов — только пример)
SOUNDS = [
    ["life", "/laɪf/", "жизнь", "Life is short.", "Life. Life is short."],
    ["lives", "/laɪvz/", "жизни — мн. ч. от life", "Doctors save lives.", "Doctors save lives."],
    ["live", "/lɪv/", "жить — глагол", "I live here.", "I live here."],
    ["lives", "/lɪvz/", "живёт — он, она", "She lives alone.", "She lives alone."],
    ["live", "/laɪv/", "живой, вживую — перед существительным", "live music", "Live music."],
    ["alive", "/əˈlaɪv/", "жив — после глагола", "He's alive.", "Alive. He's alive."],
    ["living", "/ˈlɪvɪŋ/", "живой; заработок", "living things", "Living. Living things."],
    ["lively", "/ˈlaɪvli/", "оживлённый, бойкий", "a lively town", "Lively. A lively town."],
    ["leave", "/liːv/", "уходить, уезжать — не путать с live", "I leave at seven.", "Leave. I leave at seven."],
]

# Выражения: сочетание ([…] — слово семьи) | перевод | пример | озвучка
EXPR = [
    ["save a [life]", "спасти жизнь", "Fast treatment saves lives.", "Save a life. Fast treatment saves lives."],
    ["quality of [life]", "качество жизни", "Rehabilitation improves quality of life.", "Quality of life. Rehabilitation improves quality of life."],
    ["[life] expectancy", "ожидаемая продолжительность жизни", "Smoking reduces life expectancy.", "Life expectancy. Smoking reduces life expectancy."],
    ["[life]-threatening", "угрожающий жизни", "A stroke is a life-threatening condition.", "Life-threatening. A stroke is a life-threatening condition."],
    ["on [life] support", "на аппаратах жизнеобеспечения", "He's on life support.", "On life support. He's on life support."],
    ["[lifestyle]", "образ жизни", "He needs to change his lifestyle.", "Lifestyle. He needs to change his lifestyle."],
    ["[live] on", "жить на (деньги)", "They live on his pension.", "They live on his pension."],
    ["earn a [living]", "зарабатывать на жизнь", "She earns a living as a translator.", "Earn a living. She earns a living as a translator."],
    ["cost of [living]", "стоимость жизни", "The cost of living has gone up.", "Cost of living. The cost of living has gone up."],
    ["come [alive]", "оживать", "The city comes alive at night.", "Come alive. The city comes alive at night."],
    ["[alive] and well", "жив-здоров", "Grandpa is alive and well.", "Alive and well. Grandpa is alive and well."],
    ["a [lively] discussion", "оживлённое обсуждение", "We had a lively discussion.", "A lively discussion. We had a lively discussion."],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["He is still live.", "He is still alive.", "после глагола — alive"],
    ["an alive fish", "a live fish", "перед существительным — live"],
    ["Doctors save lifes.", "Doctors save lives.", "мн. ч. от life — lives"],
    ["I leave in Yekaterinburg.", "I live in Yekaterinburg.", "жить — live [lɪv]; leave [liːv] — уезжать"],
    ["She talked lively.", "She talked in a lively way.", "lively — не наречие"],
    ["The concert was shown alive.", "The concert was shown live.", "в прямом эфире — live [laɪv]"],
    ["I live here all my life.", "I have lived here all my life.", "всю жизнь до сих пор — have lived"],
    ["The life is short.", "Life is short.", "жизнь вообще — без the"],
    ["He makes his live as a driver.", "He makes his living as a driver.", "заработок — living"],
    ["a live-threatening condition", "a life-threatening condition", "угрожающий жизни — life"],
]

TOPICS = [
    {"n": 1, "group": "life", "title": "life — жизнь", "sub": "существительное · lives",
     "rule": "life [laɪf] — жизнь, существительное. Мн. ч. — lives [laɪvz]: Doctors save lives. Lifes — ошибка. Жизнь вообще — без the: Life is short. Конкретная жизнь — с the или my, his: the life of a doctor, my whole life. Образ жизни — lifestyle.",
     "ex": [
         {"en": "[Life] is short.", "ru": "Жизнь коротка."},
         {"en": "Doctors save [lives].", "ru": "Врачи спасают жизни."},
         {"en": "I've lived here all my [life].", "ru": "Я живу здесь всю жизнь."},
     ]},
    {"n": 2, "group": "life", "title": "live [lɪv] — жить", "sub": "глагол · lives · не leave",
     "rule": "live [lɪv] — жить, глагол: I live in Yekaterinburg. Он, она — lives [lɪvz]: She lives alone. live with — жить с кем-то, live on — жить на какие-то деньги: They live on his pension. live a … life — прожить какую-то жизнь: live a healthy life. Всю жизнь до сих пор — Present Perfect: I have lived here all my life. Не путай с leave [liːv] — уходить, уезжать.",
     "ex": [
         {"en": "I [live] in Yekaterinburg.", "ru": "Я живу в Екатеринбурге."},
         {"en": "She [lives] alone.", "ru": "Она живёт одна."},
         {"en": "I [leave] home at seven.", "ru": "Я выхожу из дома в семь (leave — уходить)."},
     ]},
    {"n": 3, "group": "alive", "title": "alive — жив", "sub": "после глагола",
     "rule": "alive [əˈlaɪv] — жив, живой. Ставится после глагола: He's still alive. Is the patient alive? stay alive — остаться в живых, keep someone alive — поддерживать жизнь. Перед существительным alive не ставят: an alive fish — ошибка. Выражения: alive and well — жив-здоров, come alive — оживать.",
     "ex": [
         {"en": "He's still [alive].", "ru": "Он ещё жив."},
         {"en": "Grandpa is [alive] and well.", "ru": "Дедушка жив-здоров."},
         {"en": "The city comes [alive] at night.", "ru": "Ночью город оживает."},
     ]},
    {"n": 4, "group": "alive", "title": "live [laɪv] и living", "sub": "перед существительным · вживую · заработок",
     "rule": "Перед существительным «живой» — live [laɪv] или living: live lobsters, living things, living relatives. live [laɪv] ещё — вживую, в прямом эфире: live music, watch the match live. living — ещё и заработок: earn a living, What do you do for a living? Стоимость жизни — the cost of living.",
     "ex": [
         {"en": "I love [live] music.", "ru": "Я люблю живую музыку."},
         {"en": "We watched the match [live].", "ru": "Мы смотрели матч в прямом эфире."},
         {"en": "She earns a [living] as a translator.", "ru": "Она зарабатывает на жизнь переводами."},
     ]},
    {"n": 5, "group": "alive", "title": "lively — оживлённый", "sub": "бойкий, энергичный · не наречие",
     "rule": "lively [ˈlaɪvli] — оживлённый, бойкий, энергичный: a lively discussion, a lively child, a lively town. Это прилагательное, хоть и на -ly. Наречия нет: не talk lively, а talk in a lively way. Не путай: lively — полный энергии, alive — не умер.",
     "ex": [
         {"en": "We had a [lively] discussion.", "ru": "У нас было оживлённое обсуждение."},
         {"en": "She's a [lively] child.", "ru": "Она бойкий ребёнок."},
         {"en": "It's a [lively] town.", "ru": "Это оживлённый город."},
     ]},
    {"n": 6, "group": "med", "title": "В больнице", "sub": "life-threatening · life support",
     "rule": "life-threatening — угрожающий жизни, life-saving — спасающий жизнь, life support — жизнеобеспечение (on life support — на аппаратах), life expectancy — ожидаемая продолжительность жизни, quality of life — качество жизни. save someone's life — спасти жизнь, keep someone alive — поддерживать жизнь.",
     "ex": [
         {"en": "A stroke is [life]-threatening.", "ru": "Инсульт угрожает жизни."},
         {"en": "He's on [life] support.", "ru": "Он на аппаратах жизнеобеспечения."},
         {"en": "Fast treatment saves [lives].", "ru": "Быстрое лечение спасает жизни."},
     ]},
    {"n": 7, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · life — жизнь
    c("l1-short", 1, "___ is too short to worry about small things.", "Жизнь слишком коротка, чтобы переживать из-за мелочей.", ["Life", "Live", "Alive"], "Life",
      "Жизнь — life, существительное. Жизнь вообще — без the."),
    c("l1-lives", 1, "Fast treatment saves ___.", "Быстрое лечение спасает жизни.", ["lives", "lifes"], "lives", "Мн. ч. от life — lives [laɪvz]. Lifes — ошибка."),
    c("l1-whole", 1, "I've lived here my whole ___.", "Я живу здесь всю жизнь.", ["life", "live", "living"], "life", "Вся жизнь — my whole life, all my life."),
    c("l1-quality", 1, "Rehabilitation improves quality of ___.", "Реабилитация улучшает качество жизни.", ["life", "live"], "life", "Качество жизни — quality of life."),
    c("l1-the", 1, "___ of a doctor is never boring.", "Жизнь врача никогда не бывает скучной.", ["The life", "Life"], "The life",
      "Конкретная жизнь — с the: the life of a doctor."),
    c("l1-lifestyle", 1, "He needs to change his ___ — less salt and more exercise.", "Ему нужно изменить образ жизни — меньше соли и больше движения.",
      ["lifestyle", "livestyle", "living style"], "lifestyle", "Образ жизни — lifestyle."),

    # 2 · live [lɪv] — жить
    c("l2-where", 2, "Where do you ___?", "Где вы живёте?", ["live", "life", "leave"], "live", "Жить — live [lɪv]. Leave [liːv] — уходить, уезжать."),
    c("l2-alone", 2, "My mother ___ alone.", "Мама живёт одна.", ["lives", "lifes", "live"], "lives", "Он, она — lives [lɪvz]."),
    c("l2-leave", 2, "I ___ home at seven every morning.", "Я выхожу из дома в семь каждое утро.", ["leave", "live"], "leave",
      "Уходить — leave [liːv], долгий звук. Жить — live [lɪv], короткий."),
    c("l2-pension", 2, "They ___ on his pension.", "Они живут на его пенсию.", ["live", "life", "alive"], "live", "Жить на какие-то деньги — live on."),
    c("l2-perfect", 2, "I ___ in this city all my life.", "Я всю жизнь живу в этом городе.", ["have lived", "live", "am living"], "have lived",
      "С прошлого до сих пор — Present Perfect: I have lived."),
    c("l2-healthy", 2, "Stop smoking if you want to ___ a long and healthy life.", "Брось курить, если хочешь прожить долгую и здоровую жизнь.",
      ["live", "life", "lively"], "live", "Прожить жизнь — live a life."),

    # 3 · alive — жив
    c("l3-still", 3, "The patient is still ___.", "Пациент ещё жив.", ["alive", "live", "life"], "alive", "После глагола (is) — alive."),
    c("l3-keep", 3, "The machines kept him ___ for two weeks.", "Аппараты поддерживали в нём жизнь две недели.", ["alive", "live", "living"], "alive",
      "Поддерживать жизнь — keep someone alive."),
    c("l3-stay", 3, "You need water to stay ___.", "Чтобы остаться в живых, нужна вода.", ["alive", "live", "life"], "alive", "Остаться в живых — stay alive."),
    c("l3-well", 3, "Grandpa is ___ and well — he's 95!", "Дедушка жив-здоров — ему 95!", ["alive", "live", "lively"], "alive", "Жив-здоров — alive and well."),
    c("l3-come", 3, "The city comes ___ at night.", "Ночью город оживает.", ["alive", "live", "lively"], "alive", "Оживать — come alive."),

    # 4 · live [laɪv] и living
    c("l4-lobsters", 4, "They keep ___ lobsters in a tank at the restaurant.", "В ресторане держат живых лобстеров в аквариуме.", ["live", "alive"], "live",
      "Перед существительным — live [laɪv]. Alive — только после глагола."),
    c("l4-music", 4, "Is there ___ music at the restaurant?", "В ресторане есть живая музыка?", ["live", "alive"], "live", "Живая музыка — live music [laɪv]."),
    c("l4-tv", 4, "The match will be shown ___ on TV.", "Матч покажут в прямом эфире.", ["live", "alive"], "live", "В прямом эфире — live [laɪv]."),
    c("l4-things", 4, "Cells are the basic units of all ___ things.", "Клетки — основные единицы всего живого.", ["living", "alive", "lively"], "living",
      "Живые организмы — living things."),
    c("l4-earn", 4, "She earns a ___ as a translator.", "Она зарабатывает на жизнь переводами.", ["living", "life", "live"], "living",
      "Зарабатывать на жизнь — earn a living."),
    c("l4-relatives", 4, "Does he have any ___ relatives?", "У него есть живые родственники?", ["living", "alive", "lively"], "living",
      "Перед существительным — living: living relatives."),
    c("l4-cost", 4, "The cost of ___ keeps going up.", "Стоимость жизни всё растёт.", ["living", "life", "live"], "living", "Стоимость жизни — the cost of living."),

    # 5 · lively — оживлённый
    c("l5-discussion", 5, "We had a ___ discussion about the new guidelines.", "У нас было оживлённое обсуждение новых рекомендаций.",
      ["lively", "alive", "living"], "lively", "Оживлённый, бурный — lively."),
    c("l5-child", 5, "She's a very ___ child — she never sits still.", "Она очень бойкий ребёнок — никогда не сидит на месте.", ["lively", "alive", "live"], "lively",
      "Бойкий, энергичный — lively."),
    c("l5-town", 5, "It's a ___ town with lots of cafés.", "Это оживлённый городок с множеством кафе.", ["lively", "living", "alive"], "lively",
      "Оживлённое место — lively."),
    c("l5-way", 5, "He talked about his trip in a ___ way.", "Он оживлённо рассказывал о поездке.", ["lively", "live", "alive"], "lively",
      "lively — прилагательное. «Оживлённо» — in a lively way."),
    c("l5-injured", 5, "After the accident, he was badly injured but ___.", "После аварии он был тяжело ранен, но жив.", ["alive", "lively", "live"], "alive",
      "Не умер — alive. Lively — полный энергии."),

    # 6 · в больнице
    c("l6-threat", 6, "A stroke is a ___-threatening condition.", "Инсульт — состояние, угрожающее жизни.", ["life", "live", "living"], "life",
      "Угрожающий жизни — life-threatening."),
    c("l6-support", 6, "He's on ___ support in intensive care.", "Он в реанимации на аппаратах жизнеобеспечения.", ["life", "living", "live"], "life",
      "Жизнеобеспечение — life support."),
    c("l6-expectancy", 6, "Smoking reduces ___ expectancy.", "Курение сокращает ожидаемую продолжительность жизни.", ["life", "living", "alive"], "life",
      "Ожидаемая продолжительность жизни — life expectancy."),
    c("l6-saving", 6, "Thrombolysis can be a ___-saving treatment.", "Тромболизис может спасти жизнь.", ["life", "live", "lively"], "life",
      "Спасающий жизнь — life-saving."),
    c("l6-save", 6, "The doctors worked all night to save her ___.", "Врачи всю ночь боролись за её жизнь.", ["life", "live", "alive"], "life",
      "Спасти жизнь — save someone's life."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
