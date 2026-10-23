#!/usr/bin/env node
/** Extract the English that the published trainers actually send to playClip.
 * No trainer script or DOM code is executed. New playback formats fail closed.
 * node tools/audio_clips.mjs [--root PATH] [--out PATH]
 */
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';

export const VOICE = 'en-GB-RyanNeural';
const DEFAULT_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
// Ignore code formatting, never spaces inside spoken-string literals.
const compact = source => {
  let result = '', quote = null;
  for (let i = 0; i < source.length; i++) {
    const ch = source[i];
    if (quote) {
      result += ch;
      if (ch === '\\') result += source[++i] || '';
      else if (ch === quote) quote = null;
    } else if (ch === '"' || ch === "'") { quote = ch; result += ch; }
    else if (!/\s/.test(ch)) result += ch;
  }
  return result;
};
const fail = message => { throw new Error(message); };

// A deliberately small JavaScript data-literal reader: comments, quoted strings,
// arrays, plain objects, booleans and numbers. Calls, spreads and expressions fail.
export function readDeclaration(source, name, required = true) {
  if (!/^[A-Z][A-Z_]*$/.test(name)) fail(`Invalid declaration name: ${name}`);
  const matches = [...source.matchAll(new RegExp(`\\bconst\\s+${name}\\s*=`, 'g'))];
  if (!matches.length && !required) return null;
  if (matches.length !== 1) fail(`Expected one const ${name}, found ${matches.length}`);
  let i = matches[0].index + matches[0][0].length;
  function skip() {
    for (;;) {
      while (/\s/.test(source[i] || '') && i < source.length) i++;
      if (source.startsWith('//', i)) { const end = source.indexOf('\n', i); i = end < 0 ? source.length : end; }
      else if (source.startsWith('/*', i)) { const end = source.indexOf('*/', i + 2); if (end < 0) fail(`Unclosed comment in ${name}`); i = end + 2; }
      else return;
    }
  }
  function string() {
    const start = i, quote = source[i++];
    while (i < source.length) {
      const ch = source[i++];
      if (ch === '\\') { i++; continue; }
      if (ch === quote) {
        const literal = source.slice(start, i);
        if (quote === '"') { try { return JSON.parse(literal); } catch { /* JavaScript-only escapes below. */ } }
        return vm.runInNewContext(literal, Object.create(null), { timeout: 100 });
      }
      if (ch === '\n' || ch === '\r') fail(`Unescaped newline in ${name}`);
    }
    fail(`Unclosed string in ${name}`);
  }
  function value(depth = 0) {
    if (depth > 40) fail(`Data nesting too deep in ${name}`);
    skip();
    if (source[i] === '"' || source[i] === "'") return string();
    if (source[i] === '[' || source[i] === '{') {
      const array = source[i++] === '[', end = array ? ']' : '}', result = array ? [] : Object.create(null);
      skip();
      while (source[i] !== end) {
        let key;
        if (!array) {
          if (source[i] === '"' || source[i] === "'") key = string();
          else { const m = source.slice(i).match(/^(?:[A-Za-z_$][\w$]*|\d+)/); if (!m) fail(`Invalid object key in ${name}`); key = m[0]; i += key.length; }
          skip(); if (source[i++] !== ':') fail(`Expected : in ${name}`);
          if (Object.hasOwn(result, key)) fail(`Duplicate object key ${key} in ${name}`);
        }
        const item = value(depth + 1);
        if (array) result.push(item); else result[key] = item;
        skip();
        if (source[i] === end) break;
        if (source[i++] !== ',') fail(`Only data literals are allowed in ${name}`);
        skip();
      }
      if (source[i++] !== end) fail(`Unclosed data in ${name}`);
      return result;
    }
    const token = source.slice(i).match(/^(?:true|false|null|-?(?:\d+(?:\.\d*)?|\.\d+)(?:e[+-]?\d+)?)(?![\w$])/i);
    if (!token) fail(`Unsupported expression in ${name} near ${source.slice(i, i + 50)}`);
    i += token[0].length;
    return JSON.parse(token[0]);
  }
  const result = value(); skip();
  if (source[i] !== ';') fail(`Only a literal declaration is allowed for ${name}`);
  return result;
}

function decodeEntities(text) {
  const named = { amp: '&', quot: '"', apos: "'", lt: '<', gt: '>', nbsp: '\u00a0' };
  return text.replace(/&(#x[0-9a-f]+|#\d+|[a-z][a-z0-9]+);/gi, (all, entity) => {
    if (entity[0] === '#') return String.fromCodePoint(entity[1].toLowerCase() === 'x' ? parseInt(entity.slice(2), 16) : Number(entity.slice(1)));
    if (!Object.hasOwn(named, entity)) fail(`Unsupported HTML entity ${all}`);
    return named[entity];
  });
}

