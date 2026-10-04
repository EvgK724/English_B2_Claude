# Содержание приложения «would»: все работы слова would.
# Пометка […] — would и его формы в фокусе (оранжевый).

MIXED_TOPIC = 11

GROUPS = {
    "polite": "Вежливость",
    "imagine": "Воображаемое: «бы»",
    "past": "Прошлое",
    "wish": "Желания и сокращения",
    "mix": "Итог",
}

# Как звучит: форма | транскрипция | пояснение | пример | озвучка
SOUNDS = [
    ["would", "/wʊd/", "l не читается, как в could и should", "I would go.", "Would. I would go."],
    ["I'd", "/aɪd/", "сокращение: I would или I had", "I'd like a coffee.", "I'd. I'd like a coffee."],
    ["wouldn't", "/ˈwʊdnt/", "would not", "He wouldn't listen.", "Wouldn't. He wouldn't listen."],
    ["would have", "/ˈwʊd əv/", "в речи сливается: [ˈwʊdəv]", "I would have called.", "Would have. I would have called."],
    ["wouldn't have", "/ˈwʊdnt əv/", "не… бы — о прошлом", "I wouldn't have known.", "Wouldn't have. I wouldn't have known."],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["If I would have time, I would help.", "If I had time, I would help.", "после if — без would"],
    ["I would like that you come.", "I would like you to come.", "would like + кто-то + to"],
    ["Would you like some tea? — Yes, I like.", "Would you like some tea? — Yes, please.", "like — «нравится»"],
    ["Would you mind to wait?", "Would you mind waiting?", "mind + -ing"],
    ["I'd rather to stay.", "I'd rather stay.", "rather — без to"],
    ["I would of called.", "I would have called.", "would have, не would of"],
    ["As a child, I would have a dog.", "As a child, I used to have a dog.", "состояние — used to"],
    ["I wish I would be taller.", "I wish I were taller.", "о себе — без would"],
    ["He said he will come, but he didn't.", "He said he would come, but he didn't.", "will в прошлом — would"],
    ["You would better go.", "You had better go.", "'d better = had better"],
]

