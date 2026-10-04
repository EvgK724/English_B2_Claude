# Содержание приложения «Который»: who, which, that, whose, where, when; запятые;
# когда «который» опускают; предлог в конце; what и which «что»; сокращённые придаточные в статьях.
# Пометка […] — слово в фокусе (оранжевый).

MIXED_TOPIC = 9

GROUPS = {
    "who": "Кто, что, чей",
    "comma": "Запятая",
    "drop": "Опустить который · предлог в конце",
    "what": "То, что",
    "papers": "В статьях",
    "mix": "Итог",
}

# Кто или что: слово | когда | пример | перевод примера
WORDS = [
    ["who", "о людях", "the nurse who called", "медсестра, которая звонила"],
    ["which", "о вещах", "the scan which showed a bleed", "снимок, который показал кровоизлияние"],
    ["that", "о людях и вещах, без запятых", "the test that we ordered", "анализ, который мы назначили"],
    ["whose", "чей, у которого", "a man whose wife called", "мужчина, чья жена звонила"],
    ["where", "где, в котором", "the unit where I work", "отделение, где я работаю"],
    ["when", "когда", "the day when it happened", "день, когда это случилось"],
]

# Одна фраза — разный смысл: строки [английский, перевод или пояснение]
CONTRAST = [
    [["Patients [who had AF] received apixaban.", "без запятых: апиксабан получили только пациенты с ФП"],
     ["The patients, [who had AF], received apixaban.", "с запятыми: ФП была у всех пациентов"]],
    [["My brother [who lives in Moscow] is a surgeon.", "братьев несколько — речь о том, что в Москве"],
     ["My brother, [who lives in Moscow], is a surgeon.", "брат один, и он живёт в Москве"]],
    [["He refused surgery, [which] surprised us.", "что нас удивило: which — обо всём предложении"],
     ["[What] surprised us was his refusal.", "то, что нас удивило: what"]],
    [["The nurse [I asked] didn't know.", "who опущено: я спросил медсестру"],
     ["The nurse [who answered] didn't know.", "who нужно: медсестра ответила"]],
    [["This is the unit [where] I work.", "где: дальше своё подлежащее — I"],
     ["This is the unit [which] has 30 beds.", "в котором 30 коек: which само подлежащее"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["the patient which was admitted", "the patient who was admitted", "о людях — who"],
    ["My father, that is 80, …", "My father, who is 80, …", "после запятой that не ставят"],
    ["the drug which we prescribed it", "the drug which we prescribed", "it лишнее: which уже его заменяет"],
    ["He refused, what surprised us.", "He refused, which surprised us.", "«что» обо всём предложении — which"],
    ["everything what he said", "everything that he said", "после everything и all — that"],
    ["a patient who's father…", "a patient whose father…", "чей — whose; who's = who is"],
    ["a hospital where has an MRI", "a hospital which has an MRI", "where — только со своим подлежащим"],
    ["Patients, who smoke, have…", "Patients who smoke have…", "уточняем, какие пациенты, — без запятых"],
    ["120 patients, most of them were men", "120 patients, most of whom were men", "из которых — most of whom"],
    ["the reason because he came", "the reason why he came", "причина, по которой — the reason why"],
]

TOPICS = [
    {"n": 1, "group": "who", "title": "who, which, that", "sub": "который: о людях и о вещах",
     "rule": "О людях — who, о вещах — which: the nurse who called, the scan which showed a bleed. That подходит и для людей, и для вещей, но только без запятых; в речи без запятых that даже чаще. Which о людях — ошибка: the patient which… И «который» — никогда не what.",
     "ex": [
         {"en": "The nurse [who] took the blood sample has gone home.", "ru": "Медсестра, которая брала кровь, ушла домой."},
         {"en": "The ward [which] was closed last year has reopened.", "ru": "Отделение, которое закрыли в прошлом году, снова открылось."},
         {"en": "She's a doctor [that] everyone trusts.", "ru": "Она врач, которому все доверяют."},
     ]},
    {"n": 2, "group": "who", "title": "whose, where, when", "sub": "чей, где, когда, почему",
     "rule": "Чей, у которого — whose + существительное: a patient whose son is a surgeon. Whose бывает и о вещах: a drug whose effect lasts 24 hours. Где, в котором — where, если дальше своё подлежащее: the unit where I work. Своего подлежащего нет — which: the unit which has 30 beds. Когда — when: the day when we met. Причина, по которой — the reason why. Who's = who is, это не «чей».",
     "ex": [
         {"en": "We need a nurse [whose] English is good.", "ru": "Нам нужна медсестра, которая хорошо знает английский."},
         {"en": "This is the ward [where] I did my residency.", "ru": "Это отделение, где я проходил ординатуру."},
         {"en": "I remember the day [when] he was admitted.", "ru": "Я помню день, когда его госпитализировали."},
     ]},
    {"n": 3, "group": "comma", "title": "Запятая или нет", "sub": "уточняет или добавляет",
     "rule": "Без запятых придаточное уточняет, о ком речь: Patients who arrive within 4.5 hours can receive thrombolysis — только они. С запятыми — добавляет сведения о том, кто и так понятен: My grandfather, who is 90, still reads. Проверка: убери придаточное. Всё ещё понятно, о ком речь, — ставь запятые. В статье запятые меняют смысл: The patients, who had AF, … — ФП была у всех.",
     "ex": [
         {"en": "Patients [who arrive within 4.5 hours] can receive thrombolysis.", "ru": "Пациентам, поступившим в первые 4,5 часа, можно провести тромболизис."},
         {"en": "Aspirin, [which is cheap], is still widely used.", "ru": "Аспирин, который стоит недорого, по-прежнему широко применяется."},
         {"en": "My grandfather, [who is 90], still reads without glasses.", "ru": "Мой дедушка, которому 90, до сих пор читает без очков."},
     ]},
    {"n": 4, "group": "comma", "title": "После запятой", "sub": "who, which — не that; which = «что»",
     "rule": "В придаточном с запятыми — только who (о людях) или which (о вещах). That после запятой не ставят. Which после запятой бывает и обо всём предложении — «что»: He stopped smoking, which was great news. Здесь не what и не that.",
     "ex": [
         {"en": "My sister, [who] lives in Kazan, visits us every summer.", "ru": "Моя сестра, которая живёт в Казани, приезжает к нам каждое лето."},
         {"en": "The new scanner, [which] arrived in May, is much faster.", "ru": "Новый томограф, который привезли в мае, работает гораздо быстрее."},
         {"en": "He stopped smoking, [which] was great news.", "ru": "Он бросил курить, что стало отличной новостью."},
     ]},
    {"n": 5, "group": "drop", "title": "Когда «который» опускают", "sub": "the drug we prescribed",
     "rule": "Если «который» — дополнение, его можно опустить: the advice (that) you gave me — ты дал совет. Если «который» — подлежащее, нельзя: the paramedic who brought him in — фельдшер привёз. Проверка: сразу после «который» стоит своё подлежащее (you, we, the doctor) — можно опустить. Опускают только без запятых. И не повторяй местоимение: the drug which we prescribed, не prescribed it.",
     "ex": [
         {"en": "The advice [you gave me] really helped.", "ru": "Совет, который ты мне дал, очень помог."},
         {"en": "The paramedic [who brought him in] noticed the facial droop.", "ru": "Фельдшер, который его привёз, заметил асимметрию лица."},
         {"en": "The man [she married] is a surgeon.", "ru": "Мужчина, за которого она вышла замуж, — хирург."},
     ]},
    {"n": 6, "group": "drop", "title": "Предлог в конце", "sub": "the doctor I spoke to",
     "rule": "Русское «с которым, о котором, в котором» по‑английски обычно строится с предлогом в конце: the colleague I work with, the patient you were worried about. Книжный вариант — предлог впереди, и тогда только whom или which: the consultant to whom I spoke, the method by which… После предлога who и that не ставят.",
     "ex": [
         {"en": "That's the colleague I work [with].", "ru": "Это коллега, с которым я работаю."},
         {"en": "Who's the patient you were worried [about]?", "ru": "Кто тот пациент, о котором ты беспокоился?"},
         {"en": "The method [by which] the samples were collected is described below.", "ru": "Способ, которым собирали образцы, описан ниже."},
     ]},
    {"n": 7, "group": "what", "title": "what, that, which", "sub": "то, что · всё, что",
     "rule": "То, что — what: What he needs is rest. I don't understand what you mean. После everything, all, nothing, something и превосходной степени — that или ничего: everything (that) he said, the best treatment (that) we have. Не everything what. «Что» обо всём предложении после запятой — which: He stopped his tablets, which was a mistake.",
     "ex": [
         {"en": "[What] he needs now is rest.", "ru": "Что ему сейчас нужно, так это покой."},
         {"en": "I agree with everything [that] you said.", "ru": "Я согласен со всем, что ты сказал."},
         {"en": "He stopped taking his tablets, [which] was a mistake.", "ru": "Он перестал пить таблетки, что было ошибкой."},
     ]},
    {"n": 8, "group": "papers", "title": "В статьях", "sub": "treated, taking, most of whom",
     "rule": "В методах и результатах придаточные сокращают. Которых лечили — -ed: patients treated with thrombectomy = who were treated. Которые принимают — -ing: patients taking warfarin = who were taking. Из которых — most of whom (о людях), 40 of which (о вещах): We enrolled 85 patients, most of whom were over 70. Most of them после запятой — ошибка. Most of whom — сверх уровня, но в статьях встречается постоянно.",
     "ex": [
         {"en": "Patients [treated] with thrombectomy were analysed separately.", "ru": "Пациентов, которым провели тромбэктомию, анализировали отдельно."},
         {"en": "Patients [taking] warfarin were excluded.", "ru": "Пациентов, принимающих варфарин, исключали."},
         {"en": "We enrolled 85 patients, [most of whom] were over 70.", "ru": "Мы включили 85 пациентов, большинство из которых были старше 70 лет."},
     ]},
    {"n": 9, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · who, which, that
    c("w1-doctor", 1, "The doctor ___ examined him was very thorough.", "Врач, который его осматривал, был очень внимательным.",
      ["who", "which", "what"], "who", "О человеке — who."),
    c("w1-article", 1, "Did you read the article ___ I sent you?", "Ты прочитал статью, которую я тебе отправил?",
      ["which", "who", "what"], "which", "О вещи — which (или that)."),
    c("w1-drug", 1, "It's a drug ___ lowers blood pressure quickly.", "Это препарат, который быстро снижает давление.",
      ["that", "who", "what"], "that", "О вещи без запятых — that или which."),
    c("w1-only", 1, "She's the only neurologist ___ works on Sundays.", "Она единственный невролог, который работает по воскресеньям.",
      ["that", "which", "what"], "that", "О человеке без запятых — who или that; which — только о вещах."),
    c("w1-patients", 1, "The patients ___ took part in the study were all over 60.", "Всем пациентам, которые участвовали в исследовании, было больше 60.",
      ["who", "which", "whose"], "who", "О людях — who, не which."),
    c("w1-tablets", 1, "The tablets ___ you gave me made me feel sick.", "От таблеток, которые вы мне дали, меня тошнило.",
      ["which", "who", "whose"], "which", "О вещах — which, that или ничего."),

    # 2 · whose, where, when, why
    c("w2-son", 2, "This is the patient ___ son is a surgeon.", "Это пациент, сын которого — хирург.",
      ["whose", "who's", "who"], "whose", "Чей, у которого — whose + сущ. Who's = who is."),
    c("w2-effect", 2, "It's a drug ___ effect lasts 24 hours.", "Это препарат, действие которого длится 24 часа.",
      ["whose", "which", "who's"], "whose", "Whose бывает и о вещах: действие которого — whose effect."),
    c("w2-park", 2, "Do you know a place ___ we can park?", "Знаешь место, где можно припарковаться?",
      ["where", "which", "when"], "where", "Где — where: дальше своё подлежащее, we."),
    c("w2-met", 2, "Do you remember the day ___ we met?", "Помнишь день, когда мы познакомились?",
      ["when", "where", "which"], "when", "Когда — when."),
    c("w2-mri", 2, "We sent him to a hospital ___ has an MRI scanner.", "Мы направили его в больницу, где есть МРТ.",
      ["which", "where", "when"], "which", "Своего подлежащего нет — больница имеет: which. Where — только с подлежащим: where I work."),
    c("w2-results", 2, "We phoned the patients ___ results were abnormal.", "Мы обзвонили пациентов, у которых были отклонения в анализах.",
      ["whose", "who", "which"], "whose", "У которых результаты — whose results."),
    c("w2-reason", 2, "That's the reason ___ he was late.", "Вот причина, по которой он опоздал.",
      ["why", "because", "which"], "why", "Причина, по которой — the reason why."),

    # 3 · Запятая или нет
    c("w3-stroke", 3, "___ need a statin.", "Пациентам, перенёсшим инсульт, нужен статин.",
      ["Patients who had a stroke", "Patients, who had a stroke,", "Patients which had a stroke"], "Patients who had a stroke",
      "Уточняем, каким пациентам, — без запятых."),
    c("w3-mother", 3, "___ lives alone.", "Моя мама, которой 78, живёт одна.",
      ["My mother, who is 78,", "My mother who is 78", "My mother, that is 78,"], "My mother, who is 78,",
      "Мама одна — придаточное добавляет сведения: запятые и who."),
    c("w3-all", 3, "The relatives, who were worried, asked a lot of questions. ___ the relatives were worried.", "Родственники, которые волновались, задавали много вопросов. Волновались все?",
      ["all", "not all"], "all", "С запятыми придаточное добавляет сведения: волновались все."),
    c("w3-not-all", 3, "The relatives who were worried asked a lot of questions. ___ the relatives were worried.", "Родственники, которые волновались, задавали много вопросов. Волновались все?",
      ["not all", "all"], "not all", "Без запятых придаточное выделяет часть: спрашивали те, кто волновался."),
    c("w3-son", 3, "My son, who is a surgeon, lives in Moscow. I have ___ son.", "Мой сын, который работает хирургом, живёт в Москве. Сколько у меня сыновей?",
      ["only one", "more than one"], "only one", "С запятыми — сын один, придаточное просто добавляет сведения."),

    # 4 · После запятой
    c("w4-mri", 4, "The MRI, ___ was done on Monday, was normal.", "МРТ, которую сделали в понедельник, была в норме.",
      ["which", "that", "what"], "which", "После запятой — which, не that."),
    c("w4-petrov", 4, "Dr Petrov, ___ runs the stroke unit, is on holiday.", "Доктор Петров, который руководит отделением, в отпуске.",
      ["who", "that", "which"], "who", "После запятой о человеке — who."),
    c("w4-cancelled", 4, "The operation was cancelled, ___ upset the whole family.", "Операцию отменили, что расстроило всю семью.",
      ["which", "what", "that"], "which", "«Что» обо всём предложении — which."),
    c("w4-ambulance", 4, "The ambulance arrived in eight minutes, ___ was very quick.", "Скорая приехала за восемь минут, что было очень быстро.",
      ["which", "what", "that"], "which", "«Что» обо всём предложении — which, не what."),
    c("w4-apixaban", 4, "Apixaban, ___ is taken twice a day, doesn't need regular blood tests.", "Апиксабан, который принимают дважды в день, не требует регулярных анализов.",
      ["which", "that", "who"], "which", "После запятой о вещи — which."),
    c("w4-wife", 4, "The patient's wife, ___ is a nurse, noticed the symptoms first.", "Жена пациента, которая работает медсестрой, первой заметила симптомы.",
      ["who", "which", "that"], "who", "После запятой о человеке — who, не that."),

    # 5 · Когда «который» опускают
    c("w5-caused", 5, "The drug ___ caused the rash was stopped.", "Препарат, который вызвал сыпь, отменили.",
      ["that", "", "what"], "that", "Который — подлежащее (препарат вызвал): опускать нельзя."),
    c("w5-prescribed", 5, "The drug ___ we prescribed worked well.", "Препарат, который мы назначили, хорошо подействовал.",
      ["", "what", "who"], "", "Который — дополнение (мы назначили препарат): можно опустить. Можно и that."),
    c("w5-it", 5, "Is this the drug which you prescribed ___ yesterday?", "Это тот препарат, который вы вчера назначили?",
      ["", "it", "him"], "", "it не нужен: which уже заменяет препарат."),
    c("w5-saw", 5, "The patient ___ you saw yesterday has gone home.", "Пациент, которого ты видел вчера, уже дома.",
      ["", "what", "which"], "", "Который — дополнение (ты видел пациента): можно опустить. Можно и who или that."),
    c("w5-nurse", 5, "The nurse ___ looks after him is very experienced.", "Медсестра, которая за ним ухаживает, очень опытная.",
      ["who", "", "whose"], "who", "Который — подлежащее (медсестра ухаживает): опускать нельзя."),
    c("w5-wants", 5, "There's a man at reception ___ wants to see you.", "В регистратуре мужчина, который хочет вас видеть.",
      ["who", "", "what"], "who", "Который — подлежащее (мужчина хочет): опускать нельзя."),

    # 6 · Предлог в конце
    c("w6-for", 6, "Is this the book you were looking ___?", "Это та книга, которую ты искал?",
      ["for", "", "to"], "for", "Искать — look for: предлог остаётся в конце."),
    c("w6-to", 6, "The man I was talking ___ is my neighbour.", "Мужчина, с которым я разговаривал, — мой сосед.",
      ["to", "", "at"], "to", "Разговаривать с кем-то — talk to: предлог в конце."),
    c("w6-allergic", 6, "The drug he is allergic ___ is penicillin.", "Препарат, на который у него аллергия, — пенициллин.",
      ["to", "on", ""], "to", "Аллергия на — allergic to; предлог остаётся в конце."),
    c("w6-based", 6, "This is the trial on ___ the guidelines are based.", "Это исследование, на котором основаны рекомендации.",
      ["which", "that", "what"], "which", "После предлога — which, не that."),
    c("w6-whom", 6, "The consultant to ___ I spoke was very helpful.", "Консультант, с которым я говорил, очень помог.",
      ["whom", "who", "that"], "whom", "После предлога о человеке — whom."),
    c("w6-trained", 6, "The hospital in ___ I trained has closed.", "Больница, в которой я учился, закрылась.",
      ["which", "where", "that"], "which", "После предлога — which: in which = where."),

    # 7 · what, that, which
    c("w7-understand", 7, "I don't understand ___ you mean.", "Не понимаю, что ты имеешь в виду.",
      ["what", "that", "which"], "what", "То, что — what."),
    c("w7-everything", 7, "He told me everything ___ he knew.", "Он рассказал мне всё, что знал.",
      ["that", "what", "who"], "that", "После everything — that или ничего, не what."),
    c("w7-best", 7, "It's the best treatment ___ we have.", "Это лучшее лечение, какое у нас есть.",
      ["that", "what", "where"], "that", "После превосходной степени — that или ничего."),
    c("w7-weight", 7, "She lost ten kilos, ___ really helped her blood pressure.", "Она похудела на десять килограммов, что заметно помогло её давлению.",
      ["which", "what", "that"], "which", "«Что» обо всём предложении после запятой — which."),
    c("w7-worries", 7, "___ worries me is his speech.", "Что меня беспокоит, так это его речь.",
      ["what", "that", "which"], "what", "То, что — what."),
    c("w7-nothing", 7, "I'm afraid there's nothing ___ we can do.", "Боюсь, мы ничего не можем сделать.",
      ["", "what", "it"], "", "После nothing — ничего или that, не what."),

    # 8 · В статьях
    c("w8-treated", 8, "Patients ___ with alteplase had better outcomes.", "У пациентов, которых лечили алтеплазой, исходы были лучше.",
      ["treated", "treating", "who treated"], "treated", "Которых лечили — пассив: treated = who were treated."),
    c("w8-receiving", 8, "Patients ___ anticoagulants were excluded.", "Пациентов, получающих антикоагулянты, исключали.",
      ["receiving", "received", "who receiving"], "receiving", "Которые получают — -ing: receiving = who were receiving."),
    c("w8-living", 8, "Patients ___ alone had longer hospital stays.", "Пациенты, живущие одни, дольше лежали в больнице.",
      ["living", "lived", "who living"], "living", "Которые живут — -ing: living alone = who lived alone."),
    c("w8-admitted", 8, "All patients ___ to the unit in 2025 were included.", "Включили всех пациентов, госпитализированных в отделение в 2025 году.",
      ["admitted", "admitting", "who admitted"], "admitted", "Которых госпитализировали — пассив: admitted."),
    c("w8-whom", 8, "We enrolled 120 patients, most of ___ were men.", "Мы включили 120 пациентов, большинство из которых — мужчины.",
      ["whom", "them", "who"], "whom", "Большинство из которых (о людях) — most of whom. Most of them здесь — ошибка."),
    c("w8-which", 8, "We reviewed 300 CT scans, 40 of ___ showed a bleed.", "Мы проанализировали 300 КТ, в 40 из которых было кровоизлияние.",
      ["which", "them", "whom"], "which", "Из которых (о вещах) — of which."),
    c("w8-whose", 8, "Patients ___ symptoms resolved quickly did not receive thrombolysis.", "Пациенты, у которых симптомы быстро регрессировали, тромболизис не получали.",
      ["whose", "who", "which"], "whose", "У которых симптомы — whose symptoms."),
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
