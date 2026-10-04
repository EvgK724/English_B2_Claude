# Шаблон «can / could / be able to» собираю из шаблона «must / should»: тренажёр тот же,
# вкладка правил — своя: таблица «ситуация → форма», алгоритм, мнемоника, ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("modal/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Must, have to, should</title>", "<title>Can, could, be able to</title>")
rep("  .algo-2{margin-top:12px}\n", '''  .algo-2{margin-top:12px}
  .ct{width:100%;border-collapse:collapse;table-layout:fixed;margin-top:4px}
  .ct col.sit{width:46%}
  .ct th{padding:11px 10px 11px 0;text-align:left;vertical-align:top;font-size:15px;font-weight:600;line-height:1.35;color:var(--text);border-top:1px solid var(--line)}
  .ct td{padding:11px 0;vertical-align:top;border-top:1px solid var(--line)}
  .ct tr:first-child th,.ct tr:first-child td{border-top:0}
  .ct .f{display:block;font-family:var(--serif);font-size:21px;line-height:1.2}
  .ct .e{display:block;margin-top:2px;font-family:var(--serif);font-size:15px;line-height:1.3;color:var(--soft)}
''')

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def cls(t):
    t = t.lower()
    return "good" if ("able" in t or "managed" in t) else "st" if "could" in t else "pr" if "can" in t else "hl"
W = lambda t: f'<span class="{cls(t)}">{t.replace(" ", "&nbsp;")}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Сейчас: умею, могу, можно?", W("can") + D + W("can't"))
         + step(2, "Прошлое: умел вообще?", W("could") + D + W("couldn't"))
         + step(3, "Прошлое: удалось один раз? Could тут нельзя", W("was able to") + D + W("managed to"))
         + step(4, "Будущее, have been, после might, to, -ing?", W("will be able to") + D + W("have been able to")))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Can, could, be able to</h1>
      <p class="r-sub">По-русски всё это «могу, мог, смогу». В&nbsp;английском важно <b>когда</b> и&nbsp;<b>получилось&nbsp;ли на&nbsp;самом деле</b>: «умел вообще» и&nbsp;«смог в&nbsp;тот раз»&nbsp;— разные формы.</p>
      <div class="algo">
        <p class="algo-h">Что выбрать</p>
        <table class="ct">
          <colgroup><col class="sit"><col></colgroup>
          <tbody>
<!--__TABLE__-->
          </tbody>
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как выбрать</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m"><b class="pr" lang="en">can</b>&nbsp;— умею, <b class="st" lang="en">could</b>&nbsp;— умел, <b class="good" lang="en">was able&nbsp;to</b>&nbsp;— смог и&nbsp;сделал.</p>
        <p class="algo-note">«Не смог»&nbsp;— годятся и&nbsp;<i lang="en">couldn’t</i>, и&nbsp;<i lang="en">wasn’t able to</i>. У&nbsp;can всего две формы, остальное&nbsp;— через be able to.</p>
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

rep('const LS_STATE = "modal:state";\nconst LS_SPEAK = "modal:autospeak";\nconst LS_TAB = "modal:tab";\nconst LS_OPEN = "modal:open";',
    'const LS_STATE = "can:state";\nconst LS_SPEAK = "can:autospeak";\nconst LS_TAB = "can:tab";\nconst LS_OPEN = "can:open";')
rep('["apple-mobile-web-app-title", "must/should"],', '["apple-mobile-web-app-title", "can/could"],')
rep("// Новые карточки идут вперемешку по темам: совет, обязанность и запрет чередуются — выбирать приходится по смыслу.",
    "// Новые карточки идут вперемешку по темам: умею, умел, удалось и смогу чередуются — выбирать приходится по смыслу.")
rep('''// […] — модальный глагол: must — оранжевый, have to — синий, should — зелёный, остальные подчёркнуты
function modalCls(t){
  t = t.toLowerCase();
  if (t.includes("should")) return "good";
  if (/ha(ve|s|d|ving) to/.test(t)) return "st";
  if (t.includes("must")) return "pr";
  return "hl";
}''', '''// […] — форма: can — оранжевый, could — синий, be able to и managed to — зелёный, остальные подчёркнуты
function modalCls(t){
  t = t.toLowerCase();
  if (/able|managed/.test(t)) return "good";
  if (t.includes("could")) return "st";
  if (t.includes("can")) return "pr";
  return "hl";
}''')
assert "modal:" not in s
pathlib.Path("can/template.html").write_text(s)
print("ok", len(s))
