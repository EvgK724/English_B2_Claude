// Иконки приложения для экрана «Домой»: та же плитка, что tools/reference/render_icon.py
// (веер карточек, Aa, english), но каждая — сразу в своём размере, плюс maskable с полями для Android.
//   npm i playwright @fontsource/dm-serif-display     (в любой папке; Chromium — из Playwright)
//   node tools/render_icons.mjs [путь к node_modules]
import { createRequire } from 'node:module';
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const NM = process.argv[2] || join(process.cwd(), 'node_modules');
const require = createRequire(join(NM, 'x.js'));
const { chromium } = require('playwright');
const font = readFileSync(join(NM, '@fontsource/dm-serif-display/files/dm-serif-display-latin-400-normal.woff2')).toString('base64');

const OUT = [
  ['site/apple-touch-icon.png', 180, 1],
  ['site/icon-192.png', 192, 1],
  ['site/icon-512.png', 512, 1],
  ['site/icon-maskable-512.png', 512, 0.78],
  ['site/favicon.png', 32, 1],
  ['tools/icon-1024.png', 1024, 1],
];

const draw = async ([b64, size, scale]) => {
  if (!window.__dmsd) {
    const buf = Uint8Array.from(atob(b64), (ch) => ch.charCodeAt(0)).buffer;
    const face = new FontFace('DMSD', buf); await face.load(); document.fonts.add(face);
    window.__dmsd = true;
  }
  const S = 1024, c = document.createElement('canvas'); c.width = c.height = size;
  const x = c.getContext('2d');
  x.fillStyle = '#0e1113'; x.fillRect(0, 0, size, size);
  x.scale(size / S, size / S);
  x.translate(S / 2, S / 2); x.scale(scale, scale); x.translate(-S / 2, -S / 2);
  const W = 540, H = 660, R = 64, rad = (d) => d * Math.PI / 180;
  const card = (cx, cy, rot, fill, stroke, shadow) => {
    x.save(); x.translate(cx, cy); x.rotate(rad(rot));
    x.shadowColor = 'rgba(0,0,0,.5)'; x.shadowBlur = shadow * size / S; x.shadowOffsetY = shadow * 0.4 * size / S;
    x.beginPath(); x.roundRect(-W / 2, -H / 2, W, H, R); x.fillStyle = fill; x.fill();
    x.shadowColor = 'transparent'; x.shadowBlur = 0; x.shadowOffsetY = 0;
    x.lineWidth = 4; x.strokeStyle = stroke; x.stroke();
    return () => x.restore();
  };
  card(430, 540, -11, '#13181b', '#232a2e', 36)();
  card(600, 530, 9, '#161c1f', '#283034', 40)();
  const done = card(512, 520, -1.5, '#1b2125', '#313a3f', 48);
  x.textBaseline = 'alphabetic'; x.textAlign = 'left';
  x.fillStyle = '#7cc0dd'; x.font = '64px DMSD'; x.fillText('english', -W / 2 + 48, -H / 2 + 104);
  let fs = 360; x.font = fs + 'px DMSD';
  while (x.measureText('Aa').width > W - 120) { fs -= 6; x.font = fs + 'px DMSD'; }
  const mA = x.measureText('A'), mAa = x.measureText('Aa');
  const left = -mAa.width / 2, base = 150;
  x.fillStyle = '#ececea'; x.fillText('A', left, base);
  x.fillStyle = '#d97757'; x.fillText('a', left + mA.width, base);
  const bw = W - 96, by = H / 2 - 78;
  x.fillStyle = '#2a3236'; x.beginPath(); x.roundRect(-bw / 2, by, bw, 12, 6); x.fill();
  x.fillStyle = '#d97757'; x.beginPath(); x.roundRect(-bw / 2, by, bw * 0.62, 12, 6); x.fill();
  done();
  return c.toDataURL('image/png');
};

const b = await chromium.launch(process.env.CHROMIUM ? { executablePath: process.env.CHROMIUM } : {});
const pg = await b.newPage(); await pg.goto('about:blank');
for (const [file, size, scale] of OUT) {
  const data = await pg.evaluate(draw, [font, size, scale]);
  writeFileSync(join(ROOT, file), Buffer.from(data.split(',')[1], 'base64'));
  console.log(file, size);
}
await b.close();
