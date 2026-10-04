# Содержание приложения «Сокращения»: карточки для заучивания (english-flashcards).
# Лицевая сторона — сокращение; оборот — расшифровка (буквы-источники оранжевым), перевод,
# транскрипция, часть речи с артиклем, пример уровня B2 и заметка.
import re

MIXED_TOPIC = 7

GROUPS = {
    "med": "Медицина и наука",
    "world": "Работа и мир",
    "life": "Быт и переписка",
    "mix": "Итог",
}

TOPICS = [
    {"n": 1, "group": "med", "title": "В больнице", "sub": "CT, MRI, ICU, GP…",
     "rule": "Больничные сокращения почти все читаются по буквам, ударение — на последней: CT, MRI, ICU. Артикль — по первому звуку: an MRI, an ECG, an IV, но a CT scan, a GP, a TIA. Неотложка в Британии — A&E, в Америке — the ER."},
    {"n": 2, "group": "med", "title": "Наука и статьи", "sub": "RCT, CI, et al., e.g.…",
     "rule": "В статьях сокращения стоят рядом с цифрами: OR 1.8, HR 0.75, 95% CI, mean ± SD. Латинские — e.g., i.e., etc., et al., vs — вслух обычно заменяют словами: for example, that is, and so on."},
    {"n": 3, "group": "world", "title": "Работа и бизнес", "sub": "NDA, CEO, ASAP, FYI…",
     "rule": "Рабочие сокращения чаще пишут, чем произносят: FYI, TBC, AOB, OOO — в письмах и повестках. ASAP в письме начальнику звучит резко — вежливее as soon as you can."},
    {"n": 4, "group": "world", "title": "Организации и страны", "sub": "FBI, UN, WHO, NATO…",
     "rule": "Название читается по буквам — нужен the: the FBI, the UN, the UK, the USA. Читается как слово — без артикля: NATO, NASA, UNESCO. Перед другим существительным артикль выбирают по звуку: an FBI agent, a UN report."},
    {"n": 5, "group": "life", "title": "На каждый день", "sub": "ATM, ID, PIN, a.m.…",
     "rule": "PIN и SIM читаются как слова, остальные — по буквам. a.m. — до полудня, p.m. — после: 8 a.m. — 8 утра, 8 p.m. — 8 вечера. In the morning после a.m. не добавляют."},
    {"n": 6, "group": "life", "title": "Переписка", "sub": "BTW, LOL, IMO…",
     "rule": "Только для чатов и сообщений знакомым — в рабочих письмах их лучше не писать. Вслух их почти не произносят: говорят всю фразу — by the way, to be honest."},
    {"n": 7, "group": "mix", "title": "Всё вместе", "sub": "15 случайных карточек",
     "rule": "Карточки из всех тем вперемешку."},
]

# Частые ошибки: неверно | верно | пояснение
ERRORS = [
    ["a MRI", "an MRI", "M читается /em/ — гласный звук"],
    ["an UN report", "a UN report", "U читается /juː/ — в начале звук [j]"],
    ["a FBI agent", "an FBI agent", "F читается /ef/ — гласный звук"],
    ["two CT's", "two CTs", "множественное число — без апострофа"],
    ["I live in USA.", "I live in the USA.", "название по буквам — с the"],
    ["He works in FBI.", "He works for the FBI.", "работать в организации — work for, и с the"],
    ["Finland joined the NATO.", "Finland joined NATO.", "название словом — без the"],
    ["the only option, e.g. surgery", "the only option, i.e. surgery", "единственный вариант — i.e.; один пример из многих — e.g."],
    ["at 8 a.m. in the morning", "at 8 a.m.", "a.m. уже значит «утра»"],
    ["tests, scans and etc.", "tests, scans, etc.", "et и так значит and"],
]

# Трудные буквы: буква | транскрипция | что озвучить
LETTERS = [
    ["A", "/eɪ/", "A. A and E."], ["E", "/iː/", "E. E C G."], ["I", "/aɪ/", "I. I C U."],
    ["U", "/juː/", "U. U K."], ["Y", "/waɪ/", "Y. D I Y."], ["G", "/dʒiː/", "G. G P."],
    ["J", "/dʒeɪ/", "J."], ["H", "/eɪtʃ/", "H. H R."], ["R", "/ɑː/", "R. R C T."], ["Z", "/zed/", "Z."],
]

