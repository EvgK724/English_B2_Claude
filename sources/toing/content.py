# Содержание приложения «To или -ing».
# В примерах: {…} — форма с to (синий), […] — форма на -ing (оранжевый).

SORT_TOPIC = 11
MIXED_TOPIC = 12

# Шпаргалка: группы по смыслу. * — меняет смысл с другой формой.
TO_GROUPS = [
    {"ru": "хочу, надеюсь, жду", "verbs": ["want", "would like", "hope", "expect", "wish"]},
    {"ru": "решаю, планирую", "verbs": ["decide", "plan", "choose", "arrange", "aim"]},
    {"ru": "обещаю, соглашаюсь, отказываюсь", "verbs": ["agree", "promise", "offer", "refuse", "threaten"]},
    {"ru": "получилось или нет", "verbs": ["manage", "fail", "afford", "learn"]},
    {"ru": "кажется, склонен", "verbs": ["seem", "appear", "tend", "pretend"]},
    {"ru": "заслуживает, надо", "verbs": ["deserve", "need*"]},
]
ING_GROUPS = [
    {"ru": "нравится, не выношу, скучаю", "verbs": ["enjoy", "mind", "can't stand", "can't help", "miss"]},
    {"ru": "избегаю, откладываю, рискую", "verbs": ["avoid", "postpone", "delay", "put off", "risk"]},
    {"ru": "продолжаю, заканчиваю, бросаю", "verbs": ["keep", "practise", "finish", "give up", "quit"]},
    {"ru": "предлагаю, обдумываю", "verbs": ["suggest", "recommend", "consider", "imagine", "involve"]},
    {"ru": "признаю, отрицаю", "verbs": ["admit", "deny", "mention"]},
    {"ru": "to здесь предлог", "verbs": ["look forward to", "object to", "get used to", "be used to"]},
]

VERB_RU = {
    "want": "хотеть", "would like": "хотел бы", "hope": "надеяться", "expect": "рассчитывать, ожидать",
    "wish": "желать (официально)", "decide": "решить", "plan": "планировать", "choose": "выбрать",
    "arrange": "договориться, организовать", "aim": "стремиться, ставить целью", "agree": "согласиться",
    "promise": "обещать", "offer": "предложить сделать самому", "refuse": "отказаться", "threaten": "грозиться",
    "manage": "суметь, справиться", "fail": "не суметь, не сделать", "afford": "позволить себе",
    "learn": "научиться", "seem": "казаться", "appear": "по-видимому, оказываться", "tend": "обычно, быть склонным",
    "pretend": "притворяться", "deserve": "заслуживать", "need": "нуждаться, надо",
    "enjoy": "получать удовольствие", "mind": "возражать, быть против", "can't stand": "терпеть не могу",
    "can't help": "не могу удержаться", "miss": "скучать", "avoid": "избегать", "postpone": "откладывать",
    "delay": "откладывать, затягивать", "put off": "откладывать", "risk": "рисковать",
    "keep": "продолжать, всё время", "practise": "тренировать", "finish": "закончить", "give up": "бросить",
    "quit": "бросить", "suggest": "предлагать", "recommend": "рекомендовать", "consider": "обдумывать",
    "imagine": "представлять", "involve": "предполагать, включать", "admit": "признавать",
    "deny": "отрицать", "mention": "упоминать", "look forward to": "ждать с нетерпением",
    "object to": "возражать против", "get used to": "привыкать", "be used to": "привыкнуть",
}

# Меняют смысл: глагол | + to do | перевод | + -ing | перевод
DUAL = [
    ["remember", "remember to check", "не забыть сделать", "remember seeing", "помнить, как было"],
    ["forget", "forget to sign", "забыть сделать", "never forget doing", "не забыть, как было"],
    ["stop", "stop to pick up", "остановиться, чтобы", "stop smoking", "прекратить"],
    ["try", "try to keep still", "стараться", "try taking paracetamol", "попробовать способ"],
    ["regret", "regret to inform", "с сожалением сообщаю", "regret ordering", "жалею о сделанном"],
    ["mean", "didn't mean to upset", "намеревался", "means losing time", "означает"],
    ["go on", "go on to present", "перейти к другому", "go on talking", "продолжать то же"],
    ["need", "need to sign", "надо сделать самому", "needs changing", "надо, чтобы сделали"],
]

