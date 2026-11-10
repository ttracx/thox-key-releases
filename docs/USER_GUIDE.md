# Updating a ThoxKey™

## Which ThoxKey Start does my key run?

Open ThoxOS from the key and go to **Devices, Updates & recovery**. The **ThoxKey software** panel shows
the version.

- **0.4.2 or later:** press **Check for updates**. ThoxKey Start compares itself with this list and says
  whether a newer version exists. Nothing is downloaded or installed.
- **0.4.1 or older:** the key cannot check by itself. Compare its version with the newest entry in
  [`feed.json`](../feed.json) and update by hand once, as below. After that, the key can check.

## Update a key by hand

1. Open the release page named in the list. It needs access to the ThoxKey repository.
2. Download the files for your computer and check each one's SHA-256 against this list. Stop if any
   value differs.
3. Install the matching sealed key package with the ThoxKey provisioner. Its SHA-256 is the entry's
   `package_sha256`.
4. Plug the key back in, press **Inspect key**, then **Approve and start**.

A ThoxKey Start copied onto a key by hand does not update it: the key checks every file against its
sealed package, and a changed starter fails that check.
