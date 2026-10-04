# Содержание приложения «Идиомы»: карточки для заучивания (english-flashcards).
# Лицевая сторона — идиома; оборот — пометка (разг., брит.), буквальная картинка, значение по-английски,
# русский аналог, заметка об употреблении, пример уровня B2 с переводом.
import re

MIXED_TOPIC = 9

GROUPS = {
    "sit": "Ситуации",
    "work": "Решения и работа",
    "people": "Люди",
    "every": "Деньги и разговор",
    "mix": "Итог",
}

TOPICS = [
    {"n": 1, "group": "sit", "title": "Легко и трудно", "sub": "a piece of cake, the last straw…",
     "rule": "Как сказать, что дело лёгкое, трудное или вышло из-под контроля. Главная пара: a piece of cake — «проще простого» и easier said than done — «легко сказать»."},
    {"n": 2, "group": "sit", "title": "Время", "sub": "once in a blue moon, from scratch…",
     "rule": "Редко, круглосуточно, в последний момент, с нуля. Многие из этих идиом нейтральны — их можно сказать и на работе: around the clock, in the long run, a race against time."},
    {"n": 3, "group": "work", "title": "Решения и риски", "sub": "make up your mind, a long shot…",
     "rule": "Решиться, колебаться, рискнуть или перестраховаться. В идиомах с your местоимение меняется по смыслу: make up her mind, the ball is in their court."},
    {"n": 4, "group": "work", "title": "Работа и учёба", "sub": "hit the nail on the head, learn the ropes…",
     "rule": "Идиомы для отделения и совещаний: попасть в точку, халтурить, освоиться, быть в курсе. Большинство нейтральны и звучат нормально в рабочей речи."},
    {"n": 5, "group": "people", "title": "Люди и отношения", "sub": "break the ice, see eye to eye…",
     "rule": "Знакомство, согласие, секреты и шутки. Someone в идиоме заменяют нужным словом: pull my leg, give him the benefit of the doubt."},
    {"n": 6, "group": "people", "title": "Здоровье и чувства", "sub": "under the weather, on the mend…",
     "rule": "Как сказать о самочувствии и настроении — пригодится и с пациентами: under the weather — приболел, on the mend — идёт на поправку, back on your feet — снова на ногах."},
    {"n": 7, "group": "every", "title": "Деньги", "sub": "cost an arm and a leg, make ends meet…",
     "rule": "Дорого, дёшево, экономить, сводить концы с концами. Make ends meet — та же картинка, что в русском; cost an arm and a leg — своя, английская."},
    {"n": 8, "group": "every", "title": "Разговор", "sub": "cut to the chase, in a nutshell…",
     "rule": "Говорить прямо или ходить вокруг да около, пересказать в двух словах, выдать секрет, сообщить новость. Break the news — важная идиома для врача: сообщить плохую новость."},
    {"n": 9, "group": "mix", "title": "Всё вместе", "sub": "15 случайных карточек",
     "rule": "Карточки из всех тем вперемешку."},
]

# Не переводи дословно: калька | как говорят | пояснение
ERRORS = [
    ["kill two hares", "kill two birds with one stone", "не зайцы, а птицы — и одним камнем"],
    ["the last drop", "the last straw", "не капля, а соломинка"],
    ["a storm in a glass of water", "a storm in a teacup", "буря в чайной чашке"],
    ["like two drops of water", "like two peas in a pod", "две горошины в стручке"],
    ["in the seventh sky", "on cloud nine", "не седьмое небо, а девятое облако"],
    ["as healthy as a bull", "as fit as a fiddle", "не бык, а скрипка"],
    ["not in my plate", "like a fish out of water", "не в своей тарелке — рыба без воды"],
    ["on the same boat", "in the same boat", "в лодке — in"],
    ["learn from heart", "learn by heart", "наизусть — by heart"],
    ["under weather", "under the weather", "с the"],
]

CARDS = []

def c(id, t, ab, reg, lit, en, ru, note, ex, ex_ru, ex_say=None):
    CARDS.append(dict(id=id, t=t, ab=ab, reg=reg, lit=lit, en=en, ru=ru, note=note, ex=ex, ex_ru=ex_ru, ex_say=ex_say))

