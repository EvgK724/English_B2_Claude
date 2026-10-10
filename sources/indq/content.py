# Содержание тренажёра «Косвенные вопросы» — вопрос внутри предложения: Could you tell me where the lab is?
# Прямой порядок слов, без do, does, did; be, can, have — после подлежащего; if и whether; вопрос к подлежащему;
# I wonder и знак вопроса; пересказ; косвенный вопрос в научном тексте.
# Отличие от «Вопросов» (q, тема «Вежливые вопросы») и «Пересказа» (rep, тема «Вопросы в пересказе»): там по 7 карточек
# на основу, здесь — вся конструкция с ловушками B1+ и B2.
# Разметка в примерах: [слово|a] — вопросительное слово, if, whether (оранжевый); [слова|b] — подлежащее и глагол
# в прямом порядке (синий); [слова] — прямой вопрос для сравнения (подчёркнуто).
# Темы с полем late вступают в общую тренировку позже.

MIXED_TOPIC = 10

GROUPS = {
    "b1": "B1 — прямой порядок",
    "b1p": "B1+ — модальные, подлежащее, начала",
    "b2": "B2 — пересказ, статьи, whether",
    "mix": "Итог",
}

# Главная таблица: прямой вопрос | что меняется («главное — пояснение») | косвенный
TABLE = [
    ["Where is the lab?", "be — в конец, после подлежащего", "… where the lab is"],
    ["When did it start?", "do, does, did исчезают — время переходит в глагол", "… when it started"],
    ["Does he smoke?", "«да или нет» — if или whether", "… if he smokes"],
    ["Where can I park?", "can, should, have — после подлежащего", "… where I can park"],
    ["Who called?", "вопрос к подлежащему — порядок не меняется", "… who called"],
]