# ——— Чтение по буквам: транскрипция и текст для озвучки
LIPA = dict(A="eɪ", B="biː", C="siː", D="diː", E="iː", F="ef", G="dʒiː", H="eɪtʃ", I="aɪ", J="dʒeɪ",
            K="keɪ", L="el", M="em", N="en", O="əʊ", P="piː", Q="kjuː", R="ɑː", S="es", T="tiː",
            U="juː", V="viː", W="dʌbljuː", X="eks", Y="waɪ", Z="zed")
VOWEL_START = set("AEFHILMNORSX")      # названия этих букв начинаются с гласного звука → an

def letters(ab):
    return [ch for ch in ab.upper() if ch.isalpha()]

def letters_ipa(ab):
    ls = letters(ab)
    parts = []
    for i, ch in enumerate(ls):
        p = LIPA[ch]
        if ch == "R" and i + 1 < len(ls) and ls[i + 1] in VOWEL_START:
            p = "ɑːr"                  # связующее r перед гласным
        parts.append(p)
    parts[0] = "ˌ" + parts[0]
    parts[-1] = "ˈ" + parts[-1]
    return "/" + " ".join(parts) + "/"

# ——— Буквы-источники в расшифровке: [x] — оранжевым
FUNC = {"of", "and", "the", "to", "for", "in", "on", "a", "an", "by", "at"}

def mark_initials(full, ab):
    if "[" in full:
        return full
    ls = letters(ab)
    toks = re.split(r"(\s+|-)", full)
    words = [i for i, t in enumerate(toks) if t.strip() and t != "-"]
    norm = lambda w: re.sub(r"[^a-z']", "", w.lower())

    def solve(li, wi):
        if li == len(ls):
            return [] if all(norm(toks[w]) in FUNC for w in words[wi:]) else None
        if wi == len(words):
            return None
        w = toks[words[wi]]
        first = re.sub(r"^[^A-Za-z]+", "", w)[:1].upper()
        if first == ls[li]:
            r = solve(li + 1, wi + 1)
            if r is not None:
                return [words[wi]] + r
        if norm(w) in FUNC:
            return solve(li, wi + 1)
        return None

    hit = solve(0, 0)
    if not hit:
        return full
    for i in hit:
        w = toks[i]
        k = len(w) - len(re.sub(r"^[^A-Za-z]+", "", w))
        toks[i] = w[:k] + "[" + w[k] + "]" + w[k + 1:]
    return "".join(toks)

def mark_ex(ex, ab):
    if "[" in ex:
        return ex
    for a in [ab] + [p.strip() for p in ab.split("/")]:
        m = re.search(r"(?<![\w&.])" + re.escape(a) + r"(?![\w&])", ex)
        if m:
            return ex[:m.start()] + "[" + a + "]" + ex[m.end():]
    raise AssertionError("no abbreviation in example: " + ex)

CARDS = []

def c(id, t, ab, full, ru, gram, ex, ex_ru, note="", ipa=None, say=None, say_l=None, ex_say=None, ctx=None):
    CARDS.append(dict(id=id, t=t, ab=ab, full=full, ru=ru, gram=gram, ex=ex, ex_ru=ex_ru, note=note,
                      ipa=ipa, say=say, say_l=say_l, ex_say=ex_say, ctx=ctx))

# 1 · В больнице
c("h-ct", 1, "CT", "computed tomography", "компьютерная томография, КТ", "сущ. (C+U) · a CT scan",
  "A non-contrast CT ruled out haemorrhage.", "Бесконтрастная КТ исключила кровоизлияние.",
  "a CT scan — C /siː/, согласный звук. «На КТ» — on CT.")
c("h-mri", 1, "MRI", "magnetic resonance imaging", "магнитно-резонансная томография, МРТ", "сущ. (C+U) · an MRI",
  "The MRI showed a small infarct in the left thalamus.", "На МРТ — небольшой инфаркт в левом таламусе.",
  "an MRI — M /em/, гласный звук.")
c("h-ecg", 1, "ECG", "[e]lectro[c]ardio[g]ram", "ЭКГ, электрокардиограмма", "сущ. (C) · an ECG",
  "His ECG showed atrial fibrillation.", "На ЭКГ у него фибрилляция предсердий.",
  "Амер. — EKG. an ECG — E /iː/, гласный звук.")
