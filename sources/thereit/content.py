# Содержание приложения «There или it».
# В примерах: {…} — there (синий), […] — it (оранжевый).

MIXED_TOPIC = 10

# Пары: there | it | пояснение к there | пояснение к it
PAIRS = [
    ["{There's} a new scanner.", "[It's] very fast.", "есть — первое упоминание", "он — уже известный"],
    ["{There's} a lot of noise.", "[It's] noisy.", "шум есть", "шумно"],
    ["{There's} still time.", "[It's] time to go.", "время есть", "пора"],
    ["{There's} no point in waiting.", "[It's] no use waiting.", "нет смысла", "бесполезно"],
    ["{There was} a lot of snow.", "[It] snowed a lot.", "snow — существительное", "snow — глагол"],
]

# Девять работ it (с листка): что | пример
IT_USES = [
    ["вещь", "This drug is new — I haven't used [it] yet."],
    ["действие", "Working nights is hard, isn't [it]?"],
    ["ситуация, идея", "I have to call the family again. I hate [it]!"],
    ["кто это", "Who called? — [It] was Catherine."],
    ["время", "[It's] a quarter to eleven."],
    ["погода", "[It] was colder last week."],
    ["расстояние", "[It's] 20 km to the hospital."],
    ["+ to do", "[It's] been great to talk to you."],
    ["+ that", "[It's] a shame that you missed it."],
]

# there + be во всех видах: когда | формы
THERE_FORMS = [
    ["сейчас", "there is · there are"],
    ["было", "there was · there were"],
    ["будет", "there will be · there's going to be"],
    ["за это время", "there has been · there have been"],
    ["раньше было", "there used to be"],
    ["похоже, есть", "there seems to be"],
    ["вопрос", "Is there…? Are there any…? How many … are there?"],
    ["ответ, хвостик", "Yes, there is. …, isn't there?"],
]

# Частые ошибки русскоговорящих: неверно | верно | почему
ERRORS = [
    ["Is cold today", "It's cold today", "«холодно» — нужно it"],
    ["In the ward are 30 beds", "There are 30 beds on the ward", "«есть» — there"],
    ["It's a lot of patients today", "There are a lot of patients today", "сколько чего есть — there"],
    ["There is important to rest", "It's important to rest", "«важно» — it"],
    ["Will be a meeting tomorrow", "There will be a meeting tomorrow", "there не теряется"],
    ["There's raining", "It's raining", "погода — it"],
]

