# Записи для тренажёра «Increase by и increase to» голосом Microsoft Ryan (en-GB-RyanNeural) через edge-tts: incr/clips.json → incr/audio/<ключ>.mp3.
# Запуск из sources/: pip install edge-tts; python3 incr/tts.py   (уже записанные файлы пропускаются)
import asyncio, json, os, pathlib
import edge_tts, edge_tts.communicate as comm

here = pathlib.Path(__file__).parent
if os.path.exists("/root/.ccr/ca-bundle.crt"):                 # прокси облачной среды Claude Code
    comm._SSL_CTX.load_verify_locations("/root/.ccr/ca-bundle.crt")
VOICE = "en-GB-RyanNeural"

async def one(c, sem):
    path = here / "audio" / f"{c['key']}.mp3"
    if path.exists() and path.stat().st_size > 1024: return 0
    async with sem:
        for attempt in range(4):
            try:
                await edge_tts.Communicate(c["text"], VOICE, rate=c["rate"], proxy=os.environ.get("HTTPS_PROXY")).save(str(path))
                if path.stat().st_size > 1024: return 1
            except Exception as e:
                err = e
            await asyncio.sleep(2 ** attempt)
        raise RuntimeError(f"{c['key']}: {err!r}")

async def main():
    (here / "audio").mkdir(exist_ok=True)
    clips = json.loads((here / "clips.json").read_text())
    sem = asyncio.Semaphore(4)
    n = sum(await asyncio.gather(*(one(c, sem) for c in clips)))
    print("записано", n, "из", len(clips))

asyncio.run(main())