# Частые ошибки русскоговорящих: неверно | верно
ERRORS = [
    ["suggest to do", "suggest doing"],
    ["look forward to hear", "look forward to hearing"],
    ["avoid to drive", "avoid driving"],
    ["enjoy to work", "enjoy working"],
    ["I'd like going", "I'd like to go"],
    ["I'm used to work nights", "I'm used to working nights"],
]

TOPICS = [
    {"n": 1, "title": "to: действие впереди",
     "rule": "Глаголы решений, желаний, планов и попыток смотрят в будущее: само действие ещё впереди, поэтому после них to do. Сюда относятся want, hope, expect, plan, decide, agree, promise, refuse, offer, manage, afford, fail, tend, seem.",
     "ex": [
         {"en": "We decided {to start} thrombolysis immediately.", "ru": "Мы решили сразу начать тромболизис."},
         {"en": "The patient refused {to sign} the consent form.", "ru": "Пациент отказался подписать согласие."},
         {"en": "We can't afford {to lose} another hour.", "ru": "Мы не можем позволить себе потерять ещё час."},
     ]},
    {"n": 2, "title": "-ing: само действие",
     "rule": "Глаголы, которые говорят о самом действии — нравится ли оно, избегаем ли его, закончили ли, повторяем ли, — берут -ing: enjoy, avoid, finish, keep, mind, risk, deny, admit, miss, practise, postpone, can't stand, give up.",
     "ex": [
         {"en": "Patients should avoid [driving] for a month after a TIA.", "ru": "После ТИА пациентам следует месяц не садиться за руль."},
         {"en": "Have you finished [writing] the discharge summary?", "ru": "Вы закончили писать выписку?"},
         {"en": "He keeps [forgetting] his evening dose.", "ru": "Он постоянно забывает вечернюю дозу."},
     ]},
    {"n": 3, "title": "suggest, recommend, consider",
     "rule": "Глаголы обсуждения и предложения — suggest, recommend, consider, advise (без «кого») — и ещё imagine, involve берут -ing. Главная ошибка русскоговорящих — suggest to do: правильно suggest doing или suggest that we do. Сравни: offer to do — предложить сделать самому.",
     "ex": [
         {"en": "She suggested [repeating] the scan in 24 hours.", "ru": "Она предложила повторить КТ через сутки."},
         {"en": "We considered [stopping] aspirin before surgery.", "ru": "Мы обсуждали отмену аспирина перед операцией."},
         {"en": "The procedure involves [inserting] a catheter into the artery.", "ru": "Процедура предполагает введение катетера в артерию."},
     ]},
    {"n": 4, "title": "После предлога — всегда -ing",
     "rule": "После любого предлога глагол идёт с -ing: interested in doing, instead of doing, before doing, thank you for doing. Ловушка — сочетания, где to само предлог: look forward to, be used to, get used to, object to. Правильно I look forward to hearing from you — а не to hear.",
     "ex": [
         {"en": "I look forward to [hearing] from you.", "ru": "Жду вашего ответа."},
         {"en": "Instead of [waiting] for the MRI, we started treatment.", "ru": "Вместо того чтобы ждать МРТ, мы начали лечение."},
         {"en": "She is used to [working] night shifts.", "ru": "Она привыкла работать в ночные смены."},
     ]},
    {"n": 5, "title": "remember и forget",
     "rule": "to — дело впереди, -ing — дело позади. Remember to check — не забыть проверить, это ещё предстоит. Remember seeing — помнить, как видел, это уже было. Так же forget: forgot to take — забыл принять и не принял; never forget doing — никогда не забуду, как делал.",
     "ex": [
         {"en": "Remember {to check} the INR before discharge.", "ru": "Не забудьте проверить МНО перед выпиской."},
         {"en": "I remember [seeing] this patient last year.", "ru": "Я помню, что видел этого пациента в прошлом году."},
         {"en": "I'll never forget [doing] my first thrombectomy.", "ru": "Никогда не забуду свою первую тромбэктомию."},
     ]},
    {"n": 6, "title": "stop",
     "rule": "stop doing — прекратить само действие: he stopped smoking — бросил курить. stop to do — остановиться, чтобы сделать что-то другое, to здесь значит «чтобы»: the ambulance stopped to pick up a patient.",
     "ex": [
         {"en": "He stopped [smoking] after the stroke.", "ru": "После инсульта он бросил курить."},
         {"en": "The ambulance stopped {to pick up} a second patient.", "ru": "Скорая остановилась, чтобы забрать второго пациента."},
     ]},
    {"n": 7, "title": "try",
     "rule": "try to do — стараться, прилагать усилие, и не факт, что выйдет: try to keep still. try doing — попробовать как способ, эксперимент, чтобы посмотреть, поможет ли: try taking paracetamol.",
     "ex": [
         {"en": "Try {to keep} still during the scan.", "ru": "Постарайтесь не двигаться во время исследования."},
         {"en": "If the headache persists, try [taking] paracetamol.", "ru": "Если голова не проходит, попробуйте принять парацетамол."},
     ]},
    {"n": 8, "title": "regret, mean, go on",
     "rule": "regret to inform — «с сожалением сообщаю» (официально), regret doing — жалеть о сделанном. mean to do — намереваться, mean doing — означать. go on to do — перейти к следующему, go on doing — продолжать то же самое.",
     "ex": [
         {"en": "We regret {to inform} you that the clinic is closed.", "ru": "С сожалением сообщаем, что клиника закрыта."},
         {"en": "I regret [not ordering] an MRI earlier.", "ru": "Жалею, что не назначил МРТ раньше."},
         {"en": "Delaying the scan means [losing] brain tissue.", "ru": "Откладывать КТ — значит терять мозговую ткань."},
     ]},
    {"n": 9, "title": "Можно и так, и так",
     "rule": "like, love, hate, prefer, begin, start, continue берут обе формы почти без разницы: it started to rain = it started raining. Но would like, would love, would prefer — только с to: I'd like to speak to the consultant.",
     "ex": [
         {"en": "The patient began {to improve} on the third day.", "ru": "На третий день пациенту стало лучше."},
         {"en": "Continue [taking] the tablets until your next appointment.", "ru": "Продолжайте принимать таблетки до следующего приёма."},
         {"en": "I'd like {to speak} to the consultant, please.", "ru": "Я бы хотел поговорить с консультантом."},
     ]},
    {"n": 10, "title": "used to и needs doing",
     "rule": "used to do — «раньше делал, теперь нет»: I used to work in Moscow. be used to doing, get used to doing — «привык, привыкнуть», to здесь предлог: I'm used to working nights. needs doing — «нужно, чтобы сделали»: the dressing needs changing = needs to be changed.",
     "ex": [
         {"en": "I used {to work} in Moscow before I moved here.", "ru": "Раньше я работал в Москве, пока не переехал сюда."},
         {"en": "I'm used to [working] nights.", "ru": "Я привык работать по ночам."},
         {"en": "The dressing needs [changing] every day.", "ru": "Повязку нужно менять каждый день."},
     ]},
    {"n": SORT_TOPIC, "title": "Глагол → to или -ing",
     "rule": "Быстрая проверка по спискам: видишь глагол — выбираешь to do или doing. Под глаголом — перевод, после ответа — его группа из шпаргалки. Глаголы, которые меняют смысл, здесь не встречаются — они в темах 5–8.",
     "ex": []},
    {"n": MIXED_TOPIC, "title": "Итог — всё вместе",
     "rule": "Пятнадцать случайных предложений из тем 1–10 вперемешку.",
     "ex": []},
]

