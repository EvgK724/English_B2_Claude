# Daily decks with Codex

Repository: `EvgK724/English_B2_Claude`, branch `main`.
Published application: https://evgk724.github.io/English_B2_Claude/site/

The two Codex tasks update GitHub directly. The old Claude standalone artifacts
and the former 11:52 artifact transfer are no longer prerequisites. This document
does not install a schedule. The former tile footers specify approximately 08:00
for Breaking Bad and 11:00 for phrasal verbs, in Asia/Yekaterinburg; the scheduler
configuration must be managed separately, without duplicate tasks.

## Runtime

Python 3.11+, Node.js (the current Pages workflow uses 22), ffmpeg on PATH, and
`edge-tts==7.3.1` from `tools/requirements-audio.txt`. Use a virtual environment.
GitHub push access and network access to Microsoft's speech service must already
be available. No API key, paid speech service, or new credential is required.
If speech generation or authorization fails, stop without publishing a partial
batch. Do not change voices, install unrelated software, or alter other tasks.

For the migration's local checkout the prepared interpreter is
`../audio-venv/bin/python`, with ffmpeg in `../audio-bin`. These local paths are
not portable; a cloud runner uses its own provisioned interpreter and ffmpeg.

## Each run

1. Use a clean, current checkout of `main`. Read `AGENTS.md`, this file, and the
   last cards in `site/apps/<key>.html`. Use an isolated checkout if another task
   is working in the repository. Run `git pull --ff-only` before preparing data.
2. Run `python tools/daily_deck.py status phrasal` or `status bbapp`. The script
   computes today's date in Asia/Yekaterinburg. If today's quota is complete,
   stop successfully. A partial quota or inconsistent ledger requires inspection;
   never add another full batch to it. Do not backfill missed days.
3. Choose exactly one new phrasal verb or two new Breaking Bad units, checking all
   existing IDs and terms. Check their meaning and usage in a reputable dictionary.
   For Breaking Bad, verify the actual phrase and speaker against a script and the
   aired episode's transcript/subtitles. A draft script alone is insufficient
   where the broadcast differs. Prefer short useful excerpts. Never invent a
   series attribution or copy a long scene. Examples and explanations are original.
4. Write the JSON batch described below outside the repository. `date` and every
   card's `added` must equal the date returned by `status`.
5. Run `python tools/daily_deck.py append <key> /absolute/path/batch.json`.
   It synthesizes and decodes two clips per card before changing published files,
   checks duplicates and daily quota, preserves old audio bytes/IDs, records source
   URLs and audio fingerprints, updates the catalog/index, and rebuilds the shell.
   No device-speech fallback is accepted. The append operation uses one repo lock
   and staged replacements with rollback on caught write/build failures.
6. Review the bounded diff and validate:

   ```sh
   python -m unittest discover -s tools -p 'test_daily_deck.py' -v
   node --test tools/test_audio_clips.mjs
   python tools/ensure_ryan_audio.py --check
   git diff --check
   ```

   Check the new ledger's clip offsets/hashes against the pack and inspect the
   actual new cards. The append command decodes both raw and packed clips and
   saves their checksums. Existing historical card objects must be unchanged.
7. Commit only `site/apps/<key>.html`, `site/packs/<key>.mp3`, `tools/packs.json`,
   `tools/catalog.json`, `site/index.html`, `site/sw.js`, today's
   `data/daily/<date>-<key>.json`, and (for phrasal only)
   `tools/ryan-audio-state.json`. Commit and push to `main`; never force-push.
   If the push is rejected, fetch the new head, inspect what changed, and start
   from a clean current checkout. Re-check the daily quota before reapplying;
   another runner may already have published it. Do not manually merge generated
   pack offsets or overwrite newer content.
8. Verify the existing `Ryan audio and Pages` workflow succeeds for the published
   head and compare the live `/site/` HTML, relevant app, pack and hashes. Open the
   tile, find the new cards, and play term and example audio. A successful push
   alone is not proof of deployment. Report date, new terms, commit and deployment
   result. Do not tell the user a failed/queued deployment is live.

The shared append lock covers repository writes; it does not lock a later Git
push. Isolated checkouts plus a normal fast-forward push and a fresh quota check
on rejection prevent concurrent tasks from silently overwriting each other.

## Batch shape and style

```json
{
  "date": "YYYY-MM-DD",
  "cards": [
    {
      "id": "stable-unique-slug",
      "au": 1,
      "added": "YYYY-MM-DD",
      "term": "go over",
      "ipa": "/ˌɡəʊ ˈəʊvə/ · went over · gone over",
      "pos": "phrasal verb · переходный · неразделяемый",
      "ru": "Короткий перевод — уточнение значения",
      "note": "Русское пояснение: употребление, управление, частая ошибка, отличие от близкого выражения.",
      "ex": "An original English example.",
      "exru": "Перевод собственного примера.",
      "sources": [{"url": "https://dictionary.example/entry", "title": "Checked reference"}]
    }
  ]
}
```

`bbapp` requires two objects and uses `who` and `reg` instead of `ipa` and `pos`.
Add episode, speaker, locator/timecode and excerpt status in source metadata.
Sources are saved in the repository ledger, not inserted into the existing card
layout. `term` is the verified excerpt; `ex` is an original everyday/workplace
example, never represented as dialogue from the show.

Phrasal cards retain a useful short translation, British IPA and verb forms,
transitivity/separability, Russian usage guidance and a natural B1–B2 example.
Use medical/workplace contexts only as clearly fictional language examples unless
any clinical claims have been independently verified. Existing SRS intervals
`[1,3,7,16,35,90]`, IDs, `flashcards:state` and `bbphrases:state` stay unchanged.

## Speech identity

The existing corpus and `CLAUDE.md` identify phrasal as Ryan, en-GB, and Breaking
Bad as Andrew, en-US. Older BB files do not retain the precise original synthesis
request. New BB recordings explicitly use the standard `en-US-AndrewNeural`
voice (not the separate multilingual voice); all old recordings remain byte-for-byte
unchanged. New clips use rate `-5%`, pitch `+0Hz`, volume `+0%`; each ledger records
the exact voice, text, parameters and SHA-256 values. This is synthetic Microsoft
speech, not the actors' recordings.

The existing hourly `ryan-pages.yml` job retries audio/publication failures; it
does not create daily teaching content. Breaking Bad is intentionally excluded
from its Ryan generation. Keep that behavior and existing retry schedule.
