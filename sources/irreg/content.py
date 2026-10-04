# Содержание приложения «Неправильные глаголы».
# Глаголы собраны в семьи: те, что меняются одинаково, учатся вместе.
# В примерах: {…} — вторая форма (синий), _…_ — третья форма (оранжевый); [ ] — транскрипция.
import re

MIXED_TOPIC = 21

GROUPS = {
    "aaa": "A — A — A · не меняются",
    "abb": "A — B — B · вторая = третья",
    "aba": "A — B — A · третья = первая",
    "abc": "A — B — C · все три разные",
    "sent": "В предложениях",
}

# Четыре схемы: схема | что это | пример (v1, v2, v3) | группа
SCHEMES = [
    ["A — A — A", "все три одинаковые", ["cut", "cut", "cut"], "aaa"],
    ["A — B — B", "вторая = третья", ["buy", "bought", "bought"], "abb"],
    ["A — B — A", "третья = первая", ["come", "came", "come"], "aba"],
    ["A — B — C", "все три разные", ["begin", "began", "begun"], "abc"],
]

# Семьи: номер, группа, название, пример для заголовка, правило, короткая подсказка для карточек
FAMILIES = [
    {"n": 1, "group": "aaa", "title": "Не меняются", "ex": ["cut", "cut", "cut"],
     "rule": "Все три формы одинаковые. Почти все такие глаголы короткие и кончаются на t или d: put, cut, hit, set, spread. Read пишется так же, но звучит [riːd] — [red] — [red].",
     "hint": "Не меняется: все три формы одинаковые."},
    {"n": 2, "group": "abb", "title": "-ought / -aught", "ex": ["buy", "bought", "bought"],
     "rule": "Вторая и третья рифмуются: [ɔːt], как в слове «сорт». Пишется -ought: bought, brought, thought, fought, sought. Если в глаголе есть буква a — пишем -aught: catch → caught, teach → taught.",
     "hint": "Звук [ɔːt]: bought, brought, thought, fought, sought; если в глаголе есть a — caught, taught."},
    {"n": 3, "group": "abb", "title": "d → t", "ex": ["send", "sent", "sent"],
     "rule": "Последняя d меняется на t: send → sent, spend → spent, build → built. На слух легко спутать, поэтому говори чётко: I sent it yesterday, а не I send.",
     "hint": "d меняется на t: sent, spent, built, lent, bent."},
    {"n": 4, "group": "abb", "title": "Долгое [iː] → короткое [e]", "ex": ["keep", "kept", "kept"],
     "rule": "Долгое [iː] становится коротким [e], часто с t на конце: keep → kept, sleep → slept, feel → felt, mean → meant. Если глагол кончается на d или t, просто укорачиваем: meet → met, lead → led, bleed → bled. Отдельно: leave → left, flee → fled.",
     "hint": "Долгое [iː] стало коротким [e]: kept, slept, felt, met, led, bled."},
    {"n": 5, "group": "abb", "title": "+ d: said, made, heard", "ex": ["say", "said", "said"],
     "rule": "Прибавляется d. У say, pay, lay пишется -aid: said, paid, laid (не sayed). Said звучит [sed], heard — [hɜːd], не как hear. Make → made, have → had.",
     "hint": "Прибавляем d: said, paid, laid, made, had, heard."},
    {"n": 6, "group": "abb", "title": "-old · -ood · -ound", "ex": ["tell", "told", "told"],
     "rule": "Три маленькие рифмы: tell, sell → told, sold; stand, understand → stood, understood; find → found.",
     "hint": "Рифмы: told, sold · stood, understood · found."},
    {"n": 7, "group": "abb", "title": "Звук [ʌ]: won, stuck", "ex": ["win", "won", "won"],
     "rule": "Во второй и третьей — короткий звук [ʌ], как в слове cup: won [wʌn], stuck, hung, dug, struck, spun.",
     "hint": "Вторая и третья со звуком [ʌ]: won, stuck, hung, dug, struck, spun."},
    {"n": 8, "group": "abb", "title": "Просто запомнить", "ex": ["get", "got", "got"],
     "rule": "Общей рифмы нет — просто запомни пять пар: get — got, lose — lost, sit — sat, hold — held, shoot — shot. Вторая и третья у них одинаковые.",
     "hint": "Вторая = третья: got, lost, sat, held, shot."},
    {"n": 9, "group": "abb", "title": "Британское -t", "ex": ["learn", "learnt", "learnt"],
     "rule": "В британском английском можно и -t, и -ed: learnt или learned, burnt или burned. В американском почти всегда -ed. Оба варианта правильные — выбирай любой.",
     "hint": "Можно -t или -ed: оба варианта правильные."},
    {"n": 10, "group": "aba", "title": "Третья = первая", "ex": ["come", "came", "come"],
     "rule": "Третья форма совпадает с первой: come — came — come, run — ran — run. Так же все глаголы с -come: become, overcome. Частая ошибка: has came — правильно has come.",
     "hint": "Третья = первая: come — came — come, run — ran — run."},
    {"n": 11, "group": "abc", "title": "i — a — u", "ex": ["begin", "began", "begun"],
     "rule": "Гласная идёт как «и — а — у»: begin — began — begun, drink — drank — drunk. С a — прошлое (вчера began), с u — после have (have begun).",
     "hint": "i → a → u: с a — прошлое, с u — после have."},
    {"n": 12, "group": "abc", "title": "-ew — -wn", "ex": ["know", "knew", "known"],
     "rule": "Вторая — на -ew, третья — первая + n: know — knew — known, grow — grew — grown, draw — drew — drawn. Fly — flew — flown. Show стоит особняком: showed — shown.",
     "hint": "Вторая на -ew, третья = первая + n: knew — known, grew — grown."},
    {"n": 13, "group": "abc", "title": "Вторая + en", "ex": ["break", "broke", "broken"],
     "rule": "Во второй — звук «о», а третья — это вторая + en: broke → broken, spoke → spoken, chose → chosen, woke → woken. У forget удваиваем t: forgot → forgotten.",
     "hint": "Вторая с «о», третья = вторая + en: broke → broken, spoke → spoken."},
    {"n": 14, "group": "abc", "title": "[aɪ] — o — i + en", "ex": ["write", "wrote", "written"],
     "rule": "Первая со звуком [aɪ], вторая с «о», третья — короткое i + en: write — wrote — written, drive — drove — driven, rise — rose — risen. У hide и bite вторая короче: hid, bit. После короткого i согласную удваиваем: written, ridden, hidden, bitten.",
     "hint": "[aɪ] → о → короткое i + en: wrote — written, drove — driven."},
    {"n": 15, "group": "abc", "title": "Первая + n", "ex": ["take", "took", "taken"],
     "rule": "Третья = первая + (e)n: take → taken, give → given, eat → eaten, fall → fallen, see → seen. Вторую просто запоминаем: took, gave, ate, fell, saw.",
     "hint": "Третья = первая + n: taken, given, eaten, fallen, seen."},
    {"n": 16, "group": "abc", "title": "-ear — -ore — -orn", "ex": ["wear", "wore", "worn"],
     "rule": "-ear → -ore → -orn: wear — wore — worn, tear — tore — torn. Родиться — be born: I was born in 1985. Blood-borne — передающийся через кровь.",
     "hint": "-ear → -ore → -orn: wore — worn, tore — torn."},
    {"n": 17, "group": "abc", "title": "Особые", "ex": ["go", "went", "gone"],
     "rule": "Их учим наизусть: be — was/were — been, go — went — gone (и undergo так же), do — did — done. Lie (лежать) — lay — lain: не путай с lay — laid (класть). Swell — swelled — swollen: a swollen ankle.",
     "hint": ""},
]