# 1 · Легко и трудно
c("piece-of-cake", 1, "a piece of cake", "разг.", "кусок торта", "something very easy to do",
  "проще простого, раз плюнуть", "Обычно: it's / it was a piece of cake. Всегда с a и в единственном числе.",
  "After twenty lumbar punctures, the next one was [a piece of cake].", "После двадцати люмбальных пункций следующая была проще простого.")
c("easier-said", 1, "easier said than done", "нейтр.", "легче сказано, чем сделано", "it sounds easy, but it is hard to do",
  "легко сказать", "Обычно отдельной репликой: That's easier said than done.",
  "“Just get more sleep,” he said. That's [easier said than done] on night shifts.", "«Просто больше спи», — сказал он. Легко сказать, когда работаешь по ночам.")
c("tip-of-iceberg", 1, "the tip of the iceberg", "нейтр.", "верхушка айсберга", "a small, visible part of a much bigger problem",
  "верхушка айсберга", "Та же картинка, что в русском. Чаще: only the tip of the iceberg.",
  "The reported cases are only [the tip of the iceberg].", "Зарегистрированные случаи — лишь верхушка айсберга.")
c("out-of-hand", 1, "get out of hand", "нейтр.", "выйти из руки", "to become impossible to control",
  "выйти из-под контроля", "Подлежащее — ситуация, а не человек: things got out of hand.",
  "The queue in A&E [got out of hand] during the flu outbreak.", "Во время вспышки гриппа очередь в приёмном вышла из-под контроля.",
  ex_say="The queue in A and E got out of hand during the flu outbreak.")
c("hot-water", 1, "in hot water", "разг.", "в горячей воде", "in trouble, especially with someone in authority",
  "влипнуть, попасть в переплёт", "be / get into hot water — обычно неприятности с начальством или законом.",
  "He'll be [in hot water] if he misses another deadline.", "Он влипнет, если сорвёт ещё один срок.")
c("blessing", 1, "a blessing in disguise", "нейтр.", "переодетое благословение", "something bad that turns out to be good",
  "не было бы счастья, да несчастье помогло", "Часто: turned out to be a blessing in disguise.",
  "Failing the exam the first time turned out to be [a blessing in disguise].", "Провал на экзамене с первой попытки в итоге пошёл на пользу.")
c("last-straw", 1, "the last straw", "нейтр.", "последняя соломинка", "the last of several bad things that makes you lose patience",
  "последняя капля", "По-русски капля, по-английски соломинка — из поговорки о соломинке, сломавшей спину верблюду.",
  "The third night call in a row was [the last straw].", "Третий ночной вызов подряд стал последней каплей.")
c("storm-teacup", 1, "a storm in a teacup", "нейтр. · брит.", "буря в чайной чашке", "a lot of anger or worry about something unimportant",
  "буря в стакане воды", "Брит. Американцы говорят a tempest in a teapot.",
  "The row about the rota was just [a storm in a teacup].", "Скандал из-за графика дежурств был бурей в стакане воды.")

# 2 · Время
c("blue-moon", 2, "once in a blue moon", "разг.", "раз в голубую луну", "very rarely",
  "раз в сто лет, крайне редко", "Обычно в конце фразы: I see him once in a blue moon.",
  "We see a case like this [once in a blue moon].", "Такой случай у нас бывает раз в сто лет.")
c("long-run", 2, "in the long run", "нейтр.", "на длинной дистанции", "over a long period of time; in the end",
  "в долгосрочной перспективе, в конечном счёте", "Пара: in the short run. Часто в начале фразы.",
  "[In the long run], prevention is cheaper than treatment.", "В долгосрочной перспективе профилактика дешевле лечения.")
c("call-it-a-day", 2, "call it a day", "разг.", "назвать это днём", "to stop working for the rest of the day",
  "закончить на сегодня", "Let's call it a day — «на сегодня всё». Вечером — ещё и call it a night.",
  "We'd done six procedures, so we [called it a day].", "Мы сделали шесть процедур и на этом закончили.")
