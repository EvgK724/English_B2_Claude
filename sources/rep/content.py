# Содержание приложения «Пересказ»: косвенная речь — как передать слова пациента, родных и коллег.
# say / tell, сдвиг времён, слова времени, вопросы, просьбы и советы, complain of / deny / admit, язык истории болезни.
# Пометка […] — форма в фокусе (оранжевый).

MIXED_TOPIC = 8

GROUPS = {
    "basic": "Как пересказать",
    "verbs": "Глаголы пересказа",
    "clinic": "В истории болезни",
    "mix": "Итог",
}

# Сдвиг времён: было → стало | что с чем | пример | перевод
TABLE = [
    ["is → was", "настоящее → прошедшее", "“I feel dizzy.” → He said he felt dizzy.", "сказал, что кружится голова"],
    ["fell → had fallen", "прошедшее → past perfect", "“I fell.” → He said he had fallen.", "сказал, что упал"],
    ["have stopped → had stopped", "perfect → past perfect", "“I've stopped it.” → She said she had stopped it.", "сказала, что бросила"],
    ["will → would", "будущее", "“I'll call.” → She said she would call.", "сказала, что позвонит"],
    ["can → could", "могу", "“I can't move it.” → He said he couldn't move it.", "сказал, что не может"],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["He [said] he was tired.", "сказал — без «кому»"], ["He [told me] he was tired.", "сказал мне — tell + кому"]],
    [["“[Where is] the pain?”", "прямой вопрос"], ["I asked [where the pain was].", "косвенный — порядок как в утверждении"]],
    [["“[Do you smoke]?”", "прямой вопрос"], ["She asked [if I smoked].", "косвенный: if, без do"]],
    [["I [told him to stop] smoking.", "велел бросить"], ["I [told him not to drive].", "велел не садиться за руль"]],
    [["He [complained of] a headache.", "жаловался на головную боль"], ["He [denied] any headache.", "головную боль отрицал"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["He said me he was tired.", "He told me he was tired.", "кому — tell; say без «кому»"],
    ["She told that she felt dizzy.", "She said that she felt dizzy.", "tell без «кому» не бывает"],
    ["I asked where was the pain.", "I asked where the pain was.", "косвенный вопрос — прямой порядок"],
    ["She asked did I smoke.", "She asked if I smoked.", "«ли» — if или whether"],
    ["I said him to stop smoking.", "I told him to stop smoking.", "просьба, совет — tell + кому + to"],
    ["I told him don't drive.", "I told him not to drive.", "запрет — not to"],
    ["He complained on headache.", "He complained of a headache.", "complain of"],
    ["She denied to have chest pain.", "She denied having chest pain.", "deny + -ing или сущ."],
    ["He explained me the plan.", "He explained the plan to me.", "explain something to someone"],
    ["She suggested me to rest.", "She suggested that I rest.", "suggest — без «кому + to»"],
]

TOPICS = [
    {"n": 1, "group": "basic", "title": "say или tell", "sub": "сказал · сказал кому",
     "rule": "say — сказать что-то: He said (that) he was tired. Если нужно «кому» — say to someone: He said to me… tell — всегда с тем, кому, и без to: He told me (that)… She told the nurse… Без «кому» tell не бывает: She told that — ошибка; say me — тоже. Устойчивые сочетания: tell the truth, tell a lie; say sorry, say hello.",
     "ex": [
         {"en": "He [said] he was tired.", "ru": "Он сказал, что устал."},
         {"en": "He [told me] he was tired.", "ru": "Он сказал мне, что устал."},
         {"en": "She [told the nurse] she felt sick.", "ru": "Она сказала медсестре, что её тошнит."},
     ]},
    {"n": 2, "group": "basic", "title": "Сдвиг времён", "sub": "is → was, will → would, can → could",
     "rule": "Пересказываешь в прошедшем (he said) — время обычно сдвигается на шаг назад: am, is → was; feel → felt; fell → had fallen; have stopped → had stopped; will → would; can → could. «I feel dizzy» → He said he felt dizzy. «I'll call back» → She said she would call back. Если сказанное верно и сейчас, сдвиг можно не делать: He said he lives alone.",
     "ex": [
         {"en": "He said he [felt] dizzy.", "ru": "Он сказал, что у него кружится голова."},
         {"en": "He said he [had fallen] in the bathroom.", "ru": "Он сказал, что упал в ванной."},
         {"en": "She said she [would] call back.", "ru": "Она сказала, что перезвонит."},
     ]},
    {"n": 3, "group": "basic", "title": "Время и место", "sub": "yesterday → the day before",
     "rule": "Пересказываешь позже — меняются и слова времени и места: now → then; today → that day; yesterday → the day before; tomorrow → the next day; ago → earlier или before; here → there; this → that. «I fell yesterday» → He said he had fallen the day before.",
     "ex": [
         {"en": "He said he had fallen [the day before].", "ru": "Он сказал, что упал накануне."},
         {"en": "She said she would come back [the next day].", "ru": "Она сказала, что вернётся на следующий день."},
         {"en": "He said the pain had started two hours [earlier].", "ru": "Он сказал, что боль началась двумя часами раньше."},
     ]},
    {"n": 4, "group": "basic", "title": "Вопросы в пересказе", "sub": "asked if… · asked where…",
     "rule": "Вопрос пересказывают через ask. Порядок как в утверждении — без do, did и без вопросительного знака: I asked where the pain was; She asked when it had started. Вопрос «да или нет» — через if или whether: She asked if I smoked. Время сдвигается так же, как в словах.",
     "ex": [
         {"en": "I asked [where the pain was].", "ru": "Я спросил, где болит."},
         {"en": "She asked [if] I smoked.", "ru": "Она спросила, курю ли я."},
         {"en": "He asked [when it had started].", "ru": "Он спросил, когда это началось."},
     ]},
    {"n": 5, "group": "verbs", "title": "Просьбы и советы", "sub": "told him to… · asked her not to…",
     "rule": "Просьбу, приказ или совет пересказывают так: tell, ask, advise, warn + кому + to + глагол: I told him to stop smoking. The nurse asked her to lie down. We advised him to rest. Запрет — not to: I told him not to drive. Say здесь не подходит: I said him to stop — ошибка. suggest — особый: She suggested getting a second opinion, но не suggested me to.",
     "ex": [
         {"en": "I [told him to stop] smoking.", "ru": "Я сказал ему бросить курить."},
         {"en": "The nurse [asked her not to] eat.", "ru": "Медсестра попросила её не есть."},
         {"en": "We [advised him to] rest.", "ru": "Мы посоветовали ему отдыхать."},
     ]},
    {"n": 6, "group": "verbs", "title": "Жаловался, отрицал, признал", "sub": "complain of, deny, admit, report",
     "rule": "Глаголы для истории болезни: complain of — жаловаться на: He complained of chest pain. deny + сущ. или -ing — отрицать: She denied any headache; She denied smoking. admit + -ing — признать: He admitted drinking heavily. report — сообщать: She reported numbness. mention — упомянуть. refuse to — отказаться: He refused to take the tablets. explain something to someone — объяснить кому-то, не explain me.",
     "ex": [
         {"en": "He [complained of] chest pain.", "ru": "Он жаловался на боль в груди."},
         {"en": "She [denied smoking].", "ru": "Курение она отрицала."},
         {"en": "He [admitted drinking] heavily.", "ru": "Он признал, что много пьёт."},
     ]},
    {"n": 7, "group": "clinic", "title": "В истории болезни", "sub": "со слов пациента и родных",
     "rule": "Как передать анамнез: The patient reported… He complained of… She denied… He stated that… «Со слов жены» — according to his wife: According to his wife, he had been confused since the morning. «Как сообщил сосед» — the neighbour told us that… Вопросы родным: We asked whether he had hit his head.",
     "ex": [
         {"en": "[According to] his wife, he had been confused since the morning.", "ru": "Со слов жены, он спутан с утра."},
         {"en": "The patient [stated that] he had stopped his tablets.", "ru": "Пациент сообщил, что прекратил приём таблеток."},
         {"en": "We asked [whether] he had hit his head.", "ru": "Мы спросили, не ударялся ли он головой."},
     ]},
    {"n": 8, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · say или tell
    c("r1-said", 1, "The patient ___ he had a headache.", "Пациент сказал, что у него болит голова.",
      ["said", "told", "spoke"], "said", "Без «кому» — said."),
    c("r1-told", 1, "She ___ me she had stopped taking her tablets.", "Она сказала мне, что перестала принимать таблетки.",
      ["told", "said", "spoke"], "told", "Сказала мне — told me."),
    c("r1-said-to", 1, "He said ___ me that he felt better.", "Он сказал мне, что ему лучше.",
      ["to", "for", "at"], "to", "say to someone — с to; tell someone — без to."),
    c("r1-tell", 1, "Please ___ the nurse if the pain gets worse.", "Скажите медсестре, если боль усилится.",
      ["tell", "say", "speak"], "tell", "Сказать кому — tell."),
    c("r1-truth", 1, "I'm not sure he's telling the ___.", "Не уверен, что он говорит правду.",
      ["truth", "true", "right"], "truth", "Говорить правду — tell the truth."),
    c("r1-sorry", 1, "He didn't even ___ sorry.", "Он даже не извинился.",
      ["say", "tell", "speak"], "say", "say sorry, say hello."),
    c("r1-us", 1, "His wife told ___ that he had been confused since the morning.", "Жена сказала нам, что он спутан с утра.",
      ["us", "to us", ""], "us", "tell + кому, без to: told us."),

    # 2 · Сдвиг времён
    c("r2-felt", 2, "Yesterday he told me he ___ dizzy, but today he's fine.", "Вчера он говорил, что у него кружится голова, а сегодня всё в порядке.",
      ["felt", "feels", "is feeling"], "felt", "Пересказ в прошедшем: feel → felt."),
    c("r2-fallen", 2, "He said he ___ in the bathroom the night before.", "Он сказал, что накануне вечером упал в ванной.",
      ["had fallen", "has fallen", "falls"], "had fallen", "Прошедшее → past perfect: had fallen."),
    c("r2-would", 2, "She said she ___ call back after lunch, but she never did.", "Она сказала, что перезвонит после обеда, но так и не перезвонила.",
      ["would", "will", "shall"], "would", "will → would."),
    c("r2-could", 2, "Last week he said he ___ walk without help, but now he needs a frame.", "На прошлой неделе он говорил, что может ходить без помощи, а теперь ему нужны ходунки.",
      ["could", "can", "is able"], "could", "can → could."),
    c("r2-stopped", 2, "She told me she ___ taking warfarin a week before.", "Она сказала, что за неделю до этого перестала принимать варфарин.",
      ["had stopped", "has stopped", "stops"], "had stopped", "Раньше другого прошлого — had stopped."),
    c("r2-was", 2, "The patient said the pain ___ worse at night.", "Пациент сказал, что ночью боль сильнее.",
      ["was", "were", "been"], "was", "is → was."),
    c("r2-had-had", 2, "He said he ___ a similar episode two years earlier.", "Он сказал, что двумя годами раньше у него был похожий эпизод.",
      ["had had", "has had", "have had"], "had had", "had → had had."),
    c("r2-going", 2, "In May she said she ___ going to stop smoking, but she still smokes.", "В мае она говорила, что собирается бросить курить, но до сих пор курит.",
      ["was", "is", "were"], "was", "is going to → was going to."),

    # 3 · Время и место
    c("r3-daybefore", 3, "On Monday he told me he had fallen ___ — on Sunday.", "В понедельник он сказал мне, что упал накануне — в воскресенье.",
      ["the day before", "yesterday", "tomorrow"], "the day before", "yesterday → the day before."),
    c("r3-nextday", 3, "She said she would come back ___, but she came a week later.", "Она сказала, что вернётся на следующий день, но пришла через неделю.",
      ["the next day", "tomorrow", "yesterday"], "the next day", "tomorrow → the next day."),
    c("r3-earlier", 3, "He said the symptoms had started two hours ___.", "Он сказал, что симптомы начались двумя часами раньше.",
      ["earlier", "ago", "after"], "earlier", "ago → earlier или before.",
      {"ago": "в разговоре так скажут, но в истории болезни — earlier"}),
    c("r3-thatday", 3, "Last Friday she said she hadn't eaten anything ___.", "В прошлую пятницу она сказала, что за день ничего не ела.",
      ["that day", "today", "this day"], "that day", "today → that day."),

    # 4 · Вопросы в пересказе
    c("r4-where", 4, "I asked him where the pain ___.", "Я спросил его, где болит.",
      ["was", "did", "is it"], "was", "Косвенный вопрос — прямой порядок: where the pain was."),
    c("r4-if", 4, "The nurse asked ___ he was allergic to anything.", "Медсестра спросила, нет ли у него на что-нибудь аллергии.",
      ["if", "that", "does"], "if", "«Ли» — if или whether."),
    c("r4-order", 4, "She asked me when ___.", "Она спросила меня, когда это началось.",
      ["it had started", "had it started", "did it start"], "it had started", "Прямой порядок, без did: when it had started."),
    c("r4-whether", 4, "The doctor asked ___ I had ever had a stroke.", "Врач спросил, был ли у меня когда-нибудь инсульт.",
      ["whether", "that", "have"], "whether", "«Ли» — whether или if."),
    c("r4-smoked", 4, "She asked if I ___.", "Она спросила, курю ли я.",
      ["smoked", "did smoke", "do I smoke"], "smoked", "Без do, с прямым порядком: if I smoked."),
    c("r4-how-long", 4, "He asked how long I ___ the headache.", "Он спросил, как давно у меня эта головная боль.",
      ["had had", "had I had", "did I have"], "had had", "Прямой порядок: how long I had had."),
    c("r4-what", 4, "The paramedic asked what ___.", "Фельдшер спросил, что случилось.",
      ["had happened", "did happen", "happened it"], "had happened", "what had happened — без did."),

    # 5 · Просьбы и советы
    c("r5-to", 5, "I told him ___ smoking.", "Я сказал ему бросить курить.",
      ["to stop", "stop", "stopping"], "to stop", "tell + кому + to: told him to stop."),
    c("r5-not-to", 5, "The nurse asked her ___ eat anything before the scan.", "Медсестра попросила её ничего не есть перед обследованием.",
      ["not to", "don't", "no"], "not to", "Запрет — not to."),
    c("r5-advised", 5, "We ___ him to rest for a week.", "Мы посоветовали ему неделю отдыхать.",
      ["advised", "said", "suggested"], "advised", "Посоветовать кому — advise someone to."),
    c("r5-drive", 5, "The doctor told me ___ drive for a month.", "Врач велел мне месяц не садиться за руль.",
      ["not to", "don't", "not"], "not to", "Запрет — told me not to."),
    c("r5-suggest", 5, "She suggested ___ a second opinion.", "Она предложила получить второе мнение.",
      ["getting", "to get", "me to get"], "getting", "suggest + -ing или that…; suggest me to — ошибка."),
    c("r5-asked", 5, "He ___ me to call his daughter.", "Он попросил меня позвонить его дочери.",
      ["asked", "said", "suggested"], "asked", "Попросить кого-то — ask someone to."),
    c("r5-warned", 5, "We warned him ___ stop the tablets suddenly.", "Мы предупредили его, чтобы он не бросал таблетки резко.",
      ["not to", "don't", "no"], "not to", "warn someone not to."),

    # 6 · Жаловался, отрицал, признал
    c("r6-complain", 6, "He complained ___ chest pain and shortness of breath.", "Он жаловался на боль в груди и одышку.",
      ["of", "on", "about"], "of", "Жалобы на симптомы — complain of.",
      {"about": "в истории болезни пишут of"}),
    c("r6-denied", 6, "She denied ___ any headache.", "Головную боль она отрицала.",
      ["having", "to have", "that have"], "having", "deny + -ing: denied having."),
    c("r6-any", 6, "He denied ___ loss of consciousness.", "Потерю сознания он отрицал.",
      ["any", "to", "of"], "any", "deny + сущ.: denied any loss of consciousness."),
    c("r6-admitted", 6, "He admitted ___ a bottle of vodka a day.", "Он признал, что выпивает бутылку водки в день.",
      ["drinking", "to drink", "drink"], "drinking", "admit + -ing."),
    c("r6-reported", 6, "She ___ numbness in her left hand.", "Она сообщила об онемении в левой руке.",
      ["reported", "said", "told"], "reported", "Сообщить о симптоме — report."),
    c("r6-mentioned", 6, "His son ___ that he had fallen twice last month.", "Сын упомянул, что в прошлом месяце он дважды падал.",
      ["mentioned", "told", "spoke"], "mentioned", "Упомянуть — mention that…"),
    c("r6-explained", 6, "I explained the risks ___ him.", "Я объяснил ему риски.",
      ["to", "", "for"], "to", "explain something to someone."),
    c("r6-refused", 6, "He refused ___ the tablets.", "Он отказался принимать таблетки.",
      ["to take", "taking", "take"], "to take", "refuse to + глагол."),

    # 7 · В истории болезни
    c("r7-according", 7, "___ to his wife, he had been confused since the morning.", "Со слов жены, он спутан с утра.",
      ["according", "as", "said"], "according", "Со слов кого-то — according to."),
    c("r7-been", 7, "His daughter said he ___ confused since the morning.", "Дочь сказала, что он спутан с утра.",
      ["had been", "was being", "is"], "had been", "has been → had been."),
    c("r7-stated", 7, "The patient ___ that he had stopped taking his tablets.", "Пациент сообщил, что прекратил приём таблеток.",
      ["stated", "told", "spoke"], "stated", "Сообщил (официально) — stated that."),
    c("r7-us", 7, "The neighbour told ___ that she had found him on the floor.", "Соседка сказала нам, что нашла его на полу.",
      ["us", "to us", "for us"], "us", "tell + кому, без to."),
    c("r7-whether", 7, "We asked ___ he had hit his head.", "Мы спросили, не ударялся ли он головой.",
      ["whether", "that", "did"], "whether", "«Ли» — whether или if."),
    c("r7-complained", 7, "On admission she complained ___ a severe headache.", "При поступлении жаловалась на сильную головную боль.",
      ["of", "on", "for"], "of", "complain of."),
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
