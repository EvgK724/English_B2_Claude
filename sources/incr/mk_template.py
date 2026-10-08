# Шаблон «Increase by и increase to» собираю из шаблона «Have to, must и похожие» (oblig): тренажёр тот же,
# вкладка правил — своя: таблица «предлог — вопрос — пример», алгоритм выбора, мнемоника.
# Запуск из sources/: python3 incr/mk_template.py   (нужен oblig/template.html — python3 oblig/mk_template.py)
import pathlib
s = pathlib.Path("oblig/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Have to, must и похожие</title>", "<title>Increase by и increase to</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    # короткие формулы не переносим, длинные (an increase in mortality) — переносим, иначе на 320 px вылезут за край
    return f'<span class="{c}">{t.replace(" ", "&nbsp;") if len(t) <= 16 else t}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Называете разницу, «на&nbsp;сколько»?", W("by 10%", "pr") + D + W("a rise of 10%", "good"))
         + step(2, "Называете итог, «до&nbsp;какого значения»?", W("to 30%", "st") + D + W("from 20% to 30%", "st"))
         + step(3, "После существительного: рост чего?", W("an increase in mortality", "good"))
         + step(4, "Уровень в&nbsp;точке: пик, плато, при поступлении?", W("peaked at", "hl") + D + W("stood at", "hl") + D + W("remained at", "hl"))
         + step(5, "Меняется сам процент?", W("percentage points", "hl") + D + W("a relative increase of 50%", "good")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Increase by и&nbsp;increase to</h1>
      <p class="r-sub">По-русски «на» и&nbsp;«до» не&nbsp;спутать, а&nbsp;по-английски их&nbsp;путают постоянно: <b lang="en">by</b>&nbsp;— на&nbsp;сколько, <b lang="en">to</b>&nbsp;— до&nbsp;какого значения. Дальше&nbsp;— предлоги после существительных, глаголы, тренды, проценты и&nbsp;пункты, как в&nbsp;статьях. Темы идут от&nbsp;B1 к&nbsp;B2.</p>
      <div class="algo">
        <p class="algo-h">Главная таблица</p>
        <table class="mt vt">
          <colgroup><col><col></colgroup>
          <thead><tr><th scope="col">Вопрос</th><th scope="col">Пример</th></tr></thead>
<!--__TABLE__-->
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как выбрать</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m"><b class="pr" lang="en">by</b>&nbsp;— на&nbsp;сколько шагнул, <b class="st" lang="en">to</b>&nbsp;— куда пришёл, <b class="hl" lang="en">at</b>&nbsp;— где стоит, <b class="good" lang="en">in</b>&nbsp;— в&nbsp;чём, <b class="good" lang="en">of</b>&nbsp;— сколько.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "oblig:state";\nconst LS_SPEAK = "oblig:autospeak";\nconst LS_TAB = "oblig:tab";\nconst LS_OPEN = "oblig:open";',
    'const LS_STATE = "incr:state";\nconst LS_SPEAK = "incr:autospeak";\nconst LS_TAB = "incr:tab";\nconst LS_OPEN = "incr:open";')
rep('["apple-mobile-web-app-title", "have to"],', '["apple-mobile-web-app-title", "increase by"],')
i = s.index("// […] — ключевой глагол"); j = s.index("\n}\n", i) + 3
s = s[:i] + '''// […] — предлог в фокусе: by — оранжевый, to и from — синий, in и of — зелёный, остальные подчёркнуты
function modalCls(t){
  t = t.toLowerCase();
  if (/\\bby\\b/.test(t)) return "pr";
  if (/\\b(to|from)\\b/.test(t)) return "st";
  if (/\\b(in|of)\\b/.test(t)) return "good";
  return "hl";
}
''' + s[j:]
assert "oblig:" not in s and "havea" not in s and "must" not in s[s.index("function modalCls"):s.index("function modalCls") + 400]
pathlib.Path("incr/template.html").write_text(s)
print("ok", len(s))
