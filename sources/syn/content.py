# Содержание приложения «Синонимы» (English Collocations in Use, Units 10–11):
# пары синонимов, «старый», «один, единственный», win / beat / gain / earn / make / achieve, take / carry / wear / use, spend.
# Пометка […] — слово в фокусе (оранжевый). Примеры свои, не из учебника.

MIXED_TOPIC = 10

GROUPS = {
    "u10": "Unit 10 — пары и группы синонимов",
    "u11": "Unit 11 — выиграть, заработать, носить",
    "mix": "Итог",
}

# Пары: слово | с чем | пример | перевод (по два слова на пару)
PAIRS = [
    [["close", "официально, вежливо", "close the meeting · close your mouth", "закрыть совещание · закройте рот"],
     ["shut", "разговорно; Shut up! — грубо", "shut the door · Shut up!", "закрой дверь · заткнись"]],
    [["start", "машины, моторы; открыть дело", "start the car · start a business", "завести машину · открыть дело"],
     ["begin", "формально, абстрактно", "The universe began…", "Вселенная возникла…"]],
    [["big", "важный, серьёзный", "a big decision · a big problem", "важное решение · серьёзная проблема"],
     ["large", "размер, число, количество", "a large size · a large number", "большой размер · большое число"]],
    [["end", "прекратить, закончиться", "end a relationship · the film ended", "расстаться · фильм закончился"],
     ["finish", "довести до конца", "finish your homework · finish the course", "доделать домашку · пропить курс"]],
    [["charge", "аккумулятор, батарея", "charge your phone · charge the defibrillator", "зарядить телефон, дефибриллятор"],
     ["load", "груз, машина; доза", "load the van · a loading dose", "загрузить фургон · нагрузочная доза"]],
    [["injure", "людей, части тела", "three people were injured", "пострадали три человека"],
     ["damage", "вещи; органы и ткани", "a damaged car · brain damage", "разбитая машина · повреждение мозга"]],
    [["grow", "растения; бактерии в посеве", "grow crops · cultures grew E. coli", "выращивать урожай · в посеве выросла кишечная палочка"],
     ["raise", "животных, детей", "raise cattle · raise children", "разводить скот · растить детей"]],
]

# Получить, выиграть, заработать: слово | что | пример | перевод
WIN = [
    ["win", "что: матч, приз, выборы", "win a match · win a prize", "выиграть матч · получить приз"],
    ["beat", "кого: соперника", "beat them 3–1", "обыграть их 3:1"],
    ["gain", "абстрактное; вес", "gain access · gain weight", "получить доступ · набрать вес"],
    ["earn", "трудом", "earn a salary", "получать зарплату"],
    ["make", "прибыль, деньги", "make a profit", "получить прибыль"],
    ["achieve", "цель, результат", "achieve your goals", "достичь целей"],
]
# Взять, нести, носить: слово | что | пример | перевод
CARRY = [
    ["take", "взять с собой", "take an umbrella", "взять зонт"],
    ["carry", "нести; иметь при себе", "carry a bag · carry a phone", "нести сумку · носить с собой телефон"],
    ["wear", "носить на себе", "wear glasses · wear a mask", "носить очки, маску"],
    ["use", "пользоваться", "use a laptop", "пользоваться ноутбуком"],
    ["spend", "время и деньги", "spend a week · spend money on", "провести неделю · тратить на"],
]

