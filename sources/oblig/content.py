# Содержание тренажёра «Have to, must и похожие» — обязанность, необходимость и вынужденность, от B1 к B2.
# Пометка […] — ключевой глагол; цвет: must — оранжевый, have (got) to — синий,
# should, ought to, had better — зелёный, остальные (need, supposed, forced, required…) подчёркнуты.
# Темы с полем late вступают в общую тренировку позже: сначала B1, потом B1+, потом B2.

MIXED_TOPIC = 13

GROUPS = {
    "b1": "B1 — опора",
    "b1p": "B1+ — живая речь",
    "b2": "B2 — точность и регистр",
    "mix": "Итог",
}

# Главная таблица: глагол | смысл («главное — пояснение») | смысл отрицания | отрицательная форма
TABLE = [
    ["must", "обязательно — решил сам; правила на письме", "нельзя!", "mustn't"],
    ["have to", "надо — так требуют обстоятельства", "не обязательно", "don't have to"],
    ["need to", "нужно — для дела, для результата", "не нужно", "don't need to · needn't"],
    ["have got to", "надо — разговорное, только настоящее", "не обязательно", "haven't got to"],
    ["be supposed to", "положено — по плану, правилам, договорённости", "не положено", "not supposed to"],
    ["had better", "лучше бы — а то будут проблемы", "лучше не надо", "had better not"],
    ["be forced to", "вынужден — против воли", "не вынуждали", "wasn't forced to"],
    ["be required to", "обязан — официально: закон, протокол", "не обязан", "not required to"],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["You [mustn't] wear anything metal in the scanner.", "нельзя"],
     ["You [don't need to] fast before the MRI.", "не нужно"],
     ["You're [not supposed to] move during the scan.", "не положено"]],
    [["He [must have] left early.", "наверное, ушёл"],
     ["He [had to] leave early.", "пришлось уйти"],
     ["He [was supposed to] stay until nine.", "должен был остаться — по плану"],
     ["He [should have] stayed until nine.", "надо было остаться — упрёк"]],
    [["I [didn't need to] wait — I had an appointment.", "не нужно было, и не ждал"],
     ["I [needn't have] waited — the results were already online.", "ждал, но зря"]],
    [["They [made] him wait four hours.", "заставили — make без to"],
     ["He [was made to] wait four hours.", "его заставили — в пассиве с to"],
     ["He [had no choice but to] wait.", "ему ничего не оставалось"]],
    [["You [should] rest more.", "совет"],
     ["You['d better] rest, or the headache will come back.", "предупреждение"],
     ["You're [supposed to] rest — doctor's orders.", "так велено"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["You had better to call him.", "You had better call him.", "после had better — без to"],
    ["You'd better not to tell her.", "You'd better not tell her.", "had better not — тоже без to"],
    ["They made us to wait.", "They made us wait.", "make кого-то — без to"],
    ["We were made wait.", "We were made to wait.", "в пассиве — с to"],
    ["Yesterday I've got to stay late.", "Yesterday I had to stay late.", "have got to — только настоящее"],
    ["You don't need bring anything.", "You don't need to bring anything.", "don't need — с to"],
    ["You needn't to come.", "You needn't come.", "needn't — без to"],
    ["He is suppose to come at nine.", "He is supposed to come at nine.", "supposed — с -d, хоть его и не слышно"],
    ["Staff are prohibited to use phones.", "Staff are prohibited from using phones.", "prohibited from + -ing"],
    ["He must leave early yesterday.", "He had to leave early yesterday.", "пришлось в прошлом — had to"],
]

TOPICS = [
    {"n": 1, "group": "b1", "title": "must или have to", "sub": "кто решает · нельзя или не нужно",
     "rule": "Спроси себя, кто решил. Решил сам или так написано в правилах — must: I must call the lab. Visitors must sign in. Требуют обстоятельства: график, работа, болезнь — have to: My shift starts at eight, so I have to get up at six. В речи have to встречается намного чаще. В отрицании смысл расходится: mustn't — нельзя, don't have to — не обязательно.",
     "ex": [
         {"en": "Visitors [must] sign in at reception.", "ru": "Посетители обязаны отметиться на стойке регистрации."},
         {"en": "My shift starts at eight, so I [have to] get up at six.", "ru": "Смена в восемь, так что мне приходится вставать в шесть."},
         {"en": "You [don't have to] wear a tie — the dress code is casual.", "ru": "Галстук не обязателен — дресс-код свободный."},
     ]},
    {"n": 2, "group": "b1", "title": "have to во всех временах", "sub": "had to · has had to · would have to",
     "rule": "have to — обычный глагол, поэтому у него есть все времена и формы, а у must их нет. Пришлось — had to; уже пришлось — has had to; придётся — will have to; пришлось бы — would have to; раньше приходилось — used to have to; после like, hate, avoid — having to. Вопрос и отрицание — через do: Did you have to wait? We didn't have to pay.",
     "ex": [
         {"en": "The anaesthetist was ill, so we [had to] postpone the operation.", "ru": "Анестезиолог заболел, и нам пришлось перенести операцию."},
         {"en": "The ward [has had to] close twice this winter.", "ru": "Этой зимой отделение уже дважды приходилось закрывать."},
         {"en": "If the scan were positive, we [would have to] start treatment at once.", "ru": "Будь снимок положительным, лечение пришлось бы начинать сразу."},
     ]},
    {"n": 3, "group": "b1", "title": "need to и needn't", "sub": "нужно · не нужно · needs changing",
     "rule": "need to — нужно, это необходимо для дела: You need to drink more water. Не нужно — don't need to, а в британском ещё needn't, без to: You needn't worry. Вопрос — Do I need to…? Need + -ing имеет пассивный смысл: The dressing needs changing — повязку нужно менять, то же, что needs to be changed.",
     "ex": [
         {"en": "You [need to] drink at least two litres of water a day.", "ru": "Вам нужно пить не меньше двух литров воды в день."},
         {"en": "You [don't need to] fast before this blood test.", "ru": "Перед этим анализом голодать не нужно."},
         {"en": "The dressing [needs] changing every day.", "ru": "Повязку нужно менять каждый день."},
     ]},
    {"n": 4, "group": "b1p", "title": "have got to и gotta", "sub": "разговорное «надо» · только настоящее", "late": 0.2,
     "rule": "have got to — разговорное «надо», особенно в британском: I've got to go. Работает только в настоящем: прошлое — had to, будущее — will have to. Вопрос — Have you got to…?, отрицание — haven't got to, то есть не обязательно. В быстрой речи и переписке — gotta: Gotta run! В документах и письмах коллегам по делу — have to.",
     "ex": [
         {"en": "Sorry, I've [got to] go — my shift starts in ten minutes.", "ru": "Извини, мне пора — смена через десять минут."},
         {"en": "[Have] we [got to] fill in all these forms?", "ru": "Нам обязательно заполнять все эти бланки?"},
         {"en": "[Gotta] run — talk later!", "ru": "Бегу, потом поговорим!"},
     ]},
    {"n": 5, "group": "b1p", "title": "be supposed to", "sub": "положено · должен был, но…", "late": 0.2,
     "rule": "be supposed to — «положено, так задумано»: так велели, договорились, так в правилах или в графике. You're supposed to take it after meals. В прошлом — was supposed to: «должен был, но не вышло». The results were supposed to come back yesterday. Not supposed to — «не положено», мягче mustn't и часто о правиле, которое нарушают. В британском то же — be meant to.",
     "ex": [
         {"en": "You're [supposed to] take these tablets after meals.", "ru": "Эти таблетки положено принимать после еды."},
         {"en": "The results [were supposed to] come back yesterday.", "ru": "Результаты должны были прийти вчера (но не пришли)."},
         {"en": "Visitors [aren't supposed to] use their phones in the ICU.", "ru": "Посетителям не положено пользоваться телефонами в реанимации."},
     ]},
    {"n": 6, "group": "b1p", "title": "had better и ought to", "sub": "лучше бы, а то… · стоило бы", "late": 0.25,
     "rule": "had better (’d better) + глагол без to — «лучше бы, а то будут проблемы»: это предупреждение, а не мягкий совет. You'd better call the family. Отрицание — had better not. Хотя had, речь о сейчас и о будущем. ought to — то же, что should, чуть весомее: You ought to get that mole checked. Мягкий совет — should; had better звучит почти как приказ.",
     "ex": [
         {"en": "He's deteriorating — you['d better] call the family.", "ru": "Ему хуже — лучше позвоните родственникам, не откладывайте."},
         {"en": "We['d better not] start without the anaesthetist.", "ru": "Лучше не начинать без анестезиолога."},
         {"en": "You [ought to] get that mole checked.", "ru": "Вам стоило бы показать эту родинку врачу."},
     ]},
    {"n": 7, "group": "b2", "title": "be forced to", "sub": "вынужден · no choice but to", "late": 0.45,
     "rule": "be forced to — «вынужден»: давят обстоятельства или люди, по своей воле не стал бы. The hospital was forced to cancel planned operations. Ничего не оставалось, кроме как… — have no choice but to + глагол: We had no choice but to intubate. Формально и о моральном долге — feel compelled to. Обычное «пришлось» без драмы — по-прежнему had to.",
     "ex": [
         {"en": "The hospital [was forced to] cancel all planned operations.", "ru": "Больница была вынуждена отменить все плановые операции."},
         {"en": "We [had no choice but to] intubate him.", "ru": "Нам ничего не оставалось, кроме как его интубировать."},
         {"en": "The authors felt [compelled to] withdraw the paper.", "ru": "Авторы сочли себя обязанными отозвать статью."},
     ]},
    {"n": 8, "group": "b2", "title": "make, force, get", "sub": "заставить · уговорить · was made to", "late": 0.45,
     "rule": "Заставить — make + кого-то + глагол без to: They made him wait. В пассиве to возвращается: He was made to wait. force и get — всегда с to: force someone to do — заставить силой или правилами, get someone to do — уговорить, добиться. Make без to работает и в значении «вызывать»: The exam made me feel like a student again.",
     "ex": [
         {"en": "They [made] him wait four hours in A&E.", "ru": "Его заставили прождать четыре часа в приёмном."},
         {"en": "He [was made to] wait four hours.", "ru": "Его заставили ждать четыре часа."},
         {"en": "We finally [got] him [to] stop smoking.", "ru": "В итоге мы уговорили его бросить курить."},
     ]},
    {"n": 9, "group": "b2", "title": "be required to, be obliged to", "sub": "протоколы, правила, статьи", "late": 0.5,
     "rule": "В официальных текстах вместо have to — be required to: All staff are required to complete the training. По закону или по долгу — be obliged to: Doctors are obliged to report certain infections. Не обязаны — are not required to, это то же, что don't have to, а не запрет. Прилагательные «обязательный» — mandatory, compulsory: Written consent is mandatory. Активный залог — require: The protocol requires two readings.",
     "ex": [
         {"en": "All staff [are required to] complete annual safety training.", "ru": "Все сотрудники обязаны ежегодно проходить обучение по безопасности."},
         {"en": "Doctors [are obliged to] report certain infectious diseases.", "ru": "Врачи обязаны сообщать о некоторых инфекционных болезнях."},
         {"en": "Participants [are not required to] give a reason for leaving the study.", "ru": "Участники не обязаны объяснять, почему выходят из исследования."},
     ]},
    {"n": 10, "group": "b2", "title": "didn't need to или needn't have", "sub": "не пришлось · сделал зря", "late": 0.55,
     "rule": "Два вопроса: сделал или нет? Не нужно было и не делал — didn't need to или didn't have to: I didn't need to queue — I had an appointment. Сделал, а оказалось, что зря, — needn't have + третья форма: You needn't have come in — we could have talked by phone. Вежливое «ну зачем же» на подарок — You needn't have! или You shouldn't have!",
     "ex": [
         {"en": "I [didn't need to] queue — I had an appointment.", "ru": "В очереди стоять не пришлось — у меня была запись."},
         {"en": "You [needn't have] come in — we could have talked by phone.", "ru": "Зря вы приезжали — можно было поговорить по телефону."},
         {"en": "We [needn't have] ordered a CT — the diagnosis was clear.", "ru": "Зря назначили КТ — диагноз был ясен."},
     ]},
    {"n": 11, "group": "b2", "title": "Запрет: от мягкого к строгому", "sub": "not supposed to · can't · not allowed · prohibited", "late": 0.55,
     "rule": "Шкала строгости. not supposed to — не положено, но бывает. can't — нельзя по правилам, так чаще всего говорят: You can't park here. not allowed to — запрещено: Visitors aren't allowed to bring food. mustn't — категорично, от говорящего: You mustn't drive yet. be prohibited from + -ing, is not permitted — официальный язык объявлений и приказов.",
     "ex": [
         {"en": "You [can't] park here — this space is for ambulances.", "ru": "Здесь парковаться нельзя — это место для скорых."},
         {"en": "Visitors [aren't allowed to] bring food into the ward.", "ru": "Посетителям нельзя приносить еду в отделение."},
         {"en": "Staff [are prohibited from] sharing patient data online.", "ru": "Сотрудникам запрещено публиковать данные пациентов в интернете."},
     ]},
    {"n": 12, "group": "b2", "title": "«Должен был»: четыре перевода", "sub": "must have · had to · was supposed to · should have", "late": 0.6,
     "rule": "Русское «должен был» переводят четырьмя способами — спроси, что имеется в виду. Наверное, сделал — must have done: He must have left early. Пришлось — had to: He had to leave early. Должен был по плану, но не сделал — was supposed to: He was supposed to present the case. Надо было, а он не сделал, упрёк — should have done: He should have stayed.",
     "ex": [
         {"en": "His coat is gone — he [must have] left early.", "ru": "Пальто нет — наверное, он рано ушёл."},
         {"en": "He [was supposed to] present the case, but he didn't turn up.", "ru": "Он должен был докладывать случай, но не пришёл."},
         {"en": "He [should have] stayed until the handover.", "ru": "Ему надо было остаться до передачи смены."},
     ]},
    {"n": 13, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · must или have to
    c("o1-shift", 1, "My shift starts at eight, so I ___ get up at six.", "Смена начинается в восемь, так что мне приходится вставать в шесть.",
      ["have to", "must to", "has to"], "have to", "Так требует график — have to. Must to — ошибка, has to — для he и she."),
    c("o1-sign", 1, "Notice in the ward: Visitors ___ sign in at reception.", "Объявление в отделении: посетители обязаны отметиться на стойке регистрации.",
      ["must", "must to", "have"], "must", "Письменные правила и объявления — must, после него глагол без to."),
    c("o1-bp", 1, "He ___ check his blood pressure twice a day.", "Ему приходится мерить давление два раза в день.",
      ["has to", "have to", "must to"], "has to", "Он — has to."),
    c("o1-masks", 1, "___ we have to wear masks in the corridor?", "Нам обязательно носить маски в коридоре?",
      ["Do", "Must", "Have"], "Do", "Вопрос с have to — через do: Do we have to…? Have we to…? — устарело."),
    c("o1-gloves", 1, "You ___ touch the sterile field without gloves.", "Нельзя касаться стерильного поля без перчаток.",
      ["mustn't", "don't have to"], "mustn't", "Нельзя, запрет — mustn't."),
    c("o1-tie", 1, "You ___ wear a tie — the dress code is casual.", "Галстук носить не обязательно — дресс-код свободный.",
      ["don't have to", "mustn't"], "don't have to", "Не обязательно, можно не делать — don't have to."),

    # 2 · have to во всех временах
    c("o2-postpone", 2, "The anaesthetist was ill, so we ___ postpone the operation.", "Анестезиолог заболел, и нам пришлось перенести операцию.",
      ["had to", "must", "have to"], "had to", "Пришлось в прошлом — had to: у must прошедшего нет."),
    c("o2-close", 2, "The ward ___ close twice this winter because of flu.", "Этой зимой отделение уже дважды приходилось закрывать из-за гриппа.",
      ["has had to", "has must", "had to have"], "has had to", "Уже пришлось, итог к сегодняшнему дню — Present Perfect: has had to."),
    c("o2-would", 2, "If the scan were positive, we ___ start treatment at once.", "Будь снимок положительным, лечение пришлось бы начинать сразу.",
      ["would have to", "would must", "will have to"], "would have to", "Пришлось бы — would have to. Will have to — «придётся», без «бы»."),
    c("o2-having", 2, "Nobody likes ___ give bad news to families.", "Никому не нравится, когда приходится сообщать родственникам плохие новости.",
      ["having to", "must", "to must"], "having to", "После like, hate, avoid — форма на -ing: having to. У must такой формы нет."),
    c("o2-intern", 2, "When I was an intern, I ___ work every other weekend.", "Когда я был интерном, мне приходилось работать через выходные.",
      ["used to have to", "used to must", "had got to"], "used to have to", "Раньше приходилось — used to have to: must так не умеет."),
    c("o2-january", 2, "From January, all residents ___ log their procedures online.", "С января всем ординаторам придётся вносить свои процедуры в электронный журнал.",
      ["will have to", "will must", "must to"], "will have to", "Придётся — will have to."),

    # 3 · need to и needn't
    c("o3-water", 3, "You ___ drink at least two litres of water a day.", "Вам нужно пить не меньше двух литров воды в день.",
      ["need to", "need", "needn't"], "need to", "В утверждении — need to + глагол. Без to need ставят только в needn't и в книжном вопросе Need I…?"),
    c("o3-fast", 3, "You ___ fast before this blood test — eat as usual.", "Перед этим анализом голодать не нужно — ешьте как обычно.",
      ["don't need to", "mustn't", "need not to"], "don't need to", "Не нужно — don't need to. Mustn't — запрет, need not to — ошибка: needn't без to."),
    c("o3-worry", 3, "You ___ worry — the scan is completely normal.", "Не волнуйтесь — снимок совершенно нормальный.",
      ["needn't", "needn't to", "don't need"], "needn't", "needn't + глагол без to. Don't need без to перед глаголом не ставят."),
    c("o3-scans", 3, "Do I ___ bring my old scans to the appointment?", "Мне нужно брать с собой старые снимки на приём?",
      ["need to", "need", "must"], "need to", "Вопрос — Do I need to…? Do I must — так не говорят."),
    c("o3-dressing", 3, "The dressing needs ___ every day.", "Повязку нужно менять каждый день.",
      ["changing", "to change", "change"], "changing", "need + -ing — пассивный смысл: needs changing = needs to be changed. Needs to change — повязка сама должна измениться."),
    c("o3-checked", 3, "The results need ___ checked by a second radiologist.", "Результаты должен перепроверить второй рентгенолог.",
      ["to be", "being", "be"], "to be", "Пассив после need — to be + третья форма: need to be checked."),

    # 4 · have got to и gotta
    c("o4-go", 4, "Sorry, I've ___ go — my shift starts in ten minutes.", "Извини, мне пора — смена начинается через десять минут.",
      ["got to", "got", "to"], "got to", "Разговорное «надо» — I've got to go."),
    c("o4-see", 4, "You've got ___ this scan — it's incredible.", "Тебе обязательно надо посмотреть этот снимок — он невероятный.",
      ["to see", "see", "seeing"], "to see", "have got to + глагол: You've got to see."),
    c("o4-night", 4, "Last night I ___ stay until the patient was stable.", "Вчера вечером мне пришлось остаться, пока пациент не стабилизировался.",
      ["had to", "had got to", "'ve got to"], "had to", "have got to бывает только в настоящем. Пришлось — had to."),
    c("o4-forms", 4, "___ we got to fill in all these forms?", "Нам обязательно заполнять все эти бланки?",
      ["Have", "Do", "Are"], "Have", "Вопрос с got — Have we got to…? Без got — Do we have to…?"),
    c("o4-sunday", 4, "You ___ got to come in on Sunday — the ward is covered.", "В воскресенье приходить не обязательно — дежурный в отделении есть.",
      ["haven't", "don't", "mustn't"], "haven't", "haven't got to = don't have to: не обязательно."),
    c("o4-gotta", 4, "___ run — talk later!", "Бегу, потом поговорим! (сообщение коллеге)",
      ["Gotta", "Must to", "Got"], "Gotta", "gotta — have got to в быстрой речи и переписке. В документах — have to."),

    # 5 · be supposed to
    c("o5-meals", 5, "You're ___ take these tablets after meals, not on an empty stomach.", "Эти таблетки положено принимать после еды, а не натощак.",
      ["supposed to", "suppose to", "supposed"], "supposed to", "be supposed to + глагол. Suppose to — ошибка на слух: -d не слышно, но пишется."),
    c("o5-results", 5, "The results ___ come back yesterday, but the lab lost the sample.", "Результаты должны были прийти вчера, но лаборатория потеряла образец.",
      ["were supposed to", "must have", "had to"], "were supposed to", "Должны были по плану, но не вышло — was или were supposed to. Had to — «пришлось», must have — «наверное»."),
    c("o5-phones", 5, "Visitors ___ use their phones in the ICU, but some still do.", "Посетителям не положено пользоваться телефонами в реанимации, но некоторые всё равно пользуются.",
      ["aren't supposed to", "don't have to", "needn't"], "aren't supposed to", "Не положено, а правило нарушают — not supposed to. Don't have to и needn't — «не обязательно»."),
    c("o5-rota", 5, "Who ___ be on call tonight? The rota is blank.", "Кто сегодня ночью должен дежурить? В графике пусто.",
      ["is supposed to", "supposes to", "should have"], "is supposed to", "Кто должен по графику — is supposed to. Supposes to — ошибка: нужен пассив be supposed to."),
    c("o5-meant", 5, "This drug is ___ to be taken with food.", "Этот препарат полагается принимать с едой.",
      ["meant", "mean", "meaning"], "meant", "be meant to = be supposed to, чаще в британском: так задумано."),
    c("o5-round", 5, "It's 9:30. The ward round ___ start at nine — where is everyone?", "Уже 9:30. Обход должен был начаться в девять — где все?",
      ["was supposed to", "must", "is supposed"], "was supposed to", "Должен был начаться, но не начался — was supposed to."),

    # 6 · had better и ought to
    c("o6-call", 6, "He's deteriorating — you'd better ___ the family.", "Ему хуже — лучше позвоните родственникам.",
      ["call", "to call", "calling"], "call", "had better + глагол без to."),
    c("o6-not", 6, "We'd better ___ start without the anaesthetist.", "Лучше не начинать без анестезиолога.",
      ["not", "not to", "don't"], "not", "Отрицание — had better not + глагол без to."),
    c("o6-dose", 6, "You ___ better check the dose again — it looks too high.", "Лучше перепроверь дозу — она кажется слишком большой.",
      ["had", "would", "should"], "had", "Только had better (’d better). Would better — ошибка."),
    c("o6-mole", 6, "You ought ___ that mole checked.", "Вам стоило бы показать эту родинку врачу.",
      ["to get", "get", "getting"], "to get", "ought to + глагол: в отличие от should, с to."),
    c("o6-warn", 6, "You ___ take your anticoagulant every day, or you could have another stroke.", "Принимайте антикоагулянт каждый день, иначе может случиться повторный инсульт.",
      ["had better", "would rather", "ought"], "had better", "Предупреждение «а то будет плохо» — had better. Would rather — «предпочёл бы», ought без to не ставят."),
    c("o6-advice", 6, "It's only a suggestion, but I think you ___ apply for the fellowship.", "Это просто совет, но, по-моему, тебе стоит подать заявку на стажировку.",
      ["should", "had better", "must"], "should", "Мягкий совет — should. Had better звучит как предупреждение, must — как приказ."),

    # 7 · be forced to
    c("o7-cancel", 7, "Because of the flu outbreak, the hospital ___ cancel all planned operations.", "Из-за вспышки гриппа больница была вынуждена отменить все плановые операции.",
      ["was forced to", "forced to", "was forced"], "was forced to", "Был вынужден — was forced to + глагол."),
    c("o7-intubate", 7, "His saturation kept falling, so we had no choice but ___ him.", "Сатурация продолжала падать, и нам ничего не оставалось, кроме как его интубировать.",
      ["to intubate", "intubate", "intubating"], "to intubate", "have no choice but to + глагол."),
    c("o7-shifts", 7, "Many nurses ___ work double shifts this year.", "В этом году многие медсёстры были вынуждены работать в две смены.",
      ["have been forced to", "have forced to", "are forcing to"], "have been forced to", "Их вынудили — пассив: have been forced to. Have forced — они сами кого-то заставили."),
    c("o7-retire", 7, "After the injury, she was forced ___ early.", "После травмы ей пришлось рано уйти на пенсию.",
      ["to retire", "retiring", "retire"], "to retire", "be forced to + глагол."),
    c("o7-road", 7, "The road was closed, so the ambulance ___ take a longer route.", "Дорогу перекрыли, и скорой пришлось ехать в объезд.",
      ["had to", "must", "was forced"], "had to", "Обычное «пришлось» — had to. Was forced без to нельзя, у must нет прошедшего."),
    c("o7-paper", 7, "The authors felt ___ to withdraw the paper after the errors were found.", "Когда нашлись ошибки, авторы сочли себя обязанными отозвать статью.",
      ["compelled", "forcing", "made"], "compelled", "feel compelled to — «считать себя обязанным, не мочь иначе»: формально, часто о моральном долге."),

    # 8 · make, force, get
    c("o8-wait", 8, "They made him ___ four hours in A&E.", "Его заставили прождать четыре часа в приёмном.",
      ["wait", "to wait", "waiting"], "wait", "make + кого-то + глагол без to."),
    c("o8-passive", 8, "He was made ___ four hours in A&E.", "Его заставили ждать четыре часа в приёмном.",
      ["to wait", "wait", "waiting"], "to wait", "В пассиве to возвращается: be made to do."),
    c("o8-stop", 8, "We finally got him ___ smoking.", "В итоге мы уговорили его бросить курить.",
      ["to stop", "stop", "stopping"], "to stop", "get + кого-то + to do — уговорить, добиться. В отличие от make, с to."),
    c("o8-trial", 8, "Nobody can force you ___ part in the trial.", "Никто не может заставить вас участвовать в исследовании.",
      ["to take", "take", "taking"], "to take", "force + кого-то + to do — с to."),
    c("o8-protocol", 8, "The new protocol ___ us double-check every high-risk drug.", "Новый протокол заставляет нас перепроверять каждый препарат высокого риска.",
      ["makes", "forces", "gets"], "makes", "Без to после us — только make. Force и get требуют to."),
    c("o8-feel", 8, "The exam made me ___ like a student again.", "Из-за экзамена я снова почувствовал себя студентом.",
      ["feel", "to feel", "feeling"], "feel", "make + кого-то + глагол без to — и «заставить», и «вызвать»."),

    # 9 · be required to, be obliged to
    c("o9-training", 9, "All staff ___ complete annual fire-safety training.", "Все сотрудники обязаны ежегодно проходить обучение пожарной безопасности.",
      ["are required to", "require to", "are required"], "are required to", "Требуется по правилам — be required to + глагол."),
    c("o9-report", 9, "By law, doctors are obliged ___ certain infectious diseases.", "По закону врачи обязаны сообщать о некоторых инфекционных заболеваниях.",
      ["to report", "reporting", "report"], "to report", "be obliged to + глагол."),
    c("o9-consent", 9, "Written consent is ___ before any research procedure.", "Письменное согласие обязательно перед любой процедурой исследования.",
      ["mandatory", "obliged", "required to"], "mandatory", "Обязательный — mandatory или compulsory; можно и is required, но без to. Obliged говорят о людях: we are obliged to…"),
    c("o9-reason", 9, "Participants ___ give a reason for leaving the study.", "Участники не обязаны объяснять, почему выходят из исследования.",
      ["are not required to", "must not", "are required not to"], "are not required to", "Не обязаны — not required to, как don't have to. Must not и required not to — запрет."),
    c("o9-requires", 9, "The protocol ___ two independent readings of every scan.", "Протокол требует двух независимых прочтений каждого снимка.",
      ["requires", "is required", "obliges"], "requires", "Активный залог: the protocol requires something. Is required — когда подлежащее тот, от кого требуют."),
    c("o9-duty", 9, "Hospitals have a legal ___ to protect patient data.", "У больниц есть юридическая обязанность защищать данные пациентов.",
      ["obligation", "obliged", "must"], "obligation", "Существительное — obligation to do: have an obligation to, have a duty to."),

    # 10 · didn't need to или needn't have
    c("o10-queue", 10, "I ___ queue — I had an appointment, so I went straight in.", "В очереди стоять не пришлось — у меня была запись, и я сразу прошёл.",
      ["didn't need to", "needn't have", "mustn't"], "didn't need to", "Не нужно было — и не делал: didn't need to."),
    c("o10-came", 10, "You ___ come in — we could have discussed it by phone.", "Зря вы приезжали — можно было всё обсудить по телефону.",
      ["needn't have", "didn't need to", "mustn't have"], "needn't have", "Сделал, но зря — needn't have + третья форма.",
      also={"didn't need to": "в речи так тоже скажут: didn't need to не уточняет, сделал ли; needn't have прямо говорит — сделал, но зря"}),
    c("o10-ct", 10, "We needn't have ___ a CT — the diagnosis was obvious clinically.", "Зря назначили КТ — диагноз был очевиден клинически.",
      ["ordered", "order", "to order"], "ordered", "needn't have + третья форма: ordered."),
    c("o10-lift", 10, "My colleague gave me a lift, so I ___ take a taxi.", "Коллега меня подвёз, так что такси брать не пришлось.",
      ["didn't have to", "needn't have", "hadn't to"], "didn't have to", "Не пришлось и не делал — didn't have to."),
    c("o10-exam", 10, "I was so nervous about the exam, but I ___ worried — it was easy.", "Я так волновался перед экзаменом, а зря — он был лёгким.",
      ["needn't have", "didn't need to", "mustn't have"], "needn't have", "Волновался, но зря — needn't have worried."),
    c("o10-gift", 10, "Thank you so much — but you ___ brought anything!", "Огромное спасибо — но не стоило ничего приносить!",
      ["needn't have", "shouldn't have", "didn't need"], "needn't have", "Вежливое «ну зачем же» — You needn't have!",
      also={"shouldn't have": "тоже так говорят: You shouldn't have! — «ну зачем же, не стоило»"}),

    # 11 · запрет: от мягкого к строгому
    c("o11-park", 11, "You ___ park here — this space is for ambulances.", "Здесь парковаться нельзя — это место для скорых.",
      ["can't", "don't have to", "needn't"], "can't", "Нельзя по правилам в разговоре — чаще всего can't. Don't have to и needn't — «не обязательно»."),
    c("o11-food", 11, "Visitors ___ bring food into the ward.", "Посетителям нельзя приносить еду в отделение.",
      ["aren't allowed to", "don't allow to", "aren't allowed"], "aren't allowed to", "Запрещено правилами — be not allowed to + глагол."),
    c("o11-sharing", 11, "Staff are prohibited ___ patient data on social media.", "Сотрудникам запрещено публиковать данные пациентов в соцсетях.",
      ["from sharing", "to share", "sharing"], "from sharing", "be prohibited from + -ing — официальный язык."),
    c("o11-eeg", 11, "You ___ drive until we have the EEG results — that's final.", "Водить машину нельзя, пока нет результатов ЭЭГ, — это не обсуждается.",
      ["mustn't", "aren't supposed to", "don't need to"], "mustn't", "Категоричный запрет от говорящего — mustn't. Not supposed to мягче: «не положено»."),
    c("o11-talk", 11, "We're not supposed ___ about it, but the new scanner arrives next week.", "Вообще-то нам не положено об этом говорить, но новый томограф привезут на следующей неделе.",
      ["to talk", "talking", "talk"], "to talk", "not supposed to + глагол."),
    c("o11-smoking", 11, "Smoking is not ___ anywhere on hospital grounds.", "Курение запрещено на всей территории больницы.",
      ["permitted", "allowed to", "prohibited"], "permitted", "Объявления: Smoking is not permitted или not allowed — без to, глагола дальше нет. Not prohibited — «не запрещено», смысл обратный."),

    # 12 · «должен был»: четыре перевода
    c("o12-coat", 12, "His coat is gone — he ___ left early.", "Пальто нет — наверное, он рано ушёл.",
      ["must have", "had to", "should have"], "must have", "Догадка о прошлом — must have + третья форма."),
    c("o12-daughter", 12, "He ___ leave early — his daughter was taken ill.", "Ему пришлось уйти пораньше — заболела дочь.",
      ["had to", "must have", "was supposed to"], "had to", "Пришлось — had to."),
    c("o12-handover", 12, "He ___ stayed until the handover — now nobody knows what happened at night.", "Ему надо было остаться до передачи смены — теперь никто не знает, что было ночью.",
      ["should have", "must have", "had to"], "should have", "Надо было, а он не сделал, — should have + третья форма."),
    c("o12-case", 12, "He ___ present the case at the meeting, but he didn't turn up.", "Он должен был докладывать случай на совещании, но не пришёл.",
      ["was supposed to", "must have", "should"], "was supposed to", "Должен был по плану, но не сделал — was supposed to."),
    c("o12-inr", 12, "The patient ___ taken too much warfarin — his INR is 9.", "Пациент, должно быть, принял слишком много варфарина — МНО 9.",
      ["must have", "had to", "should have"], "must have", "Наверняка принял — догадка: must have taken."),
    c("o12-night", 12, "They ___ operate at night — there was no time to wait until morning.", "Им пришлось оперировать ночью — ждать до утра было нельзя.",
      ["had to", "must have", "were supposed to"], "had to", "Пришлось из-за обстоятельств — had to."),
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