function attributes(html) {
  return [...html.matchAll(/<[a-z][^>]*>/gi)].map(match => {
    const attrs = Object.create(null);
    for (const a of match[0].matchAll(/\b(data-(?:key|text|say))\s*=\s*(["'])(.*?)\2/g)) attrs[a[1]] = decodeEntities(a[3]);
    return attrs;
  });
}

function functionLine(source, name) {
  const match = source.match(new RegExp(`function ${name}\\([^\\n]+`));
  if (!match) fail(`Missing ${name} function`);
  return compact(match[0]);
}

const exampleTransforms = new Map([
  [String.raw`return en.replace(/[{}|_]/g, "");`, s => s.replace(/[{}|_]/g, '')],
  [String.raw`return en.replace(/[\[\]{}|]/g, "");`, s => s.replace(/[\[\]{}|]/g, '')],
  [String.raw`return en.replace(/[\[\]{}]/g, "");`, s => s.replace(/[\[\]{}]/g, '')],
  [String.raw`return en.replace(/[\[\]]/g, "");`, s => s.replace(/[\[\]]/g, '')],
  [String.raw`return en.replace(/\[0\]/g, "").replace(/\[([^\]]+)\]/g, "$1");`, s => s.replace(/\[0\]/g, '').replace(/\[([^\]]+)\]/g, '$1')],
  [String.raw`return en.replace(/\[([^\]]+)\]/g, "$1");`, s => s.replace(/\[([^\]]+)\]/g, '$1')],
  [String.raw`return en.replace(/\|\w\]/g, "]").replace(/[\[\]]/g, "");`, s => s.replace(/\|\w\]/g, ']').replace(/[\[\]]/g, '')],
  [String.raw`return en.replace(/\[([^\]|]+)(?:\|[abc])?\]/g, "$1");`, s => s.replace(/\[([^\]|]+)(?:\|[abc])?\]/g, '$1')],
  [String.raw`return en.replace(/\[([^\]|]+)(?:\|[soapr])?\]/g, "$1");`, s => s.replace(/\[([^\]|]+)(?:\|[soapr])?\]/g, '$1')],
  [String.raw`return en.replace(/\[([^\]|]+)(?:\|b)?\]/g, "$1");`, s => s.replace(/\[([^\]|]+)(?:\|b)?\]/g, '$1')],
].map(([body, fn]) => [compact(`function exText(en){ ${body} }`), fn]));

