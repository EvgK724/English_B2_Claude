# Шаблон «Сравнения» собираю из шаблона «used to»: тренажёр тот же,
# вкладка правил — своя: как образовать (шаги), как сравнить (таблица), ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("usedto/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Used to и would</title>", "<title>Сравнения</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
P = lambda t: f'<span class="pr">{t.replace(" ", "&nbsp;")}</span>'
def chain(a, b, c=None):
    return f'<span class="nw">{a} →</span> <span class="nw">{P(b)}</span>' + (f' <span class="nw">→ {P(c)}</span>' if c else "")
steps = (step(1, "Один слог", chain("tall", "taller", "the tallest") + '<br>' + chain("big", "bigger") + ' <i>(удвоение)</i>')
         + step(2, "Два слога на&nbsp;-y", chain("easy", "easier", "the easiest"))
         + step(3, "Два слога и&nbsp;длиннее", chain("careful", "more careful", "the most careful"))
         + step(4, "Неправильные&nbsp;— запомнить", chain("good", "better", "the best") + '<br>' + chain("bad", "worse", "the worst")
                + '<br>' + chain("far", "further", "the furthest") + '<br>' + chain("little", "less", "the least")))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Comparisons</h1>
      <p class="r-sub">Сравнивают тремя способами: <b>больше</b>&nbsp;— <i lang="en" class="nw">‑er / more … than</i>, <b>так же</b>&nbsp;— <i lang="en">as … as</i>, <b>самый</b>&nbsp;— <i lang="en">the -est / the most</i>.</p>
      <div class="algo">
        <p class="algo-h">Как образовать</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m">Короткое слово растёт само&nbsp;— <b class="pr" lang="en">‑er</b>, длинному нужна подпорка&nbsp;— <b class="pr" lang="en">more</b>.</p>
        <p class="algo-note">Вместе нельзя: <i lang="en">more better, more easier</i>&nbsp;— ошибки. Самый&nbsp;— всегда с&nbsp;<i lang="en">the</i>.</p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как сравнить</p>
        <table class="vt">
          <colgroup><col class="v"><col></colgroup>
          <tbody>
<!--__TABLE__-->
          </tbody>
        </table>
        <p class="algo-note">С&nbsp;<i lang="en">‑er</i> не&nbsp;ставят <i lang="en">very</i>: намного лучше&nbsp;— <i lang="en">much better</i>. В&nbsp;два раза&nbsp;— <i lang="en">twice</i>, а&nbsp;не two times.</p>
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

rep('const LS_STATE = "usedto:state";\nconst LS_SPEAK = "usedto:autospeak";\nconst LS_TAB = "usedto:tab";\nconst LS_OPEN = "usedto:open";',
    'const LS_STATE = "cmp:state";\nconst LS_SPEAK = "cmp:autospeak";\nconst LS_TAB = "cmp:tab";\nconst LS_OPEN = "cmp:open";')
rep('["apple-mobile-web-app-title", "used to"],', '["apple-mobile-web-app-title", "Сравнения"],')
rep("// Новые карточки идут вперемешку по темам: раньше, привык, привыкаю и «так бывало» чередуются — выбирать приходится по смыслу.",
    "// Новые карточки идут вперемешку по темам: формы, than и as, «насколько», «во сколько раз» и язык статей чередуются.")
assert "usedto:" not in s
pathlib.Path("cmp/template.html").write_text(s)
print("ok", len(s))