# Одна ситуация — разный порядок: строки [английский, перевод]
CONTRAST = [
    [["[Where is the lab]?", "прямой вопрос"],
     ["Could you tell me [where|a] [the lab is|b]?", "косвенный — be в конце"]],
    [["[When did it start]?", "прямой — с did"],
     ["Do you remember [when|a] [it started|b]?", "косвенный — без did, время в глаголе"]],
    [["[Does he smoke]?", "прямой"],
     ["Do you know [if|a] [he smokes|b]?", "косвенный — if, и -s возвращается"]],
    [["Do you know [who|a] [his consultant is|b]?", "who — не подлежащее: is в конце"],
     ["Do you know [who|a] [is on call|b]?", "who — подлежащее: порядок не меняется"]],
    [["Do you know [where|a] [he is|b]?", "начало — вопрос, в конце ?"],
     ["I wonder [where|a] [he is|b].", "начало — утверждение, в конце точка"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["Could you tell me where is the lab?", "Could you tell me where the lab is?", "be — после подлежащего"],
    ["Do you know when did it start?", "Do you know when it started?", "did исчезает, время — в глаголе"],
    ["Do you know does he smoke?", "Do you know if he smokes?", "«ли» — if или whether"],
    ["Can you tell me what does he take?", "Can you tell me what he takes?", "does исчезает, -s остаётся"],
    ["Do you know where can I park?", "Do you know where I can park?", "can — после подлежащего"],
    ["Can you tell me what did happen?", "Can you tell me what happened?", "вопрос к подлежащему — без did"],
    ["I wonder where is he?", "I wonder where he is.", "I wonder — прямой порядок и точка"],
    ["I asked her where did she live.", "I asked her where she lived.", "в пересказе — тоже прямой порядок"],
    ["It depends on if he agrees.", "It depends on whether he agrees.", "после предлога — whether"],
    ["I don't know what do I tell him.", "I don't know what to tell him.", "что сказать — what to"],
]

TOPICS = [
    {"n": 1, "group": "b1", "title": "where the lab is", "sub": "be уходит в конец",
     "rule": "Когда вопрос стоит внутри другого предложения (Could you tell me…, Do you know…, I'm not sure…), он перестаёт быть вопросом: порядок как в утверждении. Сначала подлежащее, потом is или are: Where is the lab? → Could you tell me where the lab is? What time is it? → Do you know what time it is? Сказать where is the lab после Could you tell me — самая частая ошибка русскоговорящих.",
     "ex": [
         {"en": "Could you tell me [where|a] [the lab is|b]?", "ru": "Подскажите, где лаборатория?"},
         {"en": "Do you know [what time|a] [it is|b]?", "ru": "Вы не знаете, который час?"},
         {"en": "Can you remind me [what|a] [the new resident's name is|b]?", "ru": "Напомните, как зовут нового ординатора?"},
     ]},
    {"n": 2, "group": "b1", "title": "when it started", "sub": "do, does, did исчезают",
     "rule": "do, does, did в косвенном вопросе не нужны — время переходит в глагол. did it start → it started; does he take → he takes (окончание -s возвращается); do you smoke → you smoke. When did it start? → Do you remember when it started? What does he take? → Do you know what he takes? Did и does, оставленные внутри, сразу выдают иностранца.",
     "ex": [
         {"en": "Do you remember [when|a] [it started|b]?", "ru": "Вы помните, когда это началось?"},
         {"en": "Do you know [what|a] [he takes|b] for his blood pressure?", "ru": "Вы знаете, что он принимает от давления?"},
         {"en": "Can you describe [how|a] [you fell|b]?", "ru": "Опишите, как вы упали."},
     ]},
    {"n": 3, "group": "b1", "title": "if и whether", "sub": "вопрос «да или нет» внутри",
     "rule": "Если в прямом вопросе нет вопросительного слова (Does he smoke? Is she allergic?), внутри ставят if или whether — это русское «ли»: Do you know if he smokes? Could you check whether she is allergic? Порядок прямой, do и does исчезают. Будущее после if в таком вопросе остаётся: Do you know if he will come? — здесь if значит «ли», а не «если».",
     "ex": [
         {"en": "Do you know [if|a] [he smokes|b]?", "ru": "Вы не знаете, курит ли он?"},
         {"en": "Could you check [whether|a] [she is|b] allergic to penicillin?", "ru": "Проверьте, нет ли у неё аллергии на пенициллин."},
         {"en": "Do you know [if|a] [he will come|b] tomorrow?", "ru": "Не знаете, придёт ли он завтра?"},
     ]},
    {"n": 4, "group": "b1p", "title": "where I can park", "sub": "can, should, have — после подлежащего", "late": 0.2,
     "rule": "can, could, should, will и have в Present Perfect в прямом вопросе стоят перед подлежащим, а в косвенном — после него. Where can I park? → Could you tell me where I can park? How long have you had it? → Can you tell me how long you have had it? What should I do? → I'm not sure what I should do. Глагол остаётся в той же форме, меняется только порядок.",
     "ex": [
         {"en": "Could you tell me [where|a] [I can park|b]?", "ru": "Подскажите, где можно припарковаться?"},
         {"en": "Can you tell me [how long|a] [you have had|b] this headache?", "ru": "Сколько времени у вас эта головная боль?"},
         {"en": "I'm not sure [what|a] [I should do|b] next.", "ru": "Не знаю, что мне делать дальше."},
     ]},
    {"n": 5, "group": "b1p", "title": "who called, what happened", "sub": "вопрос к подлежащему не меняется", "late": 0.2,
     "rule": "Если who, what или which — само подлежащее (кто вызвал? что случилось?), порядок и так прямой, и в косвенном вопросе ничего не меняется: Who called? → Do you know who called? What happened? → Can you tell me what happened? Did сюда не добавляют. Сравните: Who is on call? (кто дежурит — who подлежащее) → who is on call; Who is his consultant? (кто его врач — подлежащее consultant) → who his consultant is.",
     "ex": [
         {"en": "Can you tell me [what|a] [happened|b]?", "ru": "Расскажите, что случилось."},
         {"en": "Do you know [who|a] [is on call|b] tonight?", "ru": "Не знаете, кто сегодня дежурит?"},
         {"en": "Do you know [who|a] [his consultant is|b]?", "ru": "Не знаете, кто его лечащий врач?"},
     ]},
    {"n": 6, "group": "b1p", "title": "I wonder, I'm not sure", "sub": "начала и знак вопроса", "late": 0.25,
     "rule": "Косвенный вопрос начинают по-разному: Could you tell me, Do you know, Have you got any idea, I wonder, I'm not sure, I'd like to know, I don't know. Знак вопроса ставят, только если вопрос — всё предложение: Do you know where he is? Если начало — утверждение, в конце точка: I wonder where he is. «Не знаю, что делать, куда идти» — what to do, where to go: вопросительное слово + to.",
     "ex": [
         {"en": "I wonder [where|a] [he is|b].", "ru": "Интересно, где он."},
         {"en": "Have you got any idea [how much|a] [it costs|b]?", "ru": "Не представляете, сколько это стоит?"},
         {"en": "I don't know [what|a] [to tell him|b].", "ru": "Не знаю, что ему сказать."},
     ]},
    {"n": 7, "group": "b2", "title": "asked where she lived", "sub": "косвенный вопрос в пересказе", "late": 0.45,
     "rule": "В пересказе после asked и wanted to know — тот же прямой порядок, плюс сдвиг времени: Where do you live? → I asked her where she lived. When can I go home? → He asked when he could go home. Is the scan normal? → She wanted to know whether the scan was normal. Что случилось раньше — Past Perfect: What happened? → The police asked what had happened.",
     "ex": [
         {"en": "The patient asked [when|a] [he could go|b] home.", "ru": "Пациент спросил, когда сможет поехать домой."},
         {"en": "She wanted to know [whether|a] [the scan was|b] normal.", "ru": "Она хотела знать, нормальный ли снимок."},
         {"en": "The police asked [what|a] [had happened|b].", "ru": "Полиция спросила, что произошло."},
     ]},
    {"n": 8, "group": "b2", "title": "It remains unclear whether…", "sub": "косвенный вопрос в статье", "late": 0.5,
     "rule": "В научном тексте косвенный вопрос бывает подлежащим или дополнением: It remains unclear whether thrombolysis benefits these patients. Where the clot is determines the treatment. What he told us changed the diagnosis. We do not fully understand why some patients recover faster. The question is how quickly we can transfer him. Порядок везде прямой.",
     "ex": [
         {"en": "It remains unclear [whether|a] [thrombolysis benefits|b] these patients.", "ru": "Остаётся неясным, помогает ли этим пациентам тромболизис."},
         {"en": "[Where|a] [the clot is|b] determines the treatment.", "ru": "От того, где тромб, зависит лечение."},
         {"en": "We do not fully understand [why|a] [some patients recover|b] faster.", "ru": "Мы не до конца понимаем, почему одни пациенты восстанавливаются быстрее."},
     ]},
    {"n": 9, "group": "b2", "title": "whether или if", "sub": "когда только whether", "late": 0.55,
     "rule": "В разговоре «ли» чаще передают через if. Но только whether ставят: после предлога (It depends on whether he agrees), перед to + глагол (We need to decide whether to operate), в начале предложения (Whether he will recover is unclear) и в паре whether or not. А «если» в условии — только if: If he comes, call me.",
     "ex": [
         {"en": "It depends on [whether|a] [he agrees|b].", "ru": "Зависит от того, согласится ли он."},
         {"en": "We need to decide [whether|a] [to operate|b].", "ru": "Нужно решить, оперировать ли."},
         {"en": "[Whether|a] [he will recover|b] fully is still unclear.", "ru": "Восстановится ли он полностью, пока неясно."},
     ]},
    {"n": 10, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None, say=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    if say: d["say"] = say
    return d

CARDS = [
    # 1 · be в конец
    c("d1-lab", 1, "Could you tell me ___?", "Подскажите, где лаборатория?",
      ["where the lab is", "where is the lab", "where does the lab"], "where the lab is", "Косвенный вопрос — прямой порядок: подлежащее, потом is."),
    c("d1-time", 1, "Do you know ___?", "Вы не знаете, который час?",
      ["what time it is", "what time is it", "what time it"], "what time it is", "Прямой порядок: what time it is."),
    c("d1-name", 1, "Can you remind me ___?", "Напомните, как зовут нового ординатора?",
      ["what the new resident's name is", "what is the new resident's name", "what does the new resident's name"], "what the new resident's name is",
      "Подлежащее — the new resident's name, is — после него."),
    c("d1-bp", 1, "Could you tell me ___ now?", "Какое у него сейчас давление?",
      ["what his blood pressure is", "what is his blood pressure", "what his blood pressure"], "what his blood pressure is", "Прямой порядок, is в конце: what his blood pressure is."),
    c("d1-letter", 1, "I'm not sure ___.", "Не знаю, где его выписка.",
      ["where his discharge letter is", "where is his discharge letter", "where his discharge letter"], "where his discharge letter is", "После I'm not sure — прямой порядок: where his discharge letter is."),
    c("d1-problem", 1, "Can you explain ___?", "Объясните, в чём проблема?",
      ["what the problem is", "what is the problem", "what problem is"], "what the problem is",
      "Надёжно — what the problem is. С is и коротким словом в разговоре слышно и what is the problem, но учите прямой порядок."),

    # 2 · do, does, did исчезают
    c("d2-cigs", 2, "Can you tell me ___?", "Скажите, сколько сигарет вы выкуриваете в день?",
      ["how many cigarettes you smoke a day", "how many cigarettes do you smoke a day", "how many cigarettes you do smoke a day"],
      "how many cigarettes you smoke a day", "do исчезает: how many cigarettes you smoke."),
    c("d2-takes", 2, "Do you know ___?", "Вы знаете, что он принимает?",
      ["what he takes", "what does he take", "what he take"], "what he takes", "does исчезает, а -s переходит на глагол: what he takes."),
    c("d2-works", 2, "Could you tell me ___?", "Подскажите, где работает ваша дочь?",
      ["where your daughter works", "where does your daughter work", "where your daughter work"], "where your daughter works", "does исчезает, -s на глаголе: where your daughter works."),
    c("d2-fell", 2, "Can you describe ___?", "Опишите, как вы упали.",
      ["how you fell", "how did you fall", "how you did fall"], "how you fell", "did исчезает, глагол в прошедшем: how you fell."),
    c("d2-bed", 2, "I'd like to know ___ last night.", "Хотелось бы знать, во сколько вы легли спать вчера.",
      ["what time you went to bed", "what time did you go to bed", "what time you go to bed"], "what time you went to bed", "Прошедшее переходит в глагол: you went."),
    c("d2-means", 2, "Could you explain ___?", "Объясните, что значит этот результат.",
      ["what this result means", "what does this result mean", "what this result mean"], "what this result means", "does исчезает, -s на глаголе: means."),

    # 3 · if и whether
    c("d3-smokes", 3, "Do you know ___?", "Вы не знаете, курит ли он?",
      ["if he smokes", "does he smoke", "he smokes"], "if he smokes", "Вопрос «да или нет» внутри — if или whether + прямой порядок."),
    c("d3-allergic", 3, "Could you check ___ allergic to penicillin?", "Проверьте, нет ли у неё аллергии на пенициллин.",
      ["whether she is", "is she", "whether is she"], "whether she is", "«Ли» — whether или if, порядок прямой: whether she is."),
    c("d3-fell", 3, "Can you remember ___?", "Вы помните, падали ли вы?",
      ["if you fell", "did you fall", "if did you fall"], "if you fell", "if + прямой порядок, did исчезает: if you fell."),
    c("d3-ask", 3, "Ask the nurse ___ the scan is ready.", "Спросите медсестру, готов ли снимок.",
      ["if", "that", "is"], "if", "«Ли» — if (или whether)."),
    c("d3-ever", 3, "The doctor wants to know ___ a stroke before.", "Врач хочет знать, был ли у вас раньше инсульт.",
      ["if you have ever had", "have you ever had", "if have you ever had"], "if you have ever had", "if + подлежащее + have: if you have ever had."),
    c("d3-will", 3, "Do you know ___?", "Не знаете, придёт ли он завтра?",
      ["if he will come tomorrow", "will he come tomorrow", "if he comes tomorrow"], "if he will come tomorrow",
      "Здесь if значит «ли», поэтому будущее остаётся: if he will come. Без will — только в условии: If he comes, call me."),

    # 4 · can, should, have
    c("d4-park", 4, "Could you tell me ___?", "Подскажите, где можно припарковаться?",
      ["where I can park", "where can I park", "where I park can"], "where I can park", "can — после подлежащего: where I can park."),
    c("d4-should", 4, "I'm not sure ___ next.", "Не знаю, что мне делать дальше.",
      ["what I should do", "what should I do", "what I do should"], "what I should do", "should — после подлежащего: what I should do."),
    c("d4-long", 4, "Can you tell me ___ this headache?", "Сколько времени у вас эта головная боль?",
      ["how long you have had", "how long have you had", "how long you had have"], "how long you have had", "have — после подлежащего: how long you have had."),
    c("d4-been", 4, "Do you know ___ waiting?", "Не знаете, сколько он уже ждёт?",
      ["how long he has been", "how long has he been", "how long he been"], "how long he has been", "has — после подлежащего: how long he has been waiting."),
    c("d4-appt", 4, "Could you tell me ___ get an appointment?", "Подскажите, когда я смогу записаться на приём?",
      ["when I can", "when can I", "when I do can"], "when I can", "can — после подлежащего: when I can get."),
    c("d4-results", 4, "Do you know ___ the results?", "Не знаете, когда будут результаты?",
      ["when we will get", "when will we get", "when we get will"], "when we will get", "will — после подлежащего: when we will get."),

    # 5 · вопрос к подлежащему
    c("d5-happened", 5, "Can you tell me ___?", "Расскажите, что случилось.",
      ["what happened", "what did happen", "what it happened"], "what happened", "what — подлежащее (что случилось?): порядок не меняется, did не нужен."),
    c("d5-called", 5, "Do you know ___ the ambulance?", "Не знаете, кто вызвал скорую?",
      ["who called", "who did call", "who did he call"], "who called", "who — подлежащее (кто вызвал?): who called."),
    c("d5-oncall", 5, "Do you know ___ tonight?", "Не знаете, кто сегодня дежурит?",
      ["who is on call", "who on call is", "who does on call"], "who is on call", "who — подлежащее (кто дежурит?): порядок не меняется — who is on call."),
    c("d5-consultant", 5, "Do you know ___?", "Не знаете, кто его лечащий врач?",
      ["who his consultant is", "who does his consultant", "who his consultant"], "who his consultant is",
      "Подлежащее — his consultant, is после него. В разговоре услышите и who is his consultant — с be так тоже говорят, но надёжнее прямой порядок."),
    c("d5-caused", 5, "We still don't know ___ the bleed.", "Мы до сих пор не знаем, что вызвало кровоизлияние.",
      ["what caused", "what did cause", "what it caused"], "what caused", "what — подлежащее (что вызвало?): what caused."),
    c("d5-which", 5, "Could you tell me ___ best?", "Подскажите, какое лечение помогает лучше всего?",
      ["which treatment works", "which treatment does work", "which does treatment work"], "which treatment works", "which treatment — подлежащее: which treatment works."),

    # 6 · начала и знак
    c("d6-wonder", 6, "I wonder ___", "Интересно, где он.",
      ["where he is.", "where is he?", "where he is?"], "where he is.", "I wonder — утверждение: прямой порядок и точка."),
    c("d6-idea", 6, "Have you got any idea ___?", "Не представляете, сколько это стоит?",
      ["how much it costs", "how much does it cost", "how much it does cost"], "how much it costs", "Прямой порядок, does исчезает: how much it costs."),
    c("d6-mark", 6, "Do you know where he is___", "Вы не знаете, где он?",
      ["?", "."], "?", "Начало — вопрос (Do you know…), значит в конце знак вопроса."),
    c("d6-dose", 6, "I'm not sure ___.", "Не уверен, какую дозу он принимает.",
      ["what dose he takes", "what dose does he take", "what dose he take"], "what dose he takes", "Прямой порядок, -s на глаголе: what dose he takes."),
    c("d6-transfer", 6, "I'd like to know ___.", "Хотел бы знать, почему его не перевели раньше.",
      ["why he wasn't transferred earlier", "why wasn't he transferred earlier", "why he not was transferred earlier"],
      "why he wasn't transferred earlier", "Прямой порядок и в пассиве: why he wasn't transferred."),
    c("d6-to", 6, "I don't know ___.", "Не знаю, что ему сказать.",
      ["what to tell him", "what tell him", "what do I tell him"], "what to tell him", "«Что сказать, куда идти» — вопросительное слово + to: what to tell him."),

    # 7 · в пересказе
    c("d7-home", 7, "The patient asked when ___ home.", "Пациент спросил, когда сможет поехать домой.",
      ["he could go", "could he go", "he can going"], "he could go", "Пересказ: прямой порядок и сдвиг — can → could: when he could go."),
    c("d7-normal", 7, "She wanted to know ___ normal.", "Она хотела знать, нормальный ли снимок.",
      ["whether the scan was", "was the scan", "whether was the scan"], "whether the scan was", "«Ли» — whether, порядок прямой, is → was."),
    c("d7-lived", 7, "I asked her ___.", "Я спросил, где она живёт.",
      ["where she lived", "where did she live", "where she did live"], "where she lived", "Прямой порядок, did исчезает, время сдвигается: where she lived."),
    c("d7-taking", 7, "The GP asked ___ any other medication.", "Терапевт спросил, принимает ли он другие препараты.",
      ["if he was taking", "was he taking", "if was he taking"], "if he was taking", "if + прямой порядок: if he was taking."),
    c("d7-police", 7, "The police asked me ___.", "Полиция спросила меня, что произошло.",
      ["what had happened", "what had it happened", "what did happen"], "what had happened", "what — подлежащее; что случилось раньше — Past Perfect: what had happened."),
    c("d7-waited", 7, "His wife asked why ___ so long.", "Жена спросила, почему так долго ждали.",
      ["they had waited", "had they waited", "did they wait"], "they had waited", "Прямой порядок и Past Perfect: why they had waited."),

    # 8 · в научном тексте
    c("d8-unclear", 8, "It remains unclear ___ thrombolysis benefits these patients.", "Остаётся неясным, помогает ли этим пациентам тромболизис.",
      ["whether", "that", "does"], "whether", "«Ли» в научном тексте — whether."),
    c("d8-what", 8, "___ he told us changed the diagnosis.", "То, что он рассказал, изменило диагноз.",
      ["What", "That what", "Which"], "What", "What he told us — «то, что он рассказал»: подлежащее предложения."),
    c("d8-where", 8, "___ the clot is determines the treatment.", "От того, где тромб, зависит лечение.",
      ["Where", "Where is", "Where does"], "Where", "Where the clot is — подлежащее; порядок прямой."),
    c("d8-why", 8, "We do not fully understand ___ some patients recover faster.", "Мы не до конца понимаем, почему одни пациенты восстанавливаются быстрее.",
      ["why", "why do", "why are"], "why", "Прямой порядок без do: why some patients recover."),
    c("d8-question", 8, "The question is how ___.", "Вопрос в том, как быстро мы сможем его перевести.",
      ["quickly we can transfer him", "quickly can we transfer him", "quickly we transfer can him"], "quickly we can transfer him", "После The question is — прямой порядок: how quickly we can."),
    c("d8-how", 8, "This study looks at ___ stroke care has changed.", "В исследовании рассматривается, как изменилась помощь при инсульте.",
      ["how", "how has", "how did"], "how", "Прямой порядок: how stroke care has changed."),

    # 9 · whether или if
    c("d9-depends", 9, "It depends on ___ he agrees.", "Зависит от того, согласится ли он.",
      ["whether", "if", "that"], "whether", "После предлога — только whether: depends on whether."),
    c("d9-decide", 9, "We need to decide ___ to operate.", "Нужно решить, оперировать ли.",
      ["whether", "if", "that"], "whether", "Перед to + глагол — только whether: whether to operate."),
    c("d9-ornot", 9, "Let me know ___ or not you can come.", "Дайте знать, сможете ли вы прийти.",
      ["whether", "if", "that"], "whether", "whether or not — устойчивая пара. If or not подряд не ставят."),
    c("d9-start", 9, "___ he will recover fully is still unclear.", "Восстановится ли он полностью, пока неясно.",
      ["Whether", "If", "That"], "Whether", "В начале предложения «ли» — только whether."),
    c("d9-ask", 9, "Ask him ___ he has any allergies.", "Спросите, есть ли у него аллергия.",
      ["if", "that", "does"], "if", "В разговоре — чаще if; whether тоже верно."),
    c("d9-cond", 9, "___ he comes, call me.", "Если он придёт, позвоните мне.",
      ["If", "Whether", "Does"], "If", "«Если» в условии — только if. Whether — «ли»."),
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
