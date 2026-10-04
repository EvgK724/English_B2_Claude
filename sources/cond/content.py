# Содержание приложения «Conditionals».
# В примерах: {…} — часть с if (синий), […] — главная часть (оранжевый).

MIXED_TOPIC = 10

# Четыре типа: номер | когда | формула if-части | формула главной части | пример | перевод
TYPES = [
    ["0", "всегда так: факт, правило", "if + Present", "Present",
     "If you {take} warfarin, you [bruise] easily.", "Если принимаете варфарин, легко появляются синяки."],
    ["1", "реально может случиться", "if + Present", "will + глагол",
     "If the CT {is} clear, we['ll start] thrombolysis.", "Если КТ чистая, начнём тромболизис."],
    ["2", "воображаю: сейчас не так или вряд ли будет", "if + Past", "would + глагол",
     "If I {had} time, I['d help] you.", "Если бы у меня было время, я бы помог."],
    ["3", "уже поздно: в прошлом было иначе", "if + Past Perfect", "would have + V3",
     "If he {had come} earlier, we['d have treated] him.", "Если бы он приехал раньше, мы бы его пролечили."],
]

# «Если бы» — второй или третий: русская фраза | когда | английская
RUS_BY = [
    ["Если бы у меня было время, я бы помог.", "сейчас → 2", "If I {had} time, I['d help]."],
    ["Если бы вчера у меня было время, я бы помог.", "прошлое → 3", "If I {had had} time, I['d have helped]."],
    ["Если бы он принимал таблетки, ему было бы лучше.", "вообще, сейчас → 2", "If he {took} his tablets, he['d feel] better."],
    ["Если бы он принимал таблетки, инсульта бы не было.", "уже случилось → 3", "If he {had taken} them, he [wouldn't have had] a stroke."],
]

# Не только if: союз | перевод | пример | примечание
OTHER = [
    ["unless", "если не", "{Unless} you stop smoking, the risk stays high.", "= if … not; второе not не нужно"],
    ["as long as · provided", "при условии, что", "You can go home {as long as} someone stays with you.", ""],
    ["in case", "на случай, если", "Take a spare dose {in case} your flight is delayed.", "это не if: делаю заранее"],
    ["when · as soon as · until", "когда, как только, пока не", "I'll call you {as soon as} the results come.", "тоже без will"],
]

# I wish / If only: форма | смысл | пример
WISH = [
    ["wish + Past", "жаль, что сейчас не так", "I wish I {had} more time."],
    ["wish + Past Perfect", "жаль, что тогда было так", "I wish I {had listened} to you."],
    ["wish + would", "хочу, чтобы другой изменился", "I wish you [would stop] interrupting."],
]

# Частые ошибки: неверно | верно | почему
ERRORS = [
    ["If it will rain, we'll stay in", "If it rains, we'll stay in", "в части с if нет will"],
    ["If I would have time, I'd help", "If I had time, I'd help", "в части с if нет would"],
    ["If he would have come earlier…", "If he had come earlier…", "третий тип — had + V3"],
    ["When the results will come, I'll call", "When the results come, I'll call", "when, as soon as — тоже без will"],
    ["Unless you don't stop smoking", "Unless you stop smoking", "unless уже значит «если не»"],
    ["I wish I would have more time", "I wish I had more time", "wish о настоящем — Past"],
]

