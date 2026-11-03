# Справочник тренажёров и прежних генераторов

Подробности перенесены без изменений, чтобы сохранить назначение тренажёров, их положение
в каталоге, правила содержания и особенности звука. Все пути команд ниже считаются от корня
репозитория или от `sources/`, как указано в соответствующем пункте.

Это справка для анализа существующих исходников, а не действующий порядок публикации.
При работе соблюдать [AGENTS.md](../AGENTS.md) и [DAILY_DECKS.md](../tools/DAILY_DECKS.md):
не запускать исторические `sources/*/build.py`, не заменять проверенные пакеты аудио и не
восстанавливать старые задачи Claude. Синтез и публикация ежедневных колод выполняются
существующим GitHub Actions после проверки очереди Codex.

## Отдельные тренажёры

- **«Have to, must и похожие» (oblig)** — единственный тренажёр, который собирается прямо в `site/`, без старого артефакта:
  из `sources/` — `python3 oblig/mk_template.py` (шаблон из `modal/template.html`), `python3 oblig/clips.py`,
  `python3 oblig/tts.py` (записи голосом Ryan через edge-tts), `python3 oblig/build.py` (пишет `site/apps/oblig.html`,
  `site/packs/oblig.mp3`, запись в `tools/packs.json` и `tools/catalog.json`), затем `python3 tools/mk_shell.py`;
  проверка — `python3 oblig/test.py`. Содержание — `sources/oblig/content.py`. Записи (голос Ryan) нужны
  доступ к speech.platform.bing.com; исходные mp3 в репозиторий не кладутся — только пакет `site/packs/oblig.mp3`.
  Новая или изменённая фраза: `oblig/clips.py` → `oblig/tts.py` (дописывает недостающие) → `oblig/build.py` → `tools/mk_shell.py`;
  без записи фразу читает голос устройства.
- **«Have a look, take a seat» (havea)** собирается так же, из `sources/havea/` (шаблон — из `oblig/template.html`):
  `python3 havea/mk_template.py`, `havea/clips.py`, `havea/tts.py`, `havea/build.py`, затем `python3 tools/mk_shell.py`;
  проверка — `python3 havea/test.py`. Стоит в каталоге сразу после «Have, take, pay» (htp) и не повторяет его:
  там — отдельные сочетания, здесь — сама конструкция «глагол + a + существительное».
- **«Increase by и increase to» (incr)** — так же, из `sources/incr/` (шаблон из `oblig/template.html`):
  `python3 incr/mk_template.py`, `incr/clips.py`, `incr/tts.py`, `incr/build.py`, затем `python3 tools/mk_shell.py`;
  проверка — `python3 incr/test.py`. Стоит сразу после «Цифр» (num): там по одной-две карточки на by, to и increase in,
  здесь — вся система предлогов изменения, rise/raise, тренды, проценты и пункты, кратность, пороги, сравнение.
- **«Three, tree, sheep» (sounds)** и **«Advice и advise» (nverb)** — так же, из `sources/sounds/` и `sources/nverb/`
  (`mk_template.py`, `clips.py`, `tts.py`, `build.py`, затем `python3 tools/mk_shell.py`; проверка — `test.py`).
  Шаблон sounds (из `oblig/template.html`) добавляет: карточки на слух (`ear`: звучит Say … again, перевод скрыт до ответа,
  кнопка «Послушать ещё раз»), поле `say` — что произносить вместо предложения с ответом, и разметку примеров
  `[слово|a]`, `|b`, `|c` (оранжевый, синий, зелёный). nverb собирается из шаблона sounds; `say` нужно для ударений
  REcord и reCORD. Оба стоят сразу после «Пар слов» (pairs) и не повторяют его: там ловушки по смыслу, здесь — по звучанию
  и по паре «существительное — глагол».
