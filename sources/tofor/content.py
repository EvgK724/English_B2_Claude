# Содержание приложения «to / for».
# В примерах: {…} — to (синий), […] — for (оранжевый), |…| — глагол без to (зелёный).

SORT_TOPIC = 10
MIXED_TOPIC = 11

# Шпаргалка: группы по смыслу. * — бывает и с to, и с for.
TO_GROUPS = [
    {"ru": "отдаю, передаю", "verbs": ["give", "hand", "pass", "lend", "sell", "pay", "owe", "feed"]},
    {"ru": "предлагаю, обещаю", "verbs": ["offer", "promise"]},
    {"ru": "отправляю, несу, бросаю", "verbs": ["send", "post", "take", "bring*", "throw", "write"]},
    {"ru": "показываю, рассказываю, учу", "verbs": ["show", "tell", "read", "teach"]},
    {"ru": "никогда без to", "verbs": ["explain", "describe", "say", "suggest", "mention", "report", "introduce", "repeat"]},
]
FOR_GROUPS = [
    {"ru": "покупаю, заказываю, бронирую", "verbs": ["buy", "order", "book", "reserve"]},
    {"ru": "делаю, готовлю, строю", "verbs": ["make", "cook", "build"]},
    {"ru": "ищу, достаю, приношу", "verbs": ["find", "get", "fetch", "bring*"]},
    {"ru": "выбираю", "verbs": ["choose", "pick"]},
    {"ru": "оставляю, берегу", "verbs": ["leave", "save"]},
]

# Одно слово — to или for: предлог | когда | пример
MULTI = [
    {"verb": "bring", "rows": [
        ["to", "принести кому, передать", "bring the notes {to} me"],
        ["for", "для кого, в подарок", "flowers [for] the nurses"]]},
    {"verb": "pay", "rows": [
        ["to", "заплатить кому", "pay the fee {to} the clinic"],
        ["for", "заплатить за что", "pay [for] the scan"]]},
    {"verb": "write", "rows": [
        ["to", "написать кому", "write {to} your GP"],
        ["for", "писать для издания", "write [for] a journal"]]},
    {"verb": "leave", "rows": [
        ["for", "оставить кому", "a note [for] the night team"],
        ["to", "завещать", "left the house {to} his son"]]},
]

# Без to: после чего | пример | пояснение
BARE = [
    ["can, must, should, might…", "you must |sign|", "модальные"],
    ["had better", "you'd better |rest|", "лучше бы"],
    ["would rather", "I'd rather |wait|", "предпочёл бы"],
    ["make + кого", "made him |wait|", "заставил"],
    ["let + кого", "let me |explain|", "позволь"],
    ["help + кого", "help me (to) |lift|", "to можно опустить"],
    ["see, hear + кого", "saw him |fall|", "видел, как…"],
]
WITH_TO = ["would like to", "would prefer to", "ought to", "have to", "need to", "be able to"]

# Частые ошибки русскоговорящих: неверно | верно | почему
ERRORS = [
    ["explain me the plan", "explain the plan to me", "«объясни мне» — explain to me"],
    ["say me", "tell me / say to me", "say — только с to"],
    ["pay the scan", "pay for the scan", "«оплатить что» — pay for"],
    ["you'd better to go", "you'd better go", "had better — без to"],
    ["make him to wait", "make him wait", "make — без to"],
    ["let me to explain", "let me explain", "let — без to"],
]

