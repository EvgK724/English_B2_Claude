# Содержание приложения «Погода» (English Collocations in Use, Unit 13 Weather).
# Пометка […] — сочетание в фокусе (оранжевый). Примеры свои, не из учебника.

MIXED_TOPIC = 8

GROUPS = {
    "calm": "Солнце, дождь, туман, холод",
    "wind": "Ветер и перемены погоды",
    "storm": "Стихия",
    "mix": "Итог",
}

# «Сильный» и «слабый»: существительное | перевод | сильный | пояснение | слабый | пояснение
STRENGTH = [
    ["rain", "дождь", "heavy", "ливень — torrential", "light", ""],
    ["snow", "снег", "heavy", "", "light", ""],
    ["wind", "ветер", "strong · high", "ледяной — biting", "light", ""],
    ["sun", "солнце", "strong", "", "weak", ""],
    ["fog", "туман", "thick · dense", "", "light", "местами — patches of fog"],
    ["frost", "мороз", "hard", "", "light", "не soft"],
]
# Погода меняется: существительное | перевод | хуже, сильнее | лучше, слабее
CHANGES = [
    ["weather", "погода", "deteriorates · gets worse", "improves · gets better"],
    ["wind", "ветер", "picks up", "dies down"],
    ["fog", "туман", "comes down", "lifts"],
]

