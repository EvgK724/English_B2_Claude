# Шаблон «have, take, pay» собираю из шаблона «manage to»: тренажёр тот же,
# вкладка правил — своя: алгоритм выбора глагола, «что после», шпаргалка по глаголам с озвучкой, ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("manage/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Manage to и похожие</title>", "<title>Have, take, pay</title>")
rep("  .vt .p{", '''  .vt .w.st{color:var(--blue)}
  .vt .w.good{color:var(--yes-text)}
  .wd-w{margin:0;line-height:1.3}
  .wd-w .ph{margin-right:6px;font-family:var(--serif);font-size:21px}
  .wd-ru{font-size:15px;color:var(--muted)}
  .wd-p{margin:3px 0 0;font-family:var(--serif);font-size:17px;line-height:1.35;color:var(--soft)}
  .vt .p{''')

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
D = ' <span class="sep">·</span> '
def f(cls, verb, *rest):
    parts = [r.replace(" ", "&nbsp;") for r in rest]
    parts[-2:] = [parts[-2] + '&nbsp;<span class="sep">·</span>&nbsp;' + parts[-1]]   # последнее слово не остаётся одно на строке
    return f'<span class="{cls}">{verb}</span> ' + D.join(parts)
steps = (step(1, "Можно сказать «у&nbsp;меня был(о)…»?", f("pr", "have", "an accident", "a dream", "a chat", "fun"))
         + step(2, "«Беру» или «принимаю»: транспорт, фото, риск, меры?", f("st", "take", "a bus", "a photo", "a risk", "action"))
         + step(3, "«Плачу» вниманием или уважением?", f("good", "pay", "attention", "a compliment", "tribute")))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Have, take, pay</h1>
      <p class="r-sub">По-русски мы «делаем» перерыв, фото и&nbsp;комплимент, «попадаем» в&nbsp;аварию и&nbsp;«видим» сон. По-английски в&nbsp;этих выражениях свой глагол&nbsp;— <b>запоминай его вместе с&nbsp;существительным</b>.</p>
      <div class="algo">
        <p class="algo-h">Как выбрать</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m">Было&nbsp;— <b class="pr" lang="en">have</b>, беру&nbsp;— <b class="st" lang="en">take</b>, плачу вниманием&nbsp;— <b class="good" lang="en">pay</b>.</p>
        <p class="algo-note">make и&nbsp;get здесь не&nbsp;подходят: <i lang="en">make a photo, make a party, get an accident</i>&nbsp;— ошибки.</p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Что после</p>
        <table class="vt">
          <colgroup><col class="v"><col></colgroup>
          <tbody>
<!--__TABLE__-->
          </tbody>
        </table>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl"><span class="pr" lang="en">have</span>&nbsp;— «у&nbsp;меня было»</h2>
      <div class="mx-wrap">
<!--__HAVE__-->
      </div>
      <h2 class="lbl"><span class="st" lang="en">take</span>&nbsp;— «беру, принимаю»</h2>
      <div class="mx-wrap">
<!--__TAKE__-->
      </div>
      <h2 class="lbl"><span class="good" lang="en">pay</span>&nbsp;— «плачу вниманием»</h2>
      <div class="mx-wrap">
<!--__PAY__-->
      </div>
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

rep('const LS_STATE = "manage:state";\nconst LS_SPEAK = "manage:autospeak";\nconst LS_TAB = "manage:tab";\nconst LS_OPEN = "manage:open";',
    'const LS_STATE = "htp:state";\nconst LS_SPEAK = "htp:autospeak";\nconst LS_TAB = "htp:tab";\nconst LS_OPEN = "htp:open";')
rep('["apple-mobile-web-app-title", "manage to"],', '["apple-mobile-web-app-title", "have/take/pay"],')
rep("// ——— Ситуации: прослушать", "// ——— Шпаргалка и ситуации: прослушать")
rep("// Новые карточки идут вперемешку по темам: удалось, справиться и успеть чередуются — выбирать приходится по смыслу и конструкции.",
    "// Новые карточки идут вперемешку по темам: have, take и pay чередуются — выбирать глагол приходится по сочетанию.")
rep('''// […] — конструкция в фокусе (оранжевый)
function modalCls(){ return "pr"; }''', '''// […] — сочетание: have — оранжевый, take — синий, pay — зелёный, остальные подчёркнуты
const VERB_CLS = {};
[["pr", "have has had having"], ["st", "take takes took taken taking"], ["good", "pay pays paid paying"]]
  .forEach(([cls, forms]) => forms.split(" ").forEach(w => { VERB_CLS[w] = cls; }));
function modalCls(t){ return VERB_CLS[String(t).split(" ")[0].toLowerCase()] || "hl"; }''')
assert "manage:" not in s
pathlib.Path("htp/template.html").write_text(s)
print("ok", len(s))
