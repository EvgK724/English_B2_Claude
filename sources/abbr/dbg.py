import asyncio, json, time, pathlib, subprocess, sys
from playwright.async_api import async_playwright
root = pathlib.Path("abbr").resolve()
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8830", "--bind", "127.0.0.1"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
async def run():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for w, h in [(1180, 760), (390, 763)]:
            ctx = await b.new_context(viewport={"width": w, "height": h}); pg = await ctx.new_page()
            await pg.goto("http://127.0.0.1:8830/preview.html"); await pg.wait_for_timeout(300)
            r = await pg.evaluate("""(() => { autoSpeak = false; setTab('drill'); const box = document.getElementById('card');
                queue = [CARDS[0]]; index = 0; render(); flip();
                const kids = [...box.children].filter(n => !n.hidden).map(n => [n.id || n.className, Math.round(n.getBoundingClientRect().height)]);
                const back = [...document.getElementById('back').children].map(n => [n.id || n.className, Math.round(n.getBoundingClientRect().height)]);
                const cs = getComputedStyle(box);
                return { client: box.clientHeight, scroll: box.scrollHeight, pad: cs.paddingTop + ' ' + cs.paddingBottom, gap: cs.rowGap, kids, back,
                         view: Math.round(document.getElementById('drill').getBoundingClientRect().height), app: Math.round(document.querySelector('.app').getBoundingClientRect().height) }; })()""")
            print(w, h, json.dumps(r))
            await ctx.close()
        await b.close()
try: asyncio.run(run())
finally: srv.terminate()
