# Содержание приложения «two, too или to».
# Пометки: {…} — two (синий), _…_ — too (оранжевый), |…| — to (зелёный).

MIXED_TOPIC = 11

# Три слова: слово | цвет | звук и смысл | примеры | подсказка | текст для озвучки
WORDS = [
    {"w": "two", "cls": "st", "sound": "[tuː]", "mean": "два",
     "ex": ["two patients", "two o'clock", "the two of us"],
     "tip": "Есть w — как в twin, twice, twelve, twenty, between: у них у всех корень «два».",
     "say": "two patients. two o'clock. the two of us."},
    {"w": "too", "cls": "pr", "sound": "[tuː]", "mean": "слишком · тоже",
     "ex": ["too hot", "too late", "Me too."],
     "tip": "Лишняя o — «слишком много o». «Тоже» — в конце фразы: I'm tired too.",
     "say": "too hot. too late. me too."},
    {"w": "to", "cls": "good", "sound": "[tə]", "mean": "куда, кому, до, + глагол",
     "ex": ["to the ward", "give it to me", "want to go"],
     "tip": "Самое короткое — как стрелка →. В речи обычно звучит кратко: [tə].",
     "say": "to the ward. give it to me. I want to go."},
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["It's to late.", "It's too late.", "слишком — too"],
    ["Me to.", "Me too.", "тоже — too"],
    ["I have too children.", "I have two children.", "число 2 — two"],
    ["I'm going too the hospital.", "I'm going to the hospital.", "куда — to"],
    ["Too be honest…", "To be honest…", "to + глагол"],
    ["Go to home.", "Go home.", "home — без to"],
    ["The tea is very hot to drink.", "The tea is too hot to drink.", "слишком…, чтобы — too … to"],
    ["He isn't enough strong.", "He isn't strong enough.", "enough — после прилагательного"],
    ["I don't smoke too.", "I don't smoke either.", "«тоже» в отрицании — either"],
    ["too much patients", "too many patients", "то, что считаем, — many"],
]