TOPICS = [
    {"n": 1, "title": "to — кому: вещь переходит",
     "rule": "to — вещь переходит к человеку: отдаю в руки, отправляю, приношу, показываю, говорю. Схема: глагол + что + to + кому: give the leaflet to the patient. Так работают give, hand, pass, lend, sell, pay, owe, offer, promise, feed, send, post, take, throw, write, show, tell, read, teach.",
     "ex": [
         {"en": "Please give the leaflet {to} the patient.", "ru": "Пожалуйста, дайте пациенту листовку."},
         {"en": "Can you send the results {to} my GP?", "ru": "Можете отправить результаты моему терапевту?"},
         {"en": "Could you show the scan {to} the family?", "ru": "Покажите, пожалуйста, снимок родственникам."},
     ]},
    {"n": 2, "title": "for — для кого: делаю ради",
     "rule": "for — делаю что-то ради человека, для него, вместо него: покупаю, готовлю, ищу, бронирую. Вещь не «летит» к нему в руки — я стараюсь для него. Схема: глагол + что + for + кому: buy a coffee for her. Так работают buy, get, order, book, reserve, make, cook, build, find, fetch, choose, pick, leave, save.",
     "ex": [
         {"en": "I'll get a chair [for] you.", "ru": "Сейчас принесу вам стул."},
         {"en": "Can you book a taxi [for] Mr Smith?", "ru": "Можете заказать такси для мистера Смита?"},
         {"en": "She saved a seat [for] me at the meeting.", "ru": "Она заняла мне место на собрании."},
     ]},
    {"n": 3, "title": "Только с to: explain, describe, say",
     "rule": "explain, describe, say, suggest, mention, report, introduce, repeat — только «что + to + кому». Человека сразу после них не ставят: explain the plan to me — не explain me the plan. По-русски «объясни мне», по-английски explain to me. И say — с to (say to me), а tell — без предлога (tell me).",
     "ex": [
         {"en": "Can you explain the procedure {to} me?", "ru": "Можете объяснить мне процедуру?"},
         {"en": "Describe the pain {to} the doctor.", "ru": "Опишите врачу боль."},
         {"en": "Let me introduce you {to} Dr Petrova.", "ru": "Позвольте представить вас доктору Петровой."},
     ]},
    {"n": 4, "title": "Одно слово — to или for",
     "rule": "bring to — принести кому, передать; bring for — принести для кого, в подарок. pay to — заплатить кому; pay for — заплатить за что: pay for the scan, не pay the scan. write to — написать кому; write for — писать для издания. leave for — оставить кому; leave to — завещать.",
     "ex": [
         {"en": "Bring the notes {to} me, please.", "ru": "Принесите мне записи, пожалуйста."},
         {"en": "They brought flowers [for] the nurses.", "ru": "Они принесли цветы для медсестёр."},
         {"en": "Who pays [for] the scan?", "ru": "Кто платит за КТ?"},
     ]},
    {"n": 5, "title": "Порядок слов: кому + что",
     "rule": "У этих глаголов два порядка слов. Человек сразу после глагола — без предлога: give the patient the leaflet, buy her a coffee. Вещь первой — предлог нужен: give the leaflet to the patient, buy a coffee for her. С it и them — только второй вариант: give it to him, а не give him it.",
     "ex": [
         {"en": "Could you give me the file?", "ru": "Дайте мне, пожалуйста, папку."},
         {"en": "Could you give it {to} me?", "ru": "Дайте её мне, пожалуйста."},
         {"en": "Let me buy you a coffee.", "ru": "Давай я куплю тебе кофе."},
     ]},
    {"n": 6, "title": "Модальные — без to",
     "rule": "После модальных — can, could, must, should, may, might, will, would, shall — сразу глагол без to: you must sign, he can't lift. Ловушка — похожие конструкции с to: ought to, have to, need to, be able to. Их помни отдельно.",
     "ex": [
         {"en": "You must |sign| the consent form.", "ru": "Вы должны подписать согласие."},
         {"en": "He can't |lift| his left arm.", "ru": "Он не может поднять левую руку."},
         {"en": "You ought {to} rest for a few days.", "ru": "Вам стоит отдохнуть несколько дней."},
     ]},
    {"n": 7, "title": "had better, would rather, would like",
     "rule": "had better — «лучше бы», совет с намёком на последствия, и would rather — «я бы предпочёл» — без to: you'd better rest, I'd rather wait. Отрицание — not перед глаголом: you'd better not drive. А would like и would prefer — с to: I'd like to see the results.",
     "ex": [
         {"en": "You'd better |rest| for a couple of days.", "ru": "Вам бы лучше пару дней отдохнуть."},
         {"en": "I'd rather |wait| for the MRI.", "ru": "Я бы лучше подождал МРТ."},
         {"en": "I'd like {to} see the results.", "ru": "Я бы хотел посмотреть результаты."},
     ]},
    {"n": 8, "title": "make, let, help",
     "rule": "make + кого + глагол без to — «заставить»: they made him wait. let + кого + глагол без to — «позволить»: let me explain. help — и так и так: help me lift или help me to lift. Сверх уровня: в пассиве to возвращается — he was made to wait; у let пассива нет, говорят was allowed to.",
     "ex": [
         {"en": "The pain made him |stop|.", "ru": "Боль заставила его остановиться."},
         {"en": "Let me |explain| the results.", "ru": "Позвольте, я объясню результаты."},
         {"en": "Can you help me |move| the bed?", "ru": "Поможете мне передвинуть кровать?"},
     ]},
    {"n": 9, "title": "see, hear + кого + do",
     "rule": "see, hear, watch, notice + кого + глагол без to — видел или слышал всё действие целиком: I saw him fall. С -ing — действие в процессе, застал его кусочек: I heard someone calling. С to после них не бывает.",
     "ex": [
         {"en": "I saw him |fall| in the corridor.", "ru": "Я видел, как он упал в коридоре."},
         {"en": "I heard someone |calling| for help.", "ru": "Я слышал, как кто-то звал на помощь."},
     ]},
    {"n": SORT_TOPIC, "title": "Быстрая проверка: to или for",
     "rule": "Короткие фразы по спискам с листков: видишь глагол — выбираешь to или for. Под фразой — перевод. Правило одно: вещь переходит к человеку — to, делаю ради человека — for.",
     "ex": []},
    {"n": MIXED_TOPIC, "title": "Итог — всё вместе",
     "rule": "Пятнадцать случайных предложений из тем 1–9 вперемешку.",
     "ex": []},
]

