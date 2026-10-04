# Шаблон «remember» собираю из шаблона «have it done»: тренажёр тот же,
# вкладка правил — своя: главный ключ (шаги), пары to / -ing (таблица), ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("hsd/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>have it done</title>", "<title>remember</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
P = lambda t: f'<span class="pr">{t.replace(" ", "&nbsp;")}</span>'
B = lambda t: f'<span class="st">{t.replace(" ", "&nbsp;")}</span>'
D = ' <span class="sep">·</span> '
nw = lambda t: f'<span class="nw">{t}</span>'
steps = (step(1, "Действие ещё впереди?&nbsp;<span class=\"nw\">— to</span>", nw("remember " + B("to call")) + D + nw("forget " + B("to sign")))
         + step(2, "Уже было или само действие?&nbsp;<span class=\"nw\">— -ing</span>", nw("remember " + P("calling")) + D + nw("regret " + P("saying")))
         + step(3, "По‑русски «чтобы» или «потом»?&nbsp;<span class=\"nw\">— to</span>", nw("stop " + B("to rest")) + D + nw("go on " + B("to discuss"))))
table = '''        <table class="mt af">
          <colgroup><col><col></colgroup>
          <thead><tr><th scope="col">+&nbsp;to</th><th scope="col">+&nbsp;-ing</th></tr></thead>
          <tbody>
<!--__PAIRS__-->
          </tbody>
        </table>
'''

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">to do or doing</h1>
      <p class="r-sub">У&nbsp;этих глаголов <i lang="en">to</i> и&nbsp;<i lang="en" class="nw">-ing</i> дают два разных смысла. Главный ключ: <i lang="en">to</i> смотрит вперёд&nbsp;— дело ещё предстоит; <i lang="en" class="nw">-ing</i>&nbsp;— назад или на&nbsp;само действие.</p>
      <div class="algo">
        <p class="algo-h">Главный ключ</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m"><b class="st" lang="en">to</b> смотрит вперёд, <b class="pr nw" lang="en">-ing</b>&nbsp;— назад.</p>
        <p class="algo-note">Особый случай&nbsp;— <i lang="en">try</i>: <i lang="en">try to</i>&nbsp;— стараться, трудно; <i lang="en">try doing</i>&nbsp;— попробовать способ.</p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Пары</p>
''' + table + '''        <p class="algo-note">У&nbsp;<i lang="en">begin, start, continue</i> смысл почти не&nbsp;меняется: подойдёт и&nbsp;то и&nbsp;другое.</p>
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

rep('const LS_STATE = "hsd:state";\nconst LS_SPEAK = "hsd:autospeak";\nconst LS_TAB = "hsd:tab";\nconst LS_OPEN = "hsd:open";',
    'const LS_STATE = "vm:state";\nconst LS_SPEAK = "vm:autospeak";\nconst LS_TAB = "vm:tab";\nconst LS_OPEN = "vm:open";')
rep('["apple-mobile-web-app-title", "have it done"],', '["apple-mobile-web-app-title", "remember"],')
rep("// Новые карточки идут вперемешку по темам: have it done, времена, get, неприятность, сам или нет, make и let, «сделать МРТ» чередуются.",
    "// Новые карточки идут вперемешку по темам: remember, forget, regret, try, stop, go on, need, see и afraid чередуются.")
assert "hsd:state" not in s and "have it done" not in s
pathlib.Path("vm/template.html").write_text(s)
print("ok", len(s))
