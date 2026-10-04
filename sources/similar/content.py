# Содержание приложения «Похожие слова»: смотреть, говорить, поездки, учиться и знать.
# Пометка […] — слово в фокусе (оранжевый).

MIXED_TOPIC = 9

GROUPS = {
    "look": "Смотреть: see, look, watch…",
    "say": "Говорить: say, tell, speak, talk",
    "trip": "Поездки: trip, travel, journey…",
    "learn": "Учиться и знать: learn, study, teach…",
    "mix": "Итог",
}

# Главное в каждой группе (левая колонка): группа | [английское слово, русская подсказка]
KEYS = [
    ["Смотреть", [["see", "видишь само"], ["look at", "смотришь на что-то"], ["watch", "следишь за тем, что движется"]]],
    ["Говорить", [["say", "что сказал"], ["tell", "кому сказал"], ["speak", "язык, речь, официально"], ["talk", "беседа, разговор"]]],
    ["Поездки", [["a trip", "поездка туда и обратно"], ["travel", "путешествовать, путешествия"], ["journey", "дорога из А в Б"]]],
    ["Учиться и знать", [["learn", "сам, результат"], ["study", "процесс, предмет"], ["teach", "учить другого"], ["know", "знать"]]],
]

# Слова по группам: слово | перевод | сочетания | текст для озвучки
WORDS = {
    "look": [
        ["see", "видеть (само, без усилия); I\u00a0see\u00a0— понимаю", "I can see · see a doctor · I see what you mean", "see. see a doctor."],
        ["look at", "смотреть на, направить взгляд", "look at the scan · Look!", "look at. look at the scan."],
        ["watch", "смотреть, следить (движение, время)", "watch TV · watch the monitor", "watch. watch TV."],
        ["stare at", "пристально, неподвижно смотреть", "stare at the ceiling", "stare at. stare at the ceiling."],
        ["gaze at", "долго, задумчиво, с восхищением", "gaze at the sea", "gaze at. gaze at the sea."],
        ["glance at", "мельком взглянуть", "glance at the clock", "glance at. glance at the clock."],
        ["view", "просматривать (официально)", "view the images", "view. view the images."],
    ],
    "say": [
        ["say", "сказать что-то (слова)", "say that… · say hello · say sorry", "say. say hello."],
        ["tell", "сказать кому-то", "tell me · tell the truth · tell him to…", "tell. tell me the truth."],
        ["speak", "говорить: язык, речь, официально", "speak English · speak at a conference", "speak. speak English."],
        ["talk", "разговаривать, беседовать", "talk to · talk about · We need to talk.", "talk. we need to talk."],
    ],
    "trip": [
        ["trip", "поездка (туда и обратно)", "a business trip · a day trip", "trip. a business trip."],
        ["travel", "путешествовать; путешествия вообще", "love to travel · air travel", "travel. I love to travel."],
        ["journey", "путь, дорога из А в Б", "the journey to work", "journey. the journey to work."],
        ["tour", "поездка с осмотром, экскурсия", "a tour of the hospital", "tour. a tour of the hospital."],
        ["voyage", "долгое плавание (книжное)", "a sea voyage", "voyage. a sea voyage."],
        ["cruise", "круиз", "go on a cruise", "cruise. go on a cruise."],
        ["hitchhiking", "автостоп", "go hitchhiking", "hitchhiking. go hitchhiking."],
    ],
    "learn": [
        ["learn", "учиться, выучить, узнать (результат)", "learn to drive · learn from mistakes", "learn. learn to drive."],
        ["study", "учиться, изучать (процесс)", "study medicine · study for an exam", "study. study medicine."],
        ["teach", "учить кого-то", "teach students · teach me to swim", "teach. teach me to swim."],
        ["educate", "давать образование, просвещать", "educate patients", "educate. educate patients."],
        ["train", "обучать навыку, готовить профессионально", "train as a nurse · train staff", "train. train as a nurse."],
        ["cram", "зубрить", "cram for an exam", "cram. cram for an exam."],
        ["know", "знать (состояние)", "I know · know the answer", "know. I know the answer."],
        ["examine", "осматривать, исследовать, экзаменовать", "examine a patient", "examine. examine a patient."],
        ["scrutinize", "придирчиво изучать", "scrutinize the data", "scrutinize. scrutinize the data."],
    ],
}

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["Say me the truth.", "Tell me the truth.", "кому-то — tell"],
    ["He said me that…", "He told me that…", "с человеком — tell; без него — said that…"],
    ["She talks English well.", "She speaks English well.", "язык — speak"],
    ["I saw TV last night.", "I watched TV last night.", "телевизор — watch"],
    ["Look the X-ray.", "Look at the X-ray.", "look at — с at"],
    ["I had a good travel.", "I had a good trip.", "поездка — a trip"],
    ["He learned me to drive.", "He taught me to drive.", "учить кого-то — teach"],
    ["I'm knowing him.", "I know him.", "know — без -ing"],
    ["Tell hello to her.", "Say hello to her.", "say hello, say sorry"],
    ["I study to drive.", "I'm learning to drive.", "навык — learn"],
]

