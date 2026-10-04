# Шаблон «Мне сделали» собираю из шаблона «Цифры»: тренажёр тот же,
# вкладка правил — своя: формулы (таблица), сам или не сам (шаги), ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("num/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Цифры</title>", "<title>have it done</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
P = lambda t: f'<span class="pr">{t.replace(" ", "&nbsp;")}</span>'
D = ' <span class="sep">·</span> '
nw = lambda t: f'<span class="nw">{t}</span>'
steps = (step(1, "Сделал сам? Обычный глагол", nw("I " + P("fixed") + " the tap") + D + nw("the dentist " + P("filled") + " it"))
         + step(2, "Сделали тебе по&nbsp;просьбе? have + что + V3", nw("I " + P("had") + " the tap " + P("fixed")) + D + nw(P("got") + " it " + P("done")))
         + step(3, "Случилось против воли? То&nbsp;же самое", nw("I " + P("had") + " my bag " + P("stolen"))))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">have it done</h1>
      <p class="r-sub">Когда делаешь не&nbsp;сам, а&nbsp;тебе делают&nbsp;— врач, мастер, сервис: <b>have + что + V3</b>. <i lang="en">I had my eyes tested</i>&nbsp;— мне проверили зрение. Сюда&nbsp;же «у&nbsp;меня украли», «поручить», «заставить» и&nbsp;«сделать МРТ».</p>
      <div class="algo">
        <p class="algo-h">Формулы</p>
        <table class="vt sv">
          <colgroup><col class="v"><col></colgroup>
          <tbody>
<!--__WORDS__-->
          </tbody>
        </table>
        <p class="algo-note">После <i lang="en">have, make, let</i> + кого&nbsp;— глагол без <i lang="en">to</i>. После <i lang="en">get</i> + кого&nbsp;— с&nbsp;<i lang="en">to</i>.</p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Сам или не сам</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m">Что&nbsp;— посередине: <b class="pr" lang="en">had</b> <i lang="en">my car</i> <b class="st" lang="en">repaired</b>. Переставишь&nbsp;— выйдет «починил сам»: <i lang="en">had repaired my car</i>.</p>
        <p class="algo-note">Сделать МРТ пациенту&nbsp;— <i lang="en">have an MRI</i>, не&nbsp;<i lang="en">make</i>.</p>
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

rep('const LS_STATE = "num:state";\nconst LS_SPEAK = "num:autospeak";\nconst LS_TAB = "num:tab";\nconst LS_OPEN = "num:open";',
    'const LS_STATE = "hsd:state";\nconst LS_SPEAK = "hsd:autospeak";\nconst LS_TAB = "hsd:tab";\nconst LS_OPEN = "hsd:open";')
rep('["apple-mobile-web-app-title", "Цифры"],', '["apple-mobile-web-app-title", "have it done"],')
rep("// Новые карточки идут вперемешку по темам: by и to, fewer и less, во сколько раз, доли и запись чисел чередуются.",
    "// Новые карточки идут вперемешку по темам: have it done, времена, get, неприятность, сам или нет, make и let, «сделать МРТ» чередуются.")
assert "num:state" not in s and "Цифры" not in s
pathlib.Path("hsd/template.html").write_text(s)
print("ok", len(s))
