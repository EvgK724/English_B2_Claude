# Английский B2 — Codex

Read `CLAUDE.md` for the existing application structure and content style. For the
two daily decks, the current procedure is `tools/DAILY_DECKS.md`; it supersedes the
old Claude artifact transfer procedure only for `phrasal` and `bbapp`.

- Preserve existing card IDs, localStorage keys, intervals, layouts, and audio.
- Daily limit: one `phrasal` card, two `bbapp` cards, dated in `Asia/Yekaterinburg`.
  Do not fill missed dates in bulk. A completed day is a successful no-op.
- Voices: phrasal Microsoft Ryan (`en-GB-RyanNeural`); Breaking Bad Microsoft
  Andrew (`en-US-AndrewNeural`). Never replace unavailable recordings with another
  voice or device speech for publication.
- Verify Breaking Bad excerpts and speakers from sources; retain provenance in
  the daily ledger. Write original teaching examples; do not invent quotations.
- Use `tools/daily_deck.py` to append, validate audio, update indexes and rebuild
  cache hashes together. Do not run the historical `sources/*/build.py` files.
- Scheduled work may publish only its reviewed daily update to this repository's
  existing `main` branch. Never force-push; inspect a rejected push and reassess
  today's status against the new head. Keep unrelated applications untouched.
- Scheduling is managed separately in Codex. Do not create additional timers or
  restore the former artifact-to-GitHub transfer task.
