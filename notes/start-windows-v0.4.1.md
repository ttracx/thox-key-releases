# ThoxKey™ Start 0.4.1 for Windows

Internal engineering build: unsigned. Windows may show a SmartScreen warning before it runs.

## What changed

- **Browser models on the key.** In ThoxOS™, THOXY™ Edge 230M and the other browser models the key
  carries could not load their engine and showed "no available backend found". ThoxKey Start now lets
  ThoxOS load that engine from the key. Network access stays on this computer.
- **Automatic answers with the key's model.** In ThoxOS, **Automatic** now answers with the model
  chosen in ThoxKey Start, through ThoxBeam™, and reads "Automatic · ThoxKey Start model". A browser
  model answers only when you pick it in **Route**.

## Files

| File | SHA-256 |
| --- | --- |
| `Start-ThoxKey.exe` | `e1c95c40df0af7542d347b889846989e7010fb48d16456164c3980154b1e3ce6` |
| Matching sealed key package (installed with the ThoxKey provisioner, not attached here) | `f9b3e0c57625e3d7d49e5a467ceb809c826eba18dff340a89b1a228f69abde97` |

## Limits

- ThoxNova 12B runs on the CPU with the key's current Windows engine.
- macOS is not built for this release.
- While a browser model loads, a message sent before it is ready is refused instead of queued.
- A ThoxKey Start copied onto a key by hand fails the key's package check. Update a key with the
  sealed package and the ThoxKey provisioner.
