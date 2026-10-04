# Сборка «Английский»: берёт 46 готовых тренажёров, готовит их к запуску внутри общего приложения.
# Выход: build/apps/<key>.html, build/catalog.json, build/audio_src.json
import json, pathlib, re, hashlib

S = pathlib.Path(__file__).resolve().parent.parent          # scratchpad
OUT = S / "eng" / "build"
PHRASAL = S / "artifact-files" / "17f35b77-ec05-4e16-a5e6-516e7ef5f8d8"
BB = S / "artifact-files" / "63c4fa4f-95e7-4be6-812a-689d838c98c5"

GROUPS = [
    ("core", "Главные ошибки и артикли"),
    ("verbs", "Времена и формы глагола"),
    ("modal", "Модальные глаголы"),
    ("toing", "To, -ing и управление"),
    ("preps", "Предлоги"),
    ("words", "Слова, которые путают"),
    ("text", "Вопросы, связки, пересказ"),
    ("vocab", "Лексика и живая речь"),
]

# ключ, группа, описание (одна строка в каталоге), старый артефакт (для переноса прогресса)
APPS = [
    ("top10", "core", "Артикли, Present Perfect, вопросы без do — ошибки, которые слышно сразу", "K69HCgVa2bPQqwS39mB67t"),
    ("artikli", "core", "a, the или ничего: выбор в три вопроса", "L7mF5LyphncY6dYb6rFYLV"),
    ("bez-a-an", "core", "advice, information, news и ещё четыре слова без a/an", "E8zrNy587phQs8V4AnCfGH"),
    ("countable", "core", "Исчисляемые и неисчисляемые: much, many, a piece of", "7p2trKuntYiYHFFht3aP8M"),
    ("tenses", "verbs", "Simple или Continuous, Past или Perfect, for и since, будущее", "LwysVBLu9nbuy8hi2TTysn"),
    ("irreg", "verbs", "Неправильные глаголы по семьям: said, made, won", "2wZxUjAd3dqormy613inBC"),
    ("passive", "verbs", "is done, was done, has been done, I was told", "BMMR6JAQoRH2UANKB2grFG"),
    ("gonebeen", "verbs", "Ушёл и его нет — или сходил и вернулся", "TpzwsRS4PN5aBj612ofbHm"),
    ("stative", "verbs", "know, want, have: когда -ing не ставят", "FxxDgkD68cLvACK9dR75Km"),
    ("usedto", "verbs", "used to, would, be used to, get used to", "Um8143NVWrv7fsbHTgmixo"),
    ("would", "verbs", "Просьбы, «бы», будущее в прошлом, wouldn't", "4SqvyEJvbTWLVCzBBU4Nqm"),
    ("cond", "verbs", "Условные 0–3, смешанные, unless, I wish", "8MakAF7dtZANMUaqPqLhzF"),
    ("hsd", "verbs", "have it done, get it done: «сделать МРТ»", "NqSPUdPakSpXBw9DAzq9Ts"),
    ("modal", "modal", "Надо, нельзя, не обязательно, надо было", "75TukFzzYZ9qmmLioY3JbV"),
    ("can", "modal", "Умею, смог, удалось: can, could, be able to", "RpUJMmgNA78Nz5mKxKDJVn"),
    ("manage", "modal", "manage to, succeed in, cope with, make it", "TfDd2SmBZKYd8XUaYoPjf9"),
    ("toing", "toing", "to do или doing: suggest, remember, stop, try", "4r8EFyRvyBZbkuPgidTpWH"),
    ("vm", "toing", "remember, forget, regret, try, stop + to или -ing", "5nxyZUnM2tPsR8xSdjhhF8"),
    ("prepi", "toing", "despite, instead of, without + -ing", "JBjwLwY9aWBjZLM5cUrX9L"),
    ("kogo", "toing", "want you to do, suggest, recommend, advise", "LC1oQmGKXtGvC6827YFtAQ"),
    ("preps", "preps", "at, on, in: время и место", "DEFxpbMfK6HGQVFRVRJTfo"),
    ("into", "preps", "in или into, on или onto, транспорт", "N5EjqA8RUzawPZWJw4CqCU"),
    ("tofor", "preps", "to или for: кому и для кого, explain to", "Dhhtdnas9q7QbbRSJa5pN5"),
    ("adjprep", "preps", "good at, afraid of, interested in", "WLjfGBLTPFmg3s4dsCHLk8"),
    ("makedo", "words", "make или do — и когда ни то ни другое", "5tHxqGUy2g5NKbv24DWB6h"),
    ("htp", "words", "have lunch, take a risk, pay attention", "9WyaDqx5eoZbo5FU4LEdt2"),
    ("go", "words", "go home, go shopping, go numb, go on", "2xHkw4wMchsVf3cWudiq9K"),
    ("life", "words", "life, live, alive, living, lively", "L9N4smKfkuqrdjwfdkpW6x"),
    ("twotoo", "words", "two, too или to — и too, very, enough", "S11yRpnwTFRquYiS2MxcSk"),
    ("thereit", "words", "there is или it is", "LUfgrmPSVBux3fdfXpURde"),
    ("pron", "words", "I, me, my, mine, myself; its или it's", "DSWt6FXsEmBxtWHajX9xz4"),
    ("adjadv", "words", "Какой или как: good и well, hard и hardly", "FWq6kgKnenk4Bjz5sEbtz2"),
    ("cmp", "words", "-er или more, than, as … as, в два раза", "UQC9ay4ZtJTA36VxELaFqi"),
    ("similar", "words", "see, look, watch; say, tell; learn, study", "HPjMVRe4W71zMJLNcnbbAQ"),
    ("pairs", "words", "Похожие слова-ловушки: на работе, в еде, в жизни", "6nLfEBKaYGUEBJ81P4ALC7"),
    ("syn", "words", "close и shut, big и large, win и beat, earn и gain", "6ZoY6F5dKWgokaPipRsk82"),
    ("q", "text", "do, does, did, вопросы при осмотре и анамнез", "QfawWPDcbQwtaCNo3nubbM"),
    ("rel", "text", "who, which, that, whose — и когда без них", "FbjaKDen6wcQKAZY85QVzE"),
    ("link", "text", "although, however, therefore, in order to", "K1YDMHQ3Xd93i61vkrHHiH"),
    ("rep", "text", "say или tell, сдвиг времён, пересказ в истории болезни", "KtwWhLBLGHNvjxqk52SxuY"),
    ("num", "text", "increase by, fewer и less, twice as, per cent", "VRMYwiyRiTecPM9qtn3Xrj"),
    ("phrasal", "vocab", "Новый глагол каждый день: rule out, follow up, set in", "3xY7RH7Hvw6oKXMR8uwVuH"),
    ("bbapp", "vocab", "Две фразы в день из сериала, американский голос", "DKZLKdvSrzKtQLdUtK7rUL"),
    ("idm", "vocab", "a piece of cake, break the ice — идиомы B2", "7ZEdgP775jds7SZ4Jk7K2a"),
    ("wthr", "vocab", "Жара, дождь, туман, ветер — погода по-английски", "17sYKQAN4tHLa9swGQ9GXn"),
    ("abbr", "vocab", "Сокращения в больнице, статьях и переписке", "Nv7gk9mhp4bmmWsGuSpfGE"),
]

