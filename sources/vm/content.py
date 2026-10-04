# Содержание приложения «remember»: глаголы, у которых to и -ing дают разный смысл —
# remember, forget, regret, try, stop, go on, mean, need, like, see sb do / doing, afraid, sorry, interested.
# Пометка: [слово|g] — форма с to или без to (синий), [слово] — форма на -ing (оранжевый).

MIXED_TOPIC = 10

GROUPS = {
    "memory": "Помнить и забыть",
    "effort": "Жалеть, стараться, перестать",
    "more": "Продолжать, означать, надо, нравится",
    "sense": "Видеть, бояться, извиняться",
    "mix": "Итог",
}

# Пары: [+ to, перевод] | [+ -ing, перевод]
PAIRS = [
    ["remember to lock", "не забыть запереть", "remember locking", "помнить, что запер"],
    ["forget to send", "забыть отправить", "never forget meeting", "не забыть встречу"],
    ["regret to say", "с сожалением сказать", "regret saying", "жалеть, что сказал"],
    ["try to open", "стараться открыть", "try opening", "попробовать открыть"],
    ["stop to rest", "остановиться отдохнуть", "stop working", "перестать работать"],
    ["go on to discuss", "перейти к обсуждению", "go on discussing", "продолжать обсуждать"],
    ["mean to call", "собираться позвонить", "mean waiting", "означать ожидание"],
    ["need to check", "надо проверить", "needs checking", "надо, чтобы проверили"],
]

