# Шаблон «two, too или to» собираю из шаблона «adj / adv»: тренажёр тот же, плюс вариант «ничего» (go home).
import pathlib
s = pathlib.Path("adjadv/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Прилагательные и наречия</title>", "<title>Two, too или to</title>")

# ——— стили: три карточки слов
rep("  .legend{margin:0 2px 10px;font-size:15px;line-height:1.45;color:var(--soft)}",
    '''  .legend{margin:0 2px 10px;font-size:15px;line-height:1.45;color:var(--soft)}
  .wb{display:grid;grid-template-columns:minmax(0,1fr) 48px;column-gap:10px;align-items:start}
  .wb-h{margin:0;display:flex;align-items:baseline;flex-wrap:wrap;gap:4px 12px}
  .wb-w{font-family:var(--serif);font-size:38px;line-height:1.05}
  .wb-s{font-size:15px;color:var(--soft)}
  .wb-ex{margin:6px 0 0;font-family:var(--serif);font-size:19px;line-height:1.4}
  .wb .ex-play{grid-column:2;grid-row:1 / span 2;align-self:center}
  .zero{font-family:var(--sans);font-size:.55em;line-height:1;color:var(--yes-text);border:1px solid rgba(78,135,103,.65);border-radius:999px;padding:.12em .45em;margin:0 .35em 0 .05em;vertical-align:.25em}
  .opt small{font-family:var(--sans);font-size:13px;color:var(--muted)}''')

# ——— разметка вкладки «Правила»
a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Two, too or to?</h1>
      <p class="r-sub">Звучат почти одинаково, а&nbsp;пишутся и&nbsp;значат по-разному. На&nbsp;письме их путают даже носители. Решает смысл: <b>число</b>, <b>«слишком» или «тоже»</b>&nbsp;— или всё остальное.</p>
      <div class="algo">
        <p class="algo-h">Проверка за секунду</p>
        <ol class="steps">
          <li><span class="sn">1</span><div><p class="s-t">Число 2?</p><p class="s-f" lang="en"><span class="st">two</span> <i>patients</i></p></div></li>
          <li><span class="sn">2</span><div><p class="s-t">«Слишком» или «тоже»?</p><p class="s-f" lang="en"><span class="pr">too</span> <i>late · Me</i> <span class="pr">too</span></p></div></li>
          <li><span class="sn">3</span><div><p class="s-t">Куда, кому, до или + глагол?</p><p class="s-f" lang="en"><span class="good">to</span> <i>the ward · want</i> <span class="good">to</span> <i>go</i></p></div></li>
        </ol>
        <p class="algo-m"><b class="st" lang="en">two</b> · <b class="pr" lang="en">too</b> · <b class="good" lang="en">to</b></p>
        <p class="algo-note">two и too&nbsp;— всегда [tuː]. to в&nbsp;речи обычно звучит кратко: [tə]&nbsp;— <i lang="en">I want to go</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Три слова</h2>
<!--__WORDS__-->
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

# ——— скрипт
rep('const LS_STATE = "adjadv:state";\nconst LS_SPEAK = "adjadv:autospeak";\nconst LS_TAB = "adjadv:tab";\nconst LS_OPEN = "adjadv:open";',
    'const LS_STATE = "twotoo:state";\nconst LS_SPEAK = "twotoo:autospeak";\nconst LS_TAB = "twotoo:tab";\nconst LS_OPEN = "twotoo:open";')
rep('["apple-mobile-web-app-title", "adj / adv"],', '["apple-mobile-web-app-title", "two/too/to"],')
rep("// {…} — прилагательное (синий), _…_ — наречие (оранжевый), |…| — зелёный", "// {…} — two (синий), _…_ — too (оранжевый), |…| — to (зелёный)")
rep("// ——— Памятка: прослушать пару (hard — hardly…)", "// ——— Три слова: прослушать примеры")
rep("// Новые карточки идут вперемешку по темам: каждый раз решаешь заново — какой? или как?",
    "// Новые карточки идут вперемешку по темам: каждый раз решаешь заново — two, too или to.")

# вариант «ничего» (go home — без to)
rep('function topicLabel(n){ return n === MIXED_TOPIC ? "Всё вместе" : "Тема " + n + " · " + TOPIC_BY[n].title; }',
    'function topicLabel(n){ return n === MIXED_TOPIC ? "Всё вместе" : "Тема " + n + " · " + TOPIC_BY[n].title; }\nfunction label(a){ return a === "" ? "ничего" : a; }')
rep('''function split(card, word){
  const i = card.q.indexOf("___");
  const start = isStart(card.q, i);
  return { pre: card.q.slice(0, i), word: start ? cap(word) : word, post: card.q.slice(i + 3) };
}''', '''function split(card, word){
  const i = card.q.indexOf("___");
  const start = isStart(card.q, i);
  const pre = card.q.slice(0, i);
  let post = card.q.slice(i + 3);
  if (word) return { pre: pre, word: start ? cap(word) : word, post: post };
  post = post.replace(/^\\s+/, "");                  // ответ «ничего»: слово после пропуска встаёт на его место
  return { pre: pre, word: "", post: start ? cap(post) : post };
}''')
rep('''    const b = el("button", "opt" + (longest > 9 ? " long" : ""));
    b.type = "button";
    b.lang = "en";
    b.textContent = o;''', '''    const b = el("button", "opt" + (longest > 9 ? " long" : ""));
    b.type = "button";
    if (o === ""){
      b.setAttribute("aria-label", "Ничего не нужно");
      b.append(el("span", null, "—"), el("small", null, "ничего"));
    } else {
      b.lang = "en";
      b.textContent = o;
    }''')
rep('''  const p = split(card, card.a);
  q.append(p.pre, el("span", "good", p.word), p.post);''', '''  const p = split(card, card.a);
  if (p.word) q.append(p.pre, el("span", "good", p.word), p.post);
  else q.append(p.pre, el("span", "zero", "∅"), p.post);''')
rep('''    v.append("Нужно ", el("b", "good", card.a), " · твой ответ: ", el("b", null, opt));''',
    '''    v.append("Нужно ", el("b", "good", label(card.a)), " · твой ответ: ", el("b", null, label(opt)));''')
pathlib.Path("twotoo/template.html").write_text(s)
print("ok", len(s))
