# Содержание приложения «my / mine»: личные местоимения, притяжательные прилагательные и местоимения.
# Пометка [слово|x]: s — кто? (подчёркнуто), o — кого? (синий), a — чей? + сущ. (оранжевый),
# p — чей? без сущ. (зелёный), r — возвратное (подчёркнуто).

MIXED_TOPIC = 8

GROUPS = {
    "who": "Личные местоимения",
    "whose": "Притяжательные",
    "more": "Ловушки и бонус",
    "mix": "Итог",
}

# Все формы: кто? | кого? | чей? + сущ. | чей? без сущ. | пример | перевод | озвучка
FORMS = [
    ["I", "me", "my", "mine", "It's [my|a] bag. It's [mine|p].", "Это моя сумка. Она моя.", "I, me, my, mine. It's my bag. It's mine."],
    ["you", "you", "your", "yours", "It's [your|a] bag. It's [yours|p].", "Это твоя сумка. Она твоя.", "You, you, your, yours. It's your bag. It's yours."],
    ["he", "him", "his", "his", "It's [his|a] bag. It's [his|p].", "Это его сумка. Она его.", "He, him, his, his. It's his bag. It's his."],
    ["she", "her", "her", "hers", "It's [her|a] bag. It's [hers|p].", "Это её сумка. Она её.", "She, her, her, hers. It's her bag. It's hers."],
    ["it", "it", "its", "—", "The cat hurt [its|a] paw.", "Кошка поранила лапу.", "It, it, its. The cat hurt its paw."],
    ["we", "us", "our", "ours", "It's [our|a] bag. It's [ours|p].", "Это наша сумка. Она наша.", "We, us, our, ours. It's our bag. It's ours."],
    ["they", "them", "their", "theirs", "It's [their|a] bag. It's [theirs|p].", "Это их сумка. Она их.", "They, them, their, theirs. It's their bag. It's theirs."],
]

# Чего нет в русском: по-русски | по-английски | пояснение
RUEN = [
    ["Идёт дождь.", "[It|s]'s raining.", "подлежащее нужно всегда"],
    ["Он взял свою сумку.", "He took [his|a] bag.", "«свой» — по лицу: he → his"],
    ["Она взяла свою сумку.", "She took [her|a] bag.", "she → her"],
    ["Я сломал руку.", "I broke [my|a] arm.", "части тела — с my, his, her"],
    ["Откройте рот.", "Open [your|a] mouth.", "your — хотя по-русски его нет"],
    ["Мне эта песня нравится, а ему — нет.", "I like this song, but he doesn't like [it|o].", "песня — it, а не «её»"],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["Is raining.", "It's raining.", "подлежащее нужно всегда"],
    ["This is the my car.", "This is my car.", "с my артикль не нужен"],
    ["This book is my.", "This book is mine.", "без существительного — mine"],
    ["The bag is her's.", "The bag is hers.", "без апострофа: hers, yours, theirs"],
    ["The hospital has it's own lab.", "The hospital has its own lab.", "its — чей; it's = it is"],
    ["She took his bag. (свою)", "She took her bag.", "«свой» — по лицу: she → her"],
    ["I broke the leg.", "I broke my leg.", "части тела — с my, his, her"],
    ["Me and Anna are colleagues.", "Anna and I are colleagues.", "подлежащее — I, себя называют вторым"],
    ["between you and I", "between you and me", "после предлога — me"],
    ["I feel myself better.", "I feel better.", "«чувствую себя» — без myself"],
]