# Одна фраза — разный смысл: строки [английский, пояснение]
CONTRAST = [
    [["Did you remember [to lock|g] the door?", "не забыл запереть? — дело было впереди"],
     ["I remember [locking] the door.", "помню, как запирал, — дело позади"]],
    [["The window is stuck. Try [to open|g] it.", "постарайся: открыть трудно"],
     ["It's hot. Try [opening] the window.", "попробуй как способ: вдруг поможет"]],
    [["He stopped [to talk|g] to me.", "остановился, чтобы поговорить"],
     ["He stopped [talking] to me.", "перестал со мной разговаривать"]],
    [["I regret [to say|g] that we have no free beds.", "с сожалением сообщаю"],
     ["I regret [telling] him about it.", "жалею, что рассказал"]],
    [["I saw him [cross|g] the road.", "видел всё: перешёл от края до края"],
     ["I saw him [crossing] the road.", "видел кусок: он как раз переходил"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["I remember to meet him in 2019.", "I remember meeting him in 2019.", "было в прошлом — -ing"],
    ["I forgot locking the car.", "I forgot to lock the car.", "забыл и не сделал — to"],
    ["We regret informing you that…", "We regret to inform you that…", "с сожалением сообщаем — to"],
    ["I regret to buy this car.", "I regret buying this car.", "жалею о сделанном — -ing"],
    ["He stopped to smoke last year.", "He stopped smoking last year.", "бросил — -ing"],
    ["It means to wait three months.", "It means waiting three months.", "означает — -ing"],
    ["I didn't mean hurting you.", "I didn't mean to hurt you.", "не хотел — to"],
    ["The car needs to repair.", "The car needs repairing.", "надо, чтобы починили, — -ing"],
    ["Sorry to be late yesterday.", "Sorry for being late yesterday.", "за прошлое — for + -ing"],
    ["I saw him to cross the road.", "I saw him cross the road.", "see кого — без to"],
]

TOPICS = [
    {"n": 1, "group": "memory", "title": "remember", "sub": "не забыть сделать · помнить, как было",
     "rule": "Remember to do — не забыть сделать: дело ещё впереди. Remember doing — помнить, как делал: дело уже было. Проверка: действие случилось раньше, чем «помню»? Тогда -ing. С отрицанием: Remember not to eat before the scan. В прошлом: I remembered to call — не забыл и позвонил.",
     "ex": [
         {"en": "Remember [to bring|g] your old scans.", "ru": "Не забудьте взять старые снимки."},
         {"en": "I remember [meeting] her at a conference.", "ru": "Я помню, как познакомился с ней на конференции."},
         {"en": "Did you remember [to feed|g] the cat?", "ru": "Ты не забыл покормить кошку?"},
     ]},
    {"n": 2, "group": "memory", "title": "forget", "sub": "забыл сделать · не забуду, как было",
     "rule": "Forget to do — забыть сделать, и дело не сделано: I forgot to sign the form. Forget doing — забыть, как что-то было; почти всегда в форме I'll never forget: I'll never forget seeing her walk again. Don't forget — всегда с to: Don't forget to take your tablets.",
     "ex": [
         {"en": "I forgot [to send|g] the referral.", "ru": "Я забыл отправить направление."},
         {"en": "I'll never forget [seeing] her walk again after thrombolysis.", "ru": "Никогда не забуду, как она снова пошла после тромболизиса."},
         {"en": "Don't forget [to switch|g] off the lights.", "ru": "Не забудь выключить свет."},
     ]},
    {"n": 3, "group": "effort", "title": "regret", "sub": "жалею, что сделал · с сожалением сообщаю",
     "rule": "Regret doing — жалеть о том, что сделал или не сделал: I regret not calling him. Regret to say, to inform, to tell — «с сожалением сообщаю»: так официально начинают плохую новость. Книжный вариант прошлого — regret having done: I regret having said that.",
     "ex": [
         {"en": "I regret [not learning] English earlier.", "ru": "Жалею, что не выучил английский раньше."},
         {"en": "We regret [to announce|g] that the conference has been cancelled.", "ru": "С сожалением сообщаем, что конференция отменена."},
         {"en": "She regrets [moving] to the city.", "ru": "Она жалеет, что переехала в город."},
     ]},
    {"n": 4, "group": "effort", "title": "try", "sub": "стараться · попробовать способ",
     "rule": "Try to do — стараться, прилагать усилие; сделать трудно, и не факт, что получится: Try to relax. Try doing — попробовать как способ: не поможет — возьмём другой: Try lying on your side. Проверка: трудно само действие — to; действие лёгкое, но неизвестно, поможет ли, — -ing.",
     "ex": [
         {"en": "Try [to relax|g] — it won't hurt.", "ru": "Постарайтесь расслабиться — больно не будет."},
         {"en": "Can't sleep? Try [reading] before bed.", "ru": "Не спится? Попробуйте почитать перед сном."},
         {"en": "He tried [to stand|g] up but fell.", "ru": "Он пытался встать, но упал."},
     ]},
    {"n": 5, "group": "effort", "title": "stop", "sub": "перестать · остановиться, чтобы",
     "rule": "Stop doing — прекратить само действие: stop smoking, stop taking the tablets. Stop to do — остановиться, чтобы сделать что-то другое; to здесь значит «чтобы»: We stopped to buy water. Проверка: по-русски «перестал» — -ing; «остановился, чтобы» — to.",
     "ex": [
         {"en": "Stop [taking] the tablets if you get a rash.", "ru": "Прекратите приём таблеток, если появится сыпь."},
         {"en": "We stopped [to buy|g] some water.", "ru": "Мы остановились купить воды."},
         {"en": "It has stopped [raining].", "ru": "Дождь кончился."},
     ]},
    {"n": 6, "group": "more", "title": "go on, mean", "sub": "продолжать · перейти к · означать · собираться",
     "rule": "Go on doing — продолжать то же самое: She went on working until 70. Go on to do — перейти к следующему, потом сделать: After medical school she went on to become a neurologist. Mean doing — означать: A stroke often means losing independence. Mean to do — собираться, хотеть: I meant to call you. Didn't mean to — «не хотел, нечаянно».",
     "ex": [
         {"en": "She went on [working] until she was 70.", "ru": "Она продолжала работать до 70 лет."},
         {"en": "He went on [to become|g] head of department.", "ru": "Потом он стал заведующим отделением."},
         {"en": "I meant [to call|g] you, but I forgot.", "ru": "Я собирался тебе позвонить, но забыл."},
     ]},
    {"n": 7, "group": "more", "title": "need, like, prefer", "sub": "надо · нравится · предпочитаю",
     "rule": "Need to do — надо сделать самому: I need to call the lab. Something needs doing — надо, чтобы сделали: The results need checking = need to be checked. Like doing — нравится: I like swimming. Like to do — считаю правильным, привык: I like to arrive early. Would like — только с to: I'd like to ask a question. Prefer doing to doing: I prefer walking to driving. Would rather — без to: I'd rather stay.",
     "ex": [
         {"en": "These results need [checking] again.", "ru": "Эти результаты нужно перепроверить."},
         {"en": "I like [to arrive|g] early for my shift.", "ru": "Я стараюсь приходить на смену заранее."},
         {"en": "I'd like [to book|g] an appointment.", "ru": "Я бы хотел записаться на приём."},
     ]},
    {"n": 8, "group": "sense", "title": "see sb do / doing", "sub": "видел всё · видел кусок",
     "rule": "See, hear, watch, notice + кого + глагол без to — видел действие целиком, от начала до конца: I saw him fall. + -ing — видел кусок, действие шло: I saw him crossing the road. To после see — ошибка. В пассиве to появляется: He was seen to leave — сверх уровня.",
     "ex": [
         {"en": "I saw him [fall|g].", "ru": "Я видел, как он упал."},
         {"en": "We heard someone [shouting] in the corridor.", "ru": "Мы слышали, как в коридоре кто-то кричал."},
         {"en": "I watched the nurse [insert|g] the cannula.", "ru": "Я смотрел, как медсестра ставила катетер."},
     ]},
    {"n": 9, "group": "sense", "title": "afraid, sorry, interested", "sub": "боюсь · извините · интересно",
     "rule": "Afraid to do — боюсь сделать и потому не делаю: He was afraid to tell his wife. Afraid of doing — боюсь, что это случится само: afraid of falling. Sorry to do — извиняюсь за то, что делаю сейчас: Sorry to bother you. Sorry for doing — за то, что уже было: Sorry for being late yesterday. Interested in doing — интересуюсь, хочу; interested to hear — было интересно узнать.",
     "ex": [
         {"en": "He was afraid [to tell|g] his wife.", "ru": "Он боялся сказать жене."},
         {"en": "She's afraid of [losing] her job.", "ru": "Она боится потерять работу."},
         {"en": "Sorry [to bother|g] you, doctor.", "ru": "Извините, что беспокою, доктор."},
     ]},
    {"n": 10, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · remember
    c("v1-passport", 1, "Please remember ___ your passport tomorrow.", "Пожалуйста, не забудьте завтра паспорт.",
      ["to bring", "bringing"], "to bring", "Дело впереди — remember to."),
    c("v1-airport", 1, "I clearly remember ___ him at the airport.", "Я хорошо помню, как встречал его в аэропорту.",
      ["meeting", "to meet"], "meeting", "Было в прошлом — remember + -ing."),
    c("v1-not", 1, "Remember ___ anything after midnight before the operation.", "Не забудьте ничего не есть после полуночи перед операцией.",
      ["not to eat", "not eating"], "not to eat", "Не забыть не делать — remember not to."),
    c("v1-gas", 1, "Luckily, I remembered ___ the gas off before we left.", "К счастью, я не забыл выключить газ перед уходом.",
      ["to turn", "turning"], "to turn", "Не забыл и сделал — remembered to."),
    c("v1-sea", 1, "Do you remember ___ to the sea as a child?", "Помнишь, как ездил на море в детстве?",
      ["going", "to go"], "going", "Воспоминание — remember + -ing."),
    c("v1-ambulance", 1, "The patient doesn't remember ___ the ambulance.", "Пациент не помнит, как вызывал скорую.",
      ["calling", "to call"], "calling", "Не помнит, как было, — -ing."),

    # 2 · forget
    c("v2-call", 2, "Sorry, I forgot ___ you back.", "Извините, забыл вам перезвонить.",
      ["to call", "calling"], "to call", "Забыл и не сделал — forgot to."),
    c("v2-daughter", 2, "I'll never forget ___ my daughter for the first time.", "Никогда не забуду, как впервые взял дочь на руки.",
      ["holding", "to hold"], "holding", "Never forget + -ing — не забуду, как было."),
    c("v2-dose", 2, "Don't forget ___ the dose if his kidney function drops.", "Не забудьте снизить дозу, если упадёт функция почек.",
      ["to reduce", "reducing"], "to reduce", "Don't forget — всегда to."),
    c("v2-door", 2, "She forgot ___ the door, and someone got in.", "Она забыла запереть дверь, и кто-то вошёл.",
      ["to lock", "locking"], "to lock", "Забыла и не сделала — forgot to."),
    c("v2-results", 2, "She'll never forget ___ the results of her first trial.", "Она никогда не забудет, как узнала результаты своего первого исследования.",
      ["hearing", "to hear"], "hearing", "Never forget + -ing."),

    # 3 · regret
    c("v3-car", 3, "I really regret ___ this car — it's always breaking down.", "Очень жалею, что купил эту машину: она постоянно ломается.",
      ["buying", "to buy"], "buying", "Жалею о сделанном — regret + -ing."),
    c("v3-postponed", 3, "I regret ___ you that the operation has been postponed.", "С сожалением сообщаю, что операцию перенесли.",
      ["to tell", "telling"], "to tell", "С сожалением сообщаю — regret to tell."),
    c("v3-advice", 3, "He regrets ___ his doctor's advice.", "Он жалеет, что не послушал врача.",
      ["not following", "not to follow"], "not following", "Жалеет, что не сделал, — regret not + -ing."),
    c("v3-place", 3, "We regret ___ that we cannot offer you a place.", "К сожалению, вынуждены сообщить, что не можем предложить вам место.",
      ["to say", "saying"], "to say", "Официальная плохая новость — regret to say."),
    c("v3-surgery", 3, "Do you ever regret ___ surgery?", "Ты когда-нибудь жалеешь, что ушёл из хирургии?",
      ["leaving", "to leave"], "leaving", "Жалеть о сделанном — regret + -ing."),
    c("v3-wedding", 3, "She regrets ___ so much money on the wedding.", "Она жалеет, что потратила столько денег на свадьбу.",
      ["spending", "to spend"], "spending", "regret + -ing."),

    # 4 · try
    c("v4-stuck", 4, "The lid was stuck. I tried ___ it, but I couldn't.", "Крышку заело. Я пытался её открыть, но не смог.",
      ["to open", "opening"], "to open", "Старался, было трудно, — try to."),
    c("v4-bath", 4, "My back hurts. — Try ___ a hot bath.", "Спина болит. — Попробуй принять горячую ванну.",
      ["having", "to have"], "having", "Попробуй как способ — try + -ing."),
    c("v4-dizzy", 4, "If you feel dizzy, try ___ down for a few minutes.", "Если кружится голова, попробуйте полежать несколько минут.",
      ["lying", "to lie"], "lying", "Способ, вдруг поможет, — try + -ing."),
    c("v4-recall", 4, "Try ___ what happened before you fell.", "Постарайтесь вспомнить, что было перед падением.",
      ["to remember", "remembering"], "to remember", "Постарайтесь, это усилие, — try to."),
    c("v4-salt", 4, "Have you tried ___ less salt? It may help your blood pressure.", "Вы пробовали есть меньше соли? Может помочь давлению.",
      ["eating", "to eat"], "eating", "Попробовать способ — try + -ing."),
    c("v4-calm", 4, "I tried hard ___ calm.", "Я изо всех сил старался сохранять спокойствие.",
      ["to stay", "staying"], "to stay", "Tried hard — усилие: try to."),

    # 5 · stop
    c("v5-brother", 5, "He stopped ___ to his brother after the argument.", "После ссоры он перестал разговаривать с братом.",
      ["talking", "to talk"], "talking", "Перестал — stop + -ing."),
    c("v5-colleague", 5, "On the way to the ward, she stopped ___ to a colleague.", "По дороге в отделение она остановилась поболтать с коллегой.",
      ["to chat", "chatting"], "to chat", "Остановилась, чтобы, — stop to."),
    c("v5-warfarin", 5, "Stop ___ warfarin five days before the operation.", "Прекратите принимать варфарин за пять дней до операции.",
      ["taking", "to take"], "taking", "Прекратить — stop + -ing."),
    c("v5-alcohol", 5, "He stopped ___ alcohol after his heart attack.", "После инфаркта он бросил пить.",
      ["drinking", "to drink"], "drinking", "Бросил — stop + -ing."),
    c("v5-petrol", 5, "We stopped ___ petrol on the way.", "По пути мы остановились заправиться.",
      ["to get", "getting"], "to get", "Остановились, чтобы, — stop to."),
    c("v5-worry", 5, "Stop ___ — everything will be fine.", "Перестань волноваться — всё будет хорошо.",
      ["worrying", "to worry"], "worrying", "Перестань — stop + -ing."),

    # 6 · go on, mean
    c("v6-talking", 6, "He ignored me and went on ___.", "Он не обратил на меня внимания и продолжал говорить.",
      ["talking", "to talk"], "talking", "Продолжал то же — go on + -ing."),
    c("v6-neurologist", 6, "After medical school, she went on ___ a neurologist.", "После медицинского она стала неврологом.",
      ["to become", "becoming"], "to become", "Потом, следующий шаг — go on to."),
    c("v6-results", 6, "He described the method and went on ___ the results.", "Он описал метод, а затем перешёл к результатам.",
      ["to discuss", "discussing"], "to discuss", "Перешёл к следующему — go on to."),
    c("v6-window", 6, "Missing the window means ___ the chance of thrombolysis.", "Пропустить окно — значит лишиться шанса на тромболизис.",
      ["losing", "to lose"], "losing", "Означает — mean + -ing."),
    c("v6-wake", 6, "Sorry, I didn't mean ___ you.", "Извини, не хотел тебя будить.",
      ["to wake", "waking"], "to wake", "Не хотел — didn't mean to."),
    c("v6-weekends", 6, "The new job will mean ___ at weekends.", "Новая работа — это работа по выходным.",
      ["working", "to work"], "working", "Означает — mean + -ing."),

    # 7 · need, like, prefer
    c("v7-lab", 7, "I need ___ the lab about these results.", "Мне надо позвонить в лабораторию насчёт этих результатов.",
      ["to call", "calling"], "to call", "Надо сделать самому — need to."),
    c("v7-car", 7, "The car needs ___.", "Машину надо помыть.",
      ["washing", "to wash"], "washing", "Надо, чтобы помыли, — needs + -ing."),
    c("v7-seat", 7, "Would you like ___ a seat?", "Не хотите присесть?",
      ["to take", "taking"], "to take", "Would like — только to."),
    c("v7-prefer", 7, "I prefer walking ___ driving.", "Я больше люблю ходить пешком, чем ездить.",
      ["to", "than", "from"], "to", "prefer doing to doing."),
    c("v7-rather", 7, "I'd rather ___ at home tonight.", "Я бы лучше остался сегодня дома.",
      ["stay", "to stay", "staying"], "stay", "Would rather — без to."),
    c("v7-exercise", 7, "You need ___ more exercise.", "Вам нужно больше двигаться.",
      ["to take", "taking"], "to take", "Надо самому — need to."),

    # 8 · see sb do / doing
    c("v8-fall", 8, "I saw the patient ___ and hit his head.", "Я видел, как пациент упал и ударился головой.",
      ["fall", "to fall", "fell"], "fall", "Видел действие целиком — see кого + глагол без to."),
    c("v8-help", 8, "I could hear someone ___ for help.", "Я слышал, как кто-то звал на помощь.",
      ["shouting", "to shout"], "shouting", "Слышал, как шло действие, — -ing. To после hear не бывает."),
    c("v8-clot", 8, "We watched the surgeon ___ the clot.", "Мы смотрели, как хирург удалил тромб.",
      ["remove", "to remove", "removed"], "remove", "watch кого + глагол без to."),
    c("v8-leg", 8, "Did you notice him ___ his leg when he walked in?", "Ты заметил, что он приволакивал ногу, когда вошёл?",
      ["dragging", "to drag"], "dragging", "Заметил, как шло действие, — -ing."),
    c("v8-door", 8, "I heard the door ___.", "Я слышал, как закрылась дверь.",
      ["close", "to close", "closed"], "close", "hear кого-что + глагол без to."),

    # 9 · afraid, sorry, interested
    c("v9-stick", 9, "She walks with a stick because she's afraid ___.", "Она ходит с тростью, потому что боится упасть.",
      ["of falling", "to fall"], "of falling", "Боится, что случится само, — afraid of + -ing."),
    c("v9-late", 9, "Sorry ___ late yesterday.", "Извини, что вчера опоздал.",
      ["for being", "to be"], "for being", "Извиняюсь за прошлое — sorry for + -ing."),
    c("v9-phd", 9, "I'm interested ___ a PhD.", "Мне интересно было бы написать диссертацию.",
      ["in doing", "to do"], "in doing", "Интересуюсь, хочу — interested in + -ing."),
    c("v9-hear", 9, "I was interested ___ that the trial had been stopped.", "Мне было интересно узнать, что исследование остановили.",
      ["to hear", "in hearing"], "to hear", "Было интересно узнать — interested to hear."),
    c("v9-independence", 9, "He's afraid ___ his independence after the stroke.", "Он боится потерять самостоятельность после инсульта.",
      ["of losing", "to lose"], "of losing", "Боится, что случится, — afraid of + -ing."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
    for o, note in (k.get("also") or {}).items():
        assert o in k["opts"] and o != k["a"] and "тоже" not in note, k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
