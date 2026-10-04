// Иконки приложения для экрана «Домой» в духе want-you-to (test01): Eng / lish / B2 янтарным, бирюзовым и сиреневым
// со свечением и три цветные черты. Шрифт — Bricolage Grotesque из site/fonts. Каждая иконка рисуется сразу
// в своём размере, плюс maskable с полями для круглой маски Android. Прежняя плитка — tools/reference/render_icon.py.
//   npm i playwright        (в любой папке; Chromium — из Playwright или CHROMIUM=<путь к chrome>)
//   node tools/render_icons.mjs [путь к node_modules]
import { createRequire } from 'node:module';
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const NM = process.argv[2] || join(process.cwd(), 'node_modules');
const require = createRequire(join(NM, 'x.js'));
const { chromium } = require('playwright');
const font = readFileSync(join(ROOT, 'site/fonts/bricolage-grotesque-latin-wght-normal.woff2')).toString('base64');

const OUT = [
  ['site/apple-touch-icon.png', 180, 1],
  ['site/icon-192.png', 192, 1],
  ['site/icon-512.png', 512, 1],
  ['site/icon-maskable-512.png', 512, 0.78],
  ['site/favicon.png', 32, 1],
  ['tools/icon-1024.png', 1024, 1],
];

const draw = async ([b64, size, scale]) => {
  if (!window.__brico) {
    const buf = Uint8Array.from(atob(b64), (ch) => ch.charCodeAt(0)).buffer;
    const face = new FontFace('Brico', buf, { weight: '200 800' }); await face.load(); document.fonts.add(face);
    window.__brico = true;
  }
  const S = 1024, c = document.createElement('canvas'); c.width = c.height = size;
  const x = c.getContext('2d');
  x.scale(size / S, size / S);
  x.fillStyle = '#0b0d12'; x.fillRect(0, 0, S, S);
  const glow = (cx, cy, r, rgb, a) => {
    const g = x.createRadialGradient(cx, cy, 0, cx, cy, r);
    g.addColorStop(0, `rgba(${rgb},${a})`); g.addColorStop(1, `rgba(${rgb},0)`);
    x.fillStyle = g; x.fillRect(0, 0, S, S);
  };
  glow(-80, -60, 760, '242,183,102', 0.16);
  glow(1110, 40, 640, '169,178,255', 0.12);
  glow(1080, 1120, 760, '95,208,191', 0.12);
  x.translate(S / 2, S / 2); x.scale(scale, scale); x.translate(-S / 2, -S / 2);
  const rows = [['Eng', '242,183,102'], ['lish', '95,208,191'], ['B2', '169,178,255']];
  const left = 178;
  x.font = '800 236px Brico'; x.textBaseline = 'alphabetic';
  rows.forEach(([t, rgb], i) => {
    const y = 318 + i * 228;
    x.save();
    x.shadowColor = `rgba(${rgb},.5)`; x.shadowBlur = 46 * size / S;
    x.fillStyle = `rgb(${rgb})`; x.fillText(t, left, y);
    x.restore();
  });
  rows.forEach(([, rgb], i) => {
    x.save();
    x.shadowColor = `rgba(${rgb},.6)`; x.shadowBlur = 24 * size / S;
    x.fillStyle = `rgb(${rgb})`; x.beginPath(); x.roundRect(left + 6 + i * 158, 838, 128, 22, 11); x.fill();
    x.restore();
  });
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
