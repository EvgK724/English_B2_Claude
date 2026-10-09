# Шаблон «Three, tree, sheep» собираю из шаблона «Have to, must и похожие» (oblig). Что добавлено:
#   — карточки на слух (поле ear): перевод скрыт до ответа, запись звучит сама, кнопка «Послушать ещё раз»;
#   — поле say: что произносить вместо предложения с ответом (нужно для ударений REcord и reCORD в «Advice и advise»);
#   — разметка примеров [слово|a] — оранжевый, |b — синий, |c — зелёный, без метки — подчёркнуто.
# Вкладка правил — своя: таблица «звук — как произнести — пары», как услышать разницу, мнемоника.
# Запуск из sources/: python3 sounds/mk_template.py   (нужен oblig/template.html — python3 oblig/mk_template.py)
import pathlib
s = pathlib.Path("oblig/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Have to, must и похожие</title>", "<title>Three, tree, sheep</title>")

# ——— стили: кнопка «Послушать ещё раз» на карточке
rep("  .algo-2{margin-top:12px}\n", """  .algo-2{margin-top:12px}
  .ear{align-self:flex-start;display:inline-flex;align-items:center;gap:10px;min-height:52px;padding:0 18px;border-radius:14px;border:1px solid var(--accent);background:transparent;color:var(--accent);font-size:18px;cursor:pointer}
  .ear svg{width:24px;height:24px;flex:0 0 24px}
  .ear:active{background:var(--raise)}
""")
rep('      <p class="hint" id="hint">Выбери вариант</p>\n', '''      <p class="hint" id="hint">Выбери вариант</p>
      <button class="ear" id="ear" type="button" hidden><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/><path d="M18.2 6.4a7.6 7.6 0 0 1 0 11.2"/></svg><span>Послушать ещё раз</span></button>
''')

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    return f'<span class="{c}">{t.replace(" ", "&nbsp;") if len(t) <= 16 else t}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Сначала гласная: долгая или короткая?", W("sheep", "pr") + D + W("ship", "st") + D + W("leave", "pr") + D + W("live", "st"))
         + step(2, "Рот открыт широко или как для «э»?", W("bad", "pr") + D + W("bed", "st") + D + W("man", "pr") + D + W("men", "st"))
         + step(3, "Язык между зубами?", W("three", "pr") + D + W("tree", "st") + D + W("think", "pr") + D + W("sink", "st"))
         + step(4, "Губы трубочкой или зубы на губе? Есть лёгкий выдох?", W("wet", "pr") + D + W("vet", "st") + D + W("hill", "pr") + D + W("ill", "st"))
         + step(5, "Конец звонкий — гласная перед ним длиннее?", W("bag", "pr") + D + W("back", "st") + D + W("eyes", "pr") + D + W("ice", "st")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Three, tree, sheep</h1>
      <p class="r-sub">Слова, которые различаются одним звуком. Русскому уху эти звуки кажутся одинаковыми, а&nbsp;англичанин слышит другое слово: <b lang="en">three</b>&nbsp;— три, <b lang="en">tree</b>&nbsp;— дерево. Здесь два вида карточек: по&nbsp;смыслу и&nbsp;на&nbsp;слух. Слушайте, повторяйте вслух.</p>
      <div class="algo">
        <p class="algo-h">Главная таблица</p>
        <table class="mt vt">
          <colgroup><col><col></colgroup>
          <thead><tr><th scope="col">Как произнести</th><th scope="col">Пары</th></tr></thead>
<!--__TABLE__-->
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как услышать разницу</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m"><b class="pr" lang="en">Three trees</b>&nbsp;— сначала язык между зубами, потом за&nbsp;зубами. <b class="st" lang="en">Sheep on a&nbsp;ship</b>&nbsp;— сначала долго с&nbsp;улыбкой, потом коротко.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "oblig:state";\nconst LS_SPEAK = "oblig:autospeak";\nconst LS_TAB = "oblig:tab";\nconst LS_OPEN = "oblig:open";',
    'const LS_STATE = "sounds:state";\nconst LS_SPEAK = "sounds:autospeak";\nconst LS_TAB = "sounds:tab";\nconst LS_OPEN = "sounds:open";')
rep('["apple-mobile-web-app-title", "have to"],', '["apple-mobile-web-app-title", "sounds"],')

# ——— что произносить: поле say вместо предложения с ответом
rep('function fullText(card){ const p = split(card, card.a); return p.pre + p.word + p.post; }',
    'function fullText(card){ if (card.say) return card.say; const p = split(card, card.a); return p.pre + p.word + p.post; }')
# ——— разметка [слово|a]
rep('function exText(en){ return en.replace(/[\\[\\]]/g, ""); }', 'function exText(en){ return en.replace(/\\[([^\\]|]+)(?:\\|[abc])?\\]/g, "$1"); }')
i = s.index("// […] — ключевой глагол"); j = s.index("function marked(s){"); k = s.index("\n}\n", j) + 3
s = s[:i] + '''// […] — разметка примеров: [слово|a] — оранжевый, [слово|b] — синий, [слово|c] — зелёный, [слово] — подчёркнуто
function markCls(k){ return k === "a" ? "pr" : k === "b" ? "st" : k === "c" ? "good" : "hl"; }
function marked(s){
  const f = document.createDocumentFragment();
  const re = /\\[([^\\]|]+)(?:\\|([abc]))?\\]/g;
  let last = 0, m;
  while ((m = re.exec(s))){
    if (m.index > last) f.append(richText(s.slice(last, m.index)));
    f.append(el("span", markCls(m[2]), m[1]));
    last = re.lastIndex;
  }
  if (last < s.length) f.append(richText(s.slice(last)));
  return f;
}
''' + s[k:]

# ——— карточки на слух
rep('''  $("hint").textContent = card.ru ? card.ru : "Выбери вариант";''', '''  $("hint").textContent = card.ear ? "Послушайте: какое слово прозвучало?" : card.ru ? card.ru : "Выбери вариант";
  if (card.ear) $("kind").textContent += " · на слух";
  show("ear", !!card.ear);''')
rep('''  preloadClip(card.id);
}''', '''  preloadClip(card.id);
  // на слух: запись звучит сама — сразу после касания «Дальше» или «Начать», когда звук уже разрешён
  if (card.ear && autoSpeak) setTimeout(() => { if (queue[index] === card && !answered) playClip(card.id, fullText(card)); }, 200);
}''')
rep('''function renderDone(){
  show("kind", false);''', '''function renderDone(){
  show("kind", false);
  show("ear", false);''')
rep('''  show("hint", false);
  show("back", true);''', '''  show("hint", false);
  show("ear", false);
  show("back", true);''')
rep('''$("say").addEventListener("click", () => {''', '''$("ear").addEventListener("click", () => {
  const c = queue[index];
  if (c) playClip(c.id, fullText(c));
});
$("say").addEventListener("click", () => {''')
assert "oblig:" not in s and "must" not in s[s.index("function markCls"):s.index("function markCls") + 900]
pathlib.Path("sounds/template.html").write_text(s)
print("ok", len(s))