CARDS = [
    # 1 — to
    {"id": "to-hand", "t": 1, "q": "Please hand the chart ___ the consultant.", "opts": ["to", "for"], "a": "to",
     "why": "hand — передать в руки: вещь переходит, значит to."},
    {"id": "to-send", "t": 1, "q": "I'll send the discharge letter ___ your GP.", "opts": ["to", "for"], "a": "to",
     "why": "send — отправить кому: to."},
    {"id": "to-lend", "t": 1, "q": "Could you lend your stethoscope ___ the student?", "opts": ["to", "for"], "a": "to",
     "why": "lend — одолжить кому: to."},
    {"id": "to-owe", "t": 1, "q": "I think we owe an apology ___ the family.", "opts": ["to", "for"], "a": "to",
     "why": "owe — быть должным кому: to."},
    {"id": "to-show", "t": 1, "q": "Show your wristband ___ the nurse, please.", "opts": ["to", "for"], "a": "to",
     "why": "show — показать кому: to."},
    {"id": "to-offer", "t": 1, "q": "The hospital offered the job ___ a young neurologist.", "opts": ["to", "for"], "a": "to",
     "why": "offer — предложить кому: to."},

    # 2 — for
    {"id": "for-find", "t": 2, "q": "We're trying to find a bed ___ him.", "opts": ["for", "to"], "a": "for",
     "why": "find — найти для кого: for."},
    {"id": "for-order", "t": 2, "q": "Can you order an MRI ___ Mrs Jones?", "opts": ["for", "to"], "a": "for",
     "why": "order — заказать для кого: for."},
    {"id": "for-make", "t": 2, "q": "Could you make a copy of the ECG ___ me?", "opts": ["for", "to"], "a": "for",
     "why": "make — сделать для кого: for."},
    {"id": "for-leave", "t": 2, "q": "I've left some sandwiches ___ the night team.", "opts": ["for", "to"], "a": "for",
     "why": "leave — оставить для кого: for."},
    {"id": "for-cook", "t": 2, "q": "Her husband cooks ___ her every evening.", "opts": ["for", "to"], "a": "for",
     "why": "cook — готовить для кого: for."},
    {"id": "for-fetch", "t": 2, "q": "Could you fetch a wheelchair ___ him?", "opts": ["for", "to"], "a": "for",
     "why": "fetch — сходить и принести для кого: for."},

    # 3 — только с to
    {"id": "only-explain", "t": 3, "q": "Could you explain ___ how the drug works?", "opts": ["to me", "me"], "a": "to me",
     "why": "explain to me — «объясни мне»; без to нельзя."},
    {"id": "only-describe", "t": 3, "q": "Please describe the pain ___ the doctor.", "opts": ["to", ""], "a": "to",
     "why": "describe — только «что + to + кому»."},
    {"id": "only-told", "t": 3, "q": "He ___ me that he felt fine.", "opts": ["told", "said"], "a": "told",
     "why": "tell + кому без предлога; say — только say to me."},
    {"id": "only-say", "t": 3, "q": "What did she ___ to you?", "opts": ["say", "tell"], "a": "say",
     "why": "say to you — с to; tell you — без to."},
    {"id": "only-introduce", "t": 3, "q": "Let me introduce you ___ our new registrar.", "opts": ["to", "for", ""], "a": "to",
     "why": "introduce — представить кому: to."},
    {"id": "only-report", "t": 3, "q": "Report any side effects ___ your doctor.", "opts": ["to", "for"], "a": "to",
     "why": "report — сообщить кому: to."},

    # 4 — одно слово: to или for
    {"id": "two-pay-for", "t": 4, "q": "Who's going to pay ___ the scan?", "opts": ["for", "to"], "a": "for",
     "why": "pay for — заплатить за что. Pay the scan — ошибка."},
    {"id": "two-pay-to", "t": 4, "q": "Please pay the deposit ___ the receptionist.", "opts": ["to", "for"], "a": "to",
     "why": "pay to — отдать деньги кому."},
    {"id": "two-leave", "t": 4, "q": "I've left the keys ___ you at reception.", "opts": ["for", "to"], "a": "for",
     "why": "leave for — оставить кому; leave to — завещать."},
    {"id": "two-write", "t": 4, "q": "I'll write ___ your GP about the new tablets.", "opts": ["to", "for"], "a": "to",
     "why": "write to — написать кому."},
    {"id": "two-bring", "t": 4, "q": "She brought chocolates ___ the nurses.", "opts": ["for", "to"], "a": "for",
     "also": {"to": "brought them to the nurses — принесла и вручила им"},
     "why": "bring for — принести для кого, в подарок."},

    # 5 — порядок слов
    {"id": "wo-give", "t": 5, "q": "Could you give ___ the leaflet?", "opts": ["the patient", "to the patient"], "a": "the patient",
     "why": "Человек сразу после глагола — без to."},
    {"id": "wo-it", "t": 5, "q": "The leaflet? Please give ___.", "opts": ["it to him", "him it"], "a": "it to him",
     "why": "С it и them — вещь первой и to: give it to him."},
    {"id": "wo-buy", "t": 5, "q": "Let me buy ___ a coffee.", "opts": ["you", "for you"], "a": "you",
     "why": "buy you a coffee — человек сразу после глагола, без for."},
    {"id": "wo-send", "t": 5, "q": "Can you send ___ the results by email?", "opts": ["me", "to me"], "a": "me",
     "why": "send me the results = send the results to me."},
    {"id": "wo-them", "t": 5, "q": "The scans are ready — can you show ___?", "opts": ["them to the family", "the family them"], "a": "them to the family",
     "why": "С them — только show them to the family."},

    # 6 — модальные
    {"id": "mv-must", "t": 6, "q": "You must ___ the consent form before the procedure.", "opts": ["sign", "to sign"], "a": "sign",
     "why": "После must — глагол без to."},
    {"id": "mv-cant", "t": 6, "q": "He can't ___ his left arm.", "opts": ["lift", "to lift"], "a": "lift",
     "why": "После can — без to."},
    {"id": "mv-should", "t": 6, "q": "Patients should ___ nothing for six hours before surgery.", "opts": ["eat", "to eat"], "a": "eat",
     "why": "После should — без to."},
    {"id": "mv-ought", "t": 6, "q": "You ought ___ see a neurologist.", "opts": ["to", ""], "a": "to",
     "why": "ought to — модальный, но с to."},
    {"id": "mv-have", "t": 6, "q": "You don't have ___ fast before this test.", "opts": ["to", ""], "a": "to",
     "why": "have to — «приходится»: с to."},
    {"id": "mv-able", "t": 6, "q": "He'll be able ___ walk with a stick.", "opts": ["to", ""], "a": "to",
     "why": "be able to — с to."},

    # 7 — had better, would rather, would like
    {"id": "hb-see", "t": 7, "q": "You'd better ___ a doctor about that headache.", "opts": ["see", "to see", "seeing"], "a": "see",
     "why": "had better — без to."},
    {"id": "hb-not", "t": 7, "q": "You'd better ___ drive today.", "opts": ["not", "not to", "don't"], "a": "not",
     "why": "Отрицание: had better not + глагол."},
    {"id": "wr-wait", "t": 7, "q": "I'd rather ___ for the MRI.", "opts": ["wait", "to wait", "waiting"], "a": "wait",
     "why": "would rather — без to."},
    {"id": "wr-not", "t": 7, "q": "I'd rather ___ this on the phone.", "opts": ["not discuss", "not to discuss", "don't discuss"], "a": "not discuss",
     "why": "Отрицание: would rather not + глагол."},
    {"id": "wl-like", "t": 7, "q": "I'd like ___ the consultant, please.", "opts": ["to see", "see", "seeing"], "a": "to see",
     "why": "would like — с to, в отличие от would rather."},
    {"id": "wl-prefer", "t": 7, "q": "I'd prefer ___ until the results come back.", "opts": ["to wait", "wait"], "a": "to wait",
     "why": "would prefer — с to: I'd prefer to wait = I'd rather wait."},

    # 8 — make, let, help
    {"id": "ml-made", "t": 8, "q": "They made him ___ for four hours in A&E.", "opts": ["wait", "to wait"], "a": "wait",
     "why": "make + кого + глагол без to."},
    {"id": "ml-let", "t": 8, "q": "Let me ___ the results first.", "opts": ["check", "to check"], "a": "check",
     "why": "let + кого + глагол без to."},
    {"id": "ml-go", "t": 8, "q": "We can't let the patient ___ home alone.", "opts": ["go", "to go"], "a": "go",
     "why": "let — без to."},
    {"id": "ml-help", "t": 8, "q": "Could you help me ___ the patient?", "opts": ["move", "to move"], "a": "move",
     "also": {"to move": "после help to можно и оставить, и опустить"},
     "why": "help — и с to, и без."},
    {"id": "ml-passive", "t": 8, "q": "He was made ___ for four hours.", "opts": ["to wait", "wait"], "a": "to wait",
     "why": "Сверх уровня: в пассиве make берёт to."},
    {"id": "ml-allowed", "t": 8, "q": "Visitors ___ to stay after 8 pm.", "opts": ["aren't allowed", "aren't let"], "a": "aren't allowed",
     "why": "У let нет пассива — говорят be allowed to."},

    # 9 — see, hear
    {"id": "sh-fall", "t": 9, "q": "I saw him ___ in the corridor.", "opts": ["fall", "to fall"], "a": "fall",
     "why": "see + кого + глагол без to — видел всё действие."},
    {"id": "sh-alarm", "t": 9, "q": "Did you hear the alarm ___ off?", "opts": ["go", "to go"], "a": "go",
     "why": "hear + что + глагол без to."},
    {"id": "sh-calling", "t": 9, "q": "I could hear someone ___ for help.", "opts": ["calling", "to call"], "a": "calling",
     "why": "-ing — слышал в процессе; to после hear не бывает."},
    {"id": "sh-leave", "t": 9, "q": "Nobody noticed him ___ the ward.", "opts": ["leave", "to leave"], "a": "leave",
     "why": "notice + кого + глагол без to."},
]

