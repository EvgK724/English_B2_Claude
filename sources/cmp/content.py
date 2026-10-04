# Содержание приложения «Сравнения»: -er / more, неправильные формы, самый, than и as … as,
# насколько (much, slightly), во сколько раз (twice as), «чем…, тем…», язык статей.
# Пометка […] — форма в фокусе (оранжевый).

MIXED_TOPIC = 9

GROUPS = {
    "form": "Как образовать",
    "compare": "Как сравнить",
    "research": "В статьях",
    "mix": "Итог",
}

# Как сравнить: конструкция | смысл | пример | перевод
TABLE = [
    ["than", "больше, меньше", "older than me", "старше меня"],
    ["as … as", "так же", "as good as", "такой же хороший"],
    ["not as … as", "не такой", "not as easy as", "не такой простой"],
    ["the …, the …", "чем…, тем…", "the sooner, the better", "чем скорее, тем лучше"],
    ["much, far + -er", "намного", "much better", "намного лучше"],
    ["twice as … as", "в два раза", "twice as likely", "в два раза вероятнее"],
]

# Одна ситуация — разный смысл: строки [английский, перевод]
CONTRAST = [
    [["He's [taller than] me.", "выше меня"], ["He's [as tall as] me.", "такого же роста"], ["He's [not as tall as] me.", "ниже меня"]],
    [["She's [much better].", "намного лучше"], ["She's [a bit better].", "немного лучше"], ["She's [even better].", "ещё лучше"]],
    [["There were [fewer] complications.", "меньше осложнений — исчисляемые"], ["There was [less] bleeding.", "меньше кровотечений — неисчисляемое"]],
    [["The hospital is [further] away.", "дальше — расстояние"], ["We need [further] tests.", "дополнительные анализы"]],
    [["Smokers are [twice as likely] to have a stroke.", "в два раза чаще"], ["Non-smokers are [half as likely] to have a stroke.", "в два раза реже"]],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["more better", "better", "better — уже сравнительная"],
    ["more easy", "easier", "короткие на -y — -ier"],
    ["very better", "much better", "с -er — much, far, a lot"],
    ["taller then me", "taller than me", "чем — than, не then"],
    ["the same like", "the same as", "такой же, как — the same as"],
    ["the most good", "the best", "good — better — the best"],
    ["less patients", "fewer patients", "исчисляемые — fewer"],
    ["the best doctor of the hospital", "the best doctor in the hospital", "место, коллектив — in"],
    ["two times more expensive", "twice as expensive", "в два раза — twice as … as"],
    ["similar with", "similar to", "похожий на — similar to"],
]