# Глаголы: семья, первая, вторая, третья, перевод; note — строка под глаголом в таблице,
# why — пояснение на карточке (добавляется к подсказке семьи), say — текст для озвучки.
V = []
def verb(t, v1, v2, v3, ru, note="", why="", say=None, opts=None, also=None, card=True):
    V.append({"t": t, "v": v1, "v2": v2, "v3": v3, "ru": ru, "note": note, "why": why,
              "say": say or f"{v1}, {v2.replace(' / ', ', ')}, {v3}.", "opts": opts, "also": also, "card": card})

# 1 · A-A-A
verb(1, "put", "put", "put", "класть, ставить")
verb(1, "cut", "cut", "cut", "резать")
verb(1, "let", "let", "let", "позволять")
verb(1, "set", "set", "set", "ставить, устанавливать", note="set the alarm — поставить будильник",
     why="Sat — это sit (сидеть).", opts=["set — set", "sat — sat", "setted — setted"])
verb(1, "hit", "hit", "hit", "ударять")
verb(1, "hurt", "hurt", "hurt", "ранить; болеть", note="My back hurts — болит спина")
verb(1, "cost", "cost", "cost", "стоить", note="costed — только «рассчитали стоимость»",
     why="Costed — только в смысле «рассчитали стоимость».")
verb(1, "shut", "shut", "shut", "закрывать")
verb(1, "spread", "spread", "spread", "распространяться", opts=["spread — spread", "spreaded — spreaded", "spred — spred"])
verb(1, "read", "read", "read", "читать", note="звучит [riːd] — [red] — [red]", say="reed, red, red.",
     why="Пишется одинаково, но звучит [riːd] — [red] — [red].", opts=["read — read", "readed — readed", "red — red"])
verb(1, "split", "split", "split", "раскалывать, делить")
verb(1, "burst", "burst", "burst", "лопаться, разрываться")
verb(1, "upset", "upset", "upset", "расстраивать")

# 2 · -ought / -aught
verb(2, "buy", "bought", "bought", "покупать", why="Не путай с bring — brought (приносить).",
     opts=["bought — bought", "brought — brought", "buyed — buyed"])
verb(2, "bring", "brought", "brought", "приносить", why="Bought — это buy (покупать).",
     opts=["brought — brought", "bought — bought", "brang — brung"])
verb(2, "think", "thought", "thought", "думать", why="Taught — это teach (учить).",
     opts=["thought — thought", "taught — taught", "thinked — thinked"])
verb(2, "fight", "fought", "fought", "бороться, драться", opts=["fought — fought", "faught — faught", "fighted — fighted"],
     why="В fight нет буквы a — значит, -ought.")
verb(2, "seek", "sought", "sought", "искать", note="seek medical help — обратиться к врачу",
     opts=["sought — sought", "saught — saught", "seeked — seeked"], why="В seek нет буквы a — значит, -ought.")
