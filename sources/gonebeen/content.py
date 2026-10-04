# Содержание приложения «gone / been».
# В примерах: […] — gone (оранжевый), {…} — been to (синий), |…| — been in / been at (зелёный).

MIXED_TOPIC = 8

# Три формы: форма | класс цвета | значок | смысл | пример
FORMS = [
    ["gone to", "pr", "oneway", "ушёл, уехал — его здесь нет", "He's gone to the lab."],
    ["been to", "st", "round", "сходил и вернулся, бывал", "He's been to the lab."],
    ["been in", "good", "inside", "находится там, for / since", "He's been in the lab all morning."],
]

# Ещё полезное: что | пример | пояснение
EXTRA = [
    ["home — без to", "She's [gone home].", "ушла домой"],
    ["been to see", "I've {been to see} the GP.", "сходил к врачу"],
    ["been at", "I've |been at| work since 7.", "на работе, на событии"],
    ["went to + «когда»", "I went to Kazan in 2019.", "есть «когда» — Past Simple"],
    ["Where have you been?", "", "где ты был? — он вернулся"],
    ["Where has he gone?", "", "куда он делся? — его нет"],
]

# Частые ошибки: неверно | верно | почему
ERRORS = [
    ["I've been to London last year", "I went to London last year", "есть «когда» — went"],
    ["He's been to Moscow till Monday", "He's gone to Moscow till Monday", "его нет — gone"],
    ["Have you ever gone to Italy?", "Have you ever been to Italy?", "опыт — been"],
    ["She's gone to home", "She's gone home", "home — без to"],
    ["I'm in hospital since Monday", "I've been in hospital since Monday", "since — Present Perfect"],
]

TOPICS = [
    {"n": 1, "title": "gone to — ушёл, его нет",
     "rule": "has gone to — ушёл или уехал туда и ещё не вернулся: сейчас он там или в пути. Главный признак — человека здесь нет: Dr Petrov has gone to the ward, he'll be back soon. С I и we так почти не говорят: раз я здесь и говорю — я не ушёл.",
     "ex": [
         {"en": "Dr Petrov has [gone to] the ward — he'll be back in ten minutes.", "ru": "Доктор Петров ушёл в отделение — вернётся через десять минут."},
         {"en": "The patient has [gone to] X-ray.", "ru": "Пациента увезли на рентген."},
         {"en": "She's [gone to] Moscow for a conference.", "ru": "Она уехала в Москву на конференцию."},
     ]},
    {"n": 2, "title": "been to — сходил и вернулся",
     "rule": "has been to — побывал там и вернулся: поездка туда и обратно или опыт в жизни. Человек снова здесь. С ever, never, once, twice, three times — почти всегда been to: Have you ever been to Japan? Сверх уровня: в американском английском gone to иногда значит и «бывал», в британском — нет.",
     "ex": [
         {"en": "I've {been to} the pharmacy — here are your tablets.", "ru": "Я сходил в аптеку — вот ваши таблетки."},
         {"en": "Have you ever {been to} London?", "ru": "Вы когда-нибудь бывали в Лондоне?"},
         {"en": "She's {been to} three conferences this year.", "ru": "В этом году она была уже на трёх конференциях."},
     ]},
    {"n": 3, "title": "been in — находится там",
     "rule": "has been in — находится там какое-то время и, скорее всего, ещё там. Почти всегда с for или since: he's been in hospital for a week. Так же — живу где-то: I've been in Yekaterinburg since 2015. И работа в области: she's been in neurology for ten years.",
     "ex": [
         {"en": "He's |been in| hospital for a week.", "ru": "Он уже неделю в больнице."},
         {"en": "We've |been in| this building since 2010.", "ru": "Мы в этом здании с 2010 года."},
         {"en": "She's |been in| neurology for ten years.", "ru": "Она десять лет работает в неврологии."},
     ]},
    {"n": 4, "title": "gone или been: где он сейчас?",
     "rule": "Спроси себя: где человек сейчас? Его нет, он там или в пути — gone. Вернулся, он здесь — been. Одна и та же поездка: Tom has gone to the lab — его нет. Tom has been to the lab — сходил, уже здесь.",
     "ex": [
         {"en": "Tom has [gone to] the lab.", "ru": "Том ушёл в лабораторию — его нет."},
         {"en": "Tom has {been to} the lab.", "ru": "Том сходил в лабораторию — он уже вернулся."},
     ]},
    {"n": 5, "title": "Where have you been? Where has he gone?",
     "rule": "Where have you been? — «Где ты был?»: человек вернулся и стоит перед тобой. Where has he gone? — «Куда он делся?»: его нет. Where have you gone? — так почти не говорят: раз ты передо мной, ты никуда не ушёл. Про вещи тоже gone: Where have my glasses gone?",
     "ex": [
         {"en": "Where have you {been}? We've been looking for you!", "ru": "Где ты был? Мы тебя искали!"},
         {"en": "Where has the nurse [gone]? I need her now.", "ru": "Куда делась медсестра? Она мне сейчас нужна."},
     ]},
    {"n": 6, "title": "been to или went to",
     "rule": "Если сказано или понятно, когда — yesterday, last year, in 2019, on Monday, — нужен Past Simple: went to. Present Perfect — been to — когда время не названо и важен опыт или результат: I've been to London. I went to London last year.",
     "ex": [
         {"en": "I went to London last year.", "ru": "В прошлом году я ездил в Лондон."},
         {"en": "I've {been to} London three times.", "ru": "Я был в Лондоне три раза."},
     ]},
    {"n": 7, "title": "home, been to see, been at",
     "rule": "home — без to: gone home, been home, а не gone to home. been to see — «сходил к кому-то»: I've been to see the doctor. been at — на работе, в точке, на событии: I've been at work all day, she's been at a conference this week.",
     "ex": [
         {"en": "She's [gone home] — her shift is over.", "ru": "Она ушла домой — её смена закончилась."},
         {"en": "I've {been to see} the doctor about my back.", "ru": "Я сходил к врачу со своей спиной."},
         {"en": "I've |been at| work since seven.", "ru": "Я на работе с семи утра."},
     ]},
    {"n": MIXED_TOPIC, "title": "Итог — всё вместе",
     "rule": "Пятнадцать случайных карточек из всех тем вперемешку.",
     "ex": []},
]