# Шпаргалка: сочетание | перевод | пример
SUN = [
    ["unbroken sunshine", "солнце весь день, ни облачка", "We've had unbroken sunshine all week."],
    ["scorching hot", "палящая жара", "It's scorching hot today."],
    ["soak up the sun", "нежиться на солнце", "We lay on the beach, soaking up the sun."],
    ["strong sun ↔ weak sun", "сильное ↔ слабое солнце", "The sun is strongest at midday."],
]
RAIN = [
    ["heavy rain ↔ light rain", "сильный ↔ слабый дождь", "Heavy rain is expected tonight."],
    ["it's pouring (with rain)", "льёт как из ведра", "It's pouring — take an umbrella."],
    ["torrential rain", "ливень", "Torrential rain caused flooding."],
    ["driving rain", "дождь стеной, с ветром", "We walked home through driving rain."],
    ["get soaked", "промокнуть до нитки", "We all got soaked."],
    ["it looks like rain", "похоже, будет дождь", "Take a coat — it looks like rain."],
]
FOG = [
    ["thick cloud", "плотная облачность", "There's thick cloud over the hills."],
    ["a break in the clouds", "просвет в облаках", "The sun came out through a break in the clouds."],
    ["thick fog · dense fog", "густой туман", "Thick fog closed the airport."],
    ["patches of fog", "туман местами", "There are patches of fog on the coast."],
    ["a blanket of fog", "пелена тумана — книжн.", "A blanket of fog covered the city."],
]
COLD = [
    ["freezing cold", "жуткий холод", "It's freezing cold outside."],
    ["heavy snow · fresh snow", "сильный снег · свежий снег", "Heavy snow blocked the roads."],
    ["crisp snow", "свежий хрустящий снег", "The snow was crisp under our feet."],
    ["hard frost ↔ light frost", "сильный ↔ слабый заморозок", "There'll be a hard frost tonight."],
]
WIND = [
    ["strong wind · high winds", "сильный ветер", "High winds are expected on the coast."],
    ["light wind", "слабый ветер", "There was only a light wind."],
    ["a biting wind", "пронизывающий, ледяной ветер", "There's a biting wind today."],
    ["the wind blows · whistles", "дует · свистит", "The wind was whistling through the trees."],
    ["gale-force winds", "штормовой, ураганный ветер", "Gale-force winds hit the coast."],
]
STORM = [
    ["freak weather · freak storms", "аномальная погода, небывалые бури", "Freak storms hit the coast last night."],
    ["cause damage", "нанести ущерб", "The storm caused a lot of damage."],
    ["roofs were torn off", "сорвало крыши", "Several roofs were torn off."],
    ["trees were blown down", "повалило деревья", "Trees and fences were blown down."],
    ["rivers burst their banks", "реки вышли из берегов", "Two rivers burst their banks."],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["It's [raining].", "идёт дождь"], ["It's [pouring].", "льёт как из ведра"]],
    [["I got [wet].", "промок"], ["I got [soaked].", "промок до нитки"]],
    [["The wind [picked up].", "ветер усилился"], ["The wind [died down].", "ветер стих"]],
    [["The fog [came down].", "туман опустился"], ["The fog [lifted].", "туман рассеялся"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["strong rain", "heavy rain", "сильный дождь — heavy"],
    ["It rains strongly.", "It's raining heavily.", "сильно идёт — heavily"],
    ["big snow", "heavy snow", "сильный снег — heavy"],
    ["There's strong fog.", "There's thick fog.", "густой туман — thick или dense"],
    ["a weak wind", "a light wind", "слабый ветер — light"],
    ["a soft frost", "a light frost", "слабый мороз — light"],
    ["We got wet to the bone.", "We got soaked.", "промокнуть до нитки — get soaked"],
    ["It looks like it rains.", "It looks like rain.", "похоже на дождь — looks like rain"],
    ["The river went out of its banks.", "The river burst its banks.", "выйти из берегов — burst its banks"],
    ["The wind tore the roof.", "The wind tore off the roof.", "сорвать — tear off"],
]

TOPICS = [
    {"n": 1, "group": "calm", "title": "Солнце и жара", "sub": "unbroken sunshine, scorching hot, strong sun",
     "rule": "unbroken sunshine — солнце весь день, ни облачка. scorching hot — палящая жара (ещё boiling hot). soak up the sun — нежиться на солнце. Солнце сильное — strong sun, слабое — weak sun; это единственный случай, где «слабый» — weak, а не light.",
     "ex": [
         {"en": "We've had [unbroken sunshine] all week.", "ru": "Всю неделю светит солнце — ни облачка."},
         {"en": "It's [scorching hot] today.", "ru": "Сегодня палящая жара."},
         {"en": "The sun is [strongest] at midday.", "ru": "Солнце сильнее всего в полдень."},
     ]},
    {"n": 2, "group": "calm", "title": "Дождь", "sub": "heavy rain, pouring, torrential, soaked",
     "rule": "Сильный дождь — heavy rain, а не strong rain; идёт сильно — it's raining heavily. Льёт как из ведра — it's pouring (with rain). Ливень — torrential rain. Driving rain — сильный дождь с ветром, бьёт стеной. Слабый — light rain. Промокнуть до нитки — get soaked. Похоже, будет дождь — it looks like rain.",
     "ex": [
         {"en": "It's been [pouring with rain] all day.", "ru": "Весь день льёт как из ведра."},
         {"en": "We all [got soaked].", "ru": "Мы все промокли до нитки."},
         {"en": "Take a coat — it [looks like rain].", "ru": "Возьми куртку — похоже, будет дождь."},
     ]},
    {"n": 3, "group": "calm", "title": "Облака и туман", "sub": "thick fog, patches, a break in the clouds",
     "rule": "Густой туман — thick fog или dense fog, не strong fog. Туман местами — patches of fog; сплошная пелена — a blanket of fog (книжн.). Плотные облака — thick cloud; просвет в облаках — a break in the clouds.",
     "ex": [
         {"en": "There's [thick fog] on the motorway.", "ru": "На трассе густой туман."},
         {"en": "There are [patches of fog] on the coast.", "ru": "На побережье местами туман."},
         {"en": "The sun came out through [a break in the clouds].", "ru": "Солнце выглянуло в просвет между облаками."},
     ]},
    {"n": 4, "group": "calm", "title": "Холод, снег, мороз", "sub": "freezing cold, heavy snow, hard frost",
     "rule": "Жуткий холод — freezing cold. Сильный снег, снегопад — heavy snow; свежий — fresh snow; crisp — свежий и хрустящий: crisp snow, a crisp winter morning. Сильный мороз, заморозок — a hard frost, слабый — a light frost; soft frost — ошибка.",
     "ex": [
         {"en": "It's [freezing cold] outside.", "ru": "На улице жуткий холод."},
         {"en": "[Heavy snow] blocked the roads.", "ru": "Снегопад перекрыл дороги."},
         {"en": "There'll be a [hard frost] tonight.", "ru": "Ночью будут сильные заморозки."},
     ]},
    {"n": 5, "group": "wind", "title": "Ветер", "sub": "strong, high, light, biting; blows, whistles",
     "rule": "Сильный ветер — strong wind или high winds, слабый — light wind. Пронизывающий, ледяной — a biting wind. Ветер дует — the wind blows, свистит — whistles. Штормовой, ураганный — gale-force winds.",
     "ex": [
         {"en": "A [strong wind] is blowing from the north.", "ru": "С севера дует сильный ветер."},
         {"en": "The wind was [whistling] through the trees.", "ru": "Ветер свистел в деревьях."},
         {"en": "[Gale-force winds] hit the coast.", "ru": "На побережье обрушился ураганный ветер."},
     ]},
    {"n": 6, "group": "wind", "title": "Погода меняется", "sub": "improves, deteriorates, picks up, lifts",
     "rule": "Погода улучшается — improves, ухудшается — deteriorates (официально) или gets worse (разговорно). Deteriorate говорят и о пациенте: his condition deteriorated. Ветер усиливается — picks up, стихает — dies down. Туман опускается — comes down, рассеивается — lifts.",
     "ex": [
         {"en": "The weather should [improve] by the weekend.", "ru": "К выходным погода должна улучшиться."},
         {"en": "The wind [picked up] in the evening.", "ru": "Вечером ветер усилился."},
         {"en": "The fog [lifted] by midday.", "ru": "К полудню туман рассеялся."},
     ]},
    {"n": 7, "group": "storm", "title": "Стихия", "sub": "freak storms, damage, burst their banks",
     "rule": "Freak weather — аномальная, небывалая погода: a freak storm. Буря обрушилась — storms hit the coast. Нанести ущерб — cause damage (make damage — калька). Сорвало крыши — roofs were torn off; повалило деревья и заборы — were blown down; здания разрушены — were destroyed. Реки вышли из берегов — rivers burst their banks.",
     "ex": [
         {"en": "[Freak storms] hit the coast last night.", "ru": "Ночью на побережье обрушились небывалые бури."},
         {"en": "Several roofs were [torn off].", "ru": "Сорвало несколько крыш."},
         {"en": "The river [burst its banks].", "ru": "Река вышла из берегов."},
     ]},
    {"n": 8, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · Солнце и жара
    c("w1-unbroken", 1, "We've had ___ sunshine since we arrived — not a single cloud.", "С самого приезда светит солнце — ни облачка.",
      ["unbroken", "whole", "complete"], "unbroken", "Сплошное солнце — unbroken sunshine."),
    c("w1-scorching", 1, "It's ___ hot outside — stay in the shade.", "На улице палящая жара — держитесь в тени.",
      ["scorching", "strong", "heavy"], "scorching", "Очень жарко — scorching hot или boiling hot."),
    c("w1-heat", 1, "During the ___ heat last July, A&E was full of elderly patients with dehydration.", "Во время июльской жары в приёмном было много пожилых с обезвоживанием.",
      ["scorching", "strong", "hard"], "scorching", "Палящая жара — scorching heat."),
    c("w1-soak", 1, "We spent the afternoon on the beach, ___ up the sun.", "Мы провели полдня на пляже, нежась на солнце.",
      ["soaking", "taking", "drinking"], "soaking", "Нежиться на солнце — soak up the sun."),
    c("w1-strong", 1, "Avoid the beach at midday, when the sun is ___.", "Не ходите на пляж в полдень, когда солнце самое сильное.",
      ["strongest", "heaviest", "hardest"], "strongest", "Сильное солнце — strong sun."),
    c("w1-weak", 1, "In winter the sun is too ___ to warm the house.", "Зимой солнце слишком слабое, чтобы прогреть дом.",
      ["weak", "light", "small"], "weak", "Слабое солнце — weak sun. Со всем остальным «слабый» — light."),

    # 2 · Дождь
    c("w2-heavy", 2, "___ rain is expected in the north tonight.", "Сегодня ночью на севере ожидается сильный дождь.",
      ["heavy", "strong", "big"], "heavy", "Сильный дождь — heavy rain. Strong rain — калька."),
    c("w2-heavily", 2, "It rained ___ all day yesterday.", "Вчера весь день шёл сильный дождь.",
      ["heavily", "strongly", "hardly"], "heavily", "Сильно идёт дождь — rain heavily. Hardly — «едва»."),
    c("w2-pouring", 2, "Take an umbrella — it's ___ with rain.", "Возьми зонт — льёт как из ведра.",
      ["pouring", "falling", "going"], "pouring", "Льёт как из ведра — it's pouring (with rain)."),
    c("w2-torrential", 2, "___ rain caused flooding in several villages.", "Проливной дождь вызвал наводнения в нескольких деревнях.",
      ["torrential", "strong", "big"], "torrential", "Ливень — torrential rain."),
    c("w2-driving", 2, "It was hard to see the road through the ___ rain.", "Сквозь стену дождя было трудно разглядеть дорогу.",
      ["driving", "running", "flying"], "driving", "Driving rain — сильный дождь с ветром, бьёт стеной."),
    c("w2-soaked", 2, "We forgot our umbrellas and got ___.", "Мы забыли зонты и промокли до нитки.",
      ["soaked", "washed", "drowned"], "soaked", "Промокнуть до нитки — get soaked."),
    c("w2-looks", 2, "Take a coat — it looks ___ rain.", "Возьми куртку — похоже, будет дождь.",
      ["like", "as", "to"], "like", "Похоже на дождь — it looks like rain."),
    c("w2-light", 2, "It's only ___ rain — we can still go for a walk.", "Дождик слабый — можно погулять.",
      ["light", "weak", "small"], "light", "Слабый дождь — light rain."),

    # 3 · Облака и туман
    c("w3-thick", 3, "The ambulance was delayed by ___ fog on the motorway.", "Скорая задержалась из-за густого тумана на трассе.",
      ["thick", "strong", "big"], "thick", "Густой туман — thick fog или dense fog."),
    c("w3-dense", 3, "___ fog closed the airport for six hours.", "Из-за плотного тумана аэропорт закрыли на шесть часов.",
      ["dense", "strong", "hard"], "dense", "Плотный туман — dense fog."),
    c("w3-patches", 3, "There are ___ of fog on the coast, but they'll clear by lunch.", "На побережье местами туман, но к обеду он рассеется.",
      ["patches", "pieces", "parts"], "patches", "Туман местами — patches of fog."),
    c("w3-blanket", 3, "A thick ___ of fog covered the whole valley.", "Густая пелена тумана накрыла всю долину.",
      ["blanket", "patch", "piece"], "blanket", "Сплошная пелена — a blanket of fog. Patch — небольшой участок."),
    c("w3-cloud", 3, "There's ___ cloud today, so we won't see the eclipse.", "Сегодня плотная облачность, так что затмения не увидим.",
      ["thick", "strong", "hard"], "thick", "Плотные облака — thick cloud."),
    c("w3-break", 3, "We waited for a ___ in the clouds to photograph the mountain.", "Мы ждали просвета в облаках, чтобы сфотографировать гору.",
      ["break", "stop", "pause"], "break", "Просвет в облаках — a break in the clouds."),

    # 4 · Холод, снег, мороз
    c("w4-freezing", 4, "It was ___ cold in the tent at night.", "Ночью в палатке было жутко холодно.",
      ["freezing", "frozen", "strong"], "freezing", "Жуткий холод — freezing cold."),
    c("w4-heavy-snow", 4, "___ snow blocked the roads to the village.", "Сильный снегопад перекрыл дороги к деревне.",
      ["heavy", "strong", "big"], "heavy", "Сильный снег — heavy snow, как и heavy rain."),
    c("w4-crisp", 4, "What a beautiful ___ winter morning!", "Какое чудесное морозное утро!",
      ["crisp", "heavy", "hard"], "crisp", "Свежий, морозный, хрустящий — crisp: crisp snow, a crisp morning."),
    c("w4-hard", 4, "After a ___ frost, we always see more wrist fractures in A&E.", "После сильных заморозков в приёмном всегда больше переломов запястья.",
      ["hard", "strong", "big"], "hard", "Сильный мороз, заморозок — a hard frost."),
    c("w4-light", 4, "Only a ___ frost is expected, so the roads should be fine.", "Ожидаются лишь слабые заморозки, так что с дорогами всё будет в порядке.",
      ["light", "soft", "weak"], "light", "Слабый заморозок — a light frost. Soft frost — ошибка."),

    # 5 · Ветер
    c("w5-strong", 5, "A ___ wind is blowing from the north.", "С севера дует сильный ветер.",
      ["strong", "heavy", "hard"], "strong", "Сильный ветер — strong wind. Heavy — для дождя и снега."),
    c("w5-high", 5, "___ winds are expected on the coast tonight.", "Ночью на побережье ожидается сильный ветер.",
      ["high", "tall", "heavy"], "high", "Сильный ветер в прогнозе — high winds."),
    c("w5-light", 5, "There was only a ___ wind — perfect for a picnic.", "Ветер был слабый — идеально для пикника.",
      ["light", "weak", "small"], "light", "Слабый ветер — light wind."),
    c("w5-biting", 5, "Wear a hat — there's a ___ wind today.", "Надень шапку — сегодня пронизывающий ветер.",
      ["biting", "hitting", "eating"], "biting", "Пронизывающий, ледяной ветер — a biting wind."),
    c("w5-whistling", 5, "We could hear the wind ___ through the trees.", "Было слышно, как ветер свистит в деревьях.",
      ["whistling", "shouting", "speaking"], "whistling", "Ветер свистит — the wind whistles."),
    c("w5-blows", 5, "Here the wind usually ___ from the west.", "Здесь ветер обычно дует с запада.",
      ["blows", "goes", "walks"], "blows", "Ветер дует — the wind blows."),
    c("w5-gale", 5, "___ winds of up to 120 km/h hit the coast.", "На побережье обрушился ураганный ветер — до 120 км/ч.",
      ["gale-force", "hard-force", "big-power"], "gale-force", "Штормовой, ураганный ветер — gale-force winds."),

    # 6 · Погода меняется
    c("w6-improve", 6, "The forecast says the weather will ___ by the weekend.", "По прогнозу к выходным погода улучшится.",
      ["improve", "better", "grow"], "improve", "Погода улучшается — improves или gets better."),
    c("w6-deteriorate", 6, "The weather is expected to ___ later today, with storms in the evening.", "Ожидается, что днём погода испортится, а вечером будут грозы.",
      ["deteriorate", "decrease", "fall"], "deteriorate", "Портится — deteriorates (офиц.) или gets worse. Так же о пациенте: his condition deteriorated."),
    c("w6-worse", 6, "Take a coat — the weather is getting ___.", "Возьми куртку — погода портится.",
      ["worse", "worst", "badder"], "worse", "Портится — is getting worse."),
    c("w6-picks", 6, "The wind usually ___ up in the afternoon.", "После обеда ветер обычно усиливается.",
      ["picks", "takes", "goes"], "picks", "Ветер усиливается — the wind picks up."),
    c("w6-dies", 6, "Let's wait until the wind ___ down.", "Давай подождём, пока ветер стихнет.",
      ["dies", "falls", "sits"], "dies", "Ветер стихает — the wind dies down."),
    c("w6-lifts", 6, "The fog usually ___ by midday.", "Туман обычно рассеивается к полудню.",
      ["lifts", "opens", "goes up"], "lifts", "Туман рассеивается — the fog lifts."),
    c("w6-comes", 6, "In the mountains the mist ___ down very quickly.", "В горах туман опускается очень быстро.",
      ["comes", "sits", "goes"], "comes", "Туман опускается — fog or mist comes down."),

    # 7 · Стихия
    c("w7-freak", 7, "A ___ storm is a very unusual, unexpected one.", "Freak storm — очень необычная, неожиданная буря.",
      ["freak", "hard", "heavy"], "freak", "Аномальная, небывалая — freak: freak weather, a freak storm."),
    c("w7-hit", 7, "Severe storms ___ the south coast last night.", "Прошлой ночью на южное побережье обрушились сильные бури.",
      ["hit", "touched", "met"], "hit", "Обрушиться — hit: storms hit the coast."),
    c("w7-damage", 7, "The storm ___ a lot of damage to property.", "Буря нанесла большой ущерб имуществу.",
      ["caused", "made", "gave"], "caused", "Нанести ущерб — cause damage. Make damage — калька."),
    c("w7-roofs", 7, "Several roofs were torn ___ by the wind.", "Ветром сорвало несколько крыш.",
      ["off", "out", "up"], "off", "Сорвать — tear off: roofs were torn off."),
    c("w7-fences", 7, "Trees and fences were blown ___ in the storm.", "Во время бури повалило деревья и заборы.",
      ["down", "off", "out"], "down", "Повалить ветром — blow down."),
    c("w7-banks", 7, "After days of heavy rain, the river burst its ___.", "После нескольких дней сильных дождей река вышла из берегов.",
      ["banks", "shores", "coasts"], "banks", "Берег реки — bank: burst its banks."),
    c("w7-burst", 7, "Several rivers ___ their banks.", "Несколько рек вышли из берегов.",
      ["burst", "left", "went out of"], "burst", "Выйти из берегов — burst their banks. Went out of — калька."),
    c("w7-destroyed", 7, "A number of buildings were ___ by the storm.", "Буря разрушила несколько зданий.",
      ["destroyed", "broken", "injured"], "destroyed", "Разрушить здание — destroy. Injure — только о людях."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
    for o, note in (k.get("also") or {}).items():
        assert o in k["opts"] and o != k["a"] and "тоже" not in note, k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()),
          "sheet", sum(len(x) for x in (SUN, RAIN, FOG, COLD, WIND, STORM)))
