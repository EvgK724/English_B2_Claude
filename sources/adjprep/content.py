# Содержание приложения «Прилагательное + предлог».
# В примерах: {…} — прилагательное (синий), […] — предлог (оранжевый).

MIXED_TOPIC = 13

# Смысл предлогов: предлог | вопрос | подсказка | прилагательные | примечание
PREPS = [
    {"p": "about", "q": "о чём?", "hint": "ситуация, тема, факт",
     "adj": ["confused", "depressed", "excited", "embarrassed", "disappointed", "pleased", "annoyed", "worried"]},
    {"p": "at", "q": "на что?", "hint": "реакция на новость, вид, событие",
     "adj": ["amazed", "shocked", "surprised", "embarrassed", "annoyed", "pleased", "excited"],
     "note": "с amazed, shocked, surprised можно и by"},
    {"p": "at", "q": "в чём?", "hint": "умение",
     "adj": ["good", "bad"], "note": "но good with patients — умеет обращаться, good for you — полезно"},
    {"p": "by", "q": "чем вызвано?", "hint": "причина, как в пассиве",
     "adj": ["amazed", "shocked", "surprised", "disappointed", "bored", "confused"]},
    {"p": "with", "q": "кем, чем?", "hint": "оцениваю человека или результат",
     "adj": ["satisfied", "pleased", "happy", "disappointed", "bored", "annoyed"],
     "note": "annoyed with — на человека"},
    {"p": "in", "q": "в ком, в чём?", "hint": "интерес, разочарование в человеке",
     "adj": ["interested", "disappointed"]},
    {"p": "on", "q": "на чём?", "hint": "увлечён", "adj": ["keen"]},
    {"p": "of", "q": "чего?", "hint": "страх и «надоело»",
     "adj": ["terrified", "afraid", "scared", "tired", "bored"],
     "note": "tired of — надоело; bored of — разговорное"},
    {"p": "from", "q": "от чего?", "hint": "устал физически или умственно", "adj": ["tired"]},
    {"p": "over", "q": "из-за чего?", "hint": "потеря, затяжная беда", "adj": ["depressed"]},
]

# Одно прилагательное — разные предлоги: предлог | когда | пример ([…] — предлог)
MULTI = [
    {"adj": "disappointed", "rows": [
        ["in", "в человеке", "disappointed [in] you"],
        ["with", "результатом, вещью", "disappointed [with] the results"],
        ["about", "ситуацией, фактом", "disappointed [about] not getting the job"],
        ["by", "чем вызвано", "disappointed [by] the decision"]]},
    {"adj": "tired", "rows": [
        ["of", "надоело", "tired [of] waiting"],
        ["from", "устал физически", "tired [from] the night shift"]]},
    {"adj": "pleased", "rows": [
        ["with", "доволен человеком, результатом", "pleased [with] your progress"],
        ["about · at", "рад новости, событию", "pleased [about] the news"]]},
    {"adj": "excited", "rows": [
        ["about", "предвкушаю событие", "excited [about] the trip"],
        ["at", "перспектива, мысль", "excited [at] the prospect of…"]]},
    {"adj": "embarrassed", "rows": [
        ["about", "стыдно за что-то", "embarrassed [about] my accent"],
        ["at", "неловко в моменте", "embarrassed [at] being late"],
        ["by", "кто или что смутило", "embarrassed [by] his questions"]]},
    {"adj": "amazed · shocked · surprised", "rows": [
        ["at = by", "почти без разницы", "shocked [at] / [by] the news"]]},
    {"adj": "bored", "rows": [
        ["with", "нейтрально", "bored [with] the job"],
        ["of", "разговорно", "bored [of] the film"],
        ["by", "что нагнало скуку", "bored [by] the lecture"]]},
    {"adj": "annoyed", "rows": [
        ["with", "на человека", "annoyed [with] him"],
        ["at · about", "на ситуацию", "annoyed [about] the delay"]]},
    {"adj": "depressed", "rows": [
        ["about", "о ситуации", "depressed [about] his health"],
        ["over", "о потере, беде", "depressed [over] losing his job"]]},
]

# Частые ошибки русскоговорящих: неверно | верно | почему
ERRORS = [
    ["annoyed on him", "annoyed with him", "«злюсь на» — не on"],
    ["interested about", "interested in", "только in"],
    ["good in English", "good at English", "«хорош в» — не in"],
    ["tired from waiting", "tired of waiting", "если «надоело»"],
    ["shocked with the news", "shocked at / by the news", "«удивлён чем» — не with"],
]

