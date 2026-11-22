# Signed release feed (`thoxkey-release-feed/1`)

One JSON object in `release-feed.json`, and a signature in `release-feed.json.sig`.

```json
{"schema":"thoxkey-release-feed/1","channel":"stable","sequence":1,"published":"2026-11-22",
 "items":[
  {"kind":"model","id":"thoxmini-3b","version":"1.0.0","title":"ThoxMini 3B","host":"any",
   "url":"https://huggingface.co/Thox-ai/ThoxMini-3B/resolve/<commit>/thoxmini-3b-Q4_K_M.gguf",
   "bytes":2019373952,"sha256":"<64 hex>","notes":"The default assistant on every ThoxKey."}]}
```

| Field | Meaning |
| --- | --- |
| `sequence` | Goes up with every published feed. An app refuses a feed with a lower number than one it has accepted |
| `kind` | `setup`, `start`, `image`, `model` or `package` |
| `id` | Lower-case letters, digits, `.`, `_`, `-` |
| `version` | `major.minor.patch`, optionally `-pre` and `+build`; a prerelease sorts before its release |
| `host` | `any`, `windows`, `macos` or `linux` |
| `url` | `https://` on `huggingface.co`, `github.com`, `raw.githubusercontent.com` or `registry.ollama.ai` |
| `bytes`, `sha256` | The exact size and SHA-256 of the file |
| `files` | For a package, its files; for an image, its parts in order: `path`, `url`, `bytes`, `sha256` |

## The signature

```json
{"alg":"ed25519","keyId":"thox-release-2026-11","signature":"<base64>"}
```

The signature covers the exact bytes of `release-feed.json`. The public key is compiled into
ThoxKey Setup:

| Key id | Public key (base64) |
| --- | --- |
| `thox-release-2026-11` | `vKkaFljVSPmbIyJ5RhLoZpZdvbVVADQlUAZDKslH/VY=` |

## Check a download yourself

```sh
curl -fsSL https://raw.githubusercontent.com/ttracx/thox-key-releases/main/release-feed.json -o release-feed.json
shasum -a 256 thoxmini-3b-Q4_K_M.gguf
```

The second line must print the `sha256` the feed lists for that file.