c("round-clock", 2, "around the clock", "нейтр.", "вокруг циферблата", "all day and all night, without stopping",
  "круглосуточно", "Брит. чаще round the clock. Перед существительным — через дефисы: round-the-clock care.",
  "The stroke unit admits patients [around the clock].", "Инсультное отделение принимает пациентов круглосуточно.")
c("nick-of-time", 2, "in the nick of time", "нейтр.", "в зарубку времени", "at the last possible moment",
  "как раз вовремя, в последний момент", "Только о хорошем исходе: успели. Похоже: just in time.",
  "The ambulance arrived [in the nick of time].", "Скорая приехала как раз вовремя.")
c("spur-moment", 2, "on the spur of the moment", "нейтр.", "под шпорой момента", "suddenly, without planning",
  "спонтанно, под влиянием момента", "Перед существительным: a spur-of-the-moment decision.",
  "We booked the trip [on the spur of the moment].", "Мы забронировали поездку спонтанно.")
c("from-scratch", 2, "from scratch", "нейтр.", "от стартовой черты", "from the very beginning, without using anything done before",
  "с нуля", "start / build / learn from scratch.",
  "We had to rewrite the protocol [from scratch].", "Протокол пришлось переписать с нуля.")
c("race-time", 2, "a race against time", "нейтр.", "гонка против времени", "a situation where you must do something very quickly",
  "гонка со временем", "Ещё: a race against the clock. В инсульте это буквально: time is brain.",
  "Treating a stroke is always [a race against time].", "Лечение инсульта — всегда гонка со временем.")
c("better-late", 2, "better late than never", "нейтр.", "лучше поздно, чем никогда", "it is better to do something late than not at all",
  "лучше поздно, чем никогда", "Та же пословица, что в русском. Часто шутливо, когда кто-то опоздал.",
  "He finally quit smoking at seventy — [better late than never].", "Он наконец бросил курить в семьдесят — лучше поздно, чем никогда.")

# 3 · Решения и риски
c("make-up-mind", 3, "make up your mind", "нейтр.", "собрать свой ум", "to decide",
  "решиться, определиться", "your меняется: make up my / his / her mind. Можно и make your mind up.",
  "She couldn't [make up her mind] about the surgery.", "Она никак не могла решиться на операцию.")
c("on-the-fence", 3, "sit on the fence", "разг.", "сидеть на заборе", "to avoid choosing between two sides",
  "занимать выжидательную позицию, ни нашим ни вашим", "Обычно с неодобрением: Stop sitting on the fence!",
  "You can't [sit on the fence] forever — we need a decision.", "Нельзя вечно отмалчиваться — нужно решение.")
c("by-ear", 3, "play it by ear", "разг.", "играть на слух", "to decide what to do as things happen, without a plan",
  "действовать по обстоятельствам", "Всегда с it: Let's play it by ear.",
  "We don't know how busy it'll be, so let's [play it by ear].", "Неизвестно, сколько будет работы, так что будем действовать по обстоятельствам.")
c("pinch-salt", 3, "take something with a pinch of salt", "нейтр.", "со щепоткой соли", "not to believe something completely",
  "относиться скептически, делить на два", "Амер. — a grain of salt.",
  "Take online reviews [with a pinch of salt].", "К отзывам в интернете относись скептически.")
c("cold-feet", 3, "get cold feet", "разг.", "получить холодные ноги", "to suddenly feel too nervous to do something you planned",
  "струсить, дрогнуть в последний момент", "feet — всегда во множественном числе. Часто перед свадьбой или операцией.",
  "He [got cold feet] the night before the operation.", "Накануне операции он струсил.")
c("ball-court", 3, "the ball is in your court", "нейтр.", "мяч на твоей половине корта", "it is your turn to act or decide",
  "ход за тобой, слово за тобой", "your меняется: the ball is in their court.",
  "We've sent the offer, so [the ball is in their court] now.", "Мы отправили предложение, теперь ход за ними.")
c("long-shot", 3, "a long shot", "разг.", "выстрел издалека", "an attempt that is unlikely to succeed",
  "шансов мало, но попробовать стоит", "It's a long shot, but… — вежливое начало просьбы с малыми шансами.",
  "It's [a long shot], but the new trial might accept him.", "Шансов мало, но его могут взять в новое исследование.")