TOPICS = [
    {"n": 1, "title": "about — о чём",
     "rule": "about отвечает на вопрос «о чём?»: ситуация, тема, факт, из-за которого переживаешь. Так говорят с confused, depressed, excited, embarrassed, disappointed, pleased, annoyed — и ещё worried, nervous, upset. После about глагол идёт с -ing: embarrassed about being late.",
     "ex": [
         {"en": "The patient is {confused} [about] the new dose.", "ru": "Пациент путается в новой дозировке."},
         {"en": "We're all {excited} [about] the new CT scanner.", "ru": "Мы все ждём не дождёмся нового КТ."},
         {"en": "He's {embarrassed} [about] his speech.", "ru": "Он стесняется своей речи."},
     ]},
    {"n": 2, "title": "at — на что: реакция",
     "rule": "at — мгновенная реакция на то, что увидел, услышал или узнал: «на что?» Так говорят amazed, shocked, surprised, annoyed, pleased, embarrassed. Часто дальше the news, the sight, how или what: amazed at how quickly he recovered. С amazed, shocked и surprised можно и by.",
     "ex": [
         {"en": "I was {amazed} [at] how quickly he recovered.", "ru": "Я поразился, как быстро он поправился."},
         {"en": "Everyone was {shocked} [at] the news.", "ru": "Все были потрясены новостью."},
         {"en": "She was {annoyed} [at] the delay.", "ru": "Её раздражала задержка."},
     ]},
    {"n": 3, "title": "at — в чём: умение",
     "rule": "at — «в чём силён или слаб?»: good at, bad at, brilliant at, hopeless at. Дальше существительное или -ing: good at explaining. Не путай: good with — умеет обращаться (good with patients, with her hands), good for — полезно (walking is good for you). И никогда не good in.",
     "ex": [
         {"en": "She's really {good} [at] explaining things.", "ru": "Она очень хорошо объясняет."},
         {"en": "I'm {bad} [at] remembering names.", "ru": "Я плохо запоминаю имена."},
         {"en": "He's {good} [with] elderly patients.", "ru": "Он умеет находить подход к пожилым пациентам."},
     ]},
    {"n": 4, "title": "by — чем вызвано",
     "rule": "by — причина, как в пассиве: «что вызвало чувство?» The results amazed us → we were amazed by the results. Так говорят amazed, shocked, surprised, disappointed, bored, confused. Проверка: можно перевернуть — «это меня поразило»? Значит, by.",
     "ex": [
         {"en": "We were {amazed} [by] the results of the trial.", "ru": "Результаты исследования нас поразили."},
         {"en": "The students were {bored} [by] the lecture.", "ru": "Лекция нагнала на студентов скуку."},
     ]},
    {"n": 5, "title": "with — кем, чем: оценка",
     "rule": "with — когда оцениваешь человека или результат: «кем, чем доволен?» Так говорят satisfied, pleased, happy, disappointed, bored. На человека раздражаются тоже с with: annoyed with him — не on him. Но удивление — не with: amazed at или by.",
     "ex": [
         {"en": "Are you {satisfied} [with] your care?", "ru": "Вы довольны тем, как вас лечат?"},
         {"en": "The doctor is {pleased} [with] your progress.", "ru": "Врач доволен вашими успехами."},
         {"en": "Don't be {annoyed} [with] him — he's new.", "ru": "Не злись на него — он новенький."},
     ]},
    {"n": 6, "title": "in и on",
     "rule": "in — interested in: по-русски «интересуюсь чем-то» без предлога, по-английски только in. И disappointed in — разочаровался в человеке. on — keen on: очень увлечён. После обоих — существительное или -ing: interested in joining, keen on running.",
     "ex": [
         {"en": "Are you {interested} [in] joining the study?", "ru": "Хотите участвовать в исследовании?"},
         {"en": "I'm really {disappointed} [in] you.", "ru": "Я в тебе очень разочарован."},
         {"en": "He's very {keen} [on] running.", "ru": "Он очень увлекается бегом."},
     ]},
    {"n": 7, "title": "of — страх и «надоело»",
     "rule": "of — «чего?»: страх и «надоело». terrified, afraid, scared, frightened of; tired of — надоело; bored of — разговорный вариант bored with. После of глагол идёт с -ing: tired of waiting.",
     "ex": [
         {"en": "She's {terrified} [of] needles.", "ru": "Она панически боится игл."},
         {"en": "I'm {tired} [of] waiting for the results.", "ru": "Мне надоело ждать результатов."},
         {"en": "The kids got {bored} [of] the film.", "ru": "Детям надоел фильм."},
     ]},
    {"n": 8, "title": "tired of или tired from",
     "rule": "tired of — надоело, это эмоция: I'm tired of waiting. tired from — устал физически или умственно: tired from the night shift. Проверка: подходит «надоело» — of; «вымотался от» — from.",
     "ex": [
         {"en": "I'm {tired} [of] his excuses.", "ru": "Мне надоели его отговорки."},
         {"en": "I'm {tired} [from] the night shift.", "ru": "Я устал после ночной смены."},
     ]},
    {"n": 9, "title": "disappointed: in, with, about, by",
     "rule": "disappointed берёт четыре предлога. in — в человеке: I'm disappointed in you. with — результатом, вещью: with the results. about — ситуацией, фактом: about not getting the job. by — чем вызвано: by the decision. С человеком годится и with, с событием — и at.",
     "ex": [
         {"en": "Her parents were {disappointed} [in] her.", "ru": "Родители в ней разочаровались."},
         {"en": "We were {disappointed} [with] the results.", "ru": "Результаты нас не устроили."},
         {"en": "She's {disappointed} [about] not getting the job.", "ru": "Она расстроена, что не получила эту работу."},
         {"en": "I was {disappointed} [by] his reaction.", "ru": "Его реакция меня разочаровала."},
     ]},
    {"n": 10, "title": "amazed, shocked: at = by",
     "rule": "amazed, shocked и surprised берут и at, и by — разница минимальная. by — причина, как в пассиве: the news shocked me → shocked by the news. at — реакция, особенно с how и what: amazed at how fast he walked again. Главное — не with и не of.",
     "ex": [
         {"en": "I was {shocked} [by] the price.", "ru": "Меня шокировала цена."},
         {"en": "She was {amazed} [at] how much he remembered.", "ru": "Она поразилась, как много он помнил."},
         {"en": "Nobody was {surprised} [at] his decision.", "ru": "Его решение никого не удивило."},
     ]},
    {"n": 11, "title": "pleased, excited, embarrassed",
     "rule": "pleased with — доволен результатом или человеком; pleased about — рад новости, событию (at — то же, чуть книжнее). excited about — предвкушаю событие; excited at — с the prospect, the thought, the idea. embarrassed about — стыдно за что-то; embarrassed by — кто или что смутило.",
     "ex": [
         {"en": "I'm really {pleased} [with] my new team.", "ru": "Я очень доволен своей новой командой."},
         {"en": "We're all {pleased} [about] the news.", "ru": "Мы все рады этой новости."},
         {"en": "She's {excited} [at] the prospect of working in London.", "ru": "Её радует перспектива поработать в Лондоне."},
         {"en": "He was {embarrassed} [by] all the attention.", "ru": "Его смутило всеобщее внимание."},
     ]},
    {"n": 12, "title": "annoyed, bored, depressed",
     "rule": "annoyed with — на человека (with him for being late), annoyed at или about — на ситуацию. bored with — нейтрально, bored of — разговорно, bored by — что нагнало скуку. depressed about — о ситуации, depressed over — о потере, затяжной беде; часто это одно и то же.",
     "ex": [
         {"en": "He gets {annoyed} [with] people who interrupt.", "ru": "Его раздражают люди, которые перебивают."},
         {"en": "I'm {bored} [with] this job.", "ru": "Мне наскучила эта работа."},
         {"en": "He's still {depressed} [over] losing his job.", "ru": "Он до сих пор подавлен из-за потери работы."},
     ]},
    {"n": MIXED_TOPIC, "title": "Итог — всё вместе",
     "rule": "Пятнадцать случайных карточек из всех тем вперемешку.",
     "ex": []},
]

