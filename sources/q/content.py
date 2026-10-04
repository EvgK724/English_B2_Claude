# Содержание приложения «Вопросы»: как построить вопрос по-английски — на примере расспроса пациента.
# do / does / did, вопросы без do, вопрос к подлежащему, предлог в конце, how long / how often / how much,
# вежливые косвенные вопросы, анамнез при инсульте, просьбы при осмотре.
# Пометка […] — форма в фокусе (оранжевый).

MIXED_TOPIC = 9

GROUPS = {
    "form": "Как построить вопрос",
    "more": "Сколько, как давно, вежливо",
    "clinic": "У постели больного",
    "mix": "Итог",
}

# Сколько, как давно: вопрос | что дальше | пример | перевод
TABLE = [
    ["How long…?", "+ have you had", "How long have you had it?", "как давно (и до сих пор)"],
    ["When…?", "+ did … start", "When did it start?", "когда (момент)"],
    ["How often…?", "+ do you", "How often do you drink?", "как часто"],
    ["How many…?", "исчисляемое", "How many tablets?", "сколько штук"],
    ["How much…?", "неисчисляемое", "How much alcohol?", "сколько (объём, вес)"],
    ["What … like?", "описать", "What's the pain like?", "какая это боль?"],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["[Who called] the ambulance?", "кто вызвал — вопрос к подлежащему, без did"], ["[Who did you call]?", "кому вы звонили — к дополнению, с did"]],
    [["[When did it start]?", "прямой вопрос"], ["Can you tell me [when it started]?", "вежливый: порядок как в утверждении"]],
    [["[How long have you had] the headache?", "как давно — Present Perfect"], ["[When did] the headache [start]?", "когда — Past Simple"]],
    [["[Is he] on any blood thinners?", "be — без do"], ["[Does he take] any blood thinners?", "обычный глагол — нужен does"]],
    [["[How many] tablets do you take?", "штук — исчисляемое"], ["[How much] alcohol do you drink?", "объём — неисчисляемое"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["Where you live?", "Where do you live?", "обычный глагол — нужен do"],
    ["When it started?", "When did it start?", "прошлое — did + глагол"],
    ["When did it started?", "When did it start?", "после did — без -ed"],
    ["Does he takes aspirin?", "Does he take aspirin?", "после does — без -s"],
    ["What did happen?", "What happened?", "вопрос к подлежащему — без did"],
    ["What means this word?", "What does this word mean?", "нужен does"],
    ["How is your name?", "What is your name?", "«как вас зовут» — what"],
    ["Can you tell me where is the pain?", "Can you tell me where the pain is?", "в косвенном вопросе — прямой порядок"],
    ["Do you know does he smoke?", "Do you know if he smokes?", "«ли» — if или whether"],
    ["How long do you have this pain?", "How long have you had this pain?", "как давно — Present Perfect"],
]

TOPICS = [
    {"n": 1, "group": "form", "title": "do, does, did", "sub": "вопрос с обычным глаголом",
     "rule": "Если в предложении обычный глагол (live, smoke, take, start), для вопроса нужен помощник: do (I, you, we, they), does (he, she, it), did (прошлое). После помощника глагол в начальной форме: Does it hurt? — не hurts; When did it start? — не started. Порядок: вопросительное слово — помощник — подлежащее — глагол.",
     "ex": [
         {"en": "Where [do] you live?", "ru": "Где вы живёте?"},
         {"en": "[Does] it hurt when you breathe?", "ru": "Больно, когда дышите?"},
         {"en": "When [did] it start?", "ru": "Когда это началось?"},
     ]},
    {"n": 2, "group": "form", "title": "be, have, can — без do", "sub": "помощник уже есть",
     "rule": "Если в предложении уже есть be (am, is, are, was), can, will, should или have в Present Perfect, do не нужен — этот глагол сам встаёт вперёд: Are you in pain? Is he taking any blood thinners? Can you lift your arm? Have you ever had a stroke? «Есть ли у вас…» — Do you have…? Здесь have — обычный глагол, поэтому с do.",
     "ex": [
         {"en": "[Are] you in pain?", "ru": "Вам больно?"},
         {"en": "[Have] you ever had a stroke?", "ru": "У вас когда-нибудь был инсульт?"},
         {"en": "[Can] you lift both arms?", "ru": "Можете поднять обе руки?"},
     ]},
    {"n": 3, "group": "form", "title": "Кто? Что случилось?", "sub": "вопрос к подлежащему — без do",
     "rule": "Если who или what — сам исполнитель действия (подлежащее), do не нужен и порядок прямой: What happened? Who called the ambulance? Which arm feels weak? Сравни: Who did you call? — «кому вы звонили»: здесь who — дополнение, поэтому нужен did.",
     "ex": [
         {"en": "What [happened]?", "ru": "Что случилось?"},
         {"en": "Who [called] the ambulance?", "ru": "Кто вызвал скорую?"},
         {"en": "Who [did you call] first?", "ru": "Кому вы позвонили первым?"},
     ]},
    {"n": 4, "group": "form", "title": "Предлог в конце", "sub": "What are you allergic to?",
     "rule": "Предлог в английском вопросе обычно уходит в конец: What are you allergic to? Who do you live with? What are you worried about? Where are you from? Опишите боль — What's the pain like? Предлог берут из сочетания: allergic to, live with, worried about. По-русски «аллергия на» — но allergic to, не on.",
     "ex": [
         {"en": "What are you allergic [to]?", "ru": "На что у вас аллергия?"},
         {"en": "Who do you live [with]?", "ru": "С кем вы живёте?"},
         {"en": "What's the pain [like]?", "ru": "Какая это боль?"},
     ]},
    {"n": 5, "group": "more", "title": "How long, how often, how much", "sub": "как давно, как часто, сколько",
     "rule": "Как давно и до сих пор — How long + Present Perfect: How long have you had this headache? Когда, в какой момент — When + Past Simple: When did it start? Как часто — How often do you…? Сколько штук — How many tablets…? Сколько вещества — How much alcohol…? Вес — How much do you weigh?",
     "ex": [
         {"en": "[How long have you had] this headache?", "ru": "Как давно у вас эта головная боль?"},
         {"en": "[How often] do you drink alcohol?", "ru": "Как часто вы пьёте алкоголь?"},
         {"en": "[How many] tablets do you take a day?", "ru": "Сколько таблеток вы принимаете в день?"},
     ]},
    {"n": 6, "group": "more", "title": "Вежливые вопросы", "sub": "Could you tell me…? Do you know if…?",
     "rule": "Вежливый вопрос начинают с Could you tell me…, Do you know…, Can you show me… — а дальше порядок как в утверждении и без do: Could you tell me when it started? — не when did it start. Вопрос «да или нет» внутри — через if или whether: Do you know if he takes aspirin? Очень вежливая просьба — Would you mind + -ing.",
     "ex": [
         {"en": "Could you tell me [when it started]?", "ru": "Не могли бы вы сказать, когда это началось?"},
         {"en": "Do you know [if] he takes aspirin?", "ru": "Вы не знаете, принимает ли он аспирин?"},
         {"en": "Would you mind [rolling up] your sleeve?", "ru": "Не могли бы вы закатать рукав?"},
     ]},
    {"n": 7, "group": "clinic", "title": "Анамнез при инсульте", "sub": "last seen well, blood thinners",
     "rule": "Главные вопросы при подозрении на инсульт: When was he last seen well? — когда его последний раз видели здоровым. What time did the symptoms begin? Did he wake up with these symptoms? Did he fall or hit his head? Has he had a stroke or TIA before? Is he on any blood thinners? What was he able to do on his own before?",
     "ex": [
         {"en": "When [was] he last seen well?", "ru": "Когда его последний раз видели здоровым?"},
         {"en": "Is he on any blood [thinners]?", "ru": "Он принимает антикоагулянты?"},
         {"en": "Did he [wake up] with these symptoms?", "ru": "Он проснулся уже с этими симптомами?"},
     ]},
    {"n": 8, "group": "clinic", "title": "Просьбы при осмотре", "sub": "Can you…? Don't… Would you mind…?",
     "rule": "При осмотре чаще всего повелительное наклонение: Close your eyes. Squeeze my fingers. Запрет — Don't + глагол: Don't move your head. Мягче — Can you… или Could you…: Could you raise both arms? Совсем вежливо — Would you mind + -ing: Would you mind lying down?",
     "ex": [
         {"en": "[Squeeze] my fingers as hard as you can.", "ru": "Сожмите мои пальцы как можно сильнее."},
         {"en": "[Don't] move your head.", "ru": "Не двигайте головой."},
         {"en": "Could you [raise] both arms?", "ru": "Поднимите, пожалуйста, обе руки."},
     ]},
    {"n": 9, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · do, does, did
    c("q1-live", 1, "Where ___ you live?", "Где вы живёте?",
      ["do", "are", "does"], "do", "Обычный глагол live — нужен do."),
    c("q1-smoke", 1, "___ you smoke?", "Вы курите?",
      ["do", "are", "have"], "do", "Обычный глагол — Do you smoke?"),
    c("q1-hurt", 1, "___ it hurt when you breathe?", "Больно, когда дышите?",
      ["does", "do", "is"], "does", "it — does: Does it hurt?"),
    c("q1-start", 1, "When ___ the symptoms start?", "Когда начались симптомы?",
      ["did", "were", "have"], "did", "Прошлое, обычный глагол — did."),
    c("q1-start-form", 1, "When did the weakness ___?", "Когда началась слабость?",
      ["start", "started", "starts"], "start", "После did — начальная форма: did … start."),
    c("q1-take", 1, "Does he ___ any medication?", "Он принимает какие-нибудь лекарства?",
      ["take", "takes", "taking"], "take", "После does — без -s: does he take."),
    c("q1-mean", 1, "What ___ this word mean?", "Что значит это слово?",
      ["does", "is", "means"], "does", "Обычный глагол mean — нужен does."),
    c("q1-sleep", 1, "How ___ you sleep last night?", "Как вы спали этой ночью?",
      ["did", "were", "do"], "did", "Прошлое — did: How did you sleep?"),

    # 2 · be, have, can — без do
    c("q2-pain", 2, "___ you in pain now?", "Вам сейчас больно?",
      ["are", "do", "have"], "are", "be само встаёт вперёд: Are you in pain?"),
    c("q2-ever", 2, "___ you ever had a stroke before?", "У вас раньше был инсульт?",
      ["have", "did", "do"], "have", "Present Perfect: Have you ever had…?"),
    c("q2-lift", 2, "___ you lift both arms for me?", "Поднимите, пожалуйста, обе руки.",
      ["can", "do", "are"], "can", "can само встаёт вперёд: Can you…?"),
    c("q2-allergic", 2, "___ you allergic to anything?", "У вас есть на что-нибудь аллергия?",
      ["are", "do", "have"], "are", "be allergic — Are you allergic…?"),
    c("q2-taking", 2, "___ he taking any blood thinners?", "Он сейчас принимает антикоагулянты?",
      ["is", "does", "has"], "is", "Present Continuous — Is he taking…?"),
    c("q2-been", 2, "Have you ___ admitted to hospital recently?", "Вас недавно госпитализировали?",
      ["been", "be", "were"], "been", "Have you been admitted…? — Present Perfect, пассив."),
    c("q2-will", 2, "___ you be able to come back tomorrow?", "Вы сможете прийти завтра?",
      ["will", "do", "are"], "will", "Будущее — Will you be able…?"),

    # 3 · Кто? Что случилось?
    c("q3-happened", 3, "What ___?", "Что случилось?",
      ["happened", "did happen", "happen"], "happened", "Вопрос к подлежащему — без did: What happened?"),
    c("q3-called", 3, "Who ___ the ambulance?", "Кто вызвал скорую?",
      ["called", "did call", "did you call"], "called", "Кто сделал — без did: Who called?"),
    c("q3-found", 3, "Who ___ him on the floor?", "Кто нашёл его на полу?",
      ["found", "did find", "finds"], "found", "Кто нашёл — без did."),
    c("q3-did", 3, "Who ___ you call first?", "Кому вы позвонили первым?",
      ["did", "do", "have"], "did", "Кому — вопрос к дополнению, нужен did."),
    c("q3-which", 3, "Which arm ___ weak?", "Какая рука слабая?",
      ["feels", "does feel", "do feel"], "feels", "Which arm — подлежащее: без does."),
    c("q3-made", 3, "What ___ you come to hospital today?", "Что заставило вас прийти в больницу сегодня?",
      ["made", "did make", "did you make"], "made", "What — подлежащее: What made you…?"),

    # 4 · Предлог в конце
    c("q4-allergic", 4, "What are you allergic ___?", "На что у вас аллергия?",
      ["to", "on", "for"], "to", "allergic to — аллергия на."),
    c("q4-live", 4, "Who do you live ___?", "С кем вы живёте?",
      ["with", "by", "at"], "with", "live with — предлог в конце."),
    c("q4-like", 4, "What's the pain ___?", "Какая это боль?",
      ["like", "as", "how"], "like", "Опишите — What is it like?"),
    c("q4-worried", 4, "What are you worried ___?", "Что вас беспокоит?",
      ["about", "of", "for"], "about", "worried about."),
    c("q4-from", 4, "Where are you ___?", "Откуда вы?",
      ["from", "of", "out"], "from", "Откуда — Where are you from?"),
    c("q4-for", 4, "What is this tablet ___?", "От чего эта таблетка?",
      ["for", "from", "against"], "for", "Для чего, от чего — What is it for?"),

    # 5 · How long, how often, how much
    c("q5-long", 5, "How long ___ you had this headache?", "Как давно у вас эта головная боль?",
      ["have", "do", "are"], "have", "Как давно и до сих пор — How long have you had…?"),
    c("q5-had", 5, "How long have you ___ diabetes?", "Сколько лет у вас диабет?",
      ["had", "have", "having"], "had", "Present Perfect: have had."),
    c("q5-when", 5, "___ did the headache start?", "Когда началась головная боль?",
      ["when", "how long", "since"], "when", "Момент — When did…?"),
    c("q5-often", 5, "How ___ do you drink alcohol?", "Как часто вы пьёте алкоголь?",
      ["often", "many", "long"], "often", "Как часто — How often?"),
    c("q5-many", 5, "How ___ tablets do you take a day?", "Сколько таблеток вы принимаете в день?",
      ["many", "much", "often"], "many", "Таблетки исчисляемые — How many?"),
    c("q5-much", 5, "How ___ do you weigh?", "Сколько вы весите?",
      ["much", "many", "long"], "much", "Вес — How much do you weigh?"),
    c("q5-far", 5, "How ___ can you walk without stopping?", "Какое расстояние вы можете пройти без остановки?",
      ["far", "much", "many"], "far", "Расстояние — How far?"),

    # 6 · Вежливые вопросы
    c("q6-order", 6, "Could you tell me when ___?", "Не могли бы вы сказать, когда это началось?",
      ["it started", "did it start", "it did start"], "it started", "Косвенный вопрос — порядок как в утверждении, без did."),
    c("q6-where", 6, "Can you show me where ___?", "Покажите, пожалуйста, где болит.",
      ["it hurts", "does it hurt", "hurts it"], "it hurts", "Прямой порядок: where it hurts."),
    c("q6-if", 6, "Do you know ___ he takes aspirin?", "Вы не знаете, принимает ли он аспирин?",
      ["if", "does", "that"], "if", "«Ли» в косвенном вопросе — if или whether."),
    c("q6-time", 6, "Do you remember what time ___?", "Вы помните, во сколько это случилось?",
      ["it happened", "did it happen", "happened it"], "it happened", "Прямой порядок: what time it happened."),
    c("q6-is", 6, "Could you tell me where the toilet ___?", "Подскажите, где туалет?",
      ["is", "is it", "does"], "is", "Прямой порядок: where the toilet is."),
    c("q6-whether", 6, "I'd like to know ___ he has had a stroke before.", "Хотелось бы узнать, был ли у него раньше инсульт.",
      ["whether", "has", "that"], "whether", "«Ли» — whether или if."),
    c("q6-mind", 6, "Would you mind ___ your sleeve?", "Не могли бы вы закатать рукав?",
      ["rolling up", "to roll up", "roll up"], "rolling up", "Would you mind + -ing."),

    # 7 · Анамнез при инсульте
    c("q7-seen", 7, "When ___ he last seen well?", "Когда его последний раз видели здоровым?",
      ["was", "did", "has"], "was", "Пассив в прошлом: When was he last seen well?"),
    c("q7-fall", 7, "___ he fall or hit his head?", "Он падал, ударялся головой?",
      ["did", "was", "has"], "did", "Прошлое, обычный глагол — did."),
    c("q7-thinners", 7, "Is he on any blood ___?", "Он принимает антикоагулянты?",
      ["thinners", "thins", "thinner"], "thinners", "Разговорное название антикоагулянтов — blood thinners."),
    c("q7-before", 7, "Has he ___ a stroke or TIA before?", "У него раньше были инсульт или ТИА?",
      ["had", "have", "having"], "had", "Present Perfect: has he had."),
    c("q7-woke", 7, "Did he wake ___ with these symptoms?", "Он проснулся уже с этими симптомами?",
      ["up", "on", "out"], "up", "Проснуться — wake up."),
    c("q7-seizure", 7, "___ he have a seizure?", "У него были судороги?",
      ["did", "was", "has"], "did", "Прошлое, обычный глагол have — did."),
    c("q7-time", 7, "What time ___ the symptoms begin?", "Во сколько начались симптомы?",
      ["did", "were", "have"], "did", "Прошлое — did … begin."),
    c("q7-able", 7, "What was he able to ___ on his own before?", "Что он раньше мог делать сам?",
      ["do", "doing", "does"], "do", "be able to + глагол: able to do."),

    # 8 · Просьбы при осмотре
    c("q8-dont", 8, "___ move your head — just your eyes.", "Не двигайте головой — только глазами.",
      ["don't", "not", "no"], "don't", "Запрет — Don't + глагол."),
    c("q8-close", 8, "Close your eyes and ___ let me open them.", "Закройте глаза и не давайте мне их открыть.",
      ["don't", "not", "no"], "don't", "Запрет — don't let."),
    c("q8-could", 8, "___ you raise both arms and hold them there?", "Поднимите обе руки и удерживайте их.",
      ["could", "do", "are"], "could", "Мягкая просьба — Could you…?"),
    c("q8-mind", 8, "Would you mind ___ on the bed?", "Не могли бы вы лечь на кушетку?",
      ["lying down", "to lie down", "lie down"], "lying down", "Would you mind + -ing."),
    c("q8-touch", 8, "Touch your nose, then ___ my finger.", "Коснитесь своего носа, потом моего пальца.",
      ["touch", "touching", "to touch"], "touch", "Повелительное наклонение — просто глагол."),
    c("q8-squeeze", 8, "___ my fingers as hard as you can.", "Сожмите мои пальцы как можно сильнее.",
      ["squeeze", "push", "pull"], "squeeze", "Сжать — squeeze."),
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
