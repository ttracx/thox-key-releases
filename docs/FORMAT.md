# List format (`thoxkey-update-feed/1`)

One JSON object. `releases` holds one entry per published ThoxKey Start release, oldest first.

```json
{"schema":"thoxkey-update-feed/1","channel":"stable","releases":[
 {"host":"windows","version":"0.4.1","tag":"start-windows-v0.4.1","published":"2026-11-10",
  "release_url":"https://github.com/ttracx/thox-key/releases/tag/start-windows-v0.4.1",
  "package_sha256":"<64 hex>",
  "assets":[{"name":"Start-ThoxKey.exe","sha256":"<64 hex>"}]}]}
```

| Field | Meaning |
| --- | --- |
| `host` | `windows`, `macos` or `linux` |
| `version` | `major.minor.patch`, optionally `-pre`; a prerelease sorts before its release |
| `tag` | The release tag |
| `published` | UTC date the release was published |
| `release_url` | The release page, where the files are |
| `package_sha256` | SHA-256 of the sealed key package that release matches; the package is installed with the ThoxKey provisioner and is not attached to the release |
| `assets` | Every file attached to the release, with its SHA-256 |

ThoxKey Start reads at most 64 KiB, refuses duplicate keys and non-finite numbers, and uses the newest
entry for its own computer type. It sends no account, key or computer details with the request and
downloads nothing.
