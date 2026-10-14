"""Generate verified Ryan clips, reusing only matching Ryan recordings.

python -m pip install -r tools/requirements-audio.txt
python tools/ryan_tts.py encour vnoun like without
python tools/ryan_tts.py --clips /path/clips.json --out /path/audio

Each sources/<app>/clips.json is produced by its clips.py. ffmpeg must be on PATH.
No pack is changed here; assemble it only after this command succeeds.
"""
import argparse
import array
import asyncio
import json
import pathlib
import shutil
import subprocess

import edge_tts
from aiohttp import WSServerHandshakeError
from ryan_manifest import VOICE, digest, identity, matches, signature

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERSION = "7.3.1"


def validate_audio(path):
    pcm = subprocess.run(
        ["ffmpeg", "-v", "error", "-xerror", "-i", str(path),
         "-f", "s16le", "-ac", "1", "-ar", "24000", "-"],
        capture_output=True, check=True, timeout=30,
    ).stdout
    samples = array.array("h", pcm)
    if len(samples) < 2400 or max(map(abs, samples), default=0) < 128:
        raise ValueError(f"Silent or empty recording: {path.name}")
    return round(len(samples) / 24000, 3)


async def generate(inputs):
    if edge_tts.__version__ != VERSION:
        raise RuntimeError(f"Install tools/requirements-audio.txt (edge-tts {VERSION})")
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is required to verify each recording")
    jobs = []
    for manifest, out in inputs:
        clips = json.loads(manifest.read_text())
        if len({c["key"] for c in clips}) != len(clips):
            raise ValueError(f"Duplicate clip keys in {manifest}")
        out.mkdir(parents=True, exist_ok=True)
        jobs.extend((c, out) for c in clips)
    sem = asyncio.Semaphore(4)
    done = 0

    async def one(c, out):
        nonlocal done
        key, text, rate = c["key"], c["text"], c.get("rate", "-5%")
        if pathlib.Path(key).name != key or not text.strip():
            raise ValueError(f"Invalid clip: {key}")
        path = out / f"{key}.mp3"
        meta_path = out / f"{key}.ryan.json"
        if matches(c, out):
            done += 1
            return
        async with sem:
            temporary = path.with_suffix(".part.mp3")
            try:
                for attempt in range(3):
                    try:
                        await edge_tts.Communicate(text, VOICE, rate=rate, pitch="+0Hz", volume="+0%").save(str(temporary))
                        duration = await asyncio.to_thread(validate_audio, temporary)
                        break
                    except WSServerHandshakeError as error:
                        if error.status in (401, 403) or attempt == 2:
                            raise
                        await asyncio.sleep(2 ** (attempt + 1))
                    except Exception:
                        if attempt == 2:
                            raise
                        await asyncio.sleep(2 ** (attempt + 1))
                meta = {**identity(c), "signature": signature(c), "sha256": digest(temporary.read_bytes()),
                        "duration": duration, "edge_tts": VERSION}
                temporary.replace(path)
                meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
                done += 1
                if done % 20 == 0 or done == len(jobs):
                    print(f"Ryan: {done}/{len(jobs)} verified", flush=True)
            finally:
                temporary.unlink(missing_ok=True)

    await asyncio.gather(*(one(c, out) for c, out in jobs))
    print(f"Ready: {len(jobs)} Ryan recordings", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("apps", nargs="*")
    parser.add_argument("--clips", type=pathlib.Path)
    parser.add_argument("--out", type=pathlib.Path)
    args = parser.parse_args()
    if args.clips or args.out:
        if not args.clips or not args.out or args.apps:
            parser.error("Use --clips and --out together, without app names")
        inputs = [(args.clips, args.out)]
    else:
        if not args.apps or "bbapp" in args.apps:
            parser.error("Choose source apps; Breaking Bad keeps its existing voice")
        inputs = [(ROOT / "sources" / app / "clips.json", ROOT / "sources" / app / "audio") for app in args.apps]
    asyncio.run(generate(inputs))


if __name__ == "__main__":
    main()
