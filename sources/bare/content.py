# Содержание тренажёра «Инфинитив без to» — когда после слова идёт голая форма глагола: модальные (must rest),
# do, does, did (did you take), make и let (make him wait, let me know), had better, would rather, why not, help,
# see и hear (saw him fall), пассив, где to возвращается (was made to wait), и особые конструкции (All I did was ask).
# Отличие от «To или -ing» (toing) и «Кого + to do» (kogo): там конструкции с to и -ing; здесь — где to не нужен.
# В «remember» (vm) есть одна тема see sb do / doing; здесь она шире — с пассивом was seen to.
# Разметка в примерах: [слово|a] — то, после чего голая форма (оранжевый); [глагол|b] — голая форма (синий);
# [to …|c] — сравнение, где to нужен (зелёный).
# Темы с полем late вступают в общую тренировку позже.

MIXED_TOPIC = 9

GROUPS = {
    "b1": "B1 — модальные, did, make и let",
    "b1p": "B1+ — had better, help, see и hear",
    "b2": "B2 — пассив и особые конструкции",
    "mix": "Итог",
}

# Главная таблица: после чего | правило («главное — пояснение») | примеры
TABLE = [
    ["can, must, should, will", "модальные — кроме ought to, have to, need to", "must rest · might need"],
    ["do, does, did", "время уже в помощнике — глагол в начальной форме", "did you take · doesn't smoke"],
    ["make, let", "кого-то + глагол без to", "make him wait · let me know"],
    ["had better, would rather", "совет и предпочтение", "had better call · would rather stay"],
    ["help", "to можно поставить, можно нет", "help me carry · help to reduce"],
    ["see, hear, watch, feel", "всё действие целиком", "saw him fall · heard it go off"],
    ["в пассиве", "to возвращается", "was made to wait · was seen to leave"],
]

