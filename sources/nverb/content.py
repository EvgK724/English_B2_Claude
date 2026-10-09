# Содержание тренажёра «Advice и advise» — похожие пары «существительное — глагол»:
# advice и advise, breath и breathe, belief и believe, loss и lose, use [s] и use [z], treatment и treat,
# REcord и reCORD, death, dead и died. Отличие от «Пар слов» (pairs): там ловушки по смыслу (device и devise,
# affect и effect), здесь — система: как из существительного получается глагол и как это слышно.
# Разметка в примерах: [слово|a] — существительное (оранжевый), [слово|b] — глагол (синий), [слово|c] — прилагательное (зелёный).
# Поле say — что произносить вместо предложения с ответом (ударение REcord и reCORD, вопросы о звуке).
# Темы с полем late вступают в общую тренировку позже.

MIXED_TOPIC = 9

GROUPS = {
    "b1": "B1 — одна буква, другой звук",
    "b1p": "B1+ — разные слова и суффиксы",
    "b2": "B2 — ударение и ловушки",
    "mix": "Итог",
}

# Главная таблица: образец | правило («главное — пояснение») | пары
TABLE = [
    ["advice · advise", "c → s — существительное [s], глагол [z]", "advice · advise · practice · practise"],
    ["breath · breathe", "th → the — [θ] → [ð], гласная меняется", "breath · breathe · bath · bathe"],
    ["belief · believe", "f → v — существительное глухое, глагол звонкий", "belief · believe · proof · prove · relief · relieve"],
    ["use · use", "пишется одинаково — существительное [s], глагол [z]", "use · excuse · close · house"],
    ["loss · lose", "разные формы — запоминать парой", "loss · lose · choice · choose · success · succeed"],
    ["REcord · reCORD", "ударение — существительное на первый, глагол на второй", "REcord · reCORD · INcrease · inCREASE"],
]

