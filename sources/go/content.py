# Содержание приложения «go»: все сочетания с go — куда, с артиклем или без, чем заняться,
# go = «стать», фразовые глаголы, устойчивые выражения, went / gone / been.
# Пометка […] — оранжевый (с артиклем, ключевая часть), [...|b] — синий (без артикля, без to).

MIXED_TOPIC = 12

GROUPS = {
    "where": "Куда: с the или без",
    "what": "Чем заняться и как добраться",
    "change": "go = «стать»",
    "phrasal": "Фразовые глаголы",
    "set": "Просто запомнить",
    "mix": "Итог",
}

# С артиклем или без: [без, перевод], [с артиклем, перевод]
CONTRAST = [
    [["I go to [school|b].", "учусь в школе"], ["Mum went to [the school] to see my teacher.", "зашла в здание по делу"]],
    [["He went to [hospital|b].", "лёг в больницу (брит.)"], ["I went to [the hospital] to visit him.", "пошёл навестить"]],
    [["They go to [church|b] on Sundays.", "ходят на службу"], ["We went to [the church] to see the icons.", "зашли посмотреть"]],
    [["Let's go [shopping].", "по магазинам"], ["I need to go to [the shops].", "сходить в магазин"]],
    [["We went [by car|b].", "на машине"], ["We went [in my car].", "на моей машине"]],
    [["We're going on [holiday|b].", "в отпуск — без артикля"], ["We're going on [a trip].", "в поездку — с a"]],
]

# Фразовые глаголы: сочетание | перевод | пример
PHRASAL = [
    ["go on", "продолжать; происходить", "What's going on?"],
    ["go out", "выходить развлечься; гаснуть", "Let's go out tonight."],
    ["go out with", "встречаться с кем-то", "She's going out with a surgeon."],
    ["go off", "срабатывать; портиться", "The alarm went off at six."],
    ["go away", "уходить; проходить (о боли)", "The pain went away."],
    ["go back", "возвращаться", "She went back to work."],
    ["go up", "расти, повышаться", "Prices have gone up."],
    ["go down", "снижаться; спадать", "The swelling went down."],
    ["go over", "просмотреть, повторить", "Let's go over the results."],
    ["go through", "пережить трудное; тщательно просмотреть", "She went through a hard time."],
    ["go ahead", "начинать; «давайте»", "Can I ask a question? — Go ahead."],
    ["go with", "подходить, сочетаться", "This tie goes with your shirt."],
    ["go without", "обходиться без", "I can't go without coffee."],
]

# Просто запомнить: выражение | перевод
SET = [
    ["How's it going?", "Как дела?"],
    ["Here we go!", "Ну, поехали! / Ну вот, опять!"],
    ["Go ahead!", "Давай! Пожалуйста!"],
    ["a coffee to go", "кофе с собой"],
    ["two days to go", "осталось два дня"],
    ["on the go", "на бегу, весь в делах"],
    ["have a go", "попробовать"],
    ["It goes without saying.", "Само собой разумеется."],
    ["go too far", "перегнуть палку"],
    ["go with the flow", "плыть по течению"],
    ["Let it go.", "Отпусти, не думай об этом."],
    ["Anything goes.", "Можно всё, никаких правил."],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["go to home", "go home", "home — без to"],
    ["go to abroad", "go abroad", "abroad — без to"],
    ["I'm going to the bed. (спать)", "I'm going to bed.", "спать — без the"],
    ["go to cinema", "go to the cinema", "кино, театр — с the"],
    ["go to shopping", "go shopping", "занятие на -ing — без to"],
    ["go by foot", "go on foot", "пешком — on foot"],
    ["go by the bus", "go by bus", "by + транспорт — без артикля"],
    ["go to a walk", "go for a walk", "прогуляться — go for a walk"],
    ["The milk went wrong.", "The milk went bad.", "испортиться — go bad"],
    ["He has gone to London twice.", "He has been to London twice.", "бывал — been; gone — уехал и там"],
]