G3 = ["gone to", "been to", "been in"]
CARDS = [
    # 1 — gone to
    {"id": "g-ward", "t": 1, "q": "Dr Petrov isn't here — he's ___ the ward.", "opts": G3, "a": "gone to",
     "why": "Его здесь нет — ушёл и не вернулся: gone to."},
    {"id": "g-xray", "t": 1, "q": "The patient's bed is empty — he's ___ X-ray.", "opts": G3, "a": "gone to",
     "why": "Пациента нет на месте — gone to."},
    {"id": "g-conf", "t": 1, "q": "She's ___ Moscow for a conference. She'll be back on Friday.", "opts": G3, "a": "gone to",
     "why": "Вернётся в пятницу — значит, сейчас её нет: gone to."},
    {"id": "g-lunch", "t": 1, "q": "Sorry, the registrar has ___ lunch. Can I help you?", "opts": G3, "a": "gone to",
     "why": "Ушёл на обед и ещё не вернулся — gone to."},
    {"id": "g-country", "t": 1, "q": "Mum isn't answering — she's ___ the country for the weekend.", "opts": G3, "a": "gone to",
     "why": "Уехала на выходные и сейчас там — gone to."},

    # 2 — been to
    {"id": "b-ever", "t": 2, "q": "Have you ever ___ Japan?", "opts": G3, "a": "been to",
     "why": "Опыт с ever — been to."},
    {"id": "b-pharmacy", "t": 2, "q": "I've ___ the pharmacy — here are your tablets.", "opts": G3, "a": "been to",
     "why": "Сходил и вернулся с таблетками — been to."},
    {"id": "b-twice", "t": 2, "q": "I've ___ Kazan twice, but I've never lived there.", "opts": G3, "a": "been to",
     "why": "Поездки, сколько раз — been to."},
    {"id": "b-never", "t": 2, "q": "He's never ___ the dentist in his life.", "opts": G3, "a": "been to",
     "why": "never — опыт: been to."},
    {"id": "b-confs", "t": 2, "q": "She's ___ three conferences this year.", "opts": G3, "a": "been to",
     "why": "Побывала и вернулась — been to."},

    # 3 — been in
    {"id": "i-week", "t": 3, "q": "Mr Ivanov has ___ hospital for a week.", "opts": G3, "a": "been in",
     "why": "for a week — находится там: been in."},
    {"id": "i-since", "t": 3, "q": "I've ___ Yekaterinburg since 2015.", "opts": G3, "a": "been in",
     "why": "since — живу там до сих пор: been in."},
    {"id": "i-icu", "t": 3, "q": "She's ___ intensive care since Monday.", "opts": G3, "a": "been in",
     "why": "since Monday — лежит там: been in."},
    {"id": "i-neuro", "t": 3, "q": "Dr Orlova has ___ neurology for twenty years.", "opts": G3, "a": "been in",
     "why": "Работа в области — been in."},
    {"id": "i-queue", "t": 3, "q": "We've ___ this queue for an hour!", "opts": G3, "a": "been in",
     "why": "Стоим в очереди уже час — been in."},

    # 4 — gone или been
    {"id": "c-back", "t": 4, "q": "Tom has ___ the lab and brought the results.", "opts": G3, "a": "been to",
     "why": "Принёс результаты — значит, вернулся: been to."},
    {"id": "c-away", "t": 4, "q": "Tom has ___ the lab. He'll bring the results soon.", "opts": G3, "a": "gone to",
     "why": "Принесёт позже — сейчас его нет: gone to."},
    {"id": "c-tan", "t": 4, "q": "You look great! Have you ___ the seaside?", "opts": G3, "a": "been to",
     "why": "Человек перед тобой, уже вернулся — been to."},
    {"id": "c-sister", "t": 4, "q": "My sister has ___ Australia to work. I really miss her.", "opts": G3, "a": "gone to",
     "why": "Скучаю — её здесь нет: gone to."},
    {"id": "c-meeting", "t": 4, "q": "Is Dr Kim here? — No, she's just ___ a meeting.", "opts": G3, "a": "gone to",
     "why": "Её нет, она на совещании — gone to."},
    {"id": "c-gym", "t": 4, "q": "Why are you so tired? — I've just ___ the gym.", "opts": G3, "a": "been to",
     "why": "Сходил и вернулся уставшим — been to."},

    # 5 — вопросы
    {"id": "q-you", "t": 5, "q": "Where have you ___? We've been looking for you!", "opts": ["been", "gone"], "a": "been",
     "why": "Человек вернулся — Where have you been?"},
    {"id": "q-nurse", "t": 5, "q": "Where has the nurse ___? I need her right now.", "opts": ["gone", "been"], "a": "gone",
     "why": "Её нет — Where has she gone?"},
    {"id": "q-glasses", "t": 5, "q": "Where have my glasses ___? I had them a minute ago.", "opts": ["gone", "been"], "a": "gone",
     "why": "Вещи пропадают — gone."},
    {"id": "q-morning", "t": 5, "q": "Where have you ___ all morning? — At a conference.", "opts": ["been", "gone"], "a": "been",
     "why": "Где ты был всё утро? — been."},

    # 6 — been to или went to
    {"id": "w-last", "t": 6, "q": "I ___ London last year.", "opts": ["went to", "have been to"], "a": "went to",
     "why": "last year — «когда» названо: went to."},
    {"id": "w-sofar", "t": 6, "q": "I ___ London three times so far.", "opts": ["have been to", "went to"], "a": "have been to",
     "why": "so far — до сих пор, время не названо: have been to."},
    {"id": "w-yesterday", "t": 6, "q": "He ___ the GP yesterday.", "opts": ["went to", "has been to"], "a": "went to",
     "why": "yesterday — Past Simple: went to."},
    {"id": "w-2019", "t": 6, "q": "Have you ever been to Kazan? — Yes, I ___ there in 2019.", "opts": ["went", "have been"], "a": "went",
     "why": "in 2019 — «когда» названо: went."},
    {"id": "w-monday", "t": 6, "q": "He ___ the GP on Monday and got a referral.", "opts": ["went to", "has been to"], "a": "went to",
     "why": "on Monday — Past Simple: went to."},

    # 7 — home, been to see, been at
    {"id": "h-home", "t": 7, "q": "Where's Anna? — She's ___ home.", "opts": ["gone", "gone to", "been to"], "a": "gone",
     "why": "home — без to: gone home."},
    {"id": "h-see", "t": 7, "q": "I've ___ see the GP about my headaches.", "opts": ["been to", "gone to"], "a": "been to",
     "why": "been to see — сходил к кому-то и вернулся."},
    {"id": "h-work", "t": 7, "q": "I've ___ work since seven this morning.", "opts": ["been at", "been to", "gone to"], "a": "been at",
     "why": "since seven — на работе до сих пор: been at work."},
    {"id": "h-conf", "t": 7, "q": "She's ___ a conference all week.", "opts": ["been at", "been in", "gone to"], "a": "been at",
     "why": "На событии всю неделю — been at."},
    {"id": "h-beenhome", "t": 7, "q": "Have you ___ home since the accident?", "opts": ["been", "been to"], "a": "been",
     "why": "home — без to: been home."},
]
