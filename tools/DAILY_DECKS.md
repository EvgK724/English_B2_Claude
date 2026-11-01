# Daily decks: Codex content, GitHub Actions speech and publication

Repository: `EvgK724/English_B2_Claude`, branch `main`.
Application: https://evgk724.github.io/English_B2_Claude/site/

The user explicitly authorized this execution path on 2 November 2026. Codex
prepares verified teaching content without contacting the speech service. The
existing `Ryan audio and Pages` workflow creates recordings and publishes only
complete decks. The Claude artifacts and former 11:52 transfer are no longer
prerequisites. Scheduling is managed separately in Codex; do not create or change
timers. The existing GitHub hourly retry is not a generator of teaching content.
The daily quota for 2 November was already completed before this migration.

## Codex runtime

Python 3.11+ and an already authorized way to read/write this repository are
sufficient. Queue preparation uses the Python standard library only: no edge-tts,
ffmpeg, Node, Microsoft speech domain or speech API key is required in Codex Cloud.

Preserve the cloud network policy, inherited proxy configuration and TLS
verification. A policy denial is not permission to retry through another endpoint,
proxy, transport or credential. The user specifically authorized speech in GitHub
Actions; this is the documented execution path, not an implicit response to a denial.

Use the environment's existing GitHub integration or supported Git workflow.
Public fetch and an up-to-date `git push --dry-run` do not prove actual write
access. Actual write access from a fresh cloud task still needs confirmation.
If publication is unavailable, preserve the validated request and report the
exact blocker. Do not create a PAT, broaden grants, add paid services or use the
`gh` path that was explicitly denied in the cloud diagnostic.

## Each Codex run

1. Use a clean, current, isolated checkout of `main`. Read `AGENTS.md`, this file
   and recent cards in `site/apps/<key>.html`. Pull with `git pull --ff-only`.
2. Run `python tools/daily_queue.py status phrasal` or `status bbapp`.
   The date is calculated in `Asia/Yekaterinburg`.
   - `complete`: do not add cards; a successful no-op. This describes repository
     state, so verify deployment before claiming that the result is live.
   - `queued`: do not prepare another batch. Report the existing request and
     inspect its Actions result. An older outstanding request also blocks a new
     request for that deck.
   - `conflict`: stop and report the exact inconsistency.
   - `pending`: continue with today's new content.
3. Choose exactly one new phrasal verb or two short Breaking Bad units. Check all
   existing terms/IDs and verify meaning/usage with reliable sources. For BB verify
   exact wording and speaker against a script and the aired episode's transcript
   or subtitles. A draft alone is insufficient where it differs from broadcast.
   Do not invent quotations or copy long scenes. Examples/explanations are original.
4. Write the batch JSON below outside the repository. `date` and each `added`
   must equal the date from status. Do not backdate or fill missed dates in bulk.
5. Run `python tools/daily_queue.py prepare <key> /absolute/path/batch.json`.
   This validates the quota, duplicates, source metadata and current state, then
   creates only `data/requests/YYYY-MM-DD-<key>.json`. It does not change the site
   or generate audio. An identical retry is a no-op; a conflicting request stops.
6. Review that single JSON, its sources and the diff. Run:

   ```sh
   python tools/daily_queue.py verify
   python -m unittest discover -s tools -p 'test_daily_queue.py' -v
   git diff --check
   ```

   Commit only the exact new request file, then normal push to `main`. Never
   force-push, edit a committed request or mix unrelated changes. With a GitHub
   connector, use its supported atomic commit/ref flow against the freshly read
   parent SHA, or an exact-path create operation that rejects an existing file.
   Do not overwrite an existing request. No new credentials or broader scope are
   required by this design; whether the executor can actually write must be tested.
7. If push/ref update is rejected, read fresh `main` in a clean checkout and run
   status again. If the same request is already queued/complete, do not duplicate
   it. Re-prepare only if still pending and still the same local day. Do not merge
   MP3 files, offsets or generated journals manually. A date rollover before
   submission requires fresh current-day preparation, not a backdated push.
8. Observe the existing Actions workflow, its generated audio commit and Pages
   deployment. Fetch resulting `main`, confirm request/ledger agreement and compare
   the live app, audio pack and cache hashes. A submitted request or green unit
   tests alone are not proof of publication. Report `queued`, `failed` or
   `published` accurately, with date, terms and commit/run links. If the job
   continues past the task, report queued; the existing hourly workflow owns retries.

`au: 1` in a request is the required final card shape, not a claim that audio
already exists. Requests are outside the deployed site and cannot be displayed
to learners before the publishing workflow finishes them.

## Batch shape and teaching style

```json
{
  "date": "YYYY-MM-DD",
  "cards": [{
    "id": "stable-unique-slug",
    "au": 1,
    "added": "YYYY-MM-DD",
    "term": "a new phrasal verb",
    "ipa": "/British IPA/ · past form · past participle",
    "pos": "phrasal verb · переходный · разделяемый",
    "ru": "Короткий перевод — уточнение значения",
    "note": "Употребление, управление, типичная ошибка, отличие от близкого выражения.",
    "ex": "An original natural English example.",
    "exru": "Перевод собственного примера.",
    "sources": [{"url": "https://dictionary.example/entry", "title": "Verified reference"}]
  }]
}
```

