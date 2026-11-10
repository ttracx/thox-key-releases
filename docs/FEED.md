# Update feed (`thoxkey-update-feed/1`)

ThoxKey Start reads this repository's [`feed.json`](../feed.json) at
`https://raw.githubusercontent.com/ttracx/thox-key-releases/main/feed.json`, the value a key package sets
in `thoxkey/start.json` as `update_feed.url`.

```json
{"schema":"thoxkey-update-feed/1","channel":"stable","releases":[
 {"host":"windows","version":"0.4.1","tag":"start-windows-v0.4.1","published":"2026-11-10",
  "release_url":"https://github.com/ttracx/thox-key-releases/releases/tag/start-windows-v0.4.1",
  "notes_url":"https://github.com/ttracx/thox-key-releases/blob/main/notes/start-windows-v0.4.1.md",
  "package_sha256":"<64 hex>","assets":[{"name":"Start-ThoxKey.exe","sha256":"<64 hex>"}]}]}
```

| Field | Rule |
| --- | --- |
| `host` | `windows`, `macos` or `linux` |
| `version` | `major.minor.patch[-pre]`; a prerelease sorts before its release |
| `release_url`, `notes_url` | https on `github.com` (this repository) |
| `tag`, `published`, `package_sha256`, `assets` | optional; malformed values are dropped |

How ThoxKey Start uses it: only when the person presses **Check for updates**; at most one request a
minute; 10 s and 64 KiB limits; strict JSON (a duplicate key fails the whole feed); no cookie, key id or
host id sent; nothing downloaded or installed. It picks the newest entry for its computer type and answers
`available` or `current`. Source of those rules: `ttracx/thox-key` `starter/DEVICE_API.md`.

Keep one entry per computer type and version. Old entries may stay; the newest wins.
