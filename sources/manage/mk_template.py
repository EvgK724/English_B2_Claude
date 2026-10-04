# Шаблон «manage to и похожие» собираю из шаблона «can / could»: тренажёр тот же,
# вкладка правил — своя: таблица «глагол → конструкция», алгоритм по смыслу, ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("can/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Can, could, be able to</title>", "<title>Manage to и похожие</title>")
rep("  .ct .e{display:block;margin-top:2px;font-family:var(--serif);font-size:15px;line-height:1.3;color:var(--soft)}\n",
    '''  .ct .e{display:block;margin-top:2px;font-family:var(--serif);font-size:15px;line-height:1.3;color:var(--soft)}
  .vt{width:100%;border-collapse:collapse;table-layout:fixed;margin-top:4px}
  .vt col.v{width:40%}
  .vt th{padding:10px 10px 10px 0;text-align:left;vertical-align:top;border-top:1px solid var(--line)}
  .vt td{padding:10px 0;vertical-align:top;border-top:1px solid var(--line)}
  .vt tr:first-child th,.vt tr:first-child td{border-top:0}
  .vt .w{display:block;font-family:var(--serif);font-weight:400;font-size:21px;line-height:1.15;color:var(--accent)}
  .vt .p{display:block;margin-top:2px;font-size:13px;font-weight:600;line-height:1.3;color:var(--blue)}
  .vt .e{display:block;font-family:var(--serif);font-size:16px;line-height:1.3;color:var(--text)}
  .vt .r{display:block;margin-top:2px;font-size:13px;line-height:1.35;color:var(--muted)}
''')

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
O = lambda t: f'<span class="pr">{t.replace(" ", "&nbsp;")}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Удалось, хоть и&nbsp;с&nbsp;трудом?", O("managed to") + D + O("succeeded in") + " <i>-ing</i>")
         + step(2, "Не удалось?", O("didn't manage to") + D + O("failed to"))
         + step(3, "Справляться с&nbsp;чем-то?", O("cope with") + D + O("deal with") + D + O("handle"))
         + step(4, "Успеть, добраться, выжить?", O("make it")))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Manage to</h1>
      <p class="r-sub">«Удалось», «не получилось», «справился», «успел»&nbsp;— у&nbsp;каждого глагола своя конструкция. <b>Запоминай глагол вместе с&nbsp;тем, что после него</b>.</p>
      <div class="algo">
        <p class="algo-h">Что с чем</p>
        <table class="vt">
          <colgroup><col class="v"><col></colgroup>
          <tbody>
<!--__TABLE__-->
          </tbody>
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как выбрать</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m">manage <b class="st" lang="en">to</b>, succeed <b class="st" lang="en">in</b>, fail <b class="st" lang="en">to</b>, cope и&nbsp;deal <b class="st" lang="en">with</b>, handle&nbsp;— без всего.</p>
        <p class="algo-note">Об одной удаче в&nbsp;прошлом could не&nbsp;говорят: <i lang="en">We managed to catch the train</i>.</p>
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

rep('const LS_STATE = "can:state";\nconst LS_SPEAK = "can:autospeak";\nconst LS_TAB = "can:tab";\nconst LS_OPEN = "can:open";',
    'const LS_STATE = "manage:state";\nconst LS_SPEAK = "manage:autospeak";\nconst LS_TAB = "manage:tab";\nconst LS_OPEN = "manage:open";')
rep('["apple-mobile-web-app-title", "can/could"],', '["apple-mobile-web-app-title", "manage to"],')
rep("// Новые карточки идут вперемешку по темам: умею, умел, удалось и смогу чередуются — выбирать приходится по смыслу.",
    "// Новые карточки идут вперемешку по темам: удалось, справиться и успеть чередуются — выбирать приходится по смыслу и конструкции.")
rep('''// […] — форма: can — оранжевый, could — синий, be able to и managed to — зелёный, остальные подчёркнуты
function modalCls(t){
  t = t.toLowerCase();
  if (/able|managed/.test(t)) return "good";
  if (t.includes("could")) return "st";
  if (t.includes("can")) return "pr";
  return "hl";
}''', '''// […] — конструкция в фокусе (оранжевый)
function modalCls(){ return "pr"; }''')
assert "can:" not in s
pathlib.Path("manage/template.html").write_text(s)
print("ok", len(s))
