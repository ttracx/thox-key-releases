# ThoxKey™ releases

[![License](https://img.shields.io/badge/license-Apache--2.0-171719)](LICENSE)
[![Release](https://img.shields.io/github/v/release/ttracx/thox-key-releases?color=05A451)](https://github.com/ttracx/thox-key-releases/releases/latest)
[![Last commit](https://img.shields.io/github/last-commit/ttracx/thox-key-releases?color=171719)](https://github.com/ttracx/thox-key-releases/commits/main)
![THOX](https://img.shields.io/badge/THOX-05A451)
![Checks](https://img.shields.io/badge/checks-local%20feed%20check-171719)

Public downloads of **ThoxKey Start**, the program that runs a ThoxKey on your computer, and the
update feed that ThoxKey Start and ThoxOS™ read to tell you a newer version exists.

Your AI. Your Data. Your Rules.™

## Get the latest

1. Open the [latest release](https://github.com/ttracx/thox-key-releases/releases/latest).
2. Download the files for your computer and `SHA256SUMS.txt`.
3. Check each file: on Windows, `Get-FileHash .\Start-ThoxKey.exe -Algorithm SHA256`; on macOS or
   Linux, `shasum -a 256 <file>`. The value must match `SHA256SUMS.txt` and the release notes.
4. Update the key with its sealed package and the ThoxKey provisioner. A ThoxKey Start copied onto a key
   by hand fails the key's package check and does not start.

Full steps: [docs/USER_GUIDE.md](docs/USER_GUIDE.md). Release notes: [notes/](notes/).

## What is here

| Path | What |
| --- | --- |
| [Releases](https://github.com/ttracx/thox-key-releases/releases) | `Start-ThoxKey.exe` and `SHA256SUMS.txt` per version |
| [`feed.json`](feed.json) | `thoxkey-update-feed/1`: newest version per computer type, release link, SHA-256 values |
| [`notes/`](notes/) | Release notes per tag |
| [`docs/FEED.md`](docs/FEED.md) | Feed format and how ThoxKey Start reads it |
| [`docs/RELEASING.md`](docs/RELEASING.md) | How THOX publishes a release here |
| [`scripts/check_feed.py`](scripts/check_feed.py) | Local feed check (no hosted CI) |

This repository holds release files, notes and the feed only. ThoxKey Start's source code is not
published here.

## Status

| Computer | Latest | Notes |
| --- | --- | --- |
| Windows | 0.4.1 | Internal engineering build, unsigned |
| macOS | not released | |
| Linux | not released | |

ThoxKey Start 0.4.2 and later checks this feed when you press **Check for updates** in ThoxOS (Devices,
Updates & recovery). Earlier versions do not check; use the links above.

## License and notice

Apache License 2.0, see [LICENSE](LICENSE). [NOTICE.md](NOTICE.md) carries the THOX.ai LLC notice.
Agent pickup: [.agents/HANDOFF.md](.agents/HANDOFF.md).
