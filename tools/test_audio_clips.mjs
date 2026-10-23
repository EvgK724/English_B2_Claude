import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { extractAppClips, extractCatalogClips, readDeclaration, VOICE } from './audio_clips.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const html = key => fs.readFileSync(path.join(root, 'site/apps', `${key}.html`), 'utf8');
const extract = (key, source = html(key)) => extractAppClips({ key, title: key }, source);
const clip = (app, key) => app.clips.find(c => c.key === key)?.text;
const phrasalFixture = cards => `const CARDS = ${cards};
function playClip(key, text, rate){}
function clipKey(c, part){ return c.au ? c.id + "-" + part : null; }
playClip(clipKey(c, part), isEx ? c.ex : c.term, isEx ? 0.85 : 0.9);`;

test('literal reader accepts comments, escaped punctuation and trailing commas without executing expressions', () => {
  const source = String.raw`const CARDS = [// comments are data boundaries
    {id:'new', text:"Don't lose the patient’s notes; [keep] them.", n:-5, ok:true, value:null,},
  ];`;
  const cards = readDeclaration(source, 'CARDS');
  assert.equal(cards[0].text, "Don't lose the patient’s notes; [keep] them.");
  assert.equal(cards[0].n, -5);
  assert.equal(cards[0].ok, true);
  assert.throws(() => readDeclaration('const CARDS = (() => [])();', 'CARDS'), /Unsupported expression/);
  assert.throws(() => readDeclaration('const CARDS = [{text: globalThis.secret}];', 'CARDS'), /Unsupported expression/);
  assert.throws(() => readDeclaration('const CARDS = [{id:"a",id:"b"}];', 'CARDS'), /Duplicate object key/);
  assert.throws(() => readDeclaration('const CARDS = [] + [];', 'CARDS'), /Only a literal/);
});

test('every active app can be extracted independently of existing audio; Breaking Bad is excluded', () => {
  const catalog = JSON.parse(fs.readFileSync(path.join(root, 'tools/catalog.json')));
  const manifest = extractCatalogClips(root);
  assert.deepEqual(Object.keys(manifest), catalog.apps.filter(a => a.key !== 'bbapp').map(a => a.key));
  assert.equal(extractAppClips({ key: 'bbapp' }, 'not even valid HTML'), null);
  for (const [key, app] of Object.entries(manifest)) {
    assert.equal(app.voice, VOICE);
    assert.ok(app.clips.length > 0, key);
    assert.equal(new Set(app.clips.map(c => c.key)).size, app.clips.length, key);
    assert.ok(app.clips.every(c => c.rate === '-5%' && /[A-Za-z]/.test(c.text)), key);
    // Intentionally do not inspect packs.json: new words are extracted before
    // generation. The pipeline's --check owns post-generation audio coverage.
  }
});

test('new phrasal cards need both recordings even without au, preserving supplied English exactly', () => {
  const source = phrasalFixture(`[{id:"new-item",term:"carry on",ex:"Don’t stop — carry on, please!",added:"2026-10-23"}]`);
  const app = extract('new-deck', source);
  assert.equal(app.kind, 'phrasal');
  assert.deepEqual(app.audio_flags, [{ id: 'new-item', au: 0 }]);
  assert.equal(clip(app, 'new-item-t'), 'carry on');
  assert.equal(clip(app, 'new-item-x'), 'Don’t stop — carry on, please!');
  assert.equal(app.clips.length, 2);
  assert.equal(source, phrasalFixture(`[{id:"new-item",term:"carry on",ex:"Don’t stop — carry on, please!",added:"2026-10-23"}]`));
});

test('grammar says the completed sentence, respects say overrides and removes only display markup', () => {
  for (const key of ['whatfor', 'sounds', 'nverb', 'artikli', 'countable', 'top10']) {
    const source = html(key), app = extract(key, source), cards = readDeclaration(source, 'CARDS');
    for (const c of cards.filter(c => c.say)) assert.equal(clip(app, c.id), c.say, `${key}:${c.id}`);
    const normal = cards.find(c => !c.say && c.a && c.q.startsWith('___'));
    if (normal) assert.equal(clip(app, normal.id), normal.a[0].toUpperCase() + normal.a.slice(1) + normal.q.slice(3), key);
  }
  const articles = extract('artikli'), articleCards = readDeclaration(html('artikli'), 'CARDS');
  for (const c of articleCards.filter(c => c.a === '')) {
    const i = c.q.indexOf('___'), before = c.q.slice(0, i), after = c.q.slice(i + 3).replace(/^\s+/, '');
    const expected = before + (!before.trimEnd() || /[.!?]$/.test(before.trimEnd()) ? after[0].toUpperCase() + after.slice(1) : after);
    assert.equal(clip(articles, c.id), expected);
  }
  const topic = readDeclaration(html('whatfor'), 'TOPICS').find(t => t.ex?.length);
  assert.equal(clip(extract('whatfor'), `r${topic.n}-1`), topic.ex[0].en.replace(/\[([^\]|]+)(?:\|[abc])?\]/g, '$1'));
});

