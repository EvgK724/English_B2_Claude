// Офлайн-кэш «Английского» на GitHub Pages. Шаблон: site/sw.js собирает tools/mk_shell.py.
// Оболочка (index.html) — сначала сеть, потом кэш: в ней версии всех остальных файлов.
// Тренажёры адресуются с ?v=<хэш>: они не меняются, поэтому — сначала кэш; кэшируются заранее при установке.
// Пакеты звука (packs/) сюда не заходят: их грузит и сохраняет сама оболочка (loadPack в shell.html),
// чтобы звук не зависел от работы офлайн-кэша.
const VERSION = "04018ca4be17";
const CACHE = "eng-b2";
const PRECACHE = [
 "manifest.webmanifest",
 "apple-touch-icon.png",
 "favicon.png",
 "icon-192.png",
 "icon-512.png",
 "fonts/bricolage-grotesque-latin-ext-wght-normal.woff2",
 "fonts/bricolage-grotesque-latin-wght-normal.woff2",
 "fonts/gentium-book-plus-greek-400-normal.woff2",
 "fonts/gentium-book-plus-latin-400-normal.woff2",
 "fonts/gentium-book-plus-latin-ext-400-normal.woff2",
 "fonts/golos-text-cyrillic-wght-normal.woff2",
 "fonts/golos-text-latin-ext-wght-normal.woff2",
 "fonts/golos-text-latin-wght-normal.woff2",
 "theme.css?v=b9ffe602",
 "apps/top10.html?v=1aa8de0d",
 "apps/artikli.html?v=deb0583e",
 "apps/bez-a-an.html?v=13d936d4",
 "apps/countable.html?v=948fe5a8",
 "apps/tenses.html?v=06bb60b9",
 "apps/irreg.html?v=7b9b4602",
 "apps/passive.html?v=1356d7fe",
 "apps/gonebeen.html?v=e13ef7a3",
 "apps/stative.html?v=d392e2cf",
 "apps/usedto.html?v=153a52e9",
 "apps/would.html?v=272d520b",
 "apps/cond.html?v=e59d8fc2",
 "apps/hsd.html?v=2ef0b1b9",
 "apps/modal.html?v=2941b7dd",
 "apps/oblig.html?v=e4b943a4",
 "apps/can.html?v=46b82668",
 "apps/manage.html?v=bd51b222",
 "apps/toing.html?v=894b64b2",
 "apps/vm.html?v=dd306dec",
 "apps/prepi.html?v=92f9013e",
 "apps/kogo.html?v=c06491da",
 "apps/preps.html?v=32099f1f",
 "apps/into.html?v=ca3498e4",
 "apps/tofor.html?v=894b5654",
 "apps/adjprep.html?v=ebb7c64f",
 "apps/makedo.html?v=c54afc59",
 "apps/htp.html?v=3adf6222",
 "apps/havea.html?v=c4b67ebd",
 "apps/go.html?v=89e8ae09",
 "apps/life.html?v=c302d33d",
 "apps/twotoo.html?v=04bd63e5",
 "apps/thereit.html?v=af0c44c8",
 "apps/pron.html?v=289753ee",
 "apps/adjadv.html?v=b2f8fd51",
 "apps/cmp.html?v=7294d0ad",
 "apps/similar.html?v=c892f079",
 "apps/pairs.html?v=fe918641",
 "apps/sounds.html?v=7f6a07f8",
 "apps/nverb.html?v=8a293443",
 "apps/syn.html?v=8881450d",
 "apps/q.html?v=ab982380",
 "apps/indq.html?v=81bc8efa",
 "apps/rel.html?v=1fd616be",
 "apps/link.html?v=fd959e34",
 "apps/rep.html?v=7e2d348f",
 "apps/num.html?v=88346ab5",
 "apps/incr.html?v=1c94a2d0",
 "apps/phrasal.html?v=4b9c1210",
 "apps/bbapp.html?v=b0e6096d",
 "apps/idm.html?v=8885f190",
 "apps/wthr.html?v=ae67e6b4",
 "apps/abbr.html?v=b61e5fb8"
];

const SCOPE = new URL("./", self.location).href;
const abs = (u) => new URL(u, SCOPE).href;
const KEEP = new Set(PRECACHE.map(abs));

self.addEventListener("install", (e) => {
  e.waitUntil((async () => {
    const c = await caches.open(CACHE);
    const have = new Set((await c.keys()).map((r) => r.url));
    await c.add(new Request(abs("./"), { cache: "reload" }));  // без оболочки офлайн не работает ничего
    await Promise.allSettled(PRECACHE.filter((u) => !have.has(abs(u))).map((u) => c.add(abs(u))));
    await self.skipWaiting();
  })());
});

self.addEventListener("activate", (e) => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (k !== CACHE) await caches.delete(k);
    const c = await caches.open(CACHE);
    // старые версии тренажёров; пакеты звука чистятся при загрузке новой версии (см. putVersioned)
    for (const r of await c.keys()) {
      const u = new URL(r.url);
      if (/\.(html|css)$/.test(u.pathname) && u.searchParams.has("v") && !KEEP.has(r.url)) await c.delete(r);
    }
    await self.clients.claim();
  })());
});

async function putVersioned(c, req, res) {
  const u = new URL(req.url);
  for (const r of await c.keys()) {
    const o = new URL(r.url);
    if (o.pathname === u.pathname && o.search !== u.search) await c.delete(r);
  }
  await c.put(req, res);
}

function shellFirst(req) {
  // сеть, но не дольше 4 с, если в кэше уже есть оболочка
  return caches.open(CACHE).then(async (c) => {
    const cached = await c.match(abs("./"));
    const net = fetch(req, { cache: "no-cache" }).then((res) => {
      if (res.ok) c.put(abs("./"), res.clone()).catch(() => {});
      return res;
    });
    if (!cached) return net;
    const timeout = new Promise((r) => setTimeout(() => r(cached), 4000));
    return Promise.race([net.catch(() => cached), timeout]);
  });
}

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET" || req.headers.has("range")) return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin || !req.url.startsWith(SCOPE)) return;
  const path = url.href.slice(SCOPE.length).split(/[?#]/)[0];

  if (req.mode === "navigate" || path === "" || path === "index.html") {
    e.respondWith(shellFirst(req));
    return;
  }

  if (path.startsWith("packs/")) return;

  if (url.searchParams.has("v")) {
    e.respondWith(caches.open(CACHE).then(async (c) => {
      const hit = await c.match(req);
      if (hit) return hit;
      const res = await fetch(req);
      // в кэш — без ожидания и без ошибок наружу: даже если кэш не сохранился, тема откроется
      if (res.ok) putVersioned(c, req, res.clone()).catch(() => {});
      return res;
    }));
    return;
  }

  // шрифты не меняются: сначала кэш
  if (path.startsWith("fonts/")) {
    e.respondWith(caches.open(CACHE).then(async (c) => {
      const hit = await c.match(req);
      if (hit) return hit;
      const res = await fetch(req);
      if (res.ok) c.put(req, res.clone()).catch(() => {});
      return res;
    }));
    return;
  }

  // иконки, манифест и прочее: сеть, без сети — кэш
  e.respondWith(caches.open(CACHE).then((c) =>
    fetch(req).then((res) => {
      if (res.ok) c.put(req, res.clone()).catch(() => {});
      return res;
    }).catch(() => c.match(req).then((hit) => hit || Response.error()))
  ));
});