TOPICS = [
    {"n": 1, "group": "who", "title": "Кто? — I, he, she…", "sub": "подлежащее нужно всегда",
     "rule": "I, you, he, she, it, we, they — кто делает, подлежащее. В английском оно нужно всегда, даже там, где по-русски его нет: It's raining, It's cold, It's five o'clock, It's important to… Про себя с другими — вторым и с I: My colleague and I are neurologists. Предметы во множественном числе — they: Where are the results? — They're on your desk.",
     "ex": [
         {"en": "[It|s]'s raining again.", "ru": "Опять идёт дождь."},
         {"en": "My sister is a nurse. [She|s] works nights.", "ru": "Моя сестра — медсестра. Она работает по ночам."},
         {"en": "My colleague and [I|s] are neurologists.", "ru": "Мы с коллегой — неврологи."},
     ]},
    {"n": 2, "group": "who", "title": "Кого? кому? — me, him, her…", "sub": "после глагола и предлога",
     "rule": "me, you, him, her, it, us, them — после глагола и после предлога: Call me. Talk to them. Between you and me. «Это я» — It's me. Предметы и явления — it, даже если по-русски «его» или «её»: I love this song, but he hates it. О человеке, чей пол неизвестен, говорят them: If anyone calls, tell them I'm busy.",
     "ex": [
         {"en": "Can you call [me|o] tomorrow?", "ru": "Можешь позвонить мне завтра?"},
         {"en": "Please talk to [them|o].", "ru": "Поговори с ними, пожалуйста."},
         {"en": "This is between you and [me|o].", "ru": "Это между нами."},
     ]},
    {"n": 3, "group": "whose", "title": "Чей? — my, your, his…", "sub": "перед существительным",
     "rule": "my, your, his, her, its, our, their — «чей?», всегда перед существительным: my car, her patients, their children. Артикль с ними не нужен: the my car — ошибка. his или her — по владельцу: Dr Petrova and her patients. Предметы и животные — its: The hospital has its own lab. По-русски «мой, наш» часто опускают — в английском они нужны: We sold our car.",
     "ex": [
         {"en": "Is this [your|a] coat?", "ru": "Это твоё пальто?"},
         {"en": "Dr Petrova is on holiday, and [her|a] patients are with me.", "ru": "Доктор Петрова в отпуске, её пациенты у меня."},
         {"en": "We sold [our|a] car last year.", "ru": "В прошлом году мы продали машину."},
     ]},
    {"n": 4, "group": "whose", "title": "Чей? — mine, yours, hers…", "sub": "без существительного",
     "rule": "mine, yours, his, hers, ours, theirs — «чей?», когда существительного после нет: This bag is mine. Is this yours? Апострофа нет никогда: yours, hers, theirs (не your's). «Мой друг, один из» — a friend of mine.",
     "ex": [
         {"en": "This bag is [mine|p].", "ru": "Эта сумка моя."},
         {"en": "Our flat is small, but [theirs|p] is huge.", "ru": "Наша квартира маленькая, а их — огромная."},
         {"en": "She's a friend of [mine|p].", "ru": "Она моя подруга."},
     ]},
    {"n": 5, "group": "whose", "title": "«Свой» и части тела", "sub": "his, her, their вместо «свой»",
     "rule": "Слова «свой» в английском нет: берём притяжательное по лицу — I took my bag, she took her bag, they took their bags. С частями тела и одеждой притяжательное нужно всегда, хотя по-русски его нет: I broke my arm. Open your mouth. Raise your arms. Squeeze my fingers.",
     "ex": [
         {"en": "She forgot [her|a] phone.", "ru": "Она забыла свой телефон."},
         {"en": "Open [your|a] mouth and say 'ah'.", "ru": "Откройте рот и скажите «а»."},
         {"en": "Squeeze [my|a] fingers.", "ru": "Сожмите мои пальцы."},
     ]},
    {"n": 6, "group": "more", "title": "its или it's и другие", "sub": "звучат одинаково",
     "rule": "Звучат одинаково — пишутся по-разному. its — чей? (The cat hurt its paw), it's = it is, it has. your — твой, you're = you are. their — их, there — там, they're = they are. whose — чей, who's = who is.",
     "ex": [
         {"en": "[It|s]'s raining.", "ru": "Идёт дождь. (it is)"},
         {"en": "The cat hurt [its|a] paw.", "ru": "Кошка поранила лапу."},
         {"en": "[Their|a] car is over there.", "ru": "Их машина вон там."},
     ]},
    {"n": 7, "group": "more", "title": "Бонус: myself", "sub": "сам, себя",
     "rule": "myself, yourself, himself, herself, itself, ourselves, yourselves, themselves — «себя, сам»: I cut myself. Help yourself! — угощайтесь. by myself — сам, в одиночку. Там, где по-русски «-ся» или «себя» по привычке, английский обходится без них: I feel better (не I feel myself better), relax, wash, get dressed.",
     "ex": [
         {"en": "I cut [myself|r].", "ru": "Я порезался."},
         {"en": "Help [yourself|r]!", "ru": "Угощайтесь!"},
         {"en": "He lives by [himself|r].", "ru": "Он живёт один."},
     ]},
    {"n": 8, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · кто?
    c("p1-rain", 1, "___ is raining again.", "Опять идёт дождь.", ["It", "He", "This"], "It", "Погода, время — it: It's raining, It's cold."),
    c("p1-time", 1, "What time is ___? — Half past nine.", "Который час? — Половина десятого.", ["it", "this", "time"], "it", "Время — it: What time is it?"),
    c("p1-she", 1, "My sister is a nurse. ___ works nights.", "Моя сестра — медсестра. Она работает по ночам.", ["She", "Her", "It"], "She",
      "Кто работает? — she."),
    c("p1-they", 1, "Where are the results? — ___ are on your desk.", "Где результаты? — У вас на столе.", ["They", "It", "Them"], "They",
      "Results — множественное число: they."),
    c("p1-important", 1, "___ is important to take the tablets every day.", "Важно принимать таблетки каждый день.", ["It", "This", "That"], "It",
      "«Важно…», «трудно…» — It is important to…"),
    c("p1-and", 1, "My colleague and ___ are both neurologists.", "Мы с коллегой оба неврологи.", ["I", "me", "my"], "I",
      "Подлежащее — I. Себя называют вторым: My colleague and I."),

    # 2 · кого? кому?
    c("p2-call", 2, "Can you call ___ tomorrow?", "Можешь позвонить мне завтра?", ["me", "I", "my"], "me", "После глагола — me."),
    c("p2-her", 2, "I saw Anna yesterday and gave ___ the report.", "Вчера я видел Анну и отдал ей отчёт.", ["her", "she", "hers"], "her", "Кому? — her."),
    c("p2-them", 2, "The patients are waiting. Please talk to ___.", "Пациенты ждут. Поговори с ними, пожалуйста.", ["them", "they", "their"], "them",
      "После предлога — them."),
    c("p2-between", 2, "This is between you and ___.", "Это между нами (между тобой и мной).", ["me", "I"], "me",
      "После предлога — me: between you and me. Between you and I — ошибка."),
    c("p2-song", 2, "I love this song, but my friend hates ___.", "Я обожаю эту песню, а друг её терпеть не может.", ["it", "her", "them"], "it",
      "Песня — it, хотя по-русски «её»."),
    c("p2-itsme", 2, "Who's there? — It's ___.", "Кто там? — Это я.", ["me", "I"], "me", "«Это я» — It's me."),

    # 3 · my, your, his…
    c("p3-coat", 3, "Is this ___ coat? — Yes, it's mine.", "Это твоё пальто? — Да, моё.", ["your", "yours", "you"], "your", "Перед существительным — your."),
    c("p3-patients", 3, "Dr Petrova is on holiday, and ___ patients are with me this week.", "Доктор Петрова в отпуске, и её пациенты на этой неделе у меня.",
      ["her", "his", "hers"], "her", "Владелец — она: her patients."),
    c("p3-its", 3, "The hospital has ___ own lab.", "У больницы своя лаборатория.", ["its", "it's", "his"], "its", "Предмет — its. It's = it is."),
    c("p3-keys", 3, "Where are ___ keys? I can't find them.", "Где мои ключи? Не могу их найти.", ["my", "mine", "me"], "my", "Перед существительным — my."),
    c("p3-toys", 3, "The children are playing with ___ toys.", "Дети играют со своими игрушками.", ["their", "them", "theirs"], "their",
      "Перед существительным — their."),
    c("p3-car", 3, "We sold ___ car last year.", "В прошлом году мы продали машину.", ["our", "ours", "us"], "our",
      "По-русски «нашу» опускают, в английском — our car."),

    # 4 · mine, yours, hers…
    c("p4-pen", 4, "Is this pen yours? — No, it isn't ___.", "Это твоя ручка? — Нет, не моя.", ["mine", "my", "me"], "mine", "Без существительного — mine."),
    c("p4-bag", 4, "Whose bag is this? — It's ___.", "Чья это сумка? — Её.", ["hers", "her", "her's"], "hers", "Без существительного — hers, без апострофа."),
    c("p4-flat", 4, "Our flat is small, but ___ is huge.", "Наша квартира маленькая, а их — огромная.", ["theirs", "their", "their's"], "theirs",
      "Без существительного — theirs."),
    c("p4-results", 4, "My results are fine. How about ___?", "Мои результаты в норме. А твои?", ["yours", "your", "your's"], "yours",
      "Без существительного — yours, без апострофа."),
    c("p4-friend", 4, "She's a friend of ___.", "Она моя подруга.", ["mine", "me", "my"], "mine", "«Мой друг, один из» — a friend of mine."),
    c("p4-seat", 4, "This seat is ___ — we booked it.", "Это место наше — мы его забронировали.", ["ours", "our", "us"], "ours", "Без существительного — ours."),

    # 5 · «свой» и части тела
    c("p5-phone", 5, "She forgot ___ phone at home.", "Она забыла свой телефон дома.", ["her", "his", "its"], "her", "«Свой» — по лицу: she → her."),
    c("p5-mouth", 5, "Open ___ mouth and say 'ah'.", "Откройте рот и скажите «а».", ["your", "the", "yours"], "your",
      "Части тела — с притяжательным: open your mouth."),
    c("p5-arms", 5, "Can you raise ___ arms above your head?", "Можете поднять руки над головой?", ["your", "the", "yours"], "your",
      "Части тела — your arms, хотя по-русски просто «руки»."),
    c("p5-leg", 5, "He broke ___ leg skiing.", "Он сломал ногу, катаясь на лыжах.", ["his", "the", "him"], "his", "Сломал ногу — broke his leg."),
    c("p5-fingers", 5, "Squeeze ___ fingers as hard as you can.", "Сожмите мои пальцы как можно сильнее.", ["my", "mine", "me"], "my",
      "Пальцы врача — my fingers."),
    c("p5-tablets", 5, "The patients took ___ tablets after lunch.", "Пациенты приняли свои таблетки после обеда.", ["their", "his", "theirs"], "their",
      "«Свои» — по лицу: the patients → their."),

    # 6 · its или it's и другие
    c("p6-raining", 6, "___ raining again.", "Опять дождь.", ["It's", "Its"], "It's", "It's = it is: it is raining."),
    c("p6-paw", 6, "The cat hurt ___ paw.", "Кошка поранила лапу.", ["its", "it's"], "its", "Чья лапа? — its, без апострофа."),
    c("p6-welcome", 6, "Thank you! — ___ welcome!", "Спасибо! — Пожалуйста!", ["You're", "Your"], "You're", "You're = you are: you are welcome."),
    c("p6-bag", 6, "Is this ___ bag?", "Это твоя сумка?", ["your", "you're"], "your", "Чья? — your."),
    c("p6-waiting", 6, "___ waiting in reception.", "Они ждут в регистратуре.", ["They're", "Their", "There"], "They're", "They're = they are."),
    c("p6-there", 6, "Put the files over ___.", "Положи папки вон туда.", ["there", "their", "they're"], "there", "Там, туда — there."),
    c("p6-whose", 6, "___ coat is this?", "Чьё это пальто?", ["Whose", "Who's"], "Whose", "Чей? — whose. Who's = who is."),
    c("p6-whos", 6, "___ the doctor on duty tonight?", "Кто сегодня дежурный врач?", ["Who's", "Whose"], "Who's", "Who's = who is."),

    # 7 · бонус: myself
    c("p7-cut", 7, "I cut ___ while I was cooking.", "Я порезался, когда готовил.", ["myself", "me", "mine"], "myself", "Сам себя — myself."),
    c("p7-help", 7, "Please help ___ to coffee.", "Угощайтесь кофе.", ["yourself", "you", "yours"], "yourself", "Угощайтесь — help yourself."),
    c("p7-alone", 7, "He lives by ___.", "Он живёт один.", ["himself", "him", "his"], "himself", "Сам, в одиночку — by himself."),
    c("p7-feel", 7, "I feel ___ today.", "Сегодня я чувствую себя гораздо лучше.", ["much better", "myself much better"], "much better",
      "«Чувствовать себя» — feel, без myself."),
    c("p7-children", 7, "The children did it all by ___.", "Дети всё сделали сами.", ["themselves", "them", "theirs"], "themselves",
      "Сами, без помощи — by themselves."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
