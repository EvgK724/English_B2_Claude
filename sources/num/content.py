# Содержание приложения «Цифры»: язык чисел в результатах — by / to, increase in, fewer / less,
# twice as, доли, «примерно», a 65-year-old, как писать и читать числа.
# Пометка […] — слово в фокусе (оранжевый).

MIXED_TOPIC = 9

GROUPS = {
    "change": "Рост и снижение",
    "amount": "Сколько и во сколько раз",
    "share": "Доли и «примерно»",
    "write": "Как писать и читать",
    "mix": "Итог",
}

# Сколько и во сколько раз: слово | значение | пример | перевод примера
WORDS = [
    ["fewer", "меньше того, что считают", "fewer complications", "меньше осложнений"],
    ["less", "меньше того, что не считают", "less blood loss", "меньшая кровопотеря"],
    ["twice as", "в два раза", "twice as likely", "в два раза вероятнее"],
    ["half as", "вдвое меньше", "half as many strokes", "вдвое меньше инсультов"],
    ["three times", "в три раза", "three times higher", "в три раза выше"],
    ["one in five", "каждый пятый", "one in five patients", "каждый пятый пациент"],
]

# Одна цифра — разный смысл: строки [английский, пояснение]
CONTRAST = [
    [["Mortality fell [by] 10%.", "на 10%: это разница"],
     ["Mortality fell [to] 10%.", "до 10%: это новое значение"]],
    [["It rose from 20% to 30% — [by 10 percentage points].", "разница в пунктах: 30 − 20 = 10"],
     ["It rose from 20% to 30% — [by 50%].", "относительный рост: 10 от 20 — это половина"]],
    [["There were [fewer] complications.", "осложнения считают — fewer"],
     ["There was [less] bleeding.", "кровотечение штуками не считают — less"]],
    [["We now treat [twice as many] patients.", "вдвое больше"],
     ["We now treat [half as many] patients.", "вдвое меньше — не twice less"]],
    [["He is a [65-year-old] man.", "перед существительным: дефисы, year без s"],
     ["He is [65 years old].", "после глагола: years old"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["increased on 10%", "increased by 10%", "«на сколько» — by"],
    ["rose up to 40%", "rose to 40%", "«до» как итог — to; up to — «не больше»"],
    ["less patients", "fewer patients", "пациентов считают — fewer"],
    ["twice less side effects", "half as many side effects", "вдвое меньше — half as many"],
    ["the most of patients", "most patients", "большинство — most, без the"],
    ["a 65-years-old man", "a 65-year-old man", "перед сущ. — year без s"],
    ["1,5 mg", "1.5 mg", "дробь пишут через точку"],
    ["three hundreds patients", "three hundred patients", "hundred после числа — без s"],
    ["The number of patients were…", "The number of patients was…", "the number — одно число"],
    ["an increase of mortality", "an increase in mortality", "рост чего — increase in"],
]

TOPICS = [
    {"n": 1, "group": "change", "title": "by, to, from … to", "sub": "на, до, с … до",
     "rule": "На сколько изменилось — by: Mortality fell by 10%. До какого значения — to: Mortality fell to 10%. С какого до какого — from … to: from 12% to 8%. Up to — «до» только в смысле «не больше»: up to three doses a day. Разницу между процентами меряют в процентных пунктах: с 20% до 30% — рост на 10 percentage points, или на 50%. Percentage points — сверх уровня, но в статьях нужны постоянно.",
     "ex": [
         {"en": "Door-to-needle time fell [by] 15 minutes.", "ru": "Время «от двери до иглы» сократилось на 15 минут."},
         {"en": "The recanalisation rate rose [to] 80%.", "ru": "Частота реканализации выросла до 80%."},
         {"en": "Mortality fell [from] 12% [to] 8%.", "ru": "Смертность снизилась с 12 до 8%."},
     ]},
    {"n": 2, "group": "change", "title": "increase in, a 20% reduction", "sub": "рост чего и на сколько",
     "rule": "После существительного: рост чего — increase in, снижение чего — fall, decrease или reduction in: an increase in mortality. На сколько — of: a fall of 12 mmHg. Короче — число впереди: a 30% reduction in delays. Глаголы: rise (rose, risen) — расти сам, increase — и расти, и увеличивать: we increased the dose. Снижаться — fall, decline, drop. Не изменилось — remained stable или unchanged.",
     "ex": [
         {"en": "We saw a sharp increase [in] admissions.", "ru": "Мы наблюдали резкий рост числа госпитализаций."},
         {"en": "Systolic pressure showed a fall [of] 12 mmHg.", "ru": "Систолическое давление снизилось на 12 мм рт. ст."},
         {"en": "The new protocol led to a [30% reduction] in delays.", "ru": "Новый протокол сократил задержки на 30%."},
     ]},
    {"n": 3, "group": "amount", "title": "fewer, less, the number of", "sub": "меньше, число, количество",
     "rule": "Меньше того, что считают штуками, — fewer: fewer patients, fewer complications. Меньше того, что не считают, — less: less time, less bleeding. С числами и процентами — less than: less than 5%, less than 10 minutes. The number of patients was — «число» одно; a number of patients were — «несколько». Количество несчётного — the amount of: the amount of contrast.",
     "ex": [
         {"en": "There were [fewer] complications in the second group.", "ru": "Во второй группе было меньше осложнений."},
         {"en": "The procedure took [less] time than expected.", "ru": "Процедура заняла меньше времени, чем ожидалось."},
         {"en": "[The number of] patients treated within an hour has doubled.", "ru": "Число пациентов, пролеченных в первый час, удвоилось."},
     ]},
    {"n": 4, "group": "amount", "title": "twice as, three times", "sub": "во сколько раз",
     "rule": "В два раза больше — twice as many или much, в два раза чаще — twice as likely. Вдвое меньше — half as many: twice less — калька. В три раза и больше — three times as many или three times higher. Two times more — разговорно, в статье лучше twice. Одним глаголом: doubled — удвоилось, tripled — утроилось, halved — сократилось вдвое.",
     "ex": [
         {"en": "Smokers are [twice as] likely to have a stroke.", "ru": "Курящие в два раза чаще переносят инсульт."},
         {"en": "Patients with AF have a [five times] higher risk of stroke.", "ru": "У пациентов с ФП риск инсульта в пять раз выше."},
         {"en": "The waiting time has [halved].", "ru": "Время ожидания сократилось вдвое."},
     ]},
    {"n": 5, "group": "share", "title": "most, half, one in five", "sub": "большинство и доли",
     "rule": "Большинство — most patients (вообще) или most of the patients (конкретных). The most of patients — ошибка. Официальнее — the majority of patients. Половина — half of the patients или half the patients. Треть — a third of, четверть — a quarter of. Каждый пятый — one in five. После долей глагол согласуют с существительным: half of the patients were.",
     "ex": [
         {"en": "[Most] patients were discharged home.", "ru": "Большинство пациентов выписали домой."},
         {"en": "[One in five] patients had diabetes.", "ru": "Каждый пятый пациент страдал диабетом."},
         {"en": "[A quarter of] the beds were empty.", "ru": "Четверть коек пустовала."},
     ]},
    {"n": 6, "group": "share", "title": "about, over, at least", "sub": "примерно, больше, не меньше",
     "rule": "Примерно — about, around, в статьях approximately. Почти — nearly или almost. Чуть больше — just over, чуть меньше — just under: just over half. Больше — more than или over: more than 90%, patients over 80. Не меньше — at least. Не больше — up to. Меньше — less than или under: under 65.",
     "ex": [
         {"en": "[Approximately] 300 patients were screened.", "ru": "Было обследовано около 300 пациентов."},
         {"en": "[Just over] half of the patients were women.", "ru": "Чуть больше половины пациентов — женщины."},
         {"en": "The effect lasts [up to] 12 hours.", "ru": "Эффект длится до 12 часов."},
     ]},
    {"n": 7, "group": "write", "title": "a 65-year-old man", "sub": "число перед существительным",
     "rule": "Перед существительным число с единицей пишут через дефис и без -s: a 65-year-old man, a 12-month follow-up, a two-week course. После глагола — обычная форма: He is 65 years old. Hundred, thousand, million после числа — без -s: three hundred patients. Сотни — hundreds of. Возраст в статьях: patients aged 18 to 80.",
     "ex": [
         {"en": "A [72-year-old] woman was admitted with aphasia.", "ru": "72-летнюю женщину госпитализировали с афазией."},
         {"en": "We report [five-year] survival.", "ru": "Мы приводим пятилетнюю выживаемость."},
         {"en": "The study included two [hundred] patients.", "ru": "В исследование включили двести пациентов."},
     ]},
    {"n": 8, "group": "write", "title": "Точка, запятая, per", "sub": "как писать и читать числа",
     "rule": "Дробь пишут через точку: 2.5 mg, читают two point five. Запятая отделяет тысячи: 1,200 patients. Ноль в дроби: 0.5 — nought point five (брит.) или zero point five. 95% — ninety-five per cent. «В сутки», «на тысячу» — per: 10 mg per day, 5 per 1,000. Не путай: per day — в сутки, но by 10% — на 10%.",
     "ex": [
         {"en": "The dose is [2.5] mg twice a day.", "ru": "Доза — 2,5 мг два раза в день."},
         {"en": "The incidence was 5 [per] 1,000 people.", "ru": "Заболеваемость составила 5 на 1000 человек."},
         {"en": "About [1,200] patients were enrolled.", "ru": "Включили около 1200 пациентов."},
     ]},
    {"n": 9, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · by, to, from … to
    c("n1-by", 1, "Her blood pressure dropped ___ 30 mmHg after treatment.", "После лечения её давление снизилось на 30 мм рт. ст.",
      ["by", "to", "on"], "by", "На сколько — by."),
    c("n1-to", 1, "His sodium fell ___ 125 mmol/L.", "Натрий у него упал до 125 ммоль/л.",
      ["to", "by", "on"], "to", "До какого значения — to."),
    c("n1-from", 1, "The dose was reduced ___ 20 mg to 10 mg.", "Дозу снизили с 20 до 10 мг.",
      ["from", "of", "with"], "from", "С … до — from … to."),
    c("n1-prices", 1, "Prices have gone up ___ 15% this year.", "Цены в этом году выросли на 15%.",
      ["by", "on", "at"], "by", "«На» в изменениях — by, не on."),
    c("n1-up-to", 1, "Patients can take ___ four tablets a day.", "Пациенты могут принимать до четырёх таблеток в день.",
      ["up to", "to", "by"], "up to", "«До» в смысле «не больше» — up to."),
    c("n1-points", 1, "The rate rose from 20% to 30%, an increase of 10 percentage ___.", "Частота выросла с 20 до 30%, то есть на 10 процентных пунктов.",
      ["points", "per cent", "parts"], "points", "Разница между процентами — percentage points. 10% здесь было бы неверно: рост на 50%."),

    # 2 · increase in, a 20% reduction
    c("n2-in", 2, "There has been a steady increase ___ the number of stroke admissions.", "Число госпитализаций с инсультом неуклонно растёт.",
      ["in", "of", "on"], "in", "Рост чего — increase in."),
    c("n2-of", 2, "The drug produced a fall ___ 10 mmHg in systolic pressure.", "Препарат снизил систолическое давление на 10 мм рт. ст.",
      ["of", "in", "on"], "of", "На сколько после существительного — of."),
    c("n2-reduction", 2, "Thrombectomy led to a large ___ in disability.", "Тромбэктомия заметно уменьшила инвалидизацию.",
      ["reduction", "reduce", "reduced"], "reduction", "После a large нужно существительное — reduction in."),
    c("n2-stable", 2, "Mortality remained ___ over the study period.", "Смертность за период исследования оставалась стабильной.",
      ["stable", "stabile", "constantly"], "stable", "Не изменилась — remained stable."),
    c("n2-rose", 2, "Admissions ___ sharply in January.", "В январе число госпитализаций резко выросло.",
      ["rose", "raised", "arose"], "rose", "Растёт само — rise, rose. Raise — поднимать что-то."),
    c("n2-increased", 2, "We ___ the dose to 80 mg.", "Мы увеличили дозу до 80 мг.",
      ["increased", "rose", "grew"], "increased", "Увеличить что-то — increase. Rise и grow — расти самому."),
    c("n2-declined", 2, "Smoking rates have ___ steadily.", "Доля курящих неуклонно снижается.",
      ["declined", "lowered", "descended"], "declined", "Снижаться — decline. Lower — снижать что-то."),

    # 3 · fewer, less, the number of
    c("n3-fewer", 3, "___ patients than expected needed surgery.", "Операция понадобилась меньшему числу пациентов, чем ожидали.",
      ["fewer", "less", "little"], "fewer", "Пациентов считают — fewer."),
    c("n3-less", 3, "He's drinking ___ alcohol than before.", "Он пьёт меньше алкоголя, чем раньше.",
      ["less", "fewer", "lesser"], "less", "Алкоголь не считают штуками — less."),
    c("n3-than", 3, "The complication rate was ___ than 2%.", "Частота осложнений была меньше 2%.",
      ["less", "fewer", "little"], "less", "С процентами — less than."),
    c("n3-number", 3, "The number of beds ___ limited.", "Число коек было ограничено.",
      ["was", "were", "are"], "was", "The number — одно число: was."),
    c("n3-a-number", 3, "A number of patients ___ lost to follow-up.", "Несколько пациентов выбыли из-под наблюдения.",
      ["were", "was", "is"], "were", "A number of — «несколько»: were."),
    c("n3-amount", 3, "Reduce the ___ of salt in your diet.", "Уменьшите количество соли в рационе.",
      ["amount", "number", "many"], "amount", "Количество несчётного — the amount of."),

    # 4 · twice as, three times
    c("n4-twice", 4, "Women were ___ as likely to call an ambulance.", "Женщины в два раза чаще вызывали скорую.",
      ["twice", "two times", "double"], "twice", "В два раза — twice as.",
      {"two times": "но в статьях привычнее twice"}),
    c("n4-half", 4, "The new drug caused ___ as many side effects.", "Новый препарат вызывал вдвое меньше побочных эффектов.",
      ["half", "twice less", "two times less"], "half", "Вдвое меньше — half as many."),
    c("n4-times", 4, "The risk was three ___ higher in smokers.", "У курящих риск был в три раза выше.",
      ["times", "time", "once"], "times", "В три раза — three times."),
    c("n4-doubled", 4, "The number of thrombectomies has ___ since 2020.", "С 2020 года число тромбэктомий удвоилось.",
      ["doubled", "twiced", "double"], "doubled", "Удвоилось — doubled."),
    c("n4-many", 4, "We now treat twice as ___ patients as five years ago.", "Сейчас мы лечим вдвое больше пациентов, чем пять лет назад.",
      ["many", "much", "more"], "many", "Пациентов считают — twice as many."),
    c("n4-as", 4, "Men were three times as likely ___ women to smoke.", "Мужчины курили в три раза чаще женщин.",
      ["as", "than", "that"], "as", "three times as likely as — второе as."),
    c("n4-halved", 4, "Door-to-needle time was ___ after the new protocol.", "После нового протокола время «от двери до иглы» сократилось вдвое.",
      ["halved", "halfed", "half"], "halved", "Сократить вдвое — halve, halved."),

    # 5 · most, half, one in five
    c("n5-most", 5, "___ patients were men.", "Большинство пациентов — мужчины.",
      ["most", "the most", "most of"], "most", "Большинство — most, без the и без of."),
    c("n5-most-of", 5, "Most ___ the patients in our study were men.", "Большинство пациентов в нашем исследовании — мужчины.",
      ["of", "", "from"], "of", "Перед the — most of the."),
    c("n5-majority", 5, "The ___ of patients were treated within an hour.", "Большинство пациентов пролечили в течение часа.",
      ["majority", "most", "major"], "majority", "Официально — the majority of."),
    c("n5-one-in", 5, "Depression affects about one ___ three stroke survivors.", "Депрессия развивается примерно у каждого третьего, кто перенёс инсульт.",
      ["in", "of", "from"], "in", "Каждый третий — one in three."),
    c("n5-third", 5, "About a ___ of patients had AF.", "Примерно у трети пациентов была ФП.",
      ["third", "three", "triple"], "third", "Треть — a third of."),
    c("n5-half", 5, "Half of the patients ___ women.", "Половина пациентов — женщины.",
      ["were", "was", "is"], "were", "Глагол — по существительному: patients were."),

    # 6 · about, over, at least
    c("n6-nearly", 6, "___ 90% of patients completed the study.", "Почти 90% пациентов завершили исследование.",
      ["nearly", "near", "nearby"], "nearly", "Почти — nearly."),
    c("n6-least", 6, "Take the tablets for ___ least two weeks.", "Принимайте таблетки не меньше двух недель.",
      ["at", "in", "on"], "at", "Не меньше — at least."),
    c("n6-under", 6, "Just ___ half of the patients were women: 48%.", "Чуть меньше половины пациентов были женщинами — 48%.",
      ["under", "over", "more"], "under", "Чуть меньше — just under."),
    c("n6-more", 6, "The trial included ___ than 2,000 patients.", "В исследование включили больше 2000 пациентов.",
      ["more", "over", "above"], "more", "Больше чем — more than. Over — без than."),
    c("n6-over", 6, "Patients ___ 80 had worse outcomes.", "У пациентов старше 80 лет исходы были хуже.",
      ["over", "more", "upper"], "over", "Старше 80 — over 80."),
    c("n6-about", 6, "The procedure takes ___ an hour.", "Процедура занимает около часа.",
      ["about", "near", "approximate"], "about", "Около — about."),

    # 7 · a 65-year-old man
    c("n7-year-old", 7, "A 58-___ man presented with sudden weakness.", "58-летний мужчина обратился с внезапной слабостью.",
      ["year-old", "years-old", "years old"], "year-old", "Перед существительным — через дефисы и year без s."),
    c("n7-years-old", 7, "The patient is 58 ___.", "Пациенту 58 лет.",
      ["years old", "year-old", "years-old"], "years old", "После глагола — years old, без дефисов."),
    c("n7-month", 7, "All patients completed a 12-___ follow-up.", "Все пациенты прошли 12-месячное наблюдение.",
      ["month", "months", "monthly"], "month", "Перед существительным — без s: a 12-month follow-up."),
    c("n7-week", 7, "He was prescribed a two-___ course of antibiotics.", "Ему назначили двухнедельный курс антибиотиков.",
      ["week", "weeks", "weekly"], "week", "Перед существительным — без s: a two-week course."),
    c("n7-hundred", 7, "Three ___ patients were enrolled.", "В исследование включили триста пациентов.",
      ["hundred", "hundreds", "hundreds of"], "hundred", "После числа — hundred без s."),
    c("n7-hundreds", 7, "___ of patients are treated here every year.", "Здесь ежегодно лечат сотни пациентов.",
      ["hundreds", "hundred", "a hundreds"], "hundreds", "Сотни — hundreds of."),
    c("n7-aged", 7, "Patients ___ 18 to 80 were eligible.", "В исследование могли войти пациенты от 18 до 80 лет.",
      ["aged", "age", "ageing"], "aged", "В возрасте — aged."),

    # 8 · Точка, запятая, per
    c("n8-read", 8, "2.5 is read as \"two ___ five\".", "2,5 читается «две целых пять десятых».",
      ["point", "comma", "dot"], "point", "Дробь читают через point."),
    c("n8-decimal", 8, "The tablet contains ___ mg of warfarin.", "Таблетка содержит 2,5 мг варфарина.",
      ["2.5", "2,5"], "2.5", "Дробь пишут через точку: 2.5."),
    c("n8-thousand", 8, "The study included ___ patients.", "В исследование включили 1200 пациентов.",
      ["1,200", "1.200"], "1,200", "Тысячи отделяют запятой: 1,200. 1.200 — это 1,2."),
    c("n8-per-day", 8, "The maximum dose is 4 g ___ day.", "Максимальная доза — 4 г в сутки.",
      ["per", "in", "on"], "per", "В сутки — per day (или a day)."),
    c("n8-per-1000", 8, "The incidence is 2 cases ___ 1,000 people.", "Заболеваемость — 2 случая на 1000 человек.",
      ["per", "on", "for"], "per", "На тысячу — per 1,000."),
    c("n8-per-cent", 8, "Ninety-five ___ of patients were satisfied.", "95% пациентов остались довольны.",
      ["per cent", "percents", "percentage"], "per cent", "Процент — per cent, без s."),
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