# Английские и привычные названия — для поиска (и подписи старых плиток на экране «Домой»)
EN = {
    "top10": "top 10 mistakes 10 ошибок", "artikli": "articles a an the артикли", "bez-a-an": "uncountable a an advice information news без a/an",
    "countable": "countable uncountable исчисляемые неисчисляемые much many штуки масса", "tenses": "tenses present past perfect continuous future времена",
    "irreg": "irregular verbs неправильные", "passive": "passive voice пассив", "gonebeen": "gone been", "stative": "stative verbs состояния",
    "usedto": "used to would get used to", "would": "would", "cond": "conditionals if условные", "hsd": "causative have something done get it done",
    "modal": "modal verbs must have to should модальные", "can": "can could be able to", "manage": "manage to succeed cope",
    "toing": "gerund infinitive to -ing герундий инфинитив", "vm": "remember forget regret try stop gerund infinitive", "prepi": "preposition -ing gerund despite instead of",
    "kogo": "verb object infinitive want someone to do", "preps": "prepositions at on in time place предлоги", "into": "in into on onto prepositions предлоги",
    "tofor": "to for prepositions предлоги", "adjprep": "adjectives prepositions good at afraid of предлоги", "makedo": "make do",
    "htp": "have take pay", "go": "go phrases", "life": "life live alive", "twotoo": "two too to", "thereit": "there it",
    "pron": "pronouns my mine possessive местоимения", "adjadv": "adjectives adverbs adj adv -ly", "cmp": "comparatives superlatives comparison сравнительная степень",
    "similar": "confusing words see look watch say tell", "pairs": "confusing words pairs", "syn": "synonyms",
    "q": "questions", "rel": "relative clauses who which that", "link": "linking words connectors although however",
    "rep": "reported speech indirect speech косвенная речь", "num": "numbers statistics percent числа проценты", "phrasal": "phrasal verbs фразовые",
    "bbapp": "breaking bad фразы сериал", "idm": "idioms идиомы", "wthr": "weather погода", "abbr": "abbreviations сокращения",
}
TITLE = {"countable": "Countable и uncountable"}
DESC = {"countable": "Штуки и масса: much, many, a piece of, advice"}

