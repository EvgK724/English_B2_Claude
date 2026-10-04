# Шаблон «must / have to / should» собираю из шаблона «go»: тренажёр тот же,
# вкладка правил — своя: таблица «утверждение / отрицание», алгоритм выбора, мнемоника, ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("go/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Фразы с go</title>", "<title>Must, have to, should</title>")
rep("  .algo-m b.st{color:var(--blue)}\n", '''  .algo-m b.st{color:var(--blue)}
  .algo-m b.good{color:var(--yes-text)}
  .mt{width:100%;border-collapse:collapse;table-layout:fixed;margin-top:6px}
  .mt col.rh{width:92px}
  .mt thead th{padding:2px 6px 8px;font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);text-align:left}
  .mt tbody th{padding:12px 6px 12px 0;text-align:left;vertical-align:top;font-family:var(--serif);font-weight:400;font-size:24px;line-height:1.15;border-top:1px solid var(--line)}
  .mt td{padding:12px 6px;vertical-align:top;font-size:15px;line-height:1.4;color:var(--soft);border-top:1px solid var(--line)}
  .mt td .f{display:block;margin-bottom:2px;font-family:var(--serif);font-size:19px;line-height:1.2}
  .mt td b{color:var(--text);font-weight:600}
  .mt td b.h{display:block;margin-bottom:2px}
  .mt thead td{border-top:0}
  .cp-en + .cp-ru + .cp-en{margin-top:8px}
  .algo-2{margin-top:12px}
''')

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
C = {"must": "pr", "mustn't": "pr", "have to": "st", "don't have to": "st", "had to": "st", "will have to": "st", "should": "good", "shouldn't": "good"}
W = lambda t: f'<span class="{C[t]}">{t.replace(" ", "&nbsp;")}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Это совет, «стоит»?", W("should") + D + W("shouldn't"))
         + step(2, "Это обязанность? В&nbsp;речи&nbsp;— have to; решил сам или строгая инструкция&nbsp;— must", W("have to") + D + W("must"))
         + step(3, "Отрицание: запрещено или просто не&nbsp;нужно?", W("mustn't") + D + W("don't have to"))
         + step(4, "Прошлое или будущее? Только have to", W("had to") + D + W("will have to")))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Must, have to, should</h1>
      <p class="r-sub">По-русски всё это «должен». В&nbsp;утверждении разница в&nbsp;оттенке, <b>в&nbsp;отрицании&nbsp;— в&nbsp;смысле</b>: «нельзя» и&nbsp;«не нужно»&nbsp;— противоположные вещи.</p>
      <div class="algo">
        <p class="algo-h">Главная таблица</p>
        <table class="mt">
          <colgroup><col class="rh"><col><col></colgroup>
          <thead><tr><td></td><th scope="col">Утверждение</th><th scope="col">Отрицание</th></tr></thead>
          <tbody>
<!--__TABLE__-->
          </tbody>
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как выбрать</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m"><b class="pr" lang="en">must</b>&nbsp;— сам себе приказал, <b class="st" lang="en">have&nbsp;to</b>&nbsp;— жизнь заставила, <b class="good" lang="en">should</b>&nbsp;— совет друга.</p>
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

rep('const LS_STATE = "go:state";\nconst LS_SPEAK = "go:autospeak";\nconst LS_TAB = "go:tab";\nconst LS_OPEN = "go:open";',
    'const LS_STATE = "modal:state";\nconst LS_SPEAK = "modal:autospeak";\nconst LS_TAB = "modal:tab";\nconst LS_OPEN = "modal:open";')
rep('["apple-mobile-web-app-title", "go"],', '["apple-mobile-web-app-title", "must/should"],')
rep("// ——— Пары, фразовые глаголы и выражения: прослушать", "// ——— Ситуации: прослушать")
rep("// Новые карточки идут вперемешку по темам: схемы с go чередуются — выбирать приходится по смыслу.",
    "// Новые карточки идут вперемешку по темам: совет, обязанность и запрет чередуются — выбирать приходится по смыслу.")
rep('function exText(en){ return en.replace(/\\[([^\\]|]+)(?:\\|b)?\\]/g, "$1"); }', 'function exText(en){ return en.replace(/[\\[\\]]/g, ""); }')
rep('''// […] — ключевая часть (оранжевый), [...|b] — без артикля или без to (синий)
function marked(s){
  const f = document.createDocumentFragment();
  const re = /\\[([^\\]|]+)(?:\\|(b))?\\]/g;''', '''// […] — модальный глагол: must — оранжевый, have to — синий, should — зелёный, остальные подчёркнуты
function modalCls(t){
  t = t.toLowerCase();
  if (t.includes("should")) return "good";
  if (/ha(ve|s|d|ving) to/.test(t)) return "st";
  if (t.includes("must")) return "pr";
  return "hl";
}
function marked(s){
  const f = document.createDocumentFragment();
  const re = /\\[([^\\]]+)\\]/g;''')
rep('f.append(el("span", m[2] ? "st" : "pr", m[1]));', 'f.append(el("span", modalCls(m[1]), m[1]));')
assert "go:" not in s
pathlib.Path("modal/template.html").write_text(s)
print("ok", len(s))
