import asyncio, subprocess, sys, time, pathlib
from playwright.async_api import async_playwright
root = pathlib.Path("pron").resolve()
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8817", "--bind", "127.0.0.1"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
async def run():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for w, h in [(390, 800), (820, 1130), (1180, 760)]:
            pg = await (await b.new_context(viewport={"width": w, "height": h}, device_scale_factor=2)).new_page()
            await pg.goto("http://127.0.0.1:8817/preview.html"); await pg.wait_for_timeout(300)
            r = await pg.evaluate("""[...document.querySelectorAll('.md, .err, .algo, .ptab, .ptab th, .ptab td, .ptab small')].filter(n => n.scrollWidth > n.clientWidth + 1).map(n => n.className + ' | ' + n.textContent.trim().slice(0, 40) + ' | ' + n.scrollWidth + '>' + n.clientWidth)""")
            print(w, r)
            if w == 390:
                await pg.evaluate("document.querySelector('.ptab').scrollIntoView({block:'start'})"); await pg.wait_for_timeout(100)
                await pg.screenshot(path=str(root / "s-table.png"))
        await b.close()
try: asyncio.run(run())
finally: srv.terminate()
