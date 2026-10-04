# Шаблон «Погода» собираю из шаблона «Синонимы»: тренажёр тот же,
# вкладка правил — своя: таблица «сильный / слабый», «погода меняется», шпаргалка по разделам с озвучкой, ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("syn/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Синонимы</title>", "<title>Погода</title>")
rep("  .mt thead td{border-top:0}\n", '''  .mt thead td{border-top:0}
  .mt tbody th small{display:block;margin-top:3px;font-family:var(--sans);font-size:12px;line-height:1.2;color:var(--muted)}
  .mt.wx col.rh{width:78px}
  .mt.wx td .f{font-size:18px}
  .mt td i{display:block;font-family:var(--serif);font-style:normal;font-size:15px;line-height:1.3;color:var(--soft)}
  .mt td small{display:block;margin-top:2px;font-size:13px;line-height:1.3;color:var(--muted)}
  .mt td small i{display:inline;font-size:13px;color:var(--soft)}
''')

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
def sheet(title, key):
    return f'''      <h2 class="lbl">{title}</h2>
      <div class="mx-wrap">
<!--__{key}__-->
      </div>
'''
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Weather</h1>
      <p class="r-sub">Погоду описывают устойчивыми парами. Главная ловушка&nbsp;— слово «сильный»: <b>heavy rain, но&nbsp;strong wind</b>. Его выбирают по&nbsp;существительному.</p>
      <div class="algo">
        <p class="algo-h">Сильный или слабый</p>
        <table class="mt wx">
          <colgroup><col class="rh"><col><col></colgroup>
          <thead><tr><td></td><th scope="col">сильный</th><th scope="col">слабый</th></tr></thead>
          <tbody>
<!--__STRENGTH__-->
          </tbody>
        </table>
        <p class="algo-m">Падает&nbsp;— <b class="pr" lang="en">heavy</b>, дует или светит&nbsp;— <b class="pr" lang="en">strong</b>, висит&nbsp;— <b class="pr" lang="en">thick</b>, мороз&nbsp;— <b class="pr" lang="en">hard</b>.</p>
        <p class="algo-note">Слабое почти всегда&nbsp;— <i lang="en">light</i>, только солнце&nbsp;— <i lang="en">weak</i>. <i lang="en">Strong rain</i> и&nbsp;<i lang="en">soft frost</i>&nbsp;— ошибки.</p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Погода меняется</p>
        <table class="mt wx">
          <colgroup><col class="rh"><col><col></colgroup>
          <thead><tr><td></td><th scope="col">хуже, сильнее</th><th scope="col">лучше, слабее</th></tr></thead>
          <tbody>
<!--__CHANGES__-->
          </tbody>
        </table>
        <p class="algo-note"><i lang="en">Deteriorate</i>&nbsp;— официально; так же говорят о&nbsp;состоянии пациента: <i lang="en">his condition deteriorated</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
''' + sheet("Солнце и жара", "SUN") + sheet("Дождь", "RAIN") + sheet("Облака и туман", "FOG") + sheet("Холод, снег, мороз", "COLD") + sheet("Ветер", "WIND") + sheet("Стихия", "STORM") + '''      <h2 class="lbl">Одна ситуация&nbsp;— разный смысл</h2>
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

rep('const LS_STATE = "syn:state";\nconst LS_SPEAK = "syn:autospeak";\nconst LS_TAB = "syn:tab";\nconst LS_OPEN = "syn:open";',
    'const LS_STATE = "wthr:state";\nconst LS_SPEAK = "wthr:autospeak";\nconst LS_TAB = "wthr:tab";\nconst LS_OPEN = "wthr:open";')
rep('["apple-mobile-web-app-title", "Синонимы"],', '["apple-mobile-web-app-title", "Погода"],')
rep("// ——— Группы слов и ситуации: прослушать", "// ——— Шпаргалка и ситуации: прослушать")
rep("// Новые карточки идут вперемешку по темам: пары, группы слов и глаголы чередуются — выбирать приходится по сочетанию.",
    "// Новые карточки идут вперемешку по темам: солнце, дождь, туман, ветер и стихия чередуются — выбирать приходится по сочетанию.")
rep("// […] — слово в фокусе (оранжевый)", "// […] — сочетание в фокусе (оранжевый)")
assert "syn:" not in s
pathlib.Path("wthr/template.html").write_text(s)
print("ok", len(s))
