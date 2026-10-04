# Шаблон «Пересказ» собираю из шаблона «Вопросы»: тренажёр тот же,
# вкладка правил — своя: сдвиг времён (таблица), какой глагол выбрать (шаги), ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("q/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Вопросы</title>", "<title>Пересказ</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
P = lambda t: f'<span class="pr">{t.replace(" ", "&nbsp;")}</span>'
D = ' <span class="sep">·</span> '
nw = lambda t: f'<span class="nw">{t}</span>'
steps = (step(1, "Передаёшь слова?", nw("He " + P("said") + " (that)…") + D + nw("He " + P("told me") + " (that)…"))
         + step(2, "Передаёшь вопрос?", nw("She " + P("asked if") + " I smoked") + D + nw(P("asked where") + " it hurt"))
         + step(3, "Просьба, совет, запрет?", nw("I " + P("told him to") + " rest") + D + nw(P("not to") + " drive"))
         + step(4, "Жалобы или отрицание?", nw(P("complained of") + " pain") + D + nw(P("denied") + " smoking")))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Reported speech</h1>
      <p class="r-sub">Когда пересказываешь слова пациента или коллеги, время отступает на&nbsp;шаг назад: <b>«I feel dizzy» → He said he felt dizzy</b>. Так пишут анамнез и&nbsp;докладывают о&nbsp;больном.</p>
      <div class="algo">
        <p class="algo-h">Сдвиг времён</p>
        <table class="vt">
          <colgroup><col class="v"><col></colgroup>
          <tbody>
<!--__TABLE__-->
          </tbody>
        </table>
        <p class="algo-note">Если сказанное верно и&nbsp;сейчас, сдвиг можно не&nbsp;делать: <i lang="en">He said he lives alone</i>.</p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Какой глагол</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m"><b class="pr" lang="en">say</b> что-то, <b class="st" lang="en">tell</b> кому-то: <i lang="en">He said he was tired. He told me he was tired.</i></p>
        <p class="algo-note">В косвенном вопросе нет do, did и&nbsp;вопросительного знака: <i lang="en">I asked where the pain was</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Одна ситуация&nbsp;— разный смысл</h2>
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

rep('const LS_STATE = "q:state";\nconst LS_SPEAK = "q:autospeak";\nconst LS_TAB = "q:tab";\nconst LS_OPEN = "q:open";',
    'const LS_STATE = "rep:state";\nconst LS_SPEAK = "rep:autospeak";\nconst LS_TAB = "rep:tab";\nconst LS_OPEN = "rep:open";')
rep('["apple-mobile-web-app-title", "Вопросы"],', '["apple-mobile-web-app-title", "Пересказ"],')
rep("// Новые карточки идут вперемешку по темам: do и did, вопросы без do, вежливые вопросы и расспрос пациента чередуются.",
    "// Новые карточки идут вперемешку по темам: say и tell, сдвиг времён, вопросы, просьбы и глаголы пересказа чередуются.")
assert "q:state" not in s
pathlib.Path("rep/template.html").write_text(s)
print("ok", len(s))