CARDS = [
    # 1 — to: впереди
    {"id": "t1-decide", "t": 1, "q": "We decided ___ thrombolysis immediately.", "opts": ["to start", "starting"], "a": "to start",
     "why": "decide — решение, действие впереди: to start."},
    {"id": "t1-hope", "t": 1, "q": "We hope ___ him home by Friday.", "opts": ["to send", "sending"], "a": "to send",
     "why": "hope = надеяться, действие впереди: to send."},
    {"id": "t1-refuse", "t": 1, "q": "The patient refused ___ the consent form.", "opts": ["to sign", "signing"], "a": "to sign",
     "why": "refuse = отказаться сделать: to sign."},
    {"id": "t1-agree", "t": 1, "q": "The surgeon agreed ___ the patient this afternoon.", "opts": ["to see", "seeing"], "a": "to see",
     "why": "agree = согласиться сделать: to see."},
    {"id": "t1-manage", "t": 1, "q": "Did you manage ___ the family?", "opts": ["to contact", "contacting"], "a": "to contact",
     "why": "manage = суметь, справиться: to contact."},
    {"id": "t1-afford", "t": 1, "q": "We can't afford ___ another hour.", "opts": ["to lose", "losing"], "a": "to lose",
     "why": "afford = позволить себе: to lose."},
    {"id": "t1-expect", "t": 1, "q": "We expect ___ the CT report by noon.", "opts": ["to get", "getting"], "a": "to get",
     "why": "expect = рассчитывать: to get."},
    {"id": "t1-tend", "t": 1, "q": "Older patients tend ___ more slowly.", "opts": ["to recover", "recovering"], "a": "to recover",
     "why": "tend = обычно, иметь склонность: to recover."},

    # 2 — -ing: само действие
    {"id": "t2-avoid", "t": 2, "q": "Patients should avoid ___ for a month after a TIA.", "opts": ["driving", "to drive"], "a": "driving",
     "why": "avoid = избегать самого действия: driving."},
    {"id": "t2-enjoy", "t": 2, "q": "Do you enjoy ___ in the stroke unit?", "opts": ["working", "to work"], "a": "working",
     "why": "enjoy = нравится само действие: working. Enjoy to work — типичная ошибка."},
    {"id": "t2-finish", "t": 2, "q": "Have you finished ___ the discharge summary?", "opts": ["writing", "to write"], "a": "writing",
     "why": "finish = закончить процесс: writing."},
    {"id": "t2-keep", "t": 2, "q": "He keeps ___ his evening dose.", "opts": ["forgetting", "to forget"], "a": "forgetting",
     "why": "keep = всё время, снова и снова: forgetting."},
    {"id": "t2-mind", "t": 2, "q": "Would you mind ___ the window?", "opts": ["closing", "to close"], "a": "closing",
     "why": "mind = возражать против действия: closing."},
    {"id": "t2-help", "t": 2, "q": "I couldn't help ___ at his joke.", "opts": ["laughing", "to laugh"], "a": "laughing",
     "why": "can't help = не могу удержаться: laughing."},
    {"id": "t2-risk", "t": 2, "q": "We can't risk ___ the patient before the scan.", "opts": ["moving", "to move"], "a": "moving",
     "why": "risk = рисковать, сделав это: moving."},
    {"id": "t2-deny", "t": 2, "q": "He denied ___ any alcohol that evening.", "opts": ["drinking", "to drink"], "a": "drinking",
     "why": "deny = отрицать сделанное: drinking."},

    # 3 — suggest, recommend, consider
    {"id": "t3-suggest", "t": 3, "q": "She suggested ___ the scan in 24 hours.", "opts": ["repeating", "to repeat"], "a": "repeating",
     "why": "suggest + -ing. Suggest to do — типичная ошибка."},
    {"id": "t3-consider", "t": 3, "q": "We considered ___ aspirin before surgery.", "opts": ["stopping", "to stop"], "a": "stopping",
     "why": "consider = обдумывать: stopping."},
    {"id": "t3-recommend", "t": 3, "q": "I'd recommend ___ with a low dose.", "opts": ["starting", "to start"], "a": "starting",
     "why": "recommend + -ing: starting."},
    {"id": "t3-advise", "t": 3, "q": "I'd advise ___ for the MRI results.", "opts": ["waiting", "to wait"], "a": "waiting",
     "why": "advise без «кого» — -ing; с «кем»: advise you to wait."},
    {"id": "t3-involve", "t": 3, "q": "The procedure involves ___ a catheter into the artery.", "opts": ["inserting", "to insert"], "a": "inserting",
     "why": "involve = предполагать, включать: inserting."},
    {"id": "t3-imagine", "t": 3, "q": "Can you imagine ___ a night shift alone?", "opts": ["working", "to work"], "a": "working",
     "why": "imagine = представить само действие: working."},

    # 4 — после предлога
    {"id": "t4-forward", "t": 4, "q": "I look forward to ___ from you.", "opts": ["hearing", "hear"], "a": "hearing",
     "why": "to здесь предлог (look forward to + существительное), после него — -ing."},
    {"id": "t4-used", "t": 4, "q": "She is used to ___ night shifts.", "opts": ["working", "work"], "a": "working",
     "why": "be used to = привыкнуть; to — предлог: working."},
    {"id": "t4-instead", "t": 4, "q": "Instead of ___ for the MRI, we started treatment.", "opts": ["waiting", "to wait"], "a": "waiting",
     "why": "После предлога of — -ing."},
    {"id": "t4-before", "t": 4, "q": "Check the INR before ___ warfarin.", "opts": ["restarting", "to restart"], "a": "restarting",
     "why": "before здесь предлог: before restarting."},
    {"id": "t4-thank", "t": 4, "q": "Thank you for ___ so quickly.", "opts": ["replying", "to reply"], "a": "replying",
     "why": "После предлога for — -ing."},
    {"id": "t4-object", "t": 4, "q": "Many patients object to ___ for parking.", "opts": ["paying", "pay"], "a": "paying",
     "why": "object to = возражать против; to — предлог: paying."},

    # 5 — remember, forget
    {"id": "t5-remember-to", "t": 5, "q": "Remember ___ the INR before discharge.", "opts": ["to check", "checking"], "a": "to check",
     "why": "Не забыть сделать — дело впереди: to check."},
    {"id": "t5-remember-ing", "t": 5, "q": "I remember ___ this patient last year.", "opts": ["seeing", "to see"], "a": "seeing",
     "why": "Помню, как было, — дело позади: seeing."},
    {"id": "t5-forget-to", "t": 5, "q": "Don't forget ___ the consent form.", "opts": ["to sign", "signing"], "a": "to sign",
     "why": "Не забыть сделать — to sign."},
    {"id": "t5-forget-ing", "t": 5, "q": "I'll never forget ___ my first thrombectomy.", "opts": ["doing", "to do"], "a": "doing",
     "why": "Не забуду, как делал, — дело позади: doing."},
    {"id": "t5-forgot", "t": 5, "q": "He forgot ___ his evening dose, so his INR dropped.", "opts": ["to take", "taking"], "a": "to take",
     "why": "Забыл сделать и не сделал — forgot to take."},

    # 6 — stop
    {"id": "t6-smoking", "t": 6, "q": "He stopped ___ after the stroke.", "opts": ["smoking", "to smoke"], "a": "smoking",
     "why": "stop doing = прекратить, бросить: smoking."},
    {"id": "t6-pickup", "t": 6, "q": "The ambulance stopped ___ a second patient.", "opts": ["to pick up", "picking up"], "a": "to pick up",
     "why": "stop to do = остановиться, чтобы: to pick up."},
    {"id": "t6-talking", "t": 6, "q": "Please stop ___ — the patient is trying to sleep.", "opts": ["talking", "to talk"], "a": "talking",
     "why": "Прекратить разговор — stop talking."},
    {"id": "t6-blaming", "t": 6, "q": "Stop ___ yourself — it wasn't your fault.", "opts": ["blaming", "to blame"], "a": "blaming",
     "why": "Прекратить действие — stop blaming."},

    # 7 — try
    {"id": "t7-keep", "t": 7, "q": "Try ___ still during the scan.", "opts": ["to keep", "keeping"], "a": "to keep",
     "why": "try to do = постараться, приложить усилие."},
    {"id": "t7-taking", "t": 7, "q": "If the headache persists, try ___ paracetamol.", "opts": ["taking", "to take"], "a": "taking",
     "why": "try doing = попробовать как способ: taking."},
    {"id": "t7-turning", "t": 7, "q": "Have you tried ___ the monitor off and on again?", "opts": ["turning", "to turn"], "a": "turning",
     "why": "Попробовать способ — tried turning."},
    {"id": "t7-be", "t": 7, "q": "Please try ___ on time tomorrow.", "opts": ["to be", "being"], "a": "to be",
     "why": "Постарайтесь — усилие: try to be."},

    # 8 — regret, mean, go on
    {"id": "t8-inform", "t": 8, "q": "We regret ___ you that the clinic is closed.", "opts": ["to inform", "informing"], "a": "to inform",
     "why": "regret to inform — официальное «с сожалением сообщаем»."},
    {"id": "t8-ordering", "t": 8, "q": "I regret ___ an MRI earlier.", "opts": ["not ordering", "not to order"], "a": "not ordering",
     "why": "Жалею о сделанном или несделанном — -ing."},
    {"id": "t8-means", "t": 8, "q": "Delaying the scan means ___ brain tissue.", "opts": ["losing", "to lose"], "a": "losing",
     "why": "mean = означать: losing."},
    {"id": "t8-meant", "t": 8, "q": "I didn't mean ___ you.", "opts": ["to upset", "upsetting"], "a": "to upset",
     "why": "mean = намереваться: to upset."},
    {"id": "t8-goon", "t": 8, "q": "After a short introduction, she went on ___ a clinical case.", "opts": ["to present", "presenting"], "a": "to present",
     "why": "go on to do = перейти к следующему: to present."},

    # 9 — можно и так, и так
    {"id": "t9-like", "t": 9, "q": "I'd like ___ to the consultant, please.", "opts": ["to speak", "speaking"], "a": "to speak",
     "why": "would like — только to do."},
    {"id": "t9-began", "t": 9, "q": "The patient began ___ on the third day.", "opts": ["to improve", "improving"], "a": "to improve",
     "also": {"improving": "begin берёт обе формы без разницы в смысле"},
     "why": "begin — обе формы верны."},
    {"id": "t9-continue", "t": 9, "q": "Continue ___ the tablets until your next appointment.", "opts": ["taking", "to take"], "a": "taking",
     "also": {"to take": "continue берёт обе формы"},
     "why": "continue — обе формы верны."},
    {"id": "t9-prefer", "t": 9, "q": "Would you prefer ___ the procedure under sedation?", "opts": ["to have", "having"], "a": "to have",
     "why": "would prefer — только to do."},
    {"id": "t9-started", "t": 9, "q": "It started ___ just as we left the hospital.", "opts": ["raining", "to rain"], "a": "raining",
     "also": {"to rain": "start берёт обе формы"},
     "why": "start — обе формы верны."},

    # 10 — used to, needs doing
    {"id": "t10-used", "t": 10, "q": "I used to ___ in Moscow before I moved here.", "opts": ["work", "working"], "a": "work",
     "why": "used to do = раньше делал, больше нет: work."},
    {"id": "t10-am-used", "t": 10, "q": "I'm used to ___ nights.", "opts": ["working", "work"], "a": "working",
     "why": "be used to = привык; to — предлог: working."},
    {"id": "t10-get-used", "t": 10, "q": "You'll soon get used to ___ the new system.", "opts": ["using", "use"], "a": "using",
     "why": "get used to = привыкнуть; дальше -ing."},
    {"id": "t10-needs", "t": 10, "q": "The dressing needs ___ every day.", "opts": ["changing", "to change"], "a": "changing",
     "why": "needs doing = нужно, чтобы сделали: needs changing."},
    {"id": "t10-need-to", "t": 10, "q": "You need ___ this form before the procedure.", "opts": ["to sign", "signing"], "a": "to sign",
     "why": "Делать будете вы сами — need to sign."},
]

