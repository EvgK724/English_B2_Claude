# Содержание приложения «make / do»: make или do, «сделать» без них, спорт — play, go, do.
# Пометка […] — глагол; цвет по глаголу: make и go — синий, do — оранжевый, play — зелёный, прочие подчёркнуты.

MIXED_TOPIC = 10

GROUPS = {
    "md": "Make или do",
    "sport": "Спорт: play, go или do",
    "mix": "Итог",
}

# Левая колонка: одна и та же тема — make или do
GRID = [
    ("Еда", "make a cake", "do the cooking"),
    ("Дом", "make the bed", "do the washing\u00a0up"),
    ("Работа", "make a plan", "do the work"),
    ("Учёба", "make progress", "do homework"),
    ("Больница", "make a diagnosis", "do a blood test"),
    ("Люди", "make friends", "do a favour"),
]
# Спорт: play | go | do
SPORT = [("football", "swimming", "yoga"), ("tennis", "running", "karate"), ("chess", "skiing", "exercises")]

# Правая колонка: сочетание | перевод | пример (озвучка: сочетание + пример)
ALWAYS_MAKE = [
    ["make a decision", "принять решение", "We need to make a decision today."],
    ["make a mistake", "ошибиться", "Everyone makes mistakes."],
    ["make a phone call", "позвонить", "I need to make a phone call."],
    ["make an appointment", "записаться на приём", "I'd like to make an appointment."],
    ["make progress", "делать успехи", "She's making good progress."],
    ["make an effort", "постараться", "Please make an effort to walk every day."],
    ["make sure", "убедиться, проследить", "Make sure he takes his tablets."],
    ["make friends", "заводить друзей", "He makes friends easily."],
    ["make money", "зарабатывать", "He makes good money."],
    ["make a difference", "иметь значение, менять к лучшему", "Every minute makes a difference."],
    ["make the bed", "застелить кровать", "I make the bed every morning."],
    ["make a noise", "шуметь", "Please don't make a noise."],
]
ALWAYS_DO = [
    ["do homework", "делать домашнее задание", "Have you done your homework?"],
    ["do the shopping", "ходить за покупками", "I do the shopping on Saturdays."],
    ["do the washing up", "мыть посуду", "Who's doing the washing up?"],
    ["do the cleaning", "убираться", "We do the cleaning at the weekend."],
    ["do a good job", "хорошо справиться", "You did a good job!"],
    ["do your best", "стараться изо всех сил", "We'll do our best."],
    ["do someone a favour", "оказать услугу", "Could you do me a favour?"],
    ["do research", "проводить исследования", "She does research on stroke."],
    ["do a course", "проходить курс", "I'm doing an English course."],
    ["do harm / good", "вредить / приносить пользу", "It may do more harm than good."],
    ["do exercise", "заниматься физкультурой", "Try to do some exercise every day."],
    ["do nothing", "ничего не делать", "We can't just do nothing."],
]
NEITHER = [
    ["take a photo", "сделать фото", "Can I take a photo?"],
    ["take a deep breath", "сделать глубокий вдох", "Take a deep breath and hold it."],
    ["take a few steps", "сделать несколько шагов", "Can you take a few steps for me?"],
    ["take a break", "сделать перерыв", "Let's take a short break."],
    ["give an injection", "сделать укол", "The nurse will give you an injection."],
    ["draw a conclusion", "сделать вывод", "It's too early to draw conclusions."],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["I made my homework.", "I did my homework.", "домашнее задание — do"],
    ["I did a mistake.", "I made a mistake.", "ошибка — make"],
    ["We must do a decision.", "We must make a decision.", "решение — make"],
    ["Can you make me a favour?", "Can you do me a favour?", "одолжение — do"],
    ["I make exercises every day.", "I do exercises every day.", "упражнения — do"],
    ["I make sport.", "I do sport.", "заниматься спортом — do sport"],
    ["I play yoga.", "I do yoga.", "йога — do"],
    ["I go to swimming.", "I go swimming.", "go + -ing, без to"],
    ["Can I make a photo?", "Can I take a photo?", "фото — take"],
    ["The nurse made him an injection.", "The nurse gave him an injection.", "укол — give"],
]