c("h-eeg", 1, "EEG", "[e]lectro[e]ncephalo[g]ram", "ЭЭГ, электроэнцефалограмма", "сущ. (C) · an EEG",
  "The EEG showed no seizure activity.", "На ЭЭГ нет эпилептической активности.",
  "Две E подряд: /ˌiː iː ˈdʒiː/.")
c("h-icu", 1, "ICU", "intensive care unit", "отделение реанимации, ОРИТ", "сущ. (C) · the ICU",
  "She was transferred to the ICU after the operation.", "После операции её перевели в реанимацию.",
  "in the ICU — в реанимации. an ICU nurse — I /aɪ/, гласный звук.")
c("h-ae", 1, "A&E", "accident and emergency", "приёмное отделение, неотложка (брит.)", "сущ. (U) · без артикля",
  "He spent six hours waiting in A&E.", "Он шесть часов ждал в приёмном отделении.",
  "Брит.: go to A&E. Амер. — the ER.", ipa="/ˌeɪ ənd ˈiː/", say="A and E")
c("h-er", 1, "ER", "emergency room", "отделение неотложной помощи (амер.)", "сущ. (C) · the ER",
  "She was rushed to the ER with chest pain.", "Её срочно доставили в неотложку с болью в груди.",
  "Брит. — A&E. В документах часто ED — emergency department.")
c("h-gp", 1, "GP", "general practitioner", "врач общей практики, терапевт", "сущ. (C) · a GP",
  "Please make an appointment with your GP in two weeks.", "Запишитесь к своему терапевту через две недели.",
  "see your GP — сходить к своему врачу. G /dʒiː/, согласный звук.")
c("h-bp", 1, "BP", "blood pressure", "артериальное давление", "сущ. (U) · BP",
  "Her BP was 180 over 100 on admission.", "При поступлении давление было 180 на 100.",
  "180/100 читают «180 over 100».", ctx="BP 180/100")
c("h-iv", 1, "IV", "[i]ntra[v]enous", "внутривенно; капельница", "прил., нареч.; сущ. (C) · an IV",
  "The antibiotic was given IV.", "Антибиотик вводили внутривенно.",
  "an IV — капельница или катетер. I /aɪ/, гласный звук.")
c("h-cpr", 1, "CPR", "[c]ardio[p]ulmonary [r]esuscitation", "сердечно-лёгочная реанимация, СЛР", "сущ. (U) · CPR",
  "Bystanders started CPR before the ambulance arrived.", "Прохожие начали СЛР до приезда скорой.",
  "perform CPR, do CPR — без артикля.")
c("h-dnr", 1, "DNR", "do not resuscitate", "не реанимировать", "прил. · a DNR order",
  "The patient has a DNR order in his notes.", "В истории болезни пациента есть распоряжение не реанимировать.",
  "a DNR order — распоряжение не проводить СЛР.")
c("h-tia", 1, "TIA", "transient ischaemic attack", "транзиторная ишемическая атака, ТИА", "сущ. (C) · a TIA",
  "A TIA is often a warning sign of a stroke.", "ТИА часто предвещает инсульт.",
  "Брит. ischaemic, амер. ischemic.")
c("h-bmi", 1, "BMI", "body mass index", "индекс массы тела, ИМТ", "сущ. (C) · a BMI of 32",
  "Patients with a BMI over 40 were excluded.", "Пациентов с ИМТ больше 40 исключали.",
  "a BMI of 32 — ИМТ 32. B /biː/, согласный звук.")
c("h-mi", 1, "MI", "myocardial infarction", "инфаркт миокарда", "сущ. (C) · an MI",
  "He had an MI five years ago.", "Пять лет назад он перенёс инфаркт миокарда.",
  "С пациентом говорят heart attack.")
c("h-dvt", 1, "DVT", "deep vein thrombosis", "тромбоз глубоких вен, ТГВ", "сущ. (C+U) · a DVT",
  "Long flights increase the risk of DVT.", "Долгие перелёты повышают риск тромбоза глубоких вен.",
  "a DVT — один эпизод тромбоза; risk of DVT — без артикля.")

