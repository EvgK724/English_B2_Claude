import asyncio, json, time, pathlib, subprocess, sys
from playwright.async_api import async_playwright
from PIL import Image
root = pathlib.Path("irreg").resolve()
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8790", "--bind", "127.0.0.1"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
URL = "http://127.0.0.1:8790/preview.html"
shots = []
async def run():
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"])
        errors = []
        async def mk(w, h):
            ctx = await b.new_context(viewport={"width": w, "height": h}, device_scale_factor=2)
            pg = await ctx.new_page()
            pg.on("pageerror", lambda e: errors.append(str(e)))
            pg.on("console", lambda m: errors.append("console:" + m.text) if m.type == "error" else None)
            pg.on("requestfailed", lambda r: errors.append("reqfail:" + r.url))
            await pg.goto(URL); await pg.wait_for_timeout(400)
            return ctx, pg
        async def shot(pg, name):
            path = root / f"s-{name}.png"; await pg.screenshot(path=str(path)); shots.append(path)
        ctx, pg = await mk(390, 800)
        await shot(pg, "rule")
        H = await pg.evaluate("document.getElementById('rule').scrollHeight")
        out["rule_height"] = H
        for k, y in enumerate([700, 1500, 2300, 3100, 3900]):
            if y > H - 400: break
            await pg.evaluate(f"document.getElementById('rule').scrollTop = {y}"); await pg.wait_for_timeout(120)
            await shot(pg, f"rule{k+2}")
        out["hscroll"] = await pg.evaluate("document.documentElement.scrollWidth > window.innerWidth")
        # каждая таблица семьи помещается по ширине телефона
        out["table_overflow"] = await pg.evaluate("""(() => { const bad = []; TOPICS.filter(t => t.kind === 'fam').forEach(t => {
            openTopic = t.n; renderTopics(); const tb = document.querySelector('.vt'); const r = tb.getBoundingClientRect();
            const body = document.querySelector('.t-body').getBoundingClientRect();
            if (r.right > window.innerWidth - 16 + 0.5 || r.left < 16 - 0.5 || tb.scrollWidth > tb.clientWidth + 1) bad.push([t.n, Math.round(r.left), Math.round(r.right)]); }); openTopic = null; renderTopics(); return bad; })()""")
        # семья 2 открыта, слушаем всю семью — строки подсвечиваются
        await pg.evaluate("setTab('rule'); openAndShow(2)"); await pg.wait_for_timeout(700)
        await shot(pg, "fam2")
        await pg.click(".fam-play"); await pg.wait_for_timeout(2600)
        out["fam_src"] = await pg.evaluate("player.getAttribute('src')")
        out["fam_time"] = await pg.evaluate("player.currentTime")
        out["fam_on"] = await pg.evaluate("[...document.querySelectorAll('.vt tr.on[data-i]')].map(r => r.dataset.i)")
        out["fam_btn"] = await pg.inner_text(".fam-play")
        await shot(pg, "fam2-play")
        await pg.click(".fam-play"); await pg.wait_for_timeout(150)
        out["fam_after_stop"] = [await pg.evaluate("document.querySelectorAll('.vt tr.on').length"), await pg.inner_text(".fam-play")]
        # поиск
        res = {}
        for q in ["bring", "went", "приносить", "лежать", "learned", "work", "xyz", "по"]:
            await pg.fill("#vsearch", q); await pg.wait_for_timeout(80)
            res[q] = await pg.evaluate("[...document.querySelectorAll('#sres .sr-forms')].map(n => n.textContent).concat([...document.querySelectorAll('#sres .sr-none')].map(n => 'NONE: ' + n.textContent.slice(0, 40)))")
        out["search"] = res
        await pg.fill("#vsearch", "bring"); await pg.wait_for_timeout(80)
        await pg.evaluate("document.getElementById('vsearch').scrollIntoView({block:'start'})"); await pg.wait_for_timeout(100)
        await shot(pg, "search")
        await pg.click(".sr-fam"); await pg.wait_for_timeout(700)
        out["search_open"] = await pg.evaluate("openTopic")
        await pg.fill("#vsearch", ""); await pg.wait_for_timeout(50)
        # схема ведёт к группе
        await pg.evaluate("document.getElementById('rule').scrollTop = 0"); await pg.wait_for_timeout(100)
        await pg.click('.sch-b[data-g="abc"]'); await pg.wait_for_timeout(800)
        out["scheme_jump"] = await pg.evaluate("Math.round(document.querySelector('.t-group[data-g=\"abc\"]').getBoundingClientRect().top - document.getElementById('rule').getBoundingClientRect().top)")
        await shot(pg, "scheme-jump")
        # тема с примерами
        await pg.evaluate("openAndShow(19)"); await pg.wait_for_timeout(700)
        await shot(pg, "topic19")
        # состав первой сессии
        out["first_session"] = await pg.evaluate("""(() => { buildMain(); const n = {}; queue.forEach(c => n['t' + c.t] = (n['t' + c.t] || 0) + 1); return n; })()""")
        out["first_ids"] = await pg.evaluate("FRESH_ORDER.slice(0, 30).map(c => c.id).join(' ')")
        await pg.evaluate("buildMain(); render();")
        await pg.click("#tabDrill"); await pg.wait_for_timeout(150)
        await shot(pg, "q")
        wrong = await pg.evaluate("shownOpts.findIndex(o => o !== queue[index].a && !(queue[index].also && queue[index].also[o]))")
        await (await pg.query_selector_all("#opts .opt"))[wrong].click(); await pg.wait_for_timeout(200)
        out["verdict"] = await pg.inner_text("#verdict")
        out["kind_after"] = await pg.inner_text("#kind")
        out["audio"] = await pg.evaluate("player.getAttribute('src')")
        await shot(pg, "wrong")
        n = 0
        while n < 60:
            await pg.click("#next"); await pg.wait_for_timeout(40)
            if not await pg.evaluate("!!queue[index]"): break
            if n == 3: await shot(pg, "q2")
            i = await pg.evaluate("shownOpts.indexOf(queue[index].a)")
            await (await pg.query_selector_all("#opts .opt"))[i].click(); await pg.wait_for_timeout(40)
            if n == 3: await shot(pg, "right2")
            n += 1
        out["answered"] = n
        out["done"] = await pg.inner_text("#hint")
        # «тоже верно» — семья 12 (show)
        await pg.evaluate("buildTopic(12); setTab('drill'); render();"); await pg.wait_for_timeout(100)
        for k in range(10):
            has_also = await pg.evaluate("!!(queue[index] && queue[index].also)")
            if has_also:
                alt = await pg.evaluate("shownOpts.findIndex(o => queue[index].also[o])")
                await (await pg.query_selector_all("#opts .opt"))[alt].click(); await pg.wait_for_timeout(120)
                out["also_verdict"] = await pg.inner_text("#verdict")
                await shot(pg, "also")
                break
            i = await pg.evaluate("shownOpts.indexOf(queue[index].a)")
            await (await pg.query_selector_all("#opts .opt"))[i].click(); await pg.wait_for_timeout(60)
            await pg.click("#next"); await pg.wait_for_timeout(60)
        out["topic_status"] = await pg.inner_text("#status")
        # предложение из темы 18
        await pg.evaluate("buildTopic(18); setTab('drill'); render();"); await pg.wait_for_timeout(100)
        await shot(pg, "sent")
        out["mixed_size"] = await pg.evaluate("buildTopic(MIXED_TOPIC), queue.length")
        # самые длинные варианты на телефоне
        await pg.evaluate("queue = [CARDS.find(c => c.id === 'v-understand')]; index = 0; mode = 'topic'; topicN = 6; render();"); await pg.wait_for_timeout(100)
        await shot(pg, "long")
        out["long_overflow"] = await pg.evaluate("[...document.querySelectorAll('#opts .opt')].some(b => b.scrollWidth > b.clientWidth + 1)")
        await ctx.close()
        for (w, h, name) in [(1180, 760, "pad-land"), (820, 1130, "pad-port")]:
            ctx, pg = await mk(w, h)
            await pg.evaluate("openAndShow(4)"); await pg.wait_for_timeout(600)
            await shot(pg, name + "-rule")
            await pg.click("#go"); await pg.wait_for_timeout(200)
            await shot(pg, name + "-q")
            out[name + "_hscroll"] = await pg.evaluate("document.documentElement.scrollWidth > window.innerWidth")
            await ctx.close()
        await b.close()
    out["errors"] = errors
    print(json.dumps(out, ensure_ascii=False, indent=1))
try:
    asyncio.run(run())
finally:
    srv.terminate()
def sheet(paths, name, h=560):
    ims = [Image.open(p) for p in paths]
    ims = [im.resize((int(im.width * h / im.height), h)) for im in ims]
    W = sum(im.width for im in ims) + 10 * (len(ims) + 1)
    s = Image.new("RGB", (W, h + 20), (60, 60, 60)); x = 10
    for im in ims: s.paste(im, (x, 10)); x += im.width + 10
    s.save(root / name)
phone = [p for p in shots if "pad" not in p.name]
third = (len(phone) + 2) // 3
sheet(phone[:third], "sheet1.png"); sheet(phone[third:2 * third], "sheet2.png"); sheet(phone[2 * third:], "sheet3.png")
sheet([p for p in shots if "pad" in p.name], "sheet4.png", 420)