verb(2, "catch", "caught", "caught", "ловить; подхватить", note="catch a cold — простудиться",
     opts=["caught — caught", "cought — cought", "catched — catched"], why="В catch есть a — значит, -aught.")
verb(2, "teach", "taught", "taught", "учить, преподавать", why="Thought — это think (думать).",
     opts=["taught — taught", "thought — thought", "teached — teached"])

# 3 · d → t
verb(3, "send", "sent", "sent", "отправлять")
verb(3, "spend", "spent", "spent", "тратить; проводить (время)")
verb(3, "build", "built", "built", "строить")
verb(3, "lend", "lent", "lent", "давать взаймы")
verb(3, "bend", "bent", "bent", "сгибать", note="bend your knee — согните колено")

# 4 · долгое [iː] → короткое [e]
verb(4, "feel", "felt", "felt", "чувствовать", why="Fell — fallen — это fall (падать).",
     opts=["felt — felt", "fell — fallen", "feeled — feeled"])
verb(4, "keep", "kept", "kept", "хранить; продолжать", opts=["kept — kept", "keept — keept", "keeped — keeped"])
verb(4, "sleep", "slept", "slept", "спать", opts=["slept — slept", "sleept — sleept", "sleeped — sleeped"])
verb(4, "meet", "met", "met", "встречать")
verb(4, "leave", "left", "left", "уходить; оставлять", why="Lived — это live (жить).",
     opts=["left — left", "lived — lived", "leaved — leaved"])
verb(4, "mean", "meant", "meant", "значить; иметь в виду", note="meant звучит [ment]",
     opts=["meant — meant", "ment — ment", "meaned — meaned"], why="Meant звучит [ment], но пишется через ea.")
verb(4, "lead", "led", "led", "вести; приводить к", note="lead to — приводить к", say="leed, led, led.",
     opts=["led — led", "lead — lead", "leaded — leaded"], why="Led звучит так же, как пишется: [led].")
verb(4, "feed", "fed", "fed", "кормить", note="tube feeding — кормление через зонд")
verb(4, "bleed", "bled", "bled", "кровоточить")
verb(4, "deal", "dealt", "dealt", "иметь дело с", note="deal with — справляться с; dealt [delt]",
     opts=["dealt — dealt", "delt — delt", "dealed — dealed"])
verb(4, "sweep", "swept", "swept", "подметать", opts=["swept — swept", "sweept — sweept", "sweeped — sweeped"])
verb(4, "flee", "fled", "fled", "бежать, спасаться", why="Flew — flown — это fly (летать).",
     opts=["fled — fled", "flew — flown", "fleed — fleed"])

# 5 · + d
verb(5, "say", "said", "said", "сказать", note="said звучит [sed]")
verb(5, "pay", "paid", "paid", "платить")
verb(5, "make", "made", "made", "делать")
verb(5, "have", "had", "had", "иметь")
verb(5, "hear", "heard", "heard", "слышать", note="heard звучит [hɜːd]")
verb(5, "lay", "laid", "laid", "класть, положить", note="не путай с lie — lay — lain (лежать)",
     why="Lay — lain — это lie (лежать).", opts=["laid — laid", "lay — lain", "layed — layed"])

# 6 · -old, -ood, -ound
verb(6, "tell", "told", "told", "сказать (кому-то), рассказать")
verb(6, "sell", "sold", "sold", "продавать")
verb(6, "stand", "stood", "stood", "стоять")
verb(6, "understand", "understood", "understood", "понимать")
verb(6, "find", "found", "found", "находить", note="founded — от found (основывать)",
     why="Founded — это found (основать).", opts=["found — found", "founded — founded", "finded — finded"])

# 7 · звук [ʌ]
verb(7, "win", "won", "won", "выигрывать", note="won звучит [wʌn]")
verb(7, "stick", "stuck", "stuck", "приклеивать; застревать", opts=["stuck — stuck", "stack — stuck", "sticked — sticked"])
verb(7, "hang", "hung", "hung", "вешать, висеть", note="hanged — только «казнили через повешение»",
     why="Hanged — только «казнили через повешение».", opts=["hung — hung", "hanged — hanged", "hang — hung"])
verb(7, "dig", "dug", "dug", "копать", opts=["dug — dug", "dag — dug", "digged — digged"])
verb(7, "strike", "struck", "struck", "ударять, поражать", note="be struck by a car — быть сбитым машиной")
verb(7, "spin", "spun", "spun", "вращать(ся)", note="my head is spinning — голова кружится")

# 8 · просто запомнить
verb(8, "get", "got", "got", "получать; становиться", note="в американском: got — gotten",
     opts=["got — got", "got — gotten", "getted — getted"],
     also={"got — gotten": "это американский вариант, в британском — got"})
verb(8, "lose", "lost", "lost", "терять", note="lose weight — худеть", why="Не путай с loose [luːs] — свободный.",
     opts=["lost — lost", "losed — losed", "lost — losed"])
verb(8, "sit", "sat", "sat", "сидеть", why="Set — это «ставить, устанавливать».",
     opts=["sat — sat", "set — set", "sitted — sitted"])
verb(8, "hold", "held", "held", "держать; проводить", note="hold a meeting — провести совещание")
verb(8, "shoot", "shot", "shot", "стрелять")

