# Шаблон «Have to, must и похожие» собираю из шаблона «must / have to / should» (modal): тренажёр тот же,
# вкладка правил — своя: таблица из восьми глаголов (глагол строкой над «утверждением» и «отрицанием»),
# алгоритм выбора, мнемоника; ситуации, ошибки и темы — как в modal.
# Запуск из sources/: python3 oblig/mk_template.py
import pathlib
s = pathlib.Path("modal/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Must, have to, should</title>", "<title>Have to, must и похожие</title>")
rep("  .algo-2{margin-top:12px}\n", '''  .algo-2{margin-top:12px}
  .mt.vt col{width:50%}
  .mt.vt tbody th{padding:12px 0 2px;font-size:22px;line-height:1.2;border-top:1px solid var(--line)}
  .mt.vt tbody td{padding:2px 12px 12px 0;border-top:0}
  .mt.vt tbody td + td{padding-right:0}
  .mt.vt thead th{padding-left:0}
  .mt.vt td .f{font-size:18px;overflow-wrap:anywhere}
  .lvl{display:inline-block;margin-left:6px;padding:1px 7px;border-radius:999px;border:1px solid var(--line-2);font-size:12px;font-weight:600;letter-spacing:.04em;color:var(--muted);vertical-align:2px}
''')

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    return f'<span class="{c}">{t.replace(" ", "&nbsp;")}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Прошлое, будущее, «пришлось&nbsp;бы»? У&nbsp;must таких форм нет", W("had to", "st") + D + W("will have to", "st") + D + W("would have to", "st"))
         + step(2, "Отрицание: запрещено или просто не&nbsp;нужно?", W("mustn't", "pr") + D + W("don't have to", "st") + D + W("needn't", "hl"))
         + step(3, "Так задумано, а&nbsp;могло не&nbsp;случиться?", W("be supposed to", "hl") + D + W("was supposed to", "hl"))
         + step(4, "Предупреждение «а&nbsp;то будет плохо»?", W("had better", "good") + D + W("had better not", "good"))
         + step(5, "Против воли, под давлением?", W("be forced to", "hl") + D + W("be made to", "hl"))
         + step(6, "Официальный текст, протокол, закон?", W("be required to", "hl") + D + W("be obliged to", "hl")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Have to, must и&nbsp;похожие</h1>
      <p class="r-sub">По-русски почти всё это&nbsp;— «должен» и&nbsp;«надо». По-английски выбор зависит от&nbsp;того, <b>кто решил</b>, <b>когда</b> и&nbsp;<b>насколько официально</b>. Темы идут от&nbsp;B1 к&nbsp;B2.</p>
      <div class="algo">
        <p class="algo-h">Главная таблица</p>
        <table class="mt vt">
          <colgroup><col><col></colgroup>
          <thead><tr><th scope="col">Утверждение</th><th scope="col">Отрицание</th></tr></thead>
<!--__TABLE__-->
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как выбрать</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m"><b class="pr" lang="en">must</b>&nbsp;— сам себе приказал, <b class="st" lang="en">have&nbsp;to</b>&nbsp;— жизнь заставила, <b class="hl" lang="en">supposed&nbsp;to</b>&nbsp;— так задумано, <b class="hl" lang="en">forced&nbsp;to</b>&nbsp;— припёрли к&nbsp;стенке, <b class="good" lang="en">had&nbsp;better</b>&nbsp;— а&nbsp;то хуже будет.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "modal:state";\nconst LS_SPEAK = "modal:autospeak";\nconst LS_TAB = "modal:tab";\nconst LS_OPEN = "modal:open";',
    'const LS_STATE = "oblig:state";\nconst LS_SPEAK = "oblig:autospeak";\nconst LS_TAB = "oblig:tab";\nconst LS_OPEN = "oblig:open";')
rep('["apple-mobile-web-app-title", "must/should"],', '["apple-mobile-web-app-title", "have to"],')
rep("// Новые карточки идут вперемешку по темам: совет, обязанность и запрет чередуются — выбирать приходится по смыслу.",
    "// Новые карточки идут вперемешку по темам: сначала B1, темы B1+ и B2 (поле late) вступают позже.")
rep('''// […] — модальный глагол: must — оранжевый, have to — синий, should — зелёный, остальные подчёркнуты
function modalCls(t){
  t = t.toLowerCase();
  if (t.includes("should")) return "good";
  if (/ha(ve|s|d|ving) to/.test(t)) return "st";
  if (t.includes("must")) return "pr";
  return "hl";
}''', '''// […] — ключевой глагол: must — оранжевый, have (got) to — синий, should, ought to, had better — зелёный, остальные подчёркнуты
function modalCls(t){
  t = t.toLowerCase();
  if (/should|better|ought/.test(t)) return "good";
  if (t.includes("must")) return "pr";
  if (/^ha(ve|s|d)$/.test(t) || /\\bha(ve|s|d|ving) to\\b|got to|gotta/.test(t)) return "st";
  return "hl";
}''')
assert "modal:" not in s
pathlib.Path("oblig/template.html").write_text(s)
print("ok", len(s))