# Одна ситуация — разная форма: строки [английский, перевод]
CONTRAST = [
    [["You [must|a] [rest|b].", "модальный — без to"],
     ["You [have to|c] rest.", "have to — с to"]],
    [["They [made|a] him [wait|b].", "актив — без to"],
     ["He was [made to wait|c].", "пассив — с to"]],
    [["[Let|a] me [explain|b].", "let — без to"],
     ["Allow me [to explain|c].", "allow — с to"]],
    [["I'd [rather|a] [stay|b].", "would rather — без to"],
     ["I'd prefer [to stay|c].", "prefer — с to"]],
    [["I [saw|a] him [fall|b].", "видел всё падение"],
     ["I saw him [falling|c].", "застал, когда он падал"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["You must to rest.", "You must rest.", "после must — без to"],
    ["Did you took your tablets?", "Did you take your tablets?", "после did — начальная форма"],
    ["He doesn't smokes.", "He doesn't smoke.", "после doesn't — без -s"],
    ["They made us to wait.", "They made us wait.", "make кого-то — без to"],
    ["Let me to explain.", "Let me explain.", "let — без to"],
    ["I'd rather to stay.", "I'd rather stay.", "would rather — без to"],
    ["Why not to try?", "Why not try?", "why not — без to"],
    ["I saw him to fall.", "I saw him fall.", "see кого-то — без to"],
    ["He was made wait.", "He was made to wait.", "в пассиве — с to"],
    ["He was let to go home.", "He was allowed to go home.", "let пассива не имеет — be allowed to"],
]

TOPICS = [
    {"n": 1, "group": "b1", "title": "must rest, might need", "sub": "после модальных — без to",
     "rule": "После модальных глаголов can, could, must, should, will, would, may, might, shall — глагол без to: You must rest, He might need surgery, Can you lift your arm? Исключения, которые выглядят как модальные, но с to: ought to, have to, need to, be able to, used to. В отрицании needn't — без to: You needn't fast.",
     "ex": [
         {"en": "You [must|a] [rest|b] for a week.", "ru": "Вам нужно неделю отдыхать."},
         {"en": "He [might|a] [need|b] a second scan.", "ru": "Возможно, ему понадобится повторный снимок."},
         {"en": "You [ought to|c] stop smoking.", "ru": "Вам стоило бы бросить курить."},
     ]},
    {"n": 2, "group": "b1", "title": "did you take, doesn't smoke", "sub": "после do, does, did",
     "rule": "После do, does и did глагол всегда в начальной форме: время и окончание -s уже взял на себя помощник. Did you take your tablets? — не took. He doesn't smoke — не smokes. Does it hurt? — не hurts. Усиление «я же говорил» — тоже с голой формой: I did tell you to fast.",
     "ex": [
         {"en": "[Did|a] you [take|b] your tablets this morning?", "ru": "Вы приняли таблетки утром?"},
         {"en": "He [doesn't|a] [smoke|b].", "ru": "Он не курит."},
         {"en": "I [did|a] [tell|b] you to fast before the test!", "ru": "Я же говорил вам прийти натощак!"},
     ]},
    {"n": 3, "group": "b1", "title": "make him wait, let me know", "sub": "make и let + кого-то + глагол",
     "rule": "make + кого-то + глагол без to — заставить или вызвать: They made us wait; These tablets make me feel dizzy. let + кого-то + глагол без to — разрешить: Let me know; We can't let him go home yet. Let's — давайте: Let's start. А allow, ask, tell, want — с to: allow me to use, tell him to rest.",
     "ex": [
         {"en": "[Let|a] me [know|b] if the pain gets worse.", "ru": "Дайте знать, если боль усилится."},
         {"en": "These tablets [make|a] me [feel|b] dizzy.", "ru": "От этих таблеток у меня кружится голова."},
         {"en": "The nurse didn't allow me [to use|c] my phone.", "ru": "Медсестра не разрешила мне пользоваться телефоном."},
     ]},
    {"n": 4, "group": "b1p", "title": "had better, would rather", "sub": "why not, rather than", "late": 0.2,
     "rule": "Без to после had better (’d better) — лучше бы: You'd better call the GP. После would rather (’d rather) — предпочёл бы: I'd rather stay at home; отрицание — I'd rather not talk about it. После why not — почему бы не: Why not try the new inhaler? После rather than — вместо того чтобы: Rather than wait, we started treatment. Сравните: I'd prefer to stay — prefer с to.",
     "ex": [
         {"en": "You['d better|a] [call|b] the GP.", "ru": "Лучше позвоните терапевту."},
         {"en": "I['d rather|a] [stay|b] at home.", "ru": "Я бы предпочёл остаться дома."},
         {"en": "[Why not|a] [try|b] the new inhaler?", "ru": "Почему бы не попробовать новый ингалятор?"},
     ]},
    {"n": 5, "group": "b1p", "title": "help me carry", "sub": "help — to можно и без", "late": 0.2,
     "rule": "После help to можно поставить, а можно опустить — оба варианта верны: help me carry it = help me to carry it; Statins help reduce the risk = help to reduce. Без to чаще в разговоре и в американском. -ing после help нельзя: help carrying — ошибка. Не путайте с can't help + -ing — «не могу удержаться»: She couldn't help crying.",
     "ex": [
         {"en": "Could you [help|a] me [carry|b] these files?", "ru": "Поможете донести эти папки?"},
         {"en": "Statins [help|a] [reduce|b] the risk of another stroke.", "ru": "Статины помогают снизить риск повторного инсульта."},
         {"en": "Exercise can help [to lower|c] blood pressure.", "ru": "Физическая нагрузка помогает снизить давление."},
     ]},
    {"n": 6, "group": "b1p", "title": "saw him fall", "sub": "see, hear, watch, feel + кого-то + глагол", "late": 0.25,
     "rule": "После see, hear, watch, feel, notice + кого-то — глагол без to, если видели всё действие целиком: I saw him fall; Did you hear the alarm go off? С -ing — если застали в процессе: When I came in, I saw him climbing the stairs. To здесь не ставят: I saw him to fall — ошибка.",
     "ex": [
         {"en": "I [saw|a] him [fall|b] in the corridor.", "ru": "Я видел, как он упал в коридоре."},
         {"en": "Did you [hear|a] the alarm [go off|b]?", "ru": "Вы слышали, как сработала сигнализация?"},
         {"en": "When I came in, I saw him [climbing|c] the stairs.", "ru": "Когда я вошёл, он как раз поднимался по лестнице."},
     ]},
    {"n": 7, "group": "b2", "title": "was made to wait", "sub": "в пассиве to возвращается", "late": 0.45,
     "rule": "В активе после make, see, hear — без to, а в пассиве to возвращается: They made him wait → He was made to wait; Someone saw him leave → He was seen to leave. let пассива не имеет — вместо него be allowed to: They let him go home → He was allowed to go home. help в пассиве — тоже с to: He was helped to stand.",
     "ex": [
         {"en": "He [was made to|c] wait for three hours.", "ru": "Его заставили ждать три часа."},
         {"en": "He [was seen to|c] leave the building at 10 p.m.", "ru": "Видели, как он вышел из здания в 22:00."},
         {"en": "She [was allowed to|c] go home after two days.", "ru": "Через два дня её отпустили домой."},
     ]},
    {"n": 8, "group": "b2", "title": "All I did was ask", "sub": "особые конструкции", "late": 0.5,
     "rule": "Голая форма бывает и в выделительных конструкциях: All I did was ask a question — я всего лишь задал вопрос; What we did was call the family. После do nothing but и do everything except: He does nothing but complain. Риторическое why — зачем: Why take the bus when you can walk? В американском разговорном — go get, come see: Go get the doctor; в британском — go and get.",
     "ex": [
         {"en": "[All I did was|a] [ask|b] a question.", "ru": "Я всего лишь задал вопрос."},
         {"en": "He [does nothing but|a] [complain|b] about the food.", "ru": "Он только и делает, что жалуется на еду."},
         {"en": "[Why|a] [take|b] the bus when you can walk?", "ru": "Зачем ехать на автобусе, если можно пешком?"},
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
    # 1 · модальные
    c("x1-must", 1, "You must ___ for at least a week.", "Вам нужно отдыхать как минимум неделю.",
      ["rest", "to rest", "resting"], "rest", "После must — глагол без to."),
    c("x1-can", 1, "Can you ___ your arm?", "Вы можете поднять руку?",
      ["lift", "to lift", "lifting"], "lift", "После can — без to."),
    c("x1-might", 1, "He might ___ a second scan.", "Возможно, ему понадобится повторный снимок.",
      ["need", "to need", "needs"], "need", "После might — начальная форма, без to и без -s."),
    c("x1-should", 1, "You should ___ more water.", "Вам стоит пить больше воды.",
      ["drink", "to drink", "drinking"], "drink", "После should — без to."),
    c("x1-ought", 1, "You ought ___ smoking.", "Вам стоило бы бросить курить.",
      ["to stop", "stop", "stopping"], "to stop", "ought — исключение: ought to."),
    c("x1-able", 1, "Will he be able ___ again?", "Он сможет снова ходить?",
      ["to walk", "walk", "walking"], "to walk", "be able to — с to. А can — без: Can he walk?"),

    # 2 · do, does, did
    c("x2-did", 2, "Did you ___ your tablets this morning?", "Вы приняли таблетки утром?",
      ["take", "took", "taken"], "take", "После did — начальная форма: прошедшее уже в did."),
    c("x2-doesnt", 2, "He doesn't ___.", "Он не курит.",
      ["smoke", "smokes", "smoking"], "smoke", "После doesn't — без -s: оно уже в does."),
    c("x2-does", 2, "Does it ___ when you breathe in?", "Болит, когда вы вдыхаете?",
      ["hurt", "hurts", "hurting"], "hurt", "После does — начальная форма."),
    c("x2-didnt", 2, "She didn't ___ the pain until the next day.", "Боль она заметила только на следующий день.",
      ["notice", "noticed", "to notice"], "notice", "После didn't — начальная форма."),
    c("x2-emph", 2, "I ___ tell you to fast before the test!", "Я же говорил вам прийти натощак!",
      ["did", "do", "was"], "did", "Усиление «я же говорил» — did + начальная форма: I did tell you."),
    c("x2-why", 2, "Why didn't you ___ an ambulance?", "Почему вы не вызвали скорую?",
      ["call", "called", "to call"], "call", "После didn't — начальная форма."),

    # 3 · make и let
    c("x3-know", 3, "Let me ___ if the pain gets worse.", "Дайте знать, если боль усилится.",
      ["know", "to know", "knowing"], "know", "let + кого-то + глагол без to: let me know."),
    c("x3-wait", 3, "They made us ___ for three hours in A&E.", "Нас заставили три часа ждать в приёмном.",
      ["wait", "to wait", "waiting"], "wait", "make + кого-то + глагол без to."),
    c("x3-feel", 3, "These tablets make me ___ dizzy.", "От этих таблеток у меня кружится голова.",
      ["feel", "to feel", "feeling"], "feel", "make в значении «вызывать» — тоже без to: make me feel."),
    c("x3-go", 3, "We can't let him ___ home yet.", "Пока мы не можем отпустить его домой.",
      ["go", "to go", "going"], "go", "let + кого-то + глагол без to."),
    c("x3-lets", 3, "Let's ___ the ward round.", "Давайте начнём обход.",
      ["start", "to start", "starting"], "start", "Let's — без to."),
    c("x3-allow", 3, "The nurse didn't allow me ___ my phone.", "Медсестра не разрешила мне пользоваться телефоном.",
      ["to use", "use", "using"], "to use", "allow — с to: allow me to use. Без to — только let: let me use."),

    # 4 · had better, would rather, why not
    c("x4-better", 4, "You'd better ___ the GP.", "Лучше позвоните терапевту.",
      ["call", "to call", "calling"], "call", "had better — без to."),
    c("x4-rather", 4, "I'd rather ___ at home.", "Я бы предпочёл остаться дома.",
      ["stay", "to stay", "staying"], "stay", "would rather — без to."),
    c("x4-rathernot", 4, "I'd rather ___ about it now.", "Я бы не хотел сейчас об этом говорить.",
      ["not talk", "not to talk", "don't talk"], "not talk", "Отрицание — would rather not + глагол без to."),
    c("x4-whynot", 4, "Why not ___ the new inhaler?", "Почему бы не попробовать новый ингалятор?",
      ["try", "to try", "trying"], "try", "why not — без to."),
    c("x4-prefer", 4, "I'd prefer ___ at home.", "Я бы предпочёл остаться дома.",
      ["to stay", "stay", "staying"], "to stay", "prefer — с to. Без to — would rather: I'd rather stay."),
    c("x4-ratherthan", 4, "Rather than ___ for the results, we started treatment.", "Не дожидаясь результатов, мы начали лечение.",
      ["wait", "to wait", "waited"], "wait", "rather than + начальная форма: rather than wait. Встречается и rather than waiting."),

    # 5 · help
    c("x5-carry", 5, "Could you help me ___ these files?", "Поможете донести эти папки?",
      ["carry", "carrying", "carried"], "carry", "help + кого-то + глагол: help me carry (или to carry). -ing нельзя."),
    c("x5-reduce", 5, "Statins help ___ the risk of another stroke.", "Статины помогают снизить риск повторного инсульта.",
      ["reduce", "reducing", "reduced"], "reduce", "help reduce = help to reduce."),
    c("x5-to", 5, "Exercise can help ___ blood pressure.", "Физическая нагрузка помогает снизить давление.",
      ["to lower", "lowering", "lowered"], "to lower", "help + to + глагол — тоже верно."),
    c("x5-dressed", 5, "The nurse helped him ___ dressed.", "Медсестра помогла ему одеться.",
      ["get", "getting", "got"], "get", "help + кого-то + глагол без to: helped him get dressed."),
    c("x5-crying", 5, "She couldn't help ___ when she saw the results.", "Увидев результаты, она не смогла сдержать слёз.",
      ["crying", "cry", "to cry"], "crying", "can't help + -ing — «не могу удержаться», это не «помогать»."),
    c("x5-walk", 5, "Physiotherapists help patients ___ again.", "Физиотерапевты помогают пациентам снова ходить.",
      ["walk", "walking", "walked"], "walk", "help + кого-то + глагол без to."),

    # 6 · see, hear, watch, feel
    c("x6-fall", 6, "I saw him ___ in the corridor.", "Я видел, как он упал в коридоре.",
      ["fall", "to fall", "fell"], "fall", "see + кого-то + глагол без to — видел всё действие."),
    c("x6-alarm", 6, "Did you hear the alarm ___?", "Вы слышали, как сработала сигнализация?",
      ["go off", "to go off", "went off"], "go off", "hear + что-то + глагол без to."),
    c("x6-needle", 6, "I felt the needle ___ in.", "Я почувствовал, как вошла игла.",
      ["go", "to go", "went"], "go", "feel + что-то + глагол без to."),
    c("x6-line", 6, "We watched the nurse ___ the line.", "Мы смотрели, как медсестра ставит катетер.",
      ["insert", "to insert", "inserted"], "insert", "watch + кого-то + глагол без to."),
    c("x6-leave", 6, "Nobody noticed him ___ the ward.", "Никто не заметил, как он ушёл из отделения.",
      ["leave", "to leave", "left"], "leave", "notice + кого-то + глагол без to."),
    c("x6-climbing", 6, "When I came in, I saw him ___ the stairs.", "Когда я вошёл, он как раз поднимался по лестнице.",
      ["climbing", "climb", "to climb"], "climbing", "Застал в процессе — -ing: saw him climbing.",
      also={"climb": "грамматически верно, но значит «видел, как он поднялся целиком»; застал в процессе — climbing"}),

    # 7 · в пассиве — с to
    c("x7-made", 7, "He was made ___ for three hours.", "Его заставили ждать три часа.",
      ["to wait", "wait", "waiting"], "to wait", "В пассиве to возвращается: was made to wait."),
    c("x7-seen", 7, "He was seen ___ the building at 10 p.m.", "Видели, как он вышел из здания в 22:00.",
      ["to leave", "leave", "left"], "to leave", "Пассив от see — с to: was seen to leave."),
    c("x7-allowed", 7, "She was ___ to go home after two days.", "Через два дня её отпустили домой.",
      ["allowed", "let", "made"], "allowed", "let пассива не имеет — be allowed to."),
    c("x7-heard", 7, "He was heard ___ for help.", "Слышали, как он звал на помощь.",
      ["to shout", "shout", "shouted"], "to shout", "Пассив от hear — с to: was heard to shout."),
    c("x7-active", 7, "The new rules make doctors ___ every dose twice.", "Новые правила заставляют врачей дважды проверять каждую дозу.",
      ["check", "to check", "checking"], "check", "Актив — без to: make doctors check. Пассив — с to: doctors are made to check."),
    c("x7-helped", 7, "He was helped ___ up by two nurses.", "Две медсестры помогли ему встать.",
      ["to stand", "stand", "standing"], "to stand", "Пассив от help — с to: was helped to stand."),

    # 8 · особые конструкции
    c("x8-all", 8, "All I did was ___ a question.", "Я всего лишь задал вопрос.",
      ["ask", "asked", "asking"], "ask", "All I did was + начальная форма. На письме встречается и was to ask."),
    c("x8-what", 8, "What we did was ___ the family immediately.", "Мы сразу же позвонили родственникам.",
      ["call", "called", "calling"], "call", "What we did was + начальная форма."),
    c("x8-nothing", 8, "He does nothing but ___ about the food.", "Он только и делает, что жалуется на еду.",
      ["complain", "to complain", "complaining"], "complain", "do nothing but + начальная форма."),
    c("x8-except", 8, "He did everything except ___ the consent form.", "Он сделал всё, кроме одного — не подписал согласие.",
      ["sign", "to sign", "signed"], "sign", "do everything except + начальная форма."),
    c("x8-why", 8, "Why ___ the bus when you can walk?", "Зачем ехать на автобусе, если можно пешком?",
      ["take", "to take", "taking"], "take", "Риторическое why — «зачем» + начальная форма: Why take, Why wait."),
    c("x8-go", 8, "Go ___ the doctor — the patient is waking up.", "Сходи позови врача — пациент приходит в себя.",
      ["get", "to get", "getting"], "get", "Разговорное go get (амер.) — без to. В британском — go and get."),
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