# 9 · британское -t (без карточек форм: тренируются в предложениях)
verb(9, "learn", "learnt", "learnt", "учить, узнавать", note="или learned — learned", card=False)
verb(9, "burn", "burnt", "burnt", "жечь, обжечь", note="или burned — burned", card=False)
verb(9, "dream", "dreamt", "dreamt", "видеть сон; мечтать", note="или dreamed; dreamt звучит [dremt]", card=False)
verb(9, "smell", "smelt", "smelt", "пахнуть; нюхать", note="или smelled — smelled", card=False)
verb(9, "spell", "spelt", "spelt", "писать по буквам", note="или spelled — spelled", card=False)
verb(9, "spill", "spilt", "spilt", "проливать", note="или spilled — spilled", card=False)

# 10 · A-B-A
verb(10, "come", "came", "come", "приходить")
verb(10, "become", "became", "become", "становиться")
verb(10, "run", "ran", "run", "бежать; руководить", note="run a clinic — руководить клиникой")
verb(10, "overcome", "overcame", "overcome", "преодолевать", opts=["overcame — overcome", "overcame — overcame", "overcome — overcame"])

# 11 · i — a — u
for v1, v2, v3, ru, note in [
    ("begin", "began", "begun", "начинать", ""),
    ("drink", "drank", "drunk", "пить", ""),
    ("ring", "rang", "rung", "звонить", ""),
    ("sing", "sang", "sung", "петь", ""),
    ("sink", "sank", "sunk", "тонуть", ""),
    ("swim", "swam", "swum", "плавать", ""),
    ("shrink", "shrank", "shrunk", "сжиматься, уменьшаться", "the tumour has shrunk — опухоль уменьшилась"),
]:
    verb(11, v1, v2, v3, ru, note=note, opts=[f"{v2} — {v3}", f"{v3} — {v2}", f"{v2} — {v2}"])

# 12 · -ew — -wn
verb(12, "know", "knew", "known", "знать")
verb(12, "grow", "grew", "grown", "расти")
verb(12, "throw", "threw", "thrown", "бросать")
verb(12, "blow", "blew", "blown", "дуть", note="blow your nose — высморкаться")
verb(12, "fly", "flew", "flown", "летать")
verb(12, "draw", "drew", "drawn", "рисовать; брать (кровь)", note="draw blood — взять кровь")
verb(12, "withdraw", "withdrew", "withdrawn", "отзывать, отменять", note="the drug was withdrawn — препарат отозвали")
verb(12, "show", "showed", "shown", "показывать", note="можно и showed — showed, но shown обычнее",
     why="Show — особняком: вторая правильная, showed.", opts=["showed — shown", "showed — showed", "shown — showed"],
     also={"showed — showed": "так тоже говорят, но shown — обычнее"})

# 13 · вторая + en
verb(13, "break", "broke", "broken", "ломать")
verb(13, "speak", "spoke", "spoken", "говорить")
verb(13, "choose", "chose", "chosen", "выбирать", note="chose [tʃəʊz] — с одной o")
verb(13, "forget", "forgot", "forgotten", "забывать", opts=["forgot — forgotten", "forgot — forgot", "forgotten — forgot"])
verb(13, "wake", "woke", "woken", "будить; просыпаться", opts=["woke — woken", "woke — woke", "woken — woke"])
verb(13, "steal", "stole", "stolen", "красть")
verb(13, "freeze", "froze", "frozen", "замерзать, замораживать", note="frozen shoulder — «замороженное» плечо")

# 14 · [aɪ] — o — i + en
verb(14, "write", "wrote", "written", "писать", opts=["wrote — written", "wrote — writen", "wrote — wrote"],
     why="После короткого i t удваивается: written.")
verb(14, "drive", "drove", "driven", "водить (машину)")
verb(14, "ride", "rode", "ridden", "ездить (верхом, на велосипеде)")
verb(14, "rise", "rose", "risen", "подниматься (само)", note="raise — raised — поднимать что-то",
     why="Raised — от raise: поднимать что-то.", opts=["rose — risen", "raised — raised", "rised — rised"])
verb(14, "arise", "arose", "arisen", "возникать", note="complications arose — возникли осложнения")
verb(14, "hide", "hid", "hidden", "прятать", opts=["hid — hidden", "hid — hiden", "hided — hided"],
     why="После короткого i d удваивается: hidden.")
verb(14, "bite", "bit", "bitten", "кусать")

# 15 · первая + n
verb(15, "take", "took", "taken", "брать")
verb(15, "give", "gave", "given", "давать", opts=["gave — given", "gave — gave", "given — gave"])
verb(15, "see", "saw", "seen", "видеть", opts=["saw — seen", "seen — saw", "saw — saw"])
verb(15, "eat", "ate", "eaten", "есть", note="ate звучит [et] или [eɪt]")
verb(15, "fall", "fell", "fallen", "падать", why="Felt — это feel (чувствовать).",
     opts=["fell — fallen", "felt — felt", "fell — fell"])
verb(15, "shake", "shook", "shaken", "трясти")
verb(15, "forgive", "forgave", "forgiven", "прощать")
verb(15, "mistake", "mistook", "mistaken", "принять за (ошибочно)", note="be mistaken — ошибаться")