DECKS = {"phrasal", "bbapp"}          # пополняются каждый день задачами по расписанию

def source(key):
    if key == "bez-a-an":
        return (S / "bez-a-an.html").read_text(), S / "audio", S / "audio" / "clips.json"
    if key == "phrasal":
        s = (PHRASAL / "index.html").read_text()
        return unwrap(s), PHRASAL / "audio", None
    if key == "bbapp":
        s = (BB / "index.html").read_text()
        return unwrap(s), BB / "audio" / "us", None
    return (S / key / "index.html").read_text(), S / key / "audio", S / key / "clips.json"

def unwrap(s):
    i = s.index("<body>") + len("<body>")
    body = s[i:]
    body = re.sub(r"\s*</body></html>\s*$", "\n", body)
    assert "<body>" not in body and "</html>" not in body
    return body.lstrip("\n")

def js_array_span(s, start):
    """Позиции [ и ] массива, начинающегося с первой [ после start; учитывает строки и комментарии."""
    i = s.index("[", start); depth = 0; j = i; q = None
    while j < len(s):
        ch = s[j]
        if q:
            if ch == "\\": j += 2; continue
            if ch == q: q = None
        elif ch in "\"'`": q = ch
        elif ch == "/" and s[j + 1] == "/": j = s.index("\n", j); continue
        elif ch == "/" and s[j + 1] == "*": j = s.index("*/", j) + 2; continue
        elif ch == "[": depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0: return i, j
        j += 1
    raise ValueError("unterminated array")

def card_ids(s):
    a, b = js_array_span(s, s.index("const CARDS"))
    seg = s[a:b]
    # только id карточек верхнего уровня: объект начинается на глубине 1
    ids = []; depth = 0; j = 0; q = None; objstart = None
    while j < len(seg):
        ch = seg[j]
        if q:
            if ch == "\\": j += 2; continue
            if ch == q: q = None
        elif ch in "\"'`": q = ch
        elif ch == "/" and seg[j + 1] == "/": j = seg.index("\n", j); continue
        elif ch in "[{":
            depth += 1
            if ch == "{" and depth == 2: objstart = j
        elif ch in "]}":
            if ch == "}" and depth == 2:
                obj = seg[objstart:j + 1]
                m = re.search(r'(?:^|[{,\s])"?id"?\s*:\s*"([^"]+)"', obj)
                assert m, obj[:80]
                ids.append(m.group(1))
            depth -= 1
        j += 1
    return ids

