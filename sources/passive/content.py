# Содержание приложения «Пассив».
# Пометки: {…} — be в нужном времени (синий), _…_ — третья форма (оранжевый), |…| — by / with и глаголы без пассива (зелёный).

MIXED_TOPIC = 13

# Одна формула на все времена: время | что значит | be | V3 (всегда одна и та же)
FORMS = [
    ["Present Simple", "делают обычно", "is", "done"],
    ["Present Continuous", "делают сейчас", "is being", "done"],
    ["Past Simple", "сделали", "was", "done"],
    ["Past Continuous", "делали в тот момент", "was being", "done"],
    ["Present Perfect", "уже сделали", "has been", "done"],
    ["Past Perfect", "сделали раньше того", "had been", "done"],
    ["Future", "сделают", "will be", "done"],
    ["must, can, should", "нужно, можно сделать", "must be", "done"],
]

# По-русски «сделали» — по-английски пассив: русская фраза | английская
RUS = [
    ["Его госпитализировали.", "He {was} _admitted_."],
    ["Мне сказали подождать.", "I {was} _told_ to wait."],
    ["Ему назначили варфарин.", "He {was} _prescribed_ warfarin."],
    ["Анализы уже взяли.", "The bloods {have been} _taken_."],
    ["Пациента сейчас переводят.", "The patient {is being} _transferred_."],
    ["Вас выпишут завтра.", "You {will be} _discharged_ tomorrow."],
    ["Здесь не курят.", "Smoking {isn't} _allowed_ here."],
    ["Считается, что…", "It {is} _thought_ that…"],
]

# Глаголы без пассива: глагол | перевод
NO_PASSIVE = [
    ["happen", "случаться"], ["occur", "происходить, возникать"], ["die", "умирать"], ["arrive", "прибывать"],
    ["appear", "появляться"], ["disappear", "исчезать"], ["seem", "казаться"], ["remain", "оставаться"],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["It was happened at night.", "It happened at night.", "happen — без пассива"],
    ["He was died.", "He died.", "die — без пассива; he is dead — он мёртв"],
    ["I was said to wait.", "I was told to wait.", "«мне сказали» — I was told"],
    ["The results are send.", "The results are sent.", "после be — третья форма"],
    ["The CT has done.", "The CT has been done.", "без been выходит «КТ сделала»"],
    ["He was gave aspirin.", "He was given aspirin.", "give — gave — given"],
    ["The patient is being examine.", "The patient is being examined.", "being + третья форма"],
    ["I born in 1985.", "I was born in 1985.", "родиться — was born"],
]