TOPICS = [
    {"n": 1, "title": "there is / there are",
     "rule": "there + be сообщает, что что-то есть, существует: There's a CT scanner in A&E. be согласуется с существительным после него: there's + единственное или неисчисляемое (a bed, some blood), there are + множественное (two beds, a lot of patients). По-русски «в отделении есть…», по-английски начинаем с there: There are 30 beds on the ward.",
     "ex": [
         {"en": "{There's} a CT scanner in the emergency department.", "ru": "В приёмном отделении есть КТ."},
         {"en": "{There are} thirty beds on the stroke unit.", "ru": "В инсультном отделении тридцать коек."},
         {"en": "{There's} too much noise on the ward at night.", "ru": "Ночью в отделении слишком шумно."},
     ]},
    {"n": 2, "title": "there во всех временах",
     "rule": "Меняется только be: there was / were — было, there will be — будет, there have been — было за это время, there used to be — раньше был, there seems to be — похоже, есть. Главная ошибка — потерять there: Will be a meeting tomorrow — неверно, нужно There will be a meeting tomorrow.",
     "ex": [
         {"en": "{There was} a power cut during the night.", "ru": "Ночью отключали электричество."},
         {"en": "{There will be} a meeting at three.", "ru": "В три будет собрание."},
         {"en": "{There have been} twelve admissions since midnight.", "ru": "С полуночи поступило двенадцать пациентов."},
     ]},
    {"n": 3, "title": "Вопросы, ответы, хвостики",
     "rule": "В вопросе there меняется местами с be: Is there a lift? Are there any free beds? How many patients are there? Краткий ответ тоже с there: Yes, there is. No, there aren't. В конце ответа не сокращают: Yes, there is, а не Yes, there's. И в хвостике — there: There's a problem, isn't there?",
     "ex": [
         {"en": "{Is there} a pharmacy in the hospital?", "ru": "В больнице есть аптека?"},
         {"en": "How many beds {are there} on the unit?", "ru": "Сколько коек в отделении?"},
         {"en": "There's a problem, {isn't there}?", "ru": "Есть проблема, да?"},
     ]},
    {"n": 4, "title": "Сначала there, потом it",
     "rule": "Первый раз сообщаем, что что-то есть, — there. Дальше говорим об этом же — it (или he, she, they): There's a new scanner in the department. It's very fast. По-русски: «Есть новый аппарат. Он очень быстрый». Если вещь уже известна и мы говорим, где она, — it: Where's my phone? — It's on the desk.",
     "ex": [
         {"en": "{There's} a new MRI scanner in the department. [It's] much faster.", "ru": "В отделении новый МРТ. Он намного быстрее."},
         {"en": "Where's the defibrillator? — [It's] next to the lift.", "ru": "Где дефибриллятор? — Рядом с лифтом."},
         {"en": "{There's} a message for you. [It's] from the lab.", "ru": "Вам сообщение. Оно из лаборатории."},
     ]},
    {"n": 5, "title": "it — вещь, действие, ситуация",
     "rule": "it заменяет то, о чём уже сказали: вещь (I haven't used it yet), действие (Working nights is hard, isn't it?), целую ситуацию или идею (I have to call the family again. I hate it!). По-русски часто без дополнения — «ненавижу», «не нравится», «рекомендую». По-английски it нужен: I hate it, I don't like it, I'd recommend it.",
     "ex": [
         {"en": "This drug is new — I haven't used [it] yet.", "ru": "Это новый препарат — я его ещё не применял."},
         {"en": "Working nights is hard, isn't [it]?", "ru": "Работать по ночам тяжело, правда?"},
         {"en": "I have to tell the family bad news. I hate [it].", "ru": "Мне надо сообщить родственникам плохую новость. Ненавижу это."},
     ]},
    {"n": 6, "title": "it — время, погода, расстояние",
     "rule": "Русское «холодно», «поздно», «далеко», «десять минут пешком» — без подлежащего. Английскому оно нужно — ставим пустое it: It's cold. It's late. It's 20 km to the hospital. It takes ten minutes to walk there. Так же дни и даты: It's Monday.",
     "ex": [
         {"en": "[It's] a quarter to eleven already.", "ru": "Уже без четверти одиннадцать."},
         {"en": "[It] was much colder last week.", "ru": "На прошлой неделе было гораздо холоднее."},
         {"en": "[It's] twenty kilometres from here to the hospital.", "ru": "Отсюда до больницы двадцать километров."},
         {"en": "[It takes] ten minutes to get to the CT room.", "ru": "До кабинета КТ идти десять минут."},
     ]},
    {"n": 7, "title": "it — кто это?",
     "rule": "Когда спрашиваем или говорим, кто это был, человек ещё не назван — it: Who's at the door? — It's the physio. Who left this message? — It was Catherine. По телефону: Hi, it's Anna. Для выделения: It was the night nurse who noticed it first — «именно ночная медсестра».",
     "ex": [
         {"en": "Who left you this message? — [It] was Catherine.", "ru": "Кто оставил тебе сообщение? — Кэтрин."},
         {"en": "Who's at the door? — [It's] the physiotherapist.", "ru": "Кто там за дверью? — Физиотерапевт."},
         {"en": "[It was] the night nurse who noticed the weakness first.", "ru": "Слабость первой заметила именно ночная медсестра."},
     ]},
    {"n": 8, "title": "It's … to do, It's … that",
     "rule": "Вместо длинного подлежащего ставим it, а смысл уносим в конец: It's important to rest — а не To rest is important. It's a shame that you missed it. It's been great to talk to you. Сюда же: It's worth doing, It seems that…, It's the first time I've… По-русски «важно», «жаль», «приятно» — по-английски It's important, It's a pity.",
     "ex": [
         {"en": "[It's] important to take the tablets every day.", "ru": "Важно принимать таблетки каждый день."},
         {"en": "[It's] a shame that you couldn't come.", "ru": "Жаль, что вы не смогли прийти."},
         {"en": "[It's] been great to work with you.", "ru": "Было здорово с вами поработать."},
     ]},
    {"n": 9, "title": "Пары-ловушки",
     "rule": "Похожие фразы с разным подлежащим. There's still time — время есть; It's time to go — пора. There's no point in waiting — «нет смысла»; It's no use waiting — «бесполезно»: point — с there, no use и no good — обычно с it. There was a lot of snow — существительное snow; It snowed a lot — глагол snow.",
     "ex": [
         {"en": "{There's} still time before the ward round.", "ru": "До обхода ещё есть время."},
         {"en": "[It's] time to go.", "ru": "Пора идти."},
         {"en": "{There's} no point in waiting.", "ru": "Нет смысла ждать."},
         {"en": "[It's] no use waiting.", "ru": "Ждать бесполезно."},
     ]},
    {"n": MIXED_TOPIC, "title": "Итог — всё вместе",
     "rule": "Пятнадцать случайных карточек из всех тем вперемешку.",
     "ex": []},
]