# 11 — быстрая проверка по спискам: глагол → to do или doing
NO_SORT = {"be used to"}          # be used to do тоже бывает (= «используется для») — в проверку не берём
SPECIAL = {
    "offer": "offer — предложить сделать самому: to do. А suggest — предложить идею — с -ing.",
    "need": "need — надо сделать самому: to do.",
}
ALSO = {"need": {"doing": "needs doing — «нужно, чтобы сделали»: the dressing needs changing"}}


def slug(v):
    return v.replace("'", "").replace(" ", "-")


for kind, groups in (("to", TO_GROUPS), ("ing", ING_GROUPS)):
    for g in groups:
        for raw in g["verbs"]:
            v = raw.rstrip("*")
            if v in NO_SORT:
                continue
            prep = v.endswith(" to")
            stem = v[:-3] if prep else v
            if kind == "to":
                opts, a, rule = ["to do", "doing"], "to do", "действие впереди, поэтому to do"
            elif prep:
                opts, a, rule = ["to doing", "to do"], "to doing", None
            else:
                opts, a, rule = ["doing", "to do"], "doing", "само действие, поэтому -ing"
            if v in SPECIAL:
                why = SPECIAL[v]
            elif rule:
                why = f"{v} — {VERB_RU[v]}. Группа «{g['ru']}»: {rule}."
            else:
                why = f"{v} — {VERB_RU[v]}. to здесь предлог, после него -ing."
            card = {"id": "v-" + slug(v), "t": SORT_TOPIC, "q": stem + " ___", "ru": VERB_RU[v],
                    "opts": opts, "a": a, "why": why}
            if v in ALSO:
                card["also"] = ALSO[v]
            CARDS.append(card)