TOPICS = [
    {"n": 1, "title": "is / are + V3", "sub": "как обычно делают",
     "rule": "Как обычно делают, а кто делает — неважно: is / are + V3. Is — если предмет один, are — если их много. Отрицание: isn't / aren't + V3.",
     "ex": [
         {"en": "Aspirin {is} _given_ to most stroke patients.", "ru": "Аспирин дают большинству пациентов с инсультом."},
         {"en": "Patients {are} _seen_ within ten minutes.", "ru": "Пациентов осматривают в течение десяти минут."},
         {"en": "Visitors {aren't} _allowed_ after 8 p.m.", "ru": "После 20:00 посетителей не пускают."},
     ]},
    {"n": 2, "title": "was / were + V3", "sub": "что сделали в прошлом",
     "rule": "О прошлом: was / were + V3. Русское «его госпитализировали», «больницу построили» — это пассив в прошлом: сам он этого не делал.",
     "ex": [
         {"en": "He {was} _admitted_ at 3 a.m.", "ru": "Его госпитализировали в 3 часа ночи."},
         {"en": "Two patients {were} _transferred_ to the ICU.", "ru": "Двух пациентов перевели в реанимацию."},
         {"en": "The hospital {was} _built_ in 1975.", "ru": "Больницу построили в 1975 году."},
     ]},
    {"n": 3, "title": "has been + V3", "sub": "что уже сделано",
     "rule": "Уже сделано к этому моменту: has / have been + V3. Часто с already, just, yet, so far, since. Без been получится активный залог: has taken — «он взял».",
     "ex": [
         {"en": "The bloods {have been} _taken_.", "ru": "Анализы уже взяли."},
         {"en": "The results {haven't been} _sent_ yet.", "ru": "Результаты ещё не отправили."},
         {"en": "{Has} he {been} _seen_ by a neurologist?", "ru": "Его уже осмотрел невролог?"},
     ]},
    {"n": 4, "title": "is being + V3", "sub": "что делают прямо сейчас",
     "rule": "Действие идёт прямо сейчас: is / are being + V3. Шло в какой-то момент в прошлом: was / were being + V3.",
     "ex": [
         {"en": "The patient {is being} _transferred_ now.", "ru": "Пациента сейчас переводят."},
         {"en": "The scanner {is being} _repaired_ this week.", "ru": "Томограф на этой неделе ремонтируют."},
         {"en": "He {was being} _examined_ when the alarm went off.", "ru": "Его осматривали, когда сработала тревога."},
     ]},
    {"n": 5, "title": "will / must + be + V3", "sub": "что сделают, что нужно сделать",
     "rule": "После will и модальных глаголов — be + V3: will be done, must be done, can't be given, should be checked. Be здесь никогда не меняется. То же после going to: is going to be done.",
     "ex": [
         {"en": "Alteplase {must be} _given_ within 4.5 hours.", "ru": "Алтеплазу нужно ввести в течение 4,5 часа."},
         {"en": "You {will be} _discharged_ tomorrow.", "ru": "Вас выпишут завтра."},
         {"en": "This drug {can't be} _given_ with warfarin.", "ru": "Этот препарат нельзя давать с варфарином."},
     ]},
    {"n": 6, "title": "Активный или пассивный", "sub": "кто делает действие",
     "rule": "Спроси: подлежащее само делает действие? Да — активный залог: The nurse took blood. Нет, действие делают с ним — пассив: Blood was taken. Recover («поправиться») пациент делает сам — пассива нет.",
     "ex": [
         {"en": "The surgeon operated on him.", "ru": "Хирург его прооперировал. — делает сам"},
         {"en": "He {was} _operated_ on yesterday.", "ru": "Его прооперировали вчера. — делают с ним"},
         {"en": "He |recovered| quickly.", "ru": "Он быстро поправился. — сам, пассива нет"},
     ]},
    {"n": 7, "title": "by или with", "sub": "кто сделал и чем",
     "rule": "By — кто сделал, если это важно: by the surgeon, by a dog. With — чем: with a needle, with sutures. Если неважно, кто сделал, by не пишем вообще.",
     "ex": [
         {"en": "He {was} _operated_ on |by| Dr Ivanov.", "ru": "Его оперировал доктор Иванов. — кто: by"},
         {"en": "The wound {was} _closed_ |with| sutures.", "ru": "Рану закрыли швами. — чем: with"},
         {"en": "The bloods {were} _taken_ this morning.", "ru": "Анализы взяли утром. — кто, неважно: без by"},
     ]},
    {"n": 8, "title": "I was told, he was given", "sub": "мне сказали, ему дали",
     "rule": "Русское «мне сказали», «ему дали», «ей назначили» по-английски начинается с человека: I was told, he was given, she was prescribed. «Мне сказали» — только I was told: с say так нельзя.",
     "ex": [
         {"en": "I {was} _told_ to wait.", "ru": "Мне сказали подождать."},
         {"en": "He {was} _given_ aspirin.", "ru": "Ему дали аспирин."},
         {"en": "She {was} _offered_ a place in rehab.", "ru": "Ей предложили место в реабилитации."},
     ]},
    {"n": 9, "title": "Без пассива", "sub": "happen, die, arrive · was born",
     "rule": "С некоторыми глаголами ничего «не делают» — у них нет пассива: happen, occur, die, arrive, appear, disappear, seem. It happened, а не was happened. А «родиться» — наоборот, только пассив: I was born.",
     "ex": [
         {"en": "What |happened|?", "ru": "Что случилось?"},
         {"en": "He |died| in 2019.", "ru": "Он умер в 2019 году."},
         {"en": "She {was} _born_ in 1990.", "ru": "Она родилась в 1990 году. — только пассив"},
     ]},
    {"n": 10, "title": "have it done", "sub": "мне сделали (у врача, у мастера)",
     "rule": "Когда делаешь не сам, а тебе делают (врач, мастер): have + что + V3. I had my tooth removed — мне удалили зуб. Порядок важен: сначала что, потом V3. В разговоре вместо have часто get.",
     "ex": [
         {"en": "I {had} my tooth _removed_.", "ru": "Мне удалили зуб (у стоматолога)."},
         {"en": "You should {have} your blood pressure _checked_.", "ru": "Вам стоит проверить давление у врача."},
         {"en": "I need to {get} my hair _cut_.", "ru": "Мне нужно подстричься. — get разговорнее"},
     ]},
    {"n": 11, "title": "It is said that…", "sub": "считается, что… · сверх уровня", "late": 0.4,
     "rule": "В статьях и новостях, когда это общее мнение: It is thought / believed / said that… или He is said to… · Smoking is known to… Удобно для научных текстов и докладов.",
     "ex": [
         {"en": "It {is} _thought_ that the clot came from the heart.", "ru": "Считается, что тромб пришёл из сердца."},
         {"en": "Smoking {is} _known_ to increase the risk of stroke.", "ru": "Известно, что курение повышает риск инсульта."},
         {"en": "He {is} _said_ to be the best surgeon in town.", "ru": "Говорят, он лучший хирург в городе."},
     ]},
    {"n": 12, "title": "to be done · being done", "sub": "нужно сделать · не люблю, когда…", "late": 0.25,
     "rule": "После need to, have to, would like to — to be + V3: needs to be changed. После like, hate, avoid и предлогов — being + V3: I hate being interrupted.",
     "ex": [
         {"en": "The dressing {needs to be} _changed_ daily.", "ru": "Повязку нужно менять ежедневно."},
         {"en": "He {has to be} _monitored_ for 24 hours.", "ru": "Его нужно наблюдать 24 часа."},
         {"en": "I hate {being} _interrupted_.", "ru": "Терпеть не могу, когда меня перебивают."},
     ]},
    {"n": 13, "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]
LATE = {7: 0.05, 10: 0.15}
for t in TOPICS:
    if t["n"] in LATE: t["late"] = LATE[t["n"]]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · is / are + V3
    c("p1-given", 1, "Aspirin ___ to most patients with ischaemic stroke.", "Аспирин назначают большинству пациентов с ишемическим инсультом.",
      ["is given", "gives", "is give"], "is given", "Кто даёт — неважно: is + V3 (give — gave — given)."),
    c("p1-seen", 1, "New patients ___ by a neurologist within ten minutes.", "Новых пациентов осматривает невролог в течение десяти минут.",
      ["are seen", "is seen", "see"], "are seen", "Patients — много, значит are + V3."),
    c("p1-made", 1, "The diagnosis ___ on CT or MRI.", "Диагноз ставят по КТ или МРТ.",
      ["is made", "makes", "is make"], "is made", "Диагноз ставят, кто — неважно: is + V3 (make — made — made)."),
    c("p1-spoken", 1, "English ___ at most international conferences.", "На большинстве международных конференций говорят по-английски.",
      ["is spoken", "speaks", "is speaking"], "is spoken", "Язык сам не говорит — на нём говорят: is spoken."),
    c("p1-allowed", 1, "Visitors ___ in the ICU after 8 p.m.", "После 20:00 посетителей в реанимацию не пускают.",
      ["aren't allowed", "don't allow", "isn't allowed"], "aren't allowed", "Отрицание: aren't + V3. Visitors — много, поэтому are."),
    c("p1-called", 1, "This sign ___ the 'dense artery sign'.", "Этот признак называется «симптом гиперденсной артерии».",
      ["is called", "calls", "called"], "is called", "«Называется» — is called. Частая ошибка: it calls."),

    # 2 · was / were + V3
    c("p2-admitted", 2, "He ___ to our unit at 3 a.m.", "Его госпитализировали в наше отделение в 3 часа ночи.",
      ["was admitted", "admitted", "is admitted"], "was admitted", "Госпитализировали его, сам он этого не делал: was + V3."),
    c("p2-built", 2, "The hospital ___ in 1975.", "Больницу построили в 1975 году.",
      ["was built", "built", "was build"], "was built", "was + V3: build — built — built."),
    c("p2-transferred", 2, "Two patients ___ to the ICU last night.", "Прошлой ночью двух пациентов перевели в реанимацию.",
      ["were transferred", "was transferred", "transferred"], "were transferred", "Два пациента — много: were + V3."),
    c("p2-stolen", 2, "My bike ___ from outside the hospital.", "Мой велосипед украли прямо у больницы.",
      ["was stolen", "stole", "was stealed"], "was stolen", "Украли, а кто — неизвестно: was + V3 (steal — stole — stolen)."),
    c("p2-performed", 2, "The operation ___ by Dr Ivanov.", "Операцию провёл доктор Иванов.",
      ["was performed", "performed", "was perform"], "was performed", "was + третья форма: performed, с -ed."),
    c("p2-discharged", 2, "He ___ home on Friday.", "Его выписали домой в пятницу.",
      ["was discharged", "discharged", "has discharged"], "was discharged", "«Выписали» — пассив в прошлом: was discharged."),

    # 3 · has / have been + V3
    c("p3-taken", 3, "The bloods have already ___.", "Анализы крови уже взяли.",
      ["been taken", "taken", "be taken"], "been taken", "have + been + V3. Без been выйдет «анализы взяли что-то»."),
    c("p3-sent", 3, "The results ___ to the GP yet.", "Результаты ещё не отправили участковому врачу.",
      ["haven't been sent", "haven't sent", "aren't sent"], "haven't been sent", "yet — Present Perfect: haven't been + V3."),
    c("p3-cancelled", 3, "I'm afraid your appointment ___.", "К сожалению, ваш приём отменили.",
      ["has been cancelled", "has cancelled", "is cancelling"], "has been cancelled", "Результат сейчас: has been + V3. Has cancelled — «приём сам что-то отменил»."),
    c("p3-seen", 3, "Has the patient ___ by the neurologist?", "Невролог уже осмотрел пациента?",
      ["been seen", "seen", "be seen"], "been seen", "Вопрос: Has + подлежащее + been + V3."),
    c("p3-updated", 3, "The protocol ___ twice since 2019.", "С 2019 года протокол обновляли дважды.",
      ["has been updated", "was updated", "has updated"], "has been updated", "since — Present Perfect; протокол обновляли — has been + V3."),
    c("p3-found", 3, "No cause ___ so far.", "Причину пока не нашли.",
      ["has been found", "has found", "was finding"], "has been found", "so far — к этому моменту: has been + V3 (find — found — found)."),

    # 4 · is / was being + V3
    c("p4-transferred", 4, "The patient ___ to the ICU right now.", "Пациента прямо сейчас переводят в реанимацию.",
      ["is being transferred", "is transferred", "is transferring"], "is being transferred", "right now — процесс: is being + V3. Is transferring — «он сам кого-то переводит»."),
    c("p4-cleaned", 4, "Sorry, the room ___ at the moment.", "Извините, в палате сейчас убирают.",
      ["is being cleaned", "is cleaning", "has cleaned"], "is being cleaned", "at the moment + пассив: is being + V3."),
    c("p4-examined", 4, "He ___ when the alarm went off.", "Его осматривали, когда сработала тревога.",
      ["was being examined", "was examining", "is being examined"], "was being examined", "Процесс в прошлом, с ним: was being + V3."),
    c("p4-repaired", 4, "The MRI scanner ___ this week, so we use the CT.", "МРТ на этой неделе ремонтируют, поэтому пользуемся КТ.",
      ["is being repaired", "is repairing", "repairs"], "is being repaired", "this week, идёт сейчас: is being + V3."),
    c("p4-introduced", 4, "New guidelines ___ in all stroke units now.", "Новые рекомендации сейчас внедряют во всех инсультных отделениях.",
      ["are being introduced", "are introducing", "introduce"], "are being introduced", "now, процесс: are being + V3."),

    # 5 · will / must + be + V3
    c("p5-given", 5, "Alteplase must ___ within 4.5 hours of onset.", "Алтеплазу нужно ввести в течение 4,5 часа от начала симптомов.",
      ["be given", "give", "been given"], "be given", "После must — be + V3."),
    c("p5-discharged", 5, "You ___ tomorrow morning.", "Вас выпишут завтра утром.",
      ["will be discharged", "will discharge", "are discharging"], "will be discharged", "Будущее + пассив: will be + V3. Will discharge — «вы выпишете»."),
    c("p5-cant", 5, "This drug ___ with warfarin.", "Этот препарат нельзя давать вместе с варфарином.",
      ["can't be given", "can't give", "can't be give"], "can't be given", "can't + be + V3."),
    c("p5-screened", 5, "All patients ___ for dysphagia before eating.", "Всех пациентов нужно проверить на дисфагию до еды.",
      ["should be screened", "should screen", "should been screened"], "should be screened", "should + be + V3. Should been — такой формы нет."),
    c("p5-renovated", 5, "The old wing ___ next year.", "Старый корпус отремонтируют в следующем году.",
      ["is going to be renovated", "is going to renovate", "is renovated"], "is going to be renovated", "going to + be + V3."),
    c("p5-affected", 5, "The results may ___ by infection.", "На результаты может повлиять инфекция.",
      ["be affected", "affect", "been affected"], "be affected", "may + be + V3."),

    # 6 · активный или пассивный
    c("a6-examined", 6, "The doctor ___ the patient carefully.", "Врач внимательно осмотрел пациента.",
      ["examined", "was examined", "is examined"], "examined", "Врач осматривает сам — активный залог: examined."),
    c("a6-was-examined", 6, "The patient ___ by two doctors.", "Пациента осмотрели два врача.",
      ["was examined", "examined", "has examined"], "was examined", "Пациента осматривают — пассив: was + V3; by — кто."),
    c("a6-recovered", 6, "He ___ well after the operation.", "Он хорошо восстановился после операции.",
      ["recovered", "was recovered", "is recovered"], "recovered", "recover — «поправляться»: делает сам, пассива нет."),
    c("a6-treated", 6, "She ___ with antibiotics for a week.", "Её неделю лечили антибиотиками.",
      ["was treated", "treated", "has treated"], "was treated", "Её лечили — пассив: was treated."),
    c("a6-called", 6, "Someone ___ an ambulance.", "Кто-то вызвал скорую.",
      ["called", "was called", "is called"], "called", "Someone делает действие сам — активный залог."),
    c("a6-was-called", 6, "An ambulance ___ immediately.", "Скорую вызвали сразу.",
      ["was called", "called", "has called"], "was called", "Скорую вызвали — пассив: was called."),

    # 7 · by или with
    c("b7-sutures", 7, "The wound was closed ___ sutures.", "Рану закрыли швами.",
      ["with", "by", "from"], "with", "Чем — with."),
    c("b7-surgeon", 7, "He was operated on ___ a senior surgeon.", "Его оперировал опытный хирург.",
      ["by", "with", "from"], "by", "Кто — by."),
    c("b7-needle", 7, "The sample was taken ___ a thin needle.", "Образец взяли тонкой иглой.",
      ["with", "by", "of"], "with", "Чем — with."),
    c("b7-dog", 7, "He was bitten ___ a dog.", "Его укусила собака.",
      ["by", "with", "from"], "by", "Кто — by: собака кусает сама."),
    c("b7-book", 7, "This textbook was written ___ a famous neurologist.", "Этот учебник написал известный невролог.",
      ["by", "with", "of"], "by", "Автор, кто — by."),

    # 8 · I was told, he was given
    c("g8-told", 8, "I ___ to wait in the corridor.", "Мне сказали подождать в коридоре.",
      ["was told", "was said", "told"], "was told", "«Мне сказали» — I was told. I was said — ошибка."),
    c("g8-given", 8, "He ___ aspirin in the ambulance.", "Ему дали аспирин в скорой.",
      ["was given", "was gave", "gave"], "was given", "«Ему дали» — he was given (give — gave — given)."),
    c("g8-prescribed", 8, "She ___ warfarin after the valve replacement.", "Ей назначили варфарин после замены клапана.",
      ["was prescribed", "prescribed", "was prescribe"], "was prescribed", "«Ей назначили» — she was prescribed."),
    c("g8-offered", 8, "The patient ___ a place in a rehab centre.", "Пациенту предложили место в реабилитационном центре.",
      ["was offered", "offered", "was offering"], "was offered", "«Ему предложили» — he was offered."),
    c("g8-asked", 8, "We ___ to fill in the form again.", "Нас попросили заполнить форму ещё раз.",
      ["were asked", "asked", "were ask"], "were asked", "«Нас попросили» — we were asked."),
    c("g8-shown", 8, "The students ___ how to do a lumbar puncture.", "Студентам показали, как делать люмбальную пункцию.",
      ["were shown", "showed", "were show"], "were shown", "«Им показали» — they were shown (show — showed — shown)."),

    # 9 · без пассива
    c("n9-happened", 9, "The accident ___ at night.", "Авария произошла ночью.",
      ["happened", "was happened", "is happened"], "happened", "happen не бывает в пассиве: it happened."),
    c("n9-died", 9, "The patient ___ early in the morning.", "Пациент умер рано утром.",
      ["died", "was died", "is died"], "died", "die — без пассива: he died. He is dead — «он мёртв»."),
    c("n9-occur", 9, "Seizures ___ in some patients after a stroke.", "У некоторых пациентов после инсульта возникают судороги.",
      ["occur", "are occurred", "occurs"], "occur", "occur — без пассива. Seizures — много, поэтому occur без -s."),
    c("n9-born", 9, "She ___ in 1990.", "Она родилась в 1990 году.",
      ["was born", "born", "is born"], "was born", "«Родиться» — только пассив: was born."),
    c("n9-arrived", 9, "The ambulance ___ in eight minutes.", "Скорая приехала за восемь минут.",
      ["arrived", "was arrived", "is arrived"], "arrived", "arrive — без пассива: it arrived."),
    c("n9-appeared", 9, "The rash ___ two days later.", "Сыпь появилась через два дня.",
      ["appeared", "was appeared", "is appeared"], "appeared", "appear — без пассива: it appeared."),

    # 10 · have it done
    c("h10-tooth", 10, "I had my tooth ___ yesterday.", "Вчера мне удалили зуб.",
      ["removed", "remove", "removing"], "removed", "have + что + V3: had my tooth removed."),
    c("h10-bp", 10, "You should have your blood pressure ___ regularly.", "Вам стоит регулярно проверять давление у врача.",
      ["checked", "check", "to check"], "checked", "have + что + V3: have it checked."),
    c("h10-hair", 10, "I need to get my hair ___.", "Мне нужно подстричься.",
      ["cut", "cutted", "to cut"], "cut", "get + что + V3; cut не меняется: cut — cut — cut."),
    c("h10-ward", 10, "We're having the ward ___ next month.", "В следующем месяце нам покрасят отделение.",
      ["painted", "paint", "painting"], "painted", "having + что + V3: the ward painted."),
    c("h10-self", 10, "Did you fix the car yourself? — No, I ___.", "Ты сам починил машину? — Нет, мне её починили.",
      ["had it fixed", "fixed it", "had fixed it"], "had it fixed", "Не сам — have + it + V3: had it fixed."),

    # 11 · It is said that…
    c("r11-thought", 11, "It ___ that the clot came from the heart.", "Считается, что тромб пришёл из сердца.",
      ["is thought", "thinks", "is thinking"], "is thought", "«Считается, что…» — It is thought that…"),
    c("r11-known", 11, "Smoking ___ to increase the risk of stroke.", "Известно, что курение повышает риск инсульта.",
      ["is known", "knows", "is knowing"], "is known", "«Известно, что X…» — X is known to…"),
    c("r11-said", 11, "He ___ to be the best surgeon in town.", "Говорят, он лучший хирург в городе.",
      ["is said", "says", "is told"], "is said", "«Говорят, что он…» — He is said to be…"),
    c("r11-believed", 11, "It ___ that about a quarter of strokes are cryptogenic.", "Считается, что около четверти инсультов — криптогенные.",
      ["is believed", "believes", "believed"], "is believed", "«Считается» — It is believed that…"),
    c("r11-expected", 11, "The new unit ___ to open in March.", "Ожидается, что новое отделение откроется в марте.",
      ["is expected", "expects", "is expecting"], "is expected", "«Ожидается, что…» — X is expected to…"),

    # 12 · to be done · being done
    c("i12-changed", 12, "The dressing needs to ___ every day.", "Повязку нужно менять каждый день.",
      ["be changed", "change", "been changed"], "be changed", "need to + be + V3."),
    c("i12-monitored", 12, "He has to ___ for 24 hours after thrombolysis.", "После тромболизиса его нужно наблюдать 24 часа.",
      ["be monitored", "monitor", "being monitored"], "be monitored", "have to + be + V3."),
    c("i12-told", 12, "He doesn't like ___ what to do.", "Он не любит, когда ему указывают, что делать.",
      ["being told", "telling", "be told"], "being told", "like + being + V3: не любит, когда ему говорят."),
    c("i12-interrupted", 12, "I hate ___ during a procedure.", "Терпеть не могу, когда меня перебивают во время процедуры.",
      ["being interrupted", "interrupting", "be interrupted"], "being interrupted", "hate + being + V3."),
    c("i12-seen", 12, "I'd like ___ by a specialist.", "Я бы хотел, чтобы меня осмотрел специалист.",
      ["to be seen", "to see", "being seen"], "to be seen", "would like + to be + V3."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", Counter(k["t"] for k in CARDS))
