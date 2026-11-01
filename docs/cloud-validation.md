# Fresh cloud validation — 2 November 2026

Validated from a fresh Codex Cloud environment on 1 November 2026 UTC
(2 November in `Asia/Yekaterinburg`), after fetching `origin/main`.
Tested application commit: `348bcd3eaa79e6b689589ad5ce43bd44dc45a8b4`.
Runtime: Python 3.12.14, Node.js 24.19.0, Git 2.52.0.

## Results

- `python -m unittest discover -s tools -p 'test_*.py' -v`: **55 passed**.
- `node --test tools/test_audio_clips.mjs`: **7 passed**.
- `daily_queue.py status`: both decks **complete** for `2026-11-02`;
  phrasal has 46 cards (1 today), Breaking Bad has 88 (2 today).
- `daily_queue.py verify` and `check`: **ready**, 2 verified daily ledgers,
  no requests and no pending work. No additional teaching cards were created.
- Separate temporary fixtures exercised CLI `prepare` for both decks:
  only the expected request JSON was created; identical retries changed nothing.
  Wrong dates, quotas, missing sources, duplicate IDs and conflicting retries
  were rejected without writes. Publication `check` rejected pending requests.
- `ensure_ryan_audio.py --check`: 5,563 clips across 59 apps; no generation needed.
- `ensure_andrew_audio.py --check`: 176 clips for 88 cards; no generation needed.
- `smoke_daily_audio.py --check`: existing GitHub Actions evidence remains valid
  for pipeline SHA-256 `97fa0ed532d3aa2d57e5b29dd5182f92da24ec578e0b52a29fea43227cd1bb8f`.
- `git diff --check`: passed; the checkout was clean before adding this report.

## Actions and published application

[Run 41346127153](https://github.com/EvgK724/English_B2_Claude/actions/runs/41346127153)
was independently checked through the GitHub connector: the job and every step,
including the final Pages deployment, completed successfully. Its recorded
isolated queue test created six Ryan/Andrew clips; those test cards were not
published. The application includes the eight approved Andrew repair clips.
No speech synthesis ran in this cloud validation.

All seven live assets returned HTTP 200 and matched the tested checkout byte for
byte: root `index.html`, `site/index.html`, both deck HTML files, both MP3 packs
and `site/sw.js`. The [published application](https://evgk724.github.io/English_B2_Claude/site/)
therefore contains the verified deck and audio state. MP3 SHA-256 values:

| Pack | SHA-256 |
| --- | --- |
| phrasal | `3298f38ccafd2a3d0ac901d9f45703e08a75903900294db7b5c56c9fcf73a85b` |
| bbapp | `53f1e2f84ae25b53df4dd54d5c6622fcccde0b58375dd30b676810f153fa7f4c` |

## Publication route and limits

This file is the sole cloud write probe, published with the existing Git
transport using `git push origin HEAD:main`, without force or new credentials.
Its presence on remote `main` is the actual write evidence; a fetch or dry run
alone would not establish that capability. Daily runs use the same route to
publish only `data/requests/YYYY-MM-DD-<deck>.json`; GitHub Actions owns speech,
generated assets and Pages publication.

The workflow excludes `docs/**` from push triggers, and the Pages artifact does
not include this report. This documentation-only commit does not request new
audio or a new deployment. Live asset checks concern the application commit
above. Scheduler configuration and future scheduled execution were not changed
or tested here; this validates the cloud content/write route and the existing
Actions publication path, without an iMac dependency. No new daily batch,
browser playback test, token, grant or network-policy change was performed.