CARDS = [
    # 1 — there is / are
    {"id": "t1-beds", "t": 1, "q": "There ___ two free beds on the stroke unit.", "opts": ["is", "are"], "a": "are",
     "why": "beds — множественное: there are."},
    {"id": "t1-blood", "t": 1, "q": "There ___ some blood in the urine.", "opts": ["is", "are"], "a": "is",
     "why": "blood — неисчисляемое: there is."},
    {"id": "t1-lot", "t": 1, "q": "There ___ a lot of patients in A&E today.", "opts": ["is", "are"], "a": "are",
     "why": "Считаем по patients — множественное: there are. There's a lot of… с множественным — разговорно."},
    {"id": "t1-info", "t": 1, "q": "There ___ very little information about the side effects.", "opts": ["is", "are"], "a": "is",
     "why": "information — неисчисляемое: there is."},
    {"id": "t1-problem", "t": 1, "q": "There ___ a problem with the monitors.", "opts": ["is", "are"], "a": "is",
     "why": "Подлежащее — a problem, а не monitors: there is."},
    {"id": "t1-questions", "t": 1, "q": "There ___ several questions I'd like to ask.", "opts": ["is", "are"], "a": "are",
     "why": "questions — множественное: there are."},

    # 2 — времена
    {"id": "t2-was", "t": 2, "q": "There ___ a power cut during the operation yesterday.", "opts": ["was", "were", "has been"], "a": "was",
     "why": "yesterday и одна авария — there was."},
    {"id": "t2-will", "t": 2, "q": "___ a staff meeting tomorrow at 8.", "opts": ["There will be", "Will be", "It will be"], "a": "There will be",
     "why": "«Будет собрание» — there will be; there не теряется."},
    {"id": "t2-have", "t": 2, "q": "___ twelve admissions since midnight.", "opts": ["There have been", "There has been", "It has been"], "a": "There have been",
     "why": "since — Present Perfect; admissions — множественное: there have been."},
    {"id": "t2-used", "t": 2, "q": "___ a pharmacy on this corner, but it closed.", "opts": ["There used to be", "It used to be"], "a": "There used to be",
     "why": "«Раньше здесь была аптека» — there used to be."},
    {"id": "t2-seems", "t": 2, "q": "___ to be a problem with your blood test.", "opts": ["There seems", "It seems"], "a": "There seems",
     "why": "«Похоже, есть проблема» — there seems to be + существительное."},

    # 3 — вопросы, ответы, хвостики
    {"id": "t3-any", "t": 3, "q": "___ any free beds in ICU?", "opts": ["Are there", "Is there", "Is it"], "a": "Are there",
     "why": "beds — множественное, вопрос: Are there any…?"},
    {"id": "t3-howmany", "t": 3, "q": "How many patients ___ on the waiting list?", "opts": ["are there", "there are", "is it"], "a": "are there",
     "why": "В вопросе be идёт перед there: how many … are there?"},
    {"id": "t3-short", "t": 3, "q": "Is there a lift to the third floor? — Yes, ___.", "opts": ["there is", "there's", "it is"], "a": "there is",
     "why": "Краткий ответ — Yes, there is. В конце не сокращают."},
    {"id": "t3-tag", "t": 3, "q": "There's a problem with the ECG, ___?", "opts": ["isn't there", "isn't it"], "a": "isn't there",
     "why": "Хвостик повторяет there: isn't there?"},
    {"id": "t3-tagit", "t": 3, "q": "It's cold in here, ___?", "opts": ["isn't it", "isn't there"], "a": "isn't it",
     "why": "Начали с it — хвостик isn't it."},

    # 4 — сначала there, потом it
    {"id": "t4-new", "t": 4, "q": "We've got a new scanner. ___ much faster than the old one.", "opts": ["It's", "There's"], "a": "It's",
     "why": "Сканер уже назван — дальше it."},
    {"id": "t4-where", "t": 4, "q": "Where's my stethoscope? — ___ on your desk.", "opts": ["It's", "There's"], "a": "It's",
     "why": "Вещь известна, говорим, где она: it's."},
    {"id": "t4-message", "t": 4, "q": "Dr Ivanova, ___ a message for you at the nurses' station.", "opts": ["there's", "it's"], "a": "there's",
     "why": "Первое упоминание — there's."},
    {"id": "t4-lab", "t": 4, "q": "There's a message for you. ___ from the lab.", "opts": ["It's", "There's"], "a": "It's",
     "why": "Сообщение уже названо — it's."},
    {"id": "t4-desk", "t": 4, "q": "___ a stethoscope on your desk — is it yours?", "opts": ["There's", "It's"], "a": "There's",
     "why": "Неизвестный стетоскоп, первое упоминание — there's."},

    # 5 — it: вещь, действие, ситуация
    {"id": "t5-hate", "t": 5, "q": "I have to tell him the results myself. I hate ___.", "opts": ["it", ""], "a": "it",
     "why": "«Ненавижу это» — I hate it: без it нельзя."},
    {"id": "t5-like", "t": 5, "q": "The new rota? I don't like ___ at all.", "opts": ["it", ""], "a": "it",
     "why": "«Мне не нравится» — I don't like it."},
    {"id": "t5-running", "t": 5, "q": "Running every day is hard, isn't ___?", "opts": ["it", "there", "they"], "a": "it",
     "why": "Действие — it: isn't it?"},
    {"id": "t5-recommend", "t": 5, "q": "I tried the new app, and I'd really recommend ___.", "opts": ["it", ""], "a": "it",
     "why": "«Очень рекомендую» — I'd recommend it."},
    {"id": "t5-sense", "t": 5, "q": "Can you explain that again? ___ doesn't make sense to me.", "opts": ["It", "There"], "a": "It",
     "why": "Говорим об уже сказанном — it."},

    # 6 — время, погода, расстояние
    {"id": "t6-late", "t": 6, "q": "___ late — you should go home.", "opts": ["It's", "Is", "There's"], "a": "It's",
     "why": "«Поздно» — подлежащее нужно: it's late."},
    {"id": "t6-raining", "t": 6, "q": "Take an umbrella — ___ raining.", "opts": ["it's", "there's", "is"], "a": "it's",
     "why": "Погода — it's raining."},
    {"id": "t6-far", "t": 6, "q": "How far ___ from here to the hospital?", "opts": ["is it", "is there", "is"], "a": "is it",
     "why": "Расстояние — it: How far is it?"},
    {"id": "t6-takes", "t": 6, "q": "___ about twenty minutes to get to work.", "opts": ["It takes", "There takes", "Takes"], "a": "It takes",
     "why": "Сколько времени занимает — it takes."},
    {"id": "t6-cold", "t": 6, "q": "___ freezing in the corridor — can we close the window?", "opts": ["It's", "There's", "Is"], "a": "It's",
     "why": "«Холодно» — it's freezing."},
    {"id": "t6-monday", "t": 6, "q": "___ Monday today, so the clinic is busy.", "opts": ["It's", "There's", "Is"], "a": "It's",
     "why": "Дни и даты — it's."},

    # 7 — кто это
    {"id": "t7-door", "t": 7, "q": "Someone's knocking. — ___ probably the cleaner.", "opts": ["It's", "He's", "There's"], "a": "It's",
     "why": "Кто — ещё не назван: it's."},
    {"id": "t7-lab", "t": 7, "q": "Who's calling? — ___ Anna from the lab.", "opts": ["It's", "There's", "Is"], "a": "It's",
     "why": "Представляемся по телефону — it's."},
    {"id": "t7-who", "t": 7, "q": "Who took the blood sample? — ___ the new phlebotomist.", "opts": ["It was", "There was", "He was"], "a": "It was",
     "why": "Ответ на «кто?» — it was."},
    {"id": "t7-cleft", "t": 7, "q": "___ the night nurse who noticed the weakness first.", "opts": ["It was", "There was", "Was"], "a": "It was",
     "why": "Выделяем, кто именно: It was … who…"},
    {"id": "t7-me", "t": 7, "q": "Who's there? — ___ me, Pavel.", "opts": ["It's", "I'm", "There's"], "a": "It's",
     "why": "It's me — «это я»."},

    # 8 — It's … to do / that
    {"id": "t8-important", "t": 8, "q": "___ important to take the tablets at the same time every day.", "opts": ["It's", "There's", "Is"], "a": "It's",
     "why": "«Важно» — It's important to…"},
    {"id": "t8-shame", "t": 8, "q": "___ a pity that the scan was cancelled.", "opts": ["It's", "There's"], "a": "It's",
     "why": "«Жаль, что…» — It's a pity that…"},
    {"id": "t8-worth", "t": 8, "q": "___ worth checking the INR again.", "opts": ["It's", "There's"], "a": "It's",
     "why": "«Стоит сделать» — It's worth doing."},
    {"id": "t8-seems", "t": 8, "q": "___ that the drug isn't working.", "opts": ["It seems", "There seems", "Seems"], "a": "It seems",
     "why": "It seems that… + предложение; there seems to be — перед существительным."},
    {"id": "t8-easy", "t": 8, "q": "___ not easy to tell a family news like that.", "opts": ["It's", "There's", "Is"], "a": "It's",
     "why": "«Нелегко» — It's not easy to…"},
    {"id": "t8-first", "t": 8, "q": "___ the first time I've seen a case like this.", "opts": ["It's", "There's"], "a": "It's",
     "why": "It's the first time I've… — «впервые вижу»."},

    # 9 — пары-ловушки
    {"id": "t9-still", "t": 9, "q": "Don't rush — ___ still plenty of time before the ward round.", "opts": ["there's", "it's"], "a": "there's",
     "why": "Время есть — there's time."},
    {"id": "t9-go", "t": 9, "q": "Come on, ___ time to go.", "opts": ["it's", "there's"], "a": "it's",
     "why": "«Пора» — it's time to…"},
    {"id": "t9-point", "t": 9, "q": "___ no point in repeating the scan.", "opts": ["There's", "It's"], "a": "There's",
     "why": "no point — с there: there's no point in doing."},
    {"id": "t9-use", "t": 9, "q": "___ no use arguing with him.", "opts": ["It's", "There's"], "a": "It's",
     "also": {"There's": "there's no use тоже встречается, но чаще it's no use"},
     "why": "no use — обычно с it: it's no use doing."},
    {"id": "t9-snow", "t": 9, "q": "___ a lot of snow last winter.", "opts": ["There was", "It was"], "a": "There was",
     "why": "snow — существительное: there was a lot of snow."},
    {"id": "t9-snowing", "t": 9, "q": "___ snowing heavily when he was admitted.", "opts": ["It was", "There was"], "a": "It was",
     "why": "snowing — глагол: it was snowing."},
]