TOPICS = [
    {"n": 1, "group": "look", "title": "see, look или watch", "sub": "видеть · смотреть на · следить",
     "rule": "see — видеть само, без усилия: I can see the scar. look at — направить взгляд на что-то: Look at this scan. watch — смотреть, следить за тем, что движется или меняется: watch TV, watch his blood pressure. Фильм — и see, и watch: I saw a great film. Ещё: see a doctor — сходить к врачу, I see — «понимаю».",
     "ex": [
         {"en": "I can't [see] without my glasses.", "ru": "Без очков я не вижу."},
         {"en": "[Look] at this scan.", "ru": "Посмотри на этот снимок."},
         {"en": "[Watch] his blood pressure tonight.", "ru": "Следите за его давлением этой ночью."},
     ]},
    {"n": 2, "group": "look", "title": "stare, gaze, glance, view", "sub": "пристально · задумчиво · мельком",
     "rule": "stare at — долго и пристально, часто невежливо или неподвижно: stare at the ceiling. gaze at — долго, задумчиво или с восхищением: gaze at the sea. glance at — мельком: glance at the clock. view — просматривать, официально: view the images.",
     "ex": [
         {"en": "He [glanced] at the clock.", "ru": "Он мельком взглянул на часы."},
         {"en": "Don't [stare] at people.", "ru": "Не пялься на людей."},
         {"en": "You can [view] the images online.", "ru": "Снимки можно посмотреть онлайн."},
     ]},
    {"n": 3, "group": "say", "title": "say или tell", "sub": "что сказал · кому сказал",
     "rule": "say — что сказали, без человека: He said (that) he was tired. Нужен человек — say to: What did she say to you? tell — кому-то, человек обязателен: He told me… Всегда tell, даже без человека: tell the truth, tell a lie, tell a story. Велеть — tell someone to do. Всегда say: say hello, say goodbye, say sorry.",
     "ex": [
         {"en": "He [said] he was tired.", "ru": "Он сказал, что устал."},
         {"en": "He [told] me he was tired.", "ru": "Он сказал мне, что устал."},
         {"en": "Please [tell] me the truth.", "ru": "Пожалуйста, скажите мне правду."},
     ]},
    {"n": 4, "group": "say", "title": "speak или talk", "sub": "язык, речь · беседа",
     "rule": "speak — язык и речь, официально, по телефону, выступление: speak English, speak at a conference, Can I speak to Dr Ivanov? talk — разговаривать, беседовать: talk to someone, talk about something, We need to talk. Доклад — a talk: give a talk.",
     "ex": [
         {"en": "Do you [speak] English?", "ru": "Вы говорите по-английски?"},
         {"en": "We need to [talk].", "ru": "Нам нужно поговорить."},
         {"en": "Can I [speak] to Dr Ivanov?", "ru": "Можно поговорить с доктором Ивановым?"},
     ]},
    {"n": 5, "group": "trip", "title": "trip, travel или journey", "sub": "поездка · путешествовать · дорога",
     "rule": "trip — поездка туда и обратно, с целью: a business trip, a day trip, go on a trip. travel — глагол «путешествовать» и путешествия вообще (без a): I love to travel, air travel. A travel — ошибка. journey — сам путь из А в Б: The journey takes an hour.",
     "ex": [
         {"en": "I'm on a business [trip].", "ru": "Я в командировке."},
         {"en": "I love to [travel].", "ru": "Я обожаю путешествовать."},
         {"en": "The [journey] to work takes an hour.", "ru": "Дорога на работу занимает час."},
     ]},
    {"n": 6, "group": "trip", "title": "tour, voyage, cruise, hitchhiking", "sub": "экскурсия · плавание · круиз · автостоп",
     "rule": "tour — поездка с осмотром нескольких мест, экскурсия: a tour of the hospital, a guided tour. voyage — долгое плавание или полёт в космос, книжное слово. cruise — морское путешествие для отдыха. hitchhiking — автостоп: go hitchhiking, hitchhike to Paris.",
     "ex": [
         {"en": "We had a [tour] of the hospital.", "ru": "Нам провели экскурсию по больнице."},
         {"en": "They went on a [cruise].", "ru": "Они отправились в круиз."},
         {"en": "They went [hitchhiking] across Europe.", "ru": "Они путешествовали автостопом по Европе."},
     ]},
    {"n": 7, "group": "learn", "title": "learn, study, teach, educate, train", "sub": "учиться · изучать · учить другого",
     "rule": "learn — учиться и выучить, результат: learn to drive, I learned a lot. study — учиться, изучать, процесс: study medicine, study for an exam. teach — учить кого-то: He taught me to swim (не learned me). educate — давать образование, просвещать: educate patients. train — обучать навыку, проходить подготовку: train as a nurse.",
     "ex": [
         {"en": "I'm [learning] to drive.", "ru": "Я учусь водить."},
         {"en": "She [studied] medicine.", "ru": "Она изучала медицину."},
         {"en": "My father [taught] me to swim.", "ru": "Папа научил меня плавать."},
     ]},
    {"n": 8, "group": "learn", "title": "know, cram, examine, scrutinize", "sub": "знать · зубрить · осматривать",
     "rule": "know — знать, это состояние, без -ing: I know him. Узнать что-то новое — learn или find out. cram — зубрить в последний момент: cram for an exam. examine — осматривать пациента, исследовать, экзаменовать. scrutinize — придирчиво, очень тщательно изучать: scrutinize the data.",
     "ex": [
         {"en": "I [know] him well.", "ru": "Я его хорошо знаю."},
         {"en": "He [crammed] all night.", "ru": "Он зубрил всю ночь."},
         {"en": "The doctor [examined] the patient.", "ru": "Врач осмотрел пациента."},
     ]},
    {"n": 9, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех групп вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · see, look, watch
    c("sl-see", 1, "I can't ___ anything without my glasses.", "Без очков я ничего не вижу.", ["see", "look", "watch"], "see",
      "Видеть само, без усилия, — see."),
    c("sl-look", 1, "___ at this CT scan — what do you think?", "Посмотри на этот снимок КТ — что думаешь?", ["Look", "See", "Watch"], "Look",
      "Направить взгляд на что-то — look at."),
    c("sl-tv", 1, "I ___ TV every evening.", "Каждый вечер я смотрю телевизор.", ["watch", "look", "see"], "watch",
      "Следить за тем, что движется и меняется, — watch: watch TV, watch a match."),
    c("sl-bp", 1, "Please ___ his blood pressure closely tonight.", "Пожалуйста, внимательно следите за его давлением этой ночью.",
      ["watch", "see", "look"], "watch", "Следить за изменениями — watch."),
    c("sl-doctor", 1, "You should ___ a doctor about that cough.", "Вам стоит показаться врачу с этим кашлем.", ["see", "look", "watch"], "see",
      "Сходить к врачу — see a doctor."),
    c("sl-lookat", 1, "Don't ___ at me like that!", "Не смотри на меня так!", ["look", "see", "watch"], "look", "look at — смотреть на кого-то."),
    c("sl-isee", 1, "Ah, I ___ what you mean.", "А, понимаю, о чём ты.", ["see", "look", "watch"], "see", "I see — «понимаю»."),

    # 2 · stare, gaze, glance, view
    c("sg-glance", 2, "He ___ at his watch and hurried out.", "Он мельком взглянул на часы и поспешил выйти.", ["glanced", "stared", "gazed"], "glanced",
      "Мельком взглянуть — glance at."),
    c("sg-stare", 2, "It's rude to ___ at people.", "Пялиться на людей невежливо.", ["stare", "glance", "view"], "stare",
      "Долго и пристально, невежливо — stare at."),
    c("sg-gaze", 2, "She sat by the window, ___ at the sea.", "Она сидела у окна и задумчиво смотрела на море.", ["gazing", "glancing", "viewing"], "gazing",
      "Долго, задумчиво, с восхищением — gaze at."),
    c("sg-view", 2, "You can ___ the images on the hospital system.", "Снимки можно посмотреть в больничной системе.", ["view", "stare", "glance"], "view",
      "Просматривать изображения, документы (официально) — view."),
    c("sg-ceiling", 2, "The patient ___ at the ceiling and didn't respond.", "Пациент неподвижно смотрел в потолок и не отвечал.",
      ["stared", "glanced", "viewed"], "stared", "Неподвижно, пристально смотреть — stare."),
    c("sg-notes", 2, "Could you just ___ at my notes before the ward round?", "Можешь быстро взглянуть на мои записи до обхода?",
      ["glance", "stare", "gaze"], "glance", "Быстро взглянуть — glance at."),

    # 3 · say или tell
    c("st-time", 3, "Can you ___ me the time?", "Не подскажете, который час?", ["tell", "say", "speak"], "tell", "Кому-то — tell: tell me the time."),
    c("st-said", 3, "He ___ that he felt dizzy.", "Он сказал, что у него кружится голова.", ["said", "told", "spoke"], "said",
      "Без человека — say: He said (that)…"),
    c("st-told", 3, "He ___ me that he felt dizzy.", "Он сказал мне, что у него кружится голова.", ["told", "said", "spoke"], "told",
      "С человеком — tell: told me."),
    c("st-truth", 3, "Please ___ me the truth.", "Пожалуйста, скажите мне правду.", ["tell", "say", "talk"], "tell",
      "tell the truth, tell a lie, tell a story — всегда tell."),
    c("st-hello", 3, "Come and ___ hello to my colleagues.", "Подойди поздороваться с моими коллегами.", ["say", "tell", "speak"], "say",
      "say hello, say goodbye, say sorry — всегда say."),
    c("st-order", 3, "The doctor ___ him to stop smoking.", "Врач велел ему бросить курить.", ["told", "said", "spoke"], "told",
      "Велеть кому-то — tell someone to do."),
    c("st-sayto", 3, "What did she ___ to you?", "Что она тебе сказала?", ["say", "tell", "talk"], "say",
      "Если после say нужен человек — say to you. Tell to you — ошибка: tell you."),

    # 4 · speak или talk
    c("sp-english", 4, "Do you ___ English?", "Вы говорите по-английски?", ["speak", "talk", "say"], "speak", "Язык — speak: speak English."),
    c("sp-results", 4, "We need to ___ about your results.", "Нам нужно поговорить о ваших результатах.", ["talk", "say", "tell"], "talk",
      "Разговор, беседа — talk about."),
    c("sp-phone", 4, "Can I ___ to Dr Ivanov, please?", "Можно поговорить с доктором Ивановым? (по телефону)", ["speak", "say", "tell"], "speak",
      "По телефону и официально — speak to."),
    c("sp-atalk", 4, "She'll give a ___ at the conference.", "Она выступит с докладом на конференции.", ["talk", "speak", "say"], "talk",
      "Доклад — a talk: give a talk. Speak — глагол."),
    c("sp-chat", 4, "My grandmother loves to ___ — she can't stop!", "Моя бабушка обожает поговорить — не остановить!", ["talk", "speak", "say"], "talk",
      "Болтать, разговаривать — talk."),
    c("sp-aphasia", 4, "After the stroke, he couldn't ___ at all.", "После инсульта он совсем не мог говорить.", ["speak", "say", "tell"], "speak",
      "Речь как способность — speak."),

    # 5 · trip, travel, journey
    c("tr-business", 5, "I'm going on a business ___ to Moscow.", "Я еду в командировку в Москву.", ["trip", "travel", "journey"], "trip",
      "Поездка с целью, туда и обратно, — trip: a business trip."),
    c("tr-love", 5, "I love to ___.", "Я обожаю путешествовать.", ["travel", "trip", "journey"], "travel", "Путешествовать (глагол) — travel."),
    c("tr-work", 5, "The ___ to work takes an hour by bus.", "Дорога на работу занимает час на автобусе.", ["journey", "travel", "tour"], "journey",
      "Путь из А в Б, сама дорога — journey."),
    c("tr-howwas", 5, "How was your ___? — Great, but the flight was long.", "Как съездил? — Отлично, но перелёт был долгим.",
      ["trip", "travel", "voyage"], "trip", "Вся поездка — trip. Travel в значении «поездка» — ошибка."),
    c("tr-air", 5, "Air ___ is cheaper than it used to be.", "Авиаперелёты стали дешевле, чем раньше.", ["travel", "trip", "journey"], "travel",
      "Путешествия вообще, неисчисляемое — travel: air travel."),
    c("tr-day", 5, "We went on a day ___ to the lake.", "Мы съездили на денёк на озеро.", ["trip", "travel", "journey"], "trip",
      "Поездка на день — a day trip."),
    c("tr-long", 5, "It was a long and tiring ___ across the mountains.", "Это была долгая и утомительная дорога через горы.",
      ["journey", "travel", "voyage"], "journey", "Трудная, долгая дорога — journey."),

    # 6 · tour, voyage, cruise, hitchhiking
    c("tv-tour", 6, "The new doctors had a ___ of the hospital.", "Новым врачам провели экскурсию по больнице.", ["tour", "trip", "journey"], "tour",
      "Экскурсия с осмотром — a tour of…"),
    c("tv-cruise", 6, "We went on a ten-day ___ — the ship had three pools!", "Мы сходили в десятидневный круиз — на лайнере было три бассейна!", ["cruise", "voyage", "tour"], "cruise",
      "Морское путешествие для отдыха — cruise."),
    c("tv-voyage", 6, "Columbus's first ___ across the Atlantic was in 1492.", "Первое плавание Колумба через Атлантику было в 1492 году.",
      ["voyage", "cruise", "tour"], "voyage", "Долгое морское плавание — voyage."),
    c("tv-hitch", 6, "I had no money, so I ___ to Paris — a driver gave me a lift.", "Денег не было, и я добрался до Парижа автостопом — меня подвёз водитель.",
      ["hitchhiked", "voyaged", "toured"], "hitchhiked", "Ехать автостопом — hitchhike: go hitchhiking, hitchhike to Paris."),
    c("tv-guided", 6, "We booked a guided ___ of the old town.", "Мы заказали экскурсию с гидом по старому городу.", ["tour", "voyage", "cruise"], "tour",
      "Экскурсия с гидом — a guided tour."),

    # 7 · learn, study, teach, educate, train
    c("le-drive", 7, "I'm ___ to drive.", "Я учусь водить машину.", ["learning", "studying", "teaching"], "learning", "Учиться навыку — learn to do."),
    c("le-medicine", 7, "She's ___ medicine at university — in two years she'll be a doctor.", "Она изучает медицину в университете — через два года станет врачом.",
      ["studying", "learning", "teaching"], "studying", "Учиться в вузе, заниматься предметом — study: study medicine."),
    c("le-swim", 7, "My father ___ me to swim.", "Папа научил меня плавать.", ["taught", "learned", "studied"], "taught",
      "Учить кого-то — teach: taught me. Learned me — ошибка."),
    c("le-case", 7, "I ___ a lot from this case.", "Я многому научился на этом случае.", ["learned", "studied", "taught"], "learned",
      "Научиться, получить результат — learn."),
    c("le-educate", 7, "We need to ___ patients about the signs of stroke.", "Нужно просвещать пациентов о признаках инсульта.",
      ["educate", "learn", "study"], "educate", "Просвещать, давать знания людям — educate."),
    c("le-train", 7, "She ___ as a nurse before becoming a doctor.", "До того как стать врачом, она выучилась на медсестру.",
      ["trained", "studied", "educated"], "trained", "Получить профессиональную подготовку — train as…"),
    c("le-exam", 7, "I have to ___ for my exam tonight.", "Вечером мне нужно готовиться к экзамену.", ["study", "learn", "teach"], "study",
      "Заниматься, готовиться — study for an exam."),

    # 8 · know, cram, examine, scrutinize
    c("kn-know", 8, "I ___ him very well.", "Я его очень хорошо знаю.", ["know", "am knowing", "learn"], "know", "know — состояние, без -ing: I know."),
    c("kn-found", 8, "I only ___ about his allergy yesterday.", "Я узнал о его аллергии только вчера.", ["learned", "knew", "studied"], "learned",
      "Узнать что-то новое — learn или find out. Knew — «знал»."),
    c("kn-cram", 8, "He ___ all night before the exam.", "Он зубрил всю ночь перед экзаменом.", ["crammed", "scrutinized", "examined"], "crammed",
      "Зубрить в последний момент — cram."),
    c("kn-examine", 8, "The doctor ___ the patient and listened to his chest.", "Врач осмотрел пациента и послушал лёгкие.", ["examined", "studied", "scrutinized"], "examined",
      "Осматривать пациента — examine."),
    c("kn-scrutinize", 8, "The committee will ___ every detail of the study.", "Комиссия будет придирчиво изучать каждую деталь исследования.",
      ["scrutinize", "examine", "cram"], "scrutinize", "Придирчиво, очень тщательно изучать — scrutinize.",
      also={"examine": "так можно; scrutinize — ещё тщательнее и придирчивее"}),
    c("kn-students", 8, "Tomorrow she's ___ the third-year students in neurology.", "Завтра она принимает у третьекурсников экзамен по неврологии.",
      ["examining", "scrutinizing", "cramming"], "examining", "Экзаменовать — examine."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()), sum(len(v) for v in WORDS.values()), "words")
