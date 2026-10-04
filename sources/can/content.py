# Содержание приложения «can / could / be able to».
# Пометка […] — форма; цвет: can — оранжевый, could — синий, be able to и managed to — зелёный, прочие подчёркнуты.

MIXED_TOPIC = 8

GROUPS = {
    "can": "Умею и могу: can, could",
    "able": "Удалось и другие формы: be able to",
    "more": "Просьбы и возможность",
    "med": "В больнице",
    "mix": "Итог",
}

# Главная таблица: ситуация | форма | пример
TABLE = [
    ["Умею, могу сейчас; можно", "can", "I can swim."],
    ["Умел в прошлом вообще", "could", "I could read at four."],
    ["Смог, удалось один раз", "was able to", "We were able to save him."],
    ["Не смог — в любом случае", "couldn't", "I couldn't sleep."],
    ["Будущее и другие формы", "will be able to", "You'll be able to walk."],
    ["Вежливая просьба", "could", "Could you help me?"],
    ["Возможно, как вариант", "could", "It could be a migraine."],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["I [could] swim when I was five.", "умел вообще"], ["I [was able to] swim to the shore.", "в тот раз удалось доплыть"],
     ["I [couldn't] swim to the shore.", "не смог — можно и wasn't able to"]],
    [["[Can] you help me?", "просто, по-дружески"], ["[Could] you help me?", "вежливее"], ["I'll [be able to] help you tomorrow.", "смогу завтра"]],
    [["Stress [can] cause headaches.", "бывает, вообще"], ["This headache [could] be serious.", "возможно, в этом случае"],
     ["It [can't] be serious — the scan is normal.", "не может быть"]],
    [["You [could] call him.", "можешь позвонить — как вариант"], ["You [could have] called me!", "мог бы и позвонить — упрёк"]],
    [["I [can] read without glasses.", "могу сейчас"], ["I [haven't been able to] read since the stroke.", "не могу с тех пор"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["I can to swim.", "I can swim.", "после can — без to"],
    ["She cans speak English.", "She can speak English.", "can не меняется: she can"],
    ["Do you can help me?", "Can you help me?", "вопрос — Can you…? без do"],
    ["I will can help you.", "I will be able to help you.", "будущее — will be able to"],
    ["I haven't could sleep.", "I haven't been able to sleep.", "Present Perfect — been able to"],
    ["I'd like to can drive.", "I'd like to be able to drive.", "после to — be able to"],
    ["Everyone could escape from the fire.", "Everyone was able to escape from the fire.", "удалось один раз — was able to"],
    ["I am able speak English.", "I am able to speak English.", "be able + to"],
    ["Could I use your phone? — Yes, you could.", "Could I use your phone? — Yes, of course.", "на просьбу — Yes, of course"],
    ["You could call me yesterday!", "You could have called me yesterday!", "мог бы, но не — could have + 3-я форма"],
]

TOPICS = [
    {"n": 1, "group": "can", "title": "can — умею, могу", "sub": "сейчас · можно · бывает",
     "rule": "can — умею или могу сейчас: I can swim. I can see you on Monday. Разрешение: You can park here. Can I come in? Общая возможность, «бывает»: A stroke can happen at any age. После can — глагол без to; can не меняется: she can. Вопрос — Can you…? без do. Отрицание — can't или cannot.",
     "ex": [
         {"en": "My son [can] swim.", "ru": "Мой сын умеет плавать."},
         {"en": "You [can] park here.", "ru": "Здесь можно парковаться."},
         {"en": "A stroke [can] happen at any age.", "ru": "Инсульт может случиться в любом возрасте."},
     ]},
    {"n": 2, "group": "can", "title": "could — умел в прошлом", "sub": "вообще, как навык",
     "rule": "could — умел, мог в прошлом вообще, как навык: I could read when I was four. Не мог — couldn't: I couldn't sleep last night. Но об одной удаче в прошлом («смог, удалось») could не говорят — нужно was able to или managed to.",
     "ex": [
         {"en": "I [could] read when I was four.", "ru": "Я умел читать в четыре года."},
         {"en": "I [couldn't] sleep last night.", "ru": "Ночью я не мог уснуть."},
         {"en": "He [couldn't] walk after the stroke.", "ru": "После инсульта он не мог ходить."},
     ]},
    {"n": 3, "group": "able", "title": "was able to — удалось", "sub": "одна удача в прошлом",
     "rule": "Одна конкретная удача в прошлом — «смог, удалось» — was able to или managed to: The fire spread quickly, but everyone was able to escape. We managed to restore blood flow. Could здесь звучит неправильно. В отрицании годятся оба: I couldn't / wasn't able to open the door.",
     "ex": [
         {"en": "Everyone [was able to] escape.", "ru": "Всем удалось выбраться."},
         {"en": "We [managed to] restore blood flow.", "ru": "Нам удалось восстановить кровоток."},
         {"en": "I [couldn't] open the door.", "ru": "Я не смог открыть дверь."},
     ]},
    {"n": 4, "group": "able", "title": "be able to — все формы", "sub": "will be able · have been able",
     "rule": "У can только две формы: can и could. Всё остальное — через be able to. Будущее — will be able to. Present Perfect — have been able to. После другого модального — might be able to, should be able to. После to и -ing — to be able to, being able to. Will can и have could — ошибки.",
     "ex": [
         {"en": "You'll [be able to] walk again.", "ru": "Вы снова сможете ходить."},
         {"en": "I haven't [been able to] sleep.", "ru": "Я не могу нормально спать (уже давно)."},
         {"en": "I'd like to [be able to] read papers without a dictionary.", "ru": "Хочу уметь читать статьи без словаря."},
     ]},
    {"n": 5, "group": "more", "title": "Could you…? Can I…?", "sub": "просьбы и разрешение",
     "rule": "Просьба: Can you…? — просто, по-дружески; Could you…? — вежливее. Разрешение: Can I…? — просто; Could I…? — вежливее; May I…? — официально. Ответ: Yes, of course или Sure. Yes, you could — ошибка.",
     "ex": [
         {"en": "[Could] you help me with this form?", "ru": "Не могли бы вы помочь мне с этим бланком?"},
         {"en": "[Can] I come in?", "ru": "Можно войти?"},
         {"en": "[May] I ask you a few questions?", "ru": "Позвольте задать вам несколько вопросов?"},
     ]},
    {"n": 6, "group": "more", "title": "could = возможно; could have", "sub": "вариант · «мог бы, но не…»",
     "rule": "could — ещё и «возможно, может оказаться»: This headache could be serious. Как вариант: We could try another drug. can — «бывает вообще»: Stress can cause headaches. could have + третья форма — «мог бы, но не случилось»: It could have been worse. You could have called me! — упрёк. Не может быть — can't be.",
     "ex": [
         {"en": "This headache [could] be serious.", "ru": "Эта головная боль может оказаться серьёзной."},
         {"en": "We [could] try another drug.", "ru": "Можно попробовать другой препарат."},
         {"en": "It [could have] been worse.", "ru": "Могло быть и хуже."},
     ]},
    {"n": 7, "group": "med", "title": "В больнице", "sub": "осмотр · прогноз · результат",
     "rule": "На осмотре: Can you feel this? Can you move your fingers? Could you roll up your sleeve? Прогноз: You'll be able to go home on Friday. She should be able to walk with a stick. Результат: We were able to remove the clot. Что было до болезни: Before the stroke, he could speak three languages.",
     "ex": [
         {"en": "[Can] you feel this?", "ru": "Вы это чувствуете?"},
         {"en": "You'll [be able to] go home on Friday.", "ru": "В пятницу сможете поехать домой."},
         {"en": "We [were able to] remove the clot.", "ru": "Нам удалось удалить тромб."},
     ]},
    {"n": 8, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · can
    c("k1-swim", 1, "My son is only five, but he ___ swim.", "Сыну всего пять, а он уже умеет плавать.", ["can", "is able", "could"], "can",
      "Умеет сейчас — can."),
    c("k1-speak", 1, "I can ___ Spanish quite well.", "Я неплохо говорю по-испански.", ["speak", "to speak", "speaking"], "speak", "После can — глагол без to."),
    c("k1-park", 1, "You ___ park here — it's free after six.", "Здесь можно парковаться — после шести бесплатно.", ["can", "are able", "can to"], "can",
      "Разрешение, «можно» — can."),
    c("k1-stroke", 1, "A stroke ___ happen at any age.", "Инсульт может случиться в любом возрасте.", ["can", "is able to"], "can",
      "«Бывает, вообще» — can. Be able to — об умениях людей."),
    c("k1-hear", 1, "Sorry, I ___ hear you — the line is bad.", "Простите, я вас не слышу — плохая связь.", ["can't", "am not able", "don't can"], "can't",
      "Не могу сейчас — can't."),

    # 2 · could — умел в прошлом
    c("k2-read", 2, "I ___ read when I was four.", "Я умел читать в четыре года.", ["could", "can", "was able"], "could", "Умел в прошлом вообще — could."),
    c("k2-sleep", 2, "I ___ sleep last night — the neighbours were so noisy.", "Ночью я не мог уснуть — соседи очень шумели.", ["couldn't", "can't", "wasn't able"], "couldn't",
      "Не мог в прошлом — couldn't."),
    c("k2-young", 2, "When she was young, she ___ run ten kilometres easily.", "В молодости она легко пробегала десять километров.", ["could", "can", "is able to"], "could",
      "Умела в прошлом — could."),
    c("k2-walk", 2, "He ___ walk after the stroke, but now he can.", "После инсульта он не мог ходить, а теперь может.", ["couldn't", "can't", "won't be able to"], "couldn't",
      "Не мог тогда — couldn't; может сейчас — can."),

    # 3 · was able to — удалось
    c("k3-escape", 3, "The fire spread quickly, but everyone ___ escape.", "Пожар распространялся быстро, но всем удалось выбраться.", ["was able to", "could", "can"], "was able to",
      "Удалось один раз — was able to. Could — только «умел вообще»."),
    c("k3-restore", 3, "Thanks to fast thrombolysis, we ___ restore blood flow.", "Благодаря быстрому тромболизису нам удалось восстановить кровоток.",
      ["were able to", "could", "can"], "were able to", "Конкретная удача в прошлом — were able to."),
    c("k3-managed", 3, "It was difficult, but I ___ to finish the report on time.", "Было трудно, но мне удалось закончить отчёт вовремя.", ["managed", "could", "was able"], "managed",
      "«Удалось, справился» — managed to."),
    c("k3-door", 3, "I ___ open the door — the key didn't fit.", "Я не смог открыть дверь — ключ не подошёл.", ["couldn't", "can't", "didn't able to"], "couldn't",
      "Не смог — couldn't (или wasn't able to)."),
    c("k3-family", 3, "After three attempts, I ___ contact his family.", "С третьей попытки мне удалось связаться с его родственниками.", ["was able to", "could", "am able to"], "was able to",
      "Удалось в тот раз — was able to."),

    # 4 · be able to — все формы
    c("k4-will", 4, "After the course, you'll ___ speak confidently.", "После курса вы сможете говорить уверенно.", ["be able to", "can", "could"], "be able to",
      "Будущее — will be able to. Will can — ошибка."),
    c("k4-perfect", 4, "I haven't ___ sleep well since the operation.", "С самой операции я не могу нормально спать.", ["been able to", "could", "can"], "been able to",
      "Present Perfect — have been able to."),
    c("k4-might", 4, "We might ___ discharge him tomorrow.", "Возможно, завтра мы сможем его выписать.", ["be able to", "can", "could"], "be able to",
      "После might — be able to."),
    c("k4-like", 4, "I'd like to ___ read scientific papers without a dictionary.", "Хочу уметь читать научные статьи без словаря.", ["be able to", "can", "could"], "be able to",
      "После to — be able to."),
    c("k4-being", 4, "I love ___ work from home on Fridays.", "Мне нравится, что по пятницам можно работать из дома.", ["being able to", "can", "could"], "being able to",
      "После love — -ing: being able to."),
    c("k4-should", 4, "With physiotherapy, she should ___ walk again.", "С помощью реабилитации она должна снова начать ходить.", ["be able to", "can", "could"], "be able to",
      "После should — be able to."),

    # 5 · просьбы и разрешение
    c("k5-help", 5, "___ you help me with this form, please?", "Не могли бы вы помочь мне с этим бланком?", ["Could", "Are", "Do"], "Could", "Вежливая просьба — Could you…?"),
    c("k5-course", 5, "Could I use your phone? — Yes, of ___.", "Можно воспользоваться вашим телефоном? — Да, конечно.", ["course", "could", "can"], "course",
      "Ответ на просьбу — Yes, of course. Yes, you could — ошибка."),
    c("k5-come", 5, "___ I come in?", "Можно войти?", ["Can", "Am", "Do"], "Can", "Разрешение — Can I…?"),
    c("k5-may", 5, "___ I ask you a few questions about your symptoms?", "Позвольте задать вам несколько вопросов о симптомах?", ["May", "Am", "Do"], "May",
      "Официальная просьба о разрешении — May I…?"),

    # 6 · could = возможно; could have
    c("k6-headache", 6, "This headache ___ be a sign of high blood pressure.", "Эта головная боль может быть признаком высокого давления.", ["could", "can to", "is able to"], "could",
      "Возможно в этом случае — could."),
    c("k6-try", 6, "If this doesn't work, we ___ try a different drug.", "Если не поможет, можно попробовать другой препарат.", ["could", "can to", "were able to"], "could",
      "Предложить вариант — could."),
    c("k6-worse", 6, "It ___ have been much worse — luckily, he was wearing a helmet.", "Всё могло быть гораздо хуже — к счастью, он был в шлеме.",
      ["could", "can", "was able to"], "could", "Могло быть, но не случилось — could have + третья форма."),
    c("k6-called", 6, "You ___ have called me — I was waiting all evening!", "Мог бы и позвонить — я весь вечер ждал!", ["could", "can", "were able to"], "could",
      "Упрёк «мог бы» — could have + третья форма."),
    c("k6-anna", 6, "That ___ be Anna — she's in Moscow this week.", "Это не может быть Анна — она на этой неделе в Москве.", ["can't", "isn't able to", "mustn't"], "can't",
      "«Не может быть» — can't."),

    # 7 · в больнице
    c("k7-feel", 7, "___ you feel this? — Yes, but it's weaker on the left.", "Вы это чувствуете? — Да, но слева слабее.", ["Can", "Are"], "Can",
      "На осмотре — Can you feel this?"),
    c("k7-home", 7, "If all goes well, you'll ___ go home on Friday.", "Если всё пойдёт хорошо, в пятницу сможете поехать домой.", ["be able to", "can", "could"], "be able to",
      "Будущее — will be able to."),
    c("k7-clot", 7, "The surgeons ___ remove the clot completely.", "Хирургам удалось полностью удалить тромб.", ["were able to", "could", "can"], "were able to",
      "Конкретная удача — were able to."),
    c("k7-sleeve", 7, "___ you roll up your sleeve, please?", "Закатайте, пожалуйста, рукав.", ["Could", "Are", "Do"], "Could", "Вежливая просьба — Could you…?"),
    c("k7-languages", 7, "Before the stroke, he ___ speak three languages.", "До инсульта он говорил на трёх языках.", ["could", "can", "is able to"], "could",
      "Умел в прошлом вообще — could."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
    for alt in k.get("also", {}): assert alt in k["opts"] and alt != k["a"], k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