# 16 · -ear — -ore — -orn
verb(16, "wear", "wore", "worn", "носить (одежду)")
verb(16, "tear", "tore", "torn", "рвать", note="a torn ligament — разрыв связки", say="tare, tore, torn.",
     opts=["tore — torn", "tore — tore", "torn — tore"])
verb(16, "swear", "swore", "sworn", "клясться; ругаться")
verb(16, "bear", "bore", "borne", "выносить, терпеть", note="be born — родиться; blood-borne — передаётся с кровью",
     why="Родиться — be born: I was born in 1985.")

# 17 · особые
verb(17, "be", "was / were", "been", "быть", note="was — I, he, she, it · were — you, we, they", say="be, was, were, been.",
     why="Was — с I, he, she, it; were — с you, we, they.", opts=["was / were — been", "was — was", "been — been"])
verb(17, "go", "went", "gone", "идти, ехать", note="been to — был и вернулся; gone — ушёл",
     why="Went — прошлое, gone — после have.", opts=["went — gone", "went — went", "gone — went"])
verb(17, "do", "did", "done", "делать", why="Did — прошлое, done — после have и в пассиве.",
     opts=["did — done", "done — did", "did — did"])
verb(17, "lie", "lay", "lain", "лежать", note="lie — lied — lied: лгать",
     why="Laid — от lay (класть), lied — «лгал».", opts=["lay — lain", "laid — laid", "lied — lied"])
verb(17, "swell", "swelled", "swollen", "опухать", note="a swollen ankle — опухшая лодыжка",
     why="«Опухший» — swollen: a swollen ankle.", opts=["swelled — swollen", "swelled — swelled", "swollen — swelled"],
     also={"swelled — swelled": "так тоже можно, но «опухший» — только swollen"})
verb(17, "undergo", "underwent", "undergone", "перенести (операцию)", note="undergo surgery — перенести операцию",
     why="Как go — went — gone.")

VERBS = V

# другие написания — чтобы поиск находил и их
ALT = {"learn": ["learned"], "burn": ["burned"], "dream": ["dreamed"], "smell": ["smelled"], "spell": ["spelled"],
       "spill": ["spilled"], "get": ["gotten"], "hang": ["hanged"], "swell": ["swelled"]}
for v in VERBS:
    if v["v"] in ALT: v["alt"] = ALT[v["v"]]

# ——— Регулярная форма (для неверных вариантов)
SPECIAL_ED = {"begin": "beginned", "upset": "upsetted", "forget": "forgetted", "overcome": "overcomed",
              "undergo": "undergoed", "withdraw": "withdrawed", "understand": "understanded"}
def ed(v):
    if v in SPECIAL_ED: return SPECIAL_ED[v]
    if v.endswith("e"): return v + "d"
    if v.endswith("y") and v[-2] not in "aeiou": return v[:-1] + "ied"
    if re.fullmatch(r"[^aeiou]*[aeiou][^aeiouwxy]", v): return v + v[-1] + "ed"
    return v + "ed"

def scheme(v):
    if v["v"] == v["v2"] == v["v3"]: return "aaa"
    if v["v2"] == v["v3"]: return "abb"
    if v["v3"] == v["v"]: return "aba"
    return "abc"

FAM = {f["n"]: f for f in FAMILIES}

def form_opts(v):
    if v["opts"]: return v["opts"]
    x, y, z, r = v["v"], v["v2"], v["v3"], ed(v["v"])
    s = scheme(v)
    if s == "aaa": return [f"{x} — {x}", f"{r} — {r}", f"{x} — {r}"]
    if s == "abb":
        if v["t"] == 3: return [f"{y} — {y}", f"{x} — {y}", f"{r} — {r}"]      # send — sent: на слух путают
        return [f"{y} — {y}", f"{r} — {r}", f"{y} — {r}"]
    if s == "aba": return [f"{y} — {x}", f"{y} — {y}", f"{r} — {r}"]
    return [f"{y} — {z}", f"{y} — {y}", f"{r} — {r}"]

CARDS = []
for v in VERBS:
    if not v["card"]: continue
    f = FAM[v["t"]]
    a = f"{v['v2']} — {v['v3']}"
    opts = form_opts(v)
    assert a in opts and len(set(opts)) == len(opts), v["v"]
    why = " ".join(s for s in [f["hint"], v["why"]] if s)
    c = {"id": "v-" + v["v"], "t": v["t"], "form": 1, "q": f"{v['v']}\u00a0— ___", "ru": v["ru"],
         "opts": opts, "a": a, "why": why, "say": v["say"]}
    if v["also"]: c["also"] = v["also"]
    CARDS.append(c)

