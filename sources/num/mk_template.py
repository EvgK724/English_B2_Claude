# Шаблон «Цифры» собираю из шаблона «Который»: тренажёр тот же,
# вкладка правил — своя: на или до (шаги), сколько и во сколько раз (таблица), ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("rel/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Который</title>", "<title>Цифры</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
P = lambda t: f'<span class="pr">{t.replace(" ", "&nbsp;")}</span>'
D = ' <span class="sep">·</span> '
nw = lambda t: f'<span class="nw">{t}</span>'
steps = (step(1, "На сколько изменилось?", nw("rose " + P("by") + " 10%") + D + nw("fell " + P("by") + " half"))
         + step(2, "Какое стало значение?", nw("rose " + P("to") + " 40%") + D + nw(P("from") + " 12% " + P("to") + " 8%"))
         + step(3, "После существительного?", nw("an increase " + P("of") + " 10%") + D + nw("a fall " + P("in") + " mortality")))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Numbers in results</h1>
      <p class="r-sub">В результатах всё решают маленькие слова: <i lang="en">rose by 10%</i>&nbsp;— выросла на&nbsp;10%, <i lang="en">rose to 10%</i>&nbsp;— выросла до&nbsp;10%. Ещё&nbsp;— fewer или less, «во&nbsp;сколько раз» и&nbsp;как писать сами числа.</p>
      <div class="algo">
        <p class="algo-h">На или до</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m"><b class="pr" lang="en">by</b> — на сколько, <b class="st" lang="en">to</b> — до скольких.</p>
        <p class="algo-note"><i lang="en">up to</i>&nbsp;— «до» только в&nbsp;смысле «не&nbsp;больше»: <i lang="en">up to three doses a day</i>.</p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Сколько и во сколько раз</p>
        <table class="vt sv">
          <colgroup><col class="v"><col></colgroup>
          <tbody>
<!--__WORDS__-->
          </tbody>
        </table>
        <p class="algo-note">Вдвое меньше&nbsp;— <i lang="en">half as many</i>, не&nbsp;<i lang="en">twice less</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Одна цифра&nbsp;— разный смысл</h2>
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

rep('const LS_STATE = "rel:state";\nconst LS_SPEAK = "rel:autospeak";\nconst LS_TAB = "rel:tab";\nconst LS_OPEN = "rel:open";',
    'const LS_STATE = "num:state";\nconst LS_SPEAK = "num:autospeak";\nconst LS_TAB = "num:tab";\nconst LS_OPEN = "num:open";')
rep('["apple-mobile-web-app-title", "Который"],', '["apple-mobile-web-app-title", "Цифры"],')
rep("// Новые карточки идут вперемешку по темам: who и which, запятые, пропуск «который», предлоги и what чередуются.",
    "// Новые карточки идут вперемешку по темам: by и to, fewer и less, во сколько раз, доли и запись чисел чередуются.")
assert "rel:state" not in s and "Который" not in s
pathlib.Path("num/template.html").write_text(s)
print("ok", len(s))