c("better-safe", 3, "better safe than sorry", "нейтр.", "лучше осторожно, чем жаль", "it is wiser to be careful than to take a risk",
  "лучше перестраховаться, бережёного бог бережёт", "Обычно отдельной репликой: Better safe than sorry.",
  "Let's repeat the scan tomorrow — [better safe than sorry].", "Давай повторим снимок завтра — лучше перестраховаться.")
c("two-minds", 3, "in two minds", "нейтр. · брит.", "в двух умах", "unable to decide between two choices",
  "в раздумьях, колеблюсь", "be in two minds about something. Амер. — of two minds.",
  "I'm [in two minds] about taking the job.", "Никак не решу, соглашаться ли на эту работу.")

# 4 · Работа и учёба
c("nail-head", 4, "hit the nail on the head", "нейтр.", "попасть гвоздю по шляпке", "to describe exactly what is causing a problem",
  "попасть в точку", "Часто как похвала: You've hit the nail on the head.",
  "You've [hit the nail on the head] — the delay is in the lab.", "Ты попал в точку: задержка — в лаборатории.")
c("cut-corners", 4, "cut corners", "нейтр.", "срезать углы", "to do something quickly or cheaply by ignoring rules or quality",
  "халтурить, экономить на качестве", "Всегда с неодобрением: речь не о коротком пути, а о пренебрежении правилами.",
  "Never [cut corners] with sterile technique.", "Никогда не экономьте на стерильности.")
c("pull-weight", 4, "pull your weight", "нейтр.", "тянуть свой вес", "to do your fair share of the work",
  "работать наравне со всеми", "Чаще с отрицанием: He isn't pulling his weight. your меняется.",
  "Everyone on the team has to [pull their weight].", "Каждый в команде должен работать наравне со всеми.")
c("extra-mile", 4, "go the extra mile", "нейтр.", "пройти лишнюю милю", "to make more effort than is expected",
  "сделать больше, чем требуется", "Похвала: She always goes the extra mile for her patients.",
  "The nurses on this ward [go the extra mile] for every patient.", "Медсёстры в этом отделении делают для каждого пациента больше, чем требуется.")
c("ball-rolling", 4, "get the ball rolling", "разг.", "покатить мяч", "to start an activity",
  "начать, сдвинуть дело с мёртвой точки", "Часто в начале собрания: Let me get the ball rolling.",
  "Let's [get the ball rolling] with the first case.", "Давайте начнём с первого случая.")
c("drawing-board", 4, "back to the drawing board", "нейтр.", "назад к чертёжной доске", "to start again because a plan has failed",
  "начинать заново", "Обычно: It's back to the drawing board.",
  "The pilot project failed, so it's [back to the drawing board].", "Пилотный проект провалился — начинаем заново.")
c("learn-ropes", 4, "learn the ropes", "разг.", "выучить снасти", "to learn how to do a job",
  "освоиться, войти в курс дела", "Кто учит — show someone the ropes.",
  "It took me a month to [learn the ropes] in the new unit.", "Мне понадобился месяц, чтобы освоиться в новом отделении.")
c("midnight-oil", 4, "burn the midnight oil", "нейтр.", "жечь полуночное масло", "to work or study late at night",
  "засиживаться за работой допоздна", "Обычно о подготовке и учёбе: burning the midnight oil before exams.",
  "I've been [burning the midnight oil] to finish the paper.", "Я засиживаюсь допоздна, чтобы закончить статью.")
c("same-page", 4, "on the same page", "разг.", "на одной странице", "agreeing about what is happening or what to do",
  "на одной волне, понимать одинаково", "Часто вопросом: Are we all on the same page?",
  "Before we start, let's make sure we're all [on the same page].", "Перед началом убедимся, что все понимают план одинаково.")
c("up-to-speed", 4, "up to speed", "нейтр.", "до нужной скорости", "having the latest information about something",
  "в курсе дела", "bring someone up to speed — ввести в курс; get up to speed — войти в курс.",
  "Can you bring me [up to speed] on bed twelve?", "Введёшь меня в курс по двенадцатой койке?")