- **«Recycle → recycling» (vnoun)** — существительное из глагола: пары с карточек урока (recycle → recycling, waste → waste,
  destroy → destruction, exist → existence, solve → solution, reduce → reduction, support → support, suffer → suffering)
  и похожие по суффиксам: -ing, -ion, -ence/-ance, -ment, -al, -ure, -y, -th, ловушки написания (maintenance, pronunciation).
  Собирается так же, из `sources/vnoun/` (шаблон из `sounds/template.html`): `python3 vnoun/mk_template.py`, `vnoun/clips.py`,
  `python3 vnoun/tts.py` (см. [правила озвучки](../AGENTS.md#голос-новых-тренажёров)), `vnoun/build.py`, затем `python3 tools/mk_shell.py`;
  проверка — `python3 vnoun/test.py`. Стоит сразу после «Advice и advise» (nverb): там пары, которые различаются буквой,
  звуком или ударением, здесь — вся система суффиксов. На карточке урока опечатка existance — в тренажёре это ловушка.
- **«Like и look like» (like)** — What's she like? (какая), What does she look like? (как выглядит), What does she like?
  (что любит); look tired и look like a doctor; I'd like и I like; like doing и feel like doing; like или as; like и as if
  + предложение; such as, flu-like, likely, alike, unlike. Собирается так же, из `sources/like/` (шаблон из `sounds/template.html`):
  `python3 like/mk_template.py`, `like/clips.py`, `python3 like/tts.py`, `like/build.py`, затем `python3 tools/mk_shell.py`;
  проверка — `python3 like/test.py`. Стоит сразу после «Похожих слов» (similar); мини-диалоги озвучены Ryan.
- **«Do without и похожие» (without)** — с карточки урока Vocabulary Focus: do without (There are a great number of things
  that we can do without. Can people do without money?) и похожее: go without, manage without, cope without, can't live without,
  survive on, make do (with), get by (on, in), could do with, do away with, dispense with, get rid of, have to do with.
  Собирается так же, из `sources/without/` (шаблон из `sounds/template.html`): `python3 without/mk_template.py`, `without/clips.py`,
  `python3 without/tts.py`, `without/build.py`, затем `python3 tools/mk_shell.py`; проверка — `python3 without/test.py`.
  Стоит сразу после «Фразовых глаголов» (phrasal); не повторяет «Manage to и похожие» (manage): там справиться с делом.
- **«Косвенные вопросы» (indq)** — так же, из `sources/indq/` (шаблон из `sounds/template.html`):
  `python3 indq/mk_template.py`, `indq/clips.py`, `indq/tts.py`, `indq/build.py`, затем `python3 tools/mk_shell.py`;
  проверка — `python3 indq/test.py`. Стоит сразу после «Вопросов» (q): там и в «Пересказе» (rep) — по теме на основу,
  здесь — вся конструкция: do/did исчезают, be и can после подлежащего, if и whether, вопрос к подлежащему, I wonder,
  пересказ, косвенный вопрос в научном тексте.
- **«What is it for?» (whatfor)** — предлог в конце вопроса: What is it for? (для чего, от чего, зачем), Who are you waiting for?,
  What are you afraid of?, Where are you from?, короткие Who with? What about?, пассив (What is he being treated for?),
  официально — предлог впереди (To whom…? On which data…?, To what extent…?), косвенные вопросы и «который»
  (the patient I told you about). Собирается так же, из `sources/whatfor/` (шаблон из `sounds/template.html`):
  `python3 whatfor/mk_template.py`, `whatfor/clips.py`, `python3 whatfor/tts.py`, `whatfor/build.py`, затем `python3 tools/mk_shell.py`;
  проверка — `python3 whatfor/test.py`. Стоит сразу после «Косвенных вопросов» (indq); в «Вопросах» (q) этому отведена одна тема,
  здесь — вся конструкция. **77 записей Microsoft Ryan созданы 23 октября 2026** с edge-tts 7.3.1:
  48 карточек, 24 примера и 5 мини-диалогов. `whatfor/build.py` требует полный набор записей с подтверждённым
  голосом, текстом и SHA-256; без них сборка останавливается до изменения опубликованных файлов.
  Для нового текста: из `sources/` — `python3 whatfor/clips.py`, `python3 whatfor/tts.py`,
  `python3 whatfor/build.py`, из корня — `python3 tools/mk_shell.py`, затем коммит и push.
- **«Types of clauses» (clauses)** — по уроку 14 (Extremes) курса Awesome English B2: придаточные времени, причины, результата,
  цели, контраста и образа действия и Grammar Focus урока (as soon as I hear — без will; As …, — запятая). Главная идея:
  придаточное отвечает на один из шести вопросов, а связку выбирают по тому, что идёт после неё; цвет в примерах и в таблице:
  оранжевый — целое предложение, синий — существительное или -ing, зелёный — глагол, подчёркнуто — отдельное слово (However,).
  Ошибка урока «buy an insurance» исправлена (insurance неисчисляемое) и упомянута в правиле. Собирается так же,
  из `sources/clauses/` (шаблон из `sounds/template.html`): `python3 clauses/mk_template.py`, `clauses/clips.py`,
  `clauses/build.py`, затем `python3 tools/mk_shell.py`; проверка — `python3 clauses/test.py`. Стоит сразу после «Связок» (link):
  там связки статей и протоколов, здесь — система урока. Озвучку Ryan создаёт workflow `Ryan audio and Pages` при публикации;
  `clauses/build.py` без локальных записей пакет и индекс не трогает, чтобы не стереть созданные workflow записи.
- **«For, during, within» (during)** — так же, из `sources/during/` (шаблон из `sounds/template.html`):
  `python3 during/mk_template.py`, `during/clips.py`, `during/tts.py`, `during/build.py`, затем `python3 tools/mk_shell.py`;
  проверка — `python3 during/test.py`. «В течение»: for, during, over, throughout, within и рядом in (через), while,
  формулы статей. Стоит сразу после «Предлогов at, on, in» (preps): там время в точке, здесь — отрезок.
- **«Инфинитив без to» (bare)** — так же, из `sources/bare/` (шаблон из `sounds/template.html`):
  `python3 bare/mk_template.py`, `bare/clips.py`, `bare/tts.py`, `bare/build.py`, затем `python3 tools/mk_shell.py`;
  проверка — `python3 bare/test.py`. Модальные, do/does/did, make и let, had better, would rather, why not, help,
  see и hear, пассив (was made to), All I did was ask. Стоит сразу после «To или -ing» (toing).
- **«I know the feeling» (encour)** — фразы урока Speaking Focus (being encouraging, showing you have things in common),
  все 15 с фото урока: вставить слово, что ответить в ситуации, вспомнить фразу по-русски. Собирается так же,
  из `sources/encour/` (шаблон из `sounds/template.html`); стоит сразу после «Идиом» (idm). Озвучка — `python3 encour/tts.py`
  (см. [правила озвучки](../AGENTS.md#голос-новых-тренажёров)); в мини-диалогах «— …? — …» обе реплики читает Ryan.

## Прежний ручной импорт колод

Раньше отдельные версии колод находились в артефактах:
- phrasal: https://claude.ai/code/artifact/17f35b77-ec05-4e16-a5e6-516e7ef5f8d8
- bbapp: https://claude.ai/code/artifact/63c4fa4f-95e7-4be6-812a-689d838c98c5

Для прежнего ручного импорта читали `index.html` и записи из `audio/` или `audio/us/`
в одну папку, затем выполняли `python3 tools/deck_sync.py phrasal <папка>` (или `bbapp`)
и `python3 tools/mk_shell.py`. Этот способ сохранён для понимания формата старых данных;
он не применяется к текущим ежедневным заданиям и не разрешает перезаписывать колоды.
Текущий процесс — [DAILY_DECKS.md](../tools/DAILY_DECKS.md), без переноса из артефактов и старых таймеров.
