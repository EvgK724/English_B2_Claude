"""Validate that source clips match the requested text and Ryan voice."""
import hashlib
import json

VOICE = "en-GB-RyanNeural"


def identity(clip):
    return {"voice": VOICE, "text": clip["text"], "rate": clip.get("rate", "-5%"),
            "pitch": "+0Hz", "volume": "+0%"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def signature(clip):
    return digest(json.dumps(identity(clip), sort_keys=True, ensure_ascii=False).encode())


def matches(clip, directory):
    audio = directory / f"{clip['key']}.mp3"
    meta = directory / f"{clip['key']}.ryan.json"
    try:
        record = json.loads(meta.read_text())
        return (record.get("voice") == VOICE and record.get("signature") == signature(clip)
                and record.get("sha256") == digest(audio.read_bytes()) and audio.stat().st_size > 1024)
    except (OSError, ValueError):
        return False


def require_clips(clips, directory):
    missing = [c["key"] for c in clips if not matches(c, directory)]
    if missing:
        raise ValueError(f"Missing verified Ryan recordings: {', '.join(missing)}. Run tools/ryan_tts.py first.")
