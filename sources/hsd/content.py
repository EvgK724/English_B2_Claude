# Содержание приложения «Мне сделали»: have / get + что + V3, все времена, «у меня украли»,
# сам или не сам, have / get / make / let + кого + глагол, «сделать МРТ».
# Пометка […] — слово в фокусе (оранжевый).

MIXED_TOPIC = 8

GROUPS = {
    "form": "Мне сделали",
    "sense": "get, неприятность, сам или нет",
    "who": "Кому поручить, кого заставить",
    "clinic": "У врача",
    "mix": "Итог",
}

# Формулы: конструкция | значение | пример ([…] — оранжевым) | перевод примера
WORDS = [
    ["have it done", "мне сделали", "I had my eyes [tested].", "мне проверили зрение"],
    ["get it done", "то же, разговорно", "I got my visa [renewed].", "мне продлили визу"],
    ["had it stolen", "у меня украли", "She had her phone [stolen].", "у неё украли телефон"],
    ["have sb do", "поручить", "I'll have someone [check] it.", "попрошу кого-нибудь проверить"],
    ["get sb to do", "уговорить", "Get her [to take] her tablets.", "уговорите её принимать таблетки"],
    ["make sb do", "заставить", "Don't make him [wait].", "не заставляйте его ждать"],
    ["let sb do", "разрешить", "Let him [go] home.", "отпустите его домой"],
]

