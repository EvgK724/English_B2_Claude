# Содержание тренажёра «Have a look, take a seat» — конструкция «пустой» глагол + a + существительное-действие:
# have a look, take a seat, give it a try, go for a walk. Отличие от «Have, take, pay» (htp): там отдельные сочетания,
# здесь — как устроена сама конструкция, что она добавляет к простому глаголу и какой глагол взять.
# Пометка […] — конструкция; цвет по глаголу: have — оранжевый, take — синий, give — зелёный, прочие подчёркнуты.
# Темы с полем late вступают в общую тренировку позже: сначала B1, потом B1+, потом B2.

MIXED_TOPIC = 10

GROUPS = {
    "b1": "B1 — как устроено",
    "b1p": "B1+ — живая речь и кабинет врача",
    "b2": "B2 — тонкости",
    "mix": "Итог",
}

# Главная таблица: глагол | оттенок («главное — пояснение») | с чем сочетается (через « · »)
TABLE = [
    ["have", "коротко и по-свойски — разговорный британский", "a look · a seat · a rest · a chat · a think · a word · a go · a shower"],
    ["take", "одно действие — в инструкциях и в американском", "a seat · a look · a break · a breath · a sip · a step · a walk · a nap"],
    ["give", "сделать кому-то или чему-то", "me a call · me a hand · it a try · a smile · a squeeze · a cough · a shake"],
    ["go for", "выйти и что-то сделать", "a walk · a run · a swim · a drink · a coffee"],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["Let me [look] at it.", "посмотрю — нейтрально"],
     ["Let me [have a look] at it.", "гляну — коротко, мягко, по-свойски"],
     ["Let me [take a closer look] at it.", "присмотрюсь внимательнее"]],
    [["[Have a seat].", "присаживайтесь — дружелюбно"],
     ["[Take a seat], please.", "присаживайтесь — чуть официальнее"],
     ["[Sit down]!", "сядь! — без please звучит как приказ"]],
    [["She [had a go].", "попробовала"],
     ["She [had a go at] me.", "наехала на меня — брит., разг."]],
    [["We [went swimming] every summer.", "плавали — занятие вообще"],
     ["We [went for a swim] before breakfast.", "сходили искупаться — один раз"]],
    [["[Give me a call] tomorrow.", "позвоните мне — «кому» после give"],
     ["I need to [make a call].", "мне надо позвонить — без «кому»"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["Have a sit.", "Have a seat.", "сесть — have или take a seat"],
    ["Let me make a look.", "Let me have a look.", "look — с have или take"],
    ["Make a deep breath.", "Take a deep breath.", "вдох — take a breath"],
    ["Let's do a walk.", "Let's go for a walk.", "прогулка — go for a walk"],
    ["Have a quickly look.", "Have a quick look.", "внутри — прилагательное"],
    ["We had a fun.", "We had fun.", "fun — без a"],
    ["Take a care!", "Take care!", "care — без a"],
    ["Give a try it.", "Give it a try.", "it — сразу после give"],
    ["Breath in deeply.", "Breathe in deeply.", "breath — вдох, breathe — дышать"],
    ["Can I make a word with you?", "Can I have a word with you?", "поговорить — have a word"],
]

TOPICS = [
    {"n": 1, "group": "b1", "title": "have a look = look?", "sub": "что добавляет конструкция",
     "rule": "В have a look глагол have почти ничего не значит, смысл несёт существительное: look → a look, rest → a rest, think → a think. Получается одно короткое, лёгкое действие, сказанное мягко и по-свойски: Let me have a look — «дайте гляну». Let me look звучит нейтральнее. Сочетания устойчивые: a можно поставить не к любому глаголу, и have не меняют на make или do.",
     "ex": [
         {"en": "Let me [have a look] at your ankle.", "ru": "Дайте взгляну на вашу лодыжку."},
         {"en": "You look exhausted — why don't you [have a rest]?", "ru": "Ты вымотан — может, отдохнёшь немного?"},
         {"en": "Let me [have a think] and call you back.", "ru": "Дай подумать, я перезвоню."},
     ]},
    {"n": 2, "group": "b1", "title": "Have a seat: приглашения", "sub": "присаживайтесь · попробуйте · угощайтесь",
     "rule": "Повелительное Have a… — дружелюбное приглашение: Have a seat — присаживайтесь, Have a go — попробуйте, Have a biscuit — угощайтесь. Take a seat — то же «присаживайтесь», чуть официальнее: так говорят в регистратуре. Have a sit — так обычно не говорят, звучит как ошибка. Есть разговорное британское a sit-down — посидеть, передохнуть: I need a sit-down.",
     "ex": [
         {"en": "Come in and [have a seat] — I'll be with you in a minute.", "ru": "Заходите, присаживайтесь — я через минуту."},
         {"en": "Please [take a seat] in the waiting room.", "ru": "Пожалуйста, присядьте в зале ожидания."},
         {"en": "Never used the new scanner? [Have a go] — I'll talk you through it.", "ru": "Ещё не работали на новом аппарате? Попробуйте — я подскажу."},
     ]},
    {"n": 3, "group": "b1", "title": "have, take или give?", "sub": "какой глагол к какому слову",
     "rule": "Глагол запоминают вместе с существительным. have — разговорное британское: a look, a rest, a chat, a shower. take — одно действие, особенно в инструкциях и в американском: a seat, a break, a breath, a nap; часто подходят оба: have или take a look, a break, a shower. give — действие направлено на кого-то или на что-то: give me a call, give me a hand, give it a try. make и do с этими словами — частая ошибка.",
     "ex": [
         {"en": "We've been at it for three hours — let's [take a break].", "ru": "Мы работаем уже три часа — давай сделаем перерыв."},
         {"en": "Could you [give me a hand] with this trolley?", "ru": "Поможешь мне с этой каталкой?"},
         {"en": "I'll [give you a call] when the results come in.", "ru": "Я позвоню, когда придут результаты."},
     ]},
    {"n": 4, "group": "b1p", "title": "a quick look, a deep breath", "sub": "прилагательное вместо наречия", "late": 0.2,
     "rule": "Главный плюс конструкции: внутрь легко поставить прилагательное. По-русски «быстро взгляни, глубоко вдохните» — с наречием, по-английски — с прилагательным перед существительным: have a quick look, take a deep breath, take a closer look, give it a good shake, have a proper rest. Наречие (quickly, deeply) здесь — ошибка.",
     "ex": [
         {"en": "Could you [have a quick look] at this ECG?", "ru": "Можешь быстро глянуть на эту ЭКГ?"},
         {"en": "The rash looks odd — let's [take a closer look].", "ru": "Сыпь странная — давай присмотримся."},
         {"en": "[Give the bottle a good shake] before use.", "ru": "Перед употреблением хорошенько встряхните флакон."},
     ]},
    {"n": 5, "group": "b1p", "title": "give someone a…", "sub": "give me a call · give it a try", "late": 0.2,
     "rule": "give + кому или чему + a + существительное: give me a call — позвони мне, give him a hug — обними его, give the door a push — толкни дверь, give it a try — попробуй. «Кому» стоит сразу после give, без to. it тоже сразу после give: give it a go, а не give a go it. Подумать над чем-то — give it some thought.",
     "ex": [
         {"en": "[Give me a ring] when you get home.", "ru": "Позвони мне, когда доберёшься."},
         {"en": "I've never tried yoga, but I'll [give it a go].", "ru": "Йогой я не занимался, но попробую."},
         {"en": "The door's stuck — [give it a push].", "ru": "Дверь заело — толкни её."},
     ]},
    {"n": 6, "group": "b1p", "title": "В кабинете: команды при осмотре", "sub": "take a deep breath · give me a big smile", "late": 0.25,
     "rule": "Британские врачи дают команды при осмотре именно так: мягко, через конструкцию. Take a deep breath — глубоко вдохните. Give me a big smile — улыбнитесь (лицевой нерв). Give my fingers a squeeze — сожмите пальцы. Take a few steps — пройдите несколько шагов. Take a sip of water — сделайте глоток. Give a little cough — покашляйте. В конце часто добавляют for me — так ещё мягче: Take a few steps for me.",
     "ex": [
         {"en": "[Take a deep breath] in and hold it.", "ru": "Глубоко вдохните и задержите дыхание."},
         {"en": "Can you [give me a big smile]?", "ru": "Улыбнитесь, пожалуйста, пошире."},
         {"en": "[Give my fingers a squeeze] as hard as you can.", "ru": "Сожмите мои пальцы как можно сильнее."},
     ]},
    {"n": 7, "group": "b2", "title": "a или без a", "sub": "have fun · take care · have lunch", "late": 0.45,
     "rule": "a ставят, когда существительное — одно действие, сделанное из глагола: a look, a walk, a swim. В других устойчивых сочетаниях a нет: have fun, take care, take part, take place, have lunch, have dinner. Но с прилагательным a возвращается: We had a quick lunch, We had a lovely dinner. Самые частые ошибки — have a fun и take a care.",
     "ex": [
         {"en": "We [had fun] at the conference dinner.", "ru": "На ужине конференции было весело."},
         {"en": "Twenty hospitals [took part] in the trial.", "ru": "В исследовании участвовали двадцать больниц."},
         {"en": "We only had time for [a quick lunch].", "ru": "Успели только наскоро пообедать."},
     ]},
    {"n": 8, "group": "b2", "title": "go for a walk", "sub": "прогулка, пробежка, купание", "late": 0.45,
     "rule": "Выйти что-то сделать — go for a + существительное: go for a walk, go for a run, go for a swim, go for a drink. В британской речи это самый частый вариант; take a walk звучит книжнее и чаще в американском, do a walk и make a walk — ошибки. go for a swim — одно купание, go swimming — плавать вообще, как занятие.",
     "ex": [
         {"en": "It's a lovely evening — let's [go for a walk].", "ru": "Чудесный вечер — пойдём прогуляемся."},
         {"en": "We [went for a swim] before breakfast.", "ru": "Перед завтраком мы сходили искупаться."},
         {"en": "She [goes swimming] twice a week.", "ru": "Она плавает два раза в неделю."},
     ]},
    {"n": 9, "group": "b2", "title": "have a word, have a go at", "sub": "когда смысл меняется", "late": 0.5,
     "rule": "У части сочетаний смысл не равен простому глаголу. have a word with — коротко поговорить, часто о проблеме. have a go at someone — наехать, отругать (брит., разг.), а без at — «попробовать». give it a rest — хватит уже (разг.). take the hint — понять намёк. take a hard look at — критически разобраться. give it a shot — попробовать, как give it a go.",
     "ex": [
         {"en": "Can I [have a word with] you about tomorrow's rota?", "ru": "Можно тебя на минутку — насчёт завтрашнего графика?"},
         {"en": "My boss [had a go at] me for being late.", "ru": "Начальник наехал на меня за опоздание."},
         {"en": "We need to [take a hard look at] our infection rates.", "ru": "Надо всерьёз разобраться с нашими показателями инфекций."},
     ]},
    {"n": 10, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · have a look = look?
    c("h1-ankle", 1, "Let me ___ a look at your ankle.", "Дайте взгляну на вашу лодыжку.",
      ["have", "make", "do"], "have", "Взглянуть — have a look (брит.) или take a look (амер.). Make и do с look не сочетаются."),
    c("h1-notes", 1, "Can I ___ at your notes before the meeting?", "Можно глянуть твои записи перед совещанием?",
      ["have a look", "make a look", "do a look"], "have a look", "Глянуть — have a look at."),
    c("h1-rest", 1, "You look exhausted — why don't you ___ a rest?", "Ты вымотан — может, отдохнёшь немного?",
      ["have", "make", "do"], "have", "Немного отдохнуть — have a rest."),
    c("h1-think", 1, "I'm not sure yet. Let me ___ a think and call you back.", "Пока не знаю. Дай подумать, я перезвоню.",
      ["have", "make", "take"], "have", "have a think — подумать, не торопясь (разг., брит.)."),
    c("h1-chat", 1, "We ___ a quick chat in the corridor after the round.", "После обхода мы перекинулись парой слов в коридоре.",
      ["had", "made", "did"], "had", "Поболтать — have a chat."),
    c("h1-wash", 1, "After a week of rehab he can ___ a wash without help.", "Через неделю реабилитации он может умыться без помощи.",
      ["have", "make", "do"], "have", "Умыться — have a wash (брит.)."),

    # 2 · Have a seat: приглашения
    c("h2-seat", 2, "Come in and ___ a seat — I'll be with you in a minute.", "Заходите, присаживайтесь — я через минуту.",
      ["have", "sit", "make"], "have", "Присаживайтесь — Have a seat или Take a seat. Sit a seat — ошибка."),
    c("h2-waiting", 2, "Please ___ a seat in the waiting room.", "Пожалуйста, присядьте в зале ожидания.",
      ["take", "make", "sit"], "take", "Take a seat — чуть официальнее: так говорят в регистратуре и в объявлениях."),
    c("h2-sit", 2, "Please ___ — you must be tired after the journey.", "Присаживайтесь — вы, наверное, устали с дороги.",
      ["have a seat", "have a sit", "make a seat"], "have a seat", "Норма — have a seat или take a seat. Have a sit обычно не говорят, звучит как ошибка."),
    c("h2-sitdown", 2, "After the long walk round the hospital she needed ___.", "После долгой прогулки по больнице ей надо было посидеть, передохнуть.",
      ["a sit-down", "a sit", "a sitting"], "a sit-down", "Посидеть, передохнуть — a sit-down (разг., брит.): I need a sit-down."),
    c("h2-go", 2, "Never used the new scanner? ___ a go — I'll talk you through it.", "Ещё не работали на новом аппарате? Попробуйте — я подскажу.",
      ["Have", "Make", "Do"], "Have", "Попробуйте! — Have a go! Ещё: Give it a go, Give it a try."),
    c("h2-biscuit", 2, "___ a biscuit — they're homemade.", "Угощайтесь печеньем — домашнее.",
      ["Have", "Eat", "Make"], "Have", "Угощение — Have a…: Have a biscuit, Have some tea.",
      also={"Eat": "так скажут, но это просто «ешьте»; приглашение угоститься — Have a biscuit"}),

    # 3 · have, take или give?
    c("h3-break", 3, "We've been at it for three hours — let's ___ a break.", "Мы работаем уже три часа — давай сделаем перерыв.",
      ["take", "make", "do"], "take", "Перерыв — take a break или have a break. Make a break — ошибка."),
    c("h3-hand", 3, "Could you ___ me a hand with this trolley?", "Поможешь мне с этой каталкой?",
      ["give", "take", "make"], "give", "Помочь — give someone a hand."),
    c("h3-nap", 3, "I usually ___ a short nap after a night shift.", "После ночного дежурства я обычно ненадолго ложусь вздремнуть.",
      ["take", "make", "do"], "take", "Вздремнуть — take a nap (брит. ещё have a nap)."),
    c("h3-call", 3, "I'll ___ you a call when the results come in.", "Я позвоню, когда придут результаты.",
      ["give", "make", "take"], "give", "Позвонить кому-то — give someone a call (брит. ещё a ring). Make a call — без «кому»: I need to make a call."),
    c("h3-shower", 3, "I'm going to ___ a quick shower before dinner.", "Перед ужином быстро приму душ.",
      ["have", "make", "do"], "have", "Душ — have a shower (брит.) или take a shower."),
    c("h3-try", 3, "The new app is free — why not ___ it a try?", "Приложение бесплатное — почему бы не попробовать?",
      ["give", "make", "take"], "give", "Попробовать что-то — give it a try или give it a go."),

    # 4 · прилагательное внутри
    c("h4-quick", 4, "Could you have a ___ look at this ECG?", "Можешь быстро глянуть на эту ЭКГ?",
      ["quick", "quickly", "fastly"], "quick", "Внутри — прилагательное: a quick look. По-русски «быстро взгляни» — наречие, по-английски — прилагательное."),
    c("h4-closer", 4, "The rash looks odd — let's take a ___ look.", "Сыпь странная — давай присмотримся.",
      ["closer", "more closely", "closely"], "closer", "Присмотреться — take a closer look."),
    c("h4-shake", 4, "Give the bottle a ___ shake before use.", "Перед употреблением хорошенько встряхните флакон.",
      ["good", "well", "goodly"], "good", "Хорошенько встряхнуть — give it a good shake: good, а не well."),
    c("h4-long", 4, "We had a ___ talk with his family about the options.", "Мы долго разговаривали с его родными о вариантах лечения.",
      ["long", "longly", "long-time"], "long", "Долгий разговор — a long talk: прилагательное long."),
    c("h4-deep", 4, "Take a ___ breath in through your nose.", "Глубоко вдохните через нос.",
      ["deep", "deeply", "depth"], "deep", "Глубоко вдохнуть — take a deep breath."),
    c("h4-proper", 4, "You need to have a ___ rest, not just ten minutes on a chair.", "Тебе нужно нормально отдохнуть, а не десять минут на стуле.",
      ["proper", "properly", "right"], "proper", "Нормально, как следует отдохнуть — have a proper rest (брит., разг.)."),

    # 5 · give someone a…
    c("h5-ring", 5, "___ me a ring when you get home.", "Позвони мне, когда доберёшься.",
      ["Give", "Make", "Take"], "Give", "Позвони мне — give me a ring (брит.) или give me a call."),
    c("h5-go", 5, "I've never tried yoga, but I'll give ___ a go.", "Йогой я не занимался, но попробую.",
      ["it", "to it", "for it"], "it", "give it a go — it сразу после give, без предлога."),
    c("h5-hug", 5, "She gave her son a big ___ before the operation.", "Перед операцией она крепко обняла сына.",
      ["hug", "hugging", "hugged"], "hug", "Обнять — give someone a hug: после a — существительное."),
    c("h5-push", 5, "The door's stuck — give it a ___.", "Дверь заело — толкни её.",
      ["push", "pushing", "pushed"], "push", "Толкнуть — give it a push."),
    c("h5-me", 5, "Could you give ___ a hand with these files?", "Поможешь мне с этими папками?",
      ["me", "to me", "for me"], "me", "«Кому» сразу после give — без to: give me a hand."),
    c("h5-thought", 5, "I'm afraid I haven't given it much ___ yet.", "Боюсь, я пока над этим особо не думал.",
      ["thought", "think", "thinking"], "thought", "Подумать над чем-то — give it some thought, give it much thought: существительное thought."),

    # 6 · в кабинете
    c("h6-breath", 6, "Take a deep ___ in and hold it.", "Глубоко вдохните и задержите дыхание.",
      ["breath", "breathe", "breathing"], "breath", "Существительное — breath /breθ/, вдох. Глагол — breathe /briːð/: Breathe in."),
    c("h6-smile", 6, "Can you give me a big ___?", "Улыбнитесь, пожалуйста, пошире.",
      ["smile", "smiling", "laugh"], "smile", "Проверка лицевого нерва — Give me a big smile."),
    c("h6-squeeze", 6, "Give my fingers a ___ as hard as you can.", "Сожмите мои пальцы как можно сильнее.",
      ["squeeze", "squeezing", "squeezed"], "squeeze", "Сжать — give something a squeeze."),
    c("h6-steps", 6, "Can you ___ a few steps towards me?", "Пройдите, пожалуйста, несколько шагов ко мне.",
      ["take", "make", "do"], "take", "Сделать шаги — take steps. Make steps — калька с русского."),
    c("h6-sip", 6, "___ a small sip of water and swallow.", "Сделайте маленький глоток воды и проглотите.",
      ["Take", "Make", "Drink"], "Take", "Глоток — take a sip. Drink a sip и make a sip — кальки."),
    c("h6-cough", 6, "Can you give a little ___ for me?", "Покашляйте, пожалуйста, немного.",
      ["cough", "coughing", "coughed"], "cough", "Покашлять — give a cough: после a — существительное."),

    # 7 · a или без a
    c("h7-fun", 7, "We had ___ at the conference dinner.", "На ужине конференции было весело.",
      ["fun", "a fun", "funny"], "fun", "fun — неисчисляемое: have fun, без a."),
    c("h7-care", 7, "Take ___ on the icy roads!", "Осторожнее на скользкой дороге!",
      ["care", "a care", "caring"], "care", "Take care — без a."),
    c("h7-part", 7, "Twenty hospitals took ___ in the trial.", "В исследовании участвовали двадцать больниц.",
      ["part", "a part", "the part"], "part", "Участвовать — take part in, без артикля."),
    c("h7-lunch", 7, "Let's have ___ together after the meeting.", "Давай пообедаем вместе после совещания.",
      ["lunch", "a lunch", "the lunch"], "lunch", "Приёмы пищи — без артикля: have lunch, have dinner."),
    c("h7-quick", 7, "We only had time for ___ quick lunch.", "Успели только наскоро пообедать.",
      ["a", "", "the"], "a", "С прилагательным a возвращается: a quick lunch, a lovely dinner."),
    c("h7-place", 7, "The next meeting will take ___ on Friday.", "Следующее совещание состоится в пятницу.",
      ["place", "a place", "the place"], "place", "Состояться — take place, без артикля."),

    # 8 · go for a walk
    c("h8-walk", 8, "It's a lovely evening — let's go ___ a walk.", "Чудесный вечер — пойдём прогуляемся.",
      ["for", "on", "to"], "for", "Прогуляться — go for a walk."),
    c("h8-swim", 8, "We went ___ before breakfast.", "Перед завтраком мы сходили искупаться.",
      ["for a swim", "on a swim", "to a swim"], "for a swim", "Сходить искупаться, один раз — go for a swim."),
    c("h8-swimming", 8, "She goes ___ twice a week.", "Она плавает два раза в неделю.",
      ["swimming", "for swimming", "to swimming"], "swimming", "Регулярное занятие — go swimming; один раз — go for a swim."),
    c("h8-stick", 8, "After the stroke he can ___ a short walk with a stick.", "После инсульта он может немного погулять с тростью.",
      ["go for", "do", "make"], "go for", "Прогулка — go for a walk. Do a walk и make a walk — ошибки."),
    c("h8-drink", 8, "Shall we go ___ a drink after work?", "Сходим выпить после работы?",
      ["for", "on", "to"], "for", "Сходить выпить — go for a drink."),
    c("h8-takes", 8, "Every evening he ___ a walk around the park.", "Каждый вечер он гуляет по парку.",
      ["takes", "makes", "does"], "takes", "take a walk — тоже верно, чуть книжнее и чаще в американском; в британской речи — go for a walk."),

    # 9 · когда смысл меняется
    c("h9-word", 9, "Can I ___ a word with you about tomorrow's rota?", "Можно тебя на минутку — насчёт завтрашнего графика?",
      ["have", "say", "make"], "have", "have a word with — коротко поговорить, часто о проблеме. Say a word — «сказать слово»."),
    c("h9-go-at", 9, "My boss had a go ___ me for being late.", "Начальник наехал на меня за опоздание.",
      ["at", "on", "to"], "at", "have a go at someone — наехать, отругать (брит., разг.). Без at — «попробовать»."),
    c("h9-rest", 9, "Oh, give it a ___! We've heard enough about your new car.", "Ой, хватит уже! Мы наслушались про твою новую машину.",
      ["rest", "break", "stop"], "rest", "Give it a rest! — хватит уже (разг., грубовато)."),
    c("h9-hint", 9, "I kept looking at my watch, but he didn't ___ the hint.", "Я всё поглядывал на часы, но он так и не понял намёка.",
      ["take", "make", "do"], "take", "Понять намёк — take the hint (или get the hint)."),
    c("h9-hard", 9, "We need to take a hard ___ at our infection rates.", "Надо всерьёз разобраться с нашими показателями инфекций.",
      ["look", "see", "watch"], "look", "take a hard look at — критически, всерьёз разобраться."),
    c("h9-shot", 9, "It might not work, but it's worth ___ a shot.", "Может, и не получится, но попробовать стоит.",
      ["giving it", "making it", "doing it"], "giving it", "give it a shot — попробовать (разг.), как give it a go. После worth — -ing: worth giving it a shot."),
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
