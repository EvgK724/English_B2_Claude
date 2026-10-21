# Содержание тренажёра «What is it for?»: предлог в конце вопроса. Вопросительное слово уходит вперёд, а предлог остаётся
# при своём глаголе или прилагательном: What is it for? Who are you waiting for? What are you afraid of? Where are you from?
# Короткие переспросы (Who with? What about?), пассив (What is he being treated for?), официальный вариант с предлогом
# впереди (To whom…? On which data…?), косвенные вопросы и «который» (the patient I told you about).
# Отличие от соседей: в «Вопросах» (q) — одна тема «Предлог в конце» на шесть карточек; в «Прилагательных с предлогами»
# (adjprep) — какой предлог; здесь — куда он встаёт в вопросе. Примеры — из жизни и из больницы.
# Разметка в примерах: [слово|a] — предлог в конце (оранжевый), [слово|b] — вопросительное слово (синий),
# [слово|c] — официальный вариант, предлог впереди (зелёный). Темы с полем late вступают в общую тренировку позже.

MIXED_TOPIC = 9

GROUPS = {
    "b1": "B1 — What … for, wait for, afraid of, where from",
    "b1p": "B1+ — Who with?, пассив",
    "b2": "B2 — To whom, косвенные вопросы",
    "mix": "Итог",
}

# Главная таблица: образец | правило («главное — пояснение») | примеры
TABLE = [
    ["What is it for?", "для чего, от чего, зачем — What … for?", "What's this tablet for? · What do you need it for?"],
    ["Who are you waiting for?", "предлог глагола — в конце: wait for, look at, talk to", "What are you looking at? · Who did you talk to?"],
    ["What are you afraid of?", "предлог прилагательного — тоже в конце", "allergic to · worried about · married to"],
    ["Where are you from?", "откуда — from нужен, куда — to обычно не ставят", "Where does it come from? · What floor is it on?"],
    ["Who with? What about?", "короткий переспрос — слово и предлог", "Who with? · What about? · Who for?"],
    ["What is he treated for?", "пассив — предлог тоже в конце", "What is it used for? · Who was it written by?"],
    ["To whom…? On which…?", "официально — предлог впереди, после него whom, which", "To whom should it be sent? · On which data…?"],
    ["I don't know what it's for", "косвенный вопрос и «который» — предлог в конце", "the patient I told you about · That's what it's for"],
]

