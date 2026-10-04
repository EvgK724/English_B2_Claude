# Шаблон «Который» собираю из шаблона «Связки»: тренажёр тот же,
# вкладка правил — своя: кто или что (таблица), запятая или нет (шаги), ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("link/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Связки</title>", "<title>Который</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
P = lambda t: f'<span class="pr">{t.replace(" ", "&nbsp;")}</span>'
D = ' <span class="sep">·</span> '
nw = lambda t: f'<span class="nw">{t}</span>'
steps = (step(1, "Уточняет, о&nbsp;ком речь? Без запятых", nw("patients " + P("who") + " smoke") + D + nw("the drug " + P("that") + " works"))
         + step(2, "Добавляет сведения? Запятые с&nbsp;двух сторон", nw("my father" + P(", who") + " is 80,") + D + nw("aspirin" + P(", which") + " is cheap,"))
         + step(3, "Который&nbsp;— дополнение? Можно опустить", nw("the drug (" + P("that") + ") we gave") + D + nw("the man (" + P("who") + ") I met")))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Relative clauses</h1>
      <p class="r-sub">«Который»&nbsp;— это <i lang="en">who</i>, <i lang="en">which</i> или <i lang="en">that</i>. По‑русски перед ним всегда запятая, по‑английски&nbsp;— только когда придаточное добавляет сведения, а&nbsp;не&nbsp;уточняет, о&nbsp;ком речь.</p>
      <div class="algo">
        <p class="algo-h">Кто или что</p>
        <table class="vt sv">
          <colgroup><col class="v"><col></colgroup>
          <tbody>
<!--__WORDS__-->
          </tbody>
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Запятая или нет</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m">Запятые&nbsp;— как скобки. После запятой только <b class="pr" lang="en">who</b> или <b class="st" lang="en">which</b>, не&nbsp;that.</p>
        <p class="algo-note">Проверка: убери придаточное. Всё ещё понятно, о&nbsp;ком речь,&nbsp;— запятые нужны: <i lang="en">My father, who is 80, still drives</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Одна фраза&nbsp;— разный смысл</h2>
      <div class="mx-wrap">
<!--__CONTRAST__-->
      </div>
      <h2 class="lbl">Частые ошибки</h2>
      <div class="mx-wrap">
        <ul class="errs">
<!--__ERRORS__-->
        </ul>
      </div>
      <h2 class="lbl">Темы</h2>
      <div class="topics" id="topics"></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "link:state";\nconst LS_SPEAK = "link:autospeak";\nconst LS_TAB = "link:tab";\nconst LS_OPEN = "link:open";',
    'const LS_STATE = "rel:state";\nconst LS_SPEAK = "rel:autospeak";\nconst LS_TAB = "rel:tab";\nconst LS_OPEN = "rel:open";')
rep('["apple-mobile-web-app-title", "Связки"],', '["apple-mobile-web-app-title", "Который"],')
rep("// Новые карточки идут вперемешку по темам: хотя и несмотря на, причина и следствие, цель и условие чередуются.",
    "// Новые карточки идут вперемешку по темам: who и which, запятые, пропуск «который», предлоги и what чередуются.")
assert "link:state" not in s and "Связки" not in s
pathlib.Path("rel/template.html").write_text(s)
print("ok", len(s))
