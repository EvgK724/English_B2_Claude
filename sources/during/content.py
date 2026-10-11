# Содержание тренажёра «For, during, within» — пять способов сказать «в течение»: for, during, over, throughout, within,
# и ловушки рядом: in (через), while (пока — с подлежащим и глаголом), «в течение» в статьях.
# Отличие от «Предлогов at, on, in» (preps): там время в точке (at 5, on Monday, in May) и by к сроку; здесь — отрезок времени.
# Разметка в примерах: [for …|a] — оранжевый, [during …|b] — синий, [within и throughout …|c] — зелёный, [over, in, while …] — подчёркнуто.
# Темы с полем late вступают в общую тренировку позже.

MIXED_TOPIC = 9

GROUPS = {
    "b1": "B1 — for и during",
    "b1p": "B1+ — within, throughout, over",
    "b2": "B2 — while и язык статей",
    "mix": "Итог",
}

# Главная таблица: слово | смысл («вопрос — пояснение») | примеры
TABLE = [
    ["for", "сколько? — длительность отрезка", "for two hours · for a year"],
    ["during", "когда? во время чего? — событие или период", "during the meeting · during the night"],
    ["within", "не позднее — уложиться в срок", "within 24 hours · within 4.5 hours of onset"],
    ["throughout", "на протяжении всего — от начала до конца", "throughout the day · throughout the study"],
    ["over", "за период — изменение, тренд", "over the past five years · over the weekend"],
    ["in", "через — в конце срока", "in ten minutes · in a week"],
    ["while", "пока — дальше подлежащее и глагол", "while he was asleep · while driving"],
]