function grammarReader(html) {
  const full = functionLine(html, 'fullText');
  const fullWord = 'const p = split(card, card.a); return p.pre + p.word + p.post;';
  const fullArticle = 'const p = split(card, card.a); return p.pre + p.art + p.post;';
  const say = full === compact(`function fullText(card){ if (card.say) return card.say; ${fullWord} }`);
  if (!say && ![fullWord, fullArticle].some(body => full === compact(`function fullText(card){ ${body} }`))) fail('Unknown fullText format');
  const ex = exampleTransforms.get(functionLine(html, 'exText'));
  if (!ex) fail('Unknown exText markup format');
  const split = html.match(/function split\([^\n]+\{[\s\S]*?\n\}/)?.[0];
  const knownSplits = [
    ...['word', 'art'].map(word => `function split(card, ${word}){
      const i = card.q.indexOf("___"); const start = isStart(card.q, i);
      const pre = card.q.slice(0, i); let post = card.q.slice(i + 3);
      if (${word}) return { pre: pre, ${word}: start ? cap(${word}) : ${word}, post: post };
      post = post.replace(/^\\s+/, "");
      return { pre: pre, ${word}: "", post: start ? cap(post) : post };
    }`),
    `function split(card, word){
      const i = card.q.indexOf("___"); const start = isStart(card.q, i);
      const pre = card.q.slice(0, i); const post = card.q.slice(i + 3);
      return { pre: pre, word: start ? cap(word) : word, post: post };
    }`,
    `function split(card, word){
      const i = card.q.indexOf("___"); const start = isStart(card.q, i);
      return { pre: card.q.slice(0, i), word: start ? cap(word) : word, post: card.q.slice(i + 3) };
    }`,
  ].map(compact);
  if (!split || !knownSplits.includes(compact(split.replace(/\/\/[^\n]*/g, '')))) fail('Unknown split format');
  const start = 'function isStart(q, i){ const b = q.slice(0, i).trimEnd(); return b === "" || /[.!?]$/.test(b); }';
  const cap = 'function cap(s){ return s ? s.charAt(0).toUpperCase() + s.slice(1) : s; }';
  if (functionLine(html, 'isStart') !== compact(start) || functionLine(html, 'cap') !== compact(cap)) fail('Unknown capitalization format');
  const trimEmpty = split.includes('post.replace(/^\\s+/, "")');
  const capitalize = s => s ? s.charAt(0).toUpperCase() + s.slice(1) : s;
  return {
    example: ex,
    card(c) {
      if (say && c.say) return c.say;
      if (typeof c.q !== 'string' || typeof c.a !== 'string' || c.q.split('___').length !== 2) fail(`Unknown grammar card ${c.id}: expected one blank and a string answer`);
      const i = c.q.indexOf('___'), pre = c.q.slice(0, i), isStart = pre.trimEnd() === '' || /[.!?]$/.test(pre.trimEnd());
      let post = c.q.slice(i + 3), word = c.a;
      if (!word && trimEmpty) { post = post.replace(/^\s+/, ''); if (isStart) post = capitalize(post); }
      else if (isStart) word = capitalize(word);
      return pre + word + post;
    },
  };
}

// Every currently supported call shape is enumerated. A new path cannot silently
// publish speech without a corresponding extraction implementation.
const CALLS = [
  'key, text, rate', 'c.id, fullText(c)', 'card.id, fullText(card)',
  '"r" + t.n + "-" + (i + 1), exText(ex.en), 0.9',
  '"r" + t.n + "-" + (i + 1), pr.good.replace(/\\|/g, ""), 0.9',
  '"fw-" + (i + 1), f.en, 0.85', 'b.dataset.key, b.dataset.text, 0.85',
  'key, exText(ex.en), 0.9', '"v-" + v.v, v.say, 0.85', '"fam-" + n, text, 0.85',
  '"forms", FORMS.map(f => "It " + f[2] + " " + f[3] + ".").join(" "), 0.85',
  'c.id, c.a', 'card.id, card.a', '"w-" + b.dataset.say, b.dataset.say, 0.85', '"anchor", ANCHOR, 0.88',
  'c.id + "-a", c.sa, 0.8', 'c.id + "-e", c.se, 0.85', 'c.id + "-l", c.sl, 0.85', 'card.id + "-l", card.sl, 0.85',
  'clipKey(c, part), isEx ? c.ex : c.term, isEx ? 0.85 : 0.9',
];
const knownCalls = new Set(CALLS.map(compact));
function playbackCalls(html) {
  const calls = [];
  for (const match of html.matchAll(/\bplayClip\s*\(/g)) {
    const start = match.index + match[0].length;
    let depth = 1, quote = null, i = start;
    for (; i < html.length; i++) {
      const ch = html[i];
      if (quote) { if (ch === '\\') i++; else if (ch === quote) quote = null; continue; }
      if (ch === '"' || ch === "'") { quote = ch; continue; }
      if (ch === '(') depth++; else if (ch === ')' && --depth === 0) break;
    }
    if (depth) fail('Unclosed playClip call');
    const call = compact(html.slice(start, i));
    if (!knownCalls.has(call)) fail(`Unknown playClip format: ${html.slice(start, i)}`);
    calls.push(call);
  }
  if (calls.length < 2) fail('No supported playback controls');
  return new Set(calls);
}

export function extractAppClips(app, html) {
  if (app.key === 'bbapp') return null; // Keep the user's Breaking Bad exception.
  if (!/^[a-z][a-z0-9-]*$/.test(app.key || '')) fail(`Invalid app key ${app.key}`);
  try {
    const calls = playbackCalls(html), cards = readDeclaration(html, 'CARDS'), topics = readDeclaration(html, 'TOPICS', false) || [];
    if (!Array.isArray(cards) || !cards.length || !Array.isArray(topics)) fail('Expected nonempty CARDS and optional TOPICS arrays');
    const clips = new Map(), ids = new Set();
    const add = (key, text) => {
      if (typeof key !== 'string' || !/^[a-zA-Z0-9][a-zA-Z0-9_.-]*$/.test(key)) fail(`Invalid audio key ${key}`);
      if (typeof text !== 'string' || !/[A-Za-z]/.test(text) || /[А-Яа-яЁё]|___|undefined|\[object Object\]/.test(text)) fail(`Missing or invalid English for ${key}`);
      const clip = { key, text, rate: '-5%' };
      if (clips.has(key) && clips.get(key).text !== text) fail(`Conflicting text for ${key}`);
      clips.set(key, clip);
    };
    const phrasal = calls.has(compact(CALLS.at(-1)));
    if (phrasal && functionLine(html, 'clipKey') !== compact('function clipKey(c, part){ return c.au ? c.id + "-" + part : null; }')) {
      fail('Unknown phrasal clipKey format');
    }
    const letters = calls.has(compact('c.id + "-a", c.sa, 0.8'));
    const answers = calls.has(compact('c.id, c.a'));
    const grammar = !phrasal && !letters && !answers ? grammarReader(html) : null;
    for (const card of cards) {
      if (typeof card.id !== 'string' || !/^[a-zA-Z0-9][a-zA-Z0-9_.-]*$/.test(card.id)) fail(`Invalid card id ${card.id}`);
      if (ids.has(card.id)) fail(`Duplicate card id ${card.id}`); ids.add(card.id);
      if (phrasal) { add(`${card.id}-t`, card.term); add(`${card.id}-x`, card.ex); }
      else if (letters) for (const [suffix, field] of [['a', 'sa'], ['e', 'se'], ['l', 'sl']]) add(`${card.id}-${suffix}`, card[field]);
      else add(card.id, answers ? card.a : grammar.card(card));
    }
    for (const topic of topics) {
      if (topic.ex?.length && !grammar) fail(`Unhandled topic examples in ${topic.n}`);
      for (const [i, ex] of (topic.ex || []).entries()) add(`r${topic.n}-${i + 1}`, grammar.example(ex.en));
      for (const [i, pair] of (topic.pairs || []).entries()) add(`r${topic.n}-${i + 1}`, pair.good.replace(/\|/g, ''));
      for (const [i, word] of (topic.ff || []).entries()) add(`fw-${i + 1}`, word.en);
    }
    for (const attrs of attributes(html)) {
      if (Object.hasOwn(attrs, 'data-key')) {
        if (!Object.hasOwn(attrs, 'data-text')) fail(`Missing data-text for ${attrs['data-key']}`);
        add(attrs['data-key'], attrs['data-text']);
      }
      if (Object.hasOwn(attrs, 'data-say')) add(`w-${attrs['data-say']}`, attrs['data-say']);
    }
    if (calls.has(compact('"anchor", ANCHOR, 0.88'))) add('anchor', readDeclaration(html, 'ANCHOR'));
    if (calls.has(compact('"forms", FORMS.map(f => "It " + f[2] + " " + f[3] + ".").join(" "), 0.85'))) {
      add('forms', readDeclaration(html, 'FORMS').map(f => `It ${f[2]} ${f[3]}.`).join(' '));
    }
    if (calls.has(compact('"v-" + v.v, v.say, 0.85'))) {
      const verbs = readDeclaration(html, 'VERBS');
      for (const verb of verbs) add(`v-${verb.v}`, verb.say);
      for (const topic of topics.filter(t => t.kind === 'fam')) add(`fam-${topic.n}`, verbs.filter(v => v.t === topic.n).map(v => v.say).join(' '));
    }
    if (calls.has(compact('key, exText(ex.en), 0.9'))) {
      if (!html.includes('"g-" + t.id + "-" + (i + 1)')) fail('Unknown tense-grid keys');
      for (const tense of readDeclaration(html, 'TENSES')) for (const [i, ex] of tense.ex.entries()) add(`g-${tense.id}-${i + 1}`, grammar.example(ex.en));
    }
    return { key: app.key, title: app.title, voice: VOICE,
      ...(phrasal ? { kind: 'phrasal', audio_flags: cards.map(c => ({ id: c.id, au: c.au ?? 0 })) } : {}),
      clips: [...clips.values()].sort((a, b) => a.key.localeCompare(b.key, 'en')) };
  } catch (error) { throw new Error(`${app.key}: ${error.message}`, { cause: error }); }
}

export function extractCatalogClips(repoRoot = DEFAULT_ROOT) {
  const catalog = JSON.parse(fs.readFileSync(path.join(repoRoot, 'tools/catalog.json'), 'utf8'));
  if (!Array.isArray(catalog.apps) || !catalog.apps.length) fail('Empty or invalid catalog');
  const result = Object.create(null);
  for (const app of catalog.apps) {
    if (app.key === 'bbapp') continue;
    if (Object.hasOwn(result, app.key)) fail(`Duplicate app ${app.key}`);
    if (!/^[a-z][a-z0-9-]*$/.test(app.key || '')) fail(`Invalid app key ${app.key}`);
    result[app.key] = extractAppClips(app, fs.readFileSync(path.join(repoRoot, 'site/apps', `${app.key}.html`), 'utf8'));
  }
  return result;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    let root = DEFAULT_ROOT, out;
    for (let i = 2; i < process.argv.length; i++) {
      if (process.argv[i] === '--root' && process.argv[i + 1]) root = path.resolve(process.argv[++i]);
      else if (process.argv[i] === '--out' && process.argv[i + 1]) out = path.resolve(process.argv[++i]);
      else fail(`Usage: node tools/audio_clips.mjs [--root PATH] [--out PATH]`);
    }
    const json = JSON.stringify(extractCatalogClips(root), null, 2) + '\n';
    if (out) fs.writeFileSync(out, json); else process.stdout.write(json);
  } catch (error) { console.error(error.message); process.exitCode = 1; }
}
