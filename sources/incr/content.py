# Содержание тренажёра «Increase by и increase to» — как описать изменение числа: на сколько (by), до какого значения (to),
# с какого до какого (from … to), чего (in), на сколько после существительного (of), на каком уровне (at).
# Отличие от «Цифр» (num): там по одной-две карточки на by, to и increase in среди прочих тем о числах;
# здесь — вся система предлогов изменения, глаголы rise, raise, increase, тренды, проценты и пункты, кратность, пороги, сравнение.
# Пометка […] — предлог или оборот в фокусе; цвет: by — оранжевый, to и from — синий, in и of — зелёный, остальные подчёркнуты.
# Темы с полем late вступают в общую тренировку позже: сначала B1, потом B1+, потом B2.

MIXED_TOPIC = 11

GROUPS = {
    "b1": "B1 — на сколько и до скольких",
    "b1p": "B1+ — описать изменение",
    "b2": "B2 — точность, как в статьях",
    "mix": "Итог",
}

# Главная таблица: предлог | вопрос («главное — пояснение») | пример
TABLE = [
    ["by", "на сколько? — разница между было и стало", "rose by 10%"],
    ["to", "до какого значения? — что стало", "rose to 30%"],
    ["from … to", "с какого до какого? — оба значения", "rose from 20% to 30%"],
    ["of", "на сколько — после существительного", "a rise of 10%"],
    ["in", "чего — после существительного", "a rise in mortality"],
    ["at", "на каком уровне — значение в точке", "peaked at 40% · stood at 12%"],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["Mortality fell [by 10%].", "на 10% — разница"],
     ["Mortality fell [to 10%].", "до 10% — столько стало"],
     ["Mortality fell [from 20% to 10%].", "с 20 до 10% — оба значения"]],
    [["Prices [rose] by 5%.", "выросли сами"],
     ["The shop [raised] prices by 5%.", "кто-то поднял"],
     ["Prices [increased]. The shop [increased] prices.", "increase — и так, и так"]],
    [["The rate rose [by 10 percentage points], from 20% to 30%.", "абсолютный рост — в пунктах"],
     ["The rate rose [by 50%], from 20% to 30%.", "относительный рост — в процентах"]],
    [["The number [doubled].", "вдвое больше"],
     ["The number rose [by 100%].", "тоже вдвое"],
     ["The number rose [by 200%].", "втрое, а не вдвое"]],
    [["Blood pressure [peaked at] 210 mmHg.", "максимум — 210"],
     ["It reached a peak [of] 210 mmHg.", "существительное — of"],
     ["On admission it [stood at] 180 mmHg.", "было 180 — значение в момент"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["Mortality decreased on 10%.", "Mortality decreased by 10%.", "на сколько — by"],
    ["We increased the dose till 80 mg.", "We increased the dose to 80 mg.", "до какого значения — to"],
    ["Prices raised by 5%.", "Prices rose by 5%.", "растут сами — rise"],
    ["We rose the dose.", "We raised the dose.", "поднять что-то — raise"],
    ["an increase of mortality", "an increase in mortality", "рост чего — in"],
    ["a rise on 5%", "a rise of 5%", "на сколько после существительного — of"],
    ["It increased in two times.", "It doubled.", "«в два раза» — doubled, twofold"],
    ["It exceeded over 180.", "It exceeded 180.", "exceed — без предлога"],
    ["It rose by 10% (from 20% to 30%).", "It rose by 10 percentage points.", "разница процентов — в пунктах"],
    ["BP stood on 160.", "BP stood at 160.", "значение в точке — at"],
]

TOPICS = [
    {"n": 1, "group": "b1", "title": "by или to", "sub": "на сколько · до какого значения",
     "rule": "Один вопрос к себе: я называю разницу или итог? Разница, «на сколько» — by: Her pressure fell by 30 mmHg. Итог, «до какого значения» — to: Her pressure fell to 150 mmHg. Предлог on здесь — калька с русского «на», till и until — только о времени. Глаголы любые: rise, fall, increase, reduce, go up, drop.",
     "ex": [
         {"en": "Her systolic pressure fell [by 30 mmHg].", "ru": "Её систолическое давление снизилось на 30 мм рт. ст."},
         {"en": "Her systolic pressure fell [to 150 mmHg].", "ru": "Её систолическое давление снизилось до 150 мм рт. ст."},
         {"en": "We increased the dose of atorvastatin [to 80 mg].", "ru": "Мы увеличили дозу аторвастатина до 80 мг."},
     ]},
    {"n": 2, "group": "b1", "title": "from … to и by … to вместе", "sub": "с какого до какого",
     "rule": "С какого до какого — from … to: Door-to-needle time fell from 75 to 40 minutes. Можно сказать всё сразу — сначала разницу, потом итог: Sodium fell by 10 mmol/L to 125 mmol/L; или разницу и оба значения: Admissions rose by 12%, from 850 to 950. Колебалось в пределах — between … and. Since — «с тех пор», о времени, а не о числах.",
     "ex": [
         {"en": "Door-to-needle time fell [from 75 to 40] minutes.", "ru": "Время «от двери до иглы» сократилось с 75 до 40 минут."},
         {"en": "Admissions rose [by 12%, from 850 to 950].", "ru": "Госпитализаций стало больше на 12% — с 850 до 950."},
         {"en": "Sodium fell [by 10 mmol/L to 125] mmol/L.", "ru": "Натрий снизился на 10 ммоль/л — до 125 ммоль/л."},
     ]},
    {"n": 3, "group": "b1", "title": "rise, raise или increase", "sub": "растёт само · кто-то поднял",
     "rule": "Растёт само — rise (rose, risen), снижается само — fall (fell, fallen). Кто-то поднял — raise (raised), кто-то снизил — reduce или lower. increase, decrease и drop бывают и так, и так: The number increased; we increased the number. Пассив — только от переходных: The dose was raised, а was risen не бывает. Arise — «возникнуть» о проблеме, не о числах.",
     "ex": [
         {"en": "Her temperature [rose] to 39 °C overnight.", "ru": "За ночь температура поднялась до 39 °C."},
         {"en": "We [raised] the head of the bed to 30 degrees.", "ru": "Мы подняли головной конец кровати до 30 градусов."},
         {"en": "The cardiologist [reduced] the dose of bisoprolol.", "ru": "Кардиолог снизил дозу бисопролола."},
     ]},
    {"n": 4, "group": "b1p", "title": "an increase in … of … to", "sub": "предлоги после существительного", "late": 0.2,
     "rule": "После существительного (an increase, a rise, a fall, a reduction, a drop) предлоги другие. Рост чего — in: a rise in glucose. На сколько — of: a reduction of 25%. До какого значения — по-прежнему to: a rise to 14 mmol/L. Всё вместе: a rise in glucose of 5 mmol/L. Число можно поставить вперёд: a 25% reduction in recurrent stroke. Существительное от grow — growth.",
     "ex": [
         {"en": "We saw a 20% increase [in] demand for MRI.", "ru": "Спрос на МРТ вырос на 20%."},
         {"en": "The study showed a reduction [of] 25% in recurrent stroke.", "ru": "Исследование показало снижение повторных инсультов на 25%."},
         {"en": "Steroids caused a rise in glucose [to] 14 mmol/L.", "ru": "На фоне стероидов глюкоза поднялась до 14 ммоль/л."},
     ]},
    {"n": 5, "group": "b1p", "title": "a sharp rise, rose sharply", "sub": "как именно изменилось", "late": 0.2,
     "rule": "Характер изменения: после глагола — наречие, перед существительным — прилагательное. rose sharply → a sharp rise, fell slightly → a slight fall, declined steadily → a steady decline, improved gradually → a gradual improvement. После be — прилагательное: The improvement was gradual. В статьях significantly значит «статистически значимо» (p < 0.05); если p нет, пишут markedly или considerably.",
     "ex": [
         {"en": "Admissions rose [sharply] during the heatwave.", "ru": "Во время жары число госпитализаций резко выросло."},
         {"en": "There was a [sharp] rise in admissions during the heatwave.", "ru": "Во время жары число госпитализаций резко выросло."},
         {"en": "We've seen a [steady] decline in smoking rates.", "ru": "Доля курящих неуклонно снижается."},
     ]},
    {"n": 6, "group": "b1p", "title": "peaked at, stood at, levelled off", "sub": "значение в точке — at", "late": 0.25,
     "rule": "Не изменение, а уровень в какой-то момент — at. peak at — достичь максимума: Troponin peaked at 2,400 ng/L. stand at — быть на уровне (отчёты): On admission his pressure stood at 210/120. remain at, stabilise at — держаться на уровне. Но существительное — of: reached a peak of 120. Выйти на плато — level off (брит. levelled, амер. leveled).",
     "ex": [
         {"en": "Troponin [peaked at] 2,400 ng/L on day two.", "ru": "Тропонин достиг максимума — 2400 нг/л — на второй день."},
         {"en": "On admission, his blood pressure [stood at] 210/120.", "ru": "При поступлении давление было 210/120."},
         {"en": "Cases reached a peak [of] 120 in February.", "ru": "Пик пришёлся на февраль — 120 случаев."},
     ]},
    {"n": 7, "group": "b2", "title": "per cent или percentage points", "sub": "абсолютный и относительный рост", "late": 0.45,
     "rule": "Если меняется сам процент, разницу меряют в процентных пунктах: с 40% до 60% — рост на 20 percentage points. В процентах это относительный рост: 20 из 40 — плюс 50%. Отсюда два снижения риска в статьях: абсолютное (ARR) — в пунктах, относительное (RRR) — в процентах. С 10% до 8%: ARR — 2 пункта, RRR — 20%. Per cent без -s; доля как существительное — a percentage of.",
     "ex": [
         {"en": "Adherence rose from 40% to 60%, an increase of [20 percentage points].", "ru": "Приверженность выросла с 40 до 60% — на 20 процентных пунктов."},
         {"en": "That is a relative increase [of 50%].", "ru": "Относительный рост — 50%."},
         {"en": "Recurrence fell from 10% to 8%, a relative risk reduction [of 20%].", "ru": "Повторные события снизились с 10 до 8% — относительное снижение риска на 20%."},
     ]},
    {"n": 8, "group": "b2", "title": "doubled, threefold, by 200%", "sub": "во сколько раз", "late": 0.45,
     "rule": "«В два раза» — doubled, «вдвое меньше» — halved, «втрое» — tripled. Increased twice — это «дважды», а in two times — калька. Книжно: a twofold increase, increased threefold, by a factor of four. Ловушка с процентами: плюс 100% — вдвое больше, плюс 200% — втрое: с 60 до 180 — tripled, или increased by 200%.",
     "ex": [
         {"en": "The number of thrombectomies [doubled], from 60 to 120 a year.", "ru": "Число тромбэктомий выросло вдвое — с 60 до 120 в год."},
         {"en": "Smoking is associated with a [twofold] increase in risk.", "ru": "Курение связано с двукратным ростом риска."},
         {"en": "From 60 to 180 is an increase [of 200%].", "ru": "С 60 до 180 — это рост на 200%, то есть втрое."},
     ]},
    {"n": 9, "group": "b2", "title": "exceed, fall below, rise above", "sub": "пороги и диапазоны", "late": 0.5,
     "rule": "Порог: exceed — превысить, без предлога: if blood pressure exceeds 185/110. С предлогом — rise above, be above, be over. Опуститься ниже — fall below, drop below. Не ниже — at or above, не выше — at or below. В пределах — between 2 and 3. reach — тоже без предлога: reached 40 °C, а не reached to.",
     "ex": [
         {"en": "Do not start thrombolysis if blood pressure [exceeds] 185/110.", "ru": "Не начинайте тромболизис, если давление выше 185/110."},
         {"en": "If saturation falls [below] 92%, give oxygen.", "ru": "Если сатурация падает ниже 92%, дайте кислород."},
         {"en": "Keep the INR [between] 2 [and] 3.", "ru": "Держите МНО в пределах от 2 до 3."},
     ]},
    {"n": 10, "group": "b2", "title": "from baseline, compared with", "sub": "сравнение в статьях", "late": 0.55,
     "rule": "Изменение от исходного уровня — from baseline: fell by 12 mmHg from baseline. По сравнению с — compared with (или compared to): lower compared with placebo. Сравнение двух чисел — versus: 4% versus 7%. С прошлым годом — over: up 8% over the previous year. Than — только после сравнительной степени: 30% higher than. В пересчёте на — relative to.",
     "ex": [
         {"en": "Systolic pressure fell by 12 mmHg [from baseline].", "ru": "Систолическое давление снизилось на 12 мм рт. ст. от исходного."},
         {"en": "Mortality was lower [compared with] the control group.", "ru": "Смертность была ниже, чем в контрольной группе."},
         {"en": "Recurrence was 4% in the treatment arm [versus] 7% with placebo.", "ru": "Повторные события — 4% в группе лечения против 7% на плацебо."},
     ]},
    {"n": 11, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · by или to
    c("i1-by", 1, "After treatment, her systolic pressure fell ___ 30 mmHg — from 180 to 150.", "После лечения её систолическое давление снизилось на 30 мм рт. ст. — со 180 до 150.",
      ["by", "to", "on"], "by", "На сколько, разница — by. On — калька с русского «на»."),
    c("i1-to", 1, "After treatment, her systolic pressure fell ___ 150 mmHg.", "После лечения её систолическое давление снизилось до 150 мм рт. ст.",
      ["to", "by", "till"], "to", "До какого значения — to. Till — только о времени, не о числах."),
    c("i1-list", 1, "The waiting list has grown ___ 15% this year.", "Очередь за год выросла на 15%.",
      ["by", "on", "at"], "by", "На сколько — by."),
    c("i1-dose", 1, "We increased the dose of atorvastatin ___ 80 mg.", "Мы увеличили дозу аторвастатина до 80 мг.",
      ["to", "by", "up"], "to", "Стало 80 мг — to. By 80 mg — «на 80 мг»: к прежней дозе добавили бы ещё 80."),
    c("i1-weight", 1, "His weight went down ___ 6 kg in three months.", "За три месяца он похудел на 6 кг.",
      ["by", "to", "for"], "by", "Разница — by: went down by 6 kg."),
    c("i1-ef", 1, "His ejection fraction improved ___ 45%.", "Фракция выброса улучшилась до 45%.",
      ["to", "on", "till"], "to", "Итоговое значение — to."),

    # 2 · from … to и by … to
    c("i2-dtn", 2, "Door-to-needle time fell ___ 75 to 40 minutes.", "Время «от двери до иглы» сократилось с 75 до 40 минут.",
      ["from", "since", "of"], "from", "С какого до какого — from … to. Since — «с тех пор», о времени."),
    c("i2-adm", 2, "Admissions rose by 12%, ___ 850 to 950.", "Госпитализаций стало больше на 12% — с 850 до 950.",
      ["from", "since", "of"], "from", "Разница и оба значения: by 12%, from 850 to 950."),
    c("i2-na", 2, "Sodium fell by 10 mmol/L ___ 125 mmol/L.", "Натрий снизился на 10 ммоль/л — до 125 ммоль/л.",
      ["to", "by", "from"], "to", "Сначала на сколько (by), потом до какого (to): fell by 10 to 125."),
    c("i2-between", 2, "Systolic pressure varied ___ 140 and 190 mmHg.", "Систолическое давление колебалось от 140 до 190.",
      ["between", "from", "among"], "between", "В пределах — between … and. Можно и from … to: varied from 140 to 190, но не from … and."),
    c("i2-share", 2, "The proportion treated within an hour went up ___ 30% in 2023 to 55% in 2025.", "Доля пролеченных в течение часа выросла с 30% в 2023 году до 55% в 2025-м.",
      ["from", "since", "at"], "from", "С какого до какого — from … to, даже если между ними стоят годы."),
    c("i2-beds", 2, "The ward was expanded from 30 beds ___ 45.", "Отделение расширили с 30 коек до 45.",
      ["to", "till", "up"], "to", "from … to. Till — о времени."),

    # 3 · rise, raise или increase
    c("i3-temp", 3, "Her temperature ___ to 39 °C overnight.", "За ночь температура поднялась до 39 °C.",
      ["rose", "raised", "arose"], "rose", "Поднялась сама — rise (rose, risen). Raise — поднять что-то, arise — возникнуть (о проблеме)."),
    c("i3-bed", 3, "We ___ the head of the bed to 30 degrees.", "Мы подняли головной конец кровати до 30 градусов.",
      ["raised", "rose", "risen"], "raised", "Подняли что-то — raise (raised)."),
    c("i3-bisoprolol", 3, "The cardiologist ___ the dose of bisoprolol.", "Кардиолог снизил дозу бисопролола.",
      ["reduced", "fell", "lowered down"], "reduced", "Снизить что-то — reduce или lower (без down). Fell — снизилось само."),
    c("i3-hr", 3, "His heart rate ___ to 48 after the beta-blocker.", "После бета-блокатора пульс снизился до 48.",
      ["fell", "lowered", "reduced"], "fell", "Снизился сам — fall (fell, fallen). Lower и reduce требуют дополнения: кто-то снизил что-то."),
    c("i3-number", 3, "The number of thrombectomies ___ last year.", "В прошлом году число тромбэктомий выросло.",
      ["increased", "raised", "arose"], "increased", "increase — и сам растёт, и кто-то увеличивает: the number increased; we increased the number."),
    c("i3-inr", 3, "The target INR was ___ to 3.0.", "Целевое МНО повысили до 3,0.",
      ["raised", "risen", "rose"], "raised", "Пассив — только от raise: was raised. Was risen не бывает."),

    # 4 · an increase in … of … to
    c("i4-mri", 4, "We saw a 20% increase ___ demand for MRI.", "Спрос на МРТ вырос на 20%.",
      ["in", "of", "on"], "in", "Рост чего — an increase in."),
    c("i4-of", 4, "The study showed a reduction ___ 25% in recurrent stroke.", "Исследование показало снижение повторных инсультов на 25%.",
      ["of", "in", "on"], "of", "На сколько после существительного — of: a reduction of 25%. By — после глагола: reduced by 25%."),
    c("i4-to", 4, "Steroids caused a rise in glucose ___ 14 mmol/L.", "На фоне стероидов глюкоза поднялась до 14 ммоль/л.",
      ["to", "at", "on"], "to", "До какого значения — to, и после существительного тоже: a rise to 14."),
    c("i4-drop", 4, "Orthostatic hypotension is a drop ___ blood pressure on standing.", "Ортостатическая гипотензия — падение давления при вставании.",
      ["in", "of", "at"], "in", "Падение чего — a drop in blood pressure."),
    c("i4-fall", 4, "There was a ___ of 20 mmHg in her systolic pressure.", "Её систолическое давление снизилось на 20 мм рт. ст.",
      ["fall", "fell", "fallen"], "fall", "Существительное — a fall, как глагол без окончаний: a fall of 20 mmHg."),
    c("i4-growth", 4, "The data show steady ___ in obesity rates.", "Данные показывают неуклонный рост ожирения.",
      ["growth", "grow", "grown"], "growth", "Существительное от grow — growth: growth in obesity rates."),

    # 5 · a sharp rise, rose sharply
    c("i5-sharply", 5, "Admissions rose ___ during the heatwave.", "Во время жары число госпитализаций резко выросло.",
      ["sharply", "sharp", "sharpen"], "sharply", "После глагола — наречие: rose sharply."),
    c("i5-sharp", 5, "There was a ___ rise in admissions during the heatwave.", "Во время жары госпитализаций стало резко больше.",
      ["sharp", "sharply", "sharpen"], "sharp", "Перед существительным — прилагательное: a sharp rise."),
    c("i5-steady", 5, "We've seen a ___ decline in smoking rates over the decade.", "За десятилетие доля курящих неуклонно снижалась.",
      ["steady", "steadily", "steadied"], "steady", "a steady decline — прилагательное перед существительным."),
    c("i5-slightly", 5, "Her creatinine increased ___, from 88 to 95.", "Креатинин у неё немного вырос — с 88 до 95.",
      ["slightly", "slight", "slighter"], "slightly", "После глагола — наречие: increased slightly."),
    c("i5-sig", 5, "Mortality fell ___ in the intervention group (p < 0.01).", "В группе вмешательства смертность статистически значимо снизилась (p < 0,01).",
      ["significantly", "significant", "signify"], "significantly", "В статье significantly — статистически значимо, p < 0.05. Без p лучше markedly или considerably."),
    c("i5-gradual", 5, "The improvement was ___ rather than sudden.", "Улучшение было постепенным, а не внезапным.",
      ["gradual", "gradually", "graduate"], "gradual", "После be — прилагательное: was gradual."),

    # 6 · peaked at, stood at
    c("i6-trop", 6, "Troponin peaked ___ 2,400 ng/L on day two.", "Тропонин достиг максимума — 2400 нг/л — на второй день.",
      ["at", "to", "by"], "at", "Максимум, значение в точке — peak at."),
    c("i6-stood", 6, "On admission, his blood pressure stood ___ 210/120.", "При поступлении давление было 210/120.",
      ["at", "on", "in"], "at", "Каким было значение в момент — stand at (книжно, в отчётах)."),
    c("i6-remained", 6, "Mortality remained ___ 8% throughout the study.", "Смертность всё исследование держалась на уровне 8%.",
      ["at", "on", "by"], "at", "Держалась на уровне — remain at."),
    c("i6-peak-of", 6, "The number of cases reached a peak ___ 120 in February.", "Пик пришёлся на февраль — 120 случаев.",
      ["of", "at", "to"], "of", "Существительное — a peak of 120. Глагол — peaked at 120."),
    c("i6-level", 6, "After the initial drop, the curve ___ off.", "После первоначального снижения кривая вышла на плато.",
      ["levelled", "stood", "peaked"], "levelled", "Выйти на плато — level off (брит. levelled, амер. leveled)."),
    c("i6-sat", 6, "Her saturation stabilised ___ 94% on two litres of oxygen.", "На двух литрах кислорода сатурация стабилизировалась на 94%.",
      ["at", "to", "on"], "at", "Стабилизировалась на уровне — stabilise at."),

    # 7 · per cent или percentage points
    c("i7-points", 7, "Adherence rose from 40% to 60% — an increase of 20 ___.", "Приверженность выросла с 40 до 60% — на 20 процентных пунктов.",
      ["percentage points", "per cent", "percents"], "percentage points", "Разница между двумя процентами — в процентных пунктах."),
    c("i7-relative", 7, "Adherence rose from 40% to 60%, which is a relative increase of ___.", "Приверженность выросла с 40 до 60% — относительный рост составил…",
      ["50%", "20%", "60%"], "50%", "Относительно исходных 40% рост на 20 пунктов — это плюс 50%: 20 / 40 = 0.5."),
    c("i7-rrr", 7, "Recurrence fell from 10% to 8%: an absolute reduction of 2 points and a ___ risk reduction of 20%.", "Повторные события снизились с 10 до 8%: абсолютное снижение — 2 пункта, относительное — 20%.",
      ["relative", "absolute", "total"], "relative", "Относительное снижение риска (RRR) — 2 из 10, то есть 20%. Абсолютное (ARR) — 2 процентных пункта."),
    c("i7-smoking", 7, "Smoking rates fell by three ___ points, from 25% to 22%.", "Доля курящих снизилась на три процентных пункта — с 25 до 22%.",
      ["percentage", "percent", "per cent"], "percentage", "Процентный пункт — percentage point."),
    c("i7-percent", 7, "Forty ___ of the patients were women.", "Сорок процентов пациентов — женщины.",
      ["per cent", "percents", "percentage"], "per cent", "После числа — per cent (брит.) или percent (амер.), без -s."),
    c("i7-percentage", 7, "A large ___ of patients arrived outside the treatment window.", "Значительная доля пациентов поступила вне терапевтического окна.",
      ["percentage", "per cent", "percent"], "percentage", "Доля без числа — a percentage of. С числом — per cent: 40 per cent."),

    # 8 · doubled, threefold, by 200%
    c("i8-doubled", 8, "The number of thrombectomies ___ — from 60 to 120 a year.", "Число тромбэктомий выросло вдвое — с 60 до 120 в год.",
      ["doubled", "increased twice", "increased in two times"], "doubled", "В два раза больше — doubled. Increased twice — «увеличилось дважды», in two times — калька."),
    c("i8-tripled", 8, "From 60 to 180 a year: the number ___.", "С 60 до 180 в год: число выросло втрое.",
      ["tripled", "doubled", "rose by 300%"], "tripled", "60 → 180 — втрое: tripled, или rose by 200%. Плюс 300% дало бы 240."),
    c("i8-fold", 8, "Smoking is associated with a two___ increase in risk.", "Курение связано с двукратным ростом риска.",
      ["fold", "times", "double"], "fold", "Двукратный — twofold: a twofold increase."),
    c("i8-factor", 8, "The risk increased by a ___ of four.", "Риск вырос в четыре раза.",
      ["factor", "fold", "time"], "factor", "В четыре раза — by a factor of four (книжно)."),
    c("i8-halved", 8, "Waiting times were ___ — from eight weeks to four.", "Время ожидания сократили вдвое — с восьми недель до четырёх.",
      ["halved", "decreased twice", "reduced in two times"], "halved", "Вдвое меньше — halved. Decreased twice — «снизили дважды»."),
    c("i8-100", 8, "If a number increases by 100%, it ___.", "Если число выросло на 100%, оно…",
      ["doubles", "triples", "stays the same"], "doubles", "Плюс 100% — удвоение. Ловушка: плюс 200% — утроение."),

    # 9 · exceed, fall below, rise above
    c("i9-exceeds", 9, "Do not start thrombolysis if blood pressure ___ 185/110.", "Не начинайте тромболизис, если давление выше 185/110.",
      ["exceeds", "exceeds over", "exceeds above"], "exceeds", "exceed — без предлога. С предлогом — is above, is over, is higher than."),
    c("i9-below", 9, "If saturation falls ___ 92%, give oxygen.", "Если сатурация падает ниже 92%, дайте кислород.",
      ["below", "lower", "under of"], "below", "Опуститься ниже уровня — fall below."),
    c("i9-above", 9, "Treat if glucose rises ___ 10 mmol/L.", "Лечите, если глюкоза поднимается выше 10 ммоль/л.",
      ["above", "higher", "over of"], "above", "Подняться выше уровня — rise above."),
    c("i9-inr", 9, "Keep the INR ___ 2 and 3.", "Держите МНО в пределах от 2 до 3.",
      ["between", "from", "within"], "between", "В пределах — between 2 and 3. Within ставят со словом range: within the range of 2 to 3."),
    c("i9-at-or", 9, "Readings at or ___ 140/90 count as raised.", "Показатели 140/90 и выше считаются повышенными.",
      ["above", "over than", "upper"], "above", "Не ниже — at or above, не выше — at or below."),
    c("i9-reached", 9, "His temperature ___ 40 °C.", "Температура у него дошла до 40 °C.",
      ["reached", "reached to", "achieved to"], "reached", "reach — без предлога: reached 40 °C."),

    # 10 · from baseline, compared with
    c("i10-baseline", 10, "Systolic pressure fell by 12 mmHg ___ baseline.", "Систолическое давление снизилось на 12 мм рт. ст. от исходного.",
      ["from", "of", "since"], "from", "Изменение от исходного уровня — from baseline."),
    c("i10-compared", 10, "Mortality was lower in the thrombectomy group ___ with the control group.", "В группе тромбэктомии смертность была ниже, чем в контрольной.",
      ["compared", "comparing", "comparison"], "compared", "По сравнению с — compared with (или compared to)."),
    c("i10-than", 10, "The risk was 30% higher in smokers ___ in non-smokers.", "У курящих риск был на 30% выше, чем у некурящих.",
      ["than", "that", "as"], "than", "После сравнительной степени — than: higher than."),
    c("i10-relative", 10, "The benefit was modest ___ to the cost.", "Польза была скромной в сравнении с затратами.",
      ["relative", "relatively", "related"], "relative", "relative to — по отношению к, в сравнении с."),
    c("i10-over", 10, "Admissions increased by 8% ___ the previous year.", "Госпитализаций стало на 8% больше, чем в прошлом году.",
      ["over", "than", "of"], "over", "По сравнению с прошлым периодом — over the previous year (или compared with). Than — только после сравнительной степени."),
    c("i10-versus", 10, "Recurrence was 4% in the treatment arm ___ 7% with placebo.", "Повторные события — 4% в группе лечения против 7% на плацебо.",
      ["versus", "than", "from"], "versus", "Сравнение двух чисел — versus (vs): 4% versus 7%."),
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