test('special speech families preserve all text: tense grid, verbs, families, forms, anchor, idioms', () => {
  const tenses = extract('tenses'), tense = readDeclaration(html('tenses'), 'TENSES')[0];
  assert.equal(clip(tenses, `g-${tense.id}-1`), tense.ex[0].en.replace(/[\[\]{}|]/g, ''));
  const irregular = extract('irreg'), verbs = readDeclaration(html('irreg'), 'VERBS');
  assert.equal(clip(irregular, `v-${verbs[0].v}`), verbs[0].say);
  assert.equal(clip(irregular, `fam-${verbs[0].t}`), verbs.filter(v => v.t === verbs[0].t).map(v => v.say).join(' '));
  const forms = readDeclaration(html('passive'), 'FORMS');
  assert.equal(clip(extract('passive'), 'forms'), forms.map(f => `It ${f[2]} ${f[3]}.`).join(' '));
  assert.equal(clip(extract('bez-a-an'), 'anchor'), readDeclaration(html('bez-a-an'), 'ANCHOR'));
  assert.equal(clip(extract('bez-a-an'), 'w-equipment'), 'equipment');
  for (const key of ['abbr', 'idm']) {
    const app = extract(key), card = readDeclaration(html(key), 'CARDS')[0];
    for (const [suffix, field] of [['a','sa'],['e','se'],['l','sl']]) assert.equal(clip(app, `${card.id}-${suffix}`), card[field]);
  }
  const top = extract('top10'), topics = readDeclaration(html('top10'), 'TOPICS');
  const pair = topics.find(t => t.pairs?.length), ff = topics.find(t => t.ff?.length);
  assert.equal(clip(top, `r${pair.n}-1`), pair.pairs[0].good.replace(/\|/g, ''));
  assert.equal(clip(top, 'fw-1'), ff.ff[0].en);
});

test('HTML contrast text is decoded without rewriting punctuation or adding speech', () => {
  const source = phrasalFixture('[{id:"a",term:"carry on",ex:"Carry on."}]') +
    '<button data-text="Don&#39;t say &quot;no&quot; &amp; leave; it’s OK.&nbsp;Go!" data-key="extra"></button>';
  assert.equal(clip(extract('test-deck', source), 'extra'), 'Don\'t say "no" & leave; it’s OK.\u00a0Go!');
  assert.throws(() => extract('test-deck', source.replace('data-text=', 'data-other=')), /Missing data-text/);
});

test('unknown playback and text transforms fail closed instead of silently losing coverage', () => {
  const source = html('whatfor');
  assert.throws(() => extract('whatfor', source + '\nplayClip("brand-new", item.sentence);'), /Unknown playClip/);
  assert.throws(() => extract('whatfor', source.replace('if (card.say) return card.say;', 'if (card.say) return card.say.toLowerCase();')), /Unknown fullText/);
  assert.throws(() => extract('whatfor', source.replace('card.q.slice(i + 3)', 'card.q.slice(i + 4)')), /Unknown split/);
  assert.throws(() => extract('whatfor', source.replace('post.replace(/^\\s+/, "")', 'post.replace(/^\\s+/, " ")')), /Unknown split/);
  assert.throws(() => extract('new-deck', phrasalFixture('[{id:"a",term:"",ex:"Good."}]')), /Missing or invalid English/);
  assert.throws(() => extract('new-deck', phrasalFixture('[{term:"Good",ex:"Good."}]')), /Invalid card id/);
  assert.throws(() => extract('new-deck', phrasalFixture('[{id:"a",term:"Good",ex:""}]')), /Missing or invalid English/);
  assert.throws(() => extract('new-deck', phrasalFixture('[{id:"a",term:"Good",ex:"Good."},{id:"a",term:"Bad",ex:"Bad."}]')), /Duplicate card/);
  const phrasal = html('phrasal');
  assert.throws(() => extract('phrasal', phrasal.replace('c.au ? c.id + "-" + part : null', 'c.au ? "new-" + c.id + "-" + part : null')), /Unknown phrasal clipKey/);
  assert.throws(() => extract('phrasal', phrasal.replace('c.au ? c.id + "-" + part : null', 'c.au ? c.id + "-" + part + "-new" : null')), /Unknown phrasal clipKey/);
  assert.throws(() => extract('phrasal', phrasal.replace('c.au ? c.id + "-" + part : null', 'c.au ? c.id + "-" + (part === "x" ? "t" : "x") : null')), /Unknown phrasal clipKey/);
});