# 5 · Люди и отношения
c("break-ice", 5, "break the ice", "нейтр.", "сломать лёд", "to make people feel relaxed when they first meet",
  "растопить лёд, разрядить обстановку", "Существительное — an icebreaker.",
  "A joke about the weather helped [break the ice].", "Шутка о погоде помогла разрядить обстановку.")
c("same-boat", 5, "in the same boat", "нейтр.", "в одной лодке", "in the same difficult situation as others",
  "в одной лодке", "Та же картинка, что в русском, но предлог — in, не on.",
  "Don't worry about the exam — we're all [in the same boat].", "Не переживай из-за экзамена — мы все в одной лодке.")
c("eye-to-eye", 5, "see eye to eye", "нейтр.", "видеть глаз в глаз", "to agree with someone",
  "сходиться во мнениях", "Чаще с отрицанием: We don't always see eye to eye.",
  "Surgeons and neurologists don't always [see eye to eye].", "Хирурги и неврологи не всегда сходятся во мнениях.")
c("house-fire", 5, "get on like a house on fire", "разг. · брит.", "ладить, как горит дом", "to like each other and become friends very quickly",
  "сразу найти общий язык", "Картинка — быстро, как огонь. Амер. — get along like a house on fire.",
  "My mum and my wife [got on like a house on fire].", "Мама и жена сразу нашли общий язык.")
c("benefit-doubt", 5, "give someone the benefit of the doubt", "нейтр.", "дать кому-то выгоду сомнения", "to trust someone without proof",
  "поверить на слово, не судить заранее", "someone меняется: give him the benefit…",
  "He's never been late before, so I'll [give him the benefit of the doubt].", "Раньше он не опаздывал, так что поверю ему на слово.")
c("cat-bag", 5, "let the cat out of the bag", "разг.", "выпустить кота из мешка", "to tell a secret by mistake",
  "проболтаться", "Не путай с «кот в мешке» — это a pig in a poke. Близко: spill the beans.",
  "Who [let the cat out of the bag] about the party?", "Кто проболтался про вечеринку?")
c("pull-leg", 5, "pull someone's leg", "разг.", "тянуть кого-то за ногу", "to tell someone something untrue as a joke",
  "разыгрывать, подшучивать", "Are you pulling my leg? — «Ты шутишь?» Это безобидная шутка, а не обман.",
  "Relax, I'm just [pulling your leg]!", "Расслабься, я просто шучу!")
c("blind-eye", 5, "turn a blind eye", "нейтр.", "повернуть слепой глаз", "to pretend not to notice something wrong",
  "закрывать глаза (на что-то)", "turn a blind eye to something.",
  "Managers can't [turn a blind eye] to unsafe staffing levels.", "Руководство не может закрывать глаза на опасную нехватку персонала.")
c("behind-back", 5, "behind someone's back", "нейтр.", "за чьей-то спиной", "without someone knowing, in an unfair way",
  "за спиной", "Та же картинка, что в русском. someone меняется: behind my back.",
  "They changed the rota [behind my back].", "Они поменяли график за моей спиной.")

# 6 · Здоровье и чувства
c("weather", 6, "under the weather", "разг.", "под погодой", "slightly ill",
  "неважно себя чувствовать, приболеть", "feel / be under the weather — о лёгком недомогании, не о тяжёлой болезни.",
  "I'm feeling a bit [under the weather] today.", "Я сегодня что-то приболел.")
c("on-the-mend", 6, "on the mend", "разг.", "в починке", "getting better after an illness or injury",
  "идти на поправку", "be on the mend — о здоровье, а ещё об отношениях и экономике.",
  "His speech is improving — he's definitely [on the mend].", "Речь улучшается — он явно идёт на поправку.")
c("back-on-feet", 6, "back on your feet", "нейтр.", "снова на своих ногах", "healthy again after an illness, or recovered after a problem",
  "снова на ногах, оправиться", "get / be back on your feet; your меняется.",
  "Physio will help get you [back on your feet].", "Физиотерапия поможет вам снова встать на ноги.")
c("fit-fiddle", 6, "as fit as a fiddle", "разг.", "в форме, как скрипка", "very healthy and strong",
  "здоров как бык", "По-русски бык, по-английски скрипка. fit — «в хорошей форме».",
  "At eighty, my grandfather is still [as fit as a fiddle].", "В восемьдесят мой дедушка всё ещё здоров как бык.")