# Одна ситуация — разное слово: строки [английский, перевод]
CONTRAST = [
    [["I slept [for eight hours|a].", "сколько — восемь часов"],
     ["I woke up twice [during the night|b].", "когда — ночью"]],
    [["The doctor will see you [in ten minutes].", "через десять минут"],
     ["The doctor will see you [within ten minutes|c].", "не позже чем через десять минут"]],
    [["He woke up once [during the night|b].", "в какой-то момент ночи"],
     ["He was stable [throughout the night|c].", "всю ночь, без перерыва"]],
    [["He had a seizure [during the drive|b].", "during + существительное"],
     ["He had a seizure [while he was driving].", "while + подлежащее и глагол"]],
    [["Admissions have risen [over the past five years].", "за пять лет — тренд"],
     ["She has worked here [for five years|a].", "сколько — пять лет"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["Take it during seven days.", "Take it for seven days.", "сколько — for"],
    ["His phone rang for the meeting.", "His phone rang during the meeting.", "во время чего — during"],
    ["He fell during he was sleeping.", "He fell while he was sleeping.", "с подлежащим и глаголом — while"],
    ["while the operation", "during the operation", "с существительным — during"],
    ["I'll call you after ten minutes.", "I'll call you in ten minutes.", "через десять минут — in"],
    ["The results will be ready during two days.", "The results will be ready within two days.", "уложиться в срок — within"],
    ["He was stable during all the night.", "He was stable throughout the night.", "всю ночь — throughout или all night"],
    ["within 4.5 hours from onset", "within 4.5 hours of onset", "within … of"],
    ["He'll be back for an hour.", "He'll be back in an hour.", "вернётся через час — in"],
]

TOPICS = [
    {"n": 1, "group": "b1", "title": "for — сколько длится", "sub": "for two hours · for a year",
     "rule": "Сколько длится — for + отрезок времени: for two hours, for a week, for ten years, for ages. Это ответ на вопрос How long? Русское «в течение двух часов», «два часа», «неделю» — for two hours, for a week. During two hours — ошибка. С Present Perfect рядом с for бывает since — с какого момента: for ten years, но since 2015 (подробно — во «Временах английского»).",
     "ex": [
         {"en": "Take the antibiotics [for seven days|a].", "ru": "Принимайте антибиотики семь дней."},
         {"en": "He was unconscious [for a few minutes|a].", "ru": "Он был без сознания несколько минут."},
         {"en": "She has worked here [for ten years|a].", "ru": "Она работает здесь десять лет."},
     ]},
    {"n": 2, "group": "b1", "title": "during — во время чего", "sub": "during the meeting · during the night",
     "rule": "during + существительное — во время события или в течение периода: during the meeting, during the night, during surgery, during pregnancy, during his stay. Отвечает на вопрос «когда?», а не «сколько?». С числом during не ставят: during two hours — ошибка, нужно for two hours.",
     "ex": [
         {"en": "His phone rang [during the meeting|b].", "ru": "Во время совещания у него зазвонил телефон."},
         {"en": "His blood pressure dropped [during surgery|b].", "ru": "Во время операции давление упало."},
         {"en": "Warfarin is avoided [during pregnancy|b].", "ru": "Во время беременности варфарин не назначают."},
     ]},
    {"n": 3, "group": "b1", "title": "for или during", "sub": "сколько — или когда",
     "rule": "Два вопроса к себе: «сколько?» — for, «когда, во время чего?» — during. Часто они стоят в одном предложении: I slept for eight hours during the night. He was in hospital for two weeks during the winter. Не путайте с in: in the morning — утром, как часть дня; during the morning — в какой-то момент утра.",
     "ex": [
         {"en": "I slept [for eight hours|a] [during the night|b].", "ru": "Ночью я проспал восемь часов."},
         {"en": "He was in hospital [for two weeks|a] [during the winter|b].", "ru": "Зимой он две недели лежал в больнице."},
         {"en": "She felt sick [for an hour|a] [during the flight|b].", "ru": "Во время полёта её час мутило."},
     ]},
    {"n": 4, "group": "b1p", "title": "within — не позднее", "sub": "within 24 hours · in ten minutes", "late": 0.2,
     "rule": "within + срок — «в течение, не позднее»: действие уложится в этот срок. within 24 hours, within 4.5 hours of symptom onset — обратите внимание на of. А in + срок — «через»: in ten minutes значит примерно через десять минут, в конце срока. «Через десять минут» — in ten minutes, а не after ten minutes. Ещё within — «в пределах»: within normal limits.",
     "ex": [
         {"en": "Thrombolysis is given [within 4.5 hours of onset|c].", "ru": "Тромболизис проводят в течение 4,5 часа от начала симптомов."},
         {"en": "You will receive a reply [within 48 hours|c].", "ru": "Ответ придёт в течение 48 часов."},
         {"en": "The doctor will see you [in ten minutes].", "ru": "Врач примет вас через десять минут."},
     ]},
    {"n": 5, "group": "b1p", "title": "throughout — всё время", "sub": "throughout the night · throughout the hospital", "late": 0.2,
     "rule": "throughout — на протяжении всего, от начала до конца, без перерыва: throughout the night, throughout the treatment, throughout the year. during — в какой-то момент периода, throughout — весь период целиком: He woke up once during the night, но He was stable throughout the night. Ещё throughout — «по всему»: throughout the hospital, throughout the country.",
     "ex": [
         {"en": "The medicine should be taken [throughout the treatment|c].", "ru": "Лекарство нужно принимать на протяжении всего лечения."},
         {"en": "He was stable [throughout the night|c].", "ru": "Всю ночь он был стабилен."},
         {"en": "Hand gel is available [throughout the hospital|c].", "ru": "Антисептик для рук есть по всей больнице."},
     ]},
    {"n": 6, "group": "b1p", "title": "over — за период", "sub": "over the past five years", "late": 0.25,
     "rule": "over + период — «за, в течение»: что изменилось или произошло за этот отрезок. Особенно с Present Perfect и в статьях: over the past five years, over the last decade. О будущем — over the next few days. Ещё over the weekend — за выходные, over the years — с годами. Хорошо сочетается с трендами: Admissions have risen over the past decade.",
     "ex": [
         {"en": "Stroke admissions have risen [over the past five years].", "ru": "За последние пять лет госпитализаций с инсультом стало больше."},
         {"en": "His speech improved gradually [over the next few days].", "ru": "За следующие несколько дней речь постепенно улучшилась."},
         {"en": "I'll read your thesis [over the weekend].", "ru": "Я прочитаю твою диссертацию за выходные."},
     ]},
    {"n": 7, "group": "b2", "title": "while или during", "sub": "while he was driving · during the drive", "late": 0.45,
     "rule": "Оба — «во время, пока». during + существительное: during the drive, during sleep. while + подлежащее и глагол: while he was driving; или while + -ing: while driving. Частая ошибка — during he was sleeping. Ещё while — «тогда как», противопоставление: Some patients recover quickly, while others need months.",
     "ex": [
         {"en": "He had a seizure [while he was driving].", "ru": "У него случился приступ за рулём."},
         {"en": "He had a seizure [during the drive|b].", "ru": "У него случился приступ во время поездки."},
         {"en": "Never use your phone [while driving].", "ru": "Не пользуйтесь телефоном за рулём."},
     ]},
    {"n": 8, "group": "b2", "title": "«В течение» в статьях", "sub": "over a 12-month period · throughout follow-up", "late": 0.5,
     "rule": "В статьях каждое «в течение» — своим словом. Период наблюдения — over a 12-month period или during follow-up. Всё время наблюдения — throughout follow-up. Уложиться в срок — within 24 hours of admission. Пока длится исследование — for the duration of the study (формально). В ходе — in the course of (книжно). Во время госпитализации — during hospitalisation.",
     "ex": [
         {"en": "Patients were followed up [over a 12-month period].", "ru": "Пациентов наблюдали в течение 12 месяцев."},
         {"en": "[Throughout follow-up|c], no major bleeding occurred.", "ru": "За всё время наблюдения больших кровотечений не было."},
         {"en": "Treatment started [within 24 hours of admission|c].", "ru": "Лечение начали в течение 24 часов от поступления."},
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
    # 1 · for
    c("w1-days", 1, "Take the antibiotics ___ seven days.", "Принимайте антибиотики семь дней.",
      ["for", "during", "within"], "for", "Сколько — for. During seven days — ошибка."),
    c("w1-hours", 1, "The headache lasted ___ about two hours.", "Головная боль длилась около двух часов.",
      ["for", "during", "while"], "for", "Сколько длилась — for."),
    c("w1-years", 1, "She has worked here ___ ten years.", "Она работает здесь десять лет.",
      ["for", "during", "since"], "for", "Отрезок — for ten years. Since — с какого момента: since 2015."),
    c("w1-minutes", 1, "He was unconscious ___ a few minutes.", "Он был без сознания несколько минут.",
      ["for", "during", "over"], "for", "Сколько — for a few minutes."),
    c("w1-ages", 1, "I haven't seen him ___ ages.", "Я его сто лет не видел.",
      ["for", "during", "within"], "for", "Очень долго — for ages (разг.)."),
    c("w1-week", 1, "Keep the dressing on ___ a week.", "Не снимайте повязку неделю.",
      ["for", "during", "throughout"], "for", "Сколько — for a week."),

    # 2 · during
    c("w2-meeting", 2, "His phone rang ___ the meeting.", "Во время совещания у него зазвонил телефон.",
      ["during", "for", "while"], "during", "Во время события — during the meeting. While — дальше нужны подлежащее и глагол."),
    c("w2-night", 2, "She woke up three times ___ the night.", "Ночью она просыпалась три раза.",
      ["during", "for", "within"], "during", "Когда — during the night."),
    c("w2-surgery", 2, "His blood pressure dropped ___ surgery.", "Во время операции у него упало давление.",
      ["during", "for", "over"], "during", "Во время — during surgery."),
    c("w2-pregnancy", 2, "Warfarin is avoided ___ pregnancy.", "Во время беременности варфарин не назначают.",
      ["during", "for", "while"], "during", "Период — during pregnancy."),
    c("w2-twohours", 2, "The patient was monitored ___ two hours.", "Пациента наблюдали два часа.",
      ["for", "during", "while"], "for", "С числом, «сколько» — for. During two hours — ошибка."),
    c("w2-stay", 2, "He had a fall ___ his stay in hospital.", "Во время пребывания в больнице он упал.",
      ["during", "for", "within"], "during", "Во время — during his stay."),

    # 3 · for или during
    c("w3-night", 3, "I slept for eight hours ___ the night.", "Ночью я проспал восемь часов.",
      ["during", "for", "while"], "during", "Когда — during the night; сколько — for eight hours."),
    c("w3-eight", 3, "I slept ___ eight hours during the night.", "Ночью я проспал восемь часов.",
      ["for", "during", "while"], "for", "Сколько — for eight hours."),
    c("w3-winter", 3, "He was in hospital for two weeks ___ the winter.", "Зимой он две недели лежал в больнице.",
      ["during", "for", "within"], "during", "Когда — during the winter."),
    c("w3-howlong", 3, "How long did the seizure last? — ___ about three minutes.", "Сколько длился приступ? — Около трёх минут.",
      ["For", "During", "Within"], "For", "На How long? отвечают for."),
    c("w3-when", 3, "When did the seizure start? — ___ breakfast.", "Когда начался приступ? — Во время завтрака.",
      ["During", "For", "While"], "During", "На «когда?» — during + существительное."),
    c("w3-flight", 3, "She felt sick ___ an hour during the flight.", "Во время полёта её час мутило.",
      ["for", "during", "over"], "for", "Сколько — for an hour; когда — during the flight."),

    # 4 · within и in
    c("w4-onset", 4, "Thrombolysis is given ___ 4.5 hours of symptom onset.", "Тромболизис проводят в течение 4,5 часа от начала симптомов.",
      ["within", "during", "for"], "within", "Уложиться в срок — within … of."),
    c("w4-reply", 4, "You will receive a reply ___ 48 hours.", "Ответ придёт в течение 48 часов.",
      ["within", "during", "for"], "within", "Не позднее — within 48 hours."),
    c("w4-in", 4, "The doctor will see you ___ ten minutes.", "Врач примет вас через десять минут.",
      ["in", "after", "during"], "in", "Через — in ten minutes. After ten minutes — калька с «через».",
      also=None),
    c("w4-limits", 4, "His blood tests are ___ normal limits.", "Анализы крови у него в пределах нормы.",
      ["within", "during", "throughout"], "within", "В пределах нормы — within normal limits."),
    c("w4-of", 4, "Treatment should start within an hour ___ arrival.", "Лечение должно начаться в течение часа от поступления.",
      ["of", "at", "since"], "of", "within … of: within an hour of arrival."),
    c("w4-days", 4, "Most patients feel better ___ a few days.", "Большинству пациентов становится лучше в течение нескольких дней.",
      ["within", "during", "while"], "within", "Не позднее чем через несколько дней — within a few days."),

    # 5 · throughout
    c("w5-night", 5, "He slept well ___ the night and never woke up.", "Он хорошо спал всю ночь и ни разу не проснулся.",
      ["throughout", "during", "within"], "throughout", "Всю ночь, без перерыва — throughout. During — в какой-то момент ночи."),
    c("w5-treatment", 5, "The medicine should be taken ___ the treatment.", "Лекарство нужно принимать на протяжении всего лечения.",
      ["throughout", "within", "for"], "throughout", "На протяжении всего — throughout."),
    c("w5-hospital", 5, "Hand gel is available ___ the hospital.", "Антисептик для рук есть по всей больнице.",
      ["throughout", "during", "over"], "throughout", "По всему месту — throughout the hospital."),
    c("w5-once", 5, "He woke up once ___ the night.", "Ночью он проснулся один раз.",
      ["during", "throughout", "within"], "during", "Один раз в какой-то момент — during. Throughout — всё время."),
    c("w5-year", 5, "The clinic is open ___ the year.", "Клиника работает круглый год.",
      ["throughout", "during", "within"], "throughout", "Круглый год — throughout the year или all year round."),
    c("w5-life", 5, "She stayed active ___ her life.", "Она всю жизнь оставалась активной.",
      ["throughout", "during", "within"], "throughout", "Всю жизнь — throughout her life (или all her life)."),

    # 6 · over
    c("w6-past", 6, "Stroke admissions have risen ___ the past five years.", "За последние пять лет госпитализаций с инсультом стало больше.",
      ["over", "within", "since"], "over", "За период, тренд — over the past five years."),
    c("w6-next", 6, "His speech improved gradually ___ the next few days.", "За следующие несколько дней речь постепенно улучшилась.",
      ["over", "while", "since"], "over", "Постепенно за период — over the next few days."),
    c("w6-weekend", 6, "I'll read your thesis ___ the weekend.", "Я прочитаю твою диссертацию за выходные.",
      ["over", "for", "while"], "over", "За выходные — over the weekend."),
    c("w6-decade", 6, "Mortality has fallen by a third ___ the last decade.", "За последнее десятилетие смертность снизилась на треть.",
      ["over", "within", "since"], "over", "За десятилетие — over the last decade."),
    c("w6-period", 6, "Patients were followed up ___ a 12-month period.", "Пациентов наблюдали в течение 12 месяцев.",
      ["over", "while", "since"], "over", "Период наблюдения — over a 12-month period."),
    c("w6-years", 6, "___ the years, she became an expert in stroke care.", "С годами она стала экспертом по инсульту.",
      ["Over", "For", "Within"], "Over", "С годами — over the years."),

    # 7 · while или during
    c("w7-was", 7, "The patient fell ___ he was walking to the toilet.", "Пациент упал, когда шёл в туалет.",
      ["while", "during", "for"], "while", "Дальше подлежащее и глагол — while."),
    c("w7-night", 7, "The patient fell ___ the night.", "Пациент упал ночью.",
      ["during", "while", "for"], "during", "Дальше существительное — during."),
    c("w7-driving", 7, "Never use your phone ___ driving.", "Не пользуйтесь телефоном за рулём.",
      ["while", "during", "for"], "while", "while + -ing: while driving."),
    c("w7-sleep", 7, "His oxygen levels dropped ___ sleep.", "Во сне у него падала сатурация.",
      ["during", "while", "for"], "during", "Существительное sleep — during sleep."),
    c("w7-contrast", 7, "Some patients recover fully, ___ others need long rehabilitation.", "Одни пациенты восстанавливаются полностью, а другим нужна долгая реабилитация.",
      ["while", "during", "for"], "while", "while — «тогда как», противопоставление."),
    c("w7-op", 7, "The surgeon was called away ___ the operation.", "Хирурга вызвали прямо во время операции.",
      ["during", "while", "for"], "during", "Существительное — during the operation."),

    # 8 · в статьях
    c("w8-duration", 8, "Participants took the drug for the ___ of the study.", "Участники принимали препарат всё время исследования.",
      ["duration", "during", "period"], "duration", "Пока длится — for the duration of (формально)."),
    c("w8-course", 8, "In the ___ of the trial, three patients withdrew.", "В ходе исследования три пациента выбыли.",
      ["course", "during", "time"], "course", "В ходе — in the course of (книжно)."),
    c("w8-followup", 8, "No major bleeding occurred ___ follow-up.", "За всё время наблюдения больших кровотечений не было.",
      ["throughout", "within", "for"], "throughout", "За всё время наблюдения — throughout follow-up."),
    c("w8-admission", 8, "Antiplatelet therapy was started within 24 hours ___ admission.", "Антиагреганты начали в течение 24 часов от поступления.",
      ["of", "at", "during"], "of", "within … of: within 24 hours of admission."),
    c("w8-hosp", 8, "Pneumonia developed in 8% of patients ___ hospitalisation.", "Пневмония развилась у 8% пациентов во время госпитализации.",
      ["during", "for", "while"], "during", "Во время госпитализации — during hospitalisation."),
    c("w8-period", 8, "Data were collected ___ a two-year period.", "Данные собирали в течение двух лет.",
      ["over", "while", "since"], "over", "Период сбора данных — over a two-year period."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
    for alt in (k.get("also") or {}): assert alt in k["opts"] and alt != k["a"], k["id"]
    if "also" in k and not k["also"]: del k["also"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))
assert all(t["group"] in GROUPS for t in TOPICS) and [t["n"] for t in TOPICS] == list(range(1, MIXED_TOPIC + 1))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
