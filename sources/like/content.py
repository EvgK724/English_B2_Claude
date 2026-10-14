# Содержание тренажёра «Like и look like»: What's she like? (какая), What does she look like? (как выглядит),
# What does she like? (что любит); look tired и look like a doctor; I'd like и I like; like doing и feel like doing;
# like или as; like, as if + предложение; such as, -like, likely, alike, unlike.
# Отличие от соседей: «Похожие слова» (similar) — see, look, watch; «To или -ing» (toing) и «Would» — по одной карточке
# на like doing и would like; здесь — всё о like вместе. Примеры — из жизни и из больницы.
# Разметка в примерах: [слово|a] — like «как, похож» (оранжевый), [слово|b] — like «нравится» (синий),
# [слово|c] — прилагательное или as (зелёный). Реплики «— …? — …» озвучивают два голоса.
# Темы с полем late вступают в общую тренировку позже.

MIXED_TOPIC = 9

GROUPS = {
    "b1": "B1 — What's it like, look like, would like",
    "b1p": "B1+ — feel like, like или as",
    "b2": "B2 — as if, such as, likely",
    "mix": "Итог",
}

# Главная таблица: образец | правило («главное — пояснение») | примеры
TABLE = [
    ["What's she like?", "характер, впечатление — be … like", "What's she like? · What was the trip like?"],
    ["What does she look like?", "внешность, сходство — look like", "looks like her mum · looks like a bruise"],
    ["What does she like?", "вкусы — like-глагол", "likes jazz · likes swimming"],
    ["look tired · look like a doctor", "без like — прилагательное, с like — существительное", "sounds great · sounds like a plan"],
    ["I'd like · I like", "хочу сейчас — would like, люблю вообще — like", "I'd like a coffee · I like coffee"],
    ["feel like doing", "хочется — feel like + -ing", "don't feel like cooking · feel like a walk"],
    ["as a nurse · like a nurse", "роль, профессия — as, сходство — like", "works as a nurse · talks like a doctor"],
    ["as if · such as · likely", "как будто, например, вероятно", "as if he knew · such as aspirin · likely to recover"],
]