# 2 · Наука и статьи
c("s-rct", 2, "RCT", "randomised controlled trial", "рандомизированное контролируемое исследование, РКИ", "сущ. (C) · an RCT",
  "We conducted an RCT in 12 stroke centres.", "Мы провели РКИ в 12 инсультных центрах.",
  "an RCT — R /ɑː/, гласный звук. Амер. randomized.")
c("s-ci", 2, "CI", "confidence interval", "доверительный интервал, ДИ", "сущ. (C) · a 95% CI",
  "The 95% CI was wide because the sample was small.", "95% ДИ получился широким: выборка была маленькой.",
  "95% CI читают «ninety-five per cent C I».", ctx="95% CI")
c("s-or", 2, "OR", "odds ratio", "отношение шансов, ОШ", "сущ. (C) · an OR of 1.8",
  "The OR for stroke in smokers was 1.8.", "ОШ инсульта у курильщиков составило 1,8.",
  "В американской больнице OR — ещё и operating room, операционная.", ctx="OR 1.8")
c("s-hr", 2, "HR", "hazard ratio", "отношение рисков, ОР", "сущ. (C) · an HR of 0.75",
  "The HR for death in the treatment group was 0.75.", "ОР смерти в группе лечения — 0,75.",
  "an HR — H /eɪtʃ/, гласный звук. На работе HR — отдел кадров.", ctx="HR 0.75")
c("s-sd", 2, "SD", "standard deviation", "стандартное отклонение", "сущ. (C) · mean ± SD",
  "The mean age was 67, with an SD of 11.", "Средний возраст — 67 лет, стандартное отклонение — 11.",
  "an SD — S /es/, гласный звук.", ctx="mean ± SD")
c("s-nnt", 2, "NNT", "number needed to treat", "число больных, которых нужно пролечить, ЧБНЛ", "сущ. (C) · an NNT of 5",
  "An NNT of 5 means we treat five patients to help one.", "ЧБНЛ = 5: лечим пятерых, чтобы помочь одному.",
  "an NNT — N /en/, гласный звук.")
c("s-phd", 2, "PhD", "Doctor of Philosophy", "степень PhD (≈ кандидат наук)", "сущ. (C) · a PhD",
  "She's doing a PhD in neuroscience.", "Она пишет диссертацию по нейронаукам.",
  "От лат. Philosophiae Doctor. do a PhD — учиться в аспирантуре.")
c("s-etal", 2, "et al.", "[et al]ii — and others", "и соавторы, и др.", "лат. · после фамилии",
  "Smith et al. reported similar results.", "Смит и соавт. получили похожие результаты.",
  "Точка — после al, не после et.", ipa="/et ˈæl/", say="et al", say_l="Et al. And others.")
c("s-eg", 2, "e.g.", "[e]xempli [g]ratia — for example", "например", "лат. · вводное",
  "Some risk factors, e.g. smoking, can be changed.", "Некоторые факторы риска, например курение, можно изменить.",
  "Вслух — for example. e.g. — один пример из многих.", say="E G", say_l="E G. For example.")
c("s-ie", 2, "i.e.", "[i]d [e]st — that is", "то есть", "лат. · вводное",
  "The drug is taken once daily, i.e. every 24 hours.", "Препарат принимают раз в сутки, то есть каждые 24 часа.",
  "Вслух — that is. i.e. уточняет: другого варианта нет.", say="I E", say_l="I E. That is.",
  ex_say="The drug is taken once daily, that is, every 24 hours.")
c("s-etc", 2, "etc.", "[et c]etera — and so on", "и так далее, и т. д.", "лат. · в конце списка",
  "Bring your passport, test results, etc.", "Возьмите паспорт, результаты анализов и т. д.",
  "Не пиши and etc.: et уже значит and.", ipa="/et ˈsetərə/", say="et cetera", say_l="Et cetera. And so on.")
c("s-vs", 2, "vs", "[v]er[s]us", "против; в сравнении с", "лат. · предлог",
  "Stroke unit vs general ward: which is better?", "Инсультное отделение или обычная палата: что лучше?",
  "Брит. vs, амер. vs. — с точкой.", ipa="/ˈvɜːsəs/", say="versus", say_l="Versus. Against, or compared with.")
