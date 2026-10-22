# CodeRabbit Readiness — Bitbucket Cloud and CLI

The current customer walkthrough is [revision 2 (8:42)](deliverables/CodeRabbit-Readiness-Bitbucket-Cloud-v2.mp4). It is one silent H.264 video, with visible pointer activity, clicks and typed input. Action descriptions and transition text are permanently burned into the picture.

The complete native 3440 × 1440 browser capture remains at 1:1 pixel size. A 200-pixel action strip is appended below it, producing a 3440 × 1640 video at 30 fps. There is no crop, zoom or inset.

## Current edit

- The opening is exactly 7 seconds.
- Browser footage plays at 85% speed, slowing its pointer activity and typing together by 15%.
- Fourteen 4-second transition cards describe the next step and its purpose.
- The CLI section ends after the complete `cr auth login --help` output remains visible for exactly 4 seconds. Later authentication-status and organization commands are excluded from this version.
- The closing customer-readiness checklist is retained.

| Artifact | Purpose |
| --- | --- |
| [Current video](deliverables/CodeRabbit-Readiness-Bitbucket-Cloud-v2.mp4) | Revision 2 customer walkthrough. |
| [Poster](deliverables/CodeRabbit-Readiness-v2-Poster.png) | Opening image. |
| [Chapters](deliverables/v2-Chapters.txt) / [edit timeline](deliverables/v2-Timeline.json) | Navigation and frame-count timing. |
| [Validation](deliverables/v2-Video-validation.json) | Video hash, dimensions, track inventory, exact timing checks and successful full-file decode. |
| [Production notes](deliverables/v2-Production-notes.txt) | Demonstration coverage, limitations and source links. |
| [Earlier full-screen version](deliverables/CodeRabbit-Readiness-Bitbucket-Cloud-Fullscreen.mp4) | Preserved 7:29 version before timing and transition edits. |
| [Initial version](deliverables/CodeRabbit-Readiness-Bitbucket-Cloud.mp4) | Preserved 7:29 edit with close-ups and an inset; superseded. |
| [Package hashes](SHA256SUMS) | Integrity manifest for the published package. |

## Demonstration boundary

This is a walkthrough of an existing configured demo tenant. New cloud account creation, OAuth consent, token issuance, Forge secret exchange and final installation saves are explained rather than repeated. No cloud connections, scopes, webhook settings or review configurations were changed. The manual PR-review request was typed and cancelled without posting.

The CLI installer actually ran in an isolated directory outside this tracking repository and reported checksum and installation verification for version 0.9.1. The terminal section renders the real timed PTY capture and is labelled accordingly. CLI login is not completed in the video, and matching Bitbucket identity, organization and entitlement remain customer verification steps.

These are setup and demonstration artifacts. They do not establish independently scored framework results, a successful formal PoV or a pilot-readiness decision. No review was run against this tracking repository, and no review automation is added.

## Production sources

`production/raw/browser-window.mp4` is the native ScreenCaptureKit source with cursor and click indications and no audio. `production/raw/terminal.cast` is the real timed terminal source; the account email is redacted. JSONL event logs preserve the action-label timing. The Swift recorder and Python capture/render scripts are included as production materials.

The exported versions, posters, notes and validation files are preserved in `deliverables/`. Temporary captures, generated frames, caches, downloaded dependencies and installed CLI binaries are excluded.

To rebuild the exports on macOS, use Python 3 with `production/requirements.txt`, FFmpeg/ffprobe on PATH, and the macOS Arial/Menlo fonts referenced by the scripts. Run these rendering commands from `production/` in this order:

```sh
python3 build_video.py all
python3 build_fullscreen.py all
python3 build_iteration2.py assets
python3 build_iteration2.py browser
python3 build_iteration2.py terminal
python3 build_iteration2.py join
```

These render existing recordings; they do not run CodeRabbit or access cloud services. Generated build directories are ignored. Encoding can vary with FFmpeg, font and dependency versions, so a rebuilt video may have a different hash. Re-running capture scripts is a separate recording operation and is not needed to reproduce these edits.

The published source paths are relative to this package. Original production notes retain some historical local paths as provenance; they are not required to view the video.