# ——— Предложения
SENT_TOPICS = [
    {"n": 18, "group": "sent", "title": "V2 или V3", "sub": "I saw · I've seen",
     "rule": "Вторая форма — прошлое без помощников: I {saw} him yesterday. Третья — после have (I've _seen_) и в пассиве после be (it was _done_). После did и didn't — снова первая: Did you see? I didn't go.",
     "ex": [
         {"en": "I {saw} him an hour ago.", "ru": "Я видел его час назад."},
         {"en": "I've _seen_ this rash before.", "ru": "Я уже видел такую сыпь."},
         {"en": "The CT was _done_ at 10:40.", "ru": "КТ сделали в 10:40."},
         {"en": "Did you see the results?", "ru": "Ты видел результаты? — после did первая форма."},
     ]},
    {"n": 19, "group": "sent", "title": "Ловушки-пары", "sub": "lie · lay · rise · raise",
     "rule": "Похожие глаголы с разным смыслом: lie — лежать, lay — класть; rise — подниматься самому, raise — поднимать что-то; fall — падать, feel — чувствовать; find — находить, found — основывать; sit — сидеть, set — ставить.",
     "ex": [
         {"en": "He {lay} down on the couch.", "ru": "Он прилёг на кушетку. — lie, лечь"},
         {"en": "She {laid} the baby on the bed.", "ru": "Она положила ребёнка на кровать. — lay, класть"},
         {"en": "His temperature {rose} overnight.", "ru": "Температура поднялась за ночь. — rise, сама"},
         {"en": "We {raised} the head of the bed.", "ru": "Мы подняли изголовье кровати. — raise, что-то"},
     ]},
    {"n": 20, "group": "sent", "title": "В отделении", "sub": "lost · bled · swollen",
     "rule": "Глаголы, без которых не обойтись на работе: lose blood, break a bone, bleed, swell, spread, undergo surgery, withdraw a drug.",
     "ex": [
         {"en": "He has _lost_ a lot of blood.", "ru": "Он потерял много крови."},
         {"en": "She {broke} her hip in a fall.", "ru": "Она сломала шейку бедра при падении."},
         {"en": "He has _undergone_ three operations.", "ru": "Он перенёс три операции."},
         {"en": "The drug was _withdrawn_ in 2004.", "ru": "Препарат отозвали в 2004 году."},
     ]},
    {"n": 21, "group": "sent", "title": "Итог — всё вместе", "sub": "",
     "rule": "15 случайных карточек из всех семей и тем: формы и предложения вперемешку.", "ex": []},
]