TOPICS = [
    {"n": 1, "title": "two — два", "sub": "two patients · two o'clock",
     "rule": "two — это число 2: two patients, two o'clock, the two of us (мы вдвоём), two-thirds. Подсказка: w — как в twin, twice, twelve, twenty, between. У всех этих слов корень «два».",
     "ex": [
         {"en": "We have {two} patients waiting.", "ru": "У нас в ожидании два пациента."},
         {"en": "Take {two} tablets a day.", "ru": "Принимайте две таблетки в день."},
         {"en": "{two}, twin, twice, twelve, twenty", "ru": "tw- — «два»: близнец, дважды, двенадцать, двадцать"},
     ]},
    {"n": 2, "title": "too — слишком", "sub": "too hot · too late",
     "rule": "too — «слишком»: too hot, too late, too fast. Too + прилагательное + to + глагол — «слишком…, чтобы»: too weak to walk. Подсказка: в too лишняя o — «слишком много o».",
     "ex": [
         {"en": "It's _too_ hot.", "ru": "Слишком жарко."},
         {"en": "He's _too_ weak |to| walk.", "ru": "Он слишком слаб, чтобы ходить."},
         {"en": "Don't eat _too_ much.", "ru": "Не ешьте слишком много."},
     ]},
    {"n": 3, "title": "too — тоже", "sub": "Me too · I'm tired too",
     "rule": "too — ещё и «тоже», в конце фразы: Me too. My wife is a doctor too. Перед глаголом вместо него — also: He also has diabetes. В разговоре ещё as well — тоже в конце.",
     "ex": [
         {"en": "I'm tired. — Me _too_.", "ru": "Я устал. — Я тоже."},
         {"en": "My wife is a doctor _too_.", "ru": "Моя жена тоже врач."},
         {"en": "Nice |to| meet you, _too_.", "ru": "Мне тоже приятно познакомиться."},
     ]},
    {"n": 4, "title": "to — куда и кому", "sub": "to the ward · give it to me",
     "rule": "to — куда: go to the ward, send it to the lab; кому: give it to me, talk to him. Home — без to: go home, come home.",
     "ex": [
         {"en": "Take him |to| the ward.", "ru": "Отвезите его в отделение."},
         {"en": "Give it |to| me.", "ru": "Дайте это мне."},
         {"en": "Go home and rest.", "ru": "Идите домой и отдохните. — home без to"},
     ]},
    {"n": 5, "title": "to + глагол", "sub": "want to go · came to see",
     "rule": "to + глагол: want to go, need to rest, be able to speak. «Чтобы» — тоже to: I came to see you. Устойчивые: To be honest… Nice to meet you.",
     "ex": [
         {"en": "I want |to| check it again.", "ru": "Я хочу проверить это ещё раз."},
         {"en": "I came |to| see how you are.", "ru": "Я пришёл узнать, как вы. — to = чтобы"},
         {"en": "|To| be honest, I'm not sure.", "ru": "Честно говоря, я не уверен."},
     ]},
    {"n": 6, "title": "to — до и «без»", "sub": "from 8 to 5 · ten to six",
     "rule": "to — «до»: from 8 to 5, from Monday to Friday, count to ten. Во времени — «без»: ten to six — без десяти шесть, a quarter to two — без четверти два.",
     "ex": [
         {"en": "We're open from 8 |to| 5.", "ru": "Мы работаем с восьми до пяти."},
         {"en": "It's ten |to| six.", "ru": "Без десяти шесть."},
         {"en": "It's a quarter |to| {two}.", "ru": "Без четверти два. — здесь и to, и two"},
     ]},
    {"n": 7, "title": "two, too или to?", "sub": "все три в одной фразе",
     "rule": "Проверка: число 2 — two. «Слишком» или «тоже» — too. Всё остальное — to. В одной фразе могут быть все три.",
     "ex": [
         {"en": "{Two} teas |to| go, please — not _too_ hot.", "ru": "Два чая с собой, пожалуйста, не слишком горячих."},
         {"en": "I have |to| see {two} more patients _too_.", "ru": "Мне тоже нужно осмотреть ещё двух пациентов."},
     ]},
    {"n": 8, "title": "too, very или enough", "sub": "очень · слишком · достаточно",
     "rule": "very — «очень», без проблемы: very hot, but OK. too — «слишком», есть проблема: too hot to drink. enough — «достаточно», ставится после прилагательного: strong enough, not old enough.",
     "ex": [
         {"en": "The tea is very hot.", "ru": "Чай очень горячий. — но пить можно"},
         {"en": "The tea is _too_ hot |to| drink.", "ru": "Чай слишком горячий — пить нельзя."},
         {"en": "He isn't strong enough |to| walk.", "ru": "Он ещё недостаточно окреп, чтобы ходить."},
     ]},
    {"n": 9, "title": "too или either", "sub": "«тоже» в отрицании",
     "rule": "«Тоже» в утверждении — too: I like it too. В отрицании — either: I don't smoke either. Коротко: Me too и Me neither. Шаг к B2: So am I · Neither do I.",
     "ex": [
         {"en": "I don't smoke. — I don't either.", "ru": "Я не курю. — Я тоже."},
         {"en": "I don't smoke. — Me neither.", "ru": "Я не курю. — Я тоже нет."},
         {"en": "I'm tired. — So am I.", "ru": "Я устал. — Я тоже."},
     ]},
    {"n": 10, "title": "too much или too many", "sub": "считаем или нет",
     "rule": "too many — с тем, что считаем: too many patients, too many tablets. too much — с тем, что не считаем: too much blood, too much time. После глагола — too much: You work too much.",
     "ex": [
         {"en": "There are _too_ many patients today.", "ru": "Сегодня слишком много пациентов. — считаем"},
         {"en": "He lost _too_ much blood.", "ru": "Он потерял слишком много крови. — не считаем"},
         {"en": "You work _too_ much.", "ru": "Ты слишком много работаешь."},
     ]},
    {"n": 11, "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

W3 = ["two", "too", "to"]
def c(id, t, q, ru, a, why, opts=None, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts or W3, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · two
    c("tw-patients", 1, "We admitted ___ patients with stroke last night.", "Прошлой ночью мы госпитализировали двух пациентов с инсультом.", "two", "Число 2 — two."),
    c("tw-oclock", 1, "The meeting starts at ___ o'clock.", "Совещание начинается в два часа.", "two", "Два часа — two o'clock."),
    c("tw-tablets", 1, "Take ___ tablets in the morning.", "Утром принимайте две таблетки.", "two", "Число 2 — two."),
    c("tw-us", 1, "Just the ___ of us are on call tonight.", "Сегодня дежурим только мы вдвоём.", "two", "the two of us — «мы вдвоём»."),
    c("tw-weeks", 1, "Come back in ___ weeks.", "Приходите через две недели.", "two", "Через две недели — in two weeks."),
    c("tw-thirds", 1, "About ___-thirds of the patients improved.", "Примерно у двух третей пациентов наступило улучшение.", "two", "two-thirds — «две трети»."),

    # 2 · too — слишком
    c("ts-hot", 2, "The tea is ___ hot to drink.", "Чай слишком горячий, чтобы пить.", "too", "«Слишком» — too."),
    c("ts-late", 2, "It's ___ late for thrombolysis.", "Для тромболизиса уже слишком поздно.", "too", "«Слишком поздно» — too late."),
    c("ts-weak", 2, "He's ___ weak to walk on his own.", "Он слишком слаб, чтобы ходить самостоятельно.", "too",
      "too + прилагательное + to + глагол: too weak to walk."),
    c("ts-weak-to", 2, "He's too weak ___ walk on his own.", "Он слишком слаб, чтобы ходить самостоятельно.", "to",
      "После too weak — to + глагол: to walk."),
    c("ts-fast", 2, "You're speaking ___ fast for me.", "Вы говорите для меня слишком быстро.", "too", "«Слишком быстро» — too fast."),
    c("ts-much", 2, "Don't give him ___ much fluid.", "Не давайте ему слишком много жидкости.", "too", "«Слишком много» — too much."),

    # 3 · too — тоже
    c("tt-me", 3, "I'm tired. — Me ___.", "Я устал. — Я тоже.", "too", "«Я тоже» — Me too."),
    c("tt-end", 3, "My wife is a doctor ___.", "Моя жена тоже врач.", "too", "«Тоже» в конце фразы — too."),
    c("tt-nice", 3, "Nice to meet you. — Nice to meet you, ___.", "Приятно познакомиться. — Мне тоже.", "too",
      "…, too — «тоже» в конце фразы."),
    c("tt-also", 3, "He ___ has diabetes.", "У него также диабет.", "also",
      "Перед основным глаголом — also. Too — в конце: He has diabetes too.", opts=["also", "too", "to"],
      also={"too": "так можно, но это книжно; обычно — He also has diabetes или He has diabetes too"}),
    c("tt-love", 3, "Love you! — Love you ___!", "Люблю тебя! — И я тебя!", "too", "«И я тебя» — Love you too."),
    c("tt-coffee", 3, "I'll have a coffee ___, please.", "Мне тоже кофе, пожалуйста.", "too", "«Тоже» в конце — too."),

    # 4 · to — куда и кому
    c("tk-ward", 4, "Take him ___ the stroke unit.", "Отвезите его в инсультное отделение.", "to", "Куда — to."),
    c("tk-lab", 4, "Send the sample ___ the lab.", "Отправьте образец в лабораторию.", "to", "Куда — to: to the lab."),
    c("tk-me", 4, "Give it ___ me, please.", "Дайте это мне, пожалуйста.", "to", "Кому — to: give it to me."),
    c("tk-moscow", 4, "I'm going ___ Moscow tomorrow.", "Завтра я еду в Москву.", "to", "Куда — to: going to Moscow."),
    c("tk-talk", 4, "Can I talk ___ you for a minute?", "Можно с вами поговорить минутку?", "to", "talk to someone — «поговорить с кем-то»."),
    c("tk-home", 4, "Go ___ home and rest.", "Идите домой и отдохните.", "", "home — без to: go home.", opts=["", "to", "too"]),

    # 5 · to + глагол
    c("ti-want", 5, "I want ___ check his blood pressure again.", "Я хочу ещё раз проверить его давление.", "to", "want + to + глагол."),
    c("ti-need", 5, "You need ___ rest.", "Вам нужно отдохнуть.", "to", "need + to + глагол."),
    c("ti-purpose", 5, "I came ___ see how you're feeling.", "Я пришёл узнать, как вы себя чувствуете.", "to",
      "«Чтобы» — to: I came to see…"),
    c("ti-honest", 5, "___ be honest, I'm not sure.", "Честно говоря, я не уверен.", "To", "To be honest — «честно говоря».",
      opts=["To", "Too", "Two"]),
    c("ti-nice", 5, "Nice ___ meet you.", "Приятно познакомиться.", "to", "Nice to meet you — to + глагол. А в ответе: Nice to meet you, too."),
    c("ti-able", 5, "He wasn't able ___ speak after the stroke.", "После инсульта он не мог говорить.", "to", "be able + to + глагол."),

    # 6 · to — до и «без»
    c("tn-from", 6, "The clinic is open from 8 ___ 5.", "Поликлиника работает с 8 до 5.", "to", "from … to … — «с … до …»."),
    c("tn-ten", 6, "It's ten ___ six.", "Без десяти шесть.", "to", "ten to six — «без десяти шесть»: до шести осталось десять минут."),
    c("tn-count", 6, "Count from one ___ ten.", "Посчитайте от одного до десяти.", "to", "«До» — to."),
    c("tn-quarter", 6, "It's a quarter ___ two.", "Без четверти два.", "to", "a quarter to two — «без четверти два». Здесь и to, и two."),
    c("tn-week", 6, "I work Monday ___ Friday.", "Я работаю с понедельника по пятницу.", "to", "Monday to Friday — «с понедельника по пятницу»."),

    # 7 · все три
    c("mx-go", 7, "I have ___ go now.", "Мне пора идти.", "to", "have + to + глагол: have to go."),
    c("mx-many", 7, "There are ___ many patients on the ward today.", "Сегодня в отделении слишком много пациентов.", "too", "«Слишком» — too."),
    c("mx-children", 7, "She has ___ children.", "У неё двое детей.", "two", "Число 2 — two."),
    c("mx-early", 7, "Is it ___ early to call him?", "Не слишком ли рано ему звонить?", "too", "«Слишком рано» — too early."),
    c("mx-canteen", 7, "Let's go ___ the canteen.", "Пойдём в столовую.", "to", "Куда — to."),
    c("mx-questions", 7, "I've got ___ questions.", "У меня два вопроса.", "two", "Число 2 — two."),
    c("mx-oneday", 7, "It's ___ much for one day.", "Это слишком много для одного дня.", "too", "«Слишком много» — too much."),

    # 8 · too, very или enough
    c("ve-very", 8, "The tea is ___ hot, but I can drink it.", "Чай очень горячий, но пить можно.", "very",
      "Очень, но без проблемы — very. Too — «слишком»: пить было бы нельзя.", opts=["very", "too"]),
    c("ve-too", 8, "The tea is ___ hot — I can't drink it.", "Чай слишком горячий — пить невозможно.", "too",
      "Слишком, есть проблема — too.", opts=["too", "very"]),
    c("ve-enough", 8, "He isn't strong ___ to walk yet.", "Он ещё недостаточно окреп, чтобы ходить.", "enough",
      "not + прилагательное + enough — «недостаточно».", opts=["enough", "too", "very"]),
    c("ve-old", 8, "She's old ___ to decide for herself.", "Она достаточно взрослая, чтобы решать сама.", "enough",
      "«Достаточно» — enough, после прилагательного: old enough.", opts=["enough", "too", "very"]),
    c("ve-low", 8, "The dose is ___ low to help.", "Доза слишком мала, чтобы помочь.", "too",
      "too + прилагательное + to: слишком мала, чтобы…", opts=["too", "very", "enough"]),
    c("ve-warm", 8, "Is the room warm ___?", "В палате достаточно тепло?", "enough",
      "enough — после прилагательного: warm enough. Enough warm — ошибка.", opts=["enough", "too", "very"]),

    # 9 · too или either
    c("te-either", 9, "I don't smoke. — I don't ___.", "Я не курю. — Я тоже.", "either", "«Тоже» в отрицании — either: I don't either.",
      opts=["either", "too", "neither"]),
    c("te-neither", 9, "I don't smoke. — Me ___.", "Я не курю. — Я тоже нет.", "neither", "Коротко в отрицании — Me neither.",
      opts=["neither", "too", "either"], also={"either": "так говорят в разговорном американском; нейтрально — Me neither"}),
    c("te-too", 9, "I like it. — I like it ___.", "Мне нравится. — Мне тоже.", "too", "В утверждении — too.",
      opts=["too", "either", "neither"]),
    c("te-cant", 9, "He can't swallow, and he can't speak ___.", "Он не может глотать и говорить тоже не может.", "either",
      "В отрицании — either.", opts=["either", "too", "also"]),
    c("te-so", 9, "I'm tired. — So ___ I.", "Я устал. — Я тоже.", "am", "So am I = Me too: глагол как в первой фразе (am).",
      opts=["am", "do", "too"]),

    # 10 · too much или too many
    c("tm-people", 10, "There are too ___ people in the waiting room.", "В приёмной слишком много людей.", "many",
      "people — считаем: too many.", opts=["many", "much"]),
    c("tm-alcohol", 10, "He drinks too ___ alcohol.", "Он пьёт слишком много алкоголя.", "much", "alcohol — не считаем: too much.",
      opts=["much", "many"]),
    c("tm-time", 10, "This takes too ___ time.", "Это занимает слишком много времени.", "much", "time — не считаем: too much.",
      opts=["much", "many"]),
    c("tm-tablets", 10, "She takes too ___ tablets.", "Она принимает слишком много таблеток.", "many", "tablets — считаем: too many.",
      opts=["many", "much"]),
    c("tm-work", 10, "You work too ___.", "Ты слишком много работаешь.", "much", "После глагола — too much.", opts=["much", "many", "more"]),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
