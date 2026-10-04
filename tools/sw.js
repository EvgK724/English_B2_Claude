// Офлайн-кэш «Английского» на GitHub Pages. Шаблон: site/sw.js собирает tools/mk_shell.py.
// Оболочка (index.html) — сначала сеть, потом кэш: в ней версии всех остальных файлов.
// Тренажёры и пакеты звука адресуются с ?v=<хэш>: они не меняются, поэтому — сначала кэш.
// Тренажёры кэшируются заранее при установке, звук — при первом открытии темы (все пакеты — около 70 МБ).
const VERSION = "/*__VERSION__*/";
const CACHE = "eng-b2";
const PRECACHE = /*__PRECACHE__*/;

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