TOPICS = [
    {"n": 1, "group": "form", "title": "-er или more", "sub": "как образовать сравнительную",
     "rule": "Один слог — -er: tall → taller, cheap → cheaper. Короткий гласный + согласный — согласная удваивается: big → bigger, hot → hotter. Два слога на -y — -ier: easy → easier, early → earlier. Остальные двусложные и длинные — more: more careful, more effective, more important. Вместе нельзя: more better, more easier — ошибки.",
     "ex": [
         {"en": "Generic drugs are [cheaper] than brand-name ones.", "ru": "Дженерики дешевле оригинальных препаратов."},
         {"en": "The new form is [easier] to fill in.", "ru": "Новую форму проще заполнять."},
         {"en": "This drug is [more effective].", "ru": "Этот препарат эффективнее."},
     ]},
    {"n": 2, "group": "form", "title": "Неправильные: good, bad, far", "sub": "better, worse, further, less",
     "rule": "good → better → the best; bad → worse → the worst; far → further → the furthest (о расстоянии ещё farther); much, many → more → the most; little → less → the least. further значит ещё и «дополнительный»: further tests, further information.",
     "ex": [
         {"en": "She's feeling [better] today.", "ru": "Сегодня ей лучше."},
         {"en": "The pain is [worse] at night.", "ru": "Ночью боль сильнее."},
         {"en": "We need [further] tests.", "ru": "Нужны дополнительные анализы."},
     ]},
    {"n": 3, "group": "form", "title": "Самый: the -est, the most", "sub": "превосходная степень",
     "rule": "Один слог — the -est: the biggest, the fastest; на -y — the -iest: the easiest; длинные — the most: the most effective. Всегда с the. «Один из самых» — one of the most + множественное число: one of the most common causes. Место, коллектив — in: the best hospital in the city; из нескольких — of: the youngest of the three. Наименее — the least: the least invasive.",
     "ex": [
         {"en": "Stroke is [one of the most common] causes of disability.", "ru": "Инсульт — одна из самых частых причин инвалидности."},
         {"en": "It's [the biggest] hospital in the city.", "ru": "Это самая большая больница в городе."},
         {"en": "Start with [the least invasive] option.", "ru": "Начните с наименее инвазивного варианта."},
     ]},
    {"n": 4, "group": "compare", "title": "than, as … as, not as … as", "sub": "больше, так же, не такой",
     "rule": "Больше или меньше — -er или more + than: He's taller than me. Так же — as … as, прилагательное в обычной форме: as good as, as effective as. Не такой — not as … as: The new app isn't as easy as the old one. После than в разговоре — me, him: older than me; официально — than I am. Пишется than, а не then. Такой же — the same as, не the same like.",
     "ex": [
         {"en": "The patient is [older than] he looks.", "ru": "Пациент старше, чем выглядит."},
         {"en": "The generic is [as effective as] the original.", "ru": "Дженерик так же эффективен, как оригинал."},
         {"en": "The new app [isn't as easy as] the old one.", "ru": "Новым приложением пользоваться не так удобно, как старым."},
     ]},
    {"n": 5, "group": "compare", "title": "Насколько: much, slightly, even", "sub": "намного, немного, ещё",
     "rule": "Насколько больше — слово перед -er или more. Намного — much, far, a lot, в статьях significantly: much better, far more effective, significantly lower. Немного — a bit, a little, slightly: slightly higher. Ещё — even: even worse. Very с -er не ставят: very better — ошибка.",
     "ex": [
         {"en": "She's [much better] today.", "ru": "Сегодня ей намного лучше."},
         {"en": "Mortality was [slightly higher] in the older group.", "ru": "В старшей группе смертность была немного выше."},
         {"en": "The traffic is [even worse] than yesterday.", "ru": "Пробки ещё хуже, чем вчера."},
     ]},
    {"n": 6, "group": "compare", "title": "Во сколько раз", "sub": "twice as, three times higher, half",
     "rule": "В два раза — twice as … as: Smokers are twice as likely to have a stroke. Одним словом twice, а не two times. В три раза и больше — three times as … as или three times higher than. Вдвое меньше — half as … as или half the size; twice less — калька. В статьях: a twofold increase — двукратное увеличение.",
     "ex": [
         {"en": "Smokers are [twice as likely] to have a stroke.", "ru": "У курильщиков инсульт случается в два раза чаще."},
         {"en": "The risk was [three times higher] in smokers.", "ru": "У курильщиков риск был в три раза выше."},
         {"en": "The new pump is [half the size] of the old one.", "ru": "Новая помпа вдвое меньше старой."},
     ]},
    {"n": 7, "group": "compare", "title": "Чем…, тем…", "sub": "the earlier, the better · more and more",
     "rule": "Чем…, тем… — the + сравнительная, the + сравнительная: The earlier we treat, the better the outcome. Коротко: the sooner, the better — чем скорее, тем лучше. Всё больше и больше — more and more, всё лучше — better and better: Her speech is getting better and better.",
     "ex": [
         {"en": "[The earlier] we treat, [the better] the outcome.", "ru": "Чем раньше лечим, тем лучше исход."},
         {"en": "Call me back — [the sooner, the better].", "ru": "Перезвоните — чем скорее, тем лучше."},
         {"en": "Her speech is getting [better and better].", "ru": "Её речь становится всё лучше и лучше."},
     ]},
    {"n": 8, "group": "research", "title": "Язык статей", "sub": "compared with, fewer, less, similar to",
     "rule": "По сравнению с — compared with (или compared to): lower compared with placebo. Меньше исчисляемого — fewer: fewer patients, fewer complications; неисчисляемого — less: less bleeding, less time. Похожий на — similar to, не similar with. Отличаться от — different from. Лучше, чем ожидалось — better than expected.",
     "ex": [
         {"en": "Mortality was lower [compared with] placebo.", "ru": "Смертность была ниже по сравнению с плацебо."},
         {"en": "There were [fewer] complications in the surgical group.", "ru": "В хирургической группе было меньше осложнений."},
         {"en": "Our results are [similar to] those of earlier studies.", "ru": "Наши результаты похожи на результаты прежних исследований."},
     ]},
    {"n": 9, "group": "mix", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех тем вперемешку.", "ex": []},
]

def c(id, t, q, ru, opts, a, why, also=None):
    d = {"id": id, "t": t, "q": q, "ru": ru, "opts": opts, "a": a, "why": why}
    if also: d["also"] = also
    return d

CARDS = [
    # 1 · -er или more
    c("c1-cheap", 1, "Generic drugs are ___ than brand-name ones.", "Дженерики дешевле оригинальных препаратов.",
      ["cheaper", "more cheap", "more cheaper"], "cheaper", "Один слог — -er: cheap → cheaper."),
    c("c1-big", 1, "The infarct is ___ than it was yesterday.", "Инфаркт больше, чем был вчера.",
      ["bigger", "biger", "more big"], "bigger", "Короткий гласный + согласный — удвоение: big → bigger."),
    c("c1-easy", 1, "The new form is much ___ to fill in.", "Новую форму заполнять гораздо проще.",
      ["easier", "more easy", "easyer"], "easier", "На -y — -ier: easy → easier."),
    c("c1-early", 1, "We need to start treatment ___.", "Лечение нужно начинать раньше.",
      ["earlier", "more early", "more earlier"], "earlier", "early → earlier."),
    c("c1-effective", 1, "For large vessel occlusion, thrombectomy is ___ than thrombolysis alone.", "При окклюзии крупной артерии тромбэктомия эффективнее, чем один тромболизис.",
      ["more effective", "effectiver", "most effective"], "more effective", "Длинное слово — more: more effective."),
    c("c1-careful", 1, "You need to be ___ with the dose in elderly patients.", "С дозой у пожилых пациентов нужно быть осторожнее.",
      ["more careful", "carefuller", "more carefully"], "more careful", "Два слога не на -y — more: more careful."),
    c("c1-important", 1, "In stroke care, nothing is ___ than time.", "В лечении инсульта нет ничего важнее времени.",
      ["more important", "importanter", "most important"], "more important", "Длинное слово — more important."),

    # 2 · Неправильные
    c("c2-better", 2, "She's feeling much ___ today.", "Сегодня ей намного лучше.",
      ["better", "more good", "gooder"], "better", "good → better → the best."),
    c("c2-worse", 2, "The headache is ___ in the morning.", "По утрам головная боль сильнее.",
      ["worse", "badder", "more bad"], "worse", "bad → worse → the worst."),
    c("c2-worst", 2, "This is the ___ flu season in ten years.", "Это худший сезон гриппа за десять лет.",
      ["worst", "baddest", "most bad"], "worst", "Самый плохой — the worst."),
    c("c2-best", 2, "What's the ___ way to prevent a second stroke?", "Как лучше всего предотвратить повторный инсульт?",
      ["best", "most good", "better"], "best", "Самый хороший — the best."),
    c("c2-further", 2, "We need ___ tests to confirm the diagnosis.", "Для подтверждения диагноза нужны дополнительные анализы.",
      ["further", "farther", "more far"], "further", "Дополнительный — further: further tests."),
    c("c2-less", 2, "Try to eat ___ salt.", "Старайтесь есть меньше соли.",
      ["less", "fewer", "littler"], "less", "little → less; соль неисчисляемая — less."),
    c("c2-least", 2, "This is the ___ expensive option.", "Это самый дешёвый вариант.",
      ["least", "less", "most little"], "least", "Наименее — the least."),

    # 3 · Самый
    c("c3-causes", 3, "Stroke is one of the most common ___ of disability.", "Инсульт — одна из самых частых причин инвалидности.",
      ["causes", "cause", "causing"], "causes", "One of the most + множественное число."),
    c("c3-the", 3, "This is ___ best hospital in the region.", "Это лучшая больница в регионе.",
      ["the", "a", ""], "the", "Превосходная степень — всегда с the."),
    c("c3-in", 3, "She's the best nurse ___ the department.", "Она лучшая медсестра в отделении.",
      ["in", "of", "from"], "in", "Место, коллектив — in."),
    c("c3-of", 3, "She's the youngest ___ the three sisters.", "Она самая младшая из трёх сестёр.",
      ["of", "in", "from"], "of", "Из нескольких — of."),
    c("c3-biggest", 3, "It's the ___ hospital in the city.", "Это самая большая больница в городе.",
      ["biggest", "bigest", "most big"], "biggest", "big → bigger → the biggest."),
    c("c3-most", 3, "This is the ___ important thing to remember.", "Это самое важное, что нужно запомнить.",
      ["most", "more", "best"], "most", "Длинное слово — the most important."),
    c("c3-least", 3, "Choose the ___ invasive option first.", "Сначала выберите наименее инвазивный вариант.",
      ["least", "less", "most little"], "least", "Наименее — the least."),

    # 4 · than, as … as
    c("c4-than", 4, "The patient is older ___ he looks.", "Пациент старше, чем выглядит.",
      ["than", "then", "as"], "than", "Чем — than. Then — «потом»."),
    c("c4-as", 4, "The generic is as effective ___ the original.", "Дженерик так же эффективен, как оригинал.",
      ["as", "than", "like"], "as", "Так же, как — as … as."),
    c("c4-as-form", 4, "This year's results are as ___ as last year's.", "В этом году результаты такие же хорошие, как в прошлом.",
      ["good", "better", "best"], "good", "В as … as — обычная форма: as good as."),
    c("c4-not-as", 4, "The new app isn't ___ easy to use as the old one.", "Новым приложением пользоваться не так удобно, как старым.",
      ["as", "more", "than"], "as", "Не такой, как — not as … as."),
    c("c4-me", 4, "My brother is two years older than ___.", "Мой брат на два года старше меня.",
      ["me", "my", "mine"], "me", "После than в разговоре — me; официально — than I am."),
    c("c4-same", 4, "My results are the same ___ yours.", "Мои результаты такие же, как у вас.",
      ["as", "like", "than"], "as", "Такой же, как — the same as."),
    c("c4-morning", 4, "Blood pressure is often higher in the morning ___ in the evening.", "Давление утром часто выше, чем вечером.",
      ["than", "then", "that"], "than", "Чем — than."),

    # 5 · Насколько
    c("c5-much", 5, "She's ___ better than yesterday.", "Ей гораздо лучше, чем вчера.",
      ["much", "very", "more"], "much", "Намного лучше — much better. Very better — ошибка."),
    c("c5-far", 5, "For large vessel occlusion, thrombectomy is ___ more effective.", "При окклюзии крупной артерии тромбэктомия гораздо эффективнее.",
      ["far", "very", "too"], "far", "Намного — far more effective."),
    c("c5-slightly", 5, "Mortality was ___ higher in the older group.", "В старшей группе смертность была немного выше.",
      ["slightly", "very", "few"], "slightly", "Немного — slightly higher."),
    c("c5-even", 5, "The traffic is ___ worse than yesterday.", "Пробки ещё хуже, чем вчера.",
      ["even", "very", "more"], "even", "Ещё хуже — even worse."),
    c("c5-significantly", 5, "Blood pressure was ___ lower in the treatment group.", "В группе лечения давление было значительно ниже.",
      ["significantly", "very", "most"], "significantly", "Значительно — significantly lower."),
    c("c5-bit", 5, "Could you speak a ___ more slowly, please?", "Не могли бы вы говорить чуть медленнее?",
      ["bit", "few", "very"], "bit", "Чуть-чуть — a bit."),
    c("c5-lot", 5, "The new ward is a ___ bigger than the old one.", "Новое отделение намного больше старого.",
      ["lot", "many", "very"], "lot", "Намного — a lot bigger."),

    # 6 · Во сколько раз
    c("c6-twice", 6, "Smokers are ___ as likely to have a stroke.", "У курильщиков инсульт случается в два раза чаще.",
      ["twice", "two times", "double"], "twice", "В два раза — twice as … as."),
    c("c6-as", 6, "Men are twice as likely ___ women to have this condition.", "У мужчин это заболевание встречается в два раза чаще, чем у женщин.",
      ["as", "than", "that"], "as", "twice as likely as."),
    c("c6-three", 6, "The new drug is three times ___ expensive as the old one.", "Новый препарат в три раза дороже старого.",
      ["as", "more", "so"], "as", "three times as expensive as."),
    c("c6-higher", 6, "The risk was three times ___ in smokers.", "У курильщиков риск был в три раза выше.",
      ["higher", "high", "highest"], "higher", "three times higher."),
    c("c6-half", 6, "The new pump is ___ the size of the old one.", "Новая помпа вдвое меньше старой.",
      ["half", "twice less", "two times less"], "half", "Вдвое меньше — half the size. Twice less — калька."),
    c("c6-twofold", 6, "The study showed a ___ increase in risk.", "Исследование показало двукратное увеличение риска.",
      ["twofold", "twice", "two times"], "twofold", "Двукратное — twofold."),

    # 7 · Чем…, тем…
    c("c7-earlier", 7, "The ___ we treat, the better the outcome.", "Чем раньше мы лечим, тем лучше исход.",
      ["earlier", "early", "earliest"], "earlier", "the + сравнительная: the earlier."),
    c("c7-the", 7, "The earlier we treat, ___ better the outcome.", "Чем раньше лечим, тем лучше исход.",
      ["the", "so", "more"], "the", "Чем…, тем… — the …, the …"),
    c("c7-sooner", 7, "Call me back — the sooner, the ___.", "Перезвоните — чем скорее, тем лучше.",
      ["better", "good", "best"], "better", "Чем скорее, тем лучше — the sooner, the better."),
    c("c7-more", 7, "The ___ you practise, the easier it gets.", "Чем больше практикуешься, тем проще.",
      ["more", "most", "much"], "more", "Чем больше — the more."),
    c("c7-and", 7, "Life is getting more and ___ expensive.", "Жизнь становится всё дороже.",
      ["more", "most", "much"], "more", "Всё больше и больше — more and more."),
    c("c7-speech", 7, "Her speech is getting better and ___ every day.", "Её речь с каждым днём всё лучше.",
      ["better", "best", "good"], "better", "Всё лучше — better and better."),

    # 8 · Язык статей
    c("c8-compared", 8, "Mortality was lower ___ with placebo.", "Смертность была ниже по сравнению с плацебо.",
      ["compared", "comparing", "comparison"], "compared", "По сравнению с — compared with."),
    c("c8-fewer", 8, "There were ___ complications in the surgical group.", "В хирургической группе было меньше осложнений.",
      ["fewer", "less", "little"], "fewer", "Исчисляемые — fewer."),
    c("c8-less", 8, "The new drug caused ___ bleeding.", "Новый препарат вызывал меньше кровотечений.",
      ["less", "fewer", "littler"], "less", "Неисчисляемое — less: less bleeding."),
    c("c8-similar", 8, "Our results are similar ___ those of earlier studies.", "Наши результаты похожи на результаты прежних исследований.",
      ["to", "with", "as"], "to", "Похожий на — similar to."),
    c("c8-different", 8, "This case is very different ___ the others.", "Этот случай сильно отличается от остальных.",
      ["from", "of", "with"], "from", "Отличаться от — different from."),
    c("c8-patients", 8, "___ patients smoke these days than twenty years ago.", "Сейчас курит меньше пациентов, чем двадцать лет назад.",
      ["fewer", "less", "little"], "fewer", "Пациенты исчисляемые — fewer."),
    c("c8-expected", 8, "The response to treatment was better ___ expected.", "Ответ на лечение был лучше, чем ожидалось.",
      ["than", "as", "that"], "than", "Лучше, чем ожидалось — better than expected."),
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
