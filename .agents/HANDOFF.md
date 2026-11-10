# Agent pickup: thox-key-releases

Last verified: 2026-11-10 by Claude (Odette Lark lane) for Tommy Xaypanya.

## Status

- Public repository for ThoxKey Start release files, notes and `feed.json` (`thoxkey-update-feed/1`).
  Created on Tommy's instruction ("create a new repo for public releases", 2026-11-10).
- Published: `start-windows-v0.4.1` (files copied from the private `ttracx/thox-key` release, SHA-256
  rechecked). No macOS or Linux release.
- Open: key packages do not yet set `update_feed.url` to this feed; ThoxKey Start 0.4.2 (with the check
  routes) is not released. Owner: Codex lane, `ttracx/thox-handoffs` `lanes/thoxkey-updates/`.

## Conventions

- Publish only release files, notes and the feed. No source, key packages, models, serials, key ids or
  tokens.
- Run `python3 scripts/check_feed.py` and the tests before every push. No GitHub Actions.
- Follow `docs/RELEASING.md`.