S = [
    # 9 · британское -t
    {"id": "bt-learn", "t": 9, "q": "I've ___ a lot from this case.", "ru": "Я многому научился на этом случае.",
     "opts": ["learnt", "learned", "learn"], "a": "learnt", "also": {"learned": "в британском — оба варианта, в американском — learned"},
     "why": "learn — learnt — learnt. После have — третья форма, не learn."},
    {"id": "bt-burn", "t": 9, "q": "He ___ his hand on the kettle.", "ru": "Он обжёг руку о чайник.",
     "opts": ["burnt", "burned", "burn"], "a": "burnt", "also": {"burned": "оба варианта правильные"},
     "why": "burn — burnt — burnt или burned — burned. О прошлом — не burn."},
    {"id": "bt-dream", "t": 9, "q": "Last night I ___ about the exam.", "ru": "Прошлой ночью мне снился экзамен.",
     "opts": ["dreamt", "dreamed", "dream"], "a": "dreamt", "also": {"dreamed": "оба варианта правильные"},
     "why": "dream — dreamt [dremt] — dreamt, или dreamed."},

    # 18 · V2 или V3
    {"id": "s-seen", "t": 18, "q": "Have you ever ___ a case like this?", "ru": "Вы когда-нибудь видели такой случай?",
     "opts": ["seen", "saw"], "a": "seen", "why": "После have — третья форма: have seen."},
    {"id": "s-saw", "t": 18, "q": "I ___ him in the corridor an hour ago.", "ru": "Я видел его в коридоре час назад.",
     "opts": ["saw", "seen"], "a": "saw", "why": "ago — прошлое без have: вторая форма, saw."},
    {"id": "s-written", "t": 18, "q": "The discharge summary was ___ by the resident.", "ru": "Выписку написал ординатор.",
     "opts": ["written", "wrote"], "a": "written", "why": "Пассив: was + третья форма — was written."},
    {"id": "s-wrote", "t": 18, "q": "She ___ the referral letter yesterday.", "ru": "Она написала направление вчера.",
     "opts": ["wrote", "written"], "a": "wrote", "why": "yesterday — прошлое без have: wrote."},
    {"id": "s-gone", "t": 18, "q": "Dr Smith has already ___ home.", "ru": "Доктор Смит уже ушёл домой.",
     "opts": ["gone", "went"], "a": "gone", "why": "has + третья форма: has gone."},
    {"id": "s-went", "t": 18, "q": "He ___ home at six.", "ru": "Он ушёл домой в шесть.",
     "opts": ["went", "gone"], "a": "went", "why": "Точное время в прошлом — вторая форма: went."},
    {"id": "s-come", "t": 18, "q": "The ambulance has just ___.", "ru": "Скорая только что приехала.",
     "opts": ["come", "came"], "a": "come", "why": "has + третья форма. У come третья = первая: come — came — come."},
    {"id": "s-done", "t": 18, "q": "The CT was ___ at 10:40.", "ru": "КТ сделали в 10:40.",
     "opts": ["done", "did"], "a": "done", "why": "Пассив: was + третья форма — was done."},
    {"id": "s-did", "t": 18, "q": "Who ___ the lumbar puncture?", "ru": "Кто делал люмбальную пункцию?",
     "opts": ["did", "done"], "a": "did", "why": "Вопрос о прошлом без have — вторая форма: did."},
    {"id": "s-fallen", "t": 18, "q": "Two patients have ___ out of bed this week.", "ru": "На этой неделе двое пациентов упали с кровати.",
     "opts": ["fallen", "fell"], "a": "fallen", "why": "have + третья форма: have fallen."},
    {"id": "s-given", "t": 18, "q": "The patient was ___ aspirin in the ambulance.", "ru": "Пациенту дали аспирин в скорой.",
     "opts": ["given", "gave"], "a": "given", "why": "Пассив: was + третья форма — was given."},
    {"id": "s-did-see", "t": 18, "q": "Did you ___ the MRI report?", "ru": "Ты видел заключение МРТ?",
     "opts": ["see", "saw", "seen"], "a": "see", "why": "После did — первая форма: did you see. Прошлое уже показывает did."},

    # 19 · ловушки-пары
    {"id": "tr-lay", "t": 19, "q": "The patient ___ down on the couch.", "ru": "Пациент прилёг на кушетку.",
     "opts": ["lay", "laid", "lied"], "a": "lay", "why": "Лечь — lie — lay — lain. Laid — «положил» (lay — laid — laid)."},
    {"id": "tr-laid", "t": 19, "q": "The nurse ___ the patient on his side.", "ru": "Медсестра уложила пациента на бок.",
     "opts": ["laid", "lay", "lied"], "a": "laid", "why": "Положить кого-то — lay — laid — laid."},
    {"id": "tr-lain", "t": 19, "q": "He has ___ in bed for three weeks.", "ru": "Он пролежал в постели три недели.",
     "opts": ["lain", "laid", "lied"], "a": "lain", "why": "Лежать — lie — lay — lain: has lain."},
    {"id": "tr-lied", "t": 19, "q": "He ___ about how much he drinks.", "ru": "Он соврал о том, сколько пьёт.",
     "opts": ["lied", "lay", "laid"], "a": "lied", "why": "Лгать — правильный глагол: lie — lied — lied."},
    {"id": "tr-rose", "t": 19, "q": "His temperature ___ to 39.5 overnight.", "ru": "За ночь температура поднялась до 39,5.",
     "opts": ["rose", "raised", "rised"], "a": "rose", "why": "Поднимается само — rise — rose — risen."},
    {"id": "tr-raised", "t": 19, "q": "We ___ the head of the bed.", "ru": "Мы подняли изголовье кровати.",
     "opts": ["raised", "rose", "risen"], "a": "raised", "why": "Поднимаем что-то — raise, правильный глагол: raised."},
    {"id": "tr-fell", "t": 19, "q": "The old man ___ in the bathroom.", "ru": "Пожилой мужчина упал в ванной.",
     "opts": ["fell", "felt", "fall"], "a": "fell", "why": "Упасть — fall — fell — fallen. Felt — «почувствовал»."},
    {"id": "tr-felt", "t": 19, "q": "She ___ dizzy and sat down.", "ru": "У неё закружилась голова, и она села.",
     "opts": ["felt", "fell", "feeled"], "a": "felt", "why": "Чувствовать — feel — felt — felt."},
    {"id": "tr-founded", "t": 19, "q": "The hospital was ___ in 1890.", "ru": "Больница основана в 1890 году.",
     "opts": ["founded", "found", "finded"], "a": "founded", "why": "Основать — found — founded — founded, правильный глагол."},
    {"id": "tr-found", "t": 19, "q": "We ___ a small aneurysm on the scan.", "ru": "На снимке мы нашли небольшую аневризму.",
     "opts": ["found", "founded", "finded"], "a": "found", "why": "Найти — find — found — found."},
    {"id": "tr-sat", "t": 19, "q": "Her husband ___ by the bed all night.", "ru": "Муж просидел у кровати всю ночь.",
     "opts": ["sat", "set", "sit"], "a": "sat", "why": "Сидеть — sit — sat — sat."},
    {"id": "tr-set", "t": 19, "q": "I've ___ the alarm for 6 a.m.", "ru": "Я поставил будильник на 6 утра.",
     "opts": ["set", "sat", "setted"], "a": "set", "why": "Поставить, установить — set — set — set, не меняется."},

    # 20 · в отделении
    {"id": "w-lost", "t": 20, "q": "He has ___ a lot of blood.", "ru": "Он потерял много крови.",
     "opts": ["lost", "losed", "lose"], "a": "lost", "why": "lose — lost — lost."},
    {"id": "w-broke", "t": 20, "q": "She ___ her hip when she fell.", "ru": "Она сломала шейку бедра, когда упала.",
     "opts": ["broke", "broken", "breaked"], "a": "broke", "why": "Прошлое без have — вторая форма: broke. Broken — после have."},
    {"id": "w-bled", "t": 20, "q": "The wound ___ heavily during the night.", "ru": "Ночью рана сильно кровоточила.",
     "opts": ["bled", "bleeded", "bleed"], "a": "bled", "why": "bleed — bled — bled: долгое [iː] стало коротким."},
    {"id": "w-swollen", "t": 20, "q": "His ankle is badly ___.", "ru": "У него сильно опухла лодыжка.",
     "opts": ["swollen", "swelled", "swell"], "a": "swollen", "why": "«Опухший» — swollen: a swollen ankle, the ankle is swollen."},
    {"id": "w-spread", "t": 20, "q": "The infection has ___ to the bone.", "ru": "Инфекция распространилась на кость.",
     "opts": ["spread", "spreaded", "spred"], "a": "spread", "why": "spread не меняется: spread — spread — spread."},
    {"id": "w-bit", "t": 20, "q": "A dog ___ him on the leg.", "ru": "Собака укусила его за ногу.",
     "opts": ["bit", "bitten", "bited"], "a": "bit", "why": "Прошлое без have — bit. Bitten — после have или was: he was bitten."},
    {"id": "w-undergone", "t": 20, "q": "He has ___ three operations on his knee.", "ru": "Он перенёс три операции на колене.",
     "opts": ["undergone", "underwent", "undergoed"], "a": "undergone", "why": "has + третья форма: undergone — как go — went — gone."},
    {"id": "w-chose", "t": 20, "q": "In the end, she ___ to have the operation.", "ru": "В итоге она решила оперироваться.",
     "opts": ["chose", "chosen", "choosed"], "a": "chose", "why": "Прошлое — chose; chosen — после have."},
    {"id": "w-slept", "t": 20, "q": "He hasn't ___ for two nights because of the pain.", "ru": "Он не спит уже две ночи из-за боли.",
     "opts": ["slept", "sleeped", "sleep"], "a": "slept", "why": "has + третья форма: slept."},
    {"id": "w-showed", "t": 20, "q": "The MRI ___ a small infarct in the pons.", "ru": "МРТ показала небольшой инфаркт в мосту.",
     "opts": ["showed", "shown", "show"], "a": "showed", "why": "Прошлое — showed; shown — после have или was."},
    {"id": "w-struck", "t": 20, "q": "He was ___ by a car on his way home.", "ru": "По дороге домой его сбила машина.",
     "opts": ["struck", "striked", "strike"], "a": "struck", "why": "strike — struck — struck; пассив: was struck."},
    {"id": "w-withdrawn", "t": 20, "q": "The drug was ___ from the market in 2004.", "ru": "Препарат отозвали с рынка в 2004 году.",
     "opts": ["withdrawn", "withdrew", "withdrawed"], "a": "withdrawn", "why": "Пассив: was + третья форма — withdrawn, как draw — drew — drawn."},
]
for c in S:
    assert c["a"] in c["opts"] and c["q"].count("___") == 1, c["id"]
