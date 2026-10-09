# Содержание тренажёра «Three, tree, sheep» — слова, которые различаются одним звуком, и звуки, на которых
# спотыкаются русскоговорящие: th, долгие и короткие гласные, [æ] и [e], walk и work, w и v, h, звонкие на конце, [ŋ].
# Отличие от «Пар слов» (pairs): там слова-ловушки по смыслу и написанию, здесь — по звучанию.
# Карточки двух видов: «по смыслу» — выбрать слово для предложения и услышать его; «на слух» (ear) — Ryan
# произносит Say ___ again, нужно выбрать, какое слово прозвучало (перевод скрыт до ответа).
# Разметка в примерах: [слово|a] — оранжевый, [слово|b] — синий, [слово|c] — зелёный, [слово] — подчёркнуто.
# Темы с полем late вступают в общую тренировку позже.

MIXED_TOPIC = 11

GROUPS = {
    "b1": "B1 — согласные, которых нет в русском",
    "b1p": "B1+ — гласные: долгие, короткие, открытые",
    "b2": "B2 — концы слов",
    "mix": "Итог",
}

# Главная таблица: звук | как произнести («главное — пояснение») | пары
TABLE = [
    ["[θ] three", "язык между зубами — выдох без голоса", "three · tree · free · think · sink"],
    ["[ð] they", "то же, но с голосом — не [z] и не [d]", "they · day · breathe · breeze"],
    ["[iː] sheep · [ɪ] ship", "долгий с улыбкой — короткий, ближе к «ы»", "sheep · ship · leave · live"],
    ["[æ] bad · [e] bed", "рот широко, «э» с «а» — обычное «э»", "bad · bed · man · men"],
    ["[ɔː] walk · [ɜː] work", "долгое круглое «о» — «ё» без губ", "walk · work · ward · word"],
    ["[w] wet · [v] vet", "губы трубочкой — зубы на губе", "wet · vet · west · vest"],
    ["[h] hill", "лёгкий выдох, не русское «х»", "hill · ill · hear · ear"],
    ["bag · back", "звонкий конец не оглушать — гласная длиннее", "bag · back · eyes · ice"],
    ["[ŋ] thing", "звук в нос, без «г» на конце", "thing · thin · wing · win"],
]

# Одна ситуация — разный звук: строки [английский, перевод]
CONTRAST = [
    [["I can see [three|a] [trees|b].", "три — дерева"],
     ["Feel [free|c] to ask.", "спрашивайте, не стесняйтесь"]],
    [["The [sheep|a] are on the [ship|b].", "овцы — на корабле"],
     ["You can [leave|a] — you don't [live|b] here.", "уходить — жить"]],
    [["I [think|a] it will [sink|b].", "думаю — утонет"],
     ["[Breathe|a] in — feel the [breeze|b].", "дышите — ветерок"]],
    [["He [walks|a] to [work|b].", "ходит пешком — на работу"],
     ["Which [ward|a]? Say the [word|b].", "палата — слово"]],
    [["The [man|a] in [bed|b] three feels [bad|a].", "мужчина — кровать — плохо"],
     ["He's [ill|a] — don't let him climb the [hill|b].", "болен — холм"]],
]

# Часто путают: неверно | верно | пояснение
ERRORS = [
    ["I sink so.", "I think so.", "думаю — think, язык между зубами"],
    ["Tree tablets a day.", "Three tablets a day.", "три — three [θ]"],
    ["Breeze in slowly.", "Breathe in slowly.", "дышите — breathe [ð]"],
    ["I live hospital tomorrow.", "I leave hospital tomorrow.", "выписаться — leave, долгий [iː]"],
    ["Three man came in.", "Three men came in.", "мужчины — men [e]"],
    ["I walk in a hospital.", "I work in a hospital.", "работать — work [ɜː]"],
    ["Don't get the dressing vet.", "Don't get the dressing wet.", "мокрый — wet [w]"],
    ["He's hill.", "He's ill.", "болен — ill, без [h]"],
    ["I've got bag pain.", "I've got back pain.", "спина — back"],
    ["One more thin.", "One more thing.", "вещь — thing [ŋ]"],
]

