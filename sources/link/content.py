# Содержание приложения «Связки»: although / despite / however, whereas, because / due to, so / therefore,
# in addition / also, to / so that, unless / in case — и как ими писать протоколы и статьи.
# Пометка […] — связка в фокусе (оранжевый).

MIXED_TOPIC = 9

GROUPS = {
    "contrast": "Хотя, однако, а",
    "cause": "Причина и следствие",
    "add": "Добавить, цель, условие",
    "papers": "В протоколах и статьях",
    "mix": "Итог",
}

# Что после связки: [связки + предложение], перевод | [связки + сущ. или -ing], перевод
AFTER = [
    [["although", "even though"], "хотя", ["despite", "in spite of"], "несмотря на"],
    [["because", "as · since"], "потому что", ["because of", "due to"], "из-за"],
    [["whereas", "while"], "а, тогда как", ["unlike"], "в отличие от"],
    [["so that"], "чтобы", ["to", "in order to"], "чтобы + глагол"],
]
# В начале нового предложения: связка | перевод | пример | перевод примера
START = [
    ["However,", "однако", "The effect was small. However, it was significant.", "эффект небольшой, однако значимый"],
    ["Therefore,", "поэтому", "Therefore, the results need confirmation.", "поэтому результаты требуют подтверждения"],
    ["In addition,", "кроме того", "In addition, we measured blood pressure.", "кроме того, мы измеряли давление"],
    ["In contrast,", "напротив", "In contrast, group B did not improve.", "группа Б, напротив, не улучшилась"],
    ["As a result,", "в результате", "As a result, few patients received tPA.", "в результате тромболизис получили немногие"],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["[Although] he is 85, he walks without help.", "хотя + предложение"], ["[Despite] his age, he walks without help.", "несмотря на + существительное"],
     ["He is 85. [However], he walks without help.", "однако — в начале нового предложения"]],
    [["He was late [because] the road was closed.", "потому что + предложение"], ["He was late [because of] the snow.", "из-за + существительное"]],
    [["Take it with food [so that] it doesn't upset your stomach.", "чтобы + предложение"], ["Take it with food [to avoid] stomach upset.", "чтобы + глагол"]],
    [["We'll start treatment [unless] the scan shows bleeding.", "если только не покажет"], ["Keep diazepam nearby [in case] he has another seizure.", "на случай, если"]],
    [["Group A improved, [whereas] group B did not.", "а, тогда как — сравниваем две группы"], ["Group A improved. [However], the effect was small.", "однако — оговорка"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["Despite of the rain…", "Despite the rain…", "despite — без of"],
    ["Despite he was tired…", "Although he was tired…", "перед предложением — although"],
    ["Although he was tired, but he worked.", "Although he was tired, he worked.", "although и but вместе не ставят"],
    ["He is old, however he is fit.", "He is old. However, he is fit.", "however — новое предложение и запятая"],
    ["because of he was ill", "because he was ill", "перед предложением — because"],
    ["due to he was late", "because he was late", "due to — только с существительным"],
    ["for to reduce the risk", "to reduce the risk", "чтобы — to, без for"],
    ["Unless he doesn't improve…", "Unless he improves…", "unless = if not, второе not лишнее"],
    ["In spite the rain…", "In spite of the rain…", "in spite of — с of"],
    ["Also we measured BP.", "We also measured BP.", "в статье also — перед глаголом"],
]

TOPICS = [
    {"n": 1, "group": "contrast", "title": "although, despite, however", "sub": "хотя, несмотря на, однако",
     "rule": "Хотя — although или even though + предложение: Although he is 85, he walks without help. Несмотря на — despite или in spite of + существительное или -ing: Despite his age… Despite being 85… Не despite of и не despite he is. Однако — however в начале нового предложения, с запятой: He is 85. However, he walks without help. Внутри предложения — but. Although и but вместе не ставят.",
     "ex": [
         {"en": "[Although] he is 85, he walks without help.", "ru": "Хотя ему 85, он ходит без помощи."},
         {"en": "[Despite] treatment, the patient deteriorated.", "ru": "Несмотря на лечение, состояние пациента ухудшилось."},
         {"en": "The effect was small. [However], it was significant.", "ru": "Эффект был небольшим. Однако он был значимым."},
     ]},
    {"n": 2, "group": "contrast", "title": "whereas, while, unlike", "sub": "а, тогда как, в отличие от",
     "rule": "Сравнить две вещи внутри предложения — whereas или while: Group A improved, whereas group B did not. В начале нового предложения — In contrast или On the other hand. В отличие от + существительное — unlike: Unlike warfarin, apixaban does not need regular blood tests.",
     "ex": [
         {"en": "Group A improved, [whereas] group B did not.", "ru": "Группа А улучшилась, а группа Б — нет."},
         {"en": "[In contrast], mortality did not change.", "ru": "Смертность, напротив, не изменилась."},
         {"en": "[Unlike] warfarin, apixaban does not need regular blood tests.", "ru": "В отличие от варфарина, апиксабан не требует регулярных анализов."},
     ]},
    {"n": 3, "group": "cause", "title": "because, because of, due to", "sub": "потому что, из-за",
     "rule": "Потому что — because, as или since + предложение: He was late because the road was closed. Из-за — because of или due to + существительное: because of the snow, due to bleeding. Due to he was late — ошибка; можно due to the fact that… As и since в начале предложения звучат официальнее: As the patient was unstable, we delayed the scan. Благодаря — thanks to.",
     "ex": [
         {"en": "The scan was delayed [because] the machine was broken.", "ru": "КТ задержали, потому что аппарат сломался."},
         {"en": "Treatment was stopped [due to] bleeding.", "ru": "Лечение прекратили из-за кровотечения."},
         {"en": "[As] the patient was unstable, we delayed the MRI.", "ru": "Поскольку пациент был нестабилен, МРТ отложили."},
     ]},
    {"n": 4, "group": "cause", "title": "so, therefore, as a result", "sub": "поэтому, в результате",
     "rule": "Поэтому внутри предложения — so после запятой: He was dizzy, so we called an ambulance. В начале нового предложения и в статьях — Therefore, As a result, Consequently: The sample was small. Therefore, the results should be interpreted with caution. Thus — книжное «таким образом». Вот почему — That's why.",
     "ex": [
         {"en": "He was dizzy, [so] we called an ambulance.", "ru": "У него кружилась голова, поэтому мы вызвали скорую."},
         {"en": "The sample was small. [Therefore], the results are uncertain.", "ru": "Выборка была маленькой. Поэтому результаты неоднозначны."},
         {"en": "[As a result], few patients received thrombolysis.", "ru": "В результате тромболизис получили немногие."},
     ]},
    {"n": 5, "group": "add", "title": "in addition, also, as well as", "sub": "кроме того, также",
     "rule": "Добавить мысль в начале нового предложения — In addition, Furthermore, Moreover (сильнее, не злоупотребляй). Внутри — also перед основным глаголом: We also measured blood pressure; Also we measured — разговорно. as well as или in addition to + существительное: in addition to aspirin. В конце фразы — too: My wife likes it too.",
     "ex": [
         {"en": "[In addition], we measured blood pressure.", "ru": "Кроме того, мы измеряли давление."},
         {"en": "We [also] recorded all adverse events.", "ru": "Мы также регистрировали все нежелательные явления."},
         {"en": "He takes aspirin [as well as] a statin.", "ru": "Он принимает аспирин, а также статин."},
     ]},
    {"n": 6, "group": "add", "title": "to, in order to, so that", "sub": "чтобы",
     "rule": "Чтобы + глагол — to или in order to (официальнее): We gave heparin to prevent DVT. For to — ошибка. Для + существительное — for: admitted for observation. Чтобы + предложение с другим подлежащим — so that: Speak slowly so that he can understand. Чтобы не — to avoid + сущ. или so as not to: so as not to wake the other patients.",
     "ex": [
         {"en": "We gave heparin [to] prevent DVT.", "ru": "Мы назначили гепарин, чтобы предотвратить ТГВ."},
         {"en": "Speak slowly [so that] he can understand you.", "ru": "Говорите медленно, чтобы он вас понял."},
         {"en": "He was admitted [for] observation.", "ru": "Его госпитализировали для наблюдения."},
     ]},
    {"n": 7, "group": "add", "title": "unless, in case, provided that", "sub": "если не, на случай если",
     "rule": "unless = if not, «если не»: Give aspirin unless the patient is allergic. После unless второе отрицание не ставят: unless he improves, не unless he doesn't improve. В протоколах — unless contraindicated, «при отсутствии противопоказаний». in case — «на случай, если»: Keep a glucose gel nearby in case his sugar drops. provided that, as long as — «при условии, что».",
     "ex": [
         {"en": "Start a statin [unless] contraindicated.", "ru": "Назначьте статин при отсутствии противопоказаний."},
         {"en": "Keep a glucose gel nearby [in case] his sugar drops.", "ru": "Держите рядом глюкозу на случай, если упадёт сахар."},
         {"en": "You can take the car [provided that] you bring it back by six.", "ru": "Бери машину при условии, что вернёшь её к шести."},
     ]},
    {"n": 8, "group": "papers", "title": "В протоколах и статьях", "sub": "if, despite, given, whereas, however",
     "rule": "Типичные связки научного текста: Patients were excluded if… Despite these limitations… Given the small sample… — с учётом. …, whereas… In order to reduce bias… However, larger trials are needed. Therefore, we recommend… In addition,… Старайся не начинать каждое предложение с Moreover.",
     "ex": [
         {"en": "Patients were excluded [if] they had a history of bleeding.", "ru": "Пациентов исключали, если в анамнезе было кровотечение."},
         {"en": "[Given] the small sample, the results should be interpreted with caution.", "ru": "С учётом малой выборки к результатам следует относиться осторожно."},
         {"en": "The results were promising. [However], larger trials are needed.", "ru": "Результаты обнадёживают. Однако нужны более крупные исследования."},
     ]},
    {"n": 9, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · although, despite, however
    c("l1-although", 1, "___ she was treated early, she had a poor outcome.", "Хотя её лечили рано, исход был плохим.",
      ["although", "despite", "however"], "although", "Хотя + предложение — although."),
    c("l1-despite", 1, "___ early treatment, she had a poor outcome.", "Несмотря на раннее лечение, исход был плохим.",
      ["despite", "although", "however"], "despite", "Несмотря на + существительное — despite."),
    c("l1-spite-of", 1, "In spite ___ the rain, we went for a walk.", "Несмотря на дождь, мы пошли гулять.",
      ["of", "", "for"], "of", "in spite of — с of; despite — без of."),
    c("l1-however", 1, "The difference was small. ___, it was statistically significant.", "Разница была небольшой. Однако она была статистически значимой.",
      ["however", "although", "despite"], "however", "Однако, в начале нового предложения — However,"),
    c("l1-but", 1, "He is 85, ___ he still drives.", "Ему 85, но он до сих пор водит.",
      ["but", "however", "despite"], "but", "Внутри предложения — but. However — в начале нового."),
    c("l1-despite-ing", 1, "Despite ___ aspirin, he had another stroke.", "Несмотря на приём аспирина, у него случился повторный инсульт.",
      ["taking", "he took", "to take"], "taking", "despite + -ing."),
    c("l1-even-though", 1, "She came to work ___ she had a fever.", "Она пришла на работу, хотя у неё была температура.",
      ["even though", "despite", "in spite of"], "even though", "Хотя (даже несмотря на то что) + предложение — even though."),
    c("l1-fact", 1, "Despite the fact ___ he was young, the stroke was severe.", "Несмотря на то что он был молод, инсульт был тяжёлым.",
      ["that", "of", "which"], "that", "despite the fact that + предложение."),

    # 2 · whereas, while, unlike
    c("l2-whereas", 2, "Mortality fell in the treatment group, ___ it rose in the control group.", "В группе лечения смертность снизилась, тогда как в контрольной выросла.",
      ["whereas", "despite", "because"], "whereas", "Сравнить две группы — whereas."),
    c("l2-contrast", 2, "Group A improved. In ___, group B showed no change.", "Группа А улучшилась. Группа Б, напротив, не изменилась.",
      ["contrast", "contrary", "opposite"], "contrast", "Напротив, в сравнении — In contrast,"),
    c("l2-hand", 2, "The drug is effective. On the other ___, it's expensive.", "Препарат эффективен. С другой стороны, он дорогой.",
      ["hand", "side", "way"], "hand", "С другой стороны — on the other hand."),
    c("l2-while", 2, "My brother loves big cities, ___ I prefer the countryside.", "Мой брат любит большие города, а я предпочитаю деревню.",
      ["while", "despite", "because"], "while", "А, тогда как — while или whereas."),
    c("l2-unlike", 2, "___ warfarin, apixaban does not need regular blood tests.", "В отличие от варфарина, апиксабан не требует регулярных анализов.",
      ["unlike", "whereas", "although"], "unlike", "В отличие от + сущ. — unlike."),

    # 3 · because, because of, due to
    c("l3-because", 3, "The scan was delayed ___ the machine was broken.", "КТ задержали, потому что аппарат был сломан.",
      ["because", "because of", "due to"], "because", "Потому что + предложение — because."),
    c("l3-because-of", 3, "The scan was delayed ___ a technical problem.", "КТ задержали из-за технической неполадки.",
      ["because of", "because", "since"], "because of", "Из-за + существительное — because of."),
    c("l3-due", 3, "Treatment was stopped ___ bleeding.", "Лечение прекратили из-за кровотечения.",
      ["due to", "because", "as"], "due to", "Из-за + существительное — due to."),
    c("l3-as", 3, "___ the patient was unstable, we delayed the MRI.", "Поскольку пациент был нестабилен, МРТ отложили.",
      ["as", "due to", "because of"], "as", "Поскольку + предложение — as или since."),
    c("l3-since", 3, "___ you're here, could you help me with this?", "Раз уж вы здесь, не поможете с этим?",
      ["since", "because of", "due to"], "since", "Раз уж, поскольку — since."),
    c("l3-fact", 3, "Due to the fact ___ he lives alone, he was admitted.", "Из-за того, что он живёт один, его госпитализировали.",
      ["that", "of", "which"], "that", "due to the fact that + предложение."),
    c("l3-thanks", 3, "___ to early treatment, she made a full recovery.", "Благодаря раннему лечению она полностью восстановилась.",
      ["thanks", "due", "because"], "thanks", "Благодаря чему-то хорошему — thanks to.",
      {"due": "но о хорошем результате чаще thanks to"}),

    # 4 · so, therefore, as a result
    c("l4-so", 4, "The road was icy, ___ we drove slowly.", "Дорога была скользкой, поэтому мы ехали медленно.",
      ["so", "therefore", "because"], "so", "Внутри предложения после запятой — so."),
    c("l4-therefore", 4, "The sample was small. ___, the results should be interpreted with caution.", "Выборка была маленькой. Поэтому к результатам следует относиться с осторожностью.",
      ["therefore", "so that", "because"], "therefore", "В начале нового предложения — Therefore,"),
    c("l4-result", 4, "Many patients arrived late. As a ___, few received thrombolysis.", "Многие пациенты поступили поздно. В результате тромболизис получили немногие.",
      ["result", "reason", "cause"], "result", "В результате — as a result."),
    c("l4-thus", 4, "Patients treated within three hours had the best outcomes. ___, early treatment matters.", "Лучшие исходы были у пациентов, пролеченных в первые три часа. Таким образом, раннее лечение важно.",
      ["thus", "however", "whereas"], "thus", "Таким образом — thus (книжн.)."),
    c("l4-why", 4, "He kept missing his tablets. That's ___ he had another stroke.", "Он постоянно пропускал таблетки. Вот почему у него повторный инсульт.",
      ["why", "because", "so"], "why", "Вот почему — that's why. That's because — «это потому, что»: причина, а не следствие."),
    c("l4-late", 4, "It was late, ___ we went home.", "Было поздно, поэтому мы пошли домой.",
      ["so", "so that", "in order to"], "so", "Поэтому — so. So that — «чтобы»."),

    # 5 · in addition, also, as well as
    c("l5-addition", 5, "In ___, we recorded all adverse events.", "Кроме того, мы регистрировали все нежелательные явления.",
      ["addition", "additional", "add"], "addition", "Кроме того — In addition,"),
    c("l5-also", 5, "We ___ measured blood pressure at 24 hours.", "Мы также измеряли давление через 24 часа.",
      ["also", "too", "as well"], "also", "Также, перед основным глаголом — also."),
    c("l5-well", 5, "He takes aspirin as ___ as a statin.", "Он принимает аспирин, а также статин.",
      ["well", "good", "far"], "well", "А также — as well as."),
    c("l5-moreover", 5, "The drug is cheap. ___, it has few side effects.", "Препарат дешёвый. Более того, у него мало побочных эффектов.",
      ["moreover", "therefore", "whereas"], "moreover", "Более того — Moreover,"),
    c("l5-to", 5, "In addition ___ aspirin, he takes a statin.", "Помимо аспирина, он принимает статин.",
      ["to", "of", "with"], "to", "in addition to + сущ."),
    c("l5-too", 5, "I like tea, and my wife likes it ___.", "Я люблю чай, и жена тоже.",
      ["too", "also", "either"], "too", "Тоже, в конце фразы — too. Either — после отрицания.",
      {"also": "но в конце фразы обычно ставят too"}),

    # 6 · to, in order to, so that
    c("l6-to", 6, "We started heparin ___ prevent DVT.", "Мы начали гепарин, чтобы предотвратить ТГВ.",
      ["to", "for", "for to"], "to", "Чтобы + глагол — to."),
    c("l6-order", 6, "In order ___ reduce the risk, we lowered the dose.", "Чтобы снизить риск, мы уменьшили дозу.",
      ["to", "that", "for"], "to", "in order to + глагол."),
    c("l6-so-that", 6, "Speak slowly ___ he can understand you.", "Говорите медленно, чтобы он вас понял.",
      ["so that", "in order to", "for"], "so that", "Чтобы + предложение — so that."),
    c("l6-avoid", 6, "Take the tablet with food to ___ stomach upset.", "Принимайте таблетку во время еды, чтобы избежать расстройства желудка.",
      ["avoid", "avoiding", "not"], "avoid", "Чтобы избежать — to avoid."),
    c("l6-for", 6, "He was admitted ___ observation.", "Его госпитализировали для наблюдения.",
      ["for", "to", "so that"], "for", "Для + существительное — for."),
    c("l6-not", 6, "We kept the lights low so as ___ to wake the other patients.", "Мы приглушили свет, чтобы не разбудить других пациентов.",
      ["not", "no", "don't"], "not", "Чтобы не — so as not to."),

    # 7 · unless, in case, provided that
    c("l7-unless", 7, "Start a statin ___ contraindicated.", "Назначьте статин при отсутствии противопоказаний.",
      ["unless", "if", "in case"], "unless", "Если нет противопоказаний — unless contraindicated."),
    c("l7-form", 7, "We'll discharge him tomorrow unless his condition ___.", "Выпишем его завтра, если только состояние не ухудшится.",
      ["deteriorates", "doesn't deteriorate", "won't deteriorate"], "deteriorates", "unless = if not: второе отрицание не нужно."),
    c("l7-in-case", 7, "Keep a glucose gel nearby ___ his sugar drops.", "Держите рядом гель с глюкозой на случай, если упадёт сахар.",
      ["in case", "unless", "provided"], "in case", "На случай, если — in case."),
    c("l7-provided", 7, "You can take the car ___ that you bring it back by six.", "Можешь взять машину при условии, что вернёшь её к шести.",
      ["provided", "unless", "in case"], "provided", "При условии, что — provided that."),
    c("l7-long", 7, "The drug is safe as ___ as kidney function is normal.", "Препарат безопасен при условии, что функция почек в норме.",
      ["long", "far", "much"], "long", "При условии, что — as long as."),

    # 8 · В протоколах и статьях
    c("l8-excluded", 8, "Patients were excluded ___ they had a history of bleeding.", "Пациентов исключали, если в анамнезе было кровотечение.",
      ["if", "unless", "whereas"], "if", "Если — if."),
    c("l8-despite", 8, "___ these limitations, the study has several strengths.", "Несмотря на эти ограничения, у исследования есть ряд сильных сторон.",
      ["despite", "although", "however"], "despite", "Несмотря на + сущ. — despite."),
    c("l8-given", 8, "___ the small sample, the results should be interpreted with caution.", "С учётом малой выборки к результатам следует относиться осторожно.",
      ["given", "despite", "unless"], "given", "С учётом — given."),
    c("l8-whereas", 8, "The first dose was given IV, ___ the following doses were oral.", "Первую дозу вводили внутривенно, а последующие — перорально.",
      ["whereas", "despite", "because of"], "whereas", "Сравнить две части — whereas."),
    c("l8-because-of", 8, "The trial was stopped early ___ safety concerns.", "Исследование прекратили досрочно из-за опасений по безопасности.",
      ["because of", "because", "although"], "because of", "Из-за + сущ. — because of."),
    c("l8-order", 8, "In ___ to reduce bias, outcomes were assessed blindly.", "Чтобы снизить систематическую ошибку, исходы оценивали вслепую.",
      ["order", "case", "addition"], "order", "Чтобы — in order to."),
    c("l8-however", 8, "The results were promising. ___, larger trials are needed.", "Результаты обнадёживают. Однако нужны более крупные исследования.",
      ["however", "although", "despite"], "however", "Однако — However,"),
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