# Группы: слово | транскрипция | значение | сочетания | озвучка
OLD = [
    ["old", "/əʊld/", "старый, давний — самое общее", "an old friend · an old building", "Old. An old friend. An old building."],
    ["ancient", "/ˈeɪnʃənt/", "древний — тысячи лет", "ancient history · ancient Rome", "Ancient. Ancient history. Ancient Rome."],
    ["antique", "/ænˈtiːk/", "старинный и ценный — о вещах", "antique furniture · an antique clock", "Antique. Antique furniture. An antique clock."],
    ["elderly", "/ˈeldəli/", "пожилой — вежливо о людях", "an elderly patient · elderly people", "Elderly. An elderly patient. Elderly people."],
]
ALONE = [
    ["alone", "/əˈləʊn/", "один, без других — факт", "live alone · travel alone", "Alone. Live alone. Travel alone."],
    ["lonely", "/ˈləʊnli/", "одинокий (грустно); безлюдный", "feel lonely · a lonely place", "Lonely. Feel lonely. A lonely place."],
    ["single", "/ˈsɪŋɡl/", "одиночный, один", "a single parent · a single room", "Single. A single parent. A single room."],
    ["only", "/ˈəʊnli/", "единственный", "an only child · the only way", "Only. An only child. The only way."],
    ["sole", "/səʊl/", "единственный из всех — книжн.", "the sole survivor · the sole reason", "Sole. The sole survivor. The sole reason."],
    ["solitary", "/ˈsɒlɪtri/", "одиночный, стоящий особняком", "a solitary figure · a solitary nodule", "Solitary. A solitary figure. A solitary nodule."],
    ["unique", "/juːˈniːk/", "единственный в своём роде", "a unique occasion · a unique case", "Unique. A unique occasion. A unique case."],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["He [lives alone].", "живёт один — факт"], ["He [feels lonely].", "ему одиноко — чувство"]],
    [["We [won the match].", "выиграли матч — что"], ["We [beat them] 3–1.", "обыграли их — кого"]],
    [["[Take] an umbrella.", "возьми с собой"], ["I always [carry] an umbrella.", "всегда ношу с собой"], ["She [wears] glasses.", "носит очки"]],
    [["[Finish] the course of antibiotics.", "пропейте курс до конца"], ["They [ended] the trial early.", "прекратили исследование досрочно"]],
    [["He [injured] his back.", "травмировал спину"], ["The stroke [damaged] his brain.", "инсульт повредил мозг"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["My car didn't begin.", "My car didn't start.", "машины и моторы — start"],
    ["a big number of patients", "a large number of patients", "число, количество — large"],
    ["We won them 3–1.", "We beat them 3–1.", "выиграть у кого-то — beat"],
    ["He wins 3,000 a month.", "He earns 3,000 a month.", "зарплата — earn"],
    ["I passed three days in Paris.", "I spent three days in Paris.", "проводить время — spend"],
    ["I used a lot on petrol.", "I spent a lot on petrol.", "тратить деньги — spend on"],
    ["She carries glasses.", "She wears glasses.", "носить очки — wear"],
    ["Three people were damaged.", "Three people were injured.", "людей — injure"],
    ["She lives lonely.", "She lives alone.", "жить одному — live alone"],
    ["They grow three children.", "They're raising three children.", "растить детей — raise"],
]

TOPICS = [
    {"n": 1, "group": "u10", "title": "close / shut, start / begin", "sub": "закрыть, начать",
     "rule": "close и shut часто взаимозаменяемы: close или shut the door, close или shut your eyes. Но официально завершить — только close: close the meeting, close the conference. Shut — разговорнее, а Shut your mouth! и Shut up! — грубо. start и begin тоже часто равны, но машины и моторы — только start: start the car, start the engine. Открыть дело — start a business. begin — чуть формальнее: The universe began 13.8 billion years ago.",
     "ex": [
         {"en": "The chair [closed] the conference with a short speech.", "ru": "Председатель закрыл конференцию короткой речью."},
         {"en": "My car wouldn't [start] this morning.", "ru": "Утром машина не завелась."},
         {"en": "[Close] your eyes and don't let me open them.", "ru": "Закройте глаза и не давайте мне их открыть."},
     ]},
    {"n": 2, "group": "u10", "title": "big / large, end / finish", "sub": "большой, закончить",
     "rule": "big — важный, серьёзный: a big decision, a big problem, a big mistake. large — про размер, число и количество: a large size, a large number, a large amount, a large sample. finish — довести начатое до конца: finish your homework, finish the course of antibiotics. end — прекратить, положить конец: end a relationship, end a war; и «закончиться чем-то»: The film ends with a wedding.",
     "ex": [
         {"en": "It's a [big] decision — take your time.", "ru": "Это серьёзное решение — не торопитесь."},
         {"en": "A [large] number of patients were excluded.", "ru": "Большое число пациентов было исключено."},
         {"en": "[Finish] the whole course of antibiotics.", "ru": "Пропейте весь курс антибиотиков."},
     ]},
    {"n": 3, "group": "u10", "title": "old, ancient, antique, elderly", "sub": "старый: четыре слова",
     "rule": "old — самое общее: an old friend (давний), an old building. ancient — древний, тысячи лет: ancient history, ancient Rome. antique — старинный и ценный предмет: antique furniture, an antique clock. elderly — пожилой, вежливо о людях: an elderly patient. В научных статьях сейчас чаще пишут older adults.",
     "ex": [
         {"en": "I met an [old] friend from medical school.", "ru": "Я встретил старого друга по мединституту."},
         {"en": "The shop sells [antique] furniture.", "ru": "В магазине продают старинную мебель."},
         {"en": "[Elderly] patients are at higher risk of falls.", "ru": "У пожилых пациентов выше риск падений."},
     ]},
    {"n": 4, "group": "u10", "title": "alone, lonely, single, only, sole…", "sub": "один, одинокий, единственный",
     "rule": "alone — один, без других, это факт: live alone, travel alone; перед существительным не ставится. lonely — одинокий, когда от этого грустно: feel lonely, a lonely old man; и безлюдный: a lonely place. single — одиночный, один: a single parent, a single room. an only child — единственный ребёнок. sole — единственный из всех: the sole survivor. solitary — одиночный, стоящий особняком: a solitary figure, в медицине — a solitary nodule. unique — единственный в своём роде.",
     "ex": [
         {"en": "He lives [alone] but never feels [lonely].", "ru": "Он живёт один, но никогда не чувствует себя одиноким."},
         {"en": "She's a [single] parent.", "ru": "Она растит ребёнка одна."},
         {"en": "He was the [sole] survivor of the crash.", "ru": "Он единственный выжил в той катастрофе."},
     ]},
    {"n": 5, "group": "u10", "title": "charge / load, injure / damage, grow / raise", "sub": "зарядить, повредить, вырастить",
     "rule": "charge — зарядить аккумулятор, телефон, дефибриллятор. load — загрузить машину, судно, груз; в фармакологии — loading dose, нагрузочная доза. injure — травмировать людей: three people were injured. damage — повредить вещь: a damaged car; и органы, ткани: brain damage, nerve damage. grow — растения: grow crops; в микробиологии — cultures grew E. coli. raise — животных и детей: raise cattle, raise children.",
     "ex": [
         {"en": "[Charge] the defibrillator to 200 joules.", "ru": "Зарядите дефибриллятор на 200 джоулей."},
         {"en": "Three people were [injured] in the crash.", "ru": "В аварии пострадали три человека."},
         {"en": "It's not easy to [raise] children alone.", "ru": "Непросто растить детей в одиночку."},
     ]},
    {"n": 6, "group": "u11", "title": "win, beat, gain", "sub": "выиграть, обыграть, получить",
     "rule": "win — что-то: a match, a prize, a medal, an election, a war. beat — кого-то: beat a team, beat an opponent; defeat — то же, но официальнее. «Выиграть у них» — beat them, не win them. gain — получить что-то абстрактное благодаря усилиям: gain control, gain access, gain experience, gain recognition; и набрать вес — gain weight.",
     "ex": [
         {"en": "We [won] the match 3–1.", "ru": "Мы выиграли матч со счётом 3:1."},
         {"en": "We [beat] them 3–1.", "ru": "Мы обыграли их 3:1."},
         {"en": "She [gained] weight during pregnancy.", "ru": "За беременность она набрала вес."},
     ]},
    {"n": 7, "group": "u11", "title": "earn, make, achieve", "sub": "заработать, получить прибыль, достичь",
     "rule": "earn — заработать трудом: earn a salary, earn money, earn a living. make — получить деньги или прибыль: make a profit, make money, в том числе вложениями, а не только работой. achieve — достичь цели или результата: achieve success, achieve your goals; в медицине — achieve target blood pressure.",
     "ex": [
         {"en": "How much does a nurse [earn]?", "ru": "Сколько зарабатывает медсестра?"},
         {"en": "The clinic [made] a profit last year.", "ru": "В прошлом году клиника получила прибыль."},
         {"en": "We [achieved] the target blood pressure.", "ru": "Мы достигли целевого давления."},
     ]},
    {"n": 8, "group": "u11", "title": "take, carry, wear, use", "sub": "взять, нести, носить, пользоваться",
     "rule": "take — взять с собой: take an umbrella, take warm clothes. carry — нести в руках или иметь при себе: carry a bag, carry a phone. wear — носить на себе одежду, очки, кольцо, маску. use — пользоваться: use a laptop. «Носить очки» — wear, а не carry; «всегда ношу с собой телефон» — carry.",
     "ex": [
         {"en": "[Take] an umbrella — it might rain.", "ru": "Возьми зонт — может пойти дождь."},
         {"en": "I always [carry] my phone.", "ru": "Телефон я всегда ношу с собой."},
         {"en": "Staff must [wear] a mask on the ward.", "ru": "Персонал обязан носить маску в отделении."},
     ]},
    {"n": 9, "group": "u11", "title": "spend", "sub": "проводить время, тратить деньги",
     "rule": "Время и деньги — spend: spend three days in the mountains, spend money on petrol, spend two hours watching TV. Не pass, не use и не stay. После времени — -ing: I spent an hour looking for my keys. Тратить на что-то — spend on.",
     "ex": [
         {"en": "We [spent] three days in the mountains.", "ru": "Мы провели три дня в горах."},
         {"en": "I [spent] an hour looking for my keys.", "ru": "Я час искал ключи."},
         {"en": "How much do you [spend on] food?", "ru": "Сколько вы тратите на еду?"},
     ]},
    {"n": 10, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · close / shut, start / begin
    c("s1-conference", 1, "The chair ___ the conference with a short speech.", "Председатель закрыл конференцию короткой речью.",
      ["closed", "shut"], "closed", "Официально завершить совещание, конференцию — close."),
    c("s1-mouth", 1, "Could you ___ your mouth for a second, please?", "Закройте, пожалуйста, рот на секунду.",
      ["close", "shut"], "close", "Вежливо — close your mouth. Shut your mouth! — грубо, «заткнись»."),
    c("s1-eyes", 1, "___ your eyes and don't let me open them.", "Закройте глаза и не давайте мне их открыть.",
      ["close", "shut"], "close", "Глаза, дверь — close; shut тоже можно, но разговорнее.",
      {"shut": "но звучит разговорнее"}),
    c("s1-car", 1, "It was freezing and my car wouldn't ___.", "Был мороз, и машина не заводилась.",
      ["start", "begin"], "start", "Машины и моторы — только start."),
    c("s1-machine", 1, "Press the green button to ___ the machine.", "Нажмите зелёную кнопку, чтобы запустить аппарат.",
      ["start", "begin"], "start", "Запустить аппарат, двигатель — start."),
    c("s1-clinic", 1, "She ___ her own clinic in 2019.", "В 2019 году она открыла свою клинику.",
      ["started", "began"], "started", "Открыть дело, основать — start: start a business."),
    c("s1-universe", 1, "The universe ___ about 13.8 billion years ago.", "Вселенная возникла около 13,8 млрд лет назад.",
      ["began", "started"], "began", "Формально, абстрактно — begin.",
      {"started": "но в научном тексте лучше began"}),

    # 2 · big / large, end / finish
    c("s2-decision", 2, "It's a ___ decision — take your time.", "Это серьёзное решение — не торопитесь.",
      ["big", "large"], "big", "Важное, серьёзное — big: a big decision."),
    c("s2-problem", 2, "We have a ___ problem with staffing this winter.", "Этой зимой у нас серьёзная проблема с кадрами.",
      ["big", "large"], "big", "Серьёзная проблема — a big problem."),
    c("s2-number", 2, "A ___ number of patients were lost to follow-up.", "Большое число пациентов выбыло из наблюдения.",
      ["large", "big"], "large", "Число, количество — large: a large number."),
    c("s2-amount", 2, "The patient lost a ___ amount of blood.", "Пациент потерял много крови.",
      ["large", "big"], "large", "Количество — a large amount."),
    c("s2-homework", 2, "Have you ___ your homework yet?", "Ты уже сделал домашнее задание?",
      ["finished", "ended"], "finished", "Довести до конца — finish."),
    c("s2-antibiotics", 2, "Make sure you ___ the whole course of antibiotics.", "Обязательно пропейте весь курс антибиотиков.",
      ["finish", "end"], "finish", "Закончить начатое, пройти до конца — finish."),
    c("s2-relationship", 2, "They ___ their relationship after ten years.", "Они расстались после десяти лет вместе.",
      ["ended", "finished"], "ended", "Прекратить, положить конец — end: end a relationship."),
    c("s2-trial", 2, "The trial was ___ early because of safety concerns.", "Исследование прекратили досрочно из-за опасений по безопасности.",
      ["ended", "finished"], "ended", "Прекратить досрочно — end. Finished early — «закончили раньше срока, всё сделав»."),

    # 3 · old, ancient, antique, elderly
    c("s3-friend", 3, "I bumped into an ___ friend from medical school.", "Я случайно встретил старого друга по мединституту.",
      ["old", "ancient", "elderly"], "old", "Давний друг — an old friend. Elderly — пожилой."),
    c("s3-history", 3, "She's interested in ___ history — Egypt, Greece and Rome.", "Она увлекается древней историей — Египет, Греция, Рим.",
      ["ancient", "antique", "old"], "ancient", "Древний, тысячи лет — ancient."),
    c("s3-clock", 3, "They have an ___ clock that belonged to her great-grandmother.", "У них старинные часы, которые принадлежали её прабабушке.",
      ["antique", "ancient", "elderly"], "antique", "Старинная ценная вещь — antique."),
    c("s3-patients", 3, "___ patients are at higher risk of falls.", "У пожилых пациентов выше риск падений.",
      ["elderly", "ancient", "antique"], "elderly", "Пожилой, вежливо — elderly. В статьях сейчас чаще older adults."),
    c("s3-building", 3, "Our hospital is in a very ___ building — it's over 150 years old.", "Наша больница в очень старом здании — ему больше 150 лет.",
      ["old", "ancient", "elderly"], "old", "Просто старое — old. Ancient — тысячи лет."),
    c("s3-lady", 3, "An ___ lady asked me to help her cross the road.", "Пожилая женщина попросила помочь ей перейти дорогу.",
      ["elderly", "antique", "ancient"], "elderly", "О пожилом человеке вежливо — elderly."),

    # 4 · alone, lonely, single, only, sole…
    c("s4-alone", 4, "Since his wife died, he has lived ___.", "С тех пор как умерла жена, он живёт один.",
      ["alone", "lonely", "single"], "alone", "Жить одному — live alone. Lonely — одиноко, грустно."),
    c("s4-place", 4, "It was a ___ place, miles from the nearest village.", "Это было безлюдное место, в нескольких милях от ближайшей деревни.",
      ["lonely", "alone", "single"], "lonely", "Безлюдное место — a lonely place. Alone перед существительным не ставят."),
    c("s4-single", 4, "As a ___ parent, she can't work night shifts.", "Она растит ребёнка одна и не может работать в ночные смены.",
      ["single", "lonely", "alone"], "single", "Родитель-одиночка — a single parent."),
    c("s4-only", 4, "I'm an ___ child — I have no brothers or sisters.", "Я единственный ребёнок: братьев и сестёр у меня нет.",
      ["only", "alone", "single"], "only", "Единственный ребёнок — an only child."),
    c("s4-sole", 4, "He was the ___ survivor of the crash.", "Он единственный выжил в той катастрофе.",
      ["sole", "lonely", "alone"], "sole", "Единственный из всех — sole: the sole survivor."),
    c("s4-solitary", 4, "The CT showed a ___ nodule in the right lung.", "На КТ — одиночный узел в правом лёгком.",
      ["solitary", "lonely", "alone"], "solitary", "Одиночный — solitary: a solitary nodule."),
    c("s4-unique", 4, "Every patient is ___, so treatment has to be individual.", "Каждый пациент уникален, поэтому лечение подбирают индивидуально.",
      ["unique", "single", "only"], "unique", "Единственный в своём роде — unique."),
    c("s4-travel", 4, "I don't like travelling ___ — it's more fun with someone.", "Не люблю путешествовать в одиночку — с кем-то веселее.",
      ["alone", "lonely", "only"], "alone", "В одиночку — alone: travel alone."),

    # 5 · charge / load, injure / damage, grow / raise
    c("s5-phone", 5, "I forgot to ___ my phone last night.", "Я забыл вечером зарядить телефон.",
      ["charge", "load"], "charge", "Зарядить телефон, батарею — charge."),
    c("s5-defib", 5, "___ the defibrillator to 200 joules and stand clear.", "Зарядите дефибриллятор на 200 джоулей и отойдите.",
      ["charge", "load"], "charge", "Дефибриллятор, аккумулятор — charge."),
    c("s5-van", 5, "They ___ the van and drove to their new flat.", "Они загрузили фургон и поехали на новую квартиру.",
      ["loaded", "charged"], "loaded", "Загрузить машину, груз — load."),
    c("s5-loading", 5, "Give a ___ dose of 300 mg, then 75 mg daily.", "Дайте нагрузочную дозу 300 мг, затем по 75 мг в сутки.",
      ["loading", "charging"], "loading", "Нагрузочная доза — loading dose."),
    c("s5-injured", 5, "Three people were ___ in the accident.", "В аварии пострадали три человека.",
      ["injured", "damaged"], "injured", "Люди — injure. Вещи — damage."),
    c("s5-brain", 5, "The stroke ___ the part of her brain that controls speech.", "Инсульт повредил участок мозга, который отвечает за речь.",
      ["damaged", "injured"], "damaged", "Органы и ткани — damage: brain damage, nerve damage."),
    c("s5-plants", 5, "These plants ___ best in the shade.", "Эти растения лучше растут в тени.",
      ["grow", "raise"], "grow", "Растения — grow. Raise — животных и детей."),
    c("s5-cultures", 5, "Blood cultures ___ E. coli.", "В посевах крови выросла кишечная палочка.",
      ["grew", "raised"], "grew", "Посевы, бактерии — grow."),
    c("s5-sheep", 5, "My grandparents ___ sheep and goats in the village.", "Бабушка с дедушкой разводили в деревне овец и коз.",
      ["raised", "grew"], "raised", "Разводить животных — raise."),
    c("s5-children", 5, "It's hard to ___ three children on one salary.", "Трудно растить троих детей на одну зарплату.",
      ["raise", "grow"], "raise", "Растить детей — raise или bring up. Grow children — калька."),

    # 6 · win, beat, gain
    c("s6-medal", 6, "She ___ a gold medal at the Olympics.", "Она выиграла золотую медаль на Олимпиаде.",
      ["won", "gained", "achieved"], "won", "Медаль, приз, награду — win."),
    c("s6-election", 6, "Which party ___ the election?", "Какая партия победила на выборах?",
      ["won", "beat", "gained"], "won", "Выборы, войну, битву — win."),
    c("s6-beat", 6, "We ___ them 3–1 in the final.", "Мы обыграли их 3:1 в финале.",
      ["beat", "won", "gained"], "beat", "Обыграть кого-то — beat. Win — только что-то: win a match."),
    c("s6-match", 6, "We ___ the match 3–1.", "Мы выиграли матч 3:1.",
      ["won", "beat"], "won", "Матч — win. Соперника — beat."),
    c("s6-defeat", 6, "He ___ the defending champion in the final.", "В финале он победил действующего чемпиона.",
      ["defeated", "won"], "defeated", "Победить соперника — defeat или проще beat."),
    c("s6-access", 6, "Hackers ___ access to patient records.", "Хакеры получили доступ к историям болезни.",
      ["gained", "won", "earned"], "gained", "Получить доступ, контроль — gain."),
    c("s6-weight", 6, "She ___ ten kilos during pregnancy.", "За беременность она набрала десять килограммов.",
      ["gained", "won", "earned"], "gained", "Набрать вес — gain weight или put on weight."),
    c("s6-experience", 6, "You'll ___ a lot of experience in the ICU.", "В реанимации вы наберётесь опыта.",
      ["gain", "win", "earn"], "gain", "Набраться опыта — gain experience."),

    # 7 · earn, make, achieve
    c("s7-salary", 7, "How much does a junior doctor ___ in the UK?", "Сколько зарабатывает молодой врач в Великобритании?",
      ["earn", "win", "gain"], "earn", "Зарабатывать трудом — earn."),
    c("s7-extra", 7, "Many students ___ extra money by working at weekends.", "Многие студенты подрабатывают по выходным.",
      ["earn", "win", "gain"], "earn", "Заработать — earn money."),
    c("s7-profit", 7, "The clinic ___ a profit for the first time last year.", "В прошлом году клиника впервые получила прибыль.",
      ["made", "won", "did"], "made", "Получить прибыль — make a profit."),
    c("s7-success", 7, "It's hard to ___ success without hard work.", "Без упорного труда трудно добиться успеха.",
      ["achieve", "win", "make"], "achieve", "Добиться успеха — achieve success."),
    c("s7-goals", 7, "Set small goals — they're easier to ___.", "Ставьте небольшие цели — их проще достичь.",
      ["achieve", "win", "earn"], "achieve", "Достичь цели — achieve."),
    c("s7-target", 7, "We ___ the target blood pressure within a week.", "За неделю мы достигли целевого давления.",
      ["achieved", "won", "gained"], "achieved", "Достичь целевого показателя — achieve."),

    # 8 · take, carry, wear, use
    c("s8-umbrella", 8, "Don't forget to ___ an umbrella — it might rain later.", "Не забудь взять зонт — позже может пойти дождь.",
      ["take", "carry", "wear"], "take", "Взять с собой — take. Carry — нести, держать при себе."),
    c("s8-pocket", 8, "I always ___ my phone in my pocket.", "Телефон я всегда ношу в кармане.",
      ["carry", "wear", "take"], "carry", "Иметь при себе — carry."),
    c("s8-tray", 8, "The nurse ___ the tray carefully so as not to spill anything.", "Сестра осторожно несла поднос, чтобы ничего не пролить.",
      ["carried", "wore", "used"], "carried", "Нести в руках — carry."),
    c("s8-glasses", 8, "She has ___ glasses since she was a child.", "Она носит очки с детства.",
      ["worn", "carried", "taken"], "worn", "Носить очки, одежду — wear, worn."),
    c("s8-mask", 8, "Staff must ___ a mask on the ward.", "Персонал обязан носить маску в отделении.",
      ["wear", "carry", "put"], "wear", "Носить маску — wear. Надеть — put on."),
    c("s8-laptop", 8, "Can I ___ your laptop to check my email?", "Можно воспользоваться твоим ноутбуком, чтобы проверить почту?",
      ["use", "wear", "carry"], "use", "Пользоваться — use."),
    c("s8-ring", 8, "He doesn't ___ his wedding ring at work.", "На работе он не носит обручальное кольцо.",
      ["wear", "carry", "take"], "wear", "Кольцо, часы, украшения — wear."),

    # 9 · spend
    c("s9-days", 9, "We ___ three days in the mountains.", "Мы провели три дня в горах.",
      ["spent", "passed"], "spent", "Проводить время — spend. Passed — калька."),
    c("s9-petrol", 9, "If you buy a bigger car, you'll ___ more on petrol.", "Купишь машину побольше — будешь больше тратить на бензин.",
      ["spend", "use", "pay"], "spend", "Тратить деньги на — spend on."),
    c("s9-tv", 9, "Last night I ___ two hours watching TV.", "Вчера вечером я два часа смотрел телевизор.",
      ["spent", "stayed", "passed"], "spent", "Провести время за чем-то — spend + время + -ing."),
    c("s9-ing", 9, "I spent an hour ___ for my keys.", "Я час искал ключи.",
      ["looking", "to look", "look"], "looking", "spend + время + -ing: spent an hour looking."),
    c("s9-on", 9, "How much do you spend ___ food every month?", "Сколько вы тратите на еду в месяц?",
      ["on", "for", "to"], "on", "Тратить на — spend on."),
    c("s9-ward", 9, "Patients ___ an average of 12 days on the stroke unit.", "В среднем пациенты проводят в инсультном отделении 12 дней.",
      ["spend", "pass", "use"], "spend", "Проводить время где-то — spend."),
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
