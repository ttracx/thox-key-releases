"""Tests for check_feed.py: python3 -m unittest scripts/test_check_feed.py"""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import check_feed  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
GOOD = {"host": "windows", "version": "0.4.1", "tag": "start-windows-v0.4.1", "published": "2026-11-10",
        "release_url": "https://github.com/ttracx/thox-key-releases/releases/tag/start-windows-v0.4.1",
        "assets": [{"name": "Start-ThoxKey.exe", "sha256": "a" * 64}]}


def feed(*entries):
    return json.dumps({"schema": "thoxkey-update-feed/1", "releases": list(entries)}).encode()


class CheckFeedTests(unittest.TestCase):
    def test_published_feed_is_valid(self):
        self.assertEqual(check_feed.check((ROOT / "feed.json").read_bytes()), [])

    def test_good_entry(self):
        self.assertEqual(check_feed.check(feed(GOOD)), [])

    def test_refusals(self):
        cases = [
            feed({**GOOD, "host": "amiga"}),
            feed({**GOOD, "version": "1.0"}),
            feed({**GOOD, "release_url": "https://github.com/ttracx/thox-key/releases"}),
            feed({**GOOD, "release_url": "http://github.com/ttracx/thox-key-releases/x"}),
            feed({**GOOD, "assets": [{"name": "../x", "sha256": "a" * 64}]}),
            feed({**GOOD, "package_sha256": "XYZ"}),
            feed(GOOD, GOOD),
            b'{"schema":"thoxkey-update-feed/1","releases":[],"releases":[]}',
            b'{"schema":"thoxkey-update-feed/1","releases":[NaN]}',
            b'{"schema":"other","releases":[]}',
            feed(GOOD) + b" " * (64 * 1024),
        ]
        for raw in cases:
            self.assertNotEqual(check_feed.check(raw), [], raw[:80])


if __name__ == "__main__":
    unittest.main()
