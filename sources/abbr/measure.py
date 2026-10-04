import asyncio, json, time, pathlib, subprocess, sys
from playwright.async_api import async_playwright
root = pathlib.Path("abbr").resolve()
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8829", "--bind", "127.0.0.1"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
async def run():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for w, h in [(390, 763), (375, 647), (430, 839), (1180, 760), (1180, 796), (820, 1130)]:
            ctx = await b.new_context(viewport={"width": w, "height": h}); pg = await ctx.new_page()
            await pg.goto("http://127.0.0.1:8829/preview.html"); await pg.wait_for_timeout(300)
            r = await pg.evaluate("""(() => { autoSpeak = false; setTab('drill'); const box = document.getElementById('card'); const t = [];
                CARDS.forEach(c => { queue = [c]; index = 0; render(); flip(); const d = box.scrollHeight - box.clientHeight; if (d > 1) t.push([c.id, d]); });
                t.sort((a, b) => b[1] - a[1]); return { n: t.length, worst: t.slice(0, 6), k: getComputedStyle(document.documentElement).getPropertyValue('--k'), card: box.clientHeight }; })()""")
            print(w, h, json.dumps(r))
            await ctx.close()
        await b.close()
try: asyncio.run(run())
finally: srv.terminate()