c("s-nb", 2, "NB", "[n]ota [b]ene — note well", "обратите внимание", "лат. · в заметках",
  "NB: reduce the dose in renal failure.", "NB: при почечной недостаточности дозу снижают.",
  "Пишут в инструкциях и конспектах, вслух почти не говорят.", say_l="N B. Note well.")

# 3 · Работа и бизнес
c("w-nda", 3, "NDA", "non-disclosure agreement", "соглашение о неразглашении", "сущ. (C) · an NDA",
  "All the investigators had to sign an NDA.", "Все исследователи должны были подписать соглашение о неразглашении.",
  "an NDA — N /en/, гласный звук.")
c("w-ceo", 3, "CEO", "chief executive officer", "генеральный директор", "сущ. (C) · the CEO",
  "The hospital's new CEO used to be a surgeon.", "Новый директор больницы раньше был хирургом.",
  "Мн. ч. — CEOs, без апострофа.")
c("w-cv", 3, "CV", "curriculum vitae", "резюме", "сущ. (C) · a CV",
  "Please send your CV and a cover letter.", "Пришлите, пожалуйста, резюме и сопроводительное письмо.",
  "Амер. — résumé. Лат. «ход жизни».")
c("w-hr", 3, "HR", "human resources", "отдел кадров, HR", "сущ. (U) · HR",
  "Send your sick note to HR.", "Отправьте больничный в отдел кадров.",
  "an HR manager — H /eɪtʃ/, гласный звук.")
c("w-pr", 3, "PR", "public relations", "связи с общественностью, пиар", "сущ. (U) · PR",
  "The scandal was a PR disaster for the clinic.", "Скандал стал для клиники пиар-катастрофой.",
  "a PR disaster — P /piː/, согласный звук.")
c("w-asap", 3, "ASAP", "as soon as possible", "как можно скорее", "нареч.",
  "Please send me the results ASAP.", "Пришлите мне результаты как можно скорее.",
  "Читают по буквам или словом /ˈeɪsæp/. Начальнику вежливее — as soon as you can.")
c("w-fyi", 3, "FYI", "for your information", "к вашему сведению", "фраза · в письмах",
  "FYI, the meeting has moved to 3 p.m.", "К сведению: встречу перенесли на 15:00.",
  "Пишут в начале короткого письма или пересылки.")
c("w-eta", 3, "ETA", "estimated time of arrival", "ожидаемое время прибытия", "сущ. (C) · an ETA",
  "The ambulance's ETA is ten minutes.", "Скорая будет примерно через десять минут.",
  "What's your ETA? — Когда будешь?")
c("w-tbc", 3, "TBC", "to be confirmed", "уточняется, будет подтверждено", "прил. · после сущ.",
  "The date of the next meeting is TBC.", "Дата следующего совещания уточняется.",
  "Похожее: TBA — to be announced, «будет объявлено».")
c("w-rsvp", 3, "RSVP", "[r]épondez [s]'il [v]ous [p]laît — please reply", "просьба ответить", "глаг. · в приглашениях",
  "Please RSVP by Friday.", "Пожалуйста, ответьте до пятницы, придёте ли вы.",
  "Из французского. Стоит в конце приглашения.", say_l="R S V P. Please reply.")
c("w-kpi", 3, "KPI", "key performance indicator", "ключевой показатель эффективности, KPI", "сущ. (C) · a KPI",
  "Door-to-needle time is an important KPI for stroke units.", "Время «от двери до иглы» — важный KPI инсультного отделения.",
  "a KPI — K /keɪ/, согласный звук.")
c("w-cc", 3, "cc", "carbon copy", "копия письма", "глаг.; сущ. (C)",
  "Could you cc me on your reply?", "Поставь меня, пожалуйста, в копию ответа.",
  "bcc — скрытая копия. Прош. вр. — cc'd.")
c("w-ps", 3, "PS", "[p]ost[s]cript", "постскриптум, P. S.", "сущ. (C)",
  "PS: don't forget to bring the consent forms.", "P. S. Не забудьте принести формы согласия.",
  "Брит. чаще PS без точек, амер. — P.S.", say_l="P S. Postscript.")
