# Шаблон «Have a look, take a seat» собираю из шаблона «Have to, must и похожие» (oblig): тренажёр тот же,
# вкладка правил — своя: таблица «глагол — оттенок — с чем сочетается», алгоритм выбора, мнемоника.
# Запуск из sources/: python3 havea/mk_template.py   (нужен oblig/template.html — python3 oblig/mk_template.py)
import pathlib
s = pathlib.Path("oblig/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Have to, must и похожие</title>", "<title>Have a look, take a seat</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    return f'<span class="{c}">{t.replace(" ", "&nbsp;")}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Сказать мягче и&nbsp;по-свойски: «гляну, подумаю, передохну»?", W("have a look", "pr") + D + W("have a think", "pr") + D + W("have a rest", "pr"))
         + step(2, "Пригласить: сесть, попробовать, угоститься?", W("Have a seat", "pr") + D + W("Have a go", "pr") + D + W("Take a seat", "st"))
         + step(3, "Действие на&nbsp;кого-то или на&nbsp;что-то?", W("give me a call", "good") + D + W("give it a try", "good"))
         + step(4, "Нужно «быстро, глубоко, хорошенько»? Прилагательное внутри", W("a quick look", "pr") + D + W("a deep breath", "st"))
         + step(5, "Прогулка, пробежка, купание?", W("go for a walk", "hl") + D + W("go for a swim", "hl")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Have a look, take a seat</h1>
      <p class="r-sub">Глагол почти пустой, смысл несёт существительное: <b lang="en">look → have a&nbsp;look</b>. Получается одно короткое действие, сказанное мягче и&nbsp;по-свойски. Глагол к&nbsp;каждому слову запоминают вместе с&nbsp;ним. Темы идут от&nbsp;B1 к&nbsp;B2.</p>
      <div class="algo">
        <p class="algo-h">Главная таблица</p>
        <table class="mt vt">
          <colgroup><col><col></colgroup>
          <thead><tr><th scope="col">Оттенок</th><th scope="col">С чем</th></tr></thead>
<!--__TABLE__-->
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как выбрать</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m"><b class="pr" lang="en">have</b>&nbsp;— сам себе, по-свойски, <b class="st" lang="en">take</b>&nbsp;— сделал один шаг, <b class="good" lang="en">give</b>&nbsp;— подарил действие кому-то, <b class="hl" lang="en">go&nbsp;for</b>&nbsp;— вышел ради этого.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "oblig:state";\nconst LS_SPEAK = "oblig:autospeak";\nconst LS_TAB = "oblig:tab";\nconst LS_OPEN = "oblig:open";',
    'const LS_STATE = "havea:state";\nconst LS_SPEAK = "havea:autospeak";\nconst LS_TAB = "havea:tab";\nconst LS_OPEN = "havea:open";')
rep('["apple-mobile-web-app-title", "have to"],', '["apple-mobile-web-app-title", "have a look"],')
i = s.index("// […] — ключевой глагол"); j = s.index("\n}\n", i) + 3
s = s[:i] + '''// […] — конструкция: have — оранжевый, take — синий, give — зелёный, остальные подчёркнуты
function modalCls(t){
  t = t.toLowerCase();
  if (/\\bha(ve|s|d|ving)\\b/.test(t)) return "pr";
  if (/\\bt(ake|akes|ook|aken|aking)\\b/.test(t)) return "st";
  if (/\\bg(ive|ives|ave|iven|iving)\\b/.test(t)) return "good";
  return "hl";
}
''' + s[j:]
assert "oblig:" not in s and "must" not in s[s.index("function modalCls"):s.index("function modalCls") + 400]
pathlib.Path("havea/template.html").write_text(s)
print("ok", len(s))