# Одна фраза — разный смысл: строки [английский, пояснение]
CONTRAST = [
    [["I [dyed] my hair myself.", "покрасилась сама"],
     ["I had my hair [dyed].", "меня покрасили"]],
    [["I had [repaired] my car.", "had + V3 + что: сам починил раньше"],
     ["I had my car [repaired].", "had + что + V3: мне починили"]],
    [["I had my phone [repaired].", "мне починили — по моей просьбе"],
     ["I had my phone [stolen].", "у меня украли — неприятность"]],
    [["I'll have the nurse [call] you.", "поручу — без to"],
     ["I'll get the nurse [to call] you.", "попрошу, договорюсь — с to"]],
    [["They made him [stay] in bed.", "заставили — без to"],
     ["He was made [to stay] in bed.", "в пассиве — с to"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["I had repaired my car.", "I had my car repaired.", "мне починили — что перед V3"],
    ["I'll make a blood test.", "I'll have a blood test.", "сдать анализ — have a blood test"],
    ["have my eyes check", "have my eyes checked", "нужна V3"],
    ["I'll have the nurse to call you.", "I'll have the nurse call you.", "have кого — без to"],
    ["I got him stop smoking.", "I got him to stop smoking.", "get кого — с to"],
    ["They made him to wait.", "They made him wait.", "make — без to"],
    ["Let him to go.", "Let him go.", "let — без to"],
    ["I did my hair cut.", "I had my hair cut.", "мне сделали — have, не do"],
    ["They made me an X-ray.", "I had an X-ray.", "мне сделали снимок — I had an X-ray"],
    ["I repaired my shoes at the shoemaker's.", "I had my shoes repaired.", "чинил мастер — have them repaired"],
]

TOPICS = [
    {"n": 1, "group": "form", "title": "have + что + V3", "sub": "мне сделали",
     "rule": "Когда делаешь не сам, а тебе делают по твоей просьбе — врач, мастер, сервис: have + что + V3. I had my eyes tested — мне проверили зрение. Порядок: сначала что, потом V3. Поменяешь местами — смысл другой: I had tested my eyes — «я сам проверил» (Past Perfect). Кто делал, обычно не говорят; если нужно — by: I had my car serviced by a local mechanic.",
     "ex": [
         {"en": "I had my eyes [tested] last week.", "ru": "На прошлой неделе мне проверили зрение."},
         {"en": "We had the locks [changed].", "ru": "Нам поменяли замки."},
         {"en": "She had her ears [pierced].", "ru": "Ей прокололи уши."},
     ]},
    {"n": 2, "group": "form", "title": "Во всех временах", "sub": "is having, will have, need to have",
     "rule": "Have здесь — обычный глагол и меняется по временам: we're having the flat renovated (сейчас), I'll have it done tomorrow, I've had my passport renewed, you need to have your stitches taken out. Вопросы и отрицания — с do и did: Did you have your eyes tested? Where do you have your car serviced?",
     "ex": [
         {"en": "We're having a new CT scanner [installed].", "ru": "Нам сейчас устанавливают новый томограф."},
         {"en": "I've just had my passport [renewed].", "ru": "Мне только что продлили паспорт."},
         {"en": "You need to have your stitches [taken] out.", "ru": "Вам нужно снять швы."},
     ]},
    {"n": 3, "group": "sense", "title": "get it done", "sub": "разговорно и «наконец сделать»",
     "rule": "Get + что + V3 — то же, что have, только разговорнее: I got my visa renewed. Get ещё значит «наконец сделать, довести до конца», и тогда делаешь сам: I finally got the report finished — наконец дописал отчёт. Get it done — «сделать, закончить». В письме и в статье — have.",
     "ex": [
         {"en": "I need to get my visa [renewed].", "ru": "Мне нужно продлить визу."},
         {"en": "Let's get this [done] before lunch.", "ru": "Давай закончим с этим до обеда."},
         {"en": "I finally got the report [finished].", "ru": "Я наконец дописал отчёт."},
     ]},
    {"n": 4, "group": "sense", "title": "had my bag stolen", "sub": "у меня украли: неприятность",
     "rule": "Та же форма, но не по просьбе, а неприятность, которая с тобой случилась: I had my bag stolen — у меня украли сумку. He had his licence taken away — у него отобрали права. She had her flight cancelled — ей отменили рейс. Смысл понятен из ситуации.",
     "ex": [
         {"en": "He had his wallet [stolen] on the bus.", "ru": "У него украли кошелёк в автобусе."},
         {"en": "She had her flight [cancelled].", "ru": "Ей отменили рейс."},
         {"en": "She had her bag [searched] at the airport.", "ru": "В аэропорту ей досмотрели сумку."},
     ]},
    {"n": 5, "group": "sense", "title": "Сам или не сам", "sub": "fixed it или had it fixed",
     "rule": "Сделал сам — обычный глагол: I fixed the tap. Сделали тебе — have + что + V3: I had the tap fixed. С точки зрения мастера — снова обычный глагол: The dentist filled two of my teeth, но I had two teeth filled. Порядок меняет смысл: she had cleaned the room — убрала сама (раньше), she had the room cleaned — ей убрали. «Чиню машину в сервисе» — I'm having my car repaired: чинят мастера.",
     "ex": [
         {"en": "I [painted] the fence myself.", "ru": "Я сам покрасил забор."},
         {"en": "I had the fence [painted].", "ru": "Мне покрасили забор."},
         {"en": "I'm having my car [repaired] at the garage.", "ru": "Машину мне чинят в сервисе."},
     ]},
    {"n": 6, "group": "who", "title": "have, get, make, let + кого", "sub": "поручить, уговорить, заставить, разрешить",
     "rule": "Поручить кому-то — have + кого + глагол без to: I'll have the porter take you to X-ray. Уговорить, добиться — get + кого + to: We got him to stop smoking. Заставить — make + кого + глагол без to: The pain made him stop. Разрешить — let + кого + глагол без to: Let him go home. To нужно только после get. Allow тоже с to: allow us to visit. В пассиве make получает to: He was made to wait — сверх уровня.",
     "ex": [
         {"en": "I'll have the porter [take] you to X-ray.", "ru": "Санитар отвезёт вас на рентген — я распоряжусь."},
         {"en": "We finally got him [to stop] smoking.", "ru": "Мы наконец уговорили его бросить курить."},
         {"en": "The pain made him [stop] walking.", "ru": "Из-за боли ему пришлось остановиться."},
     ]},
    {"n": 7, "group": "clinic", "title": "«Сделать МРТ»", "sub": "have an MRI, have a blood test",
     "rule": "Русское «сделать» здесь — не make и не do. Пациенту делают обследование — have: I had an MRI, have a blood test, have an operation, have a flu jab. Врач делает — do, perform, carry out: We did a CT scan, the surgeon performed the operation. Анализ сдать — have a blood test или have your blood taken. С V3: have your blood pressure checked, have your stitches taken out.",
     "ex": [
         {"en": "I [had] an MRI last week.", "ru": "На прошлой неделе мне сделали МРТ."},
         {"en": "We [did] a CT scan on admission.", "ru": "При поступлении мы сделали КТ."},
         {"en": "You need to [have] a blood test.", "ru": "Вам нужно сдать анализ крови."},
     ]},
    {"n": 8, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · have + что + V3
    c("h1-watch", 1, "I need to have my watch ___.", "Мне нужно отдать часы в ремонт.",
      ["repaired", "repair", "repairing"], "repaired", "have + что + V3: have my watch repaired."),
    c("h1-kitchen", 1, "We had ___ last year.", "В прошлом году нам сделали ремонт на кухне.",
      ["the kitchen redecorated", "redecorated the kitchen", "the kitchen redecorate"], "the kitchen redecorated",
      "Сначала что, потом V3. Redecorated the kitchen — «сделали сами»."),
    c("h1-photo", 1, "Where did you have your passport photo ___?", "Где ты фотографировался на паспорт?",
      ["taken", "took", "take"], "taken", "Нужна V3: take — took — taken."),
    c("h1-suit", 1, "He had a suit ___ for his daughter's wedding.", "Ему сшили костюм к свадьбе дочери.",
      ["made", "make", "did"], "made", "Сшить на заказ — have something made."),
    c("h1-by", 1, "I had my car serviced ___ a local mechanic.", "Машину мне обслуживал местный механик.",
      ["by", "from", "with"], "by", "Кто сделал — by."),
    c("h1-printer", 1, "The printer was broken, so we had ___.", "Принтер сломался, и нам его починили.",
      ["it repaired", "repaired it", "it repair"], "it repaired", "have + что + V3: had it repaired."),

    # 2 · Во всех временах
    c("h2-now", 2, "We ___ our flat renovated at the moment.", "У нас сейчас идёт ремонт квартиры.",
      ["are having", "have", "are had"], "are having", "Сейчас — are having + что + V3."),
    c("h2-will", 2, "I'll ___ the results sent to your GP.", "Я распоряжусь, чтобы результаты отправили вашему терапевту.",
      ["have", "has", "having"], "have", "После will — have."),
    c("h2-ever", 2, "Have you ever ___ your cholesterol checked?", "Вам когда-нибудь проверяли холестерин?",
      ["had", "have", "having"], "had", "Present Perfect: have had + что + V3."),
    c("h2-did", 2, "___ you have your eyes tested last year?", "Тебе в прошлом году проверяли зрение?",
      ["did", "had", "were"], "did", "Вопрос в прошлом — Did you have…?"),
    c("h2-need", 2, "You need to have the dressing ___ every day.", "Повязку вам нужно менять каждый день.",
      ["changed", "change", "changing"], "changed", "need to have + что + V3."),
    c("h2-going", 2, "I'm going to have my teeth ___ next month.", "В следующем месяце буду отбеливать зубы.",
      ["whitened", "whiten", "whitening"], "whitened", "going to have + что + V3."),

    # 3 · get it done
    c("h3-prescription", 3, "Where can I get my prescription ___?", "Где мне продлить рецепт?",
      ["renewed", "renew", "to renew"], "renewed", "get + что + V3."),
    c("h3-done", 3, "Don't worry, I'll get it ___ by Friday.", "Не волнуйся, сделаю к пятнице.",
      ["done", "do", "did"], "done", "Сделать, закончить — get it done."),
    c("h3-summaries", 3, "I finally got the discharge summaries ___.", "Я наконец дописал выписки.",
      ["written", "wrote", "write"], "written", "get + что + V3: write — wrote — written."),
    c("h3-scanner", 3, "We must get the scanner ___ as soon as possible.", "Надо как можно скорее починить томограф.",
      ["repaired", "repair", "repairing"], "repaired", "get + что + V3."),
    c("h3-glasses", 3, "I got my glasses ___ at the optician's.", "Мне починили очки в оптике.",
      ["fixed", "fix", "fixing"], "fixed", "get + что + V3."),

    # 4 · had my bag stolen
    c("h4-car", 4, "I had my car ___ last night.", "Вчера ночью у меня угнали машину.",
      ["stolen", "stole", "steal"], "stolen", "Неприятность — had + что + V3: steal — stole — stolen."),
    c("h4-windows", 4, "We had our windows ___ during the storm.", "В бурю нам выбило окна.",
      ["broken", "broke", "break"], "broken", "had + что + V3: break — broke — broken."),
    c("h4-operation", 4, "He had his operation ___ twice because of bed shortages.", "Ему дважды отменяли операцию из-за нехватки коек.",
      ["cancelled", "cancel", "cancelling"], "cancelled", "Неприятность — had + что + V3."),
    c("h4-email", 4, "I had my email account ___.", "Мне взломали почту.",
      ["hacked", "hack", "hacking"], "hacked", "had + что + V3."),
    c("h4-licence", 4, "He had his licence ___ away for drink-driving.", "У него отобрали права за вождение в нетрезвом виде.",
      ["taken", "took", "take"], "taken", "had + что + V3: take — took — taken."),

    # 5 · Сам или не сам
    c("h5-self", 5, "I didn't call anyone — I ___ myself.", "Я никого не вызывал — сам починил кран.",
      ["fixed the tap", "had the tap fixed"], "fixed the tap", "Сам — обычный глагол."),
    c("h5-plumber", 5, "I called a plumber and ___.", "Я вызвал сантехника, и мне починили кран.",
      ["had the tap fixed", "fixed the tap", "had fixed the tap"], "had the tap fixed", "Чинил сантехник — have + что + V3."),
    c("h5-garage", 5, "Every year I ___ at the garage.", "Каждый год я обслуживаю машину в сервисе.",
      ["have my car serviced", "have my car service", "have my car servicing"], "have my car serviced", "В сервисе делают мастера — have + что + V3."),
    c("h5-dentist", 5, "The dentist ___ two of my teeth.", "Стоматолог запломбировал мне два зуба.",
      ["filled", "was filled", "had them filled"], "filled", "Делал сам стоматолог — обычный глагол."),
    c("h5-teeth", 5, "I ___ two teeth filled.", "Мне запломбировали два зуба.",
      ["had", "filled", "did"], "had", "Мне сделали — had + что + V3."),
    c("h5-room", 5, "By the time I arrived, she ___.", "К моему приходу она уже сама убрала комнату.",
      ["had cleaned the room", "had the room cleaned"], "had cleaned the room", "Сама, раньше — Past Perfect: had cleaned the room."),

    # 6 · have, get, make, let + кого
    c("h6-have", 6, "I'll have my assistant ___ you the details.", "Я попрошу ассистента прислать вам подробности.",
      ["send", "to send", "sent"], "send", "Поручить — have + кого + глагол без to."),
    c("h6-get", 6, "Can you get him ___ the consent form?", "Сможете уговорить его подписать согласие?",
      ["to sign", "sign", "signing"], "to sign", "Уговорить — get + кого + to."),
    c("h6-make", 6, "The doctor made him ___ in bed for a week.", "Врач заставил его неделю лежать в постели.",
      ["stay", "to stay", "staying"], "stay", "Заставить — make + кого + глагол без to."),
    c("h6-let", 6, "The doctor let her ___ home for the weekend.", "Врач отпустил её домой на выходные.",
      ["go", "to go", "going"], "go", "Разрешить — let + кого + глагол без to."),
    c("h6-allow", 6, "They didn't ___ us visit him in intensive care.", "Нам не разрешили навещать его в реанимации.",
      ["let", "allow", "make"], "let", "let us visit — без to. Allow требует to: allow us to visit."),
    c("h6-passive", 6, "He was made ___ for three hours.", "Его заставили ждать три часа.",
      ["to wait", "wait", "waiting"], "to wait", "В пассиве после made — to (сверх уровня)."),
    c("h6-brother", 6, "I got my brother ___ my computer.", "Я уговорил брата починить мне компьютер.",
      ["to fix", "fix", "fixed"], "to fix", "Уговорить кого — get + кого + to. Got my computer fixed — «мне починили»."),

    # 7 · «Сделать МРТ»
    c("h7-mri", 7, "My father ___ an MRI yesterday.", "Отцу вчера сделали МРТ.",
      ["had", "made", "did"], "had", "Пациенту делают — have."),
    c("h7-radiographer", 7, "The radiographer ___ the scan in ten minutes.", "Лаборант сделал снимок за десять минут.",
      ["did", "had", "made"], "did", "Делает сам специалист — do."),
    c("h7-blood", 7, "You'll need to ___ a blood test before the operation.", "Перед операцией нужно будет сдать анализ крови.",
      ["have", "make", "give"], "have", "Сдать анализ — have a blood test."),
    c("h7-knee", 7, "She ___ an operation on her knee last year.", "В прошлом году ей сделали операцию на колене.",
      ["had", "did", "made"], "had", "Пациенту делают операцию — have an operation."),
    c("h7-performed", 7, "The operation was ___ by Dr Ivanova.", "Операцию проводила доктор Иванова.",
      ["performed", "made", "had"], "performed", "Проводить операцию — perform."),
    c("h7-xray", 7, "They sent him to ___ an X-ray.", "Его отправили на рентген.",
      ["have", "make", "do"], "have", "Пациенту делают снимок — have an X-ray."),
    c("h7-jab", 7, "Have you ___ your flu jab yet?", "Ты уже сделал прививку от гриппа?",
      ["had", "made", "done"], "had", "Сделать прививку — have a jab."),
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