c("w-qa", 3, "Q&A", "questions and answers", "вопросы и ответы", "сущ. (C+U) · a Q&A session",
  "There will be a short Q&A after the talk.", "После доклада будет короткая сессия вопросов и ответов.",
  "a Q&A — Q /kjuː/, согласный звук.", ipa="/ˌkjuː ənd ˈeɪ/", say="Q and A")
c("w-aob", 3, "AOB", "any other business", "разное (последний пункт повестки)", "сущ. (U)",
  "The last item on the agenda is AOB.", "Последний пункт повестки — разное.",
  "Брит. В конце совещания: Any other business?")
c("w-ooo", 3, "OOO", "out of office", "нет на месте, в отъезде", "фраза · в автоответе",
  "I'm OOO until Monday with limited access to email.", "Меня не будет до понедельника, почту смотрю редко.",
  "Вслух — out of office. Автоответ — an out-of-office reply.")

# 4 · Организации и страны
c("o-fbi", 4, "FBI", "Federal Bureau of Investigation", "ФБР", "название · the FBI",
  "He worked for the FBI for twenty years.", "Он двадцать лет проработал в ФБР.",
  "an FBI agent — F /ef/, гласный звук.")
c("o-cia", 4, "CIA", "Central Intelligence Agency", "ЦРУ", "название · the CIA",
  "The CIA gathers intelligence outside the US.", "ЦРУ собирает разведданные за пределами США.",
  "a CIA officer — C /siː/, согласный звук.")
c("o-un", 4, "UN", "United Nations", "ООН", "название · the UN",
  "The UN was founded in 1945.", "ООН основали в 1945 году.",
  "a UN report — U /juː/, в начале звук [j].")
c("o-eu", 4, "EU", "European Union", "Евросоюз, ЕС", "название · the EU",
  "Poland joined the EU in 2004.", "Польша вступила в ЕС в 2004 году.",
  "an EU country — E /iː/, гласный звук.")
c("o-who", 4, "WHO", "World Health Organization", "ВОЗ", "название · the WHO",
  "The WHO declared COVID-19 a pandemic in 2020.", "ВОЗ объявила COVID-19 пандемией в 2020 году.",
  "По буквам — не как who. Сама ВОЗ пишет без артикля: WHO recommends…")
c("o-nato", 4, "NATO", "North Atlantic Treaty Organization", "НАТО", "название · без артикля",
  "NATO was founded in 1949.", "НАТО основали в 1949 году.",
  "Читается как слово, поэтому без the.", ipa="/ˈneɪtəʊ/", say="Nato")
c("o-nasa", 4, "NASA", "National Aeronautics and Space Administration", "НАСА", "название · без артикля",
  "NASA first landed astronauts on the Moon in 1969.", "НАСА впервые высадило астронавтов на Луну в 1969 году.",
  "Как слово — без the: work for NASA.", ipa="/ˈnæsə/", say="Nasa")
c("o-nhs", 4, "NHS", "National Health Service", "государственное здравоохранение Великобритании", "название · the NHS",
  "Most NHS treatment is free at the point of use.", "Большая часть лечения в NHS для пациента бесплатна.",
  "on the NHS — за счёт государства. an NHS hospital — N /en/.")
c("o-bbc", 4, "BBC", "British Broadcasting Corporation", "Би-би-си", "название · the BBC",
  "I listen to the BBC every morning to practise my English.", "Каждое утро слушаю Би-би-си, чтобы тренировать английский.",
  "a BBC journalist — B /biː/, согласный звук.")
c("o-uk", 4, "UK", "United Kingdom", "Великобритания", "название · the UK",
  "She moved to the UK to work as a doctor.", "Она переехала в Великобританию работать врачом.",
  "a UK citizen — U /juː/, в начале звук [j].")
c("o-usa", 4, "USA", "United States of America", "США", "название · the USA",
  "He did his residency in the USA.", "Он проходил ординатуру в США.",
  "Чаще просто the US. Всегда с the.")
c("o-unesco", 4, "UNESCO", "United Nations Educational, Scientific and Cultural Organization", "ЮНЕСКО", "название · без артикля",
  "The old town is a UNESCO World Heritage Site.", "Старый город — объект всемирного наследия ЮНЕСКО.",
  "Как слово /juːˈneskəʊ/: в начале звук [j], поэтому a UNESCO site.", ipa="/juːˈneskəʊ/", say="Unesco")