CARDS += S

TOPICS = []
for f in FAMILIES:
    TOPICS.append({"n": f["n"], "kind": "fam", "group": f["group"], "title": f["title"], "exv": f["ex"], "rule": f["rule"]})
for t in SENT_TOPICS:
    TOPICS.append({"n": t["n"], "kind": "sent", "group": t["group"], "title": t["title"], "sub": t["sub"], "rule": t["rule"], "ex": t["ex"]})
# «сверх основы»: предложения вступают, когда часть форм уже пройдена
LATE = {9: 0.25, 18: 0.2, 19: 0.3, 20: 0.25}
for t in TOPICS:
    if t["n"] in LATE: t["late"] = LATE[t["n"]]

# Как угадать третью форму: ключ | пояснение (с пометками)
HINTS = [
    ["Кончается на -n?", "Чаще всего это первая + n: take → _taken_, give → _given_, know → _known_, see → _seen_."],
    ["…или вторая + en", "broke → _broken_, spoke → _spoken_, chose → _chosen_, forgot → _forgotten_."],
    ["Короткий, на t или d?", "Часто вообще не меняется: cut, put, hit, set, spread."],
    ["Звук [ɔːt]", "Пишется -ought: _bought_, _thought_, _brought_. Если в глаголе есть a — -aught: catch → _caught_, teach → _taught_."],
    ["Долгое [iː]", "Становится коротким [e]: keep → _kept_, feel → _felt_, meet → _met_, bleed → _bled_."],
]

# Ловушки-пары: группы строк (v1, v2, v3, перевод)
TRAPS = [
    [("lie", "lay", "lain", "лежать, лечь"), ("lay", "laid", "laid", "класть, положить"), ("lie", "lied", "lied", "лгать")],
    [("rise", "rose", "risen", "подниматься (само)"), ("raise", "raised", "raised", "поднимать (что-то)")],
    [("fall", "fell", "fallen", "падать"), ("feel", "felt", "felt", "чувствовать")],
    [("find", "found", "found", "находить"), ("found", "founded", "founded", "основывать")],
    [("sit", "sat", "sat", "сидеть"), ("set", "set", "set", "ставить, устанавливать")],
    [("leave", "left", "left", "уходить, оставлять"), ("live", "lived", "lived", "жить")],
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["I have saw him.", "I have seen him.", "после have — третья форма"],
    ["He has went home.", "He has gone home.", "go — went — gone"],
    ["Did you saw the scan?", "Did you see the scan?", "после did — первая форма"],
    ["The CT was did.", "The CT was done.", "пассив: was + третья форма"],
    ["She has came.", "She has come.", "come — came — come"],
    ["He lied down.", "He lay down.", "лечь — lie — lay — lain"],
    ["His pressure raised.", "His pressure rose.", "поднялось само — rise — rose"],
    ["I was borned in 1980.", "I was born in 1980.", "родиться — be born"],
]

if __name__ == "__main__":
    from collections import Counter
    print(len(VERBS), "verbs;", len(CARDS), "cards;", Counter(scheme(v) for v in VERBS))
    print(Counter(c["t"] for c in CARDS))