CARDS = [
    # 1 — about
    {"id": "a-confused", "t": 1, "q": "Many patients are confused ___ their tablets.", "opts": ["about", "at", "of"], "a": "about",
     "why": "confused about — путаюсь «в чём, о чём»: тема, ситуация."},
    {"id": "a-excited", "t": 1, "q": "The whole team is excited ___ the new stroke pathway.", "opts": ["about", "with", "of"], "a": "about",
     "why": "excited about — предвкушаем событие, план."},
    {"id": "a-depressed", "t": 1, "q": "He's been depressed ___ his health since the stroke.", "opts": ["about", "at", "with"], "a": "about",
     "why": "depressed about — подавлен ситуацией. Можно и over."},
    {"id": "a-embarrassed", "t": 1, "q": "She's embarrassed ___ her accent.", "opts": ["about", "with", "on"], "a": "about",
     "why": "embarrassed about — стыдно за что-то в себе."},
    {"id": "a-worried", "t": 1, "q": "The family is worried ___ the scan results.", "opts": ["about", "of", "at"], "a": "about",
     "why": "worried about — как все чувства «о чём?»."},

    # 2 — at: реакция
    {"id": "b-amazed", "t": 2, "q": "I was amazed ___ how calm she stayed.", "opts": ["at", "with", "about"], "a": "at",
     "why": "amazed at + how / what — реакция на увиденное. by тоже можно."},
    {"id": "b-sight", "t": 2, "q": "Visitors are often shocked ___ the sight of all the monitors.", "opts": ["at", "with", "of"], "a": "at",
     "why": "shocked at the sight — реакция на увиденное; by тоже верно."},
    {"id": "b-delay", "t": 2, "q": "He was annoyed ___ the delay.", "opts": ["at", "of", "on"], "a": "at",
     "why": "annoyed at / about — на ситуацию. На человека — with."},
    {"id": "b-news", "t": 2, "q": "She was pleased ___ the news.", "opts": ["at", "of", "on"], "a": "at",
     "why": "pleased at — реакция на новость; about тоже верно."},
    {"id": "b-centre", "t": 2, "q": "He felt embarrassed ___ being the centre of attention.", "opts": ["at", "with", "on"], "a": "at",
     "why": "embarrassed at — неловко в моменте; about тоже можно. Дальше -ing."},

    # 3 — at: умение
    {"id": "c-explaining", "t": 3, "q": "She's good ___ explaining things to families.", "opts": ["at", "in", "with"], "a": "at",
     "why": "good at — «в чём силён?». in — калька с «хорош в»."},
    {"id": "c-names", "t": 3, "q": "I'm terribly bad ___ remembering names.", "opts": ["at", "in", "with"], "a": "at",
     "why": "bad at — плохо получается; дальше -ing."},
    {"id": "c-english", "t": 3, "q": "He's good ___ English, but his writing is weak.", "opts": ["at", "in", "with"], "a": "at",
     "why": "good at English — не in."},
    {"id": "c-with", "t": 3, "q": "She's very good ___ anxious patients.", "opts": ["with", "at", "in"], "a": "with",
     "why": "good with — умеет обращаться с людьми, детьми, руками. at — про навык."},
    {"id": "c-for", "t": 3, "q": "Regular walking is good ___ you.", "opts": ["for", "at", "with"], "a": "for",
     "why": "good for — полезно для."},

    # 4 — by
    {"id": "d-results", "t": 4, "q": "We were amazed ___ the results of the trial.", "opts": ["by", "of", "about"], "a": "by",
     "why": "The results amazed us → amazed by. at тоже можно."},
    {"id": "d-lecture", "t": 4, "q": "Half the audience was bored ___ the lecture.", "opts": ["by", "at", "about"], "a": "by",
     "why": "The lecture bored them → bored by. Так же bored with."},
    {"id": "d-saw", "t": 4, "q": "I was shocked ___ what I saw in A&E.", "opts": ["by", "of", "with"], "a": "by",
     "why": "What I saw shocked me → shocked by; at тоже верно."},
    {"id": "d-instructions", "t": 4, "q": "Patients are often confused ___ the discharge instructions.", "opts": ["by", "of", "with"], "a": "by",
     "why": "The instructions confuse them → confused by; about — «в чём путаются»."},
    {"id": "d-turnout", "t": 4, "q": "We were disappointed ___ the low turnout at the stroke awareness day.", "opts": ["by", "of", "on"], "a": "by",
     "why": "The turnout disappointed us → by; можно и with, about, at."},

    # 5 — with
    {"id": "e-satisfied", "t": 5, "q": "Most patients were satisfied ___ their care.", "opts": ["with", "of", "about"], "a": "with",
     "why": "satisfied with — доволен чем-то. Оценка — with."},
    {"id": "e-progress", "t": 5, "q": "I'm very pleased ___ your progress.", "opts": ["with", "of", "on"], "a": "with",
     "why": "pleased with — доволен результатом, человеком."},
    {"id": "e-him", "t": 5, "q": "Don't be annoyed ___ him — it's his first night shift.", "opts": ["with", "on", "of"], "a": "with",
     "why": "На человека — annoyed with. on — калька с «злиться на»."},
    {"id": "e-exercises", "t": 5, "q": "He soon got bored ___ the exercises.", "opts": ["with", "at", "about"], "a": "with",
     "why": "bored with — наскучило; разговорно — bored of."},
    {"id": "e-plan", "t": 5, "q": "Are you happy ___ the plan?", "opts": ["with", "at", "of"], "a": "with",
     "why": "happy with — доволен, согласен: частый вопрос пациенту."},

    # 6 — in, on
    {"id": "f-joining", "t": 6, "q": "Are you interested ___ joining our research group?", "opts": ["in", "about", "of"], "a": "in",
     "why": "interested in — только in; about — частая ошибка. Дальше -ing."},
    {"id": "f-neuro", "t": 6, "q": "She's always been interested ___ neurology.", "opts": ["in", "about", "for"], "a": "in",
     "why": "interested in — «интересуюсь чем-то»."},
    {"id": "f-him", "t": 6, "q": "His father was disappointed ___ him.", "opts": ["in", "about", "of"], "a": "in",
     "why": "Разочаровался в человеке — in (можно и with)."},
    {"id": "f-cycling", "t": 6, "q": "He's very keen ___ cycling.", "opts": ["on", "of", "in"], "a": "on",
     "why": "keen on — увлечён; дальше -ing."},
    {"id": "f-food", "t": 6, "q": "I'm not very keen ___ hospital food.", "opts": ["on", "of", "at"], "a": "on",
     "why": "not keen on — не в восторге от."},

    # 7 — of
    {"id": "g-terrified", "t": 7, "q": "My mother is terrified ___ hospitals.", "opts": ["of", "from", "about"], "a": "of",
     "why": "terrified of — «боюсь чего?» — of."},
    {"id": "g-afraid", "t": 7, "q": "Many patients are afraid ___ having another stroke.", "opts": ["of", "from", "about"], "a": "of",
     "why": "afraid / scared / terrified of + -ing."},
    {"id": "g-excuses", "t": 7, "q": "I'm tired ___ hearing the same excuses.", "opts": ["of", "about", "at"], "a": "of",
     "why": "tired of — надоело."},
    {"id": "g-scared", "t": 7, "q": "Don't be scared ___ asking questions.", "opts": ["of", "from", "at"], "a": "of",
     "why": "scared of + -ing — боюсь сделать."},
    {"id": "g-bored", "t": 7, "q": "The kids got bored ___ waiting and started running around.", "opts": ["of", "from", "in"], "a": "of",
     "why": "bored of — разговорный вариант bored with; оба верны."},

    # 8 — tired of / from
    {"id": "h-waiting", "t": 8, "q": "The family is tired ___ waiting — they want answers now.", "opts": ["of", "from"], "a": "of",
     "why": "Надоело ждать — tired of."},
    {"id": "h-legs", "t": 8, "q": "His legs were tired ___ the physio exercises.", "opts": ["from", "of"], "a": "from",
     "why": "Устали ноги — физически: tired from."},
    {"id": "h-noise", "t": 8, "q": "I'm sick and tired ___ the noise on this ward.", "opts": ["of", "from"], "a": "of",
     "why": "sick and tired of — «сыт по горло»."},
    {"id": "h-eyes", "t": 8, "q": "My eyes are tired ___ reading scans all day.", "opts": ["from", "of"], "a": "from",
     "why": "Устали глаза от работы — tired from."},
    {"id": "h-shift", "t": 8, "q": "She was too tired ___ the night shift to drive home.", "opts": ["from", "of"], "a": "from",
     "why": "Вымоталась за смену — tired from (или after)."},

    # 9 — disappointed
    {"id": "i-you", "t": 9, "q": "I'm disappointed ___ you — you promised to call.", "opts": ["in", "about", "at"], "a": "in",
     "why": "Разочаровался в человеке — in (можно и with)."},
    {"id": "i-missing", "t": 9, "q": "She's disappointed ___ missing the conference.", "opts": ["about", "in", "with"], "a": "about",
     "why": "Ситуация, факт — about; дальше -ing. at тоже возможно."},
    {"id": "i-outcome", "t": 9, "q": "The surgeon was disappointed ___ the outcome.", "opts": ["with", "of", "from"], "a": "with",
     "why": "Недоволен результатом — with."},
    {"id": "i-decision", "t": 9, "q": "Many doctors were disappointed ___ the hospital's decision.", "opts": ["by", "of", "to"], "a": "by",
     "why": "The decision disappointed them → by. Можно и with, about, at."},
    {"id": "i-herself", "t": 9, "q": "She was disappointed ___ herself for giving up.", "opts": ["in", "about", "of"], "a": "in",
     "why": "В себе — in (или with)."},

    # 10 — at = by
    {"id": "j-bp", "t": 10, "q": "I was shocked ___ his blood pressure.", "opts": ["by", "with", "of"], "a": "by",
     "why": "shocked by / at — оба верны; with — ошибка."},
    {"id": "j-dose", "t": 10, "q": "We were surprised ___ the low dose.", "opts": ["at", "with", "of"], "a": "at",
     "why": "surprised at / by — оба; with — калька «удивлён чем»."},
    {"id": "j-recovery", "t": 10, "q": "Everyone was amazed ___ her recovery.", "opts": ["by", "at", "of"], "a": "by",
     "also": {"at": "amazed at и amazed by — разницы почти нет"},
     "why": "amazed by = amazed at."},
    {"id": "j-news", "t": 10, "q": "The whole hospital was shocked ___ the news.", "opts": ["at", "by", "with"], "a": "at",
     "also": {"by": "shocked by и shocked at — одно и то же"},
     "why": "shocked at = shocked by; with — ошибка."},
    {"id": "j-result", "t": 10, "q": "Nobody was surprised ___ the result.", "opts": ["by", "with", "of"], "a": "by",
     "why": "surprised by / at — оба верны."},

    # 11 — pleased, excited, embarrassed
    {"id": "k-you", "t": 11, "q": "I'm very pleased ___ you — well done.", "opts": ["with", "about", "at"], "a": "with",
     "why": "Доволен человеком — pleased with."},
    {"id": "k-promotion", "t": 11, "q": "I'm so pleased ___ your promotion.", "opts": ["about", "of", "on"], "a": "about",
     "why": "Рад новости, событию — pleased about (или at)."},
    {"id": "k-holiday", "t": 11, "q": "The kids are excited ___ the holiday.", "opts": ["about", "at", "of"], "a": "about",
     "why": "Предвкушение события — excited about."},
    {"id": "k-prospect", "t": 11, "q": "He's excited ___ the prospect of a new job.", "opts": ["at", "of", "with"], "a": "at",
     "why": "at the prospect / the thought / the idea — устойчиво; about тоже можно."},
    {"id": "k-questions", "t": 11, "q": "He was embarrassed ___ his mother's questions.", "opts": ["by", "of", "with"], "a": "by",
     "why": "Вопросы матери смутили его → by (at тоже можно)."},

    # 12 — annoyed, bored, depressed
    {"id": "l-me", "t": 12, "q": "She's annoyed ___ me for being late.", "opts": ["with", "on", "about"], "a": "with",
     "why": "На человека — with (+ for doing). on — калька."},
    {"id": "l-parking", "t": 12, "q": "Everyone's annoyed ___ the parking situation.", "opts": ["about", "on", "for"], "a": "about",
     "why": "На ситуацию — about или at."},
    {"id": "l-series", "t": 12, "q": "I'm bored ___ this TV series.", "opts": ["of", "about", "at"], "a": "of",
     "why": "bored of — разговорное; нейтрально bored with."},
    {"id": "l-loss", "t": 12, "q": "He's been depressed ___ the loss of his wife.", "opts": ["over", "at", "with"], "a": "over",
     "why": "depressed over — из-за потери, затяжной беды; about тоже верно."},
    {"id": "l-result", "t": 12, "q": "Don't get depressed ___ one bad result.", "opts": ["about", "with", "at"], "a": "about",
     "why": "depressed about — о ситуации."},
]
