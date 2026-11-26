# ThoxKey™ release list

[![License](https://img.shields.io/badge/license-Apache--2.0-171719)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/ttracx/thox-key-releases?color=171719)](https://github.com/ttracx/thox-key-releases/commits/main)
[![List](https://img.shields.io/badge/list-thoxkey--update--feed%2F1-05A451)](feed.json)
![THOX](https://img.shields.io/badge/THOX-05A451)

The public list of ThoxKey Start releases: versions, dates, release links and SHA-256 checksums. This
repository holds the list, plus the release files of add-on packs that ThoxKey Setup installs. It has
no source code.

Your AI. Your Data. Your Rules.™

## The list

[`feed.json`](feed.json), at a stable address:

```
https://raw.githubusercontent.com/ttracx/thox-key-releases/main/feed.json
```

ThoxKey Start 0.4.2 and later reads this address when you press **Check for updates** in ThoxOS™
(Devices, Updates & recovery) and tells you whether a newer ThoxKey Start exists. Format:
[docs/FORMAT.md](docs/FORMAT.md).

## Downloads

Each entry links to its release page in the ThoxKey repository, where the files are. Opening a release
page needs access to that repository. Check every downloaded file against the SHA-256 values in this
list. Steps: [docs/USER_GUIDE.md](docs/USER_GUIDE.md).

| Computer | Newest listed |
| --- | --- |
| Windows | 0.4.2 |
| macOS | none |
| Linux | none |

## The signed release feed

[`release-feed.json`](release-feed.json) lists what is current for a ThoxKey: the THOX models,
ThoxKey Setup (1.1.1 for Windows, 1.1.2 for macOS), and the ThoxKey Portal pack. ThoxKey Start and ThoxOS images follow as they
are published. Each entry
gives an address, an exact size and a SHA-256. [`release-feed.json.sig`](release-feed.json.sig)
is an Ed25519 signature over the exact bytes of the feed.

```
https://raw.githubusercontent.com/ttracx/thox-key-releases/main/release-feed.json
```

ThoxKey Setup 1.1 and later reads this address. It checks the signature against a key compiled
into the app before it reads anything in the feed, refuses a feed older than one it has already
accepted, and checks every download against the size and SHA-256 listed here. It sends no
account, key or computer details. Format: [docs/RELEASE-FEED.md](docs/RELEASE-FEED.md).

ThoxKey Portal's files are the assets of its release here (for example
[thoxkey-portal-0.1.2](https://github.com/ttracx/thox-key-releases/releases/tag/thoxkey-portal-0.1.2)).
ThoxKey Setup downloads and checks them; you do not need to download them by hand.

The two files are published together and must not be edited by hand: any change to the feed,
even to its spacing, makes the signature fail.

## License and notice

Apache License 2.0, see [LICENSE](LICENSE). [NOTICE.md](NOTICE.md) carries the THOX.ai LLC notice.
