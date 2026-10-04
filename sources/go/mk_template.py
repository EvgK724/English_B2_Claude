# Шаблон «go» собираю из шаблона «in / into»: тренажёр тот же,
# вкладка правил — своя: восемь схем с go, с the или без, фразовые глаголы, выражения, ошибки, темы.
import pathlib
s = pathlib.Path("into/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>In или into</title>", "<title>Фразы с go</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
B = lambda t: f'<span class="st">{t}</span>'
O = lambda t: f'<span class="pr">{t}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Место по назначению&nbsp;— без артикля", "go to " + D.join(B(x) for x in ("work", "school", "bed", "hospital")))
         + step(2, "Обычное место в&nbsp;городе&nbsp;— с&nbsp;the", "go to " + D.join(O(x) for x in ("the cinema", "the gym", "the doctor")))
         + step(3, "Совсем без to", "go " + D.join(B(x) for x in ("home", "abroad", "there")))
         + step(4, "Занятие&nbsp;— go + -ing", "go " + D.join(O(x) for x in ("shopping", "swimming", "skiing")))
         + step(5, "Ненадолго&nbsp;— go for a…", "go " + D.join(O(x) for x in ("for a walk", "for a swim")))
         + step(6, "Поездка или режим&nbsp;— go on…", "go on " + D.join([B("holiday"), O("a trip"), O("a diet")]))
         + step(7, "Транспорт&nbsp;— by, пешком&nbsp;— on foot", "go " + D.join([B("by car"), B("by bus"), O("on foot")]))
         + step(8, "Перемена&nbsp;— go + прилагательное", "go " + D.join(O(x) for x in ("grey", "numb", "wrong", "bad"))))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Go</h1>
      <p class="r-sub">Одно слово&nbsp;— десятки сочетаний. Главное&nbsp;— <b>куда</b> (с&nbsp;the или без), <b>чем заняться</b> и&nbsp;<b>go&nbsp;= «стать»</b>. Остальное&nbsp;— фразовые глаголы и&nbsp;выражения, которые проще запомнить целиком.</p>
      <div class="algo">
        <p class="algo-h">Восемь схем</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m">Учиться, лечиться, молиться&nbsp;— <b class="st" lang="en">go to school</b>. Зайти в&nbsp;здание по&nbsp;делу&nbsp;— <b class="pr" lang="en">the school</b>.</p>
        <p class="algo-note">Синим&nbsp;— без артикля или без to, оранжевым&nbsp;— с&nbsp;артиклем или другим словом. Формы: <i lang="en">go&nbsp;— went&nbsp;— gone</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">С&nbsp;the или без</h2>
      <div class="mx-wrap">
<!--__CONTRAST__-->
      </div>
      <h2 class="lbl">Фразовые глаголы</h2>
      <div class="mx-wrap">
<!--__PHRASAL__-->
      </div>
      <h2 class="lbl">Просто запомнить</h2>
      <div class="mx-wrap">
<!--__SET__-->
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

rep('const LS_STATE = "into:state";\nconst LS_SPEAK = "into:autospeak";\nconst LS_TAB = "into:tab";\nconst LS_OPEN = "into:open";',
    'const LS_STATE = "go:state";\nconst LS_SPEAK = "go:autospeak";\nconst LS_TAB = "go:tab";\nconst LS_OPEN = "go:open";')
rep('["apple-mobile-web-app-title", "in / into"],', '["apple-mobile-web-app-title", "go"],')
rep("// ——— Сравнения и значения into: прослушать", "// ——— Пары, фразовые глаголы и выражения: прослушать")
rep("// Новые карточки идут вперемешку по темам: где и куда чередуются — выбирать приходится по смыслу.",
    "// Новые карточки идут вперемешку по темам: схемы с go чередуются — выбирать приходится по смыслу.")
rep('function exText(en){ return en.replace(/[\\[\\]]/g, ""); }',
    'function exText(en){ return en.replace(/\\[([^\\]|]+)(?:\\|b)?\\]/g, "$1"); }')
rep('''// […] — предлог: in и on — синий (где?), into и onto — оранжевый (куда?), остальные подчёркнуты
const PREP_CLS = { in: "st", on: "st", into: "pr", onto: "pr" };
function marked(s){
  const f = document.createDocumentFragment();
  const re = /\\[([^\\]]+)\\]/g;''', '''// […] — ключевая часть (оранжевый), [...|b] — без артикля или без to (синий)
function marked(s){
  const f = document.createDocumentFragment();
  const re = /\\[([^\\]|]+)(?:\\|(b))?\\]/g;''')
rep('f.append(el("span", PREP_CLS[m[1].toLowerCase()] || "hl", m[1]));', 'f.append(el("span", m[2] ? "st" : "pr", m[1]));')
assert "into:" not in s and "PREP_CLS" not in s
pathlib.Path("go/template.html").write_text(s)
print("ok", len(s))
