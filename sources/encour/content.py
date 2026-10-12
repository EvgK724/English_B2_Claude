# Содержание тренажёра «I know the feeling» — фразы урока (Speaking Focus), которые нужно запомнить дословно:
# Being encouraging — поддержать собеседника; Showing you have things in common — показать, что у вас было так же.
# Фразы с двух фото урока, все 15, без своих добавлений; в правилах — тонкости употребления и одна оговорка «сверх урока».
# Тренировка в четыре шага: вставить слово во фразу (темы 1–4), что ответить в ситуации (5), вспомнить фразу по-русски (6).
# Разметка в примерах: [фраза|a] — поддержать (оранжевый), [фраза|b] — общий опыт (синий).
# Темы с полем late вступают в общую тренировку позже.

MIXED_TOPIC = 7

GROUPS = {
    "enc": "Being encouraging — поддержать",
    "com": "Things in common — у меня так же",
    "use": "Применить",
    "mix": "Итог",
}

# Главная таблица: когда | смысл («главное — пояснение») | фразы
TABLE = [
    ["Подбодрить", "может, всё наладится — надежда", "It might work out fine · You never know · Never give up hope"],
    ["Успокоить", "не переживай — уверенность", "I'm sure it'll be fine · Don't worry · Good luck"],
    ["Снять вину", "ты не виноват — просто не повезло", "It's not your fault · You're just unlucky · It's never easy"],
    ["У меня так же", "общий опыт — коротко", "I know the feeling · It was the same with me · The same thing happened to me"],
    ["И у меня было", "свой похожий случай", "I've just had a similar experience · That's just like when I lost my phone"],
]

