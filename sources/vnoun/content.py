# Содержание тренажёра «Recycle → recycling» — существительное из глагола (словообразование).
# Начало — карточки урока: recycle → recycling, waste → waste, destroy → destruction, exist → existence,
# solve → solution, reduce → reduction, support → support, suffer → suffering. Дальше — похожие: суффиксы -ing, -ion,
# -ance/-ence, -ment, -al, -ure, -y, -th и ловушки написания. Отличие от «Advice и advise» (nverb): там пары, которые
# различаются буквой, звуком или ударением, и одна тема про -ment и -ion; здесь — вся система суффиксов.
# Разметка в примерах: [слово|a] — существительное (оранжевый), [слово|b] — глагол (синий), [слово|c] — прилагательное (зелёный).
# Темы с полем late вступают в общую тренировку позже.

MIXED_TOPIC = 9

GROUPS = {
    "b1": "B1 — то же слово, -ing, -ion",
    "b1p": "B1+ — корень меняется, -ence, -ment",
    "b2": "B2 — -al, -ure и ловушки написания",
    "mix": "Итог",
}

# Главная таблица: образец | правило («главное — пояснение») | пары
TABLE = [
    ["waste → waste", "то же слово — существительное узнают по a, the, of", "waste · support · damage · harm"],
    ["recycle → recycling", "-ing — процесс, занятие; обычно без a", "recycling · suffering · screening · findings"],
    ["pollute → pollution", "-ion — к глаголам на -ate, -ct, -ent, -ute", "pollution · protection · prevention · emission"],
    ["solve → solution", "корень меняется — запоминать парой", "solution · destruction · reduction · consumption"],
    ["exist → existence", "-ence или -ance — подскажет прилагательное", "existence · difference · resistance · appearance"],
    ["develop → development", "-ment — к глаголу без изменений", "development · management · assessment · argument"],
    ["arrive → arrival", "-al, -ure, -y, -th — реже, но в медицине часто", "arrival · survival · failure · exposure · injury · growth"],
    ["maintain → maintenance", "ловушки — написание меняется", "maintenance · pronunciation · explanation · repetition"],
]

