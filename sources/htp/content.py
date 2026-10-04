# Содержание приложения «have, take, pay» (English Collocations in Use, Everyday verbs 3) + тема «В больнице».
# Пометка […] — сочетание в фокусе; цвет по глаголу: have — оранжевый, take — синий, pay — зелёный, прочие подчёркнуты.
# Примеры свои, не из учебника.

MIXED_TOPIC = 8

GROUPS = {
    "have": "have — «у меня было»",
    "take": "take — «беру, принимаю»",
    "pay": "pay — «плачу вниманием»",
    "med": "В больнице",
    "mix": "Итог",
}

# Шпаргалка по странице: сочетание | перевод | пример | как озвучить сочетание
HAVE = [
    ["have an accident", "попасть в аварию, несчастный случай", "He had an accident at work and hurt his back.", "have an accident"],
    ["have an argument / a row", "поссориться; row /raʊ/", "They had a row about who should drive.", "have an argument, have a row"],
    ["have a break", "сделать перерыв", "Let's have a break for lunch.", "have a break"],
    ["have a conversation / a chat", "поговорить, поболтать", "I had a chat with the family after the round.", "have a conversation, have a chat"],
    ["have difficulty + -ing", "с трудом что-то делать", "She has difficulty finding the right words.", "have difficulty"],
    ["have a dream / a nightmare", "видеть сон, кошмар", "I had a strange dream about work.", "have a dream, have a nightmare"],
    ["have an experience", "случай, переживание", "Have you ever had a bad experience with a doctor?", "have an experience"],
    ["have a feeling", "есть ощущение, предчувствие", "I have a feeling we've met before.", "have a feeling"],
    ["have fun / a good time", "повеселиться, хорошо провести время", "We had a great time in Lisbon.", "have fun, have a good time"],
    ["have a look (at)", "взглянуть", "Could you have a look at my ECG?", "have a look"],
    ["have a party", "устроить вечеринку", "Let's have a party when the project is over.", "have a party"],
    ["have a problem / problems", "есть проблема, трудности", "I'm having problems with my computer.", "have a problem"],
    ["have a try / a go", "попробовать", "Can I have a go?", "have a try, have a go"],
]
TAKE = [
    ["take a holiday", "взять отпуск, поехать отдыхать", "You need to take a proper holiday.", "take a holiday"],
    ["take a trip", "съездить, совершить поездку", "We took a trip to Kazan last spring.", "take a trip"],
    ["take a train / a bus", "поехать поездом, автобусом", "It's quicker to take the train.", "take a train, take a bus"],
    ["take a risk", "рисковать", "I don't want to take any risks.", "take a risk"],
    ["take a chance", "рискнуть, попытать счастья", "It's a long shot, but let's take a chance.", "take a chance"],
    ["take action", "принять меры, действовать", "The hospital took action to cut waiting times.", "take action"],
    ["take advantage of", "воспользоваться", "Take advantage of the good weather.", "take advantage of"],
    ["take a liking to", "проникнуться симпатией", "Our dog took a liking to the neighbours.", "take a liking to"],
    ["take a dislike to", "невзлюбить", "She took an instant dislike to him.", "take a dislike to"],
    ["take an interest in", "заинтересоваться", "He's taken an interest in medical English.", "take an interest in"],
    ["take photos", "фотографировать", "Please don't take photos here.", "take photos"],
]
PAY = [
    ["pay attention (to)", "обращать внимание", "Pay attention to what the patient says.", "pay attention"],
    ["pay a compliment", "сделать комплимент", "He paid me a nice compliment.", "pay a compliment"],
    ["pay your (last) respects", "проститься с умершим", "We went to the funeral to pay our respects.", "pay your last respects"],
    ["pay tribute (to)", "воздать должное (офиц.)", "The minister paid tribute to the doctors.", "pay tribute"],
]