# Мини-диалоги: строки [английский, перевод]
CONTRAST = [
    [["— I failed my driving test again.", "Я опять не сдал на права."],
     ["— [Don't worry|a]. [It's never easy|a].", "Не переживай. Это всегда непросто."]],
    [["— I get my results tomorrow. I'm so nervous.", "Завтра будут результаты. Я так волнуюсь."],
     ["— [I'm sure it'll be fine|a]. [Good luck|a]!", "Уверен, всё будет хорошо. Удачи!"]],
    [["— I got lost on the way here.", "Я заблудился по дороге сюда."],
     ["— [I know the feeling|b]. [It was just like that when|b] I was looking for the cafe.", "Знакомое чувство. У меня было так же, когда я искал кафе."]],
    [["— The project was cancelled. I feel it's my fault.", "Проект закрыли. Мне кажется, это я виноват."],
     ["— [It's not your fault|a]. [We're just unlucky|a].", "Ты не виноват. Нам просто не повезло."]],
    [["— My phone died in the middle of a call.", "Телефон сел посреди разговора."],
     ["— [That's just like when|b] I lost my phone.", "Прямо как когда я потерял телефон."]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["It might work fine.", "It might work out fine.", "наладиться — work out"],
    ["Never give up the hope.", "Never give up hope.", "hope — без the"],
    ["I'm sure it will fine.", "I'm sure it'll be fine.", "будет — will be"],
    ["I know this feeling.", "I know the feeling.", "устойчиво — the feeling"],
    ["It was the same like me.", "It was the same with me.", "the same with me"],
    ["The same thing happened with me.", "The same thing happened to me.", "happen to someone"],
    ["It's not your guilt.", "It's not your fault.", "вина — fault"],
    ["I had just a similar experience.", "I've just had a similar experience.", "just — между have и had"],
    ["That's like when I have lost my phone.", "That's just like when I lost my phone.", "история — Past Simple"],
    ["Good lucky!", "Good luck!", "удача — luck"],
]

TOPICS = [
    {"n": 1, "group": "enc", "title": "It might work out fine", "sub": "подбодрить: всё может наладиться",
     "rule": "Когда человек боится, что не получится. It might work out fine — может, всё ещё наладится: work out — сложиться, наладиться; без out смысл теряется. You never know — кто знает, всякое бывает. Never give up hope — никогда не теряй надежды, hope без the. I'm sure it'll be fine — уверен, всё будет хорошо: it'll = it will, после него be. Сверх урока: пациенту исход лучше не обещать — вместо I'm sure it'll be fine скажите Let's wait for the results или We'll do everything we can.",
     "ex": [
         {"en": "[It might work out fine|a].", "ru": "Может, всё ещё наладится."},
         {"en": "[Never give up hope|a].", "ru": "Никогда не теряй надежды."},
         {"en": "[You never know|a].", "ru": "Кто знает, всякое бывает."},
         {"en": "[I'm sure it'll be fine|a].", "ru": "Уверен, всё будет хорошо."},
     ]},
    {"n": 2, "group": "enc", "title": "It's not your fault", "sub": "успокоить и снять вину",
     "rule": "Когда что-то уже пошло не так. Don't worry — не переживай. Good luck — удачи (перед событием, не после неудачи). It's not your fault — ты не виноват: fault — вина за случившееся, guilt — чувство вины. You're just unlucky / We're just unlucky — тебе (нам) просто не повезло; о прошлом — You were just unlucky. It's never easy — это всегда непросто: признать, что тяжело, — тоже поддержка.",
     "ex": [
         {"en": "[Don't worry|a].", "ru": "Не переживай."},
         {"en": "[Good luck|a].", "ru": "Удачи."},
         {"en": "[It's not your fault|a].", "ru": "Ты не виноват."},
         {"en": "[You're just unlucky|a].", "ru": "Тебе просто не повезло."},
         {"en": "[We're just unlucky|a].", "ru": "Нам просто не повезло."},
         {"en": "[It's never easy|a].", "ru": "Это всегда непросто."},
     ]},
    {"n": 3, "group": "com", "title": "I know the feeling", "sub": "у меня так же — коротко",
     "rule": "Показать, что вы понимаете, потому что было то же самое. I know the feeling — знакомое чувство: the, а не this. It was the same with me — у меня было так же: the same with, не the same like. The same thing happened to me — со мной случилось то же самое: happen to someone. I've just had a similar experience — у меня только что было похожее: just — между have и had; similar — похожий, the same — тот же самый.",
     "ex": [
         {"en": "[I know the feeling|b].", "ru": "Знакомое чувство."},
         {"en": "[It was the same with me|b].", "ru": "У меня было так же."},
         {"en": "[The same thing happened to me|b].", "ru": "Со мной случилось то же самое."},
         {"en": "[I've just had a similar experience|b].", "ru": "У меня только что было похожее."},
     ]},
    {"n": 4, "group": "com", "title": "That's just like when…", "sub": "свой похожий случай", "late": 0.2,
     "rule": "Чтобы рассказать свою похожую историю. That's just like when + прошедшее: That's just like when I lost my phone — прямо как когда я потерял телефон. It was just like that when + прошедшее: It was just like that when I was looking for the cafe — у меня было так же, когда я искал кафе. После when — Past Simple или Past Continuous, а не Present Perfect: when I lost, не when I have lost.",
     "ex": [
         {"en": "[That's just like when|b] I lost my phone.", "ru": "Прямо как когда я потерял телефон."},
         {"en": "[It was just like that when|b] I was looking for the cafe.", "ru": "У меня было так же, когда я искал кафе."},
         {"en": "[That's just like when|b] I missed my train last year.", "ru": "Прямо как когда я в прошлом году опоздал на поезд."},
     ]},
    {"n": 5, "group": "use", "title": "Что ответить", "sub": "ситуация — фраза", "late": 0.3,
     "rule": "Выбирайте по ситуации. Боится, что не получится, — It might work out fine, I'm sure it'll be fine, You never know. Сейчас начнётся — Good luck. Винит себя — It's not your fault, You're just unlucky. Устал, тяжело — It's never easy, Never give up hope. Рассказал историю, а у вас было похоже, — I know the feeling, The same thing happened to me, That's just like when…",
     "ex": [
         {"en": "— I'm so nervous about my exam. — [I'm sure it'll be fine|a].", "ru": "— Я так волнуюсь перед экзаменом. — Уверен, всё будет хорошо."},
         {"en": "— I got lost on the way here. — [I know the feeling|b].", "ru": "— Я заблудился по дороге сюда. — Знакомое чувство."},
         {"en": "— I feel it's my fault. — [It's not your fault|a].", "ru": "— Мне кажется, это я виноват. — Ты не виноват."},
     ]},
    {"n": 6, "group": "use", "title": "Как сказать по-английски", "sub": "вспомнить фразу по-русски", "late": 0.35,
     "rule": "Последний шаг — вспомнить фразу целиком по русскому смыслу. Читайте перевод, выбирайте точную формулировку и повторяйте вслух за Ryan: фразы запоминаются кусками, целиком, вместе с интонацией. Ловушки — мелочи: work out, а не work; the feeling, а не this feeling; happened to me, а не with me; it'll be, а не it will.",
     "ex": [
         {"en": "[It might work out fine|a].", "ru": "Может, всё ещё наладится."},
         {"en": "[The same thing happened to me|b].", "ru": "Со мной случилось то же самое."},
         {"en": "[It's not your fault|a].", "ru": "Ты не виноват."},
     ]},
    {"n": 7, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None, say=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    if say: d["say"] = say
    return d

CARDS = [
    # 1 · подбодрить
    c("e1-out", 1, "It might work ___ fine.", "Может, всё ещё наладится.",
      ["out", "up", "on"], "out", "work out — сложиться, наладиться."),
    c("e1-up", 1, "Never give ___ hope.", "Никогда не теряй надежды.",
      ["up", "out", "in"], "up", "give up — бросить, оставить: give up hope."),
    c("e1-hope", 1, "Never give up ___.", "Никогда не теряй надежды.",
      ["hope", "the hope", "hopes"], "hope", "hope — без the: give up hope."),
    c("e1-know", 1, "You never ___.", "Кто знает, всякое бывает.",
      ["know", "knew", "known"], "know", "You never know — устойчивая фраза: кто знает."),
    c("e1-be", 1, "I'm sure it'll ___ fine.", "Уверен, всё будет хорошо.",
      ["be", "is", "being"], "be", "it'll = it will, после will — be."),
    c("e1-might", 1, "It ___ work out fine.", "Может, всё ещё наладится.",
      ["might", "mustn't", "has"], "might", "might — может быть: It might work out fine."),

    # 2 · успокоить и снять вину
    c("e2-fault", 2, "It's not your ___.", "Ты не виноват.",
      ["fault", "guilt", "blame"], "fault", "Вина за случившееся — fault. guilt — чувство вины."),
    c("e2-unlucky", 2, "You're just ___.", "Тебе просто не повезло.",
      ["unlucky", "unhappy", "unsuccessful"], "unlucky", "Не повезло — unlucky."),
    c("e2-easy", 2, "It's never ___.", "Это всегда непросто.",
      ["easy", "easily", "simply"], "easy", "После be — прилагательное: never easy."),
    c("e2-luck", 2, "Good ___!", "Удачи!",
      ["luck", "lucky", "luckily"], "luck", "Удача — luck (существительное). Lucky — везучий."),
    c("e2-worry", 2, "Don't ___.", "Не переживай.",
      ["worry", "worried", "worrying"], "worry", "Don't + глагол в начальной форме: Don't worry."),
    c("e2-were", 2, "We're just ___ — the rain ruined everything.", "Нам просто не повезло — дождь всё испортил.",
      ["unlucky", "no lucky", "unluck"], "unlucky", "We're just unlucky — нам просто не повезло."),

    # 3 · у меня так же
    c("e3-to", 3, "The same thing happened ___ me.", "Со мной случилось то же самое.",
      ["to", "with", "for"], "to", "Случиться с кем-то — happen to someone."),
    c("e3-with", 3, "It was the same ___ me.", "У меня было так же.",
      ["with", "to", "like"], "with", "the same with me — у меня так же."),
    c("e3-feeling", 3, "I know the ___.", "Знакомое чувство.",
      ["feeling", "feel", "sense"], "feeling", "I know the feeling — устойчиво, с the."),
    c("e3-similar", 3, "I've just had a ___ experience.", "У меня только что было похожее.",
      ["similar", "same", "like"], "similar", "a similar experience — похожий опыт. The same — с the: the same experience."),
    c("e3-had", 3, "I've just ___ a similar experience.", "У меня только что было похожее.",
      ["had", "have", "having"], "had", "Present Perfect: I've just had — just между have и had."),
    c("e3-thing", 3, "The same ___ happened to me.", "Со мной случилось то же самое.",
      ["thing", "things", "think"], "thing", "The same thing — то же самое."),

    # 4 · just like when
    c("e4-like", 4, "That's just ___ when I lost my phone.", "Прямо как когда я потерял телефон.",
      ["like", "as", "so"], "like", "Прямо как когда — just like when."),
    c("e4-lost", 4, "That's just like when I ___ my phone.", "Прямо как когда я потерял телефон.",
      ["lost", "have lost", "lose"], "lost", "История из прошлого — Past Simple: when I lost."),
    c("e4-was", 4, "It was just like that when I ___ looking for the cafe.", "У меня было так же, когда я искал кафе.",
      ["was", "am", "have been"], "was", "Фон истории — Past Continuous: I was looking."),
    c("e4-that", 4, "It was just like ___ when I was looking for the cafe.", "У меня было так же, когда я искал кафе.",
      ["that", "this", "it"], "that", "It was just like that when… — у меня было так же, когда…"),
    c("e4-just", 4, "That's ___ like when I missed my train.", "Прямо как когда я опоздал на поезд.",
      ["just", "only", "even"], "just", "just like — прямо как."),
    c("e4-when", 4, "It was just like that ___ I started my first job.", "У меня было так же, когда я вышел на первую работу.",
      ["when", "what", "where"], "when", "Когда — when."),

    # 5 · что ответить
    c("e5-exam", 5, "— I'm so nervous about my exam tomorrow. — ___", "— Я так волнуюсь перед завтрашним экзаменом. Что ответить?",
      ["I'm sure it'll be fine.", "It's not your fault.", "You're just unlucky."], "I'm sure it'll be fine.", "Боится заранее — успокоить: I'm sure it'll be fine."),
    c("e5-blame", 5, "— The patient fell, and I feel it's my fault. — ___", "— Пациент упал, и мне кажется, это я виноват. Что ответить?",
      ["It's not your fault.", "Good luck.", "I'm sure it'll be fine."], "It's not your fault.", "Винит себя — снять вину: It's not your fault."),
    c("e5-lost", 5, "— I got lost on the way here. — ___ It was just like that when I was looking for the cafe.", "— Я заблудился по дороге сюда. Что ответить?",
      ["I know the feeling.", "Good luck.", "Never give up hope."], "I know the feeling.", "У вас было так же — I know the feeling."),
    c("e5-rain", 5, "— It rained every day of our holiday. — Oh no! ___", "— Весь отпуск шёл дождь. Что ответить?",
      ["You were just unlucky.", "It might work out fine.", "Good luck."], "You were just unlucky.", "О прошлом — You were just unlucky: вам просто не повезло."),
    c("e5-hard", 5, "— Rehab is so slow. I'm tired of it. — ___ But you're making progress.", "— Реабилитация идёт так медленно. Я устал. Что ответить?",
      ["It's never easy.", "It's not your fault.", "The same thing happened to me."], "It's never easy.", "Тяжело — признать это: It's never easy."),
    c("e5-job", 5, "— I don't think they'll offer me the job. — ___ They might call tomorrow.", "— Не думаю, что мне предложат эту работу. Что ответить?",
      ["You never know.", "It was the same with me.", "Good luck."], "You never know.", "Сомневается — оставить надежду: You never know."),
    c("e5-interview", 5, "— I've got an interview in ten minutes! — ___", "— У меня собеседование через десять минут! Что ответить?",
      ["Good luck!", "You're just unlucky.", "It's never easy."], "Good luck!", "Перед событием — Good luck!"),
    c("e5-flight", 5, "— My flight was cancelled and I slept at the airport. — ___ Mine was cancelled last month.", "— Мой рейс отменили, и я ночевал в аэропорту. Что ответить?",
      ["The same thing happened to me.", "Don't worry.", "Never give up hope."], "The same thing happened to me.", "У вас было то же самое — The same thing happened to me."),

    # 6 · как сказать по-английски
    c("e6-feeling", 6, "___", "Знакомое чувство.",
      ["I know the feeling.", "I know this feel.", "I know the sense."], "I know the feeling.", "I know the feeling — с the."),
    c("e6-same", 6, "___", "У меня было так же.",
      ["It was the same with me.", "It was the same like me.", "It was same with me."], "It was the same with me.", "the same with me — и the, и with."),
    c("e6-happened", 6, "___", "Со мной случилось то же самое.",
      ["The same thing happened to me.", "The same thing happened with me.", "Same thing happened at me."], "The same thing happened to me.", "happen to someone."),
    c("e6-fault", 6, "___", "Ты не виноват.",
      ["It's not your fault.", "It's not your guilt.", "It's no your fault."], "It's not your fault.", "Вина — fault; отрицание — not."),
    c("e6-workout", 6, "___", "Может, всё ещё наладится.",
      ["It might work out fine.", "It might work fine.", "It might works out fine."], "It might work out fine.", "work out — наладиться; после might — без -s."),
    c("e6-easy", 6, "___", "Это всегда непросто.",
      ["It's never easy.", "It's always not easy.", "It's never easily."], "It's never easy.", "Всегда непросто — never easy."),
    c("e6-hope", 6, "___", "Никогда не теряй надежды.",
      ["Never give up hope.", "Never give up the hope.", "Don't never give up hope."], "Never give up hope.", "hope без the; never — само отрицание, don't не нужен."),
    c("e6-know", 6, "___", "Кто знает, всякое бывает.",
      ["You never know.", "You don't never know.", "Nobody never knows."], "You never know.", "never — уже отрицание: You never know."),
    c("e6-sure", 6, "___", "Уверен, всё будет хорошо.",
      ["I'm sure it'll be fine.", "I'm sure it will fine.", "I sure it'll be fine."], "I'm sure it'll be fine.", "I'm sure — с am; будет — will be."),
    c("e6-like", 6, "___", "Прямо как когда я потерял телефон.",
      ["That's just like when I lost my phone.", "That's just as when I lost my phone.", "That's just like when I have lost my phone."],
      "That's just like when I lost my phone.", "just like when + Past Simple."),
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
