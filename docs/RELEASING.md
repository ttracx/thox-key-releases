# Publishing a ThoxKey™ Start release here

Releases are cut in the private source repository (`ttracx/thox-key`) first, then published here.

1. Take `Start-ThoxKey.exe` and `SHA256SUMS.txt` from the source release. Recompute each SHA-256 and
   compare with the source release notes; stop on any difference.
2. Write `notes/<tag>.md`: what changed in plain words, the files and their SHA-256, the matching sealed
   package SHA-256, limits. No internal commit IDs, hostnames, serials, key ids or tokens.
3. Add the entry to `feed.json` (see [FEED.md](FEED.md)) and run `python3 scripts/check_feed.py` and
   `python3 -m unittest scripts/test_check_feed.py`.
4. Commit and push to `main`, then create the GitHub Release with the same tag, the notes as its body and
   the two files attached. The feed's `release_url` must open that release.
5. Check: download the attached files from the public release and compare their SHA-256 with the notes.

Never attach a key package, model files, credentials or anything not meant for the public.