# Пары с карточек урока: строки [английский, перевод]
CONTRAST = [
    [["We [recycle|b] paper and glass.", "сдаём в переработку — глагол"],
     ["[Recycling|a] saves energy.", "переработка — существительное"]],
    [["Don't [waste|b] water.", "не тратьте зря — глагол"],
     ["Hospitals produce tonnes of [waste|a].", "отходы — то же слово"]],
    [["Fires [destroy|b] the rainforest.", "уничтожают"],
     ["The [destruction|a] is visible from space.", "уничтожение"]],
    [["Do these species still [exist|b]?", "существуют"],
     ["Their [existence|a] is under threat.", "существование — через e"]],
    [["Can we [solve|b] this problem?", "решить"],
     ["There's no easy [solution|a].", "решение"]],
    [["Statins [reduce|b] the risk.", "снижают"],
     ["We saw a 25% [reduction|a] in strokes.", "снижение"]],
    [["Our volunteers [support|b] the project.", "поддерживают"],
     ["Thank you for your [support|a].", "поддержка — то же слово"]],
    [["Many patients [suffer|b] in silence.", "страдают"],
     ["We can ease their [suffering|a].", "страдания"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["the existance of life", "the existence of life", "existent → existence, через e"],
    ["the destroyment of forests", "the destruction of forests", "уничтожение — destruction"],
    ["a solve of the problem", "a solution to the problem", "решение — solution, предлог to"],
    ["plastic recycle", "plastic recycling", "переработка — recycling"],
    ["a 20% reduce", "a 20% reduction", "снижение — reduction"],
    ["Thank you for your supporting.", "Thank you for your support.", "поддержка — support"],
    ["Don't waist time.", "Don't waste time.", "waist — талия, звучит так же"],
    ["to reduce the patient's suffer", "to reduce the patient's suffering", "страдания — suffering"],
    ["regular maintainance", "regular maintenance", "maintain → maintenance"],
    ["her pronounciation", "her pronunciation", "без o: nun, не noun"],
]

TOPICS = [
    {"n": 1, "group": "b1", "title": "waste и support", "sub": "то же слово — существительное",
     "rule": "Многие глаголы и существительные пишутся одинаково: waste — тратить впустую и отходы, support — поддерживать и поддержка, damage — повреждать и повреждение, harm — вредить и вред; так же change, use, cause, care. Различает их только место в предложении: после a, the, your, of и в роли подлежащего — существительное; после to, can, will, don't — глагол. Многие из них неисчисляемые: much waste, some support, damage to — без a и без -s. A waste of time — пустая трата времени; waist — талия, звучит так же.",
     "ex": [
         {"en": "Don't [waste|b] water — we produce too much [waste|a] already.", "ru": "Не тратьте воду зря — отходов и так слишком много."},
         {"en": "Thank you for your [support|a]. We'll [support|b] you all the way.", "ru": "Спасибо за поддержку. Мы будем поддерживать вас до конца."},
         {"en": "Smoking [damages|b] blood vessels, and the [damage|a] can be permanent.", "ru": "Курение повреждает сосуды, и повреждения бывают необратимыми."},
     ]},
    {"n": 2, "group": "b1", "title": "recycling и suffering", "sub": "-ing — процесс, занятие",
     "rule": "-ing превращает глагол в существительное-процесс: recycle — recycling (переработка), suffer — suffering (страдания), screen — screening (скрининг), fund — funding (финансирование), bleed — bleeding (кровотечение). Обычно такие слова неисчисляемые и идут без a: plastic recycling, early screening. Есть и исчисляемые: a meeting, a warning, a building; результаты исследования — findings. Слов recyclement или «the suffer» нет.",
     "ex": [
         {"en": "We [recycle|b] paper, and [recycling|a] saves trees.", "ru": "Мы сдаём бумагу в переработку — это сберегает деревья."},
         {"en": "Many patients [suffer|b] in silence; we can ease their [suffering|a].", "ru": "Многие пациенты страдают молча — мы можем облегчить их страдания."},
         {"en": "The [findings|a] support early [screening|a].", "ru": "Результаты исследования говорят в пользу раннего скрининга."},
     ]},
    {"n": 3, "group": "b1", "title": "pollution и protection", "sub": "-ion — самый частый суффикс",
     "rule": "Глаголы на -ate, -ct, -ent, -ute получают -ion почти без изменений: educate — education, protect — protection, prevent — prevention, pollute — pollution. К -ve и -ne прибавляют -ation: conserve — conservation, combine — combination. В коротких глаголах на -mit t превращается в ss: emit — emission, admit — admission, permit — permission. Не путайте: pollution — загрязнение, pollutant — загрязняющее вещество, polluter — тот, кто загрязняет.",
     "ex": [
         {"en": "Factories [pollute|b] rivers, and [pollution|a] kills fish.", "ru": "Заводы загрязняют реки, и от загрязнения гибнет рыба."},
         {"en": "[Prevention|a] is better than cure.", "ru": "Предупредить легче, чем лечить."},
         {"en": "Cars [emit|b] CO₂, so we must cut [emissions|a].", "ru": "Машины выбрасывают CO₂ — выбросы нужно сокращать."},
     ]},
    {"n": 4, "group": "b1p", "title": "solution и destruction", "sub": "корень меняется — запоминать парой", "late": 0.2,
     "rule": "У части глаголов перед -ion меняется корень — такие пары учат целиком. solve — solution (v → u, как revolve — revolution); destroy — destruction; reduce — reduction, produce — production, introduce — introduction (-duce → -duction); consume — consumption, describe — description (появляется p). Предлоги тоже запоминают сразу: a solution to, a reduction in, the destruction of. Production — процесс, product — то, что произвели.",
     "ex": [
         {"en": "Can we [solve|b] it? There's no easy [solution|a].", "ru": "Можно ли это решить? Простого решения нет."},
         {"en": "Fires [destroy|b] forests; the [destruction|a] is visible from space.", "ru": "Пожары уничтожают леса — разрушения видно из космоса."},
         {"en": "Statins [reduce|b] the risk: a 25% [reduction|a] in strokes.", "ru": "Статины снижают риск: инсультов на 25 % меньше."},
     ]},
    {"n": 5, "group": "b1p", "title": "existence или existance", "sub": "-ence или -ance", "late": 0.25,
     "rule": "-ence и -ance звучат одинаково [əns], поэтому на письме их путают. Подсказка — прилагательное: -ent → -ence, -ant → -ance. existent — existence, different — difference, resistant — resistance, important — importance. На карточке урока опечатка: правильно existence, через e. Если прилагательного нет, слово запоминают: appearance, adherence; у occur — occurrence удваивается r.",
     "ex": [
         {"en": "Do these species still [exist|b]? Their [existence|a] is under threat.", "ru": "Существуют ли ещё эти виды? Их существование под угрозой."},
         {"en": "Bacteria [resist|b] the drug — this is antibiotic [resistance|a].", "ru": "Бактерии не поддаются препарату — это устойчивость к антибиотикам."},
         {"en": "The groups [differ|b] in age, but there's no [difference|a] in outcome.", "ru": "Группы различаются по возрасту, но разницы в исходах нет."},
     ]},
    {"n": 6, "group": "b1p", "title": "development и management", "sub": "-ment — без изменений", "late": 0.25,
     "rule": "-ment прибавляют к глаголу как есть: develop — development, manage — management, assess — assessment, impair — impairment, replace — replacement, require — requirement. Исключение — argue — argument: e выпадает. Многие из этих слов исчисляемые: a requirement, an agreement, an argument. В медицине: pain management, risk assessment, cognitive impairment, hip replacement.",
     "ex": [
         {"en": "Children [develop|b] fast, so early [development|a] matters.", "ru": "Дети развиваются быстро, поэтому раннее развитие так важно."},
         {"en": "We [assess|b] every patient — a full risk [assessment|a].", "ru": "Мы обследуем каждого пациента — полная оценка рисков."},
         {"en": "They [argue|b] that plastic bags should be banned — a strong [argument|a].", "ru": "Они считают, что пакеты нужно запретить, — веский довод."},
     ]},
    {"n": 7, "group": "b2", "title": "arrival, failure, injury, growth", "sub": "-al, -ure, -y, -th", "late": 0.45,
     "rule": "Реже встречаются -al, -ure, -y и -th. -al: arrive — arrival, survive — survival, approve — approval, remove — removal, refuse — refusal. -ure: fail — failure, expose — exposure, press — pressure, close — closure. -y: injure — injury, recover — recovery, discover — discovery, deliver — delivery. -th: grow — growth. В медицине: heart failure, survival rate, exposure to, head injury.",
     "ex": [
         {"en": "Fewer patients [survive|b] without treatment: the [survival|a] rate is 40%.", "ru": "Без лечения выживают меньше: выживаемость — 40 %."},
         {"en": "His kidneys [failed|b] — acute renal [failure|a].", "ru": "Почки отказали — острая почечная недостаточность."},
         {"en": "Don't [expose|b] the scar to the sun: [exposure|a] makes it darker.", "ru": "Не держите шрам на солнце: от загара он темнеет."},
     ]},
    {"n": 8, "group": "b2", "title": "maintenance, pronunciation", "sub": "ловушки написания", "late": 0.5,
     "rule": "В части пар вместе с суффиксом меняется написание — на письме это самые частые ошибки. maintain — maintenance (ai → e), pronounce — pronunciation (o пропадает: nun, а не noun), explain — explanation (ai → a), repeat — repetition (ea → e), compare — comparison, proceed — procedure (ee → e). Меняется и звук: maintain [eɪ], maintenance [ə].",
     "ex": [
         {"en": "We [maintain|b] the equipment; [maintenance|a] is done monthly.", "ru": "Мы обслуживаем оборудование — техобслуживание каждый месяц."},
         {"en": "How do you [pronounce|b] it? Check the [pronunciation|a].", "ru": "Как это произносится? Проверьте произношение."},
         {"en": "Can you [explain|b] the risks? I need a clear [explanation|a].", "ru": "Можете объяснить риски? Мне нужно понятное объяснение."},
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
    # 1 · то же слово
    c("n1-waste", 1, "Hospitals produce tonnes of plastic ___ every year.", "Больницы каждый год производят тонны пластиковых отходов.",
      ["waste", "wasting", "wasted"], "waste", "Отходы — waste, то же слово, что и глагол. Неисчисляемое: much waste, a lot of waste."),
    c("n1-waste-time", 1, "Arguing about it is a ___ of time.", "Спорить об этом — пустая трата времени.",
      ["waste", "waist", "wasting"], "waste", "A waste of time — пустая трата времени. Waist /weɪst/ — талия, звучит так же."),
    c("n1-support", 1, "Thank you for your ___.", "Спасибо за поддержку.",
      ["support", "supporting", "supportive"], "support", "После your — существительное: support. Supportive — прилагательное: поддерживающий."),
    c("n1-support-a", 1, "The project needs more financial ___.", "Проекту нужна дополнительная финансовая поддержка.",
      ["support", "a support", "supports"], "support", "Support неисчисляемое: more support, some support — без a и без -s."),
    c("n1-damage", 1, "Smoking causes serious ___ to blood vessels.", "Курение серьёзно повреждает сосуды.",
      ["damage", "damages", "damaging"], "damage", "Повреждение — damage to, неисчисляемое. Damages — компенсация по суду."),
    c("n1-harm", 1, "The drug did more ___ than good.", "Лекарство принесло больше вреда, чем пользы.",
      ["harm", "harmful", "harming"], "harm", "Вред — harm: do more harm than good. Harmful — вредный, прилагательное."),

    # 2 · -ing
    c("n2-recycling", 2, "Plastic ___ saves energy and raw materials.", "Переработка пластика экономит энергию и сырьё.",
      ["recycling", "recycle", "recyclement"], "recycling", "Переработка — recycling: процесс, -ing. Recyclement — такого слова нет."),
    c("n2-recycled", 2, "Most of this packaging can be ___.", "Большую часть этой упаковки можно переработать.",
      ["recycled", "recycling", "recycle"], "recycled", "Здесь нужен глагол: can be + третья форма — can be recycled."),
    c("n2-suffering", 2, "Palliative care aims to relieve ___.", "Задача паллиативной помощи — облегчить страдания.",
      ["suffering", "suffer", "sufferance"], "suffering", "Страдания — suffering, неисчисляемое. Sufferance — устаревшее «терпимость», не то."),
    c("n2-suffer", 2, "Many patients ___ from chronic pain.", "Многие пациенты страдают от хронической боли.",
      ["suffer", "suffering", "suffers"], "suffer", "Здесь глагол: suffer from — страдать от. Many patients — множественное, без -s."),
    c("n2-screening", 2, "Breast cancer ___ starts at 40.", "Скрининг рака молочной железы начинается с 40 лет.",
      ["screening", "screen", "screened"], "screening", "Скрининг — screening, процесс. A screen — экран; to screen — обследовать."),
    c("n2-findings", 2, "The ___ of the study were published last month.", "Результаты исследования опубликовали в прошлом месяце.",
      ["findings", "finds", "foundings"], "findings", "Результаты исследования — findings (find → finding). Finds — находки археологов."),

    # 3 · -ion
    c("n3-pollution", 3, "Air ___ increases the risk of stroke.", "Загрязнение воздуха повышает риск инсульта.",
      ["pollution", "pollutant", "polluting"], "pollution", "Загрязнение — pollution: pollute + -ion. Pollutant — само загрязняющее вещество."),
    c("n3-pollutant", 3, "PM2.5 is the most dangerous air ___.", "PM2.5 — самый опасный загрязнитель воздуха.",
      ["pollutant", "pollution", "polluter"], "pollutant", "Вещество — pollutant (как coolant, antioxidant). Polluter — тот, кто загрязняет: завод, страна."),
    c("n3-protection", 3, "Sunscreen gives some ___ against UV.", "Солнцезащитный крем частично защищает от ультрафиолета.",
      ["protection", "protect", "protecting"], "protection", "Защита — protection: -ct → -ction. Protection against, from."),
    c("n3-prevention", 3, "___ is better than cure.", "Предупредить легче, чем лечить.",
      ["Prevention", "Preventing", "Prevent"], "Prevention", "Профилактика — prevention: prevent + -ion. Поговорка: Prevention is better than cure."),
    c("n3-conservation", 3, "The charity works in wildlife ___.", "Фонд занимается охраной дикой природы.",
      ["conservation", "conserve", "conservement"], "conservation", "Охрана природы — conservation: -ve → -vation. Глагол — conserve."),
    c("n3-emissions", 3, "The city wants to cut carbon ___ by half.", "Город хочет вдвое сократить выбросы CO₂.",
      ["emissions", "emittions", "emits"], "emissions", "Выбросы — emissions: emit → emission, t → ss. Emittion — ошибка."),

    # 4 · корень меняется
    c("n4-solution", 4, "There's no simple ___ to this problem.", "У этой проблемы нет простого решения.",
      ["solution", "solving", "solve"], "solution", "Решение — solution: v → u. Предлог — to: a solution to the problem."),
    c("n4-destruction", 4, "The fires caused massive ___ of the rainforest.", "Пожары привели к массовому уничтожению тропических лесов.",
      ["destruction", "destroyment", "destroying"], "destruction", "Уничтожение — destruction: destroy → destruct-ion. Destroyment — ошибка."),
    c("n4-reduction", 4, "We saw a 20% ___ in hospital admissions.", "Госпитализаций стало на 20 % меньше.",
      ["reduction", "reduce", "reducement"], "reduction", "Снижение — reduction: -duce → -duction. Предлог — in: a reduction in admissions."),
    c("n4-reduce", 4, "Statins ___ the risk of a second stroke.", "Статины снижают риск повторного инсульта.",
      ["reduce", "reduction", "reducing"], "reduce", "Здесь глагол: statins reduce — снижают. Reduce the risk."),
    c("n4-consumption", 4, "High salt ___ raises blood pressure.", "Избыток соли повышает давление.",
      ["consumption", "consuming", "consumement"], "consumption", "Потребление — consumption: consume → consumption, появляется p. Alcohol consumption."),
    c("n4-production", 4, "___ of plastic has doubled since 2000.", "Производство пластика с 2000 года выросло вдвое.",
      ["Production", "Product", "Produce"], "Production", "Производство — production, процесс. Product — изделие; produce /ˈprɒdjuːs/ — овощи и фрукты."),

    # 5 · -ence или -ance
    c("n5-existence", 5, "Scientists doubt the ___ of life on Mars.", "Учёные сомневаются, что на Марсе есть жизнь.",
      ["existence", "existance", "existing"], "existence", "Существование — existence, через e: existent → existence. Existance — частая ошибка."),
    c("n5-resistance", 5, "Antibiotic ___ is a growing problem.", "Устойчивость к антибиотикам — растущая проблема.",
      ["resistance", "resistence", "resisting"], "resistance", "Устойчивость — resistance, через a: resistant → resistance. Resistance to antibiotics."),
    c("n5-difference", 5, "There was no significant ___ between the groups.", "Значимой разницы между группами не было.",
      ["difference", "differance", "differ"], "difference", "Разница — difference: different → difference. No significant difference — штамп статей."),
    c("n5-appearance", 5, "The sudden ___ of new symptoms needs urgent review.", "Если внезапно появились новые симптомы, нужен срочный осмотр.",
      ["appearance", "appearence", "appearing"], "appearance", "Появление, внешний вид — appearance, через a. Прилагательного нет — запоминать."),
    c("n5-occurrence", 5, "The ___ of side effects was low.", "Побочные эффекты встречались редко.",
      ["occurrence", "occurence", "occurance"], "occurrence", "occur → occurrence: ударение на конце, r удваивается, и -ence."),
    c("n5-adherence", 5, "Poor ___ to treatment often leads to relapse.", "Низкая приверженность лечению часто ведёт к рецидиву.",
      ["adherence", "adherance", "adhering"], "adherence", "Приверженность — adherence to treatment: adhere → adherence. Синоним — compliance."),

    # 6 · -ment
    c("n6-development", 6, "Sustainable ___ means meeting today's needs without harming the future.", "Устойчивое развитие — это когда нынешние нужды удовлетворяют, не вредя будущему.",
      ["development", "developing", "develop"], "development", "Развитие — development: develop + -ment, без изменений."),
    c("n6-management", 6, "Pain ___ is part of every ward round.", "Обезболивание обсуждают на каждом обходе.",
      ["management", "managing", "manage"], "management", "Ведение, лечение — management: pain management, waste management."),
    c("n6-assessment", 6, "A full risk ___ is needed before discharge.", "Перед выпиской нужна полная оценка рисков.",
      ["assessment", "assessing", "assess"], "assessment", "Оценка — assessment: assess + -ment, ss сохраняется."),
    c("n6-impairment", 6, "He has mild cognitive ___.", "У него лёгкое когнитивное расстройство.",
      ["impairment", "impairing", "impair"], "impairment", "Нарушение функции — impairment: mild cognitive impairment, hearing impairment."),
    c("n6-argument", 6, "There's a strong ___ for banning plastic bags.", "Есть веский довод за запрет пластиковых пакетов.",
      ["argument", "arguement", "arguing"], "argument", "argue → argument: e выпадает. Arguement — ошибка. Argument for, against."),
    c("n6-replacement", 6, "She's on the waiting list for a hip ___.", "Она стоит в очереди на эндопротезирование тазобедренного сустава.",
      ["replacement", "replacing", "replace"], "replacement", "Замена — replacement: hip replacement, hormone replacement therapy."),

    # 7 · -al, -ure, -y, -th
    c("n7-arrival", 7, "Estimated time of ___: 10:40.", "Ожидаемое время прибытия — 10:40.",
      ["arrival", "arriving", "arrive"], "arrival", "Прибытие — arrival: arrive + -al. ETA — estimated time of arrival."),
    c("n7-survival", 7, "The five-year ___ rate is about 90%.", "Пятилетняя выживаемость — около 90 %.",
      ["survival", "surviving", "survive"], "survival", "Выживаемость — survival rate: survive + -al."),
    c("n7-failure", 7, "He was admitted with acute heart ___.", "Его госпитализировали с острой сердечной недостаточностью.",
      ["failure", "fail", "failing"], "failure", "Недостаточность — failure: heart failure, renal failure. fail + -ure."),
    c("n7-exposure", 7, "Long-term ___ to noise damages hearing.", "Длительное воздействие шума повреждает слух.",
      ["exposure", "exposing", "exposition"], "exposure", "Воздействие — exposure to: expose → exposure. Exposition — выставка, изложение."),
    c("n7-injury", 7, "He suffered a serious head ___.", "Он получил тяжёлую травму головы.",
      ["injury", "injure", "injuring"], "injury", "Травма — injury: injure → injury. Head injury, injury to the knee."),
    c("n7-growth", 7, "Population ___ puts pressure on water supplies.", "Рост населения увеличивает нагрузку на водоснабжение.",
      ["growth", "grow", "growing"], "growth", "Рост — growth: grow + -th. Economic growth, growth rate."),

    # 8 · ловушки написания
    c("n8-maintenance", 8, "The ventilator needs regular ___.", "Аппарату ИВЛ нужно регулярное техобслуживание.",
      ["maintenance", "maintainance", "maintaining"], "maintenance", "maintain → maintenance: ai превращается в e. Maintainance — ошибка."),
    c("n8-pronunciation", 8, "Her ___ is very clear.", "У неё очень чёткое произношение.",
      ["pronunciation", "pronounciation", "pronouncing"], "pronunciation", "pronounce → pronunciation: o пропадает — nun, а не noun."),
    c("n8-explanation", 8, "The doctor gave a clear ___ of the risks.", "Врач понятно объяснил риски.",
      ["explanation", "explaination", "explaining"], "explanation", "explain → explanation: ai → a. Explaination — ошибка."),
    c("n8-repetition", 8, "Spaced ___ helps you remember new words.", "Интервальное повторение помогает запоминать новые слова.",
      ["repetition", "repeatition", "repeating"], "repetition", "repeat → repetition: ea → e, и -ition."),
    c("n8-comparison", 8, "In ___ with last year, admissions fell.", "По сравнению с прошлым годом госпитализаций стало меньше.",
      ["comparison", "comparation", "comparing"], "comparison", "compare → comparison: -ison. In comparison with, to."),
    c("n8-procedure", 8, "The ___ takes about an hour.", "Процедура длится около часа.",
      ["procedure", "proceedure", "proceeding"], "procedure", "proceed → procedure: ee → e. Proceedings — протоколы, материалы конференции."),
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
