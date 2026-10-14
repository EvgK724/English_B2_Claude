# Содержание тренажёра «Do without и похожие»: с карточки урока (Vocabulary Focus: do without — «When you do without something,
# you manage, work, or perform successfully without having it»: There are a great number of things that we can do without.
# Can people do without money?) и похожее — как ещё сказать «обойтись без» (go without, can't live without, manage without,
# make do, get by) и фразы с do, которые с ними путают (could do with, do away with, dispense with, have to do with).
# Отличие от соседей: в «Manage to и похожие» (manage) — справиться с делом (manage to, cope with, get by — по карточке),
# в «Фразах с go» — одна карточка на go without; здесь — всё про «обойтись без» вместе.
# Разметка в примерах: [фраза|a] — обойтись без (оранжевый), [фраза|b] — нужно, хочется (синий),
# [фраза|c] — другие фразы с do (зелёный). Реплики «— …? — …» озвучивают два голоса. Темы с полем late вступают позже.

MIXED_TOPIC = 9

GROUPS = {
    "b1": "B1 — do without, go without, can't live without",
    "b1p": "B1+ — make do, get by, could do with",
    "b2": "B2 — do away with, dispense with, have to do with",
    "mix": "Итог",
}

# Главная таблица: образец | правило («главное — пояснение») | примеры
TABLE = [
    ["do without", "обойтись без — и справиться", "can do without a car · we'll have to do without"],
    ["go without", "остаться без нужного — лишения", "go without sleep · go without food"],
    ["manage without · can't live without", "справиться без · жить не могу без", "manage without help · can't live without music"],
    ["make do (with)", "обойтись тем, что есть", "make do with a scarf · we'll make do"],
    ["get by (on, in)", "свести концы с концами, объясниться", "get by on a pension · get by in Spanish"],
    ["could do with", "не помешало бы — наоборот, нужно", "could do with a coffee"],
    ["do away with · dispense with", "убрать насовсем, отменить", "did away with paper records"],
    ["have to do with", "связано с; nothing to do with — ни при чём", "has nothing to do with age"],
]