TOPICS = [
    {"n": 1, "title": "0 — всегда так",
     "rule": "Нулевой тип — факты, законы, правила, инструкции: то, что происходит всегда, когда выполнено условие. Обе части в Present Simple: If you take warfarin, you bruise easily. if здесь почти равно when. Никаких would.",
     "ex": [
         {"en": "If you {take} warfarin, you [bruise] more easily.", "ru": "Если принимаете варфарин, легче появляются синяки."},
         {"en": "If blood sugar {drops} too low, the patient [gets] confused.", "ru": "Если сахар сильно падает, пациент становится спутанным."},
     ]},
    {"n": 2, "title": "1 — реальное будущее",
     "rule": "Первый тип — то, что реально может случиться: if + Present, в главной части will, can, may или повелительное наклонение. Главная ловушка: по-русски «если будет», по-английски в части с if — Present: If the CT is clear, we'll start thrombolysis, а не if the CT will be clear. Так же после when, as soon as, before, after, until: I'll call you as soon as the results come.",
     "ex": [
         {"en": "If the CT {is} clear, we['ll start] thrombolysis.", "ru": "Если КТ чистая, начнём тромболизис."},
         {"en": "I['ll call] you as soon as the results {come} back.", "ru": "Позвоню, как только придут результаты."},
         {"en": "If the pain {gets} worse, [call] us.", "ru": "Если боль усилится, звоните нам."},
     ]},
    {"n": 3, "title": "2 — воображаю: сейчас не так",
     "rule": "Второй тип — воображаемое: сейчас не так или вряд ли будет. if + Past Simple, в главной части would (could, might) + глагол: If I had more time, I'd do a PhD — времени нет. По-русски «бы» в обеих частях, по-английски would — только в главной. If I were you — «на твоём месте»: were для всех лиц; в разговоре бывает и was.",
     "ex": [
         {"en": "If I {had} more time, I['d do] a PhD.", "ru": "Если бы у меня было больше времени, я бы писал диссертацию."},
         {"en": "If I {were} you, I['d see] a neurologist.", "ru": "На твоём месте я бы сходил к неврологу."},
         {"en": "What [would you do] if a patient {refused} treatment?", "ru": "Что бы вы сделали, если бы пациент отказался от лечения?"},
     ]},
    {"n": 4, "title": "3 — уже поздно: прошлое",
     "rule": "Третий тип — прошлое, которое уже не изменить: сожаление, разбор ошибок. if + Past Perfect (had + V3), в главной части would have + V3 (или could have, might have): If he had arrived earlier, we could have given thrombolysis — но он приехал поздно.",
     "ex": [
         {"en": "If he {had arrived} earlier, we [could have given] thrombolysis.", "ru": "Если бы он приехал раньше, мы могли бы провести тромболизис."},
         {"en": "If we {had known} about the allergy, we [wouldn't have given] penicillin.", "ru": "Если бы мы знали об аллергии, мы бы не дали пенициллин."},
     ]},
    {"n": 5, "title": "«Если бы»: второй или третий?",
     "rule": "Русское «если бы» — одна форма, английских две. Решает время. Речь о сейчас или вообще — второй тип: If I had time, I'd help. Речь о прошлом, которое уже случилось, — третий: If I'd had time yesterday, I'd have helped. Подсказки третьего: yesterday, then, last year, уже случилось.",
     "ex": [
         {"en": "If I {had} time, I['d help] you.", "ru": "Если бы у меня было время (сейчас), я бы помог."},
         {"en": "If I {had had} time, I['d have helped] you.", "ru": "Если бы у меня было время (тогда), я бы помог."},
     ]},
    {"n": 6, "title": "unless, as long as, in case",
     "rule": "unless — «если не»: Unless you stop smoking = If you don't stop smoking; второе not не нужно. as long as, provided (that) — «при условии, что». in case — «на случай, если»: делаю заранее, это не if: Take a spare dose in case your flight is delayed. После всех них, как после if, — без will.",
     "ex": [
         {"en": "{Unless} you stop smoking, your risk will stay high.", "ru": "Если не бросите курить, риск останется высоким."},
         {"en": "You can go home {as long as} someone stays with you.", "ru": "Можете идти домой, если кто-то останется с вами."},
         {"en": "Take a spare dose {in case} your flight is delayed.", "ru": "Возьмите запасную дозу на случай, если рейс задержат."},
     ]},
    {"n": 7, "title": "Смешанные: прошлое → сейчас", "late": 0.35,
     "rule": "Сверх уровня, но часто нужно. Причина в прошлом, результат сейчас: if + Past Perfect, в главной части would + глагол: If he had taken his tablets, he wouldn't be in hospital now. Подсказка — now, today, still в главной части.",
     "ex": [
         {"en": "If he {had taken} his tablets, he [wouldn't be] in hospital now.", "ru": "Если бы он принимал таблетки, он бы сейчас не лежал в больнице."},
         {"en": "If I {hadn't become} a doctor, I['d probably be] a teacher.", "ru": "Если бы я не стал врачом, я бы, наверное, был учителем."},
     ]},
    {"n": 8, "title": "I wish и If only", "late": 0.15,
     "rule": "I wish и If only — «жаль, что…», те же сдвиги, что во втором и третьем типе. О настоящем — Past: I wish I had more time. О прошлом — Past Perfect: I wish I had listened. wish + would — хочу, чтобы другой изменил поведение: I wish you would stop interrupting.",
     "ex": [
         {"en": "I wish I {had} more time.", "ru": "Жаль, что у меня мало времени."},
         {"en": "I wish I {had listened} to you.", "ru": "Жаль, что я тебя не послушал."},
         {"en": "I wish you [would stop] interrupting me.", "ru": "Хоть бы ты перестал меня перебивать."},
     ]},
    {"n": 9, "title": "Для писем: Should you…", "late": 0.5,
     "rule": "Сверх уровня, но пригодится в официальных письмах: if убирают и меняют порядок слов. Should you have any questions = If you have any questions. Had I known = If I had known. Were it not for = If it weren't for.",
     "ex": [
         {"en": "{Should} you have any questions, please contact us.", "ru": "Если у вас возникнут вопросы, свяжитесь с нами."},
         {"en": "{Had} I known, I would have called you.", "ru": "Знал бы я — позвонил бы тебе."},
     ]},
    {"n": MIXED_TOPIC, "title": "Итог — всё вместе",
     "rule": "Пятнадцать случайных карточек из всех тем вперемешку.",
     "ex": []},
]