def deck_items(s):
    a, b = js_array_span(s, s.index("const CARDS"))
    seg = s[a:b]
    out = []
    for m in re.finditer(r'\{\s*id:\s*"([^"]+)"(.*?)\n  \}', seg, re.S):
        body = m.group(2)
        f = lambda k: (re.search(r'\b' + k + r':\s*"([^"]*)"', body) or [None, ""])[1]
        ru = f("ru").split(" — ")[0].split(". ")[0].rstrip(".")
        out.append({"id": m.group(1), "term": f("term"), "ru": ru, "added": f("added")})
    return out

def keywords(s):
    """Названия тем тренажёра — для поиска в каталоге."""
    if "const TOPICS" not in s: return []
    a, b = js_array_span(s, s.index("const TOPICS"))
    return re.findall(r'"title":\s*"([^"]+)"', s[a:b])

PRELUDE = '<script>(function(){try{var B=window.parent&&window.parent.__eng;if(B&&B.attach)B.attach(%s,window)}catch(e){}})();</script>'
MERGE = ('\n(window.__EXTRA_CARDS||[]).forEach(function(c){if(c&&c.id&&!CARDS.some(function(x){return x.id===c.id}))CARDS.push(c)});\n')

catalog = []; audio_src = {}
titles = {}
for key, group, desc, old in APPS:
    s, adir, clips = source(key)
    title = re.search(r"<title>([^<]*)</title>", s).group(1)
    ids = card_ids(s)
    ls_state = re.search(r'const LS_STATE = "([^"]+)"', s).group(1)
    kw = keywords(s)
    assert len(ids) == len(set(ids)), (key, "дубли id")
    # 1) значки для «Домой» внутри общего приложения не нужны
    s, n_ic = re.subn(r'"data:image/png;base64,[A-Za-z0-9+/=]+"', '""', s)
    assert n_ic == 2, (key, n_ic)
    # 2) мост к общему приложению — до всех скриптов тренажёра
    assert s.startswith("<title>"), key
    s = s.replace("</title>", "</title>\n" + PRELUDE % json.dumps(key), 1)
    # 3) колоды, которые пополняются каждый день: новые карточки приходят из базы общего приложения
    if key in DECKS:
        mk = "// НОВАЯ КАРТОЧКА ВСТАВЛЯЕТСЯ ВЫШЕ ЭТОЙ СТРОКИ\n];\n"
        assert s.count(mk) == 1, key
        s = s.replace(mk, mk + MERGE, 1)
    # проверки: одинаковые пути хранения и звука, без которых мост не сработает
    if key in DECKS:
        assert 'const DOC_PATH = "progress/main";' in s, key
    else:
        assert s.count('db.doc("data/users/" + uid + "/progress")') == 1, key
    assert s.count("new Audio(") == 1, key
    (OUT / "apps" / f"{key}.html").write_text(s)
    # звук: все записи этого тренажёра
    files = sorted(p for p in adir.glob("*.mp3"))
    assert files, key
    audio_src[key] = {p.stem: str(p) for p in files}
    item = {"key": key, "title": TITLE.get(key, title), "group": group, "desc": DESC.get(key, desc), "old": old, "ids": ids, "ls": ls_state, "en": EN[key],
            "kw": " · ".join(kw), "voice": "Andrew" if key == "bbapp" else "Ryan", "size": len(s.encode())}
    if key in DECKS:
        item["deck"] = True
        item["items"] = deck_items(s)
        assert [x["id"] for x in item["items"]] == ids, key
        item["kw"] = " · ".join(x["term"] for x in item["items"])
    catalog.append(item)
    titles[key] = title

assert len(catalog) == 46 and len({c["key"] for c in catalog}) == 46
(OUT / "catalog.json").write_text(json.dumps({"groups": GROUPS, "apps": catalog}, ensure_ascii=False))
(OUT / "audio_src.json").write_text(json.dumps(audio_src, ensure_ascii=False))
tot = sum(c["size"] for c in catalog)
print("ok", len(catalog), "apps;", sum(len(c["ids"]) for c in catalog), "cards;", sum(len(v) for v in audio_src.values()), "clips; html", tot)
for c in catalog: print(f'  {c["key"]:9} {len(c["ids"]):4} cards {len(audio_src[c["key"]]):4} clips  {c["title"]}')