# Мини-диалоги: строки [английский, перевод]; реплики «— » говорят два голоса
CONTRAST = [
    [["— Can you [do without|a] the car this week?", "Обойдёшься без машины на этой неделе?"],
     ["— Sure, I'll take the bus.", "Конечно, поеду на автобусе."]],
    [["— How are you [getting by|a] on your pension?", "Как вы живёте на пенсию?"],
     ["— It's tight, but we [make do|a].", "Впритык, но как-то обходимся."]],
    [["— You look shattered.", "Ты выглядишь вымотанным."],
     ["— I [could do with|b] a holiday.", "Отпуск бы мне не помешал."]],
    [["— Did he eat anything?", "Он что-нибудь ел?"],
     ["— No, he [went without|a] food all day.", "Нет, весь день ничего не ел."]],
    [["— Is the cough anything [to do with|c] the new tablets?", "Кашель не из-за новых таблеток?"],
     ["— No, it [has nothing to do with|c] them.", "Нет, они тут ни при чём."]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["We can do without of sugar.", "We can do without sugar.", "без of: do without + существительное"],
    ["We can do with no car.", "We can do without a car.", "обойтись без — do without"],
    ["There are many things we can do without them.", "There are many things we can do without.", "дополнение уже есть — things"],
    ["I could do without a coffee.", "I could do with a coffee.", "хочется — could do with"],
    ["We'll make it with what we have.", "We'll make do with what we have.", "обойтись тем, что есть — make do"],
    ["It's hard to get by with a small salary.", "It's hard to get by on a small salary.", "деньги — get by on"],
    ["They did away paper records.", "They did away with paper records.", "do away with — с with"],
    ["Let's dispense the formalities.", "Let's dispense with the formalities.", "dispense with — с with"],
    ["It has nothing with age.", "It has nothing to do with age.", "have nothing to do with"],
    ["He went without to sleep.", "He went without sleep.", "go without + существительное"],
]

TOPICS = [
    {"n": 1, "group": "b1", "title": "do without", "sub": "обойтись без — и справиться",
     "rule": "Do without something — обойтись без чего-то и при этом справиться: We can do without a car. Без дополнения do without ставят в конце: There's no milk, so we'll have to do without. С can — «можно и без этого»: There are a great number of things that we can do without (пример из урока: дополнение things уже есть, them не нужно). Can't do without — «без этого никак»: I can't do without my phone. После without — сразу существительное, без of.",
     "ex": [
         {"en": "There are a great number of things that we can [do without|a].", "ru": "Есть очень много вещей, без которых можно обойтись."},
         {"en": "Can people [do without|a] money?", "ru": "Могут ли люди обходиться без денег?"},
         {"en": "We've run out of milk, so we'll have to [do without|a].", "ru": "Молоко кончилось — придётся обойтись без него."},
     ]},
    {"n": 2, "group": "b1", "title": "go without", "sub": "остаться без нужного",
     "rule": "Go without — остаться без нужного, обычно вынужденно и тяжело: go without food, go without sleep. Do without — спокойно обойтись: We can do without a TV. Go without — лишения: Many families go without heating in winter. Часто с for + время: He went without sleep for two days. Без дополнения тоже в конце: If there isn't enough food, the parents go without.",
     "ex": [
         {"en": "He [went without|a] sleep for two days.", "ru": "Он два дня не спал."},
         {"en": "Many families [go without|a] heating in winter.", "ru": "Многие семьи зимой сидят без отопления."},
         {"en": "If there isn't enough food, the parents [go without|a].", "ru": "Если еды не хватает, родители остаются голодными."},
     ]},
    {"n": 3, "group": "b1", "title": "manage without, can't live without", "sub": "справиться без, жить не могу без",
     "rule": "Manage without — справиться без помощи или вещи: Can you manage without the stick? Cope without — выдержать без: How do they cope without electricity? А cope with — справляться с трудностью: cope with night shifts. Can't live without — «жить не могу без» (с чувством): I can't live without music. Survive on — прожить на: survive on very little money. Сравни: can't do without — без этого никак по делу, can't live without — очень люблю.",
     "ex": [
         {"en": "I [can't live without|a] music.", "ru": "Я не могу жить без музыки."},
         {"en": "— Can you [manage without|a] the walker? — Yes, I think so.", "ru": "— Справитесь без ходунков? — Да, думаю, да."},
         {"en": "How do they [cope without|a] electricity?", "ru": "Как они обходятся без электричества?"},
     ]},
    {"n": 4, "group": "b1p", "title": "make do", "sub": "обойтись тем, что есть", "late": 0.2,
     "rule": "Make do — обойтись тем, что есть, хотя хотелось бы лучшего. Make do with + то, чем заменяем: There was no bandage, so we made do with a scarf. Make do without + то, чего нет: make do without a proper kitchen. Без дополнения: It's not ideal, but we'll make do. Не путать с make it — успеть, добраться, получиться: We'll never make it on time.",
     "ex": [
         {"en": "There was no splint, so we [made do with|a] a rolled-up magazine.", "ru": "Шины не было — обошлись свёрнутым журналом."},
         {"en": "It's not ideal, but we'll [make do|a].", "ru": "Не идеально, но обойдёмся."},
         {"en": "We had to [make do without|a] a proper kitchen for a month.", "ru": "Месяц пришлось обходиться без нормальной кухни."},
     ]},
    {"n": 5, "group": "b1p", "title": "get by", "sub": "свести концы с концами", "late": 0.2,
     "rule": "Get by — справляться с трудом, хватает впритык. Get by on + деньги: It's hard to get by on a nurse's salary. Get by in + язык — объясниться на минимальном уровне: I can get by in Spanish. Get by with — обойтись чем-то: We get by with one car. Близко к make do, но get by — о жизни и деньгах в целом: How are you getting by? — Как справляетесь?",
     "ex": [
         {"en": "It's hard to [get by|a] on a nurse's salary.", "ru": "На зарплату медсестры прожить трудно."},
         {"en": "I can [get by|a] in Spanish, but I'm not fluent.", "ru": "По-испански я объяснюсь, но свободно не говорю."},
         {"en": "We [get by|a] with one car.", "ru": "Нам хватает одной машины."},
     ]},
    {"n": 6, "group": "b1p", "title": "could do with", "sub": "не помешало бы", "late": 0.25,
     "rule": "Could do with — «не помешало бы, хочется»: I could do with a coffee. The ward could do with more nurses. Это противоположность do without: can do without — можно и без этого, could do with — нужно. Мягче, чем need: You could do with some rest. Предложить помощь: Could you do with some help? — Вам помочь? После could do with — существительное: a coffee, some help, a coat of paint.",
     "ex": [
         {"en": "I [could do with|b] a coffee.", "ru": "Кофе бы сейчас не помешал."},
         {"en": "The ward [could do with|b] two more nurses.", "ru": "Отделению не помешали бы ещё две медсестры."},
         {"en": "We can [do without|a] the meeting, but we [could do with|b] more time.", "ru": "Без совещания обойдёмся, а вот времени бы побольше."},
     ]},
    {"n": 7, "group": "b2", "title": "do away with, dispense with", "sub": "убрать насовсем, отменить", "late": 0.45,
     "rule": "Do away with — избавиться, отменить насовсем (правило, систему, вещь): The hospital did away with paper records. Dispense with — обойтись без, отказаться (книжно): Let's dispense with the formalities — давайте без формальностей; dispense with the need for a biopsy — избавить от необходимости в биопсии. Get rid of — разговорное «избавиться»: get rid of old equipment. Do without — временно, do away with — насовсем.",
     "ex": [
         {"en": "The hospital [did away with|c] paper records in 2020.", "ru": "В 2020 году больница отказалась от бумажных карт."},
         {"en": "Let's [dispense with|c] the formalities.", "ru": "Давайте без формальностей."},
         {"en": "We should [get rid of|c] this old equipment.", "ru": "Пора избавиться от этого старого оборудования."},
     ]},
    {"n": 8, "group": "b2", "title": "have to do with", "sub": "связано с, ни при чём", "late": 0.5,
     "rule": "Have something to do with — быть связанным с: Your headaches have something to do with your blood pressure. Have nothing to do with — не иметь отношения: It has nothing to do with age. Have a lot to do with — во многом зависит. В вопросе — anything: Does it have anything to do with the new drug? What does that have to do with me? — А я тут при чём? Не путать с have to do — «надо сделать»: I have to do the paperwork.",
     "ex": [
         {"en": "Your headaches probably [have something to do with|c] your blood pressure.", "ru": "Головные боли, скорее всего, связаны с давлением."},
         {"en": "It [has nothing to do with|c] age.", "ru": "Возраст тут ни при чём."},
         {"en": "What does that [have to do with|c] me?", "ru": "А я тут при чём?"},
     ]},
    {"n": 9, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None, say=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    if say: d["say"] = say
    return d

CARDS = [
    # 1 · do without
    c("w1-money", 1, "Can people ___ money?", "Могут ли люди обходиться без денег?",
      ["do without", "do with", "go with"], "do without", "Обойтись без — do without + существительное."),
    c("w1-end", 1, "There's no sugar left, so you'll have to ___.", "Сахар кончился — придётся обойтись без него.",
      ["do without", "do with", "do away"], "do without", "Без дополнения do without ставят в конце фразы."),
    c("w1-coffee", 1, "I can't ___ my morning coffee.", "Не могу без утреннего кофе.",
      ["do without", "do with", "do away with"], "do without", "Can't do without — без этого никак."),
    c("w1-things", 1, "There are many things that we can ___.", "Есть много вещей, без которых можно обойтись.",
      ["do without", "do without them", "do with"], "do without", "Дополнение уже есть — things; do without them — лишнее them."),
    c("w1-car", 1, "Living in the city centre, we can easily ___ a car.", "Мы живём в центре и легко обходимся без машины.",
      ["do without", "do with", "go with"], "do without", "Спокойно обходиться без — do without."),
    c("w1-interpreter", 1, "We can't ___ an interpreter — the patient speaks only Arabic.", "Без переводчика не обойтись: пациент говорит только по-арабски.",
      ["do without", "do with", "deal without"], "do without", "Can't do without — без этого никак, нужно."),

    # 2 · go without
    c("w2-sleep", 2, "During the exams she ___ sleep for two nights.", "Во время сессии она две ночи не спала.",
      ["went without", "did away with", "made do"], "went without", "Остаться без сна — go without: went without sleep."),
    c("w2-food", 2, "No one should have to ___ food.", "Никто не должен голодать.",
      ["go without", "do away with", "make do"], "go without", "Остаться без нужного — go without."),
    c("w2-meds", 2, "Some patients ___ their medication because they can't afford it.", "Некоторые пациенты не принимают лекарства, потому что не могут их купить.",
      ["go without", "do away with", "get by"], "go without", "Вынужденно остаться без — go without."),
    c("w2-tv", 2, "We never watch it anyway — we can easily ___ a TV.", "Мы его всё равно не смотрим — легко обойдёмся без телевизора.",
      ["do without", "go without"], "do without", "Спокойно, без лишений — do without.",
      also={"go without": "тоже скажут, но go without — о лишениях; спокойное «обойдёмся» — do without"}),
    c("w2-parents", 2, "When money was short, the parents ___ so the children could eat.", "Когда денег не хватало, родители недоедали, чтобы накормить детей.",
      ["went without", "did away", "got by with"], "went without", "Без дополнения в конце: the parents went without."),
    c("w2-water", 2, "After the flood, the village went ___ clean water for a week.", "После наводнения деревня неделю сидела без чистой воды.",
      ["without", "with", "out"], "without", "Go without + существительное."),

    # 3 · manage without, can't live without
    c("w3-music", 3, "I ___ music — it's on all day.", "Жить не могу без музыки — она играет весь день.",
      ["can't live without", "can't live with", "live without"], "can't live without", "Can't live without — «жить не могу без»."),
    c("w3-stick", 3, "Can you ___ the stick, or do you still need it?", "Справитесь без трости или она ещё нужна?",
      ["manage without", "manage out", "manage off"], "manage without", "Справиться без — manage without."),
    c("w3-air", 3, "How do people ___ air conditioning in this heat?", "Как люди обходятся без кондиционера в такую жару?",
      ["cope without", "cope with", "cope no"], "cope without", "Cope without — выдержать без. Cope with — справляться с трудностью."),
    c("w3-nights", 3, "She's finding it hard to ___ the night shifts.", "Ей тяжело даются ночные смены.",
      ["cope with", "cope without", "do without"], "cope with", "Справляться с трудностью — cope with."),
    c("w3-survive", 3, "They ___ less than ten dollars a day.", "Они живут меньше чем на десять долларов в день.",
      ["survive on", "survive with", "survive without"], "survive on", "Прожить на сумму — survive on."),
    c("w3-help", 3, "He's 92 but still ___ any help at home.", "Ему 92, но он до сих пор справляется дома без посторонней помощи.",
      ["manages without", "goes with", "does with"], "manages without", "Справляться без — manages without."),

    # 4 · make do
    c("w4-splint", 4, "There was no splint, so we made ___ a rolled-up magazine.", "Шины не было — обошлись свёрнутым журналом.",
      ["do with", "do without", "it with"], "do with", "Make do with — обойтись тем, что есть."),
    c("w4-ideal", 4, "It's not ideal, but we'll make ___.", "Не идеально, но обойдёмся.",
      ["do", "done", "doing"], "do", "Без дополнения — we'll make do."),
    c("w4-kitchen", 4, "During the renovation we had to make do ___ a proper kitchen.", "Пока шёл ремонт, приходилось обходиться без нормальной кухни.",
      ["without", "with", "of"], "without", "Make do without + то, чего нет."),
    c("w4-old", 4, "We can't afford a new ultrasound machine, so we'll have to ___ the old one.", "Новый аппарат УЗИ нам не по карману — придётся обходиться старым.",
      ["make do with", "make do without", "make with"], "make do with", "Make do with + то, чем пользуемся вместо лучшего."),
    c("w4-makeit", 4, "Hurry up — we'll never ___ to the station on time!", "Поторопись — ни за что не успеем на вокзал!",
      ["make it", "make do", "do it"], "make it", "Успеть, добраться — make it. Make do — обойтись тем, что есть."),
    c("w4-chair", 4, "We've only got one wheelchair, so we'll have to ___.", "Кресло-каталка у нас одно — придётся как-то обойтись.",
      ["make do", "make it", "do away"], "make do", "Обойтись тем, что есть — make do."),

    # 5 · get by
    c("w5-grant", 5, "Students often struggle to get ___ on their grants.", "Студентам часто трудно прожить на стипендию.",
      ["by", "through", "over"], "by", "Свести концы с концами — get by."),
    c("w5-month", 5, "How do they get by ___ a thousand pounds a month?", "Как они живут на тысячу фунтов в месяц?",
      ["on", "with", "by"], "on", "Get by on + сумма."),
    c("w5-spanish", 5, "I'm not fluent, but I can get by ___ Spanish.", "Свободно не говорю, но по-испански объяснюсь.",
      ["in", "on", "with"], "in", "Объясниться на языке — get by in."),
    c("w5-onecar", 5, "We don't need a second car — we get by ___ one.", "Вторая машина нам не нужна — хватает одной.",
      ["with", "on", "without"], "with", "Обходиться чем-то — get by with."),
    c("w5-pension", 5, "My grandmother just ___ on her pension.", "Бабушка еле сводит концы с концами на пенсию.",
      ["gets by", "gets over", "gets through"], "gets by", "Get by on — прожить на. Get over — пережить, оправиться."),
    c("w5-managing", 5, "— How are you managing since the operation? — We're getting ___, thanks.", "— Как вы справляетесь после операции? — Потихоньку, спасибо.",
      ["by", "away", "off"], "by", "We're getting by — справляемся потихоньку."),

    # 6 · could do with
    c("w6-coffee", 6, "I'm exhausted — I could ___ a strong coffee.", "Я вымотан — крепкий кофе бы не помешал.",
      ["do with", "do without", "make do"], "do with", "Хочется, не помешало бы — could do with."),
    c("w6-ward", 6, "The ward could do ___ two more nurses.", "Отделению не помешали бы ещё две медсестры.",
      ["with", "without", "by"], "with", "Нужно — could do with."),
    c("w6-rest", 6, "You look tired. You could ___ a few days off.", "Ты выглядишь усталым. Пара выходных тебе бы не помешала.",
      ["do with", "go without", "get by"], "do with", "Мягкое «тебе нужно» — you could do with."),
    c("w6-paperwork", 6, "We can ___ the extra paperwork — it only slows us down.", "Без лишней бумажной работы обойдёмся — она только тормозит.",
      ["do without", "do with", "could do with"], "do without", "Можно и без этого — can do without."),
    c("w6-paint", 6, "This room could do with ___.", "Эту комнату не мешало бы покрасить.",
      ["a coat of paint", "to paint", "paint it"], "a coat of paint", "Could do with + существительное: a coat of paint, some help."),
    c("w6-help", 6, "— ___ some help with that? — Yes, please.", "— Вам помочь? — Да, пожалуйста.",
      ["Could you do with", "Could you do without", "Can you do with"], "Could you do with",
      "Предложить помощь — Could you do with some help?"),

    # 7 · do away with, dispense with
    c("w7-paper", 7, "In 2020 the hospital did ___ with paper records.", "В 2020 году больница отказалась от бумажных карт.",
      ["away", "without", "out"], "away", "Отменить насовсем — do away with."),
    c("w7-formal", 7, "Let's ___ the formalities and start the meeting.", "Давайте без формальностей — начинаем совещание.",
      ["dispense with", "dispense of", "do without of"], "dispense with", "Dispense with — обойтись без (книжно)."),
    c("w7-rule", 7, "Many staff want to ___ the old dress code.", "Многие сотрудники хотят отменить старый дресс-код.",
      ["do away with", "do without", "make do with"], "do away with", "Отменить правило — do away with."),
    c("w7-rid", 7, "We need to get ___ of this broken equipment.", "Надо избавиться от этого сломанного оборудования.",
      ["rid", "away", "out"], "rid", "Избавиться — get rid of."),
    c("w7-need", 7, "The new test may dispense with the need ___ a biopsy.", "Новый тест, возможно, избавит от необходимости в биопсии.",
      ["for", "of", "with"], "for", "The need for — необходимость в: dispense with the need for."),
    c("w7-lift", 7, "We'll ___ the lift until the repairs are finished.", "Пока идёт ремонт, обойдёмся без лифта.",
      ["do without", "do away with", "dispense"], "do without", "Временно обходиться — do without; do away with — убрать насовсем."),

    # 8 · have to do with
    c("w8-bp", 8, "Your headaches probably have something to do ___ your blood pressure.", "Головные боли, скорее всего, связаны с давлением.",
      ["with", "without", "about"], "with", "Быть связанным с — have something to do with."),
    c("w8-age", 8, "At forty, memory problems usually have ___ to do with age.", "В сорок лет проблемы с памятью обычно с возрастом не связаны.",
      ["nothing", "no", "anything"], "nothing", "Не иметь отношения — have nothing to do with."),
    c("w8-me", 8, "What does that have to do ___ me?", "А я тут при чём?",
      ["with", "to", "for"], "with", "What does that have to do with me?"),
    c("w8-lot", 8, "Recovery has a lot ___ with motivation.", "Выздоровление во многом зависит от мотивации.",
      ["to do", "do", "doing"], "to do", "Have a lot to do with — во многом связано с."),
    c("w8-haveto", 8, "Sorry, I can't stay — I have to ___ the discharge papers.", "Извините, не могу остаться — надо оформить выписку.",
      ["do", "do with", "do without"], "do", "Have to do — «надо сделать». Have to do with — «связано с»."),
    c("w8-rash", 8, "Does the rash have ___ to do with the new drug?", "Сыпь не связана с новым препаратом?",
      ["anything", "nothing", "something of"], "anything", "В вопросе — anything: Does it have anything to do with…?"),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
    for alt in k.get("also", {}): assert alt in k["opts"] and alt != k["a"], k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))
assert all(t["group"] in GROUPS for t in TOPICS) and [t["n"] for t in TOPICS] == list(range(1, MIXED_TOPIC + 1))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