c("clean-bill", 6, "a clean bill of health", "нейтр.", "чистое свидетельство о здоровье", "a report that someone is healthy or something is in good condition",
  "заключение «здоров», «всё чисто»", "give someone a clean bill of health. Бывает и о зданиях, компаниях.",
  "After the tests, the cardiologist gave him [a clean bill of health].", "После обследования кардиолог признал его здоровым.")
c("over-moon", 6, "over the moon", "разг. · брит.", "выше луны", "extremely happy",
  "вне себя от радости", "be over the moon about something. Похоже: on cloud nine.",
  "She was [over the moon] when her paper was accepted.", "Она была вне себя от радости, когда её статью приняли.")
c("butterflies", 6, "butterflies in your stomach", "разг.", "бабочки в животе", "a nervous feeling before something important",
  "мандраж, волнение", "have / get butterflies (in my stomach).",
  "I always get [butterflies in my stomach] before a presentation.", "Перед выступлением у меня всегда мандраж.")
c("chin-up", 6, "keep your chin up", "разг.", "держи подбородок выше", "stay positive in a difficult situation",
  "не вешай нос, держись", "Обычно как поддержка: Keep your chin up!",
  "[Keep your chin up] — the worst part is over.", "Не вешай нос — самое трудное позади.")
c("off-chest", 6, "get something off your chest", "разг.", "снять что-то с груди", "to talk about something that has been worrying you",
  "выговориться, облегчить душу", "something меняется: get it off my chest.",
  "Talking to a counsellor helped her [get it off her chest].", "Разговор с психологом помог ей выговориться.")
c("pain-neck", 6, "a pain in the neck", "разг.", "боль в шее", "a person or thing that is very annoying",
  "зануда, сплошная головная боль", "О надоедливом человеке или деле: The paperwork is a real pain in the neck.",
  "Filling in these forms is [a pain in the neck].", "Заполнять эти бланки — сплошная головная боль.")

# 7 · Деньги
c("arm-leg", 7, "cost an arm and a leg", "разг.", "стоить руки и ноги", "to be very expensive",
  "стоить целое состояние", "Обычно: It cost (me) an arm and a leg.",
  "The new scanner [cost an arm and a leg].", "Новый томограф стоил целое состояние.")
c("break-bank", 7, "break the bank", "разг.", "сорвать банк", "to cost too much money",
  "разорить, ударить по карману", "Обычно с отрицанием: It won't break the bank — «не разоришься».",
  "A good pair of trainers won't [break the bank].", "Хорошие кроссовки не разорят.")
c("ends-meet", 7, "make ends meet", "нейтр.", "свести концы", "to have just enough money for basic things",
  "сводить концы с концами", "Та же картинка, что в русском. Часто: struggle to make ends meet.",
  "Many junior doctors struggle to [make ends meet].", "Многим молодым врачам трудно сводить концы с концами.")
c("tighten-belt", 7, "tighten your belt", "нейтр.", "затянуть свой ремень", "to spend less money",
  "затянуть пояса, экономить", "В русском — пояса, в английском — your belt; your меняется: its, their.",
  "After the cuts, the hospital had to [tighten its belt].", "После сокращений больнице пришлось затянуть пояса.")
c("shoestring", 7, "on a shoestring", "разг.", "на шнурке", "with very little money",
  "на копейки, с минимальным бюджетом", "run something on a shoestring; a shoestring budget.",
  "They ran the whole study [on a shoestring].", "Всё исследование они провели на копейки.")
c("money-trees", 7, "money doesn't grow on trees", "разг.", "деньги не растут на деревьях", "money is limited, so you should not waste it",
  "деньги с неба не падают", "Обычно родители — детям.",
  "No new phone this year — [money doesn't grow on trees]!", "В этом году без нового телефона — деньги с неба не падают!")

# 8 · Разговор
c("beat-bush", 8, "beat around the bush", "разг.", "бить по кустам вокруг", "to avoid talking about the main point",
  "ходить вокруг да около", "Брит. — beat about the bush. Чаще с отрицанием: Don't beat around the bush.",
  "Don't [beat around the bush] — just tell me the results.", "Не ходи вокруг да около — просто скажи результаты.")
