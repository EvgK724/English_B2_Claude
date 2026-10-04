# Содержание приложения «manage to и похожие»: удалось, не удалось, справляться, успеть, достичь, в итоге.
# Пометка […] — конструкция в фокусе (оранжевый).

MIXED_TOPIC = 8

GROUPS = {
    "succeed": "Удалось или нет",
    "cope": "Справляться",
    "more": "Успеть, достичь, в итоге",
    "med": "В больнице и в статьях",
    "mix": "Итог",
}

# Что с чем: глагол | конструкция | пример | перевод
TABLE = [
    ["manage", "to + глагол", "I managed to finish.", "удалось, с трудом"],
    ["succeed", "in + -ing", "We succeeded in reaching him.", "удалось — официально"],
    ["fail", "to + глагол", "The drug failed to work.", "не удалось, не сделал"],
    ["achieve", "+ сущ.", "achieve a goal", "достичь цели"],
    ["cope", "with + сущ.", "cope with stress", "справляться с трудностями"],
    ["deal", "with + сущ.", "deal with a problem", "заниматься, разбираться"],
    ["handle", "без предлога", "handle the situation", "справиться, управиться"],
    ["make it", "—", "We made it on time.", "успеть, добраться, выжить"],
    ["end up", "+ -ing", "We ended up staying.", "в итоге оказаться"],
    ["afford", "to + глагол", "We can't afford to wait.", "позволить себе"],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["I [managed to] finish it.", "удалось, с трудом"], ["We [succeeded in] finishing it.", "удалось — официально"], ["We [failed to] finish it.", "не удалось"]],
    [["Don't worry, I'll [manage].", "справлюсь"], ["I can't [cope with] all this stress.", "не справляюсь — тяжело"], ["I'll [deal with] it tomorrow.", "займусь этим завтра"]],
    [["She [handles] difficult patients well.", "справляется, ладит"], ["She [manages] the stroke unit.", "руководит отделением"]],
    [["We [made it] to the station on time.", "успели, добрались"], ["Sadly, he didn't [make it].", "не выжил"]],
    [["We [ended up] staying at home.", "в итоге остались"], ["It didn't [work out].", "не сложилось"], ["They [pulled it off].", "у них получилось — трудное дело"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["I managed finishing the report.", "I managed to finish the report.", "manage to + глагол"],
    ["We succeeded to reach him.", "We succeeded in reaching him.", "succeed in + -ing"],
    ["She achieved to pass the exam.", "She managed to pass the exam.", "achieve + существительное: achieve a goal"],
    ["We could catch the last train. (один раз)", "We managed to catch the last train.", "удалось один раз — managed to"],
    ["The drug failed working.", "The drug failed to work.", "fail to + глагол"],
    ["I can't cope stress.", "I can't cope with stress.", "cope with"],
    ["Can you handle with it?", "Can you handle it?", "handle — без with"],
    ["I'll deal it later.", "I'll deal with it later.", "deal with"],
    ["We ended up to stay at home.", "We ended up staying at home.", "end up + -ing"],
    ["I can't afford buying a car.", "I can't afford to buy a car.", "afford to + глагол"],
]

TOPICS = [
    {"n": 1, "group": "succeed", "title": "manage to — удалось", "sub": "и manage без to — справлюсь",
     "rule": "manage to + глагол — «удалось, сумел», обычно с трудом: I managed to finish the report on time. Не удалось — didn't manage to или couldn't. Об одной удаче в прошлом could не говорят: We managed to catch the last train. manage без to — «справиться, обойтись»: Don't worry, I'll manage. How do you manage without a car? И ещё manage — «руководить»: She manages the stroke unit.",
     "ex": [
         {"en": "I [managed to] finish the report on time.", "ru": "Мне удалось закончить отчёт вовремя."},
         {"en": "Don't worry — I'll [manage].", "ru": "Не волнуйся — я справлюсь."},
         {"en": "We [managed to] catch the last train.", "ru": "Мы успели на последний поезд."},
     ]},
    {"n": 2, "group": "succeed", "title": "succeed in, fail to", "sub": "официально: статьи, отчёты",
     "rule": "succeed in + -ing — «удалось», официально: The team succeeded in restoring blood flow. Succeed to — ошибка. fail to + глагол — «не удалось, не сделал», официально и в научных статьях: The drug failed to reduce mortality. The patient failed to attend follow-up. В разговоре — didn't manage to, couldn't.",
     "ex": [
         {"en": "The team [succeeded in] restoring blood flow.", "ru": "Команде удалось восстановить кровоток."},
         {"en": "The drug [failed to] reduce mortality.", "ru": "Препарат не снизил смертность."},
         {"en": "He [failed to] attend his follow-up.", "ru": "Он не пришёл на контрольный приём."},
     ]},
    {"n": 3, "group": "cope", "title": "cope with, deal with, handle", "sub": "справляться",
     "rule": "cope with — справляться с трудностями, стрессом, эмоциями: She's coping well with the diagnosis. How are you coping? deal with — заниматься, разбираться с задачей или проблемой: I'll deal with it tomorrow. handle — справиться с ситуацией, задачей, человеком, без предлога: Can you handle it? She handles difficult patients well.",
     "ex": [
         {"en": "She's [coping] well with the diagnosis.", "ru": "Она хорошо справляется с диагнозом."},
         {"en": "I'll [deal with] it tomorrow.", "ru": "Займусь этим завтра."},
         {"en": "Can you [handle] it on your own?", "ru": "Справишься с этим сам?"},
     ]},
    {"n": 4, "group": "more", "title": "make it — успеть, выжить", "sub": "добраться · прийти · выжить",
     "rule": "make it — «успеть, добраться, прийти»: We made it to the station just in time. Can you make it to the meeting? В медицине make it — «выжить», часто в отрицании: Sadly, he didn't make it.",
     "ex": [
         {"en": "We [made it] to the station just in time.", "ru": "Мы едва успели на вокзал."},
         {"en": "Can you [make it] to the meeting?", "ru": "Ты успеешь на совещание?"},
         {"en": "Sadly, he didn't [make it].", "ru": "К сожалению, он не выжил."},
     ]},
    {"n": 5, "group": "more", "title": "achieve, afford, get by", "sub": "достичь · позволить себе · обходиться",
     "rule": "achieve — достичь цели или результата, с существительным: achieve a goal, achieve good results. Achieve to do — ошибка; «удалось сделать» — managed to. afford — позволить себе (деньги, время, риск): I can't afford a new car. We can't afford to wait. get by — обходиться, сводить концы с концами: We get by on one salary. I can get by in German.",
     "ex": [
         {"en": "She [achieved] her goal.", "ru": "Она достигла своей цели."},
         {"en": "We can't [afford to] wait.", "ru": "Мы не можем позволить себе ждать."},
         {"en": "I can [get by] in German.", "ru": "По-немецки я объяснюсь."},
     ]},
    {"n": 6, "group": "more", "title": "end up, work out, pull off", "sub": "в итоге · сложилось · провернуть",
     "rule": "end up + -ing или + место — «в итоге оказаться»: We ended up staying at home. He ended up in hospital. work out — «получиться, сложиться»: I hope everything works out. It didn't work out. pull off — «провернуть, суметь сделать трудное» (разг.): Nobody believed in it, but they pulled it off.",
     "ex": [
         {"en": "We [ended up] staying at home.", "ru": "В итоге мы остались дома."},
         {"en": "I hope everything [works out].", "ru": "Надеюсь, всё сложится."},
         {"en": "They [pulled it off].", "ru": "У них получилось."},
     ]},
    {"n": 7, "group": "med", "title": "В больнице и в статьях", "sub": "failed to · achieved · coping",
     "rule": "В научных статьях: The intervention failed to reduce mortality. We succeeded in recruiting 500 patients. The trial achieved its primary endpoint. В клинике: We managed to restore blood flow. How are you coping? Sadly, he didn't make it.",
     "ex": [
         {"en": "The trial [achieved] its primary endpoint.", "ru": "Исследование достигло первичной конечной точки."},
         {"en": "We [managed to] restore blood flow.", "ru": "Нам удалось восстановить кровоток."},
         {"en": "How are you [coping]?", "ru": "Как вы справляетесь?"},
     ]},
    {"n": 8, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · manage
    c("n1-finish", 1, "It was hard, but I ___ finish the report on time.", "Было трудно, но мне удалось закончить отчёт вовремя.", ["managed to", "managed", "could"], "managed to",
      "Удалось один раз — managed to. Could — «умел вообще»."),
    c("n1-call", 1, "Did you manage ___ him?", "Тебе удалось ему дозвониться?", ["to call", "calling", "call"], "to call", "manage to + глагол."),
    c("n1-ill", 1, "Don't worry about me — I'll ___.", "Не беспокойся обо мне — я справлюсь.", ["manage", "manage to", "cope with"], "manage",
      "«Справлюсь» без дополнения — I'll manage."),
    c("n1-car", 1, "How do you ___ without a car?", "Как ты обходишься без машины?", ["manage", "succeed", "achieve"], "manage", "Обходиться — manage without."),
    c("n1-tickets", 1, "I tried, but I didn't ___ to get tickets.", "Я пытался, но билеты достать не удалось.", ["manage", "succeed", "achieve"], "manage",
      "Не удалось — didn't manage to."),
    c("n1-train", 1, "We ran and ___ to catch the last train.", "Мы бежали и успели на последний поезд.", ["managed", "could", "succeeded"], "managed",
      "Удалось один раз — managed to."),

    # 2 · succeed in, fail to
    c("n2-in", 2, "The team succeeded ___ restoring blood flow within an hour.", "Команде удалось восстановить кровоток в течение часа.", ["in", "to", "at"], "in",
      "succeed in + -ing."),
    c("n2-ing", 2, "They succeeded in ___ the patient's condition.", "Им удалось стабилизировать состояние пациента.", ["stabilising", "stabilise", "to stabilise"], "stabilising",
      "После succeed in — -ing."),
    c("n2-fail", 2, "The new drug failed ___ mortality.", "Новый препарат не снизил смертность.", ["to reduce", "reducing", "in reducing"], "to reduce", "fail to + глагол."),
    c("n2-attend", 2, "The patient failed ___ his follow-up appointment.", "Пациент не пришёл на контрольный приём.", ["to attend", "attending", "attend"], "to attend",
      "«Не сделал» (официально) — failed to."),
    c("n2-surgeons", 2, "Did the surgeons ___ in removing the whole tumour?", "Хирургам удалось удалить всю опухоль?", ["succeed", "manage", "achieve"], "succeed",
      "С in + -ing — только succeed."),

    # 3 · cope with, deal with, handle
    c("n3-stress", 3, "It's hard to ___ stress when you work night shifts.", "Трудно справляться со стрессом, когда работаешь по ночам.", ["cope with", "cope", "handle with"], "cope with",
      "Справляться с трудностями — cope with."),
    c("n3-request", 3, "I'm busy now — I'll ___ your request tomorrow.", "Сейчас я занят — займусь вашим запросом завтра.", ["deal with", "deal", "cope"], "deal with",
      "Заняться задачей — deal with."),
    c("n3-alone", 3, "Can you ___ this on your own?", "Справишься с этим сам?", ["handle", "handle with", "cope"], "handle", "handle — без предлога."),
    c("n3-coping", 3, "How are you ___ since the diagnosis?", "Как вы справляетесь с тех пор, как узнали диагноз?", ["coping", "dealing", "handling"], "coping",
      "«Как справляетесь?» — How are you coping?"),
    c("n3-patients", 3, "She ___ difficult patients very well.", "Она отлично ладит с трудными пациентами.", ["handles", "copes", "deals"], "handles",
      "Без предлога — handles. Copes и deals требуют with."),
    c("n3-complaints", 3, "Who ___ complaints in your hospital?", "Кто у вас в больнице разбирается с жалобами?", ["deals with", "copes with", "handles with"], "deals with",
      "Разбираться с задачей — deals with."),

    # 4 · make it
    c("n4-station", 4, "We ran and just ___ it to the station on time.", "Мы бежали и едва успели на вокзал.", ["made", "did", "managed"], "made", "Успеть, добраться — make it."),
    c("n4-meeting", 4, "Sorry, I can't ___ it to the meeting today.", "Извините, сегодня я не успею на совещание.", ["make", "do", "manage"], "make", "Успеть, прийти — make it."),
    c("n4-survive", 4, "We did everything we could, but sadly he didn't ___ it.", "Мы сделали всё возможное, но, к сожалению, он не выжил.", ["make", "do", "manage"], "make",
      "Выжить — make it."),
    c("n4-home", 4, "The road was closed, but we ___ it home before midnight.", "Дорогу перекрыли, но мы добрались домой до полуночи.", ["made", "did", "got"], "made",
      "Добраться — make it."),

    # 5 · achieve, afford, get by
    c("n5-goal", 5, "She finally ___ her goal of running a marathon.", "Она наконец достигла своей цели — пробежала марафон.", ["achieved", "managed", "succeeded"], "achieved",
      "Достичь цели — achieve a goal."),
    c("n5-exam", 5, "He ___ to pass the exam on his third attempt.", "Ему удалось сдать экзамен с третьей попытки.", ["managed", "achieved", "succeeded"], "managed",
      "Удалось сделать — managed to. Achieve to — ошибка."),
    c("n5-wait", 5, "We can't ___ to wait — every minute counts.", "Мы не можем позволить себе ждать — дорога каждая минута.", ["afford", "allow", "manage"], "afford",
      "Позволить себе — afford to."),
    c("n5-car", 5, "I can't afford ___ a new car.", "Я не могу позволить себе купить новую машину.", ["to buy", "buying", "buy"], "to buy", "afford to + глагол."),
    c("n5-getby", 5, "My German isn't perfect, but I can get ___.", "Мой немецкий не идеален, но объясниться я могу.", ["by", "on", "over"], "by", "Обходиться, справляться — get by."),

    # 6 · end up, work out, pull off
    c("n6-staying", 6, "It was raining, so we ended up ___ at home.", "Шёл дождь, и в итоге мы остались дома.", ["staying", "to stay", "stay"], "staying", "end up + -ing."),
    c("n6-hospital", 6, "He ignored the symptoms and ended up ___ hospital.", "Он не обращал внимания на симптомы и в итоге попал в больницу.", ["in", "at", "to"], "in",
      "Оказаться где-то — end up in."),
    c("n6-hope", 6, "I hope everything works ___ for you.", "Надеюсь, у тебя всё сложится.", ["out", "up", "off"], "out", "Сложиться, получиться — work out."),
    c("n6-pull", 6, "It was a very difficult operation, but they pulled it ___.", "Операция была очень сложной, но у них получилось.", ["off", "out", "up"], "off",
      "Провернуть трудное — pull it off."),
    c("n6-moscow", 6, "We tried living in Moscow, but it didn't work ___.", "Мы пробовали жить в Москве, но не сложилось.", ["out", "off", "up"], "out", "Не сложилось — didn't work out."),

    # 7 · в больнице и в статьях
    c("n7-endpoint", 7, "The trial ___ its primary endpoint.", "Исследование достигло первичной конечной точки.", ["achieved", "managed", "succeeded"], "achieved",
      "Достичь результата — achieve."),
    c("n7-recruit", 7, "We succeeded in ___ 500 patients.", "Нам удалось набрать 500 пациентов.", ["recruiting", "recruit", "to recruit"], "recruiting", "succeed in + -ing."),
    c("n7-mortality", 7, "The intervention failed ___ mortality at 90 days.", "Вмешательство не снизило смертность к 90-му дню.", ["to reduce", "reducing", "reduce"], "to reduce",
      "fail to + глагол."),
    c("n7-restore", 7, "We ___ restore blood flow within 20 minutes.", "Нам удалось восстановить кровоток за 20 минут.", ["managed to", "could", "succeeded to"], "managed to",
      "Удалось один раз — managed to."),
    c("n7-mother", 7, "Your mother is ___ well after the stroke.", "Ваша мама хорошо справляется после инсульта.", ["coping", "dealing with", "handling with"], "coping",
      "Справляться с трудностями — cope. Handle with и dealing with без дополнения — ошибки."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