TOPICS = [
    {"n": 1, "group": "polite", "title": "Просьбы и предложения", "sub": "Would you…? · I'd like…",
     "rule": "Would you…? — вежливая просьба, мягче, чем Can you…: Would you open the window, please? Would you like…? — предложение: Would you like some tea? Would you like to sit down? I'd like = I would like — вежливое «хотел бы»: I'd like a coffee, please. Отвечают: Yes, please или No, thank you. I like — это «мне нравится», а не «хочу».",
     "ex": [
         {"en": "[Would] you like some tea?", "ru": "Хотите чаю?"},
         {"en": "[I'd like] to make an appointment.", "ru": "Я хотел бы записаться на приём."},
         {"en": "[Would] you open the door, please?", "ru": "Не могли бы вы открыть дверь?"},
     ]},
    {"n": 2, "group": "polite", "title": "Would you mind…?", "sub": "вы не против…?",
     "rule": "Would you mind + -ing? — очень вежливая просьба: Would you mind waiting? Отрицание — not + -ing: Would you mind not talking so loudly? Would you mind if I + прошедшее — просишь разрешения: Would you mind if I opened the window? С Do you mind if I — настоящее: Do you mind if I sit here? Ответ «пожалуйста» — No, not at all: mind — «возражать».",
     "ex": [
         {"en": "[Would you mind] waiting a moment?", "ru": "Не могли бы вы минутку подождать?"},
         {"en": "[Would you mind if] I opened the window?", "ru": "Вы не против, если я открою окно?"},
         {"en": "[No], not at all.", "ru": "Конечно, пожалуйста (дословно: «нет, не возражаю»)."},
     ]},
    {"n": 3, "group": "polite", "title": "I'd rather, I'd prefer", "sub": "лучше бы · мягкое мнение",
     "rule": "I'd rather + глагол без to — «я бы лучше»: I'd rather stay at home. I'd rather walk than take the bus. Отказ — I'd rather not. Про другого человека — прошедшее: I'd rather you didn't smoke here. I'd prefer + to + глагол: I'd prefer to wait. Осторожное мнение — I would say…, I would think…: I would say it's a migraine.",
     "ex": [
         {"en": "[I'd rather] stay at home.", "ru": "Я бы лучше остался дома."},
         {"en": "[I'd prefer] to wait.", "ru": "Я бы предпочёл подождать."},
         {"en": "[I would say] it's a migraine.", "ru": "Я бы сказал, что это мигрень."},
     ]},
    {"n": 4, "group": "imagine", "title": "Воображаемое: «бы»", "sub": "If I had…, I would…",
     "rule": "would + глагол — «бы» о воображаемом сейчас или в будущем: What would you do? It would be better to leave early. В условии с if — прошедшее, would — во второй части: If I had more time, I would learn Spanish. Совет: If I were you, I would… Would после if — ошибка.",
     "ex": [
         {"en": "If I had more time, I [would] learn Spanish.", "ru": "Будь у меня больше времени, я бы выучил испанский."},
         {"en": "If I were you, I['d] see a doctor.", "ru": "На твоём месте я бы сходил к врачу."},
         {"en": "What [would] you do?", "ru": "Что бы ты сделал?"},
     ]},
    {"n": 5, "group": "imagine", "title": "Прошлое, которого не было", "sub": "would have + третья форма",
     "rule": "would have + третья форма — «бы» о прошлом, которое не случилось: I would have called, but I didn't have your number. If I had known, I would have come. В части с if — had + третья форма. You would have loved it — «тебе бы понравилось». В речи have звучит [əv], но писать would of — ошибка.",
     "ex": [
         {"en": "If I had known, I [would have] come.", "ru": "Если бы я знал, я бы пришёл."},
         {"en": "You [would have] loved it.", "ru": "Тебе бы понравилось."},
         {"en": "I [would have] called, but I didn't have your number.", "ru": "Я бы позвонил, но у меня не было твоего номера."},
     ]},
    {"n": 6, "group": "past", "title": "Будущее в прошлом", "sub": "will → would",
     "rule": "Рассказываешь о прошлом — will становится would: He says he will call → He said he would call. I knew she would be late. I thought it would rain. won't → wouldn't: She promised she wouldn't be late again.",
     "ex": [
         {"en": "He said he [would] call.", "ru": "Он сказал, что позвонит."},
         {"en": "I knew she [would] be late.", "ru": "Я знал, что она опоздает."},
         {"en": "I thought it [would] rain.", "ru": "Я думал, что пойдёт дождь."},
     ]},
    {"n": 7, "group": "past", "title": "Привычки в прошлом", "sub": "«бывало» · would или used to",
     "rule": "would — повторяющиеся действия в прошлом, «бывало»: Every summer we would go to the sea. Как used to, но только для действий. Состояние — только used to: I used to have a dog, My father used to be a surgeon. I would have a dog — ошибка.",
     "ex": [
         {"en": "Every summer we [would] go to the sea.", "ru": "Каждое лето мы ездили на море."},
         {"en": "My grandfather [would] tell us stories.", "ru": "Дедушка, бывало, рассказывал нам истории."},
         {"en": "I [used to] have a dog.", "ru": "Раньше у меня была собака."},
     ]},
    {"n": 8, "group": "past", "title": "Отказ: wouldn't", "sub": "не хотел — и всё",
     "rule": "wouldn't — отказ в прошлом, «ни в какую»: He wouldn't listen. The patient wouldn't take his tablets. Так говорят и о вещах: The car wouldn't start, the door wouldn't open. Отказ сейчас — won't: My son won't eat vegetables.",
     "ex": [
         {"en": "The car [wouldn't] start.", "ru": "Машина никак не заводилась."},
         {"en": "He [wouldn't] listen.", "ru": "Он ни в какую не слушал."},
         {"en": "She [wouldn't] tell me.", "ru": "Она так и не сказала мне."},
     ]},
    {"n": 9, "group": "wish", "title": "wish + would", "sub": "хоть бы ты… · если бы только",
     "rule": "I wish + кто-то + would — хочу, чтобы другой человек или обстоятельства изменились, часто с раздражением: I wish you would stop smoking. I wish it would stop raining. I wish you wouldn't interrupt me. О себе would не ставят: I wish I could speak English fluently, I wish I had more time. If only he would listen! — «если бы только».",
     "ex": [
         {"en": "I wish you [would] stop smoking.", "ru": "Хорошо бы ты бросил курить."},
         {"en": "I wish it [would] stop raining.", "ru": "Хоть бы дождь перестал."},
         {"en": "If only he [would] listen!", "ru": "Если бы только он послушал!"},
     ]},
    {"n": 10, "group": "wish", "title": "'d — would или had?", "sub": "I'd go · I'd gone · I'd better",
     "rule": "'d — это would или had. Смотри, что дальше. I'd + глагол — would: I'd call you. I'd + третья форма — had: She'd already gone. I'd have + третья форма — would have. I'd better + глагол без to — had better, «лучше бы»: You'd better see a doctor. I'd rather — would rather.",
     "ex": [
         {"en": "[I'd] like a coffee.", "ru": "Мне кофе, пожалуйста. (I would)"},
         {"en": "[She'd] already left.", "ru": "Она уже ушла. (she had)"},
         {"en": "[You'd] better go.", "ru": "Тебе лучше пойти. (you had)"},
     ]},
    {"n": 11, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · просьбы и предложения
    c("w1-water", 1, "___ you like some water?", "Хотите воды?", ["Would", "Do", "Will"], "Would", "Предложение — Would you like…?"),
    c("w1-appt", 1, "I ___ like to make an appointment, please.", "Я хотел бы записаться на приём.", ["would", "will", "am"], "would",
      "Вежливое «хотел бы» — I would like, коротко I'd like."),
    c("w1-sit", 1, "Would you like ___ down?", "Не хотите присесть?", ["to sit", "sitting", "sit"], "to sit", "Would you like + to + глагол."),
    c("w1-window", 1, "___ you open the window, please?", "Не могли бы вы открыть окно?", ["Would", "Do", "Are"], "Would", "Вежливая просьба — Would you…?"),
    c("w1-yes", 1, "Would you like some tea? — Yes, ___.", "Хотите чаю? — Да, пожалуйста.", ["please", "I like", "I want"], "please",
      "На предложение отвечают Yes, please. Yes, I like — ошибка: like — «нравится»."),
    c("w1-cup", 1, "I ___ a cup of tea, please.", "Мне чашку чая, пожалуйста.", ["would like", "like"], "would like",
      "Хочу сейчас, вежливо, — I'd like. I like — «мне нравится вообще»."),

    # 2 · would you mind
    c("w2-wait", 2, "Would you mind ___ here for a moment?", "Не могли бы вы подождать здесь минутку?", ["waiting", "to wait", "wait"], "waiting",
      "Would you mind + -ing."),
    c("w2-shirt", 2, "Would you mind ___ your shirt? I need to listen to your chest.", "Не могли бы вы снять рубашку? Мне нужно послушать лёгкие.",
      ["taking off", "to take off", "take off"], "taking off", "Would you mind + -ing: taking off."),
    c("w2-notalk", 2, "Would you mind ___ so loudly? The patients are asleep.", "Не могли бы вы не разговаривать так громко? Пациенты спят.",
      ["not talking", "not to talk", "don't talk"], "not talking", "Отрицание — Would you mind not + -ing."),
    c("w2-if", 2, "Would you mind if I ___ the window?", "Вы не против, если я открою окно?", ["opened", "open", "will open"], "opened",
      "Would you mind if I + прошедшее. С Do you mind if I — настоящее: open."),
    c("w2-do", 2, "Do you mind if I ___ here?", "Не возражаете, если я здесь сяду?", ["sit", "sat", "would sit"], "sit",
      "Do you mind if I + настоящее. С Would you mind if I — прошедшее: sat."),
    c("w2-no", 2, "Would you mind closing the door? — ___, not at all.", "Не закроете дверь? — Конечно, без проблем.", ["No", "Yes"], "No",
      "mind — «возражать»: No, not at all — «нет, не возражаю», то есть «конечно»."),

    # 3 · I'd rather, I'd prefer
    c("w3-stay", 3, "I'd rather ___ at home tonight.", "Я бы лучше остался сегодня дома.", ["stay", "to stay", "staying"], "stay", "I'd rather + глагол без to."),
    c("w3-prefer", 3, "I'd prefer ___ for the results.", "Я бы предпочёл дождаться результатов.", ["to wait", "wait", "waiting"], "to wait", "I'd prefer + to + глагол."),
    c("w3-you", 3, "I'd rather you ___ smoke in the car.", "Я бы предпочёл, чтобы ты не курил в машине.", ["didn't", "don't", "won't"], "didn't",
      "I'd rather + другой человек + прошедшее: I'd rather you didn't."),
    c("w3-not", 3, "Shall we go out tonight? — I'd rather ___.", "Сходим куда-нибудь вечером? — Пожалуй, нет.", ["not", "not to", "don't"], "not",
      "Вежливый отказ — I'd rather not."),
    c("w3-than", 3, "I'd rather walk ___ take the bus.", "Я лучше пройдусь, чем поеду на автобусе.", ["than", "to", "that"], "than", "I'd rather A than B."),
    c("w3-say", 3, "It's hard to be sure, but I ___ it's a migraine.", "Трудно сказать наверняка, но я бы сказал, что это мигрень.",
      ["would say", "will say", "say"], "would say", "Осторожное мнение — I would say…"),

    # 4 · воображаемое
    c("w4-time", 4, "If I ___ more time, I would learn Spanish.", "Будь у меня больше времени, я бы выучил испанский.", ["had", "would have", "have"], "had",
      "В части с if — прошедшее. Would — только во второй части."),
    c("w4-you", 4, "If I were you, I ___ see a doctor.", "На твоём месте я бы сходил к врачу.", ["would", "will", "am"], "would", "Совет: If I were you, I would…"),
    c("w4-million", 4, "What ___ you do if you won a million?", "Что бы ты сделал, если бы выиграл миллион?", ["would", "will", "do"], "would",
      "Воображаемое — would: What would you do?"),
    c("w4-took", 4, "If he ___ his tablets, he wouldn't feel so bad.", "Если бы он принимал таблетки, ему не было бы так плохо.",
      ["took", "would take", "takes"], "took", "В части с if — прошедшее: took."),
    c("w4-were", 4, "If I ___ you, I'd take a few days off.", "На твоём месте я бы взял пару выходных.", ["were", "would be", "am"], "were",
      "«На твоём месте» — If I were you. Would после if не ставят."),
    c("w4-better", 4, "It would be better ___ early.", "Лучше было бы выехать пораньше.", ["to leave", "leave", "leaving"], "to leave",
      "It would be better / nice + to + глагол."),

    # 5 · would have + третья форма
    c("w5-known", 5, "If I had known, I ___ earlier.", "Если бы я знал, я бы пришёл раньше.", ["would have come", "would come", "had come"], "would have come",
      "О прошлом — would have + третья форма."),
    c("w5-arrived", 5, "If we ___ earlier, we could have given thrombolysis.", "Если бы мы приехали раньше, можно было бы провести тромболизис.",
      ["had arrived", "would have arrived", "arrived"], "had arrived", "В части с if о прошлом — had + третья форма."),
    c("w5-number", 5, "I ___ you, but I didn't have your number.", "Я бы тебе позвонил, но у меня не было твоего номера.",
      ["would have called", "would call", "will call"], "would have called", "Не случилось в прошлом — would have + третья форма."),
    c("w5-loved", 5, "You ___ loved the concert — it was amazing!", "Тебе бы понравился концерт — он был потрясающим!", ["would have", "would", "will have"], "would have",
      "«Тебе бы понравилось» — you would have loved."),
    c("w5-survived", 5, "He would have ___ if the ambulance had come sooner.", "Он бы выжил, если бы скорая приехала раньше.", ["survived", "survive", "survives"], "survived",
      "would have + третья форма: survived."),
    c("w5-of", 5, "I would ___ told you, but I forgot.", "Я бы тебе сказал, но забыл.", ["have", "of", "had"], "have",
      "would have, не would of: в речи have звучит [əv], отсюда ошибка."),

    # 6 · будущее в прошлом
    c("w6-call", 6, "He said he ___ call me back, but he never did.", "Он сказал, что перезвонит, но так и не перезвонил.", ["would", "will"], "would",
      "will в рассказе о прошлом — would."),
    c("w6-late", 6, "I knew she ___ be late — she always is.", "Я знал, что она опоздает, — она всегда опаздывает.", ["would", "will"], "would",
      "После knew, thought, said — would."),
    c("w6-results", 6, "Last week the doctor said the results ___ be ready by Friday, but they weren't.",
      "На прошлой неделе врач сказал, что результаты будут готовы к пятнице, но их не было.", ["would", "will"], "would",
      "Будущее, увиденное из прошлого, — would."),
    c("w6-promise", 6, "She promised she ___ be late again, but she was late today.", "Она обещала, что больше не будет опаздывать, но сегодня опять опоздала.",
      ["wouldn't", "won't", "didn't"], "wouldn't", "won't в рассказе о прошлом — wouldn't."),
    c("w6-rain", 6, "I thought it ___ rain, so I took an umbrella.", "Я думал, что пойдёт дождь, поэтому взял зонт.", ["would", "will"], "would",
      "I thought it would… — будущее из прошлого."),

    # 7 · привычки в прошлом
    c("w7-fishing", 7, "When I was a child, my grandfather ___ take me fishing every Sunday.", "Когда я был маленьким, дедушка каждое воскресенье брал меня на рыбалку.",
      ["would", "will", "was"], "would", "Повторяющееся действие в прошлом — would (или used to)."),
    c("w7-hair", 7, "I ___ have long hair when I was at university.", "В университете у меня были длинные волосы.", ["used to", "would"], "used to",
      "Состояние — только used to. Would — только для действий."),
    c("w7-read", 7, "Every evening after work, she ___ read to her children.", "Каждый вечер после работы она читала детям.", ["would", "will", "was"], "would",
      "Привычное действие в прошлом — would."),
    c("w7-surgeon", 7, "My father ___ be a surgeon.", "Мой отец раньше был хирургом.", ["used to", "would"], "used to", "Профессия, состояние — used to."),
    c("w7-wait", 7, "Before the new hospital opened, patients ___ wait for hours.", "До открытия новой больницы пациентам, бывало, приходилось ждать часами.",
      ["would", "will", "are"], "would", "«Бывало» — would + глагол."),

    # 8 · отказ
    c("w8-car", 8, "The car ___ start this morning.", "Сегодня утром машина никак не заводилась.", ["wouldn't", "won't", "didn't want"], "wouldn't",
      "Отказ в прошлом, даже у вещей, — wouldn't."),
    c("w8-listen", 8, "I told him to rest, but he ___ listen.", "Я говорил ему отдыхать, но он ни в какую не слушал.", ["wouldn't", "won't", "doesn't"], "wouldn't",
      "Не хотел, и всё, — wouldn't."),
    c("w8-tablets", 8, "The patient ___ take his tablets, so we called his daughter.", "Пациент отказывался принимать таблетки, и мы позвонили его дочери.",
      ["wouldn't", "won't", "doesn't"], "wouldn't", "Отказывался — wouldn't."),
    c("w8-veg", 8, "My son ___ eat vegetables — he just refuses.", "Мой сын не ест овощи — отказывается, и всё.", ["won't", "wouldn't"], "won't",
      "Отказ сейчас — won't, в прошлом — wouldn't."),
    c("w8-tell", 8, "She ___ tell me what had happened, so I asked her husband.", "Она так и не сказала мне, что случилось, и я спросил её мужа.",
      ["wouldn't", "won't"], "wouldn't", "Отказ в прошлом — wouldn't."),

    # 9 · wish + would
    c("w9-smoking", 9, "I wish you ___ smoking.", "Хорошо бы ты бросил курить.", ["would stop", "stop", "will stop"], "would stop",
      "Хочу, чтобы другой изменился, — wish + would."),
    c("w9-rain", 9, "I wish it ___ raining — I want to go for a walk.", "Хоть бы дождь перестал — хочу погулять.", ["would stop", "stops", "will stop"], "would stop",
      "wish + would — и о том, что от нас не зависит."),
    c("w9-could", 9, "I wish I ___ speak English fluently.", "Жаль, что я не говорю по-английски свободно.", ["could", "would", "will"], "could",
      "О себе — wish + could, не would."),
    c("w9-had", 9, "I wish I ___ more free time.", "Жаль, что у меня мало свободного времени.", ["had", "would have", "have"], "had",
      "О том, что есть сейчас, — wish + прошедшее: had."),
    c("w9-only", 9, "If only he ___ listen to me!", "Если бы только он меня послушал!", ["would", "will", "does"], "would",
      "Сильное желание, чтобы кто-то изменился, — If only… would."),
    c("w9-interrupt", 9, "I wish you ___ interrupt me all the time.", "Перестань, пожалуйста, всё время меня перебивать.", ["wouldn't", "don't", "won't"], "wouldn't",
      "Раздражение — I wish you wouldn't…"),

    # 10 · 'd — would или had
    c("w10-call", 10, "I'd ___ you if I had your number.", "Я бы тебе позвонил, если бы у меня был твой номер.", ["call", "called"], "call",
      "'d + глагол — would: I'd call."),
    c("w10-gone", 10, "By the time I arrived, she'd already ___ home.", "Когда я пришёл, она уже ушла домой.", ["gone", "go"], "gone",
      "'d + третья форма — had: she'd gone."),
    c("w10-better", 10, "You'd ___ see a doctor about that pain.", "Тебе лучше показаться врачу с этой болью.", ["better", "rather"], "better",
      "Совет «лучше бы» — you'd better = you had better."),
    c("w10-tomorrow", 10, "She promised she'd ___ me tomorrow.", "Она пообещала, что позвонит мне завтра.", ["call", "called"], "call",
      "'d + глагол — would: she would call."),
    c("w10-seen", 10, "I'd never ___ such a big hospital before.", "Я никогда раньше не видел такой большой больницы.", ["seen", "see"], "seen",
      "'d + третья форма — had: I had never seen."),
    c("w10-go", 10, "You'd better ___ now, or you'll miss the bus.", "Тебе лучше выйти сейчас, а то опоздаешь на автобус.", ["go", "to go", "going"], "go",
      "had better + глагол без to."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