# 5 · На каждый день
c("d-atm", 5, "ATM", "automated teller machine", "банкомат", "сущ. (C) · an ATM",
  "Is there an ATM near the hospital?", "Рядом с больницей есть банкомат?",
  "Брит. в речи — cash machine.")
c("d-id", 5, "ID", "[id]entification", "удостоверение личности, документ", "сущ. (C+U) · an ID card",
  "Please bring some photo ID with you.", "Возьмите с собой документ с фотографией.",
  "some ID — какой-нибудь документ. an ID card — I /aɪ/, гласный звук.")
c("d-pin", 5, "PIN", "personal identification number", "ПИН-код", "сущ. (C) · a PIN",
  "Never tell anyone your PIN.", "Никому не говорите свой ПИН-код.",
  "Читается как слово /pɪn/, поэтому a PIN.", ipa="/pɪn/", say="pin")
c("d-diy", 5, "DIY", "do it yourself", "ремонт своими руками", "сущ. (U); прил. · a DIY store",
  "He spends his weekends doing DIY.", "Выходные он проводит за ремонтом своими руками.",
  "a DIY store — строительный магазин.")
c("d-vip", 5, "VIP", "very important person", "важная персона, VIP", "сущ. (C) · a VIP",
  "The minister was treated like a VIP.", "С министром обращались как с VIP-гостем.",
  "Читается по буквам, не «вип».")
c("d-gps", 5, "GPS", "Global Positioning System", "спутниковая навигация, GPS", "сущ. (U) · by GPS",
  "The ambulance found us using GPS.", "Скорая нашла нас по GPS.",
  "Навигатор в машине — satnav (брит.) или GPS.")
c("d-ai", 5, "AI", "artificial intelligence", "искусственный интеллект, ИИ", "сущ. (U) · an AI tool",
  "AI can help radiologists read CT scans faster.", "ИИ помогает рентгенологам быстрее читать КТ.",
  "an AI tool — A /eɪ/, гласный звук.")
c("d-dob", 5, "DOB", "date of birth", "дата рождения", "сущ. (C)",
  "Please check the patient's name and DOB.", "Проверьте имя пациента и дату рождения.",
  "В анкетах. Вслух — date of birth.")
c("d-ampm", 5, "a.m. / p.m.", "[a]nte [m]eridiem · [p]ost [m]eridiem", "до полудня · после полудня", "нареч. · после числа",
  "The ward round starts at 8 a.m.", "Обход начинается в 8 утра.",
  "12 p.m. — полдень, 12 a.m. — полночь. «8 a.m. in the morning» — ошибка.",
  ipa="/ˌeɪ ˈem/ · /ˌpiː ˈem/", say="A M. P M.", say_l="A M: before noon. P M: after noon.")
c("d-na", 5, "n/a", "not applicable", "не применимо; нет данных", "в анкетах и таблицах",
  "If a question doesn't apply to you, write n/a.", "Если вопрос вас не касается, напишите n/a.",
  "Ещё not available — «нет данных, нет в наличии».")
c("d-sim", 5, "SIM", "subscriber identity module", "SIM-карта", "сущ. (C) · a SIM card",
  "I need a local SIM card for my trip.", "Мне нужна местная SIM-карта для поездки.",
  "Читается как слово /sɪm/.", ipa="/sɪm/", say="sim")
c("d-it", 5, "IT", "information technology", "ИТ, информационные технологии", "сущ. (U) · the IT department",
  "Call IT if the system goes down again.", "Звоните айтишникам, если система снова упадёт.",
  "IT specialist — без дефиса. an IT problem — I /aɪ/.")

# 6 · Переписка
c("c-btw", 6, "BTW", "by the way", "кстати", "фраза · в чатах",
  "BTW, did you get my email about the rota?", "Кстати, ты получил моё письмо про график дежурств?",
  "Вслух — by the way.")
c("c-lol", 6, "LOL", "laughing out loud", "очень смешно, «ржу»", "межд. · в чатах",
  "He replied “LOL” to my serious question.", "На мой серьёзный вопрос он ответил «LOL».",
  "Читают по буквам или словом /lɒl/. Не для рабочих писем.")
c("c-imo", 6, "IMO", "in my opinion", "по-моему", "фраза · в чатах",
  "IMO, the new protocol is too complicated.", "По-моему, новый протокол слишком сложный.",
  "IMHO — in my humble opinion, «по моему скромному мнению».")
