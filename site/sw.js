// Офлайн-кэш «Английского» на GitHub Pages. Шаблон: site/sw.js собирает tools/mk_shell.py.
// Оболочка (index.html) — сначала сеть, потом кэш: в ней версии всех остальных файлов.
// Тренажёры и пакеты звука адресуются с ?v=<хэш>: они не меняются, поэтому — сначала кэш.
// Тренажёры кэшируются заранее при установке, звук — при первом открытии темы (все пакеты — около 70 МБ).
const VERSION = "e57c8ad6c828";
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
 "theme.css?v=e3aba0a4",
 "apps/top10.html?v=11ab0c51",
 "apps/artikli.html?v=c988ea95",
 "apps/bez-a-an.html?v=13d936d4",
 "apps/countable.html?v=10b69bd7",
 "apps/tenses.html?v=83c94c05",
 "apps/irreg.html?v=5c0920da",
 "apps/passive.html?v=c68bbd97",
 "apps/gonebeen.html?v=008bbb50",
 "apps/stative.html?v=c72dce7b",
 "apps/usedto.html?v=f0281b30",
 "apps/would.html?v=e6f5b9fe",
 "apps/cond.html?v=4d14268f",
 "apps/hsd.html?v=d07f9603",
 "apps/modal.html?v=578ba99c",
 "apps/can.html?v=9456eec2",
 "apps/manage.html?v=4c2b7bf3",
 "apps/toing.html?v=f579978a",
 "apps/vm.html?v=495ffff1",
 "apps/prepi.html?v=00c36c1c",
 "apps/kogo.html?v=a6dcf5ca",
 "apps/preps.html?v=8cedaaa6",
 "apps/into.html?v=d66ec53a",
 "apps/tofor.html?v=da652296",
 "apps/adjprep.html?v=30b0fe20",
 "apps/makedo.html?v=3d62b518",
 "apps/htp.html?v=0baab8d6",
 "apps/go.html?v=c4c50474",
 "apps/life.html?v=fdc24a39",
 "apps/twotoo.html?v=bfb0e6a3",
 "apps/thereit.html?v=428aad9f",
 "apps/pron.html?v=b104b5f7",
 "apps/adjadv.html?v=497620ac",
 "apps/cmp.html?v=c72b803a",
 "apps/similar.html?v=d498b48f",
 "apps/pairs.html?v=ef8ab088",
 "apps/syn.html?v=c87140c1",
 "apps/q.html?v=f50e42cf",
 "apps/rel.html?v=851a89b9",
 "apps/link.html?v=4a5fd737",
 "apps/rep.html?v=6a7adf23",
 "apps/num.html?v=59b55b65",
 "apps/phrasal.html?v=aaba675a",
 "apps/bbapp.html?v=bf7e026d",
 "apps/idm.html?v=81fca3f0",
 "apps/wthr.html?v=b424b8d0",
 "apps/abbr.html?v=96f02a76"
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
      if (res.ok) c.put(abs("./"), res.clone());
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

  if (url.searchParams.has("v")) {
    e.respondWith(caches.open(CACHE).then(async (c) => {
      const hit = await c.match(req);
      if (hit) return hit;
      const res = await fetch(req);
      if (res.ok) await putVersioned(c, req, res.clone());
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
      if (res.ok) await c.put(req, res.clone());
      return res;
    }));
    return;
  }

  // иконки, манифест и прочее: сеть, без сети — кэш
  e.respondWith(caches.open(CACHE).then((c) =>
    fetch(req).then((res) => {
      if (res.ok) c.put(req, res.clone());
      return res;
    }).catch(() => c.match(req).then((hit) => hit || Response.error()))
  ));
});
