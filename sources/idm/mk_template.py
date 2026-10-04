# Шаблон «Идиомы» собираю из шаблона «Сокращения»: движок карточек тот же (лицо — оборот, «не знаю / почти / знаю»,
# свайп, озвучка), вкладка правил — своя: как запомнить, как ведут себя идиомы, кальки, темы со списками.
import pathlib
s = pathlib.Path("abbr/template.html").read_text()

def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)

rep("<title>Сокращения</title>", "<title>Идиомы</title>")
rep(".ab2{font-family:var(--serif);font-size:46px;line-height:1.1}", ".ab2{font-family:var(--serif);font-size:32px;line-height:1.15}")
rep("    .ab2{font-size:38px}\n", "    .ab2{font-size:28px}\n")
rep("  .ab.s{font-size:46px}\n", "  .ab.s{font-size:46px}\n  .ab.s2{font-size:40px}\n  .ab.xs{font-size:34px}\n  .b-head .ipa2{white-space:nowrap}\n")
rep('<button class="say say-front" id="say" type="button" aria-label="Прослушать сокращение">',
    '<button class="say say-front" id="say" type="button" aria-label="Прослушать идиому">')
rep('<p class="hint" id="hint">Вспомни расшифровку и&nbsp;перевод, потом открой карточку</p>',
    '<p class="hint" id="hint">Вспомни смысл и&nbsp;русский аналог, потом открой карточку</p>')
rep('<button class="ex-play" id="playL" type="button" aria-label="Прослушать расшифровку">',
    '<button class="ex-play" id="playL" type="button" aria-label="Прослушать идиому и значение">')
rep('<span class="kind" id="kind">В больнице</span>', '<span class="kind" id="kind">Легко и трудно</span>')

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
P = lambda t: f'<span class="pr">{t}</span>'
D = ' <span class="sep">·</span> '
nw = lambda t: f'<span class="nw">{t}</span>'
ru = lambda t: f'<i lang="ru">{t}</i>'
how = (step(1, "Представь буквальную картинку", nw(P("a piece of cake")) + " " + ru("— кусок торта"))
       + step(2, "Свяжи с&nbsp;русским аналогом", nw(P("the last straw")) + " " + ru("— последняя капля"))
       + step(3, "Скажи пример вслух", "It was " + P("a piece of cake") + ".")
       + step(4, "Вставь в&nbsp;свою фразу сегодня&nbsp;же", "OK, let's " + P("call it a day") + "."))
behave = (step(1, "Слова не&nbsp;заменяют", nw("the last " + P("straw")) + ", " + ru("не") + " the last drop")
          + step(2, "Глагол меняется по&nbsp;временам", nw(P("spilled") + " the beans") + D + nw(P("got") + " cold feet"))
          + step(3, "your и&nbsp;someone&nbsp;— по&nbsp;смыслу", nw("make up " + P("her") + " mind") + D + nw("pull " + P("my") + " leg"))
          + step(4, "Большинство&nbsp;— разговорные: в&nbsp;статье и&nbsp;протоколе обходись без них", ru("пометки:") + " " + P("разг.") + D + P("нейтр.") + D + P("брит.")))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Idioms</h1>
      <p class="r-sub">Идиому нельзя перевести по&nbsp;словам&nbsp;— её запоминают целиком, как картинку. На&nbsp;лицевой стороне карточки&nbsp;— идиома, на&nbsp;обороте&nbsp;— буквальная картинка, смысл, русский аналог и&nbsp;пример.</p>
      <div class="algo">
        <p class="algo-h">Как запомнить</p>
        <ol class="steps">
''' + how + '''        </ol>
        <p class="algo-m"><b class="pr">картинка</b> → <b class="st">смысл</b> → своя фраза</p>
        <p class="algo-note">На&nbsp;обороте нажми на&nbsp;значок звука: прозвучат идиома, её значение и&nbsp;пример.</p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как ведут себя идиомы</p>
        <ol class="steps">
''' + behave + '''        </ol>
        <p class="algo-note">Пометка «брит.»: американцы поймут, но&nbsp;скажут иначе&nbsp;— <i lang="en">a storm in a teacup</i> у&nbsp;них <i lang="en">a tempest in a teapot</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Не переводи дословно</h2>
      <div class="mx-wrap">
        <ul class="errs">
<!--__ERRORS__-->
        </ul>
      </div>
      <h2 class="lbl">Темы</h2>
      <div class="topics" id="topics"></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "abbr:state";\nconst LS_SPEAK = "abbr:autospeak";\nconst LS_TAB = "abbr:tab";\nconst LS_OPEN = "abbr:open";',
    'const LS_STATE = "idm:state";\nconst LS_SPEAK = "idm:autospeak";\nconst LS_TAB = "idm:tab";\nconst LS_OPEN = "idm:open";')
rep('["apple-mobile-web-app-title", "Сокращения"],', '["apple-mobile-web-app-title", "Идиомы"],')
rep("// Новые карточки идут вперемешку по темам: больница, статьи, работа, организации, быт и переписка чередуются.",
    "// Новые карточки идут вперемешку по темам: ситуации, время, решения, работа, люди, здоровье, деньги и разговор чередуются.")
rep('  ab.className = "ab" + (card.ab.length > 7 ? " s" : card.ab.length > 4 ? " m" : "");',
    '  ab.className = "ab " + (card.ab.length > 22 ? "xs" : card.ab.length > 12 ? "s2" : "s");')
rep("// ——— Карточка: лицевая сторона — сокращение; оборот — расшифровка, перевод, пример",
    "// ——— Карточка: лицевая сторона — идиома; оборот — картинка, смысл, русский аналог, пример")
rep("// ——— Разметка: [x] — оранжевым (буквы-источники в расшифровке, сокращение в примере)",
    "// ——— Разметка: [x] — оранжевым (идиома в примере)")
assert "abbr:state" not in s and "Сокращения" not in s and "<!--__LETTERS__-->" not in s
pathlib.Path("idm/template.html").write_text(s)
print("ok", len(s))