c("cut-chase", 8, "cut to the chase", "разг.", "перейти к погоне", "to talk about the most important thing immediately",
  "сразу к делу", "Из кино: скучное вырезают и сразу переходят к погоне.",
  "Let me [cut to the chase]: we need two more nurses.", "Сразу к делу: нам нужны ещё две медсестры.")
c("nutshell", 8, "in a nutshell", "нейтр.", "в ореховой скорлупе", "in a very short summary",
  "в двух словах, вкратце", "Часто в начале итога: In a nutshell, the trial was negative.",
  "[In a nutshell], the new drug didn't work.", "Вкратце: новый препарат не сработал.")
c("speak-mind", 8, "speak your mind", "нейтр.", "сказать, что на уме", "to say honestly what you think",
  "говорить прямо", "your меняется: She always speaks her mind.",
  "At the meeting, feel free to [speak your mind].", "На собрании можете говорить прямо.")
c("wrong-end", 8, "get the wrong end of the stick", "разг. · брит.", "взяться не за тот конец палки", "to understand something wrongly",
  "неправильно понять, всё перепутать", "Брит. Обычно: you've got the wrong end of the stick.",
  "I think you've [got the wrong end of the stick] — the scan was normal.", "Кажется, ты не так понял: снимок в норме.")
c("spill-beans", 8, "spill the beans", "разг.", "рассыпать бобы", "to tell people secret information",
  "проболтаться, выложить всё", "Come on, spill the beans! — «Ну, выкладывай!» Близко: let the cat out of the bag.",
  "Come on, [spill the beans] — did you get the job?", "Ну, выкладывай — тебя взяли на работу?")
c("break-news", 8, "break the news", "нейтр.", "разбить новость", "to tell someone important, often bad, news",
  "сообщить (плохую) новость", "break the news to someone. В медицине — breaking bad news.",
  "The consultant [broke the news] to the family.", "Консультант сообщил родственникам печальную новость.")
c("word-mouth", 8, "word of mouth", "нейтр.", "слово из уст", "information passed from person to person by talking",
  "сарафанное радио, из уст в уста", "by word of mouth.",
  "Most of our patients find us by [word of mouth].", "Большинство пациентов узнают о нас по сарафанному радио.")
c("by-heart", 8, "by heart", "нейтр.", "сердцем", "from memory",
  "наизусть", "learn / know something by heart. Не from heart.",
  "Every resident should know the NIHSS [by heart].", "Каждый ординатор должен знать шкалу NIHSS наизусть.",
  ex_say="Every resident should know the N I H S S by heart.")
c("bite-tongue", 8, "bite your tongue", "разг.", "прикусить язык", "to stop yourself from saying something",
  "прикусить язык, сдержаться", "Та же картинка, что в русском. your меняется: I bit my tongue.",
  "I wanted to argue, but I [bit my tongue].", "Хотелось возразить, но я сдержался.")

# ——— Озвучка
def plain(s):
    return re.sub(r"[\[\]]", "", s)

def sentence(s):
    s = s.replace("“", "").replace("”", "").strip()
    s = s[:1].upper() + s[1:]
    return s if s[-1:] in ".!?" else s + "."

for k in CARDS:
    k["say"] = sentence(k["ab"])
    k["say_l"] = sentence(k["ab"]) + " " + sentence(k["en"])
    if not k["ex_say"]:
        k["ex_say"] = sentence(plain(k["ex"]))

# ——— Проверки
ids = [k["id"] for k in CARDS]
assert len(ids) == len(set(ids))
assert {k["t"] for k in CARDS} == set(range(1, MIXED_TOPIC))
for k in CARDS:
    assert k["ex"].count("[") == 1 and k["ex"].count("]") == 1, k["id"]
    for f in ("reg", "lit", "en", "ru", "note", "ex_ru"):
        assert k[f] and "  " not in k[f], (k["id"], f)

if __name__ == "__main__":
    from collections import Counter
    print(len(CARDS), "cards", sorted(Counter(k["t"] for k in CARDS).items()))
    print(max((len(k["ab"]), k["ab"]) for k in CARDS))