# 10 — быстрая проверка по спискам: глагол | фраза | перевод фразы | перевод глагола
SORT_TO = [
    ["give", "give the leaflet ___ her", "дать ей листовку", "дать"],
    ["hand", "hand the chart ___ me", "передать мне карту", "передать в руки"],
    ["pass", "pass the notes ___ him", "передать ему записи", "передать"],
    ["lend", "lend my pen ___ him", "одолжить ему ручку", "одолжить"],
    ["sell", "sell the car ___ a friend", "продать машину другу", "продать"],
    ["pay", "pay the fee ___ the clinic", "заплатить взнос клинике", "заплатить кому"],
    ["owe", "owe money ___ the bank", "быть должным банку", "быть должным"],
    ["offer", "offer a seat ___ her", "предложить ей место", "предложить"],
    ["promise", "promise the job ___ her", "пообещать ей работу", "пообещать"],
    ["feed", "feed the leftovers ___ the dog", "скормить остатки собаке", "скормить"],
    ["send", "send the results ___ the GP", "отправить результаты терапевту", "отправить"],
    ["post", "post the letter ___ him", "отправить ему письмо почтой", "отправить почтой"],
    ["take", "take the samples ___ the lab", "отнести образцы в лабораторию", "отнести"],
    ["throw", "throw the ball ___ me", "бросить мне мяч", "бросить"],
    ["write", "write a letter ___ her", "написать ей письмо", "написать"],
    ["show", "show the scan ___ the family", "показать снимок родственникам", "показать"],
    ["tell", "tell the truth ___ the patient", "сказать пациенту правду", "сказать"],
    ["read", "read a story ___ the kids", "почитать детям сказку", "прочитать вслух"],
    ["teach", "teach English ___ nurses", "преподавать английский медсёстрам", "учить, преподавать"],
]
SORT_FOR = [
    ["buy", "buy a coffee ___ her", "купить ей кофе", "купить"],
    ["get", "get a glass of water ___ him", "принести ему стакан воды", "достать, принести"],
    ["order", "order a taxi ___ him", "заказать ему такси", "заказать"],
    ["book", "book a table ___ us", "забронировать нам столик", "забронировать"],
    ["reserve", "reserve a parking space ___ him", "зарезервировать ему парковку", "зарезервировать"],
    ["make", "make a copy ___ me", "сделать мне копию", "сделать"],
    ["cook", "cook dinner ___ the family", "приготовить ужин для семьи", "приготовить"],
    ["build", "build a ramp ___ wheelchair users", "построить пандус для колясочников", "построить"],
    ["find", "find a bed ___ him", "найти ему койку", "найти"],
    ["fetch", "fetch a chair ___ her", "сходить за стулом для неё", "сходить и принести"],
    ["choose", "choose a gift ___ her", "выбрать ей подарок", "выбрать"],
    ["pick", "pick some flowers ___ her", "нарвать ей цветов", "выбрать, сорвать"],
    ["leave", "leave the keys ___ her", "оставить ей ключи", "оставить"],
    ["save", "save a seat ___ me", "занять мне место", "приберечь, занять"],
]
for kind, rows in (("to", SORT_TO), ("for", SORT_FOR)):
    for verb, phrase, ru, vru in rows:
        other = "for" if kind == "to" else "to"
        rule = "вещь переходит к человеку — to." if kind == "to" else "делаю ради человека — for."
        CARDS.append({"id": "v-" + kind + "-" + verb, "t": SORT_TOPIC, "q": phrase, "ru": ru,
                      "opts": [kind, other], "a": kind, "why": f"{verb} — {vru}: {rule}"})