# Мини-диалоги: строки [английский, перевод]
CONTRAST = [
    [["— What's this tablet [for|a]?", "От чего эта таблетка?"],
     ["— It's for your blood pressure.", "От давления."]],
    [["— I'm going out tonight.", "Я вечером ухожу."],
     ["— Oh? [Who|b] [with|a]?", "Да? С кем?"]],
    [["— [Who|b] are you waiting [for|a]?", "Кого вы ждёте?"],
     ["— Dr Patel. My appointment is at ten.", "Доктора Пател, у меня приём на десять."]],
    [["— [What|b] are you allergic [to|a]?", "На что у вас аллергия?"],
     ["— Penicillin. I get a rash.", "На пенициллин — появляется сыпь."]],
    [["— [What|b] did you do that [for|a]?", "Ну и зачем ты это сделал?"],
     ["— Sorry, I thought it would help.", "Извини, думал, так будет лучше."]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["For what do you need it?", "What do you need it for?", "для чего — What … for?, for в конце"],
    ["Whom are you waiting?", "Who are you waiting for?", "wait for — предлог не теряется"],
    ["What are you looking?", "What are you looking at?", "смотреть на — look at"],
    ["From where are you?", "Where are you from?", "откуда — Where … from?"],
    ["Who you were talking to?", "Who were you talking to?", "в вопросе вспомогательный глагол — перед подлежащим"],
    ["What are you afraid?", "What are you afraid of?", "afraid of — без of нельзя"],
    ["With who did you go?", "Who did you go with?", "впереди — только With whom, и это официально"],
    ["What is this drug used?", "What is this drug used for?", "be used for — для чего применяют"],
    ["Could you tell me what is this for?", "Could you tell me what this is for?", "косвенный вопрос — прямой порядок, for в конце"],
    ["About what are you talking?", "What are you talking about?", "talk about — предлог в конце"],
]

TOPICS = [
    {"n": 1, "group": "b1", "title": "What is it for?", "sub": "для чего, от чего, зачем",
     "rule": "Для чего, от чего, зачем — What … for? What в начале, for в конце: What's this tablet for? — It's for high blood pressure. What do you need the car for? — зачем тебе машина. Отвечают for + существительное или -ing (It's for measuring pressure) либо to do (To rule out an infection). For what is it? — так не говорят, хотя по-русски «для чего» стоит впереди. What did you do that for? — «зачем ты это сделал?», часто с упрёком.",
     "ex": [
         {"en": "— [What|b]'s this tablet [for|a]? — It's for high blood pressure.", "ru": "— От чего эта таблетка? — От давления."},
         {"en": "[What|b] do you need the scan [for|a]?", "ru": "Зачем вам этот снимок?"},
         {"en": "— [What|b] are these tests [for|a]? — To rule out an infection.", "ru": "— Для чего эти анализы? — Чтобы исключить инфекцию."},
     ]},
    {"n": 2, "group": "b1", "title": "Who are you waiting for?", "sub": "предлог глагола — в конце",
     "rule": "Предлог принадлежит глаголу: wait for, look at, talk to, listen to, depend on. Вопрос строят в три шага: утверждение You're waiting for someone → someone меняем на who и выносим вперёд → вспомогательный глагол перед подлежащим: Who are you waiting for? Предлог при этом остаётся на месте — в конце. По-русски «Кого вы ждёте?» — без предлога, а в английском for обязателен: Who are you waiting? — ошибка. Look at — смотреть на, look for — искать.",
     "ex": [
         {"en": "[Who|b] are you waiting [for|a]?", "ru": "Кого вы ждёте?"},
         {"en": "[What|b] are you looking [at|a]?", "ru": "На что ты смотришь?"},
         {"en": "[What|b] does the dose depend [on|a]?", "ru": "От чего зависит доза?"},
     ]},
    {"n": 3, "group": "b1", "title": "What are you afraid of?", "sub": "предлог прилагательного",
     "rule": "У прилагательных свои предлоги: afraid of, allergic to, worried about, interested in, good at, married to, responsible for. В вопросе они тоже уходят в конец: What are you afraid of? What are you allergic to? По-русски часто без предлога («Чего вы боитесь?») или с другим («аллергия на», «замужем за») — поэтому предлог теряют или берут не тот. Married to, не married with; allergic to, не allergic on.",
     "ex": [
         {"en": "[What|b] are you allergic [to|a]?", "ru": "На что у вас аллергия?"},
         {"en": "[What|b] are you so worried [about|a]?", "ru": "Что вас так тревожит?"},
         {"en": "[Who|b] is she married [to|a]?", "ru": "За кем она замужем?"},
     ]},
    {"n": 4, "group": "b1", "title": "Where are you from?", "sub": "откуда, где, на каком этаже",
     "rule": "Where … from? — откуда, from обязателен: Where are you from? Where does the bleeding come from? Куда — просто Where are you going?, to обычно не ставят: where уже значит «куда». Which и what + существительное — предлог тоже в конце: What floor is the lab on? Which hospital does she work at? How long … for? — for можно поставить или опустить: How long are you staying (for)? До какого часа — What time … until?",
     "ex": [
         {"en": "[Where|b] does the bleeding come [from|a]?", "ru": "Откуда идёт кровотечение?"},
         {"en": "[What floor|b] is the MRI unit [on|a]?", "ru": "На каком этаже МРТ?"},
         {"en": "[How long|b] are you staying [for|a]?", "ru": "Надолго вы к нам?"},
     ]},
    {"n": 5, "group": "b1p", "title": "Who with? What about?", "sub": "короткий переспрос", "late": 0.2,
     "rule": "В разговоре переспрашивают коротко: вопросительное слово и предлог — Who with? (с кем?), What about? (о чём?), Who for? (для кого?), Where to? (куда?), Where from? (откуда?), What for? (зачем?). Предлог берут из той фразы, которую услышали: I'm going out → Who with? We need to talk → What about? Варианты с предлогом впереди (About what? With whom?) тоже бывают, но звучат резче или официальнее.",
     "ex": [
         {"en": "— I'm meeting someone for lunch. — [Who|b] [with|a]?", "ru": "— Я обедаю кое с кем. — С кем?"},
         {"en": "— Can I talk to you? — Sure. [What|b] [about|a]?", "ru": "— Можно с вами поговорить? — Конечно. О чём?"},
         {"en": "— I bought some flowers. — [Who|b] [for|a]?", "ru": "— Я купил цветы. — Для кого?"},
     ]},
    {"n": 6, "group": "b1p", "title": "What is he being treated for?", "sub": "пассив: предлог тоже в конце", "late": 0.25,
     "rule": "В пассиве предлог остаётся после причастия: be treated for, be used for, be referred to, be caused by, be written by. What is he being treated for? — от чего его лечат. Вопрос «кем, чем» — by в конце: Who was the guideline written by? What was the outbreak caused by? «Лечат от» — for, не from: treated for pneumonia. Compared with и compared to в статьях взаимозаменяемы.",
     "ex": [
         {"en": "[What|b] is he being treated [for|a]?", "ru": "От чего его лечат?"},
         {"en": "[What|b] is this drug mainly used [for|a]?", "ru": "Для чего в основном применяют этот препарат?"},
         {"en": "[Who|b] was the patient referred [to|a]?", "ru": "К кому направили пациента?"},
     ]},
    {"n": 7, "group": "b2", "title": "To whom…? On which…?", "sub": "официально — предлог впереди", "late": 0.45,
     "rule": "В официальном письме и научном тексте предлог можно поставить в начало: To whom should the form be sent? On which data was the analysis based? После такого предлога — только whom, which или what + существительное: With whom…?, не With who…? Предлог дважды (To whom … to?) — ошибка. В разговоре и обычной переписке это звучит натянуто — там предлог в конце: Who should I send it to? Устойчивые обороты — всегда с предлогом впереди: To what extent…? In what way…? For what reason…? Сочетания с особым смыслом (look after — присматривать) не разбивают: Which patient are you looking after?",
     "ex": [
         {"en": "[To whom|c] should the application be addressed?", "ru": "Кому адресовать заявление?"},
         {"en": "[On which|c] data was the analysis based?", "ru": "На каких данных основан анализ?"},
         {"en": "[To what extent|c] do these findings apply to older patients?", "ru": "В какой мере эти выводы применимы к пожилым пациентам?"},
     ]},
    {"n": 8, "group": "b2", "title": "I don't know what it's for", "sub": "косвенный вопрос и «который»", "late": 0.5,
     "rule": "В косвенном вопросе порядок прямой, а предлог по-прежнему в конце: Could you tell me what this button is for? I'm not sure who she works for. Так же в придаточном «который»: the patient (that) I told you about, the drug she's allergic to, the guidelines we rely on — that часто опускают. Официально предлог ставят перед which и whom: the guidelines on which we rely; после предлога that не бывает. Идиома: That's what friends are for — на то и друзья.",
     "ex": [
         {"en": "Could you tell me [what|b] this valve is [for|a]?", "ru": "Не подскажете, для чего этот клапан?"},
         {"en": "This is the patient I told you [about|a].", "ru": "Это тот пациент, о котором я вам рассказывал."},
         {"en": "These are the guidelines [on which|c] we rely.", "ru": "Вот рекомендации, на которые мы опираемся."},
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
    # 1 · What is it for?
    c("f1-inhaler", 1, "— What's this inhaler ___? — It's for asthma.", "— От чего этот ингалятор? — От астмы.",
      ["for", "from", "against"], "for", "Для чего, от чего — What's it for? «От астмы» — for asthma: from и against здесь не говорят."),
    c("f1-need", 1, "What do you need the car ___?", "Зачем тебе машина?",
      ["for", "to", "with"], "for", "Зачем — What do you need it for? То же, что Why do you need it?"),
    c("f1-order", 1, "___", "Для чего этот тест?",
      ["What is this test for?", "For what is this test?", "What for is this test?"], "What is this test for?",
      "What — в начале, for — в конце. For what is this test? — так не говорят, хотя по-русски «для чего» стоит впереди."),
    c("f1-tests", 1, "— What are these blood tests ___? — To rule out an infection.", "— Для чего эти анализы крови? — Чтобы исключить инфекцию.",
      ["for", "to", "about"], "for", "What … for? — для чего. Ответ — to do: To rule out an infection."),
    c("f1-did", 1, "What did you do that ___? Now we have to start again.", "Ну и зачем ты это сделал? Теперь начинать заново.",
      ["for", "to", "about"], "for", "What did you do that for? — «зачем ты это сделал?», часто с упрёком."),
    c("f1-answer", 1, "— What's this valve for? — ___", "— Для чего этот клапан?",
      ["It's for releasing pressure.", "It's for to release pressure.", "It's for release pressure."], "It's for releasing pressure.",
      "Ответ: for + -ing или for + существительное. For to do — ошибка; можно просто To release pressure."),

    # 2 · Who are you waiting for?
    c("f2-wait", 2, "Who are you waiting ___?", "Кого вы ждёте?",
      ["for", "to", "at"], "for", "wait for — ждать кого-то. По-русски «кого» без предлога, а for нужен."),
    c("f2-look", 2, "What are you looking ___? Is there something on my face?", "На что ты смотришь? У меня что-то на лице?",
      ["at", "on", "to"], "at", "Смотреть на — look at. Look for — искать."),
    c("f2-search", 2, "— What are you looking ___? — My car keys. I can't find them anywhere.", "— Что ты ищешь? — Ключи от машины, нигде не могу найти.",
      ["for", "at", "after"], "for", "Искать — look for. Look at — смотреть на, look after — присматривать."),
    c("f2-talk", 2, "Who were you talking ___ on the phone?", "С кем ты говорил по телефону?",
      ["to", "with", "at"], "to", "talk to — говорить с кем-то. Предлог в конце.",
      also={"with": "Тоже верно: talk with, чаще в американском английском."}),
    c("f2-send", 2, "___", "Кому вы отправили результаты?",
      ["Who did you send the results to?", "To who did you send the results?", "Who you sent the results to?"], "Who did you send the results to?",
      "Who — вперёд, did — перед подлежащим, to — в конце. To who — ошибка: после предлога в начале бывает только whom."),
    c("f2-depend", 2, "What does the dose depend ___?", "От чего зависит доза?",
      ["on", "of", "from"], "on", "depend on — зависеть от. «От» здесь — on, не from и не of."),

    # 3 · What are you afraid of?
    c("f3-afraid", 3, "What are you afraid ___?", "Чего ты боишься?",
      ["of", "from", "about"], "of", "afraid of — бояться чего-то. По-русски без предлога, но of обязателен."),
    c("f3-interested", 3, "What kind of research are you interested ___?", "Какими исследованиями вы интересуетесь?",
      ["in", "on", "about"], "in", "interested in — интересоваться. Предлог в конце вопроса."),
    c("f3-married", 3, "— Who is she married ___? — A surgeon from our hospital.", "— За кем она замужем? — За хирургом из нашей больницы.",
      ["to", "with", "on"], "to", "married to — женат на, замужем за. Married with — ошибка (with children — «с детьми»)."),
    c("f3-good", 3, "What is your daughter good ___ at school?", "Что у вашей дочки хорошо получается в школе?",
      ["at", "on", "of"], "at", "good at — хорошо получается, силён в."),
    c("f3-responsible", 3, "— What exactly is she responsible ___? — Infection control.", "— За что именно она отвечает? — За инфекционный контроль.",
      ["for", "of", "about"], "for", "responsible for — отвечать за."),
    c("f3-worried", 3, "You look tense. What are you so worried ___?", "Ты напряжён. Что тебя так тревожит?",
      ["about", "of", "with"], "about", "worried about — беспокоиться о, тревожиться из-за."),

    # 4 · Where are you from?
    c("f4-from", 4, "Where does the bleeding come ___?", "Откуда идёт кровотечение?",
      ["from", "of", "out"], "from", "come from — откуда: Where … from? Без from вопрос неполный."),
    c("f4-going", 4, "— Where are you ___? — To the lab.", "— Ты куда? — В лабораторию.",
      ["going", "going at", "going in"], "going", "Куда — Where are you going? Where уже значит «куда»; Where are you going to? тоже бывает, но обычно to не ставят."),
    c("f4-floor", 4, "What floor is the MRI unit ___?", "На каком этаже МРТ?",
      ["on", "in", "at"], "on", "on the second floor — на этаже. What floor … on?"),
    c("f4-hospital", 4, "Which hospital does she work ___?", "В какой больнице она работает?",
      ["at", "on", "to"], "at", "work at (или in) a hospital. Which hospital…? — предлог в конце."),
    c("f4-long", 4, "— How long are you staying ___? — Just two nights.", "— Надолго вы к нам? — Всего на две ночи.",
      ["for", "since", "during"], "for", "How long … for? — for можно поставить или опустить: How long are you staying?"),
    c("f4-until", 4, "What time is the pharmacy open ___?", "До скольки работает аптека?",
      ["until", "since", "by"], "until", "До какого часа — until: What time … until? Open until six."),

    # 5 · Who with? What about?
    c("f5-with", 5, "— I'm having dinner out tonight. — Oh? Who ___?", "— Я сегодня ужинаю не дома. — Да? С кем?",
      ["with", "to", "for"], "with", "Короткий переспрос: who + предлог. Who with? — с кем?"),
    c("f5-about", 5, "— We need to talk. — What ___?", "— Нам надо поговорить. — О чём?",
      ["about", "of", "for"], "about", "talk about → What about? — о чём?"),
    c("f5-for", 5, "— I bought some chocolates. — Who ___?", "— Я купил конфеты. — Кому?",
      ["for", "to", "with"], "for", "buy for — для кого: Who for?"),
    c("f5-to", 5, "— I've sent the report. — Who ___?", "— Я отправил отчёт. — Кому?",
      ["to", "for", "with"], "to", "send to — кому отправили: Who to? Полностью — Who did you send it to?"),
    c("f5-where", 5, "— I'm moving next month. — Where ___?", "— Я переезжаю в следующем месяце. — Куда?",
      ["to", "at", "for"], "to", "Короткое «куда?» — Where to? В полном вопросе to обычно не ставят: Where are you moving?"),
    c("f5-whatfor", 5, "— I'm going to the pharmacy. — What ___? — To get my prescription.", "— Я в аптеку. — Зачем? — Забрать лекарство по рецепту.",
      ["for", "to", "about"], "for", "What for? — зачем? Отвечают to do: To get my prescription."),

    # 6 · What is he being treated for?
    c("f6-treated", 6, "What is he being treated ___?", "От чего его лечат?",
      ["for", "from", "against"], "for", "be treated for — лечить от. «От» — for, не from."),
    c("f6-used", 6, "What is this drug mainly used ___?", "Для чего в основном применяют этот препарат?",
      ["for", "from", "by"], "for", "be used for — для чего применяют. Предлог в конце."),
    c("f6-written", 6, "Who was the guideline written ___?", "Кем написаны эти рекомендации?",
      ["by", "from", "with"], "by", "Кем — by: Who was it written by?"),
    c("f6-referred", 6, "— Who was the patient referred ___? — To a neurologist.", "— К кому направили пациента? — К неврологу.",
      ["to", "for", "at"], "to", "refer to — направить к. В пассиве to остаётся в конце."),
    c("f6-compared", 6, "What were the results compared ___?", "С чем сравнивали результаты?",
      ["with", "to", "from"], "with", "be compared with — сравнивать с.",
      also={"to": "Тоже верно: compared to и compared with в статьях взаимозаменяемы."}),
    c("f6-caused", 6, "What was the outbreak caused ___?", "Чем была вызвана вспышка?",
      ["by", "from", "of"], "by", "be caused by — вызван чем: What was it caused by?"),

    # 7 · To whom…? On which…?
    c("f7-whom", 7, "To ___ should the application be addressed?", "Кому адресовать заявление?",
      ["whom", "who", "which"], "whom", "После предлога в начале — только whom: To whom…? В разговоре — Who should I address it to?"),
    c("f7-which", 7, "___ data was the analysis based?", "На каких данных основан анализ?",
      ["On which", "Which on", "On that"], "On which",
      "Официально — предлог + which в начале. Разговорно — Which data was it based on? После предлога that не ставят."),
    c("f7-email", 7, "In an email to a colleague: ___", "Кому мне отправить форму?",
      ["Who should I send the form to?", "To whom should I send the form to?", "To who should I send the form?"], "Who should I send the form to?",
      "В обычной переписке — предлог в конце. To whom … to — предлог дважды; To who — ошибка.",
      say="Who should I send the form to?"),
    c("f7-letter", 7, "In a formal letter: ___", "С кем я могу обсудить этот вопрос?",
      ["With whom may I discuss this matter?", "With who may I discuss this matter?", "Whom with may I discuss this matter?"], "With whom may I discuss this matter?",
      "Официально — With whom…? Разговорно — Who can I talk to about this?",
      say="With whom may I discuss this matter?"),
    c("f7-after", 7, "___", "За каким пациентом вы присматриваете?",
      ["Which patient are you looking after?", "After which patient are you looking?"], "Which patient are you looking after?",
      "Look after — «присматривать», сочетание с особым смыслом: его не разбивают, after остаётся в конце."),
    c("f7-extent", 7, "___ extent do these findings apply to older patients?", "В какой мере эти выводы применимы к пожилым пациентам?",
      ["To what", "What", "For what"], "To what",
      "To what extent…? — «в какой мере», устойчивый оборот: предлог всегда в начале. Так же In what way…?, For what reason…?"),

    # 8 · I don't know what it's for
    c("f8-button", 8, "Could you tell me what this button ___?", "Не подскажете, для чего эта кнопка?",
      ["is for", "for is", "is it for"], "is for", "Косвенный вопрос — прямой порядок: what this button is for. Is it for — порядок прямого вопроса."),
    c("f8-works", 8, "I'm not sure who she works ___.", "Не знаю точно, на кого она работает.",
      ["for", "to", "by"], "for", "work for — работать на кого-то. В косвенном вопросе предлог тоже в конце."),
    c("f8-about", 8, "This is the patient I told you ___ yesterday.", "Это тот пациент, о котором я вам вчера рассказывал.",
      ["about", "of", "for"], "about",
      "the patient I told you about — предлог в конце придаточного, who или that можно опустить. По-русски «о котором» — предлог впереди."),
    c("f8-rely", 8, "These are the guidelines ___ we rely.", "Вот рекомендации, на которые мы опираемся.",
      ["on which", "which on", "on that"], "on which",
      "Официально — предлог + which: on which we rely. После предлога that не ставят. Разговорно — the guidelines we rely on."),
    c("f8-friends", 8, "— Thanks for helping me move. — No problem, that's what friends are ___.", "— Спасибо, что помог с переездом. — Не за что, на то и друзья.",
      ["for", "to", "with"], "for", "That's what friends are for — на то и друзья."),
    c("f8-allergic", 8, "Do you know what the patient is allergic ___?", "Вы знаете, на что у пациента аллергия?",
      ["to", "on", "for"], "to", "allergic to; в косвенном вопросе предлог тоже в конце."),
]

assert len({c["id"] for c in CARDS}) == len(CARDS)
assert all(c["a"] in c["opts"] for c in CARDS)
assert all(c["q"].count("___") == 1 for c in CARDS)
assert {c["t"] for c in CARDS} == {t["n"] for t in TOPICS if t["n"] != MIXED_TOPIC}