CARDS = [
    # 0 — всегда так
    {"id": "z-neurons", "t": 1, "q": "If the brain doesn't get oxygen for a few minutes, neurons ___.", "opts": ["die", "would die", "died"], "a": "die",
     "why": "Факт, так всегда — Present: die."},
    {"id": "z-warfarin", "t": 1, "q": "If you ___ warfarin, you bruise more easily.", "opts": ["take", "will take", "took"], "a": "take",
     "why": "Нулевой тип: Present в обеих частях."},
    {"id": "z-sugar", "t": 1, "q": "When blood sugar ___ too low, patients often feel confused.", "opts": ["drops", "will drop", "dropped"], "a": "drops",
     "why": "Так бывает всегда — Present: drops."},
    {"id": "z-cuff", "t": 1, "q": "If the cuff is too small, the reading ___ falsely high.", "opts": ["is", "would be", "was"], "a": "is",
     "why": "Правило, так всегда — Present: is."},
    {"id": "z-stroke", "t": 1, "q": "If a patient ___ a stroke, every minute counts.", "opts": ["has", "will have", "had"], "a": "has",
     "why": "Общее правило — Present: has."},

    # 1 — реальное будущее
    {"id": "f-ct", "t": 2, "q": "If the CT ___ clear, we'll start thrombolysis.", "opts": ["is", "will be", "would be"], "a": "is",
     "why": "В части с if нет will: if the CT is clear."},
    {"id": "f-call", "t": 2, "q": "If the pain gets worse, ___ me immediately.", "opts": ["call", "you would call", "you called"], "a": "call",
     "why": "Первый тип с повелительным: If…, call me."},
    {"id": "f-dose", "t": 2, "q": "___ the dose if his INR is still high tomorrow.", "opts": ["We'll reduce", "We'd reduce", "We reduced"], "a": "We'll reduce",
     "why": "Реальное будущее — will в главной части."},
    {"id": "f-results", "t": 2, "q": "I'll call you as soon as the results ___ back.", "opts": ["come", "will come", "came"], "a": "come",
     "why": "После as soon as, как после if, — без will."},
    {"id": "f-until", "t": 2, "q": "Don't discharge him until he ___ able to walk.", "opts": ["is", "will be", "would be"], "a": "is",
     "why": "После until — без will: until he is able."},
    {"id": "f-smoking", "t": 2, "q": "If you ___ smoking, your risk will fall.", "opts": ["stop", "will stop", "stopped"], "a": "stop",
     "why": "Реально — if + Present: if you stop."},

    # 2 — воображаю
    {"id": "s-phd", "t": 3, "q": "If I ___ more time, I'd do a PhD.", "opts": ["had", "have", "would have"], "a": "had",
     "why": "Времени нет — второй тип: if + Past. Would в части с if не ставят."},
    {"id": "s-were", "t": 3, "q": "If I ___ you, I'd see a neurologist.", "opts": ["were", "would be", "am"], "a": "were",
     "why": "If I were you — «на твоём месте»."},
    {"id": "s-refused", "t": 3, "q": "What ___ you do if a patient refused treatment?", "opts": ["would", "will", "did"], "a": "would",
     "why": "refused — воображаемая ситуация: what would you do?"},
    {"id": "s-scanner", "t": 3, "q": "If we had a second scanner, patients ___ so long.", "opts": ["wouldn't wait", "won't wait", "didn't wait"], "a": "wouldn't wait",
     "why": "Второго сканера нет — would в главной части."},
    {"id": "s-tablets", "t": 3, "q": "If he ___ his tablets regularly, his blood pressure would be normal.", "opts": ["took", "takes", "would take"], "a": "took",
     "why": "Он их не принимает — воображаем: if + Past."},
    {"id": "s-drug", "t": 3, "q": "I ___ that drug if I were you.", "opts": ["wouldn't take", "won't take", "didn't take"], "a": "wouldn't take",
     "why": "if I were you — второй тип: would."},

    # 3 — прошлое
    {"id": "t-arrived", "t": 4, "q": "If he ___ earlier, we could have given thrombolysis.", "opts": ["had arrived", "arrived", "would have arrived"], "a": "had arrived",
     "why": "Прошлое, уже поздно — if + Past Perfect."},
    {"id": "t-allergy", "t": 4, "q": "If we had known about the allergy, we ___ penicillin.", "opts": ["wouldn't have given", "wouldn't give", "didn't give"], "a": "wouldn't have given",
     "why": "Третий тип — would have + V3."},
    {"id": "t-rails", "t": 4, "q": "She ___ the fall if the bed rails had been up.", "opts": ["wouldn't have had", "wouldn't have", "hadn't had"], "a": "wouldn't have had",
     "why": "Упала в прошлом — would have + V3."},
    {"id": "t-ecg", "t": 4, "q": "If I ___ at the ECG more carefully, I would have spotted the AF.", "opts": ["had looked", "looked", "would look"], "a": "had looked",
     "why": "Сожаление о прошлом — if + had + V3."},
    {"id": "t-might", "t": 4, "q": "If the ambulance had come sooner, he ___ survived.", "opts": ["might have", "might", "will have"], "a": "might have",
     "why": "Третий тип — might have + V3."},

    # «если бы» — второй или третий
    {"id": "b-now", "t": 5, "q": "If I ___ more time, I'd help you.", "ru": "Если бы у меня было больше времени (сейчас), я бы тебе помог.",
     "opts": ["had", "had had"], "a": "had", "why": "Сейчас — второй тип: had."},
    {"id": "b-then", "t": 5, "q": "If I ___ more time yesterday, I'd have helped you.", "ru": "Если бы вчера у меня было больше времени, я бы тебе помог.",
     "opts": ["had had", "had"], "a": "had had", "why": "Вчера, уже прошло — третий тип: had had."},
    {"id": "b-stroke", "t": 5, "q": "If he ___ his anticoagulant, he wouldn't have had a stroke.", "ru": "Если бы он принимал антикоагулянт, инсульта бы не было.",
     "opts": ["had taken", "took"], "a": "had taken", "why": "Инсульт уже случился — третий тип."},
    {"id": "b-safer", "t": 5, "q": "If he ___ his anticoagulant every day, he'd be safer.", "ru": "Если бы он принимал антикоагулянт каждый день (а он не принимает), ему было бы безопаснее.",
     "opts": ["took", "had taken"], "a": "took", "why": "Вообще, сейчас — второй тип: took."},
    {"id": "b-called", "t": 5, "q": "If you ___ me, I would have come.", "ru": "Если бы ты мне тогда позвонил, я бы пришёл.",
     "opts": ["had called", "called"], "a": "had called", "why": "Тогда — третий тип: had called."},
    {"id": "b-often", "t": 5, "q": "If you ___ me more often, I'd know what's going on.", "ru": "Если бы ты чаще звонил, я бы знал, что происходит.",
     "opts": ["called", "had called"], "a": "called", "why": "Сейчас, вообще — второй тип: called."},

    # unless, as long as, in case
    {"id": "u-unless", "t": 6, "q": "___ you stop smoking, your risk will stay high.", "ru": "Если не бросите курить, риск останется высоким.",
     "opts": ["Unless", "If", "In case"], "a": "Unless", "why": "«Если не» — unless."},
    {"id": "u-inr", "t": 6, "q": "Unless the INR ___ below 1.7, we can't operate.", "ru": "Пока МНО не будет ниже 1,7, оперировать нельзя.",
     "opts": ["is", "isn't", "will be"], "a": "is", "why": "unless уже значит «если не» — второе not не нужно."},
    {"id": "u-flight", "t": 6, "q": "Take a spare dose ___ your flight is delayed.", "ru": "Возьмите запасную дозу на случай, если рейс задержат.",
     "opts": ["in case", "if", "unless"], "a": "in case", "why": "Делаю заранее, на всякий случай — in case."},
    {"id": "u-home", "t": 6, "q": "You can go home ___ someone stays with you tonight.", "ru": "Можете идти домой при условии, что кто-то останется с вами на ночь.",
     "opts": ["as long as", "in case", "unless"], "a": "as long as", "why": "«При условии, что» — as long as."},
    {"id": "u-write", "t": 6, "q": "Write the dose down ___ you forget it.", "ru": "Запишите дозу на случай, если забудете.",
     "opts": ["in case", "if", "unless"], "a": "in case", "why": "На всякий случай — in case."},

    # смешанные
    {"id": "m-now", "t": 7, "q": "If he had taken his tablets, he ___ in hospital now.", "opts": ["wouldn't be", "wouldn't have been", "won't be"], "a": "wouldn't be",
     "why": "Причина в прошлом, результат сейчас (now) — would be."},
    {"id": "m-teacher", "t": 7, "q": "If I hadn't become a doctor, I ___ a teacher now.", "opts": ["would be", "would have been"], "a": "would be",
     "why": "now — результат сейчас: would be."},
    {"id": "m-scanner", "t": 7, "q": "If we had bought a new scanner last year, we ___ faster results now.", "opts": ["would have", "would have had", "will have"], "a": "would have",
     "why": "now — сейчас: would have (глагол have)."},
    {"id": "m-lungs", "t": 7, "q": "If he hadn't smoked for forty years, his lungs ___ healthier today.", "opts": ["would be", "would have been"], "a": "would be",
     "why": "today — результат сейчас: would be."},

    # I wish / If only
    {"id": "w-time", "t": 8, "q": "I wish I ___ more time for my family.", "opts": ["had", "have", "would have"], "a": "had",
     "why": "Жаль, что сейчас не так — wish + Past."},
    {"id": "w-spoken", "t": 8, "q": "I wish I ___ to him before he left.", "opts": ["had spoken", "spoke", "would speak"], "a": "had spoken",
     "why": "Жаль, что тогда не поговорил — wish + Past Perfect."},
    {"id": "w-stop", "t": 8, "q": "I wish you ___ interrupting me!", "opts": ["would stop", "stopped", "had stopped"], "a": "would stop",
     "why": "Раздражает, хочу, чтобы перестал, — wish + would."},
    {"id": "w-checked", "t": 8, "q": "If only I ___ the results earlier!", "opts": ["had checked", "checked", "would check"], "a": "had checked",
     "why": "earlier — о прошлом: If only + Past Perfect."},
    {"id": "w-french", "t": 8, "q": "I wish I ___ French — the patient doesn't speak English.", "opts": ["spoke", "speak", "had spoken"], "a": "spoke",
     "why": "Сейчас не говорю — wish + Past."},

    # для писем
    {"id": "i-should", "t": 9, "q": "___ you have any questions, please contact the ward.", "opts": ["Should", "Would", "Will"], "a": "Should",
     "why": "Should you… = If you… — официально."},
    {"id": "i-had", "t": 9, "q": "___ I known about his allergy, I would never have prescribed it.", "opts": ["Had", "If", "Have"], "a": "Had",
     "why": "Had I known = If I had known."},
    {"id": "i-return", "t": 9, "q": "___ the symptoms return, seek medical help immediately.", "opts": ["Should", "Would", "Will"], "a": "Should",
     "why": "Should the symptoms return = If the symptoms return."},
]
