# Содержание приложения «Прилагательное или наречие».
# Пометки: {…} — прилагательное (синий), _…_ — наречие (оранжевый), |…| — зелёный.

MIXED_TOPIC = 13

# Памятка: четыре группы исключений (как на листках пользователя)
MEMO = [
    {"h": "На -ly, но это прилагательные", "kind": "adj",
     "words": [["elderly", "пожилой"], ["friendly", "дружелюбный"], ["likely", "вероятный"], ["lovely", "милый, чудесный"],
               ["lonely", "одинокий"], ["silly", "глупый"], ["ugly", "некрасивый"]],
     "note": "Наречий из них нет. «Как?» — in a friendly way."},
    {"h": "Одна форма — и «какой?», и «как?»", "kind": "both",
     "words": [["deep", "глубокий · глубоко"], ["early", "ранний · рано"], ["fast", "быстрый · быстро"], ["hard", "трудный · усердно"],
               ["high", "высокий · высоко"], ["late", "поздний · поздно"], ["long", "долгий · долго"], ["low", "низкий · низко"],
               ["near", "близкий · близко"], ["right", "верный · верно"], ["straight", "прямой · прямо"], ["wrong", "неверный · неверно"],
               ["daily", "ежедневный · ежедневно"]],
     "note": "Fastly — такого слова нет. Сравнение тоже без more: faster, harder, earlier."},
    {"h": "С -ly — другое слово", "kind": "pairs",
     "pairs": [["hard", "усердно, сильно", "hardly", "почти не"], ["late", "поздно", "lately", "в последнее время"],
               ["near", "близко", "nearly", "почти"], ["great", "отлично", "greatly", "значительно"],
               ["high", "высоко", "highly", "весьма, очень"], ["deep", "глубоко", "deeply", "глубоко (о чувствах)"],
               ["close", "близко", "closely", "внимательно"], ["short", "коротко", "shortly", "скоро"],
               ["most", "больше всего", "mostly", "в основном"]],
     "note": ""},
    {"h": "В разговоре можно без -ly", "kind": "adv",
     "words": [["cheap", "дёшево"], ["loud", "громко"], ["quick", "быстро"], ["slow", "медленно"]],
     "note": "Come quick! Go slow. В письме и нейтрально — quickly, slowly, loudly, cheaply."},
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["He works very hardly.", "He works very hard.", "hardly — «почти не»"],
    ["He drives fastly.", "He drives fast.", "fastly не бывает"],
    ["She smiled friendly.", "She smiled in a friendly way.", "friendly — прилагательное"],
    ["He speaks English good.", "He speaks English well.", "как? — well"],
    ["I feel badly.", "I feel bad.", "feel + прилагательное"],
    ["It sounds strangely.", "It sounds strange.", "sound + прилагательное"],
    ["I came lately.", "I came late.", "lately — «в последнее время»"],
    ["It's near impossible.", "It's nearly impossible.", "почти — nearly"],
    ["The drug great reduces the risk.", "The drug greatly reduces the risk.", "значительно — greatly"],
]