# Что после: сочетание | конструкция | пример | перевод
TABLE = [
    ["pay attention", "to + сущ.", "Pay attention to his speech.", "обращать внимание на"],
    ["pay tribute", "to + сущ.", "They paid tribute to the nurses.", "воздать должное"],
    ["take an interest", "in + сущ.", "She takes an interest in research.", "интересоваться"],
    ["take a liking", "to + сущ.", "He took a liking to her.", "проникнуться симпатией"],
    ["take advantage", "of + сущ.", "Take advantage of the offer.", "воспользоваться"],
    ["have a look", "at + сущ.", "Have a look at this.", "взглянуть на"],
    ["have difficulty", "+ -ing", "He has difficulty walking.", "с трудом делать"],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["We [had an argument] about the plan.", "поспорили, поссорились"], ["She [made a good argument] for surgery.", "привела веский довод в пользу операции"]],
    [["You [have a good chance] of recovery.", "у вас хорошие шансы"], ["We decided to [take a chance].", "решили рискнуть"]],
    [["She [has experience] in stroke care.", "опыт работы — (U), без a"], ["She [had a bad experience] with anaesthesia.", "случай, переживание — (C), с a"]],
    [["[Have a look] at this scan.", "британский вариант"], ["[Take a look] at this scan.", "американский — оба верны"]],
    [["We [had fun] at the party.", "нам было весело"], ["They [made fun of] him.", "они смеялись над ним"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["Can I make a photo?", "Can I take a photo?", "фото — take"],
    ["We're making a party.", "We're having a party.", "устроить вечеринку — have"],
    ["I saw a strange dream.", "I had a strange dream.", "видеть сон — have a dream"],
    ["He got an accident.", "He had an accident.", "попасть в аварию — have an accident"],
    ["Let's make a break.", "Let's have a break.", "перерыв — have или take"],
    ["Give attention to his speech.", "Pay attention to his speech.", "внимание — pay"],
    ["Pay attention on this.", "Pay attention to this.", "pay attention to"],
    ["Don't make risks.", "Don't take risks.", "рисковать — take a risk"],
    ["He made me a compliment.", "He paid me a compliment.", "комплимент — pay"],
    ["She has difficulty to walk.", "She has difficulty walking.", "have difficulty + -ing"],
]

TOPICS = [
    {"n": 1, "group": "have", "title": "have — что случилось", "sub": "авария, ссора, сон, чувство, трудности",
     "rule": "have — когда по-русски хочется сказать «у меня был(о)»: у меня была авария — I had an accident, приснился кошмар — I had a nightmare, была ссора — we had an argument, есть ощущение — I have a feeling, есть проблемы — I have problems. Трудно что-то делать — have difficulty + -ing: He has difficulty walking. Попасть в аварию — have, не get; видеть сон — have, не see.",
     "ex": [
         {"en": "He [had an accident] on his way to work.", "ru": "По дороге на работу он попал в аварию."},
         {"en": "I [had a strange dream] last night.", "ru": "Мне ночью приснился странный сон."},
         {"en": "He [has difficulty] swallowing.", "ru": "Ему трудно глотать."},
     ]},
    {"n": 2, "group": "have", "title": "have — чем заняты", "sub": "перерыв, разговор, вечеринка, попробовать",
     "rule": "have + занятие: have a break, have a chat, have a look, have a go, have a party, have fun. По-русски тут «сделать», «устроить», «поговорить», а по-английски — have. В американском английском чаще take a break, take a look — это тоже верно.",
     "ex": [
         {"en": "Let's [have a break] after the ward round.", "ru": "Давай сделаем перерыв после обхода."},
         {"en": "Can I [have a look] at the scan?", "ru": "Можно взглянуть на снимок?"},
         {"en": "Did you [have a good time] at the conference?", "ru": "Хорошо провели время на конференции?"},
     ]},
    {"n": 3, "group": "take", "title": "take — транспорт, поездки, фото", "sub": "bus, train, trip, holiday, photos",
     "rule": "take — «беру»: транспорт — take the bus, take a train, take a taxi; поездки и отпуск — take a trip, take a holiday; фото — take photos. Сфотографировать — take a photo, не make. Съездить — take a trip или go on a trip, но не go a trip.",
     "ex": [
         {"en": "I usually [take the bus] to work.", "ru": "Обычно я езжу на работу на автобусе."},
         {"en": "We [took a trip] to the mountains.", "ru": "Мы съездили в горы."},
         {"en": "Visitors may not [take photos] on the ward.", "ru": "Посетителям нельзя фотографировать в отделении."},
     ]},
    {"n": 4, "group": "take", "title": "take — риск и решительные шаги", "sub": "risk, chance, action, advantage of",
     "rule": "take a risk — рисковать; take a chance — рискнуть, попытать счастья; take action — принять меры (без артикля); take advantage of — воспользоваться возможностью. Сравни: have a chance — иметь шанс: You have a good chance of recovery. А take a chance — рискнуть: We decided to take a chance.",
     "ex": [
         {"en": "Don't [take any risks] with your health.", "ru": "Не рискуйте здоровьем."},
         {"en": "We must [take action] now.", "ru": "Нужно принимать меры сейчас."},
         {"en": "[Take advantage of] the free course.", "ru": "Воспользуйтесь бесплатным курсом."},
     ]},
    {"n": 5, "group": "take", "title": "take — отношение", "sub": "liking to, dislike to, interest in",
     "rule": "take a liking to — проникнуться симпатией, take a dislike to — невзлюбить, take an interest in — заинтересоваться, проявить интерес. Предлоги держатся крепко: liking to, dislike to, interest in.",
     "ex": [
         {"en": "The children [took a liking to] the new nurse.", "ru": "Дети сразу полюбили новую медсестру."},
         {"en": "He [took a dislike to] his new boss.", "ru": "Он невзлюбил нового начальника."},
         {"en": "She's [taken an interest in] neurology.", "ru": "Она заинтересовалась неврологией."},
     ]},
    {"n": 6, "group": "pay", "title": "pay — внимание и уважение", "sub": "attention, compliment, respects, tribute",
     "rule": "pay — «платишь» вниманием и уважением: pay attention to — обращать внимание на; pay someone a compliment — сделать комплимент; pay your last respects — проститься с умершим; pay tribute to — воздать должное (официально). Внимание — pay, не give; предлог — to, не on. Ещё: pay someone a visit — навестить.",
     "ex": [
         {"en": "[Pay attention to] the patient's speech.", "ru": "Обращайте внимание на речь пациента."},
         {"en": "He [paid her a compliment] on her talk.", "ru": "Он сделал ей комплимент по поводу доклада."},
         {"en": "The director [paid tribute to] the nurses.", "ru": "Директор воздал должное медсёстрам."},
     ]},
    {"n": 7, "group": "med", "title": "В больнице", "sub": "сверх страницы: stroke, history, blood",
     "rule": "Сверх страницы учебника, но пригодится каждый день. have — что случилось с пациентом или что ему делают: have a stroke, have a seizure, have surgery, have a scan. take — что делают врач и сестра: take a history, take blood, take someone's blood pressure; и пациент: take tablets. Пить таблетки — take, не drink.",
     "ex": [
         {"en": "She [had a stroke] two years ago.", "ru": "Два года назад она перенесла инсульт."},
         {"en": "The nurse will [take some blood].", "ru": "Сестра возьмёт кровь."},
         {"en": "[Take] one tablet twice a day.", "ru": "Принимайте по одной таблетке два раза в день."},
     ]},
    {"n": 8, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · have — что случилось
    c("h1-accident", 1, "Mr Lee ___ an accident on his way to work, but he's fine now.", "По дороге на работу мистер Ли попал в аварию, но сейчас с ним всё в порядке.",
      ["had", "got", "made"], "had", "Попасть в аварию — have an accident."),
    c("h1-row", 1, "They ___ a row about money again.", "Они опять поругались из-за денег.",
      ["had", "did", "took"], "had", "Поссориться — have a row /raʊ/ (разг.) или have an argument."),
    c("h1-argument", 1, "They ___ a terrible argument and stopped speaking to each other.", "Они ужасно поссорились и перестали разговаривать.",
      ["had", "made", "did"], "had", "Поссориться — have an argument. Make an argument — привести довод."),
    c("h1-nightmare", 1, "I ___ a terrible nightmare last night.", "Мне ночью приснился ужасный кошмар.",
      ["had", "saw", "made"], "had", "Видеть сон, кошмар — have a dream, have a nightmare. Saw a dream — калька."),
    c("h1-feeling", 1, "I ___ a feeling that something is wrong with him.", "У меня такое чувство, что с ним что-то не так.",
      ["have", "take", "make"], "have", "У меня такое чувство — I have a feeling."),
    c("h1-experience", 1, "She ___ a bad experience with anaesthesia years ago.", "Много лет назад у неё был неприятный случай с наркозом.",
      ["had", "made", "got"], "had", "Случай, переживание — have an experience (C)."),
    c("h1-difficulty", 1, "He ___ difficulty swallowing after the stroke.", "После инсульта ему трудно глотать.",
      ["has", "makes", "takes"], "has", "Трудно что-то делать — have difficulty + -ing."),
    c("h1-diff-ing", 1, "She has difficulty ___ long sentences.", "Ей трудно понимать длинные предложения.",
      ["understanding", "to understand", "understand"], "understanding", "have difficulty + -ing: difficulty understanding."),
    c("h1-problems", 1, "Are you ___ any problems with the new tablets?", "С новыми таблетками есть какие-то проблемы?",
      ["having", "making", "taking"], "having", "Есть проблемы — have problems; сейчас, в процессе — are you having problems."),

    # 2 · have — чем заняты
    c("h2-break", 2, "Let's ___ a short break after the ward round.", "Давай сделаем небольшой перерыв после обхода.",
      ["have", "make", "take"], "have", "Перерыв — have a break (брит.). Make a break — ошибка.",
      {"take": "так чаще говорят в Америке"}),
    c("h2-chat", 2, "I ___ a long chat with his daughter yesterday.", "Вчера я долго разговаривал с его дочерью.",
      ["had", "made", "did"], "had", "Поговорить, поболтать — have a chat, have a conversation."),
    c("h2-conversation", 2, "We need to ___ a serious conversation about his treatment.", "Нам нужно серьёзно поговорить о его лечении.",
      ["have", "make", "take"], "have", "Поговорить — have a conversation."),
    c("h2-look", 2, "Can I ___ a look at the CT scan?", "Можно взглянуть на КТ?",
      ["have", "make", "do"], "have", "Взглянуть — have a look (брит.), take a look (амер.)."),
    c("h2-time", 2, "Did you ___ a good time at the conference?", "Хорошо провели время на конференции?",
      ["have", "make", "spend"], "have", "Хорошо провести время — have a good time. Spend — просто «проводить»: spend a week in Paris."),
    c("h2-fun", 2, "The kids ___ great fun at the party.", "Детям на празднике было очень весело.",
      ["had", "made", "got"], "had", "Веселиться — have fun. Make fun of — смеяться над кем-то."),
    c("h2-party", 2, "We're ___ a party for her retirement on Friday.", "В пятницу устраиваем вечеринку в честь её выхода на пенсию.",
      ["having", "making", "doing"], "having", "Устроить вечеринку — have a party. Make a party — калька."),
    c("h2-go", 2, "It looks hard, but ___ a go — you'll see it's easy.", "Выглядит сложно, но попробуй — увидишь, что это легко.",
      ["have", "make", "do"], "have", "Попробовать — have a go, have a try (разг.)."),

    # 3 · take — транспорт, поездки, фото
    c("t3-bus", 3, "I usually ___ the bus to the hospital.", "Обычно я езжу в больницу на автобусе.",
      ["take", "go", "make"], "take", "Поехать на транспорте — take the bus, take a train, take a taxi."),
    c("t3-train", 3, "We ___ a train to a small town and walked from there.", "Мы доехали поездом до маленького городка, а дальше пошли пешком.",
      ["took", "went", "made"], "took", "Поехать поездом — take a train."),
    c("t3-trip", 3, "Why don't we ___ a trip to the mountains this summer?", "Может, съездим летом в горы?",
      ["take", "go", "do"], "take", "Съездить — take a trip или go on a trip (с on). Go a trip — ошибка."),
    c("t3-holiday", 3, "I'm going to ___ a holiday in October.", "В октябре я собираюсь взять отпуск.",
      ["take", "make", "do"], "take", "Взять отпуск — take a holiday (брит.), take a vacation (амер.)."),
    c("t3-photos", 3, "Visitors are not allowed to ___ photos on the ward.", "Посетителям нельзя фотографировать в отделении.",
      ["take", "make", "do"], "take", "Фотографировать — take photos. Make a photo — калька."),
    c("t3-taxi", 3, "It was late, so we ___ a taxi home.", "Было поздно, и мы поехали домой на такси.",
      ["took", "went", "made"], "took", "Поехать на такси — take a taxi."),

    # 4 · take — риск и решительные шаги
    c("t4-risk", 4, "Don't ___ any risks with your health.", "Не рискуйте своим здоровьем.",
      ["take", "make", "do"], "take", "Рисковать — take a risk."),
    c("t4-the-risk", 4, "Operating on him was risky, but we decided to ___ the risk.", "Оперировать его было рискованно, но мы решили рискнуть.",
      ["take", "make", "have"], "take", "Пойти на риск — take the risk."),
    c("t4-chance", 4, "I decided to ___ a chance and apply for the job in London.", "Я решил рискнуть и подать заявку на работу в Лондоне.",
      ["take", "have", "make"], "take", "Рискнуть — take a chance. Have a chance — иметь шанс."),
    c("t4-have-chance", 4, "You ___ a good chance of a full recovery.", "У вас хорошие шансы на полное выздоровление.",
      ["have", "take", "make"], "have", "Иметь шансы — have a chance. Take a chance — рискнуть."),
    c("t4-action", 4, "We must ___ action before the infection spreads.", "Нужно принять меры, пока инфекция не распространилась.",
      ["take", "make", "do"], "take", "Принять меры — take action, без артикля."),
    c("t4-advantage", 4, "___ advantage of the free training courses.", "Воспользуйтесь бесплатными курсами повышения квалификации.",
      ["take", "make", "have"], "take", "Воспользоваться — take advantage of."),
    c("t4-adv-of", 4, "He took advantage ___ the quiet night shift to finish his paper.", "Он воспользовался спокойной ночной сменой, чтобы дописать статью.",
      ["of", "from", "on"], "of", "take advantage of — только of."),

    # 5 · take — отношение
    c("t5-liking", 5, "The children ___ a liking to the new nurse at once.", "Дети сразу полюбили новую медсестру.",
      ["took", "had", "made"], "took", "Проникнуться симпатией — take a liking to."),
    c("t5-liking-to", 5, "He took a liking ___ her from the start.", "Она понравилась ему с самого начала.",
      ["to", "for", "on"], "to", "take a liking to — с to."),
    c("t5-dislike", 5, "For some reason, the boss ___ a dislike to him.", "Почему-то начальник его невзлюбил.",
      ["took", "had", "made"], "took", "Невзлюбить — take a dislike to."),
    c("t5-interest", 5, "The new doctor ___ a real interest in our research.", "Новый врач всерьёз заинтересовался нашим исследованием.",
      ["took", "made", "gave"], "took", "Заинтересоваться — take an interest in."),
    c("t5-interest-in", 5, "He's never taken much interest ___ politics.", "Он никогда особо не интересовался политикой.",
      ["in", "to", "for"], "in", "take an interest in — с in."),

    # 6 · pay — внимание и уважение
    c("p6-attention", 6, "Please ___ attention to the patient's speech.", "Обратите внимание на речь пациента.",
      ["pay", "make", "take"], "pay", "Обращать внимание — pay attention to."),
    c("p6-to", 6, "You should pay more attention ___ your blood pressure.", "Вам нужно внимательнее следить за давлением.",
      ["to", "on", "at"], "to", "pay attention to — с to. On — калька с «внимание на»."),
    c("p6-listen", 6, "Sorry, I wasn't ___ attention. Could you repeat that?", "Извините, я отвлёкся. Повторите, пожалуйста.",
      ["paying", "giving", "making"], "paying", "Быть внимательным — pay attention. «Я отвлёкся» — I wasn't paying attention."),
    c("p6-compliment", 6, "He ___ her a compliment on her presentation.", "Он сделал ей комплимент по поводу её доклада.",
      ["paid", "made", "did"], "paid", "Сделать комплимент — pay a compliment. Make a compliment — калька."),
    c("p6-respects", 6, "Hundreds of people came to ___ their last respects.", "Сотни людей пришли проститься.",
      ["pay", "make", "take"], "pay", "Проститься с умершим — pay your last respects."),
    c("p6-tribute", 6, "The director ___ tribute to the nurses for their work during the pandemic.", "Директор воздал должное медсёстрам за их работу во время пандемии.",
      ["paid", "made", "gave"], "paid", "Воздать должное (офиц.) — pay tribute to."),

    # 7 · В больнице
    c("m7-stroke", 7, "She ___ a stroke two years ago.", "Два года назад она перенесла инсульт.",
      ["had", "got", "made"], "had", "Перенести инсульт, инфаркт, приступ — have a stroke, a heart attack, a seizure."),
    c("m7-seizure", 7, "He ___ a seizure in the waiting room.", "В зале ожидания у него случился судорожный приступ.",
      ["had", "made", "took"], "had", "Случился приступ — have a seizure."),
    c("m7-surgery", 7, "My father is ___ surgery on his knee next week.", "На следующей неделе отцу оперируют колено.",
      ["having", "making", "doing"], "having", "Пациент — have surgery, have an operation. Хирург — do или perform surgery."),
    c("m7-scan", 7, "You need to ___ an MRI scan before we decide.", "Прежде чем решать, вам нужно сделать МРТ.",
      ["have", "make", "do"], "have", "Пациент проходит обследование — have a scan, have a blood test."),
    c("m7-history", 7, "The first step is to ___ a detailed history.", "Первым делом нужно собрать подробный анамнез.",
      ["take", "make", "collect"], "take", "Собрать анамнез — take a history."),
    c("m7-blood", 7, "The nurse will ___ some blood from your arm.", "Сестра возьмёт кровь из вены.",
      ["take", "make", "do"], "take", "Взять кровь — take blood."),
    c("m7-bp", 7, "Let me ___ your blood pressure again.", "Давайте ещё раз измерим давление.",
      ["take", "make", "do"], "take", "Измерить давление, пульс, температуру — take someone's blood pressure, pulse, temperature."),
    c("m7-tablets", 7, "___ one tablet twice a day with food.", "Принимайте по одной таблетке два раза в день во время еды.",
      ["take", "drink", "eat"], "take", "Принимать лекарство — take. Drink tablets — калька с «пить таблетки»."),
    c("m7-visit", 7, "A neurologist will ___ you a visit on the ward.", "Невролог зайдёт к вам в отделение.",
      ["pay", "make", "do"], "pay", "Навестить, зайти — pay someone a visit."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
    for o in (k.get("also") or {}):
        assert o in k["opts"] and o != k["a"], k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()), "memo", len(HAVE), len(TAKE), len(PAY))
