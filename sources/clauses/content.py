# Содержание тренажёра «Types of clauses» — по уроку 14 (Extremes) курса Awesome English B2: придаточные времени, результата,
# причины, цели, контраста и образа действия и Grammar Focus «avoiding mistakes» (as soon as I hear — без will;
# придаточное впереди — запятая). Примеры урока сохранены, кроме ошибки «buy an insurance» (insurance неисчисляемое).
# Главная идея для запоминания: придаточное отвечает на один из шести вопросов (когда? почему? что в итоге? зачем?
# вопреки чему? как?), а связку выбирают по тому, что идёт после неё: целое предложение, существительное или -ing, глагол.
# Отличие от соседей: «Связки» (link) — связки в статьях и протоколах; здесь — система урока и его ошибки.
# Разметка в примерах: [связка|a] — дальше целое предложение (оранжевый), [связка|b] — дальше существительное или -ing (синий),
# [связка|c] — дальше глагол (зелёный), [связка] без метки — отдельное слово между предложениями (подчёркнуто).
# Темы с полем late вступают в общую тренировку позже.

MIXED_TOPIC = 9

GROUPS = {
    "b1": "B1 — когда, почему, что в итоге, зачем",
    "b1p": "B1+ — хотя и несмотря на, ошибки урока",
    "b2": "B2 — however, whereas, as if",
    "mix": "Итог",
}

# Главная таблица: образец | правило («главное — пояснение») | примеры
TABLE = [
    ["[as soon as|a] I hear the news", "Когда? — when, as soon as, until, since, once; о будущем — Present, без will",
     "[when|a] I get home · [since|a] he was 20 · [by the time|a] we arrived"],
    ["[because|a] it's too risky", "Почему? — because, as, since + предложение; because of, due to + существительное",
     "[as|a] I was scared · [because of|b] the risk · [due to|b] the weather"],
    ["[so|a] we stayed at home", "Что в итоге? — so, therefore, as a result; so … that, such … that",
     "and [therefore] · [as a result of|b] the fall · [so|a] tired [that|a] I fell asleep"],
    ["[so as to|c] stay safe", "Зачем? — to, in order to, so as to + глагол; so that + предложение",
     "[to|c] save money · [so that|a] we can see · [in case|a] it rains"],
    ["[although|a] we were tired", "Вопреки чему? — although + предложение; despite, in spite of + существительное или -ing",
     "[even though|a] it rained · [despite|b] the rain · [in spite of|b] being tired"],
    ["[However], it's worth it.", "Однако — however, nevertheless: после точки, за ними запятая",
     "[Nevertheless], · [on the other hand] · [whereas|a] I prefer"],
    ["[as though|a] it was painted yesterday", "Как? — as if, as though + предложение",
     "[as if|a] he knew · feel [as if|a] I've known you"],
]