TOPICS = [
    {"n": 1, "group": "md", "title": "make — создаём", "sub": "еда, вещи, документы, планы",
     "rule": "make — когда создаёшь то, чего раньше не было: еду, напиток, вещь, документ, план. make a cake, make coffee, make a list, make a copy, make a plan. Звук тоже создаёшь: make a noise.",
     "ex": [
         {"en": "She [made] a cake for my birthday.", "ru": "Она испекла торт мне на день рождения."},
         {"en": "Let's [make] a list of his medications.", "ru": "Давай составим список его лекарств."},
         {"en": "Could you [make] a copy of this ECG?", "ru": "Сделайте, пожалуйста, копию этой ЭКГ."},
     ]},
    {"n": 2, "group": "md", "title": "make — решения, ошибки, звонки", "sub": "сочетания, которые надо запомнить",
     "rule": "Эти сочетания проще запомнить, чем объяснить, — в них всегда make: make a decision, make a mistake, make a phone call, make an appointment, make progress, make an effort, make sure, make friends, make money, make a difference, make the bed.",
     "ex": [
         {"en": "Everyone [makes] mistakes.", "ru": "Все ошибаются."},
         {"en": "We have to [make] a decision now.", "ru": "Нам нужно принять решение прямо сейчас."},
         {"en": "I'd like to [make] an appointment.", "ru": "Я хотел бы записаться на приём."},
     ]},
    {"n": 3, "group": "md", "title": "do — работа, учёба, дом", "sub": "действие, обязанность",
     "rule": "do — действие, работа, обязанность; нового предмета не появляется. Работа и учёба: do the work, do a good job, do homework, do a course. Дела по дому: do the shopping, do the washing up, do the cleaning. Исключение: make the bed.",
     "ex": [
         {"en": "Have you [done] your homework?", "ru": "Ты сделал домашнее задание?"},
         {"en": "I [do] the shopping on Saturdays.", "ru": "По субботам я хожу за покупками."},
         {"en": "I have a lot of work to [do].", "ru": "У меня много работы."},
     ]},
    {"n": 4, "group": "md", "title": "do — «делать» вообще", "sub": "something, nothing, your best",
     "rule": "Если не говоришь, что именно делаешь, — всегда do: What are you doing? What do you do? — «Кем работаешь?», do something, do nothing. Ещё: do your best, do someone a favour, do research, do harm, do good.",
     "ex": [
         {"en": "What do you [do]? — I'm a neurologist.", "ru": "Кем вы работаете? — Я невролог."},
         {"en": "We'll [do] our best.", "ru": "Мы сделаем всё возможное."},
         {"en": "Could you [do] me a favour?", "ru": "Можешь оказать мне услугу?"},
     ]},
    {"n": 5, "group": "md", "title": "make или do в больнице", "sub": "диагноз · анализ · смена",
     "rule": "Решение, вывод, результат — make: make a diagnosis, make a full recovery, make a complaint. Процедура, анализ, работа — do: do a blood test, do an ECG, do night shifts, do CPR.",
     "ex": [
         {"en": "It's too early to [make] a diagnosis.", "ru": "Ставить диагноз пока рано."},
         {"en": "We need to [do] a blood test.", "ru": "Нужно сделать анализ крови."},
         {"en": "She [made] a full recovery.", "ru": "Она полностью восстановилась."},
     ]},
    {"n": 6, "group": "md", "title": "«Сделать» — не make и не do", "sub": "take · give · draw",
     "rule": "Русское «сделать» — не всегда make или do. take: take a photo, take a deep breath, take a few steps, take a break. give: give an injection — сделать укол. draw: draw a conclusion — сделать вывод.",
     "ex": [
         {"en": "[Take] a deep breath.", "ru": "Сделайте глубокий вдох."},
         {"en": "Can I [take] a photo?", "ru": "Можно сфотографировать?"},
         {"en": "The nurse will [give] you an injection.", "ru": "Медсестра сделает вам укол."},
     ]},
    {"n": 7, "group": "sport", "title": "play — мяч и игры", "sub": "football · tennis · chess",
     "rule": "play — игры с мячом и игры, где соревнуешься с кем-то: play football, play tennis, play volleyball, play hockey, play chess, play cards. Без the: play football. С the — музыка: play the guitar.",
     "ex": [
         {"en": "My son [plays] football.", "ru": "Мой сын играет в футбол."},
         {"en": "Do you [play] tennis?", "ru": "Ты играешь в теннис?"},
         {"en": "Let's [play] chess.", "ru": "Давай сыграем в шахматы."},
     ]},
    {"n": 8, "group": "sport", "title": "go + -ing", "sub": "swimming · running · skiing",
     "rule": "go + занятие на -ing: go swimming, go running, go skiing, go cycling, go fishing. Без to: go swimming, а не go to swimming. Место — с to: go to the gym, go to the pool.",
     "ex": [
         {"en": "I [go] swimming twice a week.", "ru": "Я хожу плавать два раза в неделю."},
         {"en": "She [goes] running every morning.", "ru": "Она бегает каждое утро."},
         {"en": "I [go] to the gym on Mondays.", "ru": "По понедельникам я хожу в спортзал."},
     ]},
    {"n": 9, "group": "sport", "title": "do — йога, борьба, упражнения", "sub": "без мяча и не на -ing",
     "rule": "do — всё остальное: без мяча и не на -ing. do yoga, do Pilates, do karate, do judo, do gymnastics, do athletics, do exercises. Заниматься спортом вообще — do sport: Do you do any sport? (В американском — play sports.)",
     "ex": [
         {"en": "She [does] yoga every evening.", "ru": "Она каждый вечер занимается йогой."},
         {"en": "He [did] karate as a teenager.", "ru": "Подростком он занимался карате."},
         {"en": "[Do] these exercises twice a day.", "ru": "Делайте эти упражнения дважды в день."},
     ]},
    {"n": 10, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · make — создаём
    c("mk-cake", 1, "My daughter ___ a cake for my birthday.", "Дочь испекла торт мне на день рождения.", ["made", "did"], "made",
      "Приготовить, создать — make: make a cake, make coffee."),
    c("mk-coffee", 1, "Sit down, I'll ___ some coffee.", "Садись, я сварю кофе.", ["make", "do"], "make", "Напитки и еду готовят — make."),
    c("mk-list", 1, "Let's ___ a list of his medications.", "Давай составим список его лекарств.", ["make", "do"], "make",
      "Составить список — make a list: появляется новый документ."),
    c("mk-copy", 1, "Could you ___ a copy of this ECG?", "Сделайте, пожалуйста, копию этой ЭКГ.", ["make", "do"], "make",
      "Сделать копию — make a copy: появляется новый лист."),
    c("mk-plan", 1, "We need to ___ a plan for his discharge.", "Нужно составить план его выписки.", ["make", "do"], "make", "Составить план — make a plan."),
    c("mk-noise", 1, "Please don't ___ a noise — the patients are sleeping.", "Пожалуйста, не шумите — пациенты спят.", ["make", "do"], "make",
      "Шуметь — make a noise: звук тоже создаёшь."),

    # 2 · make — решения, ошибки, звонки
    c("mc-mistake", 2, "Don't worry — everyone ___ mistakes.", "Не переживай — все ошибаются.", ["makes", "does"], "makes", "Ошибка — make a mistake."),
    c("mc-decision", 2, "We have to ___ a decision about thrombolysis now.", "Нам нужно прямо сейчас принять решение о тромболизисе.", ["make", "do"], "make",
      "Решение — make a decision."),
    c("mc-call", 2, "Excuse me, I need to ___ a phone call.", "Извините, мне нужно позвонить.", ["make", "do"], "make", "Позвонить — make a phone call."),
    c("mc-appointment", 2, "I'd like to ___ an appointment with a neurologist.", "Я хотел бы записаться на приём к неврологу.", ["make", "do"], "make",
      "Записаться на приём — make an appointment."),
    c("mc-progress", 2, "She's ___ good progress with her speech.", "Она делает хорошие успехи в восстановлении речи.", ["making", "doing"], "making",
      "Успехи — make progress."),
    c("mc-sure", 2, "___ sure he takes his tablets every day.", "Проследите, чтобы он каждый день принимал таблетки.", ["Make", "Do"], "Make",
      "Убедиться, проследить — make sure."),
    c("mc-difference", 2, "In stroke, every minute ___ a difference.", "При инсульте каждая минута имеет значение.", ["makes", "does"], "makes",
      "Иметь значение, менять к лучшему — make a difference."),
    c("mc-bed", 2, "The nurse ___ the bed and opened the window.", "Медсестра застелила кровать и открыла окно.", ["made", "did"], "made",
      "Застелить кровать — make the bed. Это исключение: запомнить."),

    # 3 · do — работа, учёба, дом
    c("dw-homework", 3, "Have you ___ your homework?", "Ты сделал домашнее задание?", ["done", "made"], "done", "Домашнее задание — do homework."),
    c("dw-shopping", 3, "I usually ___ the shopping on Saturdays.", "Обычно я хожу за покупками по субботам.", ["do", "make"], "do",
      "Дела по дому — do: do the shopping, do the cleaning."),
    c("dw-washing", 3, "Who's going to ___ the washing up?", "Кто будет мыть посуду?", ["do", "make"], "do", "Мыть посуду — do the washing up."),
    c("dw-cleaning", 3, "We ___ the cleaning at the weekend.", "Мы убираемся по выходным.", ["do", "make"], "do", "Убираться — do the cleaning."),
    c("dw-course", 3, "I'm ___ an online English course.", "Я прохожу онлайн-курс английского.", ["doing", "making"], "doing", "Проходить курс — do a course."),
    c("dw-job", 3, "You ___ a great job with that patient.", "Вы отлично справились с этим пациентом.", ["did", "made"], "did",
      "Справиться с работой — do a good job."),
    c("dw-work", 3, "I have a lot of work to ___ today.", "Сегодня у меня много работы.", ["do", "make"], "do", "Работа — do: do the work."),

    # 4 · do — «делать» вообще
    c("dg-living", 4, "What do you ___ for a living? — I'm a neurologist.", "Кем вы работаете? — Я невролог.", ["do", "make"], "do",
      "Чем занимаешься, кем работаешь — do: What do you do?"),
    c("dg-nothing", 4, "We can't just ___ nothing.", "Мы не можем просто ничего не делать.", ["do", "make"], "do",
      "do nothing, do something, do anything — всегда do."),
    c("dg-best", 4, "Don't worry, we'll ___ our best.", "Не волнуйтесь, мы сделаем всё возможное.", ["do", "make"], "do", "Стараться изо всех сил — do your best."),
    c("dg-favour", 4, "Could you ___ me a favour?", "Можешь оказать мне услугу?", ["do", "make"], "do", "Одолжение — do someone a favour."),
    c("dg-harm", 4, "This drug can ___ more harm than good.", "Этот препарат может навредить больше, чем помочь.", ["do", "make"], "do",
      "Вред и польза — do harm, do good."),
    c("dg-research", 4, "She ___ research on stroke rehabilitation.", "Она занимается исследованиями по реабилитации после инсульта.", ["does", "makes"], "does",
      "Исследования — do research."),

    # 5 · make или do в больнице
    c("hs-diagnosis", 5, "It's too early to ___ a diagnosis.", "Ставить диагноз пока рано.", ["make", "do"], "make", "Поставить диагноз — make a diagnosis."),
    c("hs-blood", 5, "We need to ___ a blood test.", "Нужно сделать анализ крови.", ["do", "make"], "do", "Анализ, процедура — do: do a blood test."),
    c("hs-ecg", 5, "Can you ___ an ECG before he goes to CT?", "Сделаете ЭКГ, пока он не ушёл на КТ?", ["do", "make"], "do", "Процедура — do an ECG."),
    c("hs-recovery", 5, "She ___ a full recovery after the stroke.", "После инсульта она полностью восстановилась.", ["made", "did"], "made",
      "Полностью восстановиться — make a full recovery."),
    c("hs-complaint", 5, "The patient's son ___ a complaint about the waiting time.", "Сын пациента пожаловался на долгое ожидание.", ["made", "did"], "made",
      "Жалоба — make a complaint."),
    c("hs-shifts", 5, "I ___ three night shifts a week.", "Я работаю три ночные смены в неделю.", ["do", "make"], "do", "Смены, дежурства — do: do night shifts."),
    c("hs-cpr", 5, "They ___ CPR for twenty minutes.", "Реанимацию проводили двадцать минут.", ["did", "made"], "did", "Процедура — do CPR."),

    # 6 · «сделать» — не make и не do
    c("tk-breath", 6, "___ a deep breath and hold it.", "Сделайте глубокий вдох и задержите дыхание.", ["Take", "Make", "Do"], "Take",
      "Сделать вдох — take a breath."),
    c("tk-steps", 6, "Can you ___ a few steps for me?", "Пройдите, пожалуйста, несколько шагов.", ["take", "make", "do"], "take", "Сделать шаг — take a step."),
    c("tk-photo", 6, "Can I ___ a photo of the rash?", "Можно я сфотографирую сыпь?", ["take", "make", "do"], "take", "Сделать фото — take a photo."),
    c("tk-break", 6, "Let's ___ a short break.", "Давай сделаем небольшой перерыв.", ["take", "make", "do"], "take", "Сделать перерыв — take a break."),
    c("tk-injection", 6, "The nurse will ___ you an injection.", "Медсестра сделает вам укол.", ["give", "make", "do"], "give",
      "Сделать укол — give an injection."),

    # 7 · play — мяч и игры
    c("pl-football", 7, "My son ___ football on Saturdays.", "Мой сын по субботам играет в футбол.", ["plays", "goes", "does"], "plays", "Мяч — play: play football."),
    c("pl-tennis", 7, "Do you ___ tennis?", "Ты играешь в теннис?", ["play", "go", "do"], "play", "Игры с мячом — play: play tennis."),
    c("pl-chess", 7, "My grandfather taught me to ___ chess.", "Дедушка научил меня играть в шахматы.", ["play", "do", "go"], "play",
      "Игры, где соревнуешься, — play: play chess, play cards."),
    c("pl-hockey", 7, "They ___ hockey every winter.", "Каждую зиму они играют в хоккей.", ["play", "go", "do"], "play", "Командная игра — play: play hockey."),
    c("pl-volleyball", 7, "We ___ volleyball on the beach.", "Мы играли в волейбол на пляже.", ["played", "went", "did"], "played", "Мяч — play: play volleyball."),

    # 8 · go + -ing
    c("go-swim", 8, "I ___ swimming twice a week.", "Я хожу плавать два раза в неделю.", ["go", "play", "do"], "go", "Занятие на -ing — go: go swimming."),
    c("go-ski", 8, "Every February we ___ skiing in the Urals.", "Каждый февраль мы катаемся на лыжах на Урале.", ["go", "do", "play"], "go",
      "Занятие на -ing — go: go skiing."),
    c("go-run", 8, "She ___ running every morning before work.", "Каждое утро перед работой она бегает.", ["goes", "does", "plays"], "goes",
      "Занятие на -ing — go: go running."),
    c("go-cycling", 8, "Let's ___ cycling on Sunday.", "Давай в воскресенье покатаемся на велосипеде.", ["go", "do", "play"], "go", "Занятие на -ing — go: go cycling."),
    c("go-noto", 8, "On Fridays I go ___.", "По пятницам я хожу плавать.", ["swimming", "to swimming"], "swimming",
      "go + -ing без to: go swimming. To — только перед местом: go to the pool."),
    c("go-gym", 8, "I ___ the gym three times a week.", "Я хожу в спортзал три раза в неделю.", ["go to", "go", "do"], "go to",
      "Место — go to: go to the gym, go to the pool."),

    # 9 · do — йога, борьба, упражнения
    c("ds-yoga", 9, "She ___ yoga every evening.", "Она каждый вечер занимается йогой.", ["does", "plays", "goes"], "does", "Йога, пилатес — do: do yoga."),
    c("ds-karate", 9, "He ___ karate when he was a teenager.", "Подростком он занимался карате.", ["did", "played", "went"], "did",
      "Единоборства — do: do karate, do judo."),
    c("ds-exercise", 9, "Patients should ___ these exercises twice a day.", "Пациентам нужно выполнять эти упражнения дважды в день.", ["do", "make", "play"], "do",
      "Упражнения — do exercises. Make exercises — ошибка."),
    c("ds-sport", 9, "Do you ___ any sport?", "Ты занимаешься спортом?", ["do", "make", "go"], "do", "Заниматься спортом — do sport. Make sport — ошибка."),
    c("ds-gym", 9, "She ___ gymnastics at school.", "В школе она занималась гимнастикой.", ["did", "played", "went"], "did", "Гимнастика, лёгкая атлетика — do."),
]

for k in CARDS:
    assert k["a"] in k["opts"] and len(set(k["opts"])) == len(k["opts"]) and k["q"].count("___") == 1, k["id"]
assert len({k["id"] for k in CARDS}) == len(CARDS)
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()),
          "answers:", Counter(k["a"].lower().split()[0] for k in CARDS).most_common())