Replace the example URL with the actual checked source. Each source requires
`url` (HTTP(S), without credentials) and `title`; additional evidence metadata
is retained. Optional source metadata must be valid finite JSON.

`bbapp` requires two cards, using `who` and `reg` instead of `ipa` and `pos`.
Include episode, speaker, locator/timecode and short-excerpt status in source
metadata. Its `term` is a verified excerpt; `ex` is an original everyday/workplace
example, never represented as dialogue from the show. Phrasal cards retain British
IPA, verb forms, transitivity/separability, Russian usage guidance and natural
B1–B2 examples. Medical examples are fictional and must not introduce unchecked
treatment claims.

Preserve IDs, layouts, localStorage keys `flashcards:state`/`bbphrases:state`
and intervals `[1,3,7,16,35,90]`. Existing content and correct audio stay unchanged.

## Queue and retry contract

Requests are immutable receipts and remain at
`data/requests/YYYY-MM-DD-<key>.json` after completion. The envelope contains
`schema`, `deck`, `submitted_at` (UTC), `batch` and `batch_sha256`. Let
`prepare` generate it; do not construct or alter its timestamp/hash manually.
The matching `data/daily/YYYY-MM-DD-<key>.json` records reviewed sources and
verified audio text, voice, parameters, offsets and hashes.

New preparation accepts today only. An already-submitted request may finish after
midnight: its UTC submission timestamp must fall on its original Yekaterinburg
date. At most one outstanding request per deck is allowed. This permits retrying
an approved batch without inventing a backlog of missed days. `verify` permits a
valid outstanding queue; the publishing gate `check` requires it to be complete.

`process` validates all pending requests before synthesis, runs each through
`daily_deck.append_batch` in an isolated staged copy, and installs the bounded
output bundle only after all batches succeed. A failed second deck cannot leave
the first deck partially installed. Existing files are restored on caught write
failures. A repository lock protects local operations; normal Git push/ref
comparison prevents one checkout from silently overwriting a newer remote head.

## Publishing workflow

The existing `.github/workflows/ryan-pages.yml` retains its permissions, single
`english-b2-pages` concurrency group and `23 * * * *` hourly retry. GitHub runs
Python 3.11, Node 22, ffmpeg and pinned `edge-tts==7.3.1`. No new secret is used.

1. Run extraction, queue and safe-publication regression tests.
2. Verify fresh Ryan and Andrew in an isolated queue roundtrip when the tracked
   pipeline code changes, or on `workflow_dispatch` with `verify_tts: true`.
   Six synthetic test recordings and their cards stay in a temporary copy and
   never enter the published site. `tools/speech-smoke-state.json` records the
   source hash, GitHub run and audio evidence; unchanged code reuses that evidence.
3. Run `python tools/daily_queue.py process`.
4. Run Ryan ensure/check, then separate Andrew ensure/check, queue `check` and
   speech-evidence `--check`. No incomplete request may pass publication.
5. Commit generated audio, HTML, indexes, state and daily journals together; push
   without force and reject a stale head. Publish one verified Pages artifact.
   A scheduled run skips redeployment when the published shell already matches.

If synthesis, validation or push fails before deployment, the prior complete
Pages deployment remains. Every retry starts from current `main`; it never merges
generated MP3/index conflicts. Push-triggered and hourly jobs use the same workflow
and concurrency group. If a newer request arrives during generation, a rejected
generated commit is left unpublished and a later run processes fresh main.
The head is checked again immediately before deployment; no partial audio bundle
is published. A deployment failure is reported as such, even if its audio commit
was saved; the hourly workflow can retry the deployment.

## Voices and the approved historical repair

Phrasal: `en-GB-RyanNeural`; BB: standard `en-US-AndrewNeural`. New clips use
rate `-5%`, pitch `+0Hz`, volume `+0%`. These are synthetic Microsoft voices,
not actors' recordings. Never substitute another voice or device TTS for publication.

Ryan's global extractor continues to exclude BB. Andrew has its own state/checks;
new daily clips are adopted only from matching verified ledgers. Historical bytes
are fingerprinted with `baseline_parameters_verified: false`, without claiming
that old synthesis parameters were recovered. Four explicitly approved old cards
receive their missing term/example recordings: `what-the-hell`,
`sorry-for-your-loss`, `smartest-guy-i-ever-met`, `could-have-saved-her`.
Their content/IDs stay unchanged; only `au: 1` is added after verification.
Other missing/replaced/changed old Andrew recordings stop for inspection rather
than being silently overwritten.

The two complete task prompts are in [CODEX_DAILY_PROMPTS.md](CODEX_DAILY_PROMPTS.md).