# Одна мысль — разные связки: строки [английский, перевод]; кнопка читает все строки подряд
CONTRAST = [
    [["We stayed in [because|a] it was raining.", "Мы остались дома, потому что шёл дождь. — дальше предложение"],
     ["We stayed in [because of|b] the rain.", "Мы остались дома из-за дождя. — дальше существительное"],
     ["It was raining, [so|a] we stayed in.", "Шёл дождь, поэтому мы остались дома. — результат"]],
    [["[Although|a] she was tired, she finished the climb.", "Хотя она устала, она дошла до вершины."],
     ["[Despite|b] being tired, she finished the climb.", "Несмотря на усталость, она дошла до вершины."],
     ["She was tired. [However], she finished the climb.", "Она устала. Однако дошла до вершины."]],
    [["He bought special trainers [to|c] go free running.", "Он купил кроссовки, чтобы заниматься фриранном. — дальше глагол"],
     ["He bought special trainers [so that|a] he could go free running.", "…чтобы он мог заниматься фриранном. — дальше предложение"],
     ["He bought special trainers [for|b] free running.", "…для фриранна. — дальше существительное"]],
    [["I'll email you [as soon as|a] I hear the news.", "Напишу, как только узнаю новости. — без will"],
     ["I'll call you [when|a] I get home.", "Позвоню, когда приду домой. — без will"],
     ["When will you be home?", "Когда ты будешь дома? — в вопросе will нужен"]],
    [["[As|a] many people are buying cars, the traffic is getting worse.", "Так как многие покупают машины, пробки растут. — придаточное впереди, запятая"],
     ["The traffic is getting worse [as|a] many people are buying cars.", "Пробки растут, так как многие покупают машины. — без запятой"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["I'll email you as soon as I will hear the news.", "I'll email you as soon as I hear the news.", "после as soon as, when, until — Present, не will"],
    ["As many people are buying cars the traffic is getting worse.", "As many people are buying cars, the traffic is getting worse.", "придаточное впереди — запятая"],
    ["Although we were tired, but we enjoyed the trip.", "Although we were tired, we enjoyed the trip.", "although и but вместе не ставят"],
    ["Despite of the rain, we went out.", "Despite the rain, we went out.", "despite — без of; in spite of — с of"],
    ["Despite he was tired, he kept going.", "Despite being tired, he kept going.", "после despite — существительное или -ing"],
    ["We stayed in because of it was raining.", "We stayed in because it was raining.", "because of + существительное, because + предложение"],
    ["He went to London for learning English.", "He went to London to learn English.", "цель — to do"],
    ["Take an umbrella in case it will rain.", "Take an umbrella in case it rains.", "in case — без will"],
    ["It was so cold day that we stayed in.", "It was such a cold day that we stayed in.", "such a + прилагательное + существительное"],
    ["The course is expensive, however it's worth it.", "The course is expensive. However, it's worth it.", "however — после точки, за ним запятая"],
]

TOPICS = [
    {"n": 1, "group": "b1", "title": "Когда? as soon as, since", "sub": "время: when, until, by the time",
     "rule": "Придаточное времени отвечает на вопрос «когда?»: when, while, as, before, after, until (till), as soon as, once, the moment, whenever, by the time, the first/last/next time. Главное — о будущем после этих слов ставят Present, а will только в главной части: As soon as I learn how to swim, I'll go white-water rafting. Законченное к тому моменту — Present Perfect: Don't eat until the doctor has seen you. Since — «с тех пор как»: в главной части Present Perfect, после since — Past: He's been working as an instructor since he was 20. By the time — «к тому времени, как»: By the time we arrived, the bus had left. В примере урока — buy an insurance; правильно buy insurance: слово неисчисляемое.",
     "ex": [
         {"en": "[As soon as|a] I learn how to swim, I'll go white-water rafting.", "ru": "Как только научусь плавать, пойду на рафтинг."},
         {"en": "He's been working as a skydiving instructor [since|a] he was 20.", "ru": "Он работает инструктором по прыжкам с парашютом с 20 лет."},
         {"en": "Always buy insurance [whenever|a] you plan to do high-risk activities.", "ru": "Всегда покупайте страховку, когда собираетесь заняться чем-то рискованным."},
     ]},
    {"n": 2, "group": "b1", "title": "Почему? because, because of", "sub": "причина: as, since, due to",
     "rule": "Причина — «почему?». Целое предложение (подлежащее и глагол) — после because, as, since, now that: Don't do this alone because it's too risky. I decided not to go skydiving as I was scared of heights. As и since в начале — «так как», после придаточного запятая. Существительное или -ing — после because of, due to, on account of: The flight was delayed because of the fog. The reason for + существительное, the reason why + предложение. Now that — «теперь, когда»: Now that you're here, we can start. For — «ибо», книжное, только после главной части и запятой: We turned back, for it was getting dark.",
     "ex": [
         {"en": "Don't do this alone [because|a] it's too risky.", "ru": "Не делай этого один: это слишком опасно."},
         {"en": "I decided not to go skydiving [as|a] I was scared of heights.", "ru": "Я решил не прыгать с парашютом, потому что боялся высоты."},
         {"en": "The trip was cancelled [due to|b] bad weather.", "ru": "Поездку отменили из-за плохой погоды."},
     ]},
    {"n": 3, "group": "b1", "title": "Что в итоге? so, therefore", "sub": "результат: as a result, so … that",
     "rule": "Результат — «что в итоге?». So — «поэтому» между двумя предложениями, перед ним запятая: It was raining, so we stayed in. Therefore и consequently — то же, но строже: после точки или после and: …, and therefore strained your joints. As a result, — в начале нового предложения; as a result of + существительное или -ing: His shoulders hurt as a result of going rafting. «Настолько…, что»: so + прилагательное + that (so tired that), such (a) + прилагательное + существительное + that (such a long day that).",
     "ex": [
         {"en": "It was raining, [so|a] we stayed at home.", "ru": "Шёл дождь, поэтому мы остались дома."},
         {"en": "His shoulders really hurt [as a result of|b] going white-water rafting.", "ru": "У него сильно болели плечи после рафтинга."},
         {"en": "The path was [so|a] steep [that|a] my knees hurt.", "ru": "Тропа была такой крутой, что болели колени."},
     ]},
    {"n": 4, "group": "b1", "title": "Зачем? to, so that", "sub": "цель: in order to, so as to, in case",
     "rule": "Цель — «зачем?». Глагол — после to, in order to, so as to: He bought special trainers in order to go free running. Listen to your instructor so as to stay safe. Отрицание — in order not to, so as not to: so as not to fall. Целое предложение — после so that, обычно с can, could, will, would: Speak slowly so that he can understand. In order that — то же, официально. In case — «на случай, если», без will: Take a map in case you get lost. For — с существительным (for a walk) или о назначении вещи (a knife for cutting bread); «поехал для изучения английского» — went to learn English, не for learning.",
     "ex": [
         {"en": "[In order to|c] go free running, he bought special trainers.", "ru": "Чтобы заниматься фриранном, он купил специальные кроссовки."},
         {"en": "Please listen to your instructor [so as to|c] stay safe.", "ru": "Слушайте инструктора, чтобы не пострадать."},
         {"en": "Take a map [in case|a] you get lost.", "ru": "Возьмите карту на случай, если заблудитесь."},
     ]},
    {"n": 5, "group": "b1p", "title": "Вопреки чему? although, despite", "sub": "хотя и несмотря на", "late": 0.2,
     "rule": "Контраст — «вопреки чему?». Целое предложение — после although, though, even though (even though — сильнее, «хотя даже»): Although we were very tired and dirty, we really enjoyed our trip. Существительное или -ing — после despite и in spite of: despite the rain, in spite of being tired. Despite of — ошибка: of только в in spite of. Нужно предложение после despite — despite the fact that. «Хотя…, но…» по-английски без but: although и but вместе не ставят. Yet — «и всё же», как but между предложениями: It was hard, yet we loved it.",
     "ex": [
         {"en": "[Although|a] we were very tired and dirty, we really enjoyed our trip.", "ru": "Хотя мы очень устали и испачкались, поездка нам очень понравилась."},
         {"en": "We went rafting [despite|b] the rain.", "ru": "Мы пошли на рафтинг, несмотря на дождь."},
         {"en": "[In spite of|b] being afraid of heights, she went bungee jumping.", "ru": "Хотя она боится высоты, она прыгнула с тарзанки."},
     ]},
    {"n": 6, "group": "b1p", "title": "Ошибки урока: will и запятая", "sub": "as soon as I hear · As …, …", "late": 0.25,
     "rule": "Две ошибки из Grammar Focus. Первая: после when, as soon as, before, after, until, once, in case о будущем — Present, не will: I'll email you as soon as I hear the news. В вопросе «когда?» will нужен: When will the results be ready? — это не придаточное. Вторая: если придаточное стоит впереди, после него запятая: As many people are buying cars, the traffic is getting worse. Если главное впереди — запятая обычно не нужна: The traffic is getting worse as many people are buying cars. Лишнее so после придаточного (As …, so …) — калька с «так как…, то…».",
     "ex": [
         {"en": "I'll email you [as soon as|a] I hear the news.", "ru": "Напишу вам, как только узнаю новости."},
         {"en": "[As|a] many people are buying cars, the traffic is getting worse.", "ru": "Так как многие покупают машины, пробки растут."},
         {"en": "The traffic is getting worse [as|a] many people are buying cars.", "ru": "Пробки растут, так как многие покупают машины."},
     ]},
    {"n": 7, "group": "b2", "title": "However, whereas, nevertheless", "sub": "контраст между предложениями", "late": 0.45,
     "rule": "However, nevertheless, on the other hand — отдельные слова, которые связывают два предложения: их ставят после точки (или точки с запятой), а за ними — запятая: The course is expensive. However, it's worth it. «…, however …» посреди фразы после запятой — частая ошибка. Nevertheless — «тем не менее», on the other hand — «с другой стороны»: I'd like to go bungee jumping next week, but on the other hand I should be trying to save money. Still — «всё же», перед глаголом: we still went out. While и whereas сравнивают двоих в одной фразе: My brother loves extreme sports, whereas I prefer a quiet walk.",
     "ex": [
         {"en": "I'd like to go bungee jumping next week, but [on the other hand] I should be trying to save money for my vacation.", "ru": "Хочу на следующей неделе прыгнуть с тарзанки, но, с другой стороны, надо копить на отпуск."},
         {"en": "The course is expensive. [However], it's worth every penny.", "ru": "Курс дорогой. Однако он стоит своих денег."},
         {"en": "My brother loves extreme sports, [whereas|a] I prefer a quiet walk.", "ru": "Брат обожает экстрим, а я предпочитаю спокойную прогулку."},
     ]},
    {"n": 8, "group": "b2", "title": "Как? as if, as though", "sub": "образ действия: будто", "late": 0.5,
     "rule": "«Как, будто» — as if и as though, разницы почти нет: The boat looks as though it was painted yesterday. He talks as if he knows everything — может, и знает; He talks as if he knew everything — на самом деле не знает: нереальное «будто» — прошедшее, официально were: as if she were the boss. Часто после look, sound, feel, seem: I feel as if I've known you for years. As без if — «так, как»: Do it as I showed you. В разговоре вместо as if говорят like — подробнее в тренажёре «Like и look like».",
     "ex": [
         {"en": "The boat looks [as though|a] it was painted yesterday.", "ru": "Лодка выглядит так, будто её покрасили вчера."},
         {"en": "He talks [as if|a] he knew everything about climbing.", "ru": "Он говорит так, будто знает о скалолазании всё."},
         {"en": "I feel [as if|a] I've known you for years.", "ru": "У меня такое чувство, будто я знаю вас много лет."},
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
    # 1 · Когда?
    c("c1-swim", 1, "As soon as I ___ how to swim, I'll go white-water rafting.", "Как только научусь плавать, пойду на рафтинг.",
      ["learn", "will learn", "learned"], "learn", "О будущем после as soon as — Present: as soon as I learn. Will — только в главной части."),
    c("c1-moment", 1, "I knew something was wrong ___ I saw his face.", "Я понял, что что-то не так, как только увидел его лицо.",
      ["the moment", "by the time", "until"], "the moment", "the moment — в ту же секунду, как. By the time — к тому времени, как; until — пока не."),
    c("c1-until", 1, "Please don't eat anything until the doctor ___ you.", "Пожалуйста, ничего не ешьте, пока вас не осмотрит врач.",
      ["has seen", "will see", "is seeing"], "has seen", "until — «пока не», без will: until the doctor has seen you (или sees you)."),
    c("c1-since", 1, "He has worked as an instructor ___ he was twenty.", "Он работает инструктором с двадцати лет.",
      ["since", "for", "from"], "since", "since + момент или событие: since he was twenty. For — срок: for ten years."),
    c("c1-bytime", 1, "By the time the ambulance arrived, the climber ___ consciousness.", "К приезду скорой альпинист уже пришёл в себя.",
      ["had regained", "regained", "has regained"], "had regained", "By the time — «к тому времени, как»: что случилось раньше другого прошедшего — Past Perfect."),
    c("c1-whenever", 1, "Always buy insurance ___ you plan to do high-risk activities.", "Всегда покупайте страховку, когда собираетесь заняться чем-то рискованным.",
      ["whenever", "however", "whatever"], "whenever", "whenever — всякий раз, когда. В уроке — buy an insurance; правильно buy insurance."),

    # 2 · Почему?
    c("c2-because", 2, "Don't go climbing alone ___ it's too risky.", "Не ходи в горы один: это слишком опасно.",
      ["because", "because of", "due to"], "because", "Дальше целое предложение (it's too risky) — because."),
    c("c2-of", 2, "The flight was delayed ___ the fog.", "Рейс задержали из-за тумана.",
      ["because of", "because", "since"], "because of", "Дальше существительное (the fog) — because of."),
    c("c2-due", 2, "The match was cancelled ___ heavy rain.", "Матч отменили из-за сильного дождя.",
      ["due to", "as", "because"], "due to", "due to + существительное: due to heavy rain. As и because — с целым предложением."),
    c("c2-as", 2, "___ I was scared of heights, I decided not to go skydiving.", "Так как я боялся высоты, я решил не прыгать с парашютом.",
      ["As", "Due to", "Because of"], "As", "As + предложение — «так как». Придаточное впереди — запятая."),
    c("c2-nowthat", 2, "___ you've got your licence, you can drive to work.", "Теперь, когда у тебя есть права, можешь ездить на работу на машине.",
      ["Now that", "Since that", "Because of"], "Now that", "Now that — «теперь, когда». Since that — так не говорят."),
    c("c2-reason", 2, "The reason ___ the delay was a technical problem.", "Причиной задержки была техническая неполадка.",
      ["for", "why", "of"], "for", "the reason for + существительное; the reason why + предложение: the reason why we were late."),

    # 3 · Что в итоге?
    c("c3-so", 3, "It was raining, ___ we stayed at home.", "Шёл дождь, поэтому мы остались дома.",
      ["so", "because", "as"], "so", "Результат — so. С because и as получилось бы, что дождь шёл из-за того, что мы остались дома."),
    c("c3-therefore", 3, "You've been walking down a steep path for three hours, and ___ strained your joints.", "Вы три часа спускались по крутой тропе и поэтому потянули суставы.",
      ["therefore", "because", "although"], "therefore", "and therefore — «и поэтому», результат."),
    c("c3-of", 3, "His shoulders hurt as a result ___ going white-water rafting.", "У него болят плечи после рафтинга.",
      ["of", "to", "from"], "of", "as a result of + существительное или -ing."),
    c("c3-such", 3, "It was ___ cold day that we stayed in.", "Был такой холодный день, что мы не выходили из дома.",
      ["such a", "so", "so a"], "such a", "such a + прилагательное + существительное: such a cold day. So — без существительного: so cold that."),
    c("c3-sotired", 3, "I was ___ tired that I fell asleep on the bus.", "Я так устал, что уснул в автобусе.",
      ["so", "such", "such a"], "so", "so + прилагательное: so tired that."),
    c("c3-asresult", 3, "The roads were icy. ___, there were several accidents.", "Дороги обледенели. В результате случилось несколько аварий.",
      ["As a result", "As a result of", "Because"], "As a result", "As a result, — в начале нового предложения, с запятой. As a result of — только перед существительным."),

    # 4 · Зачем?
    c("c4-learn", 4, "She went to London ___ English.", "Она поехала в Лондон учить английский.",
      ["to learn", "for learning", "for learn"], "to learn", "Цель человека — to do: to learn. For learning — калька «для изучения»."),
    c("c4-soasnot", 4, "Walk slowly ___ fall on the ice.", "Иди медленно, чтобы не упасть на льду.",
      ["so as not to", "so not as to", "not so as to"], "so as not to", "Отрицание цели — so as not to, in order not to: not перед to."),
    c("c4-sothat", 4, "Speak slowly ___ everyone can understand you.", "Говорите медленно, чтобы все вас поняли.",
      ["so that", "in order to", "so as to"], "so that", "Дальше целое предложение (everyone can understand) — so that."),
    c("c4-incase", 4, "Take a torch in case it ___ dark before we get back.", "Возьми фонарик на случай, если стемнеет до нашего возвращения.",
      ["gets", "will get", "would get"], "gets", "in case — без will: in case it gets dark."),
    c("c4-for", 4, "We went out ___ a walk.", "Мы вышли прогуляться.",
      ["for", "to", "so that"], "for", "for + существительное: for a walk, for a coffee. To — с глаголом: to have a walk."),
    c("c4-inorder", 4, "___ to reduce the risk, always wear a helmet.", "Чтобы снизить риск, всегда надевайте шлем.",
      ["In order", "So that", "For"], "In order", "In order to + глагол — «чтобы». So that — с целым предложением."),

    # 5 · Вопреки чему?
    c("c5-although", 5, "___ we were very tired, we really enjoyed our trip.", "Хотя мы очень устали, поездка нам очень понравилась.",
      ["Although", "Despite", "In spite of"], "Although", "Дальше целое предложение (we were tired) — although."),
    c("c5-despite", 5, "___ the rain, we went white-water rafting.", "Несмотря на дождь, мы пошли на рафтинг.",
      ["Despite", "Although", "Even though"], "Despite", "Дальше существительное (the rain) — despite."),
    c("c5-of", 5, "We went out in spite ___ the storm.", "Мы вышли, несмотря на бурю.",
      ["of", "from", "to"], "of", "in spite of — с of; despite — без of."),
    c("c5-being", 5, "Despite ___ tired, she finished the climb.", "Несмотря на усталость, она дошла до вершины.",
      ["being", "she was", "to be"], "being", "После despite — -ing: despite being tired. С предложением — although she was tired."),
    c("c5-but", 5, "___", "Хотя было дорого, мы это купили.",
      ["Although it was expensive, we bought it.", "Although it was expensive, but we bought it.", "Despite it was expensive, we bought it."],
      "Although it was expensive, we bought it.", "«Хотя…, но…» по-английски без but. Despite + предложение — ошибка."),
    c("c5-yet", 5, "The trip was long and exhausting, ___ we loved every minute of it.", "Поездка была долгой и утомительной, и всё же нам понравилась каждая минута.",
      ["yet", "despite", "in spite"], "yet", "yet — «и всё же», как but между предложениями."),

    # 6 · Ошибки урока: will и запятая
    c("c6-comma", 6, "___", "Так как многие покупают машины, пробки растут.",
      ["As many people are buying cars, the traffic is getting worse.", "As many people are buying cars the traffic is getting worse.",
       "As many people are buying cars, so the traffic is getting worse."],
      "As many people are buying cars, the traffic is getting worse.", "Придаточное впереди — запятая. So после него — калька «так как…, то…»."),
    c("c6-nocomma", 6, "___", "Пробки растут, так как многие покупают машины.",
      ["The traffic is getting worse as many people are buying cars.", "The traffic is getting worse because of many people are buying cars."],
      "The traffic is getting worse as many people are buying cars.", "Главное впереди — без запятой. Because of + предложение — ошибка."),
    c("c6-before", 6, "Before you ___ climbing, check your harness.", "Прежде чем начать подъём, проверьте страховочную систему.",
      ["start", "will start", "started"], "start", "before + Present о будущем: before you start."),
    c("c6-once", 6, "Once you ___ the course, you'll get a certificate.", "Как только закончите курс, получите сертификат.",
      ["have completed", "will complete", "completed"], "have completed", "once — «как только»; законченное к тому моменту — Present Perfect, не will. Можно и once you complete."),
    c("c6-when", 6, "When ___ the results be ready?", "Когда будут готовы результаты?",
      ["will", "do", "are"], "will", "В вопросе «когда?» will нужен. Без will — только в придаточном: I'll call you when they're ready."),
    c("c6-tell", 6, "I'll tell you as soon as the results ___ ready.", "Скажу вам, как только будут готовы результаты.",
      ["are", "will be", "would be"], "are", "Придаточное после as soon as — Present: as soon as they are ready."),

    # 7 · However, whereas, nevertheless
    c("c7-however", 7, "___", "Курс дорогой. Однако он того стоит.",
      ["The course is expensive. However, it's worth it.", "The course is expensive, however it's worth it.", "However the course is expensive, it's worth it."],
      "The course is expensive. However, it's worth it.", "However — после точки, за ним запятая. However в значении «хотя» — ошибка."),
    c("c7-nevertheless", 7, "The weather was terrible. ___, we reached the summit.", "Погода была ужасной. Тем не менее мы дошли до вершины.",
      ["Nevertheless", "Although", "Despite"], "Nevertheless", "Nevertheless, — «тем не менее», начинает новое предложение. Although и despite связывают части одной фразы."),
    c("c7-hand", 7, "I'd like to go bungee jumping, but on the other ___ I should be saving money.", "Хочу прыгнуть с тарзанки, но, с другой стороны, надо копить деньги.",
      ["hand", "side", "way"], "hand", "on the other hand — «с другой стороны»."),
    c("c7-whereas", 7, "I love extreme sports, ___ my wife prefers a quiet holiday by the sea.", "Я обожаю экстрим, а жена предпочитает спокойный отдых у моря.",
      ["whereas", "however", "despite"], "whereas", "whereas, while — «а, тогда как»: сравнение двоих в одной фразе."),
    c("c7-still", 7, "It was pouring with rain, but we ___ went out.", "Лил дождь, но мы всё же вышли.",
      ["still", "yet still", "however"], "still", "still — «всё же», перед смысловым глаголом: we still went out."),
    c("c7-while", 7, "___ some people love heights, others are terrified of them.", "Одни обожают высоту, а другие её боятся.",
      ["While", "However", "Despite"], "While", "While — «в то время как»: While some people…, others…"),

    # 8 · Как? as if, as though
    c("c8-boat", 8, "The boat looks ___ it was painted yesterday.", "Лодка выглядит так, будто её покрасили вчера.",
      ["as though", "as", "like as"], "as though", "as though = as if — «будто»."),
    c("c8-knew", 8, "He talks as if he ___ everything, but he's never been climbing.", "Он говорит так, будто всё знает, а сам ни разу не был в горах.",
      ["knew", "will know", "has known"], "knew", "Нереальное «будто» (на самом деле не знает) — прошедшее: as if he knew."),
    c("c8-were", 8, "She gives orders as if she ___ the boss.", "Она командует, будто она начальница.",
      ["were", "is being", "will be"], "were", "Нереальное — прошедшее; официально were: as if she were the boss, в разговоре — was."),
    c("c8-feel", 8, "I feel ___ I've known you for years.", "У меня такое чувство, будто я знаю вас много лет.",
      ["as if", "as", "so that"], "as if", "feel as if — «такое чувство, будто»."),
    c("c8-rain", 8, "Look at those clouds. It looks ___ it's going to rain.", "Посмотри на тучи. Похоже, пойдёт дождь.",
      ["as if", "so that", "as a result"], "as if", "«Похоже, что» — looks as if; в разговоре — looks like."),
    c("c8-as", 8, "Do it ___ I showed you.", "Сделай так, как я показал.",
      ["as", "as if", "like as"], "as", "as — «так, как»; as if — «будто»."),
]

assert len({c["id"] for c in CARDS}) == len(CARDS)
assert all(c["a"] in c["opts"] for c in CARDS)
assert all(c["q"].count("___") == 1 for c in CARDS)
assert {c["t"] for c in CARDS} == {t["n"] for t in TOPICS if t["n"] != MIXED_TOPIC}