# Одна ситуация — разное слово: строки [английский, перевод]
CONTRAST = [
    [["Take my [advice|a].", "совет — [s]"],
     ["I [advise|b] you to rest.", "советую — [z]"]],
    [["Take a deep [breath|a].", "вдох — [θ]"],
     ["[Breathe|b] in slowly.", "дышите — [ð]"]],
    [["What's the [use|a] of worrying?", "польза — [s]"],
     ["How do I [use|b] this inhaler?", "пользоваться — [z]"]],
    [["Keep a [record|a] of your blood pressure.", "запись — ударение на re"],
     ["[Record|b] it every morning.", "записывайте — ударение на cord"]],
    [["The cause of [death|a] was a stroke.", "смерть — существительное"],
     ["He [died|b] in 2020.", "умер — глагол"],
     ["He was [dead|c] on arrival.", "мёртв — прилагательное"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["Can you give me an advise?", "Can you give me some advice?", "совет — advice, без a"],
    ["I advice you to rest.", "I advise you to rest.", "советовать — advise [z]"],
    ["Take a deep breathe.", "Take a deep breath.", "вдох — breath"],
    ["I can't breath.", "I can't breathe.", "дышать — breathe"],
    ["There's no prove.", "There's no proof.", "доказательство — proof"],
    ["It's your choose.", "It's your choice.", "выбор — choice"],
    ["The operation was succeed.", "The operation was a success.", "успех — success"],
    ["a weight lose", "weight loss", "потеря — loss"],
    ["Her father is died.", "Her father died. / He is dead.", "умер — died, мёртв — dead"],
    ["I born in 1980.", "I was born in 1980.", "родился — was born"],
]

TOPICS = [
    {"n": 1, "group": "b1", "title": "advice или advise", "sub": "c — существительное, s — глагол",
     "rule": "Существительное пишется с c и звучит с [s]: advice /ədˈvaɪs/ — совет. Глагол — с s и звучит с [z]: advise /ədˈvaɪz/ — советовать. Так же в британском: practice — практика, practise — практиковаться; licence — лицензия, права, license — разрешать. В американском practice и license пишут одинаково для обоих. Прошедшее — advised, а не adviced.",
     "ex": [
         {"en": "Thank you for your [advice|a].", "ru": "Спасибо за совет."},
         {"en": "I'd [advise|b] you to stop smoking.", "ru": "Я бы посоветовал вам бросить курить."},
         {"en": "You need to [practise|b] in general [practice|a].", "ru": "Вам нужно поработать в общей практике."},
     ]},
    {"n": 2, "group": "b1", "title": "breath или breathe", "sub": "[θ] → [ð], гласная меняется",
     "rule": "Существительное кончается на th без e и звучит с глухим [θ]: breath /breθ/ — вдох, дыхание; bath /bɑːθ/ — ванна; cloth /klɒθ/ — ткань. Глагол — с e на конце и звонким [ð], а гласная становится долгой: breathe /briːð/ — дышать; bathe /beɪð/ — промывать, купать; clothe /kləʊð/ — одевать. Одышка — short of breath; дышите — breathe in.",
     "ex": [
         {"en": "Take a deep [breath|a] and [breathe|b] out slowly.", "ru": "Глубоко вдохните и медленно выдохните."},
         {"en": "[Bathe|b] the wound, then have a [bath|a] tomorrow.", "ru": "Промойте рану, а ванну можно завтра."},
         {"en": "Clean it with a damp [cloth|a].", "ru": "Протрите влажной тряпкой."},
     ]},
    {"n": 3, "group": "b1", "title": "belief или believe", "sub": "f — существительное, v — глагол",
     "rule": "Существительное кончается глухим [f], глагол — звонким [v]: belief — believe, proof — prove, relief — relieve, grief — grieve, half — halve. Обезболивание — pain relief, облегчить боль — relieve the pain. Доказательство — proof, доказать — prove. Уменьшить вдвое — halve the dose.",
     "ex": [
         {"en": "The injection gave quick [relief|a].", "ru": "Укол быстро облегчил боль."},
         {"en": "Paracetamol should [relieve|b] the pain.", "ru": "Парацетамол должен снять боль."},
         {"en": "There's no [proof|a], so we can't [prove|b] it.", "ru": "Доказательств нет, поэтому доказать это мы не можем."},
     ]},
    {"n": 4, "group": "b1p", "title": "loss или lose, choice или choose", "sub": "разные слова — запоминать парой", "late": 0.2,
     "rule": "У части пар формы совсем разные — их учат парой. loss — потеря, lose — терять: hearing loss, weight loss; lose weight. choice — выбор, choose — выбирать. success — успех, succeed — добиться успеха. complaint — жалоба, complain — жаловаться. speech — речь, speak — говорить. Типичная ошибка — глагол на месте существительного: it's your choose, weight lose.",
     "ex": [
         {"en": "He has some hearing [loss|a] in his left ear.", "ru": "Слух на левое ухо у него снижен."},
         {"en": "Try to [lose|b] some weight.", "ru": "Постарайтесь немного похудеть."},
         {"en": "It's your [choice|a] — you can [choose|b] either option.", "ru": "Решать вам — можете выбрать любой вариант."},
     ]},
    {"n": 5, "group": "b1p", "title": "use [s] и use [z]", "sub": "пишется одинаково, звучит по-разному", "late": 0.2,
     "rule": "У некоторых слов существительное и глагол пишутся одинаково, а звучат по-разному: существительное с [s], глагол с [z]. use /juːs/ — польза, применение; use /juːz/ — пользоваться. excuse /ɪkˈskjuːs/ — оправдание; excuse /ɪkˈskjuːz/ — извинить. house /haʊs/ — дом; house /haʊz/ — размещать. Прилагательное close /kləʊs/ — близкий; глагол close /kləʊz/ — закрывать.",
     "ex": [
         {"en": "What's the [use|a] of worrying?", "ru": "Какой смысл волноваться?"},
         {"en": "How do I [use|b] this inhaler?", "ru": "Как пользоваться этим ингалятором?"},
         {"en": "She lives [close|c] to the hospital — [close|b] the door, please.", "ru": "Она живёт рядом с больницей. Закройте дверь, пожалуйста."},
     ]},
    {"n": 6, "group": "b1p", "title": "treat или treatment", "sub": "-ment, -ion, -y — существительные", "late": 0.25,
     "rule": "Многие существительные получаются из глагола суффиксом: treat → treatment, improve → improvement, admit → admission, prescribe → prescription, decide → decision, recover → recovery. На месте подлежащего, после a, the, his, of — существительное: The treatment was effective, on admission. После to, can, will — глагол: to treat, can recover.",
     "ex": [
         {"en": "The [treatment|a] was effective — we can [treat|b] it at home.", "ru": "Лечение помогло — дальше можно лечить дома."},
         {"en": "On [admission|a], his blood pressure was 190/100.", "ru": "При поступлении давление было 190/100."},
         {"en": "He made a full [recovery|a].", "ru": "Он полностью поправился."},
     ]},
    {"n": 7, "group": "b2", "title": "REcord или reCORD", "sub": "ударение: существительное — вперёд", "late": 0.45,
     "rule": "У двусложных пар, которые пишутся одинаково, существительное ударное на первом слоге, глагол — на втором. a REcord — запись, to reCORD — записывать; an INcrease — рост, to inCREASE — увеличивать; PROgress — прогресс, to proGRESS — прогрессировать; a PREsent — подарок, to preSENT — представить, доложить; an OBject — предмет, to obJECT — возражать. Слушайте, как Ryan меняет ударение.",
     "ex": [
         {"en": "Keep a [record|a] of your blood pressure.", "ru": "Записывайте давление (ведите дневник)."},
         {"en": "[Record|b] it every morning.", "ru": "Записывайте его каждое утро."},
         {"en": "There's been an [increase|a], so we'll [increase|b] the dose.", "ru": "Показатель вырос, поэтому увеличим дозу."},
     ]},
    {"n": 8, "group": "b2", "title": "died, dead, death, born", "sub": "глагол, прилагательное, существительное", "late": 0.5,
     "rule": "die — глагол: He died last year, he is dying. dead — прилагательное: He is dead, dead on arrival. death — существительное: the cause of death. Ошибки: he is died, the dead was sudden. Родиться — пассив: I was born. Born — форма, а не глагол: I born — ошибка. Рождение — birth: date of birth.",
     "ex": [
         {"en": "He [died|b] last year — the cause of [death|a] was a stroke.", "ru": "Он умер в прошлом году — причина смерти инсульт."},
         {"en": "The patient was [dead|c] on arrival.", "ru": "Пациент поступил уже мёртвым."},
         {"en": "I was [born|b] in 1975 — my date of [birth|a] is on the form.", "ru": "Я родился в 1975 году — дата рождения есть в бланке."},
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
    # 1 · advice или advise
    c("v1-advice", 1, "Thank you for your ___.", "Спасибо за совет.",
      ["advice", "advise"], "advice", "Существительное — advice /ədˈvaɪs/, с [s]."),
    c("v1-advise", 1, "I'd ___ you to stop smoking.", "Я бы посоветовал вам бросить курить.",
      ["advise", "advice"], "advise", "Глагол — advise /ədˈvaɪz/, с [z]."),
    c("v1-advised", 1, "She was ___ to rest for a week.", "Ей посоветовали неделю отдыхать.",
      ["advised", "adviced"], "advised", "Прошедшее от advise — advised. Adviced — ошибка."),
    c("v1-practice", 1, "General ___ is very busy in winter.", "Зимой у врачей общей практики много работы.",
      ["practice", "practise"], "practice", "Существительное — practice: практика врача, тренировка."),
    c("v1-practise", 1, "You need to ___ your English every day.", "Вам нужно каждый день заниматься английским.",
      ["practise", "practice"], "practise", "Глагол в британском — practise.",
      also={"practice": "в американском так и пишут: глагол тоже practice"}),
    c("v1-licence", 1, "He lost his driving ___ after the seizure.", "После приступа у него отобрали права.",
      ["licence", "license"], "licence", "В британском существительное — licence, глагол — license.",
      also={"license": "американское написание — и для существительного"}),

    # 2 · breath или breathe
    c("v2-breath", 2, "Take a deep ___.", "Глубоко вдохните.",
      ["breath", "breathe"], "breath", "Вдох — breath /breθ/: существительное, глухой [θ]."),
    c("v2-breathe", 2, "Can you ___ through your nose?", "Вы можете дышать носом?",
      ["breathe", "breath"], "breathe", "Дышать — breathe /briːð/: глагол, звонкий [ð], долгое [iː]."),
    c("v2-short", 2, "She gets short of ___ on the stairs.", "На лестнице у неё одышка.",
      ["breath", "breathe"], "breath", "Одышка — short of breath: существительное."),
    c("v2-bath", 2, "The nurse helped him have a ___.", "Медсестра помогла ему принять ванну.",
      ["bath", "bathe"], "bath", "Ванна — bath /bɑːθ/."),
    c("v2-bathe", 2, "___ the wound gently with salt water.", "Аккуратно промойте рану солевым раствором.",
      ["Bathe", "Bath"], "Bathe", "Промывать, омывать — bathe /beɪð/: глагол, звонкий [ð]."),
    c("v2-cloth", 2, "Clean the cut with a damp ___.", "Протрите порез влажной салфеткой.",
      ["cloth", "clothe", "clothes"], "cloth", "cloth /klɒθ/ — ткань, салфетка. clothes /kləʊðz/ — одежда, clothe — одевать (книжно)."),

    # 3 · belief или believe
    c("v3-relief", 3, "The injection gave him immediate ___.", "Укол сразу облегчил ему боль.",
      ["relief", "relieve"], "relief", "Облегчение — relief: существительное, [f]."),
    c("v3-relieve", 3, "Paracetamol should ___ the pain.", "Парацетамол должен снять боль.",
      ["relieve", "relief"], "relieve", "Облегчить — relieve: глагол, [v]."),
    c("v3-proof", 3, "There's no ___ that it works.", "Нет доказательств, что это работает.",
      ["proof", "prove"], "proof", "Доказательство — proof."),
    c("v3-prove", 3, "The trial didn't ___ that the drug works.", "Исследование не доказало, что препарат работает.",
      ["prove", "proof"], "prove", "Доказать — prove."),
    c("v3-belief", 3, "It's a common ___ that antibiotics help with colds.", "Многие считают, что антибиотики помогают при простуде.",
      ["belief", "believe"], "belief", "Убеждение, мнение — belief: существительное."),
    c("v3-halve", 3, "We decided to ___ the dose.", "Мы решили уменьшить дозу вдвое.",
      ["halve", "half"], "halve", "Уменьшить вдвое — halve /hɑːv/: глагол. Половина — half /hɑːf/."),

    # 4 · loss, choice, success
    c("v4-loss", 4, "He has some hearing ___ in his left ear.", "Слух на левое ухо у него снижен.",
      ["loss", "lose", "lost"], "loss", "Потеря — loss: hearing loss, weight loss."),
    c("v4-lose", 4, "Try to ___ some weight.", "Постарайтесь немного похудеть.",
      ["lose", "loss", "loose"], "lose", "Терять — lose /luːz/. loose /luːs/ — свободный, неплотный."),
    c("v4-choice", 4, "It's your ___.", "Решать вам.",
      ["choice", "choose"], "choice", "Выбор — choice."),
    c("v4-choose", 4, "You can ___ between two treatments.", "Вы можете выбрать один из двух методов лечения.",
      ["choose", "choice"], "choose", "Выбирать — choose."),
    c("v4-success", 4, "The operation was a ___.", "Операция прошла успешно.",
      ["success", "succeed", "successful"], "success", "Успех — success. succeed — добиться успеха, successful — успешный."),
    c("v4-complaint", 4, "We received a ___ about the waiting time.", "Мы получили жалобу на время ожидания.",
      ["complaint", "complain"], "complaint", "Жалоба — complaint, жаловаться — complain."),

    # 5 · use [s] и use [z]
    c("v5-use-n", 5, "What's the use of worrying? Here use ends in ___.", "Какой смысл волноваться? Как здесь звучит use?",
      ["[s]", "[z]"], "[s]", "Существительное use /juːs/ — польза, смысл — с [s].", say="What's the use of worrying?"),
    c("v5-use-v", 5, "How do I use this inhaler? Here use ends in ___.", "Как пользоваться этим ингалятором? Как здесь звучит use?",
      ["[z]", "[s]"], "[z]", "Глагол use /juːz/ — пользоваться — с [z].", say="How do I use this inhaler?"),
    c("v5-close-adj", 5, "She lives close to the hospital. Here close ends in ___.", "Она живёт рядом с больницей. Как здесь звучит close?",
      ["[s]", "[z]"], "[s]", "Прилагательное и наречие close /kləʊs/ — близкий, рядом — с [s].", say="She lives close to the hospital."),
    c("v5-close-v", 5, "Please close the door. Here close ends in ___.", "Закройте дверь, пожалуйста. Как здесь звучит close?",
      ["[z]", "[s]"], "[z]", "Глагол close /kləʊz/ — закрывать — с [z].", say="Please close the door."),
    c("v5-excuse", 5, "That's no excuse for being late. Here excuse ends in ___.", "Это не оправдание опозданию. Как здесь звучит excuse?",
      ["[s]", "[z]"], "[s]", "Существительное excuse /ɪkˈskjuːs/ — оправдание — с [s]. Глагол excuse me — с [z].", say="That's no excuse for being late."),
    c("v5-house", 5, "We house stroke patients in the new wing. Here house ends in ___.", "Пациентов с инсультом мы размещаем в новом крыле. Как здесь звучит house?",
      ["[z]", "[s]"], "[z]", "Глагол house /haʊz/ — размещать — с [z]. Существительное house /haʊs/ — дом — с [s].", say="We house stroke patients in the new wing."),

    # 6 · treat или treatment
    c("v6-treatment", 6, "The ___ was effective.", "Лечение оказалось эффективным.",
      ["treatment", "treat", "treating"], "treatment", "После the и в роли подлежащего — существительное: treatment."),
    c("v6-improvement", 6, "There's been a slight ___ in his speech.", "Речь у него немного улучшилась.",
      ["improvement", "improve", "improving"], "improvement", "После a slight — существительное: improvement."),
    c("v6-admission", 6, "On ___, his blood pressure was 190/100.", "При поступлении давление было 190/100.",
      ["admission", "admit", "admittance"], "admission", "При поступлении — on admission. admit — госпитализировать; admittance — допуск, вход (No admittance)."),
    c("v6-recovery", 6, "He made a full ___.", "Он полностью поправился.",
      ["recovery", "recover", "recovering"], "recovery", "Выздоровление — recovery: make a full recovery."),
    c("v6-prescription", 6, "You'll need a ___ for this drug.", "На этот препарат нужен рецепт.",
      ["prescription", "prescribe", "prescript"], "prescription", "Рецепт — prescription, выписать — prescribe."),
    c("v6-decision", 6, "We need to make a ___ today.", "Решение нужно принять сегодня.",
      ["decision", "decide", "decisive"], "decision", "Решение — decision: make a decision. decisive — решительный."),

    # 7 · ударение
    c("v7-record-n", 7, "Keep a ___ of your blood pressure.", "Записывайте давление — ведите дневник.",
      ["REcord", "reCORD"], "REcord", "Существительное — ударение на первый слог: a REcord /ˈrekɔːd/.",
      say="Keep a record of your blood pressure."),
    c("v7-record-v", 7, "We need to ___ his weight every day.", "Его вес нужно записывать каждый день.",
      ["reCORD", "REcord"], "reCORD", "Глагол — ударение на второй слог: to reCORD /rɪˈkɔːd/.",
      say="We need to record his weight every day."),
    c("v7-increase", 7, "There's been an ___ in cases.", "Случаев стало больше.",
      ["INcrease", "inCREASE"], "INcrease", "Существительное — an INcrease /ˈɪŋkriːs/.",
      say="There's been an increase in cases."),
    c("v7-progress", 7, "The disease can ___ quickly.", "Болезнь может быстро прогрессировать.",
      ["proGRESS", "PROgress"], "proGRESS", "Глагол — to proGRESS /prəˈɡres/. Существительное — PROgress /ˈprəʊɡres/.",
      say="The disease can progress quickly."),
    c("v7-present", 7, "I'm going to ___ the case at the meeting.", "Я буду докладывать этот случай на совещании.",
      ["preSENT", "PREsent"], "preSENT", "Глагол — to preSENT /prɪˈzent/: представить, доложить. Существительное — a PREsent: подарок.",
      say="I'm going to present the case at the meeting."),
    c("v7-object", 7, "Does anyone ___ to this plan?", "Кто-нибудь возражает против этого плана?",
      ["obJECT", "OBject"], "obJECT", "Глагол — to obJECT /əbˈdʒekt/: возражать. Существительное — an OBject: предмет.",
      say="Does anyone object to this plan?"),

    # 8 · died, dead, death, born
    c("v8-died", 8, "Her father ___ last year.", "Её отец умер в прошлом году.",
      ["died", "dead", "death"], "died", "Умер — died: прошедшее от die."),
    c("v8-dead", 8, "The patient was ___ on arrival.", "Пациент поступил уже мёртвым.",
      ["dead", "died", "death"], "dead", "Мёртвый — dead: прилагательное. Was died — ошибка."),
    c("v8-death", 8, "The cause of ___ was a stroke.", "Причина смерти — инсульт.",
      ["death", "dead", "died"], "death", "Смерть — death: существительное."),
    c("v8-born", 8, "I was ___ in Yekaterinburg.", "Я родился в Екатеринбурге.",
      ["born", "birth", "bear"], "born", "Родиться — be born: I was born."),
    c("v8-birth", 8, "What's your date of ___?", "Какая у вас дата рождения?",
      ["birth", "born", "birthday"], "birth", "Рождение — birth: date of birth. Birthday — день рождения, праздник: date of birthday — ошибка."),
    c("v8-dying", 8, "He's ___ — the family should come now.", "Он умирает — родным надо приехать сейчас.",
      ["dying", "dieing", "death"], "dying", "Умирает — is dying: ie перед -ing меняется на y."),
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
