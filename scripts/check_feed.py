"""check_feed.py: validate feed.json before it is pushed. Local check; this repository runs no hosted CI.

The rules match ThoxKey Start's parser (ttracx/thox-key starter/linux/thoxkey_device_api.py
parse_feed): schema thoxkey-update-feed/1, every entry with a known host, a major.minor.patch[-pre]
version and an https release_url on github.com; optional fields well formed; no duplicate JSON keys;
at most 64 KiB, the size ThoxKey Start reads. It also checks each entry's release_url and notes_url
point at this repository, and that versions are unique per host.

Usage: python3 scripts/check_feed.py [feed.json]   (exit 0 when valid)
"""
import json
import re
import sys
from pathlib import Path

REPO = "https://github.com/ttracx/thox-key-releases/"
HOSTS = {"windows", "macos", "linux"}
VERSION = re.compile(r"(0|[1-9][0-9]{0,5})\.(0|[1-9][0-9]{0,5})\.(0|[1-9][0-9]{0,5})(?:-([0-9A-Za-z.-]{1,40}))?")
SHA256 = re.compile(r"[0-9a-f]{64}")
TAG = re.compile(r"[A-Za-z0-9._/-]{1,80}")
DATE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}([T ][0-9:.]+Z?)?")
ASSET = re.compile(r"[A-Za-z0-9._ -]{1,120}")
LIMIT = 64 * 1024


def no_duplicates(pairs):
    keys = [k for k, _ in pairs]
    if len(keys) != len(set(keys)):
        raise ValueError("duplicate JSON key")
    return dict(pairs)


def check(raw: bytes) -> list[str]:
    problems = []
    if len(raw) > LIMIT:
        problems.append(f"feed is {len(raw)} bytes; ThoxKey Start reads at most {LIMIT}")
    try:
        feed = json.loads(raw, object_pairs_hook=no_duplicates,
                          parse_constant=lambda c: (_ for _ in ()).throw(ValueError("non-finite number " + c)))
    except ValueError as exc:
        return problems + [f"not valid strict JSON: {exc}"]
    if not isinstance(feed, dict) or feed.get("schema") != "thoxkey-update-feed/1":
        return problems + ["schema must be thoxkey-update-feed/1"]
    releases = feed.get("releases")
    if not isinstance(releases, list) or len(releases) > 200:
        return problems + ["releases must be a list of at most 200 entries"]
    seen = set()
    for i, entry in enumerate(releases):
        where = f"releases[{i}]"
        if not isinstance(entry, dict):
            problems.append(f"{where} is not an object")
            continue
        host, version = entry.get("host"), entry.get("version")
        if host not in HOSTS:
            problems.append(f"{where}.host must be one of {sorted(HOSTS)}")
        if not isinstance(version, str) or not VERSION.fullmatch(version):
            problems.append(f"{where}.version must be major.minor.patch[-pre]")
        if (host, version) in seen:
            problems.append(f"{where} repeats {host} {version}")
        seen.add((host, version))
        for key in ("release_url", "notes_url"):
            url = entry.get(key)
            if url is None and key == "notes_url":
                continue
            if not isinstance(url, str) or not url.startswith(REPO) or len(url) > 512:
                problems.append(f"{where}.{key} must be an https URL under {REPO}")
        if "tag" in entry and not (isinstance(entry["tag"], str) and TAG.fullmatch(entry["tag"])):
            problems.append(f"{where}.tag is malformed")
        if "published" in entry and not (isinstance(entry["published"], str) and DATE.fullmatch(entry["published"])):
            problems.append(f"{where}.published must be YYYY-MM-DD")
        if "package_sha256" in entry and not (isinstance(entry["package_sha256"], str) and SHA256.fullmatch(entry["package_sha256"])):
            problems.append(f"{where}.package_sha256 must be 64 lowercase hex")
        for j, asset in enumerate(entry.get("assets") or []):
            if not (isinstance(asset, dict) and isinstance(asset.get("name"), str) and ASSET.fullmatch(asset["name"])
                    and isinstance(asset.get("sha256"), str) and SHA256.fullmatch(asset["sha256"])):
                problems.append(f"{where}.assets[{j}] needs a plain file name and a 64-hex sha256")
    return problems


def main(argv: list[str]) -> int:
    path = Path(argv[1] if len(argv) > 1 else Path(__file__).resolve().parent.parent / "feed.json")
    problems = check(path.read_bytes())
    for problem in problems:
        print("FAIL", problem)
    if not problems:
        print("OK", path.name)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
