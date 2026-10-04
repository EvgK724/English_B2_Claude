# Содержание приложения «used to, be used to, get used to, would».
# Пометка [текст|x] — форма в фокусе; цвет: без метки — used to (оранжевый), |b — be used to (зелёный),
# |g — get used to (синий), |w — would и |p — пассив «используется» (подчёркнуто).

MIXED_TOPIC = 8

GROUPS = {
    "past": "Прошлое: used to и would",
    "now": "Привычка: be used to и get used to",
    "med": "В статьях",
    "mix": "Итог",
}

# Что с чем: форма | что после | пример | смысл | метка цвета
TABLE = [
    ["used to", "+ глагол", "I used to smoke.", "раньше курил, теперь нет", ""],
    ["would", "+ глагол", "We would go fishing.", "так бывало — только действия", "w"],
    ["be used to", "+ -ing или сущ.", "I'm used to working nights.", "привык, мне привычно", "b"],
    ["get used to", "+ -ing или сущ.", "You'll get used to it.", "привыкаешь, привыкнешь", "g"],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["I [used to work] nights.", "раньше работал по ночам, теперь нет"], ["I'm [used to working|b] nights.", "привык работать по ночам"],
     ["I'm [getting used to working|g] nights.", "привыкаю работать по ночам"]],
    [["She [used to live] in Moscow.", "жила — это состояние, только used to"], ["Every Sunday she [would visit|w] her mother.", "навещала — действие, можно would"]],
    [["I [used to] smoke.", "раньше курил"], ["[Did you use to] smoke?", "в вопросе — use без d"], ["I [didn't use to] smoke.", "в отрицании — тоже без d"]],
    [["You'll [get used to|g] it.", "привыкнешь — процесс"], ["I'm [used to|b] it.", "привык — уже привычно"]],
    [["She's [used to reading|b] MRI scans.", "привыкла читать МРТ"], ["MRI [is used to detect|p] small infarcts.", "МРТ используют, чтобы выявлять мелкие инфаркты"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["I'm used to work at night.", "I'm used to working at night.", "после be used to — -ing"],
    ["I used to working nights.", "I used to work nights.", "раньше делал — used to + глагол"],
    ["I didn't used to smoke.", "I didn't use to smoke.", "после did — use без d"],
    ["I was used to smoke.", "I used to smoke.", "«раньше курил» — без was"],
    ["I would live in Moscow.", "I used to live in Moscow.", "состояние — только used to"],
    ["She would have long hair.", "She used to have long hair.", "have — состояние, только used to"],
    ["There would be a cinema here.", "There used to be a cinema here.", "«раньше был» — there used to be"],
    ["I use to get up at six.", "I usually get up at six.", "сейчас обычно — usually"],
    ["I can't get used to live here.", "I can't get used to living here.", "после get used to — -ing"],
    ["You will used to it.", "You'll get used to it.", "привыкнешь — get used to"],
]

TOPICS = [
    {"n": 1, "group": "past", "title": "used to — раньше, а теперь нет", "sub": "привычки и состояния в прошлом",
     "rule": "used to + глагол — «раньше делал, а теперь нет»: I used to smoke. We used to live in Perm. There used to be a cinema here. Подходит и для действий, и для состояний: быть, жить, иметь, любить, знать. В отрицании и вопросе — use без d: I didn't use to like coffee. Did you use to work nights? Про настоящее use to не говорят: «обычно встаю» — I usually get up. Читается /ˈjuːstə/, с глухим s.",
     "ex": [
         {"en": "I [used to smoke], but I quit ten years ago.", "ru": "Раньше я курил, но бросил десять лет назад."},
         {"en": "There [used to be] a cinema here.", "ru": "Раньше здесь был кинотеатр."},
         {"en": "[Did you use to] work nights?", "ru": "Ты раньше работал по ночам?"},
     ]},
    {"n": 2, "group": "past", "title": "would — так бывало", "sub": "повторявшиеся действия в рассказе",
     "rule": "would + глагол — повторявшиеся действия в прошлом, чаще в рассказе и с ностальгией: Every summer we would go to the village. My grandfather would tell us stories. Только действия: состояние (live, have, be, know, like) — used to. Обычно рядом есть время: every summer, when I was a child. Рассказ часто начинают с used to, а дальше идут would.",
     "ex": [
         {"en": "Every summer we [would go|w] to the lake.", "ru": "Каждое лето мы ездили на озеро."},
         {"en": "My grandfather [would tell|w] us stories.", "ru": "Дедушка, бывало, рассказывал нам истории."},
         {"en": "Before exams I [would stay|w] up all night.", "ru": "Перед экзаменами я, бывало, не спал всю ночь."},
     ]},
    {"n": 3, "group": "past", "title": "used to, would или Past Simple", "sub": "действие, состояние или один раз",
     "rule": "Повторявшееся действие — и used to, и would: We used to go fishing = We would go fishing. Состояние — только used to: I used to have a dog. He used to be shy. Было один раз — ни то, ни другое, а Past Simple: I went to Paris in 2019.",
     "ex": [
         {"en": "I [used to have] a dog.", "ru": "Раньше у меня была собака."},
         {"en": "On Sundays we [would go|w] fishing.", "ru": "По воскресеньям мы ходили на рыбалку."},
         {"en": "People [used to believe] that stress caused ulcers.", "ru": "Раньше считали, что язву вызывает стресс."},
     ]},
    {"n": 4, "group": "now", "title": "be used to — привык", "sub": "уже привычно: + -ing или сущ.",
     "rule": "be used to + существительное или -ing — «привык, мне привычно»: I'm used to night shifts. I'm used to working at night. to здесь — предлог, поэтому дальше -ing: used to working, а не used to work. Время показывает be: I was used to it, I'll be used to it. Не привык — I'm not used to it.",
     "ex": [
         {"en": "I'm [used to|b] night shifts.", "ru": "Я привык к ночным сменам."},
         {"en": "She's [used to dealing|b] with difficult patients.", "ru": "Она привыкла иметь дело с трудными пациентами."},
         {"en": "I'm not [used to|b] the cold yet.", "ru": "Я ещё не привык к холоду."},
     ]},
    {"n": 5, "group": "now", "title": "get used to — привыкаю", "sub": "процесс: + -ing или сущ.",
     "rule": "get used to + существительное или -ing — «привыкать, привыкнуть», это процесс: You'll soon get used to it. I'm getting used to driving on the left. It took me a year to get used to the time difference. Здесь тоже -ing после to. «Никак не могу привыкнуть» — I can't get used to it.",
     "ex": [
         {"en": "You'll soon [get used to|g] it.", "ru": "Скоро привыкнешь."},
         {"en": "I'm [getting used to|g] the new system.", "ru": "Я привыкаю к новой системе."},
         {"en": "It took me months to [get used to working|g] nights.", "ru": "Мне понадобились месяцы, чтобы привыкнуть работать по ночам."},
     ]},
    {"n": 6, "group": "now", "title": "Три формы рядом", "sub": "раньше · привык · привыкаю",
     "rule": "Сравни: I used to work nights — раньше работал по ночам, теперь нет. I'm used to working nights — привык, мне это привычно. I'm getting used to working nights — привыкаю. Правило: если перед used to стоит be или get — дальше -ing; если нет — обычный глагол.",
     "ex": [
         {"en": "I [used to work] nights.", "ru": "Раньше я работал по ночам."},
         {"en": "I'm [used to working|b] nights.", "ru": "Я привык работать по ночам."},
         {"en": "I'm [getting used to working|g] nights.", "ru": "Я привыкаю работать по ночам."},
     ]},
    {"n": 7, "group": "med", "title": "is used to treat — «используется»", "sub": "пассив: + глагол",
     "rule": "В статьях и инструкциях часто встречается ещё одно used to — пассив от use: be used to + глагол — «используется, чтобы»: Aspirin is used to prevent strokes. MRI is used to detect small infarcts. Читается /juːzd/, со звонким z. Проверка: если по-русски «используется для» — дальше обычный глагол; если «привык» — -ing.",
     "ex": [
         {"en": "Aspirin [is used to prevent|p] strokes.", "ru": "Аспирин применяют для профилактики инсульта."},
         {"en": "MRI [is used to detect|p] small infarcts.", "ru": "МРТ используют, чтобы выявлять мелкие инфаркты."},
         {"en": "She's [used to reading|b] MRI scans.", "ru": "Она привыкла читать МРТ."},
     ]},
    {"n": 8, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · used to — раньше
    c("u1-smoke", 1, "I ___ smoke, but I quit ten years ago.", "Раньше я курил, но бросил десять лет назад.",
      ["used to", "was used to", "use to"], "used to", "Раньше делал, теперь нет — used to + глагол."),
    c("u1-live", 1, "We ___ live in Perm before we moved here.", "До переезда сюда мы жили в Перми.",
      ["used to", "were used to", "would"], "used to", "Жить — состояние: только used to."),
    c("u1-cinema", 1, "There ___ be a cinema on this corner.", "Раньше на этом углу был кинотеатр.",
      ["used to", "would", "was used to"], "used to", "Раньше был — there used to be."),
    c("u1-didnt", 1, "I didn't ___ like coffee, but now I drink three cups a day.", "Раньше я не любил кофе, а теперь пью по три чашки в день.",
      ["use to", "used to", "using"], "use to", "После did — use без d: didn't use to."),
    c("u1-question", 1, "Did you ___ work nights when you were younger?", "В молодости ты работал по ночам?",
      ["use to", "used to", "get used to"], "use to", "Вопрос с did — use to, без d."),
    c("u1-now", 1, "I ___ get up at six — every day, even at weekends.", "Я обычно встаю в шесть — каждый день, даже в выходные.",
      ["usually", "use to", "used to"], "usually", "Сейчас, обычно — usually. Used to — только о прошлом."),
    c("u1-surgeon", 1, "My father ___ a surgeon before he retired.", "До пенсии мой отец был хирургом.",
      ["used to be", "would be", "was used to be"], "used to be", "Кем был раньше — used to be. Would — только для действий."),

    # 2 · would — так бывало
    c("u2-summer", 2, "Every summer we ___ go to my grandmother's in the village.", "Каждое лето мы ездили к бабушке в деревню.",
      ["would", "were used to", "use to"], "would", "Повторявшееся действие в рассказе — would или used to."),
    c("u2-read", 2, "When I was little, my mother ___ read to me every night.", "Когда я был маленьким, мама читала мне каждый вечер.",
      ["would", "was used to", "got used to"], "would", "Так бывало, каждый вечер — would."),
    c("u2-stories", 2, "My grandfather ___ tell us stories about the war.", "Дедушка, бывало, рассказывал нам о войне.",
      ["would", "will", "was used to"], "would", "Повторявшееся действие — would."),
    c("u2-cat", 2, "As a child, I ___ have a cat called Murka.", "В детстве у меня была кошка Мурка.",
      ["used to", "would"], "used to", "have — иметь, это состояние: только used to."),
    c("u2-know", 2, "I ___ know all my patients by name.", "Раньше я знал всех пациентов по именам.",
      ["used to", "would"], "used to", "know — состояние: только used to."),
    c("u2-exams", 2, "Before exams I ___ stay up all night.", "Перед экзаменами я, бывало, не спал всю ночь.",
      ["would", "was used to", "am used to"], "would", "Так бывало перед каждым экзаменом — would."),

    # 3 · used to, would или Past Simple
    c("u3-paris", 3, "I ___ to Paris in 2019.", "В 2019 году я ездил в Париж.",
      ["went", "used to go", "would go"], "went", "Один раз в прошлом — Past Simple."),
    c("u3-hair", 3, "She ___ long hair when she was at school.", "В школе у неё были длинные волосы.",
      ["used to have", "would have", "was used to having"], "used to have", "have — состояние: used to have."),
    c("u3-fishing", 3, "On Sundays my dad and I ___ go fishing.", "По воскресеньям мы с папой ходили на рыбалку.",
      ["would", "used to", "were used to"], "would", "Повторявшееся действие — would или used to.",
      {"used to": "с действиями подходят оба"}),
    c("u3-shy", 3, "He ___ be very shy, but now he gives lectures.", "Раньше он был очень застенчивым, а теперь читает лекции.",
      ["used to", "would"], "used to", "be — состояние: только used to."),
    c("u3-sochi", 3, "We ___ a great holiday in Sochi last year.", "В прошлом году мы отлично отдохнули в Сочи.",
      ["had", "used to have", "would have"], "had", "Один раз — Past Simple."),
    c("u3-ulcers", 3, "People ___ believe that stress caused stomach ulcers.", "Раньше считали, что язву желудка вызывает стресс.",
      ["used to", "would"], "used to", "believe — состояние: только used to."),

    # 4 · be used to — привык
    c("u4-nights", 4, "I'm used to ___ at night.", "Я привык работать по ночам.",
      ["working", "work", "worked"], "working", "be used to + -ing: to здесь предлог."),
    c("u4-noise", 4, "After ten years in the ICU, she ___ the noise.", "За десять лет в реанимации она привыкла к шуму.",
      ["is used to", "used to", "uses to"], "is used to", "Привыкла, ей привычно — be used to + сущ."),
    c("u4-early", 4, "Don't worry about the early start — I'm used to ___ up at five.", "Не переживай из-за раннего подъёма — я привык вставать в пять.",
      ["getting", "get", "got"], "getting", "be used to + -ing."),
    c("u4-not", 4, "I'm not ___ to driving on the left.", "Я не привык ездить по левой стороне.",
      ["used", "use", "using"], "used", "Не привык — be not used to."),
    c("u4-was", 4, "The heat was hard at first, but by August I ___ used to it.", "Сначала жара давалась тяжело, но к августу я к ней привык.",
      ["was", "did", "had"], "was", "Время показывает be: I was used to it."),
    c("u4-dealing", 4, "She's used to ___ with difficult patients.", "Она привыкла иметь дело с трудными пациентами.",
      ["dealing", "deal", "dealt"], "dealing", "be used to + -ing."),
    c("u4-hard-work", 4, "I ___ to hard work — it doesn't scare me.", "Я привык к тяжёлой работе — она меня не пугает.",
      ["am used", "used", "use"], "am used", "К чему-то привык — be used to + сущ."),

    # 5 · get used to — привыкаю
    c("u5-soon", 5, "Don't worry — you'll soon ___ to it.", "Не волнуйся — скоро привыкнешь.",
      ["get used", "used", "use"], "get used", "Привыкнешь — you'll get used to it."),
    c("u5-driving", 5, "I'm slowly getting used to ___ on the left.", "Я понемногу привыкаю ездить по левой стороне.",
      ["driving", "drive", "drove"], "driving", "get used to + -ing."),
    c("u5-year", 5, "It took me a year to ___ used to the time difference.", "Мне понадобился год, чтобы привыкнуть к разнице во времени.",
      ["get", "be", "use"], "get", "Процесс «привыкнуть» — get used to."),
    c("u5-early", 5, "I can't get used to ___ so early.", "Никак не могу привыкнуть вставать так рано.",
      ["getting up", "get up", "got up"], "getting up", "get used to + -ing."),
    c("u5-system", 5, "The staff are still getting used ___ the new system.", "Персонал всё ещё привыкает к новой системе.",
      ["to", "with", "for"], "to", "Привыкать к — get used to."),
    c("u5-cpap", 5, "Most patients ___ used to the CPAP mask within a week.", "Большинство пациентов привыкают к маске CPAP за неделю.",
      ["get", "are", "use"], "get", "Привыкают за неделю, это процесс — get used to."),

    # 6 · Три формы рядом
    c("u6-used", 6, "I ___ work nights, but now I only do day shifts.", "Раньше я работал по ночам, а теперь только днём.",
      ["used to", "am used to", "am getting used to"], "used to", "Раньше, теперь нет — used to."),
    c("u6-am-used", 6, "I've worked nights for 20 years, so I ___ it.", "Я 20 лет работаю по ночам, так что привык.",
      ["am used to", "used to", "am getting used to"], "am used to", "Уже привык — be used to."),
    c("u6-getting", 6, "I started night shifts last month, and I'm slowly ___ them.", "Месяц назад я начал работать в ночь и понемногу привыкаю.",
      ["getting used to", "used to", "use to"], "getting used to", "Привыкаю, процесс — getting used to."),
    c("u6-live", 6, "She ___ live alone, but now she has a flatmate.", "Раньше она жила одна, а теперь у неё есть соседка.",
      ["used to", "is used to", "gets used to"], "used to", "Раньше жила — used to live."),
    c("u6-alone", 6, "She has lived alone for years — she ___ it.", "Она много лет живёт одна и привыкла.",
      ["is used to", "used to", "would"], "is used to", "Привыкла — be used to."),
    c("u6-city", 6, "Moving from a village to Moscow was hard, but she ___ city life quickly.", "Переехать из деревни в Москву было тяжело, но она быстро привыкла к городской жизни.",
      ["got used to", "used to", "would"], "got used to", "Быстро привыкла, процесс — got used to."),
    c("u6-work", 6, "I used to ___ on Saturdays.", "Раньше я работал по субботам.",
      ["work", "working"], "work", "used to + глагол: раньше делал."),
    c("u6-working", 6, "I'm used to ___ on Saturdays.", "Я привык работать по субботам.",
      ["working", "work"], "working", "be used to + -ing: привык."),

    # 7 · is used to treat — «используется»
    c("u7-aspirin", 7, "Aspirin is used to ___ strokes.", "Аспирин применяют для профилактики инсульта.",
      ["prevent", "preventing"], "prevent", "Используется, чтобы — is used to + глагол (пассив)."),
    c("u7-mri", 7, "MRI is used to ___ small infarcts.", "МРТ используют, чтобы выявлять мелкие инфаркты.",
      ["detect", "detecting"], "detect", "Пассив «используется» — + глагол."),
    c("u7-reading", 7, "She's a radiologist, so she's used to ___ MRI scans.", "Она рентгенолог и привыкла читать МРТ.",
      ["reading", "read"], "reading", "Привыкла — be used to + -ing."),
    c("u7-alteplase", 7, "Alteplase is used ___ dissolve blood clots.", "Алтеплазу применяют для растворения тромбов.",
      ["to", "for", "in"], "to", "Используется, чтобы — used to + глагол."),
    c("u7-scale", 7, "This scale is ___ to assess stroke severity.", "Эта шкала используется для оценки тяжести инсульта.",
      ["used", "use", "using"], "used", "Используется — is used (пассив)."),
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