c("c-tbh", 6, "TBH", "to be honest", "честно говоря", "фраза · в чатах",
  "TBH, I didn't read the whole paper.", "Честно говоря, я не прочитал статью целиком.",
  "Вслух — to be honest.")
c("c-idk", 6, "IDK", "I don't know", "не знаю", "фраза · в чатах",
  "IDK if I can make it to the meeting.", "Не знаю, успею ли на встречу.",
  "Вслух — I don't know.")
c("c-omg", 6, "OMG", "oh my God", "о боже", "межд. · в чатах",
  "OMG, I forgot my badge again!", "О боже, я опять забыл пропуск!",
  "Вслух чаще целиком: oh my God.")
c("c-dm", 6, "DM", "direct message", "личное сообщение, «личка»", "сущ. (C); глаг.",
  "DM me the details.", "Скинь подробности в личку.",
  "Прош. вр. — DMed или DM'd.")
c("c-brb", 6, "BRB", "be right back", "сейчас вернусь", "фраза · в чатах",
  "BRB, my pager is going off.", "Сейчас вернусь — пейджер пищит.",
  "Вслух — be right back.")

# ——— Озвучка
WORD_READ = {"NATO": "Nato", "NASA": "Nasa", "UNESCO": "Unesco", "PIN": "pin", "SIM": "sim"}
EX_SPOKEN = {"A&E": "A and E", "Q&A": "Q and A", "e.g.": "for example", "i.e.": "that is", "etc.": "et cetera",
             "vs": "versus", "a.m.": "A M", "p.m.": "P M", "et al.": "et al", "n/a": "N A", "US": "U S",
             "PhD": "P H D", "cc": "C C", "OOO": "out of office", "BTW": "by the way", "IMO": "in my opinion",
             "TBH": "to be honest", "IDK": "I don't know", "OMG": "oh my God", "BRB": "be right back"}
EX_SPOKEN.update(WORD_READ)

def spaced(ab):
    return " ".join(letters(ab))

for k in CARDS:
    ab = k["ab"]
    if k["say"] is None:
        k["say"] = WORD_READ.get(ab, spaced(ab))
    if k["ipa"] is None:
        k["ipa"] = letters_ipa(ab)
    if ab not in EX_SPOKEN and ab not in WORD_READ and re.fullmatch(r"[A-Za-z]+", ab):
        EX_SPOKEN[ab] = spaced(ab)

TOKEN = re.compile(r"A&E|Q&A|e\.g\.|i\.e\.|etc\.|et al\.|a\.m\.|p\.m\.|n/a|[A-Za-z]+")

def spoken(text):
    s = TOKEN.sub(lambda m: EX_SPOKEN.get(m.group(0), m.group(0)), text)
    s = s.replace("“", "").replace("”", "").replace("«", "").replace("»", "")
    s = s[:1].upper() + s[1:]
    return s if s.rstrip()[-1:] in ".!?" else s + "."

def plain(s):
    return re.sub(r"[\[\]]", "", s)

for k in CARDS:
    k["full"] = mark_initials(k["full"], k["ab"])
    k["ex_mark"] = mark_ex(k["ex"], k["ab"])
    if k["say_l"] is None:
        f = plain(k["full"])
        k["say_l"] = k["say"] + ". " + f[:1].upper() + f[1:] + "."
        k["say_l"] = k["say_l"][:1].upper() + k["say_l"][1:]
    if k["ex_say"] is None:
        k["ex_say"] = spoken(k["ex"])

# ——— Проверки
ids = [k["id"] for k in CARDS]
assert len(ids) == len(set(ids))
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))
for k in CARDS:
    assert "[" in k["full"] or k["id"] == "s-phd", ("нет подсветки", k["id"], k["full"])
    assert k["ex_mark"].count("[") == 1, k["id"]
    for f in ("ru", "gram", "ex_ru", "note"):
        assert k[f] and "  " not in k[f], (k["id"], f)

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
    for k in CARDS:
        print(f'{k["ab"]:12} {k["ipa"]:24} {k["full"]}')
        print(f'{"":12} a: {k["say"]} | l: {k["say_l"]} | e: {k["ex_say"]}')