# Мини-диалоги: строки [английский, перевод]; реплики начинаются с «— » — их говорят два голоса
CONTRAST = [
    [["— What's your new boss [like|a]?", "Какой у тебя новый начальник? — характер"],
     ["— She's strict but fair.", "Строгая, но справедливая."]],
    [["— What does she [look like|a]?", "Как она выглядит? — внешность"],
     ["— She's tall, with short dark hair.", "Высокая, с короткими тёмными волосами."]],
    [["— What does she [like|b]?", "Что она любит? — вкусы"],
     ["— She [likes|b] jazz and long walks.", "Любит джаз и долгие прогулки."]],
    [["— [Would you like|b] some tea?", "Хотите чаю? — предложение сейчас"],
     ["— Yes, please. I'd love some.", "Да, с удовольствием."]],
    [["— What's the pain [like|a]?", "Какая боль? — просьба описать"],
     ["— It [feels like|a] a tight band around my head.", "Как будто голову стянули обручем."]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["How does she look like?", "What does she look like?", "внешность — What … look like"],
    ["What is he look like?", "What does he look like?", "look — глагол, нужен does"],
    ["You look like tired.", "You look tired.", "после look — прилагательное без like"],
    ["It sounds a good idea.", "It sounds like a good idea.", "перед существительным — like"],
    ["I like a coffee, please.", "I'd like a coffee, please.", "просьба сейчас — would like"],
    ["I don't feel like to go out.", "I don't feel like going out.", "feel like + -ing"],
    ["She works like a nurse.", "She works as a nurse.", "профессия, роль — as"],
    ["How was the weather like?", "What was the weather like?", "What … like? или How was …?"],
    ["It looks like as if it'll rain.", "It looks like it's going to rain.", "like или as if — не вместе"],
    ["He is likely recover.", "He is likely to recover.", "be likely to do"],
]

TOPICS = [
    {"n": 1, "group": "b1", "title": "What's she like?", "sub": "характер и впечатление",
     "rule": "What + be + … + like? — просьба описать: какой он, как там. Отвечают прилагательными, без like: What's your new boss like? — She's strict but fair. What was the conference like? — Interesting, but far too long. What's the weather like? — Cold and windy. Частая ошибка — How is she like? Нужно либо What's she like? (какая она), либо How is she? (как она себя чувствует). How was the trip? и What was the trip like? — почти одно и то же.",
     "ex": [
         {"en": "— What's your new boss [like|a]? — She's strict but fair.", "ru": "— Какой у тебя новый начальник? — Строгая, но справедливая."},
         {"en": "— What was the conference [like|a]? — Interesting, but far too long.", "ru": "— Как прошла конференция? — Интересно, но слишком долго."},
         {"en": "— How is your mother? — Much better, thanks.", "ru": "— Как мама? — Гораздо лучше, спасибо."},
     ]},
    {"n": 2, "group": "b1", "title": "What does she look like?", "sub": "внешность и сходство",
     "rule": "Look like — «выглядит как, похож на», после него существительное. What does she look like? — вопрос о внешности: She's tall, with dark hair. She looks like her mother — похожа на маму. The rash looks like an allergic reaction — сыпь похожа на аллергию. В вопросе нужен does, а look — без -s: What does he look like? How does he look like — ошибка; How does he look? — как он выглядит (усталым, хорошо). Похож характером — be like: He's like his father.",
     "ex": [
         {"en": "— What does your brother [look like|a]? — He's tall and thin, with glasses.", "ru": "— Как выглядит твой брат? — Высокий, худой, в очках."},
         {"en": "She [looks like|a] her mother, but she's [like|a] her father.", "ru": "Внешне она в маму, а характером в папу."},
         {"en": "The rash [looks like|a] an allergic reaction.", "ru": "Сыпь похожа на аллергическую реакцию."},
     ]},
    {"n": 3, "group": "b1", "title": "look tired или look like a doctor", "sub": "прилагательное — без like",
     "rule": "После look, sound, feel, taste, smell ставят прилагательное — без like: You look tired. That sounds great. I feel sick. Перед существительным нужен like: You look like a doctor. That sounds like a plan. It feels like a cramp. Ошибки: look like tired, it sounds a good idea. На приёме: What does the pain feel like? — It feels sharp. / It feels like pressure.",
     "ex": [
         {"en": "That [sounds great|c] — it [sounds like|a] a plan.", "ru": "Звучит отлично — договорились."},
         {"en": "The pain [feels sharp|c], like a knife.", "ru": "Боль острая, как ножом."},
         {"en": "This milk [smells sour|c] — it [smells like|a] cheese.", "ru": "Молоко кисло пахнет — как сыр."},
     ]},
    {"n": 4, "group": "b1", "title": "I'd like или I like", "sub": "хочу сейчас или люблю вообще",
     "rule": "I like — люблю, нравится вообще: I like coffee, I like working with people. I'd like (= I would like) — хочу сейчас, вежливая просьба: I'd like a coffee, please. I'd like to make an appointment. Предложение — Would you like…?: Would you like some tea? Would you like to sit down? Do you like…? — вопрос о вкусах. После would like — to do; I'd like you to… — я хочу, чтобы вы…",
     "ex": [
         {"en": "I [like|b] coffee, but right now I'd [like|b] a glass of water.", "ru": "Я люблю кофе, но сейчас хочу стакан воды."},
         {"en": "— [Would you like|b] to sit down? — Yes, thank you.", "ru": "— Не хотите присесть? — Да, спасибо."},
         {"en": "I'd [like|b] to make an appointment with Dr Smith.", "ru": "Я бы хотел записаться к доктору Смиту."},
     ]},
    {"n": 5, "group": "b1p", "title": "like doing и feel like doing", "sub": "любить делать и хотеться", "late": 0.2,
     "rule": "Like + -ing — нравится занятие: I like swimming. Like + to do — привычка, «считаю правильным»: I like to check the results myself. Разница небольшая, обе формы верны. Feel like + -ing или существительное — хочется: I don't feel like cooking tonight. Do you feel like a walk? Feel like to do — ошибка. Would like — всегда + to do: Would you like to come?",
     "ex": [
         {"en": "I [like|b] swimming, but I don't [feel like|a] going today.", "ru": "Я люблю плавать, но сегодня не хочется."},
         {"en": "I [like|b] to check the results myself.", "ru": "Я предпочитаю сам проверять результаты."},
         {"en": "— Do you [feel like|a] a walk? — Not really, I'm exhausted.", "ru": "— Хочешь прогуляться? — Не особо, я вымотан."},
     ]},
    {"n": 6, "group": "b1p", "title": "like или as", "sub": "похоже или в роли", "late": 0.25,
     "rule": "Like + существительное — сходство, «как, подобно»: He sings like a professional (но он не профессионал). As + существительное — роль, профессия, функция: She works as a nurse. We use this room as an office. As your doctor, I… — я и есть ваш врач; Like a doctor, he checked my pulse — он не врач. Устойчиво: as usual, as I said, as you know; like I said — разговорное.",
     "ex": [
         {"en": "She works [as|c] a nurse, but she talks [like|a] a doctor.", "ru": "Она работает медсестрой, а говорит как врач."},
         {"en": "[As|c] your doctor, I strongly advise you to stop smoking.", "ru": "Как ваш врач, настоятельно советую бросить курить."},
         {"en": "He treats the clinic [like|a] his own home.", "ru": "Он обращается с клиникой как со своим домом."},
     ]},
    {"n": 7, "group": "b2", "title": "It looks like it's going to rain", "sub": "like и as if + предложение", "late": 0.45,
     "rule": "Look like, seem like, sound like + целое предложение — «похоже, что; как будто»: It looks like it's going to rain. It sounds like you need a break. Это разговорный стиль; в письме и аккуратной речи — as if или as though: It looks as if the patient has fallen asleep. Нереальное «как будто» — прошедшее: He talks as if he knew everything (на самом деле не знает); She acts as if she were the boss. Like и as if вместе — ошибка.",
     "ex": [
         {"en": "It [looks like|a] it's going to rain.", "ru": "Похоже, сейчас пойдёт дождь."},
         {"en": "It [sounds like|a] you need a break.", "ru": "Похоже, тебе нужен отдых."},
         {"en": "He talks [as if|a] he knew everything.", "ru": "Он говорит так, будто всё знает."},
     ]},
    {"n": 8, "group": "b2", "title": "such as, flu-like, likely, alike", "sub": "слова с like", "late": 0.5,
     "rule": "Such as — «например, такие как» перед списком: drugs such as aspirin and clopidogrel; в статьях — such as, в разговоре — like. -like — «похожий на»: flu-like symptoms, lifelike. Likely — вероятный: He is likely to recover — скорее всего поправится. Alike — одинаковые, после глагола: The twins look alike. Unlike — в отличие от: Unlike aspirin, paracetamol doesn't thin the blood. Dislike — не любить: I dislike flying.",
     "ex": [
         {"en": "Avoid painkillers [such as|c] ibuprofen.", "ru": "Избегайте обезболивающих вроде ибупрофена."},
         {"en": "He has [flu-like|c] symptoms.", "ru": "У него гриппоподобные симптомы."},
         {"en": "[Unlike|a] aspirin, paracetamol doesn't thin the blood.", "ru": "В отличие от аспирина, парацетамол не разжижает кровь."},
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
    # 1 · What's she like?
    c("l1-boss", 1, "What's your new boss ___?", "Какой у тебя новый начальник?",
      ["like", "look like", "likes"], "like", "Характер — What's … like? Look like — о внешности."),
    c("l1-how", 1, "___ was the conference like?", "Как прошла конференция?",
      ["What", "How"], "What", "What … like? How … like — ошибка. Можно и без like: How was the conference?"),
    c("l1-weather", 1, "What's the weather ___ in Yekaterinburg in winter?", "Какая погода в Екатеринбурге зимой?",
      ["like", "look like", "as"], "like", "Описание — What's the weather like?"),
    c("l1-answer", 1, "— What's she like? — ___", "— Какая она?",
      ["She's very kind.", "She likes music.", "She looks like her mum."], "She's very kind.",
      "What's she like? — о характере: kind, quiet, funny. She likes music — ответ на What does she like?"),
    c("l1-howis", 1, "— ___ is your mother? — Much better, thanks.", "— Как мама? — Гораздо лучше, спасибо.",
      ["How", "What"], "How", "О самочувствии — How is she? What is she like? — о характере."),
    c("l1-nights", 1, "What's it ___ working night shifts?", "Каково это — работать в ночные смены?",
      ["like", "look like", "as"], "like", "What's it like + -ing — каково это: What's it like working nights?"),

    # 2 · What does she look like?
    c("l2-appearance", 2, "— What does he ___? — He's tall, with short grey hair.", "— Как он выглядит? — Высокий, с короткими седыми волосами.",
      ["look like", "like", "looks like"], "look like", "Внешность — What does he look like? После does — look без -s."),
    c("l2-mother", 2, "She ___ her mother — the same eyes and the same smile.", "Она похожа на маму: те же глаза, та же улыбка.",
      ["looks like", "is like", "likes"], "looks like", "Внешнее сходство — look like. Be like — похожи характером."),
    c("l2-what", 2, "___ does she look like?", "Как она выглядит?",
      ["What", "How"], "What", "What does she look like? How does she look like — ошибка; How does she look? — как она выглядит (усталой, хорошо)."),
    c("l2-rash", 2, "This rash ___ an allergic reaction.", "Эта сыпь похожа на аллергическую реакцию.",
      ["looks like", "looks", "is looking"], "looks like", "Перед существительным — looks like."),
    c("l2-father", 2, "He's very calm — he's ___ his father.", "Он очень спокойный — весь в отца.",
      ["like", "look like", "likes"], "like", "Характер — be like: he's like his father. Look like — внешне."),
    c("l2-flat", 2, "— What does your new flat look like? — ___", "— Как выглядит твоя новая квартира?",
      ["It's small but bright.", "I like it a lot.", "It's like I said."], "It's small but bright.",
      "Look like — как выглядит: маленькая, но светлая. I like it — ответ на Do you like it?"),

    # 3 · look tired или look like a doctor
    c("l3-tired", 3, "You look ___. Did you sleep at all?", "Ты выглядишь усталым. Ты вообще спал?",
      ["tired", "like tired", "tiredly"], "tired", "После look — прилагательное, без like."),
    c("l3-plan", 3, "Meet at eight? That ___ a plan.", "Встречаемся в восемь? Договорились.",
      ["sounds like", "sounds", "sounds as"], "sounds like", "Перед существительным — sounds like: That sounds like a plan — договорились."),
    c("l3-great", 3, "Your new job sounds ___!", "Твоя новая работа — звучит здорово!",
      ["great", "like great", "greatly"], "great", "Sound + прилагательное: sounds great."),
    c("l3-pain", 3, "— What does the pain feel like? — It ___ a tight band.", "— На что похожа боль? — Как будто стягивает обручем.",
      ["feels like", "feels", "is feeling like"], "feels like", "Перед существительным — feels like."),
    c("l3-sick", 3, "I feel ___ — I think I ate something bad.", "Меня тошнит — наверное, съел что-то не то.",
      ["sick", "like sick", "sickly"], "sick", "Feel + прилагательное: feel sick — тошнит. Sickly — болезненный, хилый."),
    c("l3-smell", 3, "This room ___ a hospital.", "В этой комнате пахнет больницей.",
      ["smells like", "smells", "smells as"], "smells like", "Перед существительным — smells like."),

    # 4 · I'd like или I like
    c("l4-coffee", 4, "___ a black coffee, please.", "Мне чёрный кофе, пожалуйста.",
      ["I'd like", "I like", "I'm liking"], "I'd like", "Просьба сейчас — I'd like. I like coffee — люблю кофе вообще."),
    c("l4-jazz", 4, "I ___ jazz, but I can't stand rap.", "Джаз я люблю, а рэп терпеть не могу.",
      ["like", "would like", "am liking"], "like", "Вкусы вообще — like. Would like — хочу сейчас; like в -ing о вкусах не ставят."),
    c("l4-offer", 4, "___ some more tea?", "Хотите ещё чаю?",
      ["Would you like", "Do you like", "Are you liking"], "Would you like", "Предложение — Would you like…? Do you like tea? — любите ли вы чай."),
    c("l4-appointment", 4, "I'd like ___ an appointment for Monday.", "Я бы хотел записаться на понедельник.",
      ["to make", "making", "make"], "to make", "Would like + to do."),
    c("l4-job", 4, "— ___ your new job? — Yes, I love it.", "— Тебе нравится новая работа? — Да, очень.",
      ["Do you like", "Would you like", "Are you like"], "Do you like", "О вкусах и впечатлениях — Do you like…?"),
    c("l4-you-to", 4, "I'd like you ___ these results with the patient.", "Я хочу, чтобы вы обсудили эти результаты с пациентом.",
      ["to discuss", "discuss", "discussing"], "to discuss", "Would like + кто-то + to do: I'd like you to discuss."),

    # 5 · like doing и feel like doing
    c("l5-cook", 5, "I don't feel like ___ tonight — let's order a pizza.", "Мне сегодня не хочется готовить — закажем пиццу.",
      ["cooking", "to cook", "cook"], "cooking", "Feel like + -ing. Feel like to cook — ошибка."),
    c("l5-walk", 5, "Do you feel like ___ after dinner?", "Хочешь прогуляться после ужина?",
      ["a walk", "to walk", "walk"], "a walk", "Feel like + существительное: feel like a walk, a coffee."),
    c("l5-swim", 5, "I really like ___ in the sea.", "Я очень люблю плавать в море.",
      ["swimming", "swim", "to swimming"], "swimming", "Like + -ing — нравится занятие."),
    c("l5-habit", 5, "I like ___ the results myself before I call the patient.", "Я предпочитаю сам проверять результаты, прежде чем звонить пациенту.",
      ["to check", "check", "checked"], "to check", "Like + to do — привычка, «так правильно». Like checking — тоже верно."),
    c("l5-come", 5, "Would you like ___ with us on Saturday?", "Хотите пойти с нами в субботу?",
      ["to come", "coming", "come"], "to come", "Would like — всегда + to do."),
    c("l5-cry", 5, "When she heard the news, she felt like ___.", "Услышав новость, она чуть не расплакалась.",
      ["crying", "to cry", "cry"], "crying", "Feel like doing — хочется: felt like crying — хотелось плакать."),

    # 6 · like или as
    c("l6-nurse", 6, "My sister works ___ a nurse in a children's hospital.", "Сестра работает медсестрой в детской больнице.",
      ["as", "like"], "as", "Профессия, роль — as."),
    c("l6-sing", 6, "He sings ___ a professional, but he's actually a surgeon.", "Он поёт как профессионал, хотя на самом деле хирург.",
      ["like", "as"], "like", "Сходство — like: поёт как профессионал, но им не является."),
    c("l6-doctor", 6, "___ your doctor, I must warn you about the side effects.", "Как ваш врач, я должен предупредить о побочных эффектах.",
      ["As", "Like"], "As", "В роли — as: я и есть ваш врач."),
    c("l6-usual", 6, "___ usual, the train was late.", "Как обычно, поезд опоздал.",
      ["As", "Like"], "As", "As usual — устойчивое сочетание."),
    c("l6-said", 6, "___ I said yesterday, the scan was normal.", "Как я и говорил вчера, снимок в норме.",
      ["As", "Like"], "As", "As I said — нейтрально, в докладе и письме.",
      also={"Like": "тоже говорят, но разговорно; в докладе и письме — As"}),
    c("l6-office", 6, "We use this room ___ an office.", "Эта комната у нас вместо кабинета.",
      ["as", "like"], "as", "Функция — as: use something as — использовать в качестве."),

    # 7 · like и as if + предложение
    c("l7-rain", 7, "Take an umbrella — it looks ___ it's going to rain.", "Возьми зонт — похоже, будет дождь.",
      ["like", "as", "like as"], "like", "Look like + предложение — похоже, что (разговорное). Нейтрально — it looks as if."),
    c("l7-break", 7, "You've been working for twelve hours. It sounds ___ you need a break.", "Ты работаешь двенадцать часов подряд. Похоже, тебе нужен отдых.",
      ["like", "as", "that"], "like", "Sound like + предложение — похоже, что."),
    c("l7-asif", 7, "He talks ___ he knew everything about medicine.", "Он говорит так, будто всё знает о медицине.",
      ["as if", "like as", "as like"], "as if", "As if — как будто; прошедшее knew — на самом деле не знает."),
    c("l7-were", 7, "She acts as if she ___ the head of department.", "Она ведёт себя так, будто она заведующая.",
      ["were", "was", "be"], "were", "Нереальное «как будто» — прошедшее: as if she were.",
      also={"was": "тоже верно, разговорнее; were — книжнее"}),
    c("l7-seems", 7, "It seems ___ only yesterday that we started medical school.", "Кажется, только вчера мы поступили в медицинский.",
      ["like", "as", "that like"], "like", "It seems like yesterday — как будто вчера. Можно и It seems as if…"),
    c("l7-though", 7, "It looks as ___ the patient has fallen asleep.", "Похоже, пациент уснул.",
      ["though", "like", "if like"], "though", "As though = as if; нейтрально и в письме."),

    # 8 · such as, -like, likely, alike
    c("l8-suchas", 8, "Avoid NSAIDs ___ ibuprofen and naproxen.", "Избегайте НПВС, таких как ибупрофен и напроксен.",
      ["such as", "as", "alike"], "such as", "Примеры перед списком — such as. В разговоре — like."),
    c("l8-flu", 8, "She developed ___ symptoms after the vaccine.", "После прививки у неё появились гриппоподобные симптомы.",
      ["flu-like", "flu-alike", "likely flu"], "flu-like", "-like — «похожий на»: flu-like symptoms."),
    c("l8-likely", 8, "With treatment, he is ___ to make a full recovery.", "При лечении он, скорее всего, полностью поправится.",
      ["likely", "alike", "like"], "likely", "Be likely to do — скорее всего."),
    c("l8-alike", 8, "The two scans look ___ — I can't see any difference.", "Два снимка одинаковые — разницы не вижу.",
      ["alike", "like", "likely"], "alike", "Alike — одинаковые, после глагола: look alike. Look like — перед существительным."),
    c("l8-unlike", 8, "___ aspirin, paracetamol doesn't affect bleeding.", "В отличие от аспирина, парацетамол не влияет на кровотечение.",
      ["Unlike", "Dislike", "Not like"], "Unlike", "В отличие от — unlike."),
    c("l8-dislike", 8, "Many patients ___ taking pills every day.", "Многие пациенты не любят каждый день пить таблетки.",
      ["dislike", "unlike", "unliked"], "dislike", "Не любить — dislike + -ing."),
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
