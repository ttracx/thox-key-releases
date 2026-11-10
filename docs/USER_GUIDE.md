# Updating a ThoxKey™

## Do I need an update?

- **ThoxKey Start 0.4.2 or later:** open ThoxOS from your key, go to **Devices, Updates & recovery** and
  press **Check for updates**. ThoxKey Start compares itself with [`feed.json`](../feed.json) and tells
  you whether a newer version exists. It sends no account, key or computer details, and downloads nothing.
- **Earlier versions:** the same page shows your version. Compare it with the
  [latest release](https://github.com/ttracx/thox-key-releases/releases/latest).

## Update

1. Download the release files for your computer and `SHA256SUMS.txt`.
2. Check every file's SHA-256 against `SHA256SUMS.txt` and the release notes. Stop if any differs.
3. Install the matching sealed key package with the ThoxKey provisioner. The release notes name the
   package's SHA-256.
4. Plug the key in, press **Inspect key**, then **Approve and start**.

Copying `Start-ThoxKey.exe` onto a key by hand does not update it: the key checks every file against its
sealed package, and a changed starter fails that check.

## Windows warning

Builds marked "unsigned" are internal engineering builds. Windows SmartScreen may warn before the first
run. Run one only after its SHA-256 matches.
