# Шаблон «Синонимы» собираю из шаблона «have, take, pay»: тренажёр тот же,
# вкладка правил — своя: таблицы пар, «выиграть — заработать», «взять — нести — носить», группы «старый» и «один» с озвучкой.
import pathlib
s = pathlib.Path("htp/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Have, take, pay</title>", "<title>Синонимы</title>")
rep("  .vt .w.st{color:var(--blue)}\n", "  .vt .w.st{color:var(--blue)}\n  .vt tr.pb th,.vt tr.pb td{border-top:0;padding-top:0}\n")

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
def table(key):
    return f'''        <table class="vt">
          <colgroup><col class="v"><col></colgroup>
          <tbody>
<!--__{key}__-->
          </tbody>
        </table>
'''
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Synonyms</h1>
      <p class="r-sub">Синонимы часто взаимозаменяемы, но в&nbsp;устойчивых сочетаниях годится только один: <i lang="en">start the car</i>, но <i lang="en">the universe began</i>. <b>Учи слово вместе с&nbsp;соседом</b>.</p>
      <div class="algo">
        <p class="algo-h">Пары: что с&nbsp;чем</p>
''' + table("PAIRS") + '''      </div>
      <div class="algo algo-2">
        <p class="algo-h">Выиграть, получить, заработать</p>
''' + table("WIN") + '''        <p class="algo-m"><b class="pr" lang="en">win</b> что-то, <b class="st" lang="en">beat</b> кого-то: <i lang="en">win the match, beat the team</i>.</p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Взять, нести, носить</p>
''' + table("CARRY") + '''        <p class="algo-m">На&nbsp;тебе&nbsp;— <b class="pr" lang="en">wear</b>, в&nbsp;руках или в&nbsp;кармане&nbsp;— <b class="st" lang="en">carry</b>, берёшь с&nbsp;собой&nbsp;— <b class="good" lang="en">take</b>.</p>
        <p class="algo-note">Проводить время и&nbsp;тратить деньги&nbsp;— <i lang="en">spend</i>, не&nbsp;pass и&nbsp;не&nbsp;use.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">«Старый»</h2>
      <div class="mx-wrap">
<!--__OLD__-->
      </div>
      <h2 class="lbl">«Один, единственный»</h2>
      <div class="mx-wrap">
<!--__ALONE__-->
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

rep('const LS_STATE = "htp:state";\nconst LS_SPEAK = "htp:autospeak";\nconst LS_TAB = "htp:tab";\nconst LS_OPEN = "htp:open";',
    'const LS_STATE = "syn:state";\nconst LS_SPEAK = "syn:autospeak";\nconst LS_TAB = "syn:tab";\nconst LS_OPEN = "syn:open";')
rep('["apple-mobile-web-app-title", "have/take/pay"],', '["apple-mobile-web-app-title", "Синонимы"],')
rep("// ——— Шпаргалка и ситуации: прослушать", "// ——— Группы слов и ситуации: прослушать")
rep("// Новые карточки идут вперемешку по темам: have, take и pay чередуются — выбирать глагол приходится по сочетанию.",
    "// Новые карточки идут вперемешку по темам: пары, группы слов и глаголы чередуются — выбирать приходится по сочетанию.")
rep('''// […] — сочетание: have — оранжевый, take — синий, pay — зелёный, остальные подчёркнуты
const VERB_CLS = {};
[["pr", "have has had having"], ["st", "take takes took taken taking"], ["good", "pay pays paid paying"]]
  .forEach(([cls, forms]) => forms.split(" ").forEach(w => { VERB_CLS[w] = cls; }));
function modalCls(t){ return VERB_CLS[String(t).split(" ")[0].toLowerCase()] || "hl"; }''', '''// […] — слово в фокусе (оранжевый)
function modalCls(){ return "pr"; }''')
assert "htp:" not in s and "VERB_CLS" not in s
pathlib.Path("syn/template.html").write_text(s)
print("ok", len(s))