TOPICS = [
    {"n": 1, "group": "b1", "title": "three, tree, free", "sub": "глухой th [θ]",
     "rule": "th в three, think, thank, mouth, health — глухой [θ]: кончик языка между зубами или у края верхних зубов, выдох без голоса. Русскоговорящие ставят вместо него [t], [s] или [f] — и выходит другое слово: three — tree — free, think — sink, thank — tank, mouth — mouse, thin — tin. Тренируйте медленно: язык между зубами, потом подуть.",
     "ex": [
         {"en": "I can see [three|a] [trees|b].", "ru": "Я вижу три дерева."},
         {"en": "I [think|a] it will [sink|b].", "ru": "Думаю, оно утонет."},
         {"en": "Open your [mouth|a] — it's not a [mouse|b].", "ru": "Откройте рот — это не мышь."},
     ]},
    {"n": 2, "group": "b1", "title": "they, day, breathe", "sub": "звонкий th [ð]",
     "rule": "th в the, this, they, then, mother, breathe, clothing — звонкий [ð]: язык так же между зубами, но с голосом. Русскоговорящие заменяют его на [z] или [d]: they — day, then — den, breathe — breeze, clothing — closing. Положение языка то же, что в three, — просто добавьте голос.",
     "ex": [
         {"en": "[They|a] came the next [day|b].", "ru": "Они пришли на следующий день."},
         {"en": "[Breathe|a] in — feel the [breeze|b].", "ru": "Вдохните — почувствуйте ветерок."},
         {"en": "[Clothing|a] shops are [closing|b] early today.", "ru": "Магазины одежды сегодня закрываются рано."},
     ]},
    {"n": 3, "group": "b1", "title": "w и v, h и без h", "sub": "wet · vet · hill · ill",
     "rule": "[w] — губы трубочкой, зубы не участвуют, как короткое «у»: wet, west, wine, worse. [v] — верхние зубы на нижней губе: vet, vest, vine, verse. Русскоговорящие говорят [v] в обоих случаях. [h] — лёгкий выдох, как на холодное стекло, без хрипа русского «х». Пропустите его — получится другое слово: hill — ill, hear — ear, hair — air. В hour, honest, heir h не читается.",
     "ex": [
         {"en": "Don't get it [wet|a] — take the dog to the [vet|b].", "ru": "Не мочите — отведите собаку к ветеринару."},
         {"en": "He's [ill|a] — don't let him climb the [hill|b].", "ru": "Он болен — не пускайте его на холм."},
         {"en": "Can you [hear|a] me in your left [ear|b]?", "ru": "Вы слышите меня левым ухом?"},
     ]},
    {"n": 4, "group": "b1p", "title": "sheep или ship", "sub": "долгий [iː] и короткий [ɪ]", "late": 0.2,
     "rule": "[iː] — долгий и напряжённый, губы в улыбке: sheep, leave, feel, seat, heel, peel. [ɪ] — короткий и расслабленный, между русскими «и» и «ы»: ship, live, fill, sit, hill, pill. Русское «и» где-то посередине, поэтому пары сливаются: leave — live, peel — pill. Осторожно: sheet, beach, piece с коротким звуком превращаются в грубые слова — тяните [iː].",
     "ex": [
         {"en": "The [sheep|a] are on the [ship|b].", "ru": "Овцы на корабле."},
         {"en": "You can [leave|a] tomorrow — you don't [live|b] here.", "ru": "Завтра можете выписываться — вы же здесь не живёте."},
         {"en": "Don't [peel|a] the [pill|b].", "ru": "Не счищайте оболочку с таблетки."},
     ]},
    {"n": 5, "group": "b1p", "title": "bad или bed, man или men", "sub": "открытое [æ] и [e]", "late": 0.2,
     "rule": "[æ] — рот открыт широко, нижняя челюсть вниз, звук между «а» и «э»: bad, man, sad, had, pan. [e] — обычное русское «э»: bed, men, said, head, pen. Русскоговорящие говорят «э» в обоих — и man (один) звучит как men (несколько), bad — как bed. Проверьте себя: на [æ] под подбородок должен помещаться палец.",
     "ex": [
         {"en": "The [man|a] in [bed|b] three feels [bad|a].", "ru": "Мужчине на третьей кровати плохо."},
         {"en": "Three [men|b] and one [man|a].", "ru": "Трое мужчин и ещё один."},
         {"en": "She [said|b] she felt [sad|a].", "ru": "Она сказала, что ей грустно."},
     ]},
    {"n": 6, "group": "b1p", "title": "cat, cut, cart", "sub": "[æ], [ʌ] и [ɑː]", "late": 0.25,
     "rule": "Три «а». [æ] — широко, «э-а»: cat, hat, cap, match. [ʌ] — короткое русское «а», рот открыт средне: cut, hut, cup, much. [ɑː] — долгое глубокое «а», как у врача «скажите а-а»: cart, heart, carp, march; r в британском не читается. Перепутаете — и вместо heart rate выйдет hat rate.",
     "ex": [
         {"en": "His [heart|c] rate is 110.", "ru": "Пульс у него 110."},
         {"en": "He [cut|b] his finger on the [cat|a] food tin.", "ru": "Он порезал палец о банку кошачьего корма."},
         {"en": "Would you like a [cup|b] of tea?", "ru": "Хотите чашку чая?"},
     ]},
    {"n": 7, "group": "b1p", "title": "walk или work", "sub": "[ɔː] и [ɜː]", "late": 0.25,
     "rule": "[ɔː] — долгое округлённое «о»: walk, ward, born, short, law. [ɜː] — «ё» без округления губ, язык посередине, как в задумчивом «э-э»: work, word, burn, shirt, turn. Русскоговорящие говорят «уо» в обоих: walk — work, ward — word. В больнице это особенно заметно: ward — палата, word — слово; born — рождён, burn — ожог.",
     "ex": [
         {"en": "He [walks|a] to [work|b].", "ru": "Он ходит на работу пешком."},
         {"en": "Which [ward|a]? Say the [word|b].", "ru": "Какая палата? Назовите."},
         {"en": "I was [born|a] here, but the old house [burned|b] down.", "ru": "Я здесь родился, но старый дом сгорел."},
     ]},
    {"n": 8, "group": "b2", "title": "bag или back", "sub": "звонкий конец не оглушать", "late": 0.45,
     "rule": "По-русски звонкий в конце оглушается: «дуб» — «дуп». По-английски нельзя: bag — back, leave — leaf, prize — price, eyes — ice, cab — cap. Главный признак звонкого конца даже не сам звук, а гласная перед ним: перед звонким она заметно длиннее. bag — протяжно, back — коротко и резко.",
     "ex": [
         {"en": "Put the [bag|a] behind your [back|b].", "ru": "Положите сумку за спину."},
         {"en": "Close your [eyes|a] — I'll put some [ice|b] on it.", "ru": "Закройте глаза — я приложу лёд."},
         {"en": "The [prize|a] is worth the [price|b].", "ru": "Приз стоит своей цены."},
     ]},
    {"n": 9, "group": "b2", "title": "thing или thin", "sub": "[ŋ] — звук в нос", "late": 0.5,
     "rule": "[ŋ] — задняя часть языка прижата к нёбу, звук идёт в нос, как в «гонг» без «г». Это не [n] и не «нг»: [g] в конце не добавляйте — sing, а не «синг». В окончании -ing тоже [ŋ]: walking, bleeding. Если сказать [n], выйдет другое слово: thing — thin, wing — win, rang — ran, tongue — ton.",
     "ex": [
         {"en": "One more [thing|a] — you look very [thin|b].", "ru": "И ещё — вы очень худой."},
         {"en": "Stick out your [tongue|a], please.", "ru": "Покажите язык, пожалуйста."},
         {"en": "The phone [rang|a] as I [ran|b] in.", "ru": "Телефон зазвонил, когда я вбежал."},
     ]},
    {"n": 10, "group": "b2", "title": "Всё на слух", "sub": "Say ___ again", "late": 0.6,
     "rule": "Тема только на слух: Ryan произносит Say … again, а вы выбираете, какое слово прозвучало. Сначала слушайте гласную: долгая или короткая, открытая или нет; потом начало и конец слова: th или t, w или v, h или нет, звонкий конец или глухой. Если трудно — нажмите «Послушать ещё раз» и повторите вслух.",
     "ex": [
         {"en": "Say [sheep|a] again. Say [ship|b] again.", "ru": "Скажите sheep ещё раз. Скажите ship ещё раз."},
         {"en": "Say [walk|a] again. Say [work|b] again.", "ru": "Скажите walk ещё раз. Скажите work ещё раз."},
         {"en": "Say [three|a] again. Say [tree|b] again.", "ru": "Скажите three ещё раз. Скажите tree ещё раз."},
     ]},
    {"n": 11, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

def ear(id, t, opts, a, why):
    """Карточка на слух: Ryan произносит Say <слово> again, перевод скрыт до ответа."""
    return {"id": id, "t": t, "q": "Say ___ again.", "ru": "", "opts": opts, "a": a, "why": why, "ear": 1}

CARDS = [
    # 1 · [θ]
    c("s1-three", 1, "Take one tablet ___ times a day.", "Принимайте по одной таблетке три раза в день.",
      ["three", "tree", "free"], "three", "three /θriː/ — три: язык между зубами. tree /triː/ — дерево, free /friː/ — бесплатный, свободный."),
    c("s1-free", 1, "The consultation is ___ for pensioners.", "Для пенсионеров консультация бесплатная.",
      ["free", "three", "tree"], "free", "free /friː/ — бесплатный. Скажете [θ] вместо [f] — получится three."),
    c("s1-think", 1, "What do you ___ about his scan?", "Что вы думаете о его снимке?",
      ["think", "sink", "thing"], "think", "think /θɪŋk/ — думать. sink /sɪŋk/ — раковина, тонуть; thing /θɪŋ/ — вещь."),
    c("s1-mouth", 1, "Open your ___ and say ah.", "Откройте рот и скажите «а».",
      ["mouth", "mouse", "mouths"], "mouth", "mouth /maʊθ/ — рот, на конце [θ]. mouse /maʊs/ — мышь."),
    ear("s1-ear-tree", 1, ["three", "tree", "free"], "tree", "Прозвучало tree /triː/ — дерево: [t], язык за зубами. three /θriː/ — язык между зубами, free /friː/ — губа и зубы."),
    ear("s1-ear-thank", 1, ["thank", "tank", "sank"], "thank", "Прозвучало thank /θæŋk/ — благодарить: язык между зубами. tank /tæŋk/ — бак, sank /sæŋk/ — утонул."),

    # 2 · [ð]
    c("s2-they", 2, "___ arrived at the hospital at midnight.", "Они приехали в больницу в полночь.",
      ["They", "Day"], "They", "they /ðeɪ/ — они: звонкий th. day /deɪ/ — день."),
    c("s2-breathe", 2, "___ in slowly through your nose.", "Медленно вдохните через нос.",
      ["Breathe", "Breeze"], "Breathe", "breathe /briːð/ — дышать, звонкий th. breeze /briːz/ — ветерок."),
    c("s2-then", 2, "Take the first tablet now and ___ another one at night.", "Первую таблетку примите сейчас, а потом ещё одну на ночь.",
      ["then", "den", "than"], "then", "then /ðen/ — потом. den /den/ — логово, than /ðæn/ — чем (в сравнениях)."),
    c("s2-clothing", 2, "Remove any ___ with metal before the MRI.", "Перед МРТ снимите одежду с металлом.",
      ["clothing", "closing"], "clothing", "clothing /ˈkləʊðɪŋ/ — одежда, звонкий th. closing /ˈkləʊzɪŋ/ — закрытие."),
    ear("s2-ear-day", 2, ["they", "day"], "day", "Прозвучало day /deɪ/ — день: [d], язык за зубами. they /ðeɪ/ — язык между зубами, с голосом."),
    ear("s2-ear-breeze", 2, ["breathe", "breeze"], "breeze", "Прозвучало breeze /briːz/ — ветерок: [z]. breathe /briːð/ — язык между зубами."),

    # 3 · w и v, h
    c("s3-wet", 3, "Keep the dressing dry — don't let it get ___.", "Повязка должна оставаться сухой — не мочите её.",
      ["wet", "vet"], "wet", "wet /wet/ — мокрый: губы трубочкой. vet /vet/ — ветеринар: зубы на губе."),
    c("s3-worse", 3, "His speech is getting ___.", "Речь у него становится хуже.",
      ["worse", "verse"], "worse", "worse /wɜːs/ — хуже. verse /vɜːs/ — стих."),
    c("s3-ill", 3, "He's been ___ for a week.", "Он болеет уже неделю.",
      ["ill", "hill"], "ill", "ill /ɪl/ — больной, без [h]. hill /hɪl/ — холм."),
    c("s3-hour", 3, "Come back in an ___.", "Приходите через час.",
      ["hour", "our"], "hour", "hour /ˈaʊə/ — час: h не читается, поэтому an hour. our — наш, звучит так же."),
    ear("s3-ear-vest", 3, ["west", "vest"], "vest", "Прозвучало vest /vest/ — майка, жилет: зубы на губе. west /west/ — запад: губы трубочкой."),
    ear("s3-ear-eat", 3, ["heat", "eat"], "eat", "Прозвучало eat /iːt/ — есть, без [h]. heat /hiːt/ — жара: лёгкий выдох в начале."),

    # 4 · [iː] и [ɪ]
    c("s4-pill", 4, "Take this ___ with a glass of water.", "Примите эту таблетку, запив стаканом воды.",
      ["pill", "peel"], "pill", "pill /pɪl/ — таблетка, короткий звук. peel /piːl/ — кожура, чистить, долгий."),
    c("s4-leave", 4, "You can ___ hospital tomorrow.", "Завтра можете выписываться.",
      ["leave", "live"], "leave", "leave /liːv/ — уйти, выписаться, долгий. live /lɪv/ — жить, короткий."),
    c("s4-heel", 4, "The pain is in my ___ when I walk.", "При ходьбе болит пятка.",
      ["heel", "hill"], "heel", "heel /hiːl/ — пятка, долгий. hill /hɪl/ — холм, короткий."),
    c("s4-seat", 4, "Please take a ___.", "Присаживайтесь, пожалуйста.",
      ["seat", "sit"], "seat", "seat /siːt/ — место, сиденье: take a seat. sit /sɪt/ — сидеть."),
    ear("s4-ear-ship", 4, ["sheep", "ship"], "ship", "Прозвучало ship /ʃɪp/ — корабль: короткий, расслабленный. sheep /ʃiːp/ — овца: долгий, с улыбкой."),
    ear("s4-ear-feel", 4, ["feel", "fill"], "feel", "Прозвучало feel /fiːl/ — чувствовать: долгий. fill /fɪl/ — наполнить: короткий."),

    # 5 · [æ] и [e]
    c("s5-men", 5, "Three ___ were admitted after the accident.", "После аварии госпитализировали троих мужчин.",
      ["men", "man"], "men", "men /men/ — мужчины, как «э». man /mæn/ — мужчина, рот шире."),
    c("s5-bed", 5, "He's been in ___ for three days.", "Он лежит уже три дня.",
      ["bed", "bad"], "bed", "bed /bed/ — кровать. bad /bæd/ — плохой, рот шире."),
    c("s5-bad", 5, "I've got a ___ headache.", "У меня сильно болит голова.",
      ["bad", "bed"], "bad", "bad /bæd/ — плохой, сильный (о боли): рот открыт широко."),
    c("s5-pen", 5, "Can I borrow your ___ to sign the form?", "Можно вашу ручку — подписать бланк?",
      ["pen", "pan"], "pen", "pen /pen/ — ручка. pan /pæn/ — сковорода."),
    ear("s5-ear-man", 5, ["man", "men"], "man", "Прозвучало man /mæn/ — мужчина: рот широко, «э» с «а». men /men/ — обычное «э»."),
    ear("s5-ear-said", 5, ["sad", "said"], "said", "Прозвучало said /sed/ — сказал: обычное «э». sad /sæd/ — грустный: рот шире."),

    # 6 · [æ], [ʌ], [ɑː]
    c("s6-heart", 6, "His ___ rate is 110.", "Пульс у него 110.",
      ["heart", "hut", "hat"], "heart", "heart /hɑːt/ — сердце: долгое глубокое «а». hut /hʌt/ — хижина, hat /hæt/ — шляпа."),
    c("s6-cut", 6, "He ___ his finger on a broken glass.", "Он порезал палец о разбитый стакан.",
      ["cut", "cat", "cart"], "cut", "cut /kʌt/ — порезать: короткое «а». cat /kæt/ — кошка, cart /kɑːt/ — тележка."),
    c("s6-cup", 6, "Would you like a ___ of tea?", "Хотите чашку чая?",
      ["cup", "cap", "carp"], "cup", "cup /kʌp/ — чашка. cap /kæp/ — кепка, колпачок, carp /kɑːp/ — карп."),
    c("s6-much", 6, "How ___ does it hurt?", "Насколько сильно болит?",
      ["much", "match", "march"], "much", "much /mʌtʃ/ — много. match /mætʃ/ — спичка, матч, march /mɑːtʃ/ — марш."),
    ear("s6-ear-hat", 6, ["hat", "hut", "heart"], "hat", "Прозвучало hat /hæt/ — шляпа: широко, «э-а». hut /hʌt/ — короткое «а», heart /hɑːt/ — долгое."),
    ear("s6-ear-cart", 6, ["cat", "cut", "cart"], "cart", "Прозвучало cart /kɑːt/ — тележка: долгое глубокое «а». cat /kæt/ — широкое «э-а», cut /kʌt/ — короткое «а»."),

    # 7 · [ɔː] и [ɜː]
    c("s7-ward", 7, "He was moved to the stroke ___ this morning.", "Утром его перевели в инсультное отделение.",
      ["ward", "word"], "ward", "ward /wɔːd/ — палата, отделение: круглое «о». word /wɜːd/ — слово."),
    c("s7-work", 7, "I go to ___ by bus.", "На работу я езжу на автобусе.",
      ["work", "walk"], "work", "work /wɜːk/ — работа: «ё» без губ. walk /wɔːk/ — ходить пешком."),
    c("s7-burn", 7, "She has a ___ on her hand from the kettle.", "У неё ожог на руке от чайника.",
      ["burn", "born"], "burn", "burn /bɜːn/ — ожог. born /bɔːn/ — рождён."),
    c("s7-born", 7, "He was ___ in 1958.", "Он родился в 1958 году.",
      ["born", "burn"], "born", "born /bɔːn/ — рождён: круглое «о»."),
    ear("s7-ear-walk", 7, ["walk", "work"], "walk", "Прозвучало walk /wɔːk/ — ходить: круглое долгое «о», l не читается. work /wɜːk/ — «ё» без губ."),
    ear("s7-ear-word", 7, ["ward", "word"], "word", "Прозвучало word /wɜːd/ — слово: «ё» без губ. ward /wɔːd/ — круглое «о»."),

    # 8 · звонкий конец
    c("s8-back", 8, "I've had ___ pain for a month.", "Спина болит уже месяц.",
      ["back", "bag"], "back", "back /bæk/ — спина: коротко и резко. bag /bæɡ/ — сумка: гласная длиннее, [g] звонкий."),
    c("s8-bag", 8, "Put your phone in your ___.", "Положите телефон в сумку.",
      ["bag", "back"], "bag", "bag /bæɡ/ — сумка: не оглушайте [g], тяните гласную."),
    c("s8-eyes", 8, "Close your ___.", "Закройте глаза.",
      ["eyes", "ice"], "eyes", "eyes /aɪz/ — глаза: звонкий [z]. ice /aɪs/ — лёд."),
    c("s8-cab", 8, "We'll call you a ___ to take you home.", "Мы вызовем вам такси домой.",
      ["cab", "cap"], "cab", "cab /kæb/ — такси: звонкий [b]. cap /kæp/ — кепка, колпачок."),
    ear("s8-ear-leaf", 8, ["leave", "leaf"], "leaf", "Прозвучало leaf /liːf/ — лист: глухой [f], гласная короче. leave /liːv/ — звонкий [v], гласная длиннее."),
    ear("s8-ear-prize", 8, ["prize", "price"], "prize", "Прозвучало prize /praɪz/ — приз: звонкий [z], гласная длиннее. price /praɪs/ — цена."),

    # 9 · [ŋ]
    c("s9-thing", 9, "There's one more ___ I need to ask.", "Мне нужно спросить ещё одну вещь.",
      ["thing", "thin"], "thing", "thing /θɪŋ/ — вещь: [ŋ] в нос. thin /θɪn/ — худой, тонкий."),
    c("s9-thin", 9, "She's very ___ — she's lost 10 kg.", "Она очень худая — похудела на 10 кг.",
      ["thin", "thing"], "thin", "thin /θɪn/ — худой: обычное [n]."),
    c("s9-tongue", 9, "Stick out your ___, please.", "Покажите язык, пожалуйста.",
      ["tongue", "ton"], "tongue", "tongue /tʌŋ/ — язык: на конце [ŋ], ue не читается. ton /tʌn/ — тонна."),
    c("s9-rang", 9, "The phone ___ in the middle of the night.", "Посреди ночи зазвонил телефон.",
      ["rang", "ran"], "rang", "rang /ræŋ/ — зазвонил. ran /ræn/ — бежал."),
    ear("s9-ear-win", 9, ["wing", "win"], "win", "Прозвучало win /wɪn/ — победить: [n]. wing /wɪŋ/ — крыло, крыло больницы: [ŋ] в нос."),
    ear("s9-ear-sung", 9, ["sun", "sung"], "sung", "Прозвучало sung /sʌŋ/ — спет: [ŋ] в нос. sun /sʌn/ — солнце: [n]."),

    # 10 · всё на слух
    ear("s10-sheep", 10, ["sheep", "ship"], "sheep", "Прозвучало sheep /ʃiːp/ — овца: долгий звук с улыбкой."),
    ear("s10-think", 10, ["think", "sink"], "sink", "Прозвучало sink /sɪŋk/ — раковина, тонуть: [s]. think /θɪŋk/ — язык между зубами."),
    ear("s10-work", 10, ["walk", "work"], "work", "Прозвучало work /wɜːk/ — работа: «ё» без губ."),
    ear("s10-bad", 10, ["bad", "bed"], "bad", "Прозвучало bad /bæd/ — плохой: рот открыт широко."),
    ear("s10-wet", 10, ["wet", "vet"], "wet", "Прозвучало wet /wet/ — мокрый: губы трубочкой, зубы не касаются губы."),
    ear("s10-hill", 10, ["hill", "ill"], "hill", "Прозвучало hill /hɪl/ — холм: лёгкий выдох в начале."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
    for alt in k.get("also", {}): assert alt in k["opts"] and alt != k["a"], k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))
assert all(t["group"] in GROUPS for t in TOPICS) and [t["n"] for t in TOPICS] == list(range(1, MIXED_TOPIC + 1))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sum(1 for k in CARDS if k.get("ear")), "на слух", sorted(Counter(k["t"] for k in CARDS).items()))