TOPICS = [
    {"n": 1, "group": "where", "title": "go to work, school, bed", "sub": "без артикля — по назначению",
     "rule": "Когда место нужно по его главному назначению — учиться, работать, спать, лечиться, молиться, — артикля нет: go to work, go to school, go to university, go to bed, go to church, go to hospital (британский вариант). Если идёшь в здание по другому делу — с the: My mum went to the school to see my teacher.",
     "ex": [
         {"en": "I go to [work|b] by bus.", "ru": "Я езжу на работу на автобусе."},
         {"en": "It's late — I'm going to [bed|b].", "ru": "Поздно — иду спать."},
         {"en": "Mum went to [the school] to see my teacher.", "ru": "Мама сходила в школу к моему учителю."},
     ]},
    {"n": 2, "group": "where", "title": "go to the cinema, the doctor", "sub": "с the · страны · события",
     "rule": "Обычные места в городе — с the: go to the shops, the cinema, the theatre, the bank, the gym, the park, the station, the airport, the toilet. К врачу — go to the doctor, the dentist (или the doctor's). Страны и города — без артикля: go to Italy, go to Kazan; но the USA, the UK. Событие — с a: go to a meeting, a party, a concert.",
     "ex": [
         {"en": "Let's go to [the cinema].", "ru": "Пойдём в кино."},
         {"en": "I need to go to [the dentist].", "ru": "Мне нужно к зубному."},
         {"en": "She's going to [the USA].", "ru": "Она едет в США."},
     ]},
    {"n": 3, "group": "where", "title": "go home, abroad, there", "sub": "совсем без to",
     "rule": "Без to: go home, go abroad, go there, go downstairs, go upstairs, go outside, go inside, go somewhere, go anywhere, go nowhere. Go to home, go to abroad, go to there — ошибки.",
     "ex": [
         {"en": "Let's go [home|b].", "ru": "Пошли домой."},
         {"en": "They often go [abroad|b].", "ru": "Они часто ездят за границу."},
         {"en": "I went [there|b] last year.", "ru": "Я ездил туда в прошлом году."},
     ]},
    {"n": 4, "group": "what", "title": "go shopping, swimming…", "sub": "go + -ing",
     "rule": "Занятия и развлечения — go + -ing, без to: go shopping, go swimming, go skiing, go fishing, go camping, go dancing, go sightseeing, go hiking. Go to shopping — ошибка. Место — с to: go to the shops, go to the pool.",
     "ex": [
         {"en": "We went [shopping].", "ru": "Мы ходили по магазинам."},
         {"en": "Let's go [swimming].", "ru": "Пойдём плавать."},
         {"en": "My father goes [fishing] every Sunday.", "ru": "Отец каждое воскресенье ездит на рыбалку."},
     ]},
    {"n": 5, "group": "what", "title": "go for a walk, go on holiday", "sub": "go for a … · go on …",
     "rule": "go for a + короткое занятие: go for a walk, a run, a swim, a drive, a drink, a meal. go on + поездка или режим: go on holiday (без a), go on a trip, go on a cruise, go on a business trip, go on a diet, go on strike (без a).",
     "ex": [
         {"en": "Let's go [for a walk].", "ru": "Пойдём прогуляемся."},
         {"en": "We're going [on holiday] in July.", "ru": "В июле мы едем в отпуск."},
         {"en": "I need to go [on a diet].", "ru": "Мне нужно сесть на диету."},
     ]},
    {"n": 6, "group": "what", "title": "go by car, on foot", "sub": "как добраться",
     "rule": "Способ передвижения — by без артикля: go by car, by bus, by train, by plane, by taxi, by bike. Пешком — on foot (не by foot). С my, the — уже in или on: go in my car, go on the 8 o'clock train.",
     "ex": [
         {"en": "I go to work [by bus|b].", "ru": "Я езжу на работу на автобусе."},
         {"en": "Let's go [on foot].", "ru": "Пойдём пешком."},
         {"en": "We went [in my car].", "ru": "Мы поехали на моей машине."},
     ]},
    {"n": 7, "group": "change", "title": "go numb, go grey, go wrong", "sub": "go + прилагательное = стать",
     "rule": "go + прилагательное — «стать», обычно о переменах к худшему: go red — покраснеть, go pale — побледнеть, go grey — поседеть, go bald — облысеть, go deaf — оглохнуть, go blind — ослепнуть, go numb — онеметь, go wrong — пойти не так, go bad — испортиться (о еде), go missing — пропасть. Состояние: go into shock, go into labour, go into a coma.",
     "ex": [
         {"en": "His arm went [numb].", "ru": "У него онемела рука."},
         {"en": "Something went [wrong].", "ru": "Что-то пошло не так."},
         {"en": "The milk has gone [bad].", "ru": "Молоко испортилось."},
     ]},
    {"n": 8, "group": "phrasal", "title": "go on, out, off, away, back", "sub": "продолжать · выходить · срабатывать",
     "rule": "go on — продолжать; происходить: Go on! What's going on? go out — выходить развлечься: go out for dinner; go out with — встречаться с кем-то. go off — срабатывать (будильник); портиться (еда). go away — уходить; проходить (о боли): The pain went away. go back — возвращаться: go back to work.",
     "ex": [
         {"en": "What's going [on]?", "ru": "Что происходит?"},
         {"en": "The pain went [away].", "ru": "Боль прошла."},
         {"en": "My alarm went [off] at six.", "ru": "Будильник зазвонил в шесть."},
     ]},
    {"n": 9, "group": "phrasal", "title": "go up, down, through, ahead", "sub": "расти · снижаться · пережить",
     "rule": "go up — расти: Prices went up. go down — снижаться, спадать: His blood pressure went down. The swelling went down. go over — просмотреть, повторить. go through — пережить трудное; тщательно просмотреть. go ahead — начинать, «давайте»: Go ahead! go with — подходить, сочетаться. go without — обходиться без.",
     "ex": [
         {"en": "Prices went [up].", "ru": "Цены выросли."},
         {"en": "His blood pressure went [down].", "ru": "Давление у него снизилось."},
         {"en": "Does this go [with] my shirt?", "ru": "Это подходит к моей рубашке?"},
     ]},
    {"n": 10, "group": "set", "title": "How's it going?", "sub": "выражения целиком",
     "rule": "Эти выражения проще запомнить целиком: How's it going? — как дела? Here we go! — ну, поехали! Go ahead! — давай! to go — с собой (a coffee to go) или «осталось» (two days to go). on the go — на бегу. have a go — попробовать. It goes without saying — само собой разумеется. go too far — перегнуть палку.",
     "ex": [
         {"en": "How's it [going]?", "ru": "Как дела?"},
         {"en": "A coffee [to go], please.", "ru": "Кофе с собой, пожалуйста."},
         {"en": "Let me [have a go].", "ru": "Дай попробовать."},
     ]},
    {"n": 11, "group": "set", "title": "went, gone, been, going to", "sub": "формы и будущее",
     "rule": "Формы: go — went — gone. He's gone to Moscow — уехал и сейчас там. He's been to Moscow — бывал и вернулся. be going to + глагол — план или прогноз: I'm going to call him. It's going to rain. В разговоре — gonna.",
     "ex": [
         {"en": "Yesterday we [went] to the theatre.", "ru": "Вчера мы ходили в театр."},
         {"en": "He's [gone] home.", "ru": "Он ушёл домой."},
         {"en": "I've [been] to London.", "ru": "Я бывал в Лондоне."},
     ]},
    {"n": 12, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · без артикля
    c("g1-work", 1, "I go to ___ by bus.", "Я езжу на работу на автобусе.", ["work", "the work", "a work"], "work", "go to work — без артикля."),
    c("g1-bed", 1, "It's late — I'm going to ___.", "Уже поздно — я иду спать.", ["bed", "the bed", "a bed"], "bed",
      "Спать — go to bed, без артикля. The bed — конкретная кровать."),
    c("g1-school", 1, "In Russia, children start going to ___ at six or seven.", "В России дети идут в школу в шесть-семь лет.", ["school", "the school", "a school"], "school",
      "Учиться — go to school, без артикля."),
    c("g1-hospital", 1, "He was badly hurt and had to go to ___.", "Он сильно пострадал, и его пришлось положить в больницу.", ["hospital", "the hospital"], "hospital",
      "Лечиться — go to hospital, без артикля (британский вариант).",
      also={"the hospital": "так говорят в американском английском; в британском о пациенте — go to hospital"}),
    c("g1-mum", 1, "My mum went to ___ to talk to my teacher.", "Мама сходила в школу поговорить с моим учителем.", ["the school", "school"], "the school",
      "Не учиться, а по делу в здание — the school."),
    c("g1-church", 1, "They go to ___ every Sunday.", "Они ходят в церковь каждое воскресенье.", ["church", "the church"], "church",
      "На службу — go to church, без артикля."),

    # 2 · с the
    c("g2-cinema", 2, "Let's go to ___ tonight.", "Пойдём сегодня в кино.", ["the cinema", "cinema"], "the cinema", "Кино, театр — с the."),
    c("g2-dentist", 2, "I need to go to ___ — I've got toothache.", "Мне нужно к зубному — болит зуб.", ["the dentist", "dentist"], "the dentist",
      "К врачу — go to the dentist, the doctor."),
    c("g2-gym", 2, "I go to ___ three times a week.", "Я хожу в спортзал три раза в неделю.", ["the gym", "gym"], "the gym", "Спортзал — с the."),
    c("g2-usa", 2, "She's going to ___ next month.", "В следующем месяце она едет в США.", ["the USA", "USA"], "the USA",
      "Страны без артикля, но the USA, the UK."),
    c("g2-italy", 2, "We went to ___ last summer.", "Прошлым летом мы ездили в Италию.", ["Italy", "the Italy"], "Italy", "Страна — без артикля."),
    c("g2-meeting", 2, "I can't talk now — I'm going to ___.", "Не могу говорить — иду на совещание.", ["a meeting", "meeting"], "a meeting",
      "Событие — с артиклем: a meeting, a party."),
    c("g2-toilet", 2, "Excuse me, I need to go to ___.", "Извините, мне нужно в туалет.", ["the toilet", "toilet"], "the toilet", "Туалет — с the."),

    # 3 · без to
    c("g3-home", 3, "It's six o'clock — let's go ___.", "Шесть часов — пошли домой.", ["home", "to home", "to the home"], "home", "home — без to."),
    c("g3-abroad", 3, "They go ___ every summer.", "Каждое лето они ездят за границу.", ["abroad", "to abroad"], "abroad", "abroad — без to."),
    c("g3-there", 3, "Have you been to Kazan? — Yes, I went ___ last year.", "Ты был в Казани? — Да, ездил туда в прошлом году.", ["there", "to there"], "there",
      "there — без to."),
    c("g3-downstairs", 3, "Go ___ and wait in reception.", "Спуститесь вниз и подождите в регистратуре.", ["downstairs", "to downstairs"], "downstairs",
      "downstairs, upstairs — без to."),
    c("g3-somewhere", 3, "Let's go ___ quiet.", "Пойдём куда-нибудь, где тихо.", ["somewhere", "to somewhere"], "somewhere", "somewhere, anywhere — без to."),

    # 4 · go + -ing
    c("g4-shopping", 4, "We usually go ___ on Saturdays.", "Обычно мы ходим по магазинам по субботам.", ["shopping", "to shopping"], "shopping",
      "Занятие — go + -ing, без to."),
    c("g4-fishing", 4, "My father loves to go ___.", "Отец обожает рыбалку.", ["fishing", "to fishing"], "fishing", "go fishing — без to."),
    c("g4-skiing", 4, "Last winter we went ___ in the Urals.", "Прошлой зимой мы катались на лыжах на Урале.", ["skiing", "to skiing"], "skiing",
      "go skiing — без to."),
    c("g4-sightseeing", 4, "In Rome we went ___ every day.", "В Риме мы каждый день осматривали достопримечательности.", ["sightseeing", "to sightseeing"], "sightseeing",
      "go sightseeing — без to."),
    c("g4-dancing", 4, "Shall we go ___ tonight?", "Пойдём сегодня потанцевать?", ["dancing", "to dancing"], "dancing", "go dancing — без to."),

    # 5 · go for a … / go on …
    c("g5-walk", 5, "After dinner we went for ___.", "После ужина мы пошли прогуляться.", ["a walk", "walk", "the walk"], "a walk", "Прогуляться — go for a walk."),
    c("g5-swim", 5, "It's hot — let's go for ___.", "Жарко — пойдём искупаемся.", ["a swim", "swim", "swimming"], "a swim",
      "go for a swim или go swimming. Go for swimming — ошибка."),
    c("g5-holiday", 5, "We're going on ___ in July.", "В июле мы едем в отпуск.", ["holiday", "the holiday"], "holiday", "В отпуск — go on holiday, без артикля."),
    c("g5-trip", 5, "She's going on ___ to Kazan.", "Она едет в командировку в Казань.", ["a business trip", "business trip"], "a business trip",
      "Поездка — с a: go on a trip, a business trip."),
    c("g5-diet", 5, "I need to go on ___.", "Мне нужно сесть на диету.", ["a diet", "diet", "the diet"], "a diet", "Сесть на диету — go on a diet."),
    c("g5-strike", 5, "The nurses went on ___ for more pay.", "Медсёстры объявили забастовку, требуя повышения зарплаты.", ["strike", "a strike", "the strike"], "strike",
      "Бастовать — go on strike, без артикля."),

    # 6 · by car, on foot
    c("g6-bus", 6, "I usually go to work ___ bus.", "Обычно я езжу на работу на автобусе.", ["by", "on", "with"], "by", "Способ — by + транспорт без артикля."),
    c("g6-foot", 6, "It's close — let's go ___ foot.", "Тут близко — пойдём пешком.", ["on", "by", "with"], "on", "Пешком — on foot."),
    c("g6-train", 6, "They went to Moscow by ___.", "Они поехали в Москву на поезде.", ["train", "the train", "a train"], "train", "by train — без артикля."),
    c("g6-mycar", 6, "We went ___ my car.", "Мы поехали на моей машине.", ["in", "by"], "in", "С my — in my car. By — только без артикля: by car."),

    # 7 · go + прилагательное
    c("g7-numb", 7, "Suddenly his left arm went ___.", "Внезапно у него онемела левая рука.", ["numb", "numbness"], "numb", "Онеметь — go numb."),
    c("g7-grey", 7, "My father went ___ when he was forty.", "Отец поседел в сорок лет.", ["grey", "old", "tired"], "grey", "Поседеть — go grey."),
    c("g7-deaf", 7, "My grandmother is going ___ — she can't hear the phone.", "Бабушка глохнет — не слышит телефон.", ["deaf", "blind", "bald"], "deaf",
      "Глохнуть — go deaf."),
    c("g7-wrong", 7, "Something went ___ during the operation.", "Во время операции что-то пошло не так.", ["wrong", "bad"], "wrong",
      "Пойти не так — go wrong. Go bad — об испорченной еде."),
    c("g7-bad", 7, "Don't drink that milk — it's gone ___.", "Не пей это молоко — оно испортилось.", ["bad", "wrong"], "bad", "Испортиться (о еде) — go bad."),
    c("g7-shock", 7, "The patient went into ___ after the injury.", "После травмы у пациента развился шок.", ["shock", "the shock", "a shock"], "shock",
      "Впасть в шок — go into shock, без артикля."),
    c("g7-pale", 7, "She went ___ when she saw the results.", "Она побледнела, увидев результаты.", ["pale", "pallor"], "pale", "Побледнеть — go pale."),

    # 8 · go on, out, off, away, back
    c("g8-on", 8, "What's going ___ here? Why is everyone shouting?", "Что здесь происходит? Почему все кричат?", ["on", "off", "out"], "on",
      "Происходить — go on."),
    c("g8-alarm", 8, "My alarm went ___ at six.", "Будильник зазвонил в шесть.", ["off", "on", "out"], "off", "Сработать (будильник) — go off."),
    c("g8-pain", 8, "Take this tablet and the pain will go ___.", "Примите таблетку, и боль пройдёт.", ["away", "off", "out"], "away",
      "Пройти (о боли) — go away."),
    c("g8-dinner", 8, "Let's go ___ for dinner tonight.", "Давай сходим сегодня куда-нибудь поужинать.", ["out", "off", "away"], "out",
      "Выйти развлечься — go out."),
    c("g8-continue", 8, "Sorry for interrupting — please go ___.", "Простите, что перебил, — продолжайте.", ["on", "off", "away"], "on", "Продолжать — go on."),
    c("g8-back", 8, "She went ___ to work two weeks after the stroke.", "Через две недели после инсульта она вернулась на работу.", ["back", "on", "away"], "back",
      "Вернуться — go back."),

    # 9 · go up, down, through, ahead, with, without
    c("g9-bp", 9, "After the treatment, his blood pressure went ___.", "После лечения давление у него снизилось.", ["down", "off", "out"], "down",
      "Снизиться — go down."),
    c("g9-prices", 9, "Prices keep going ___.", "Цены всё растут.", ["up", "on", "over"], "up", "Расти — go up."),
    c("g9-through", 9, "She went ___ a very difficult time after the accident.", "После аварии ей пришлось пережить очень трудное время.", ["through", "over", "on"], "through",
      "Пережить трудное — go through."),
    c("g9-ahead", 9, "Can I ask you something? — Sure, go ___.", "Можно вас кое о чём спросить? — Конечно, спрашивайте.", ["ahead", "over", "off"], "ahead",
      "«Давайте, пожалуйста» — go ahead."),
    c("g9-with", 9, "Does this tie go ___ my shirt?", "Этот галстук подходит к моей рубашке?", ["with", "on", "over"], "with", "Подходить, сочетаться — go with."),
    c("g9-without", 9, "In the desert, you can't go ___ water for long.", "В пустыне без воды долго не протянешь.", ["without", "with", "over"], "without",
      "Обходиться без — go without."),

    # 10 · просто запомнить
    c("g10-how", 10, "Hi, Anna! How's it ___?", "Привет, Анна! Как дела?", ["going", "go", "gone"], "going", "Как дела? — How's it going?"),
    c("g10-coffee", 10, "A large cappuccino to ___, please.", "Большой капучино с собой, пожалуйста.", ["go", "going", "went"], "go", "С собой — to go."),
    c("g10-days", 10, "Only three days ___ go until my holiday!", "До отпуска осталось всего три дня!", ["to", "for", "till"], "to", "«Осталось» — … to go."),
    c("g10-have", 10, "I've never tried skiing, but I'd like to have a ___.", "Я никогда не катался на лыжах, но хотел бы попробовать.", ["go", "going", "went"], "go",
      "Попробовать — have a go."),
    c("g10-onthego", 10, "She's a busy doctor — always on the ___.", "Она занятой врач — вечно на бегу.", ["go", "going", "way"], "go", "На бегу, весь в делах — on the go."),
    c("g10-saying", 10, "It goes without ___ that patient safety comes first.", "Само собой разумеется, что безопасность пациента превыше всего.",
      ["saying", "say", "said"], "saying", "Само собой разумеется — it goes without saying."),
    c("g10-far", 10, "That joke went too ___.", "С этой шуткой ты перегнул палку.", ["far", "much", "long"], "far", "Перегнуть палку — go too far."),

    # 11 · went, gone, been, going to
    c("g11-went", 11, "Yesterday we ___ to the theatre.", "Вчера мы ходили в театр.", ["went", "gone", "go"], "went", "Прошедшее время — went."),
    c("g11-gone", 11, "Dr Ivanov isn't here — he's ___ home.", "Доктора Иванова нет — он ушёл домой.", ["gone", "been", "went"], "gone",
      "Ушёл и сейчас там — has gone."),
    c("g11-been", 11, "Have you ever ___ to London?", "Ты когда-нибудь бывал в Лондоне?", ["been", "gone", "went"], "been", "Бывал и вернулся — have been."),
    c("g11-plan", 11, "I'm going ___ my mother tonight.", "Вечером я собираюсь позвонить маме.", ["to call", "calling", "call"], "to call",
      "План — be going to + глагол."),
    c("g11-rain", 11, "Look at those clouds — it's ___ to rain.", "Посмотри на тучи — сейчас пойдёт дождь.", ["going", "go", "gone"], "going",
      "Прогноз по признакам — it's going to…"),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
    for alt in k.get("also", {}): assert alt in k["opts"] and alt != k["a"], k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
