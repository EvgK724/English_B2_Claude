# Содержание приложения «must / have to / should».
# Пометка […] — модальный глагол; цвет по глаголу: must — оранжевый, have to — синий, should — зелёный, прочие подчёркнуты.

MIXED_TOPIC = 8

GROUPS = {
    "core": "Совет, обязанность, запрет",
    "time": "Прошлое, будущее, догадка",
    "med": "В больнице",
    "mix": "Итог",
}

# Главная таблица: глагол | утверждение | отрицание | отрицательная форма
TABLE = [
    ["must", "обязательно — так решил я или гласит инструкция", "нельзя!", "mustn't"],
    ["have to", "надо — так требуют правила и обстоятельства", "не нужно, можно не делать", "don't have to"],
    ["should", "стоит, лучше бы — совет", "не стоит", "shouldn't"],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["You [mustn't] take it with alcohol.", "нельзя"], ["You [don't have to] take it with food.", "не обязательно"], ["You [shouldn't] take it late at night.", "не стоит"]],
    [["I [have to] work on Saturday.", "такой график"], ["I [must] call my mother tonight.", "сам решил"], ["I [should] call my mother more often.", "хорошо бы"]],
    [["You [should] see a doctor.", "совет"], ["You [have to] see a doctor to get a sick note.", "так положено"], ["You [must] see a doctor today!", "обязательно, настаиваю"]],
    [["I [had to] stay late.", "пришлось"], ["I [didn't have to] stay late.", "не пришлось"], ["I [should have] stayed late.", "надо было, но не остался"]],
    [["He [must] be tired.", "наверняка устал"], ["He [can't] be tired — he slept all day.", "не может быть, что устал"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["I must to go.", "I must go.", "после must — без to"],
    ["She have to work.", "She has to work.", "она — has to"],
    ["Yesterday I must stay late.", "Yesterday I had to stay late.", "прошлое — had to"],
    ["You will must wait.", "You will have to wait.", "будущее — will have to"],
    ["Do I must come?", "Do I have to come?", "вопрос — Do I have to…?"],
    ["You mustn't come tomorrow. (не нужно)", "You don't have to come tomorrow.", "не нужно — don't have to"],
    ["You don't have to smoke here. (нельзя)", "You mustn't smoke here.", "нельзя — mustn't"],
    ["You should to see a doctor.", "You should see a doctor.", "после should — без to"],
    ["You should call me yesterday.", "You should have called me yesterday.", "надо было — should have + 3-я форма"],
    ["That mustn't be true.", "That can't be true.", "не может быть — can't"],
]

TOPICS = [
    {"n": 1, "group": "core", "title": "should — совет", "sub": "стоит · не стоит",
     "rule": "should — совет, «стоит, лучше бы»: You should see a neurologist. Не выполнишь — ничего страшного, но лучше сделать. Не стоит — shouldn't: You shouldn't eat so much salt. Спросить совета — Should I…? What should I do? После should — глагол без to.",
     "ex": [
         {"en": "You [should] see a neurologist.", "ru": "Вам стоит сходить к неврологу."},
         {"en": "You [shouldn't] eat so much salt.", "ru": "Не стоит есть столько соли."},
         {"en": "What [should] I do if I miss a dose?", "ru": "Что мне делать, если я пропущу приём?"},
     ]},
    {"n": 2, "group": "core", "title": "have to и must — надо", "sub": "обязанность: смысл и формы",
     "rule": "have to — надо, приходится: так требуют правила, работа, обстоятельства. I have to work on Saturday. must — обязательно: так решил я сам или гласит строгая инструкция: I must call my mother. Visitors must wash their hands. В утверждении они часто взаимозаменяемы, в речи чаще have to. Формы: he has to; вопрос — Do I have to…?; после will, might — have to; после must — глагол без to.",
     "ex": [
         {"en": "I [have to] work on Saturday.", "ru": "В субботу мне надо работать (такой график)."},
         {"en": "I [must] call my mother tonight.", "ru": "Мне обязательно надо позвонить маме вечером."},
         {"en": "Do I [have to] take them every day?", "ru": "Мне обязательно принимать их каждый день?"},
     ]},
    {"n": 3, "group": "core", "title": "mustn't или don't have to", "sub": "нельзя · не нужно · не стоит",
     "rule": "Главная ловушка. mustn't — нельзя, запрет: You mustn't smoke here. don't have to — не нужно, не обязательно, можно не делать: You don't have to come tomorrow. shouldn't — не стоит, совет: You shouldn't work so hard. По-русски всё это «не должен», поэтому спроси себя: запрещено, не обязательно или не советую?",
     "ex": [
         {"en": "You [mustn't] smoke in the hospital.", "ru": "В больнице курить нельзя."},
         {"en": "It's Sunday — you [don't have to] come to work.", "ru": "Воскресенье — тебе не нужно приходить на работу."},
         {"en": "You [shouldn't] work so hard.", "ru": "Не стоит так много работать."},
     ]},
    {"n": 4, "group": "time", "title": "had to, will have to", "sub": "у must нет прошедшего и будущего",
     "rule": "У must нет прошедшего и будущего — их берут у have to. Прошлое — had to: I had to stay late yesterday. Не пришлось — didn't have to: I didn't have to pay. Будущее — will have to: You'll have to wait. Вопрос о прошлом — Did you have to…?",
     "ex": [
         {"en": "Yesterday I [had to] stay late.", "ru": "Вчера мне пришлось задержаться."},
         {"en": "I [didn't have to] pay.", "ru": "Платить не пришлось."},
         {"en": "You'll [have to] wait.", "ru": "Вам придётся подождать."},
     ]},
    {"n": 5, "group": "time", "title": "should have — надо было", "sub": "упрёк и сожаление",
     "rule": "should have + третья форма — «надо было», но не сделали: упрёк или сожаление. You should have called me. I should have listened to you. shouldn't have — «не надо было»: You shouldn't have eaten so much. Не путай с must have — «наверное, сделал».",
     "ex": [
         {"en": "You [should have] called me.", "ru": "Надо было мне позвонить."},
         {"en": "I [should have] listened to you.", "ru": "Надо было тебя послушать."},
         {"en": "I [shouldn't have] eaten so much.", "ru": "Не надо было столько есть."},
     ]},
    {"n": 6, "group": "time", "title": "must = наверняка", "sub": "уверенная догадка · can't be",
     "rule": "Ещё одно значение must — уверенная догадка, «наверняка, должно быть»: He must be tired after a night shift. It must be a migraine. Не может быть — can't, а не mustn't: That can't be true. О прошлом — must have + третья форма: She must have forgotten.",
     "ex": [
         {"en": "He [must] be exhausted after the night shift.", "ru": "После ночной смены он наверняка вымотан."},
         {"en": "That [can't] be true.", "ru": "Не может быть."},
         {"en": "She [must] have forgotten.", "ru": "Наверное, она забыла."},
     ]},
    {"n": 7, "group": "med", "title": "В больнице", "sub": "инструкции пациенту",
     "rule": "Запрет — mustn't: You mustn't drive for a month after a stroke. Совет — should: You should cut down on salt. Так положено — have to: You'll have to stay overnight. Не обязательно — don't have to: You don't have to stay in bed. Вопрос пациента — Do I have to…?",
     "ex": [
         {"en": "You [mustn't] drive for a month.", "ru": "Месяц нельзя водить машину."},
         {"en": "You [should] cut down on salt.", "ru": "Вам стоит меньше солить."},
         {"en": "You [don't have to] stay in bed.", "ru": "Лежать в постели не обязательно."},
     ]},
    {"n": 8, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · should — совет
    c("m1-see", 1, "You've had these headaches for weeks — you ___ see a neurologist.", "Голова болит уже несколько недель — вам стоит сходить к неврологу.",
      ["should", "have to", "mustn't"], "should", "«Стоит» — совет: should."),
    c("m1-salt", 1, "You ___ eat so much salt — it's bad for your blood pressure.", "Не стоит есть столько соли — это вредно для давления.",
      ["shouldn't", "don't have to", "haven't to"], "shouldn't", "«Не стоит» — shouldn't. Don't have to — «не обязательно»."),
    c("m1-what", 1, "What ___ I do if I miss a dose?", "Что мне делать, если я пропущу приём?", ["should", "have to", "mustn't"], "should",
      "Спросить совета — What should I do?"),
    c("m1-sorry", 1, "I think you ___ apologise to her.", "Думаю, тебе стоит извиниться перед ней.", ["should", "have to", "mustn't"], "should",
      "«Думаю, тебе стоит» — I think you should."),
    c("m1-hard", 1, "You ___ work so hard — you look exhausted.", "Не стоит так много работать — ты выглядишь измотанным.",
      ["shouldn't", "don't have to", "mustn't"], "shouldn't", "Совет «не стоит» — shouldn't. Mustn't — запрет."),

    # 2 · have to и must
    c("m2-saturday", 2, "I can't come to the party — I ___ work on Saturday.", "Не смогу прийти на вечеринку — в субботу мне надо работать.",
      ["have to", "should", "don't have to"], "have to", "Так требует график — have to."),
    c("m2-question", 2, "Do I ___ take these tablets every day?", "Мне обязательно принимать эти таблетки каждый день?", ["have to", "must", "should"], "have to",
      "Вопрос с do — только have to: Do I have to…?"),
    c("m2-has", 2, "She ___ wear a uniform at work.", "На работе ей приходится носить форму.", ["has to", "have to", "must to"], "has to",
      "Она — has to. Must to — ошибка."),
    c("m2-will", 2, "You'll ___ wait — the doctor is with another patient.", "Вам придётся подождать — врач занят с другим пациентом.", ["have to", "must", "should"], "have to",
      "После will — have to: will must не бывает."),
    c("m2-might", 2, "If the bleeding continues, we might ___ operate.", "Если кровотечение продолжится, возможно, придётся оперировать.", ["have to", "must", "should"], "have to",
      "После might — have to."),
    c("m2-having", 2, "I hate ___ get up at six.", "Терпеть не могу вставать в шесть.", ["having to", "must", "have to"], "having to",
      "После hate — -ing: having to. У must такой формы нет."),
    c("m2-sign", 2, "You must ___ this form before the operation.", "Эту форму нужно обязательно подписать до операции.", ["sign", "to sign", "signing"], "sign",
      "После must — глагол без to."),

    # 3 · mustn't или don't have to
    c("m3-smoke", 3, "You ___ smoke in the hospital.", "В больнице курить нельзя.", ["mustn't", "don't have to"], "mustn't", "Нельзя, запрет — mustn't."),
    c("m3-sunday", 3, "It's Sunday — you ___ come to work.", "Воскресенье — тебе не нужно приходить на работу.", ["don't have to", "mustn't"], "don't have to",
      "Не нужно, можно не делать — don't have to."),
    c("m3-drive", 3, "After a stroke, you ___ drive for at least a month.", "После инсульта нельзя водить машину как минимум месяц.", ["mustn't", "don't have to"], "mustn't",
      "Запрет — mustn't."),
    c("m3-food", 3, "You ___ take these tablets with food — any time is fine.", "Эти таблетки не обязательно принимать с едой — можно в любое время.",
      ["don't have to", "mustn't"], "don't have to", "Не обязательно — don't have to."),
    c("m3-secret", 3, "You ___ tell anyone — it's a secret.", "Никому нельзя говорить — это секрет.", ["mustn't", "don't have to"], "mustn't", "Нельзя — mustn't."),
    c("m3-free", 3, "The consultation is free — you ___ pay.", "Консультация бесплатная — платить не нужно.", ["don't have to", "mustn't"], "don't have to",
      "Не нужно — don't have to."),
    c("m3-fastfood", 3, "You ___ eat so much fast food.", "Не стоит есть столько фастфуда.", ["shouldn't", "don't have to", "mustn't"], "shouldn't",
      "«Не стоит» — совет: shouldn't."),

    # 4 · had to, will have to
    c("m4-late", 4, "Yesterday I ___ stay at the hospital until midnight.", "Вчера мне пришлось остаться в больнице до полуночи.", ["had to", "must", "should"], "had to",
      "Прошлое — had to. У must прошедшего нет."),
    c("m4-intubate", 4, "His breathing got worse, so we ___ intubate him.", "Дыхание ухудшилось, и нам пришлось его интубировать.", ["had to", "must", "have to"], "had to",
      "Пришлось в прошлом — had to."),
    c("m4-parking", 4, "Luckily, I ___ pay for the parking — it was free.", "К счастью, платить за парковку не пришлось — она была бесплатной.",
      ["didn't have to", "mustn't", "hadn't to"], "didn't have to", "Не пришлось — didn't have to."),
    c("m4-exam", 4, "Next year, all doctors ___ pass a new exam.", "В следующем году всем врачам придётся сдавать новый экзамен.",
      ["will have to", "will must", "must to"], "will have to", "Будущее — will have to."),
    c("m4-did", 4, "___ you have to wait long at the clinic?", "Тебе долго пришлось ждать в поликлинике?", ["Did", "Had", "Must"], "Did",
      "Вопрос о прошлом — Did you have to…?"),

    # 5 · should have
    c("m5-called", 5, "You ___ called me — I was so worried!", "Надо было мне позвонить — я так волновался!", ["should have", "must have", "had to"], "should have",
      "«Надо было» — should have + третья форма."),
    c("m5-earlier", 5, "He ___ come to hospital earlier — now it's too late for thrombolysis.", "Ему надо было приехать в больницу раньше — теперь для тромболизиса уже поздно.",
      ["should have", "must have", "had to"], "should have", "Упрёк: надо было, но не сделал — should have."),
    c("m5-ate", 5, "I ___ eaten so much — now I feel sick.", "Не надо было столько есть — теперь меня мутит.", ["shouldn't have", "mustn't have", "didn't have to"], "shouldn't have",
      "«Не надо было» — shouldn't have."),
    c("m5-listened", 5, "I should have ___ to you.", "Надо было тебя послушать.", ["listened", "listen", "listening"], "listened", "should have + третья форма: listened."),

    # 6 · must = наверняка
    c("m6-tired", 6, "He's been on duty for 24 hours — he ___ be exhausted.", "Он на дежурстве сутки — наверняка вымотан.", ["must", "mustn't", "can't"], "must",
      "Уверенная догадка — must be."),
    c("m6-true", 6, "That ___ be true — I saw him this morning!", "Не может быть — я видел его сегодня утром!", ["can't", "mustn't", "don't have to"], "can't",
      "«Не может быть» — can't. Mustn't — это запрет."),
    c("m6-forgot", 6, "She's not here. She ___ have forgotten about the meeting.", "Её нет. Наверное, она забыла о совещании.", ["must", "should", "had to"], "must",
      "Догадка о прошлом — must have + третья форма."),
    c("m6-migraine", 6, "Flashing lights before the headache? It ___ be a migraine with aura.", "Мелькание перед глазами перед головной болью? Скорее всего, это мигрень с аурой.",
      ["must", "mustn't", "has"], "must", "Уверенная догадка — must be."),

    # 7 · в больнице
    c("m7-overnight", 7, "Your blood pressure is still high, so you'll ___ stay overnight.", "Давление всё ещё высокое, так что придётся остаться на ночь.",
      ["have to", "must", "should"], "have to", "Будущее — will have to."),
    c("m7-bed", 7, "You ___ stay in bed — you can walk around the ward.", "Лежать в постели не обязательно — можете ходить по отделению.",
      ["don't have to", "mustn't", "shouldn't"], "don't have to", "Не обязательно — don't have to."),
    c("m7-salt", 7, "You ___ cut down on salt and walk every day.", "Вам стоит меньше солить и каждый день гулять.", ["should", "mustn't", "don't have to"], "should",
      "Совет — should."),
    c("m7-aspirin", 7, "You ___ stop taking aspirin without talking to your doctor.", "Нельзя прекращать приём аспирина, не посоветовавшись с врачом.",
      ["mustn't", "don't have to", "shouldn't"], "mustn't", "«Нельзя» — mustn't.",
      also={"shouldn't": "так говорят, это мягче — «не стоит»; запрет — mustn't"}),
    c("m7-mri", 7, "___ I have to fast before the MRI? — No, you can eat as usual.", "Мне нужно голодать перед МРТ? — Нет, можете есть как обычно.",
      ["Do", "Must", "Should"], "Do", "Вопрос — Do I have to…?"),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
    for alt in k.get("also", {}): assert alt in k["opts"] and alt != k["a"], k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