TOPICS = [
    {"n": 1, "title": "Какой? или как?", "sub": "careful — carefully",
     "rule": "Какой? — прилагательное, оно описывает существительное: a careful surgeon. Как? — наречие, оно описывает действие: she operates carefully. Наречие обычно = прилагательное + -ly.",
     "ex": [
         {"en": "She's a {careful} surgeon.", "ru": "Она аккуратный хирург. — какой?"},
         {"en": "She operates _carefully_.", "ru": "Она аккуратно оперирует. — как?"},
         {"en": "He was _badly_ injured.", "ru": "Он сильно пострадал."},
     ]},
    {"n": 2, "title": "На -ly, но прилагательные", "sub": "elderly, friendly, likely…",
     "rule": "Эти слова кончаются на -ly, но это прилагательные: elderly, friendly, likely, lovely, lonely, silly, ugly. Наречий из них не делают. Нужно «как?» — in a friendly way. Likely как наречие — только в most likely и very likely, обычно говорят probably.",
     "ex": [
         {"en": "An {elderly} man was admitted.", "ru": "Поступил пожилой мужчина."},
         {"en": "The nurses are very {friendly}.", "ru": "Медсёстры очень дружелюбные."},
         {"en": "She smiled _in a friendly way_.", "ru": "Она дружелюбно улыбнулась."},
         {"en": "It's {likely} that he'll need surgery.", "ru": "Вероятно, ему понадобится операция."},
     ]},
    {"n": 3, "title": "Одна форма: fast, hard, early", "sub": "a fast test — works fast",
     "rule": "Одна форма — и «какой?», и «как?»: deep, early, fast, hard, high, late, long, low, near, right, straight, wrong, а ещё daily, weekly. Fastly не бывает. Сравнение тоже без more: faster, harder, earlier. У некоторых из них есть форма на -ly, но с другим значением — это следующие темы.",
     "ex": [
         {"en": "She's a {hard} worker — she works _hard_.", "ru": "Она трудяга — много работает."},
         {"en": "It was an {early} sign, and we caught it _early_.", "ru": "Это был ранний признак, и мы заметили его рано."},
         {"en": "Take it twice _daily_.", "ru": "Принимайте два раза в день."},
     ]},
    {"n": 4, "title": "hard — hardly", "sub": "усердно — почти не",
     "rule": "hard — усердно, сильно: work hard, hit hard. hardly — почти не: I can hardly hear you. Hardly уже отрицание, not с ним не ставим.",
     "ex": [
         {"en": "She works _hard_.", "ru": "Она много работает."},
         {"en": "I can _hardly_ hear you.", "ru": "Я тебя почти не слышу."},
         {"en": "He _hardly_ slept last night.", "ru": "Он почти не спал ночью."},
     ]},
    {"n": 5, "title": "late — lately", "sub": "поздно — в последнее время",
     "rule": "late — поздно: come late, work late. lately — в последнее время: Have you been sleeping well lately? С lately обычно Present Perfect.",
     "ex": [
         {"en": "He came _late_.", "ru": "Он пришёл поздно."},
         {"en": "I often work _late_.", "ru": "Я часто работаю допоздна."},
         {"en": "Have you been sleeping well _lately_?", "ru": "Вы хорошо спите в последнее время?"},
     ]},
    {"n": 6, "title": "near — nearly", "sub": "близко — почти",
     "rule": "near — близко, рядом: near the hospital, near here. nearly — почти: nearly all, nearly ten o'clock. He nearly died — «он чуть не умер».",
     "ex": [
         {"en": "Is there a pharmacy _near_ here?", "ru": "Здесь поблизости есть аптека?"},
         {"en": "_Nearly_ all the patients recovered.", "ru": "Почти все пациенты поправились."},
         {"en": "He _nearly_ died.", "ru": "Он чуть не умер."},
     ]},
    {"n": 7, "title": "greatly, highly, deeply", "sub": "значительно, весьма, глубоко",
     "rule": "great — отлично (в разговоре): It works great. greatly — значительно: greatly reduces the risk. high — высоко, highly — весьма: highly effective. deep — глубоко в прямом смысле: a deep wound, deeply — о чувствах: deeply sorry.",
     "ex": [
         {"en": "It works _great_.", "ru": "Работает отлично. — разговорное"},
         {"en": "The risk is _greatly_ reduced.", "ru": "Риск значительно снижается."},
         {"en": "This drug is _highly_ effective.", "ru": "Препарат высокоэффективен."},
         {"en": "I'm _deeply_ sorry.", "ru": "Глубоко сожалею."},
     ]},
    {"n": 8, "title": "closely, shortly, mostly", "sub": "внимательно, скоро, в основном",
     "rule": "close — близко: stand close. closely — внимательно, тщательно: monitor closely. short — коротко: cut short. shortly — скоро: The doctor will see you shortly. most — больше всего, mostly — в основном.",
     "ex": [
         {"en": "Monitor him _closely_.", "ru": "Внимательно наблюдайте за ним."},
         {"en": "The doctor will see you _shortly_.", "ru": "Врач скоро вас примет."},
         {"en": "Our patients are _mostly_ elderly.", "ru": "Наши пациенты в основном пожилые."},
         {"en": "What worries you _most_?", "ru": "Что вас больше всего беспокоит?"},
     ]},
    {"n": 9, "title": "cheap, loud, quick, slow", "sub": "в разговоре — без -ly",
     "rule": "cheap, loud, quick, slow в разговоре бывают наречиями без -ly: Come quick! Go slow. Buy it cheap. В письме и в нейтральной речи — с -ly: quickly, slowly, loudly, cheaply. Перед глаголом — только с -ly. В сравнении короткая форма обычна: louder, quicker, slower.",
     "ex": [
         {"en": "Come _quick_! He's fallen.", "ru": "Скорее сюда! Он упал. — разговорное"},
         {"en": "Please drive _slowly_.", "ru": "Пожалуйста, езжайте медленно. — нейтрально"},
         {"en": "Could you speak _louder_?", "ru": "Можете говорить громче?"},
     ]},
    {"n": 10, "title": "good или well", "sub": "a good doctor — works well",
     "rule": "good — прилагательное: a good doctor. well — наречие: she works well, he speaks English well. Well — ещё и «здоров»: I'm not well today. Feel good — хорошее самочувствие и настроение, feel well — здоров.",
     "ex": [
         {"en": "She's a {good} doctor.", "ru": "Она хороший врач."},
         {"en": "She works _well_ under pressure.", "ru": "Она хорошо работает в стрессе."},
         {"en": "I'm not {well} today.", "ru": "Мне сегодня нездоровится. — well = здоров"},
     ]},
    {"n": 11, "title": "look, feel, sound + прилагательное", "sub": "You look tired",
     "rule": "После be, look, seem, feel, sound, smell, taste, get, become, stay — прилагательное, а не наречие: You look tired. It sounds strange. По-русски здесь часто наречие («звучит странно»), по-английски — прилагательное. Но если look — действие «посмотреть», нужно наречие: He looked angrily at me.",
     "ex": [
         {"en": "You look {tired}.", "ru": "Ты выглядишь уставшим."},
         {"en": "That sounds {strange}.", "ru": "Звучит странно. — по-английски прилагательное"},
         {"en": "He looked _angrily_ at me.", "ru": "Он сердито посмотрел на меня. — look здесь действие"},
     ]},
    {"n": 12, "title": "Как пишется -ly", "sub": "easily, gently, basically",
     "rule": "Обычно просто + ly: slow → slowly, careful → carefully (два l). y → ily: easy → easily. le → ly: gentle → gently. ic → ically: basic → basically (исключение: public → publicly). true → truly, full → fully.",
     "ex": [
         {"en": "easy → _easily_ · happy → _happily_", "ru": "-y → -ily"},
         {"en": "gentle → _gently_ · simple → _simply_", "ru": "-le → -ly"},
         {"en": "basic → _basically_ · dramatic → _dramatically_", "ru": "-ic → -ically (но public → publicly)"},
         {"en": "careful → _carefully_ · true → _truly_", "ru": "careful + ly — два l; true → truly без e"},
     ]},
    {"n": 13, "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · какой? или как?
    c("b1-careful", 1, "She is a very ___ surgeon.", "Она очень аккуратный хирург.", ["careful", "carefully"], "careful",
      "Какой хирург? — прилагательное careful."),
    c("b1-carefully", 1, "She examined the wound ___.", "Она внимательно осмотрела рану.", ["carefully", "careful"], "carefully",
      "Как осмотрела? — наречие carefully."),
    c("b1-quick", 1, "We need a ___ decision.", "Нам нужно быстрое решение.", ["quick", "quickly"], "quick", "Какое решение? — quick."),
    c("b1-rapidly", 1, "His speech improved ___ after the stroke.", "После инсульта его речь быстро восстановилась.", ["rapidly", "rapid"], "rapidly",
      "Как восстановилась? — наречие rapidly. Rapid — «быстрый»: a rapid improvement."),
    c("b1-badly", 1, "He was ___ injured in the accident.", "Он сильно пострадал в аварии.", ["badly", "bad"], "badly",
      "Как пострадал? — badly: сильно, тяжело."),
    c("b1-patiently", 1, "She explained the procedure ___.", "Она терпеливо объяснила процедуру.", ["patiently", "patient"], "patiently",
      "Как объяснила? — patiently."),

    # 2 · на -ly, но прилагательные
    c("ly-friendly", 2, "He's a very ___ nurse — the patients love him.", "Он очень дружелюбный медбрат — пациенты его любят.",
      ["friendly", "friendlily", "friend"], "friendly", "friendly — прилагательное, хоть и на -ly."),
    c("ly-way", 2, "She smiled at the child ___.", "Она дружелюбно улыбнулась ребёнку.", ["in a friendly way", "friendly", "friendlily"],
      "in a friendly way", "Наречия от friendly нет — говорят in a friendly way."),
    c("ly-likely", 2, "It's ___ that he'll need surgery.", "Вероятно, ему понадобится операция.", ["likely", "probably", "likelily"], "likely",
      "It's likely that… — здесь likely прилагательное: «вероятно, что…». It's probably — ошибка."),
    c("ly-probably", 2, "He'll ___ be discharged tomorrow.", "Его, вероятно, выпишут завтра.", ["probably", "likely", "likelily"], "probably",
      "«Вероятно» перед глаголом — probably.",
      also={"likely": "так говорят в американском; в британском — probably или most likely"}),
    c("ly-silly", 2, "That was ___ of me.", "Глупо с моей стороны.", ["silly", "sillily", "a silly"], "silly",
      "silly — прилагательное: It was silly of me."),
    c("ly-lonely", 2, "Many ___ elderly people need support.", "Многим одиноким пожилым людям нужна поддержка.", ["lonely", "alone", "lonelily"], "lonely",
      "Перед существительным — lonely, «одинокий». Alone — «один», перед существительным его не ставят. Elderly — тоже прилагательное."),

    # 3 · одна форма
    c("sf-fast", 3, "He drives too ___.", "Он ездит слишком быстро.", ["fast", "fastly"], "fast",
      "fast — одна форма: a fast car, drive fast. Fastly — такого слова нет."),
    c("sf-early", 3, "The ambulance arrived ___.", "Скорая приехала рано.", ["early", "earlily"], "early",
      "early — одна форма: an early sign, arrive early."),
    c("sf-straight", 3, "Sit up ___, please.", "Сядьте, пожалуйста, прямо.", ["straight", "straightly"], "straight",
      "straight — одна форма: a straight line, sit up straight."),
    c("sf-wrong", 3, "Something went ___ during the procedure.", "Во время процедуры что-то пошло не так.", ["wrong", "wrongly"], "wrong",
      "go wrong — «пойти не так»: здесь wrong без -ly."),
    c("sf-daily", 3, "Take this tablet twice ___.", "Принимайте эту таблетку два раза в день.", ["daily", "dayly", "in day"], "daily",
      "daily — и «ежедневный», и «ежедневно»: a daily dose, twice daily."),
    c("sf-long", 3, "Have you been waiting ___?", "Вы давно ждёте?", ["long", "longly"], "long",
      "long — и «длинный», и «долго»: Have you been waiting long?"),
    c("sf-faster", 3, "Could you walk a bit ___?", "Можешь идти чуть быстрее?", ["faster", "more fast", "more fastly"], "faster",
      "Сравнение без more: faster, harder, earlier, later."),

    # 4 · hard — hardly
    c("hh-works", 4, "She works very ___.", "Она очень много и усердно работает.", ["hard", "hardly"], "hard",
      "Усердно — hard. Hardly — «почти не»."),
    c("hh-hear", 4, "I can ___ hear you — the line is bad.", "Я тебя почти не слышу — плохая связь.", ["hardly", "hard"], "hardly",
      "Почти не — hardly."),
    c("hh-slept", 4, "I ___ slept last night.", "Я почти не спал прошлой ночью.", ["hardly", "hard"], "hardly", "hardly = почти не: hardly slept."),
    c("hh-hit", 4, "He hit his head ___ on the floor.", "Он сильно ударился головой об пол.", ["hard", "hardly"], "hard",
      "Сильно — hard. Hit hardly — «еле задел»."),
    c("hh-any", 4, "There's ___ any improvement.", "Улучшения почти нет.", ["hardly", "hard", "not hardly"], "hardly",
      "hardly any — почти никакого."),
    c("hh-surprising", 4, "It's ___ surprising that he's tired after a night shift.", "Неудивительно, что он устал после ночной смены.",
      ["hardly", "hard"], "hardly", "hardly surprising — «вряд ли удивительно», то есть неудивительно."),

    # 5 · late — lately
    c("ll-came", 5, "He came to the clinic ___.", "Он пришёл в поликлинику поздно.", ["late", "lately"], "late", "Поздно — late."),
    c("ll-lately", 5, "Have you been sleeping well ___?", "Вы хорошо спите в последнее время?", ["lately", "late"], "lately",
      "В последнее время — lately, обычно с Present Perfect."),
    c("ll-fridays", 5, "I often work ___ on Fridays.", "По пятницам я часто работаю допоздна.", ["late", "lately"], "late", "Допоздна — late."),
    c("ll-feeling", 5, "He hasn't been feeling well ___.", "В последнее время ему нездоровится.", ["lately", "late"], "lately",
      "lately — «в последнее время»."),
    c("ll-toolate", 5, "It's too ___ to start thrombolysis.", "Начинать тромболизис уже слишком поздно.", ["late", "lately"], "late",
      "Поздно — late: too late."),

    # 6 · near — nearly
    c("nn-all", 6, "___ all the patients recovered.", "Почти все пациенты поправились.", ["Nearly", "Near"], "Nearly", "Почти — nearly."),
    c("nn-pharmacy", 6, "Is there a pharmacy ___ here?", "Здесь поблизости есть аптека?", ["near", "nearly"], "near", "Рядом, поблизости — near."),
    c("nn-died", 6, "He ___ died during the operation.", "Он чуть не умер во время операции.", ["nearly", "near"], "nearly",
      "Чуть не — nearly: he nearly died."),
    c("nn-live", 6, "I live ___ the hospital.", "Я живу рядом с больницей.", ["near", "nearly"], "near", "Рядом с — near."),
    c("nn-ten", 6, "It's ___ ten o'clock.", "Уже почти десять.", ["nearly", "near"], "nearly", "Почти, около — nearly."),

    # 7 · greatly, highly, deeply
    c("gr-greatly", 7, "Early treatment ___ reduces the risk of disability.", "Раннее лечение значительно снижает риск инвалидности.",
      ["greatly", "great"], "greatly", "Значительно — greatly."),
    c("gr-great", 7, "The new scanner works ___.", "Новый томограф работает отлично.", ["great", "greatly"], "great",
      "Отлично (в разговоре) — great. Greatly — «значительно»."),
    c("hi-highly", 7, "This drug is ___ effective.", "Этот препарат высокоэффективен.", ["highly", "high"], "highly",
      "Очень, весьма — highly: highly effective."),
    c("hi-high", 7, "Lift your arm up ___.", "Поднимите руку высоко.", ["high", "highly"], "high", "Высоко — high. Highly — «весьма, очень»."),
    c("de-deeply", 7, "I'm ___ sorry for your loss.", "Глубоко соболезную вашей утрате.", ["deeply", "deep"], "deeply",
      "О чувствах — deeply: deeply sorry."),
    c("de-deep", 7, "Take a ___ breath.", "Сделайте глубокий вдох.", ["deep", "deeply"], "deep", "Какой вдох? — прилагательное deep."),

    # 8 · closely, shortly, mostly
    c("cl-closely", 8, "The patient must be monitored ___.", "За пациентом нужно внимательно наблюдать.", ["closely", "close"], "closely",
      "Внимательно, тщательно — closely."),
    c("cl-close", 8, "Don't stand too ___ to the patient.", "Не стойте слишком близко к пациенту.", ["close", "closely"], "close",
      "Близко — close. Closely — «внимательно»."),
    c("sh-shortly", 8, "The doctor will see you ___.", "Врач скоро вас примет.", ["shortly", "short"], "shortly",
      "Скоро — shortly. Short — «коротко»."),
    c("sh-short", 8, "The meeting was cut ___.", "Совещание прервали раньше времени.", ["short", "shortly"], "short",
      "cut short — прервать. Shortly — «скоро»."),
    c("mo-mostly", 8, "Our patients are ___ over seventy.", "Наши пациенты в основном старше семидесяти.", ["mostly", "most"], "mostly",
      "В основном — mostly. Most — «больше всего», «большинство»."),
    c("mo-most", 8, "What worries you ___?", "Что вас больше всего беспокоит?", ["most", "mostly"], "most",
      "Больше всего — most. Mostly — «в основном»."),

    # 9 · cheap, loud, quick, slow
    c("cq-slowly", 9, "Please drive ___ near the hospital.", "Пожалуйста, езжайте медленно возле больницы.", ["slowly", "slow"], "slowly",
      "Нейтрально — slowly.", also={"slow": "в разговоре так говорят, но нейтрально — slowly"}),
    c("cq-louder", 9, "Could you speak a bit ___?", "Можете говорить чуть громче?", ["louder", "more loudly", "loud"], "louder",
      "В сравнении короткая форма обычна: louder, quicker, slower.", also={"more loudly": "это правильно, но louder обычнее"}),
    c("cq-quickly", 9, "The nurse ___ called the doctor.", "Медсестра быстро позвала врача.", ["quickly", "quick"], "quickly",
      "Перед глаголом — только quickly. Quick без -ly — разговорное и только после глагола: Come quick!"),
    c("cq-cheaply", 9, "The clinic was built very ___.", "Поликлинику построили очень дёшево.", ["cheaply", "cheap"], "cheaply",
      "Нейтрально — cheaply. Cheap как наречие — разговорное и в основном в buy it cheap, get it cheap."),
    c("cq-quick", 9, "Come ___! He's not breathing!", "Скорее сюда! Он не дышит!", ["quick", "quickly"], "quick",
      "В спешке, в разговоре — Come quick!", also={"quickly": "это нейтральный вариант"}),

    # 10 · good или well
    c("gw-speaks", 10, "He speaks English very ___.", "Он очень хорошо говорит по-английски.", ["well", "good"], "well",
      "Как говорит? — наречие well. Good — прилагательное."),
    c("gw-doctor", 10, "She's a very ___ doctor.", "Она очень хороший врач.", ["good", "well"], "good", "Какой врач? — good."),
    c("gw-unwell", 10, "I'm not ___ today — I've got a temperature.", "Мне сегодня нездоровится — температура.", ["well", "good"], "well",
      "О здоровье — well: I'm not well = мне нездоровится."),
    c("gw-went", 10, "The operation went ___.", "Операция прошла хорошо.", ["well", "good"], "well", "Как прошла? — well."),
    c("gw-sounds", 10, "That sounds ___!", "Звучит отлично!", ["good", "well"], "good", "После sound — прилагательное: sounds good."),
    c("gw-recovering", 10, "The patient is recovering ___.", "Пациент хорошо восстанавливается.", ["well", "good"], "well",
      "Как восстанавливается? — well."),

    # 11 · look, feel, sound + прилагательное
    c("lk-tired", 11, "You look ___. Did you sleep at all?", "Ты выглядишь уставшим. Ты вообще спал?", ["tired", "tiredly"], "tired",
      "look «выглядеть» + прилагательное: look tired."),
    c("lk-bad", 11, "I feel ___ about forgetting her birthday.", "Мне неловко, что я забыл про её день рождения.", ["bad", "badly"], "bad",
      "feel + прилагательное: feel bad. Feel badly — ошибка."),
    c("lk-strange", 11, "His story sounds a bit ___.", "Его рассказ звучит немного странно.", ["strange", "strangely"], "strange",
      "sound + прилагательное: sounds strange. По-русски «странно», но по-английски это не наречие."),
    c("lk-smells", 11, "The wound smells ___ — it may be infected.", "Рана плохо пахнет — возможно, инфекция.", ["bad", "badly"], "bad",
      "smell + прилагательное: smells bad."),
    c("lk-angrily", 11, "He looked ___ at the nurse.", "Он сердито посмотрел на медсестру.", ["angrily", "angry"], "angrily",
      "Здесь look — действие «посмотрел»: как посмотрел? angrily. Сравни: He looked angry — выглядел сердитым."),
    c("lk-calm", 11, "Try to stay ___.", "Постарайтесь сохранять спокойствие.", ["calm", "calmly"], "calm",
      "stay «оставаться» + прилагательное: stay calm."),
    c("lk-worse", 11, "His condition got ___ overnight.", "За ночь его состояние ухудшилось.", ["worse", "badly", "worsely"], "worse",
      "get «становиться» + прилагательное: got worse."),

    # 12 · как пишется -ly
    c("sp-easily", 12, "He can walk ___ now.", "Теперь он легко ходит.", ["easily", "easyly", "easy"], "easily", "-y → -ily: easy → easily."),
    c("sp-gently", 12, "Press ___ on the abdomen.", "Мягко надавите на живот.", ["gently", "gentlely", "gentle"], "gently", "-le → -ly: gentle → gently."),
    c("sp-basically", 12, "___, it's a viral infection.", "По сути, это вирусная инфекция.", ["Basically", "Basicly", "Basic"], "Basically",
      "-ic → -ically: basic → basically."),
    c("sp-carefully", 12, "Read the instructions ___.", "Внимательно прочитайте инструкцию.", ["carefully", "carefuly", "carefull"], "carefully",
      "careful + ly = carefully, с двумя l."),
    c("sp-truly", 12, "I'm ___ sorry.", "Мне искренне жаль.", ["truly", "truely", "true"], "truly", "true → truly: e выпадает."),
    c("sp-possibly", 12, "Could you ___ come a bit earlier tomorrow?", "Вы не могли бы завтра прийти чуть раньше?",
      ["possibly", "possiblely", "possible"], "possibly", "-le → -ly: possible → possibly."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
