# Microsoft Ryan only; validates voice/text before reusing existing files.
import asyncio
import pathlib
import sys

here = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(here.parents[1] / "tools"))
from ryan_tts import generate

if __name__ == "__main__":
    asyncio.run(generate([(here / "clips.json", here / "audio")]))
