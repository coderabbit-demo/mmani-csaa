# Bitbucket Cloud onboarding recording — October 22, 2026

The current customer video is [CodeRabbit Readiness v2](deliverables/CodeRabbit-Readiness-Bitbucket-Cloud-2026-10-22-v2.mp4): **12:13.1, 3024 × 1964, 30 fps, silent**. It shows the laptop's main-screen browser with visible cursor movements, clicks, and typed input. Small action captions are permanently burned into the video.

This retake supersedes the [October 21 walkthrough](../../2026-10-21/coderabbit-readiness/README.md), which is preserved as a historical package.

## Coverage

The video follows the CodeRabbit Bitbucket Cloud documentation through service-account guidance, API-token scopes, workspace connection, and installation on `coderabbit-test-repo` in the `coderabbit-demo` project. It demonstrates Account fields and the repository webhook, Jira OAuth authorization, a repository scope, root `.coderabbit.yaml` configuration, mock PR creation, a completed review, Change Stack, pre-merge checks, and an actual `@coderabbitai help` exchange. The terminal section shows the recorded CLI installation, version check, and `cr auth login --help` output.

Account credentials are dummy demonstrations without Save. The added Bitbucket webhook shot visibly types `DEMO_WEBHOOK_SECRET_NOT_VALID`, then the dummy entry is discarded off camera without saving. The existing webhook secret remains configured. Jira OAuth and the demo repository installation were completed in the separate demo environment; CLI authentication is not completed in the video.

These are onboarding demonstration artifacts. Formal CSAA evaluation remains unscored. No review was run against this tracking repository, and its disabled-review configuration is preserved.

## Latest revision

- Non-typing footage plays at 1.2× speed; protected typing intervals retain their existing speed. This also accelerates cards and holds from the prior cut.
- The browser debugging banner and Chrome profile image/name are masked. Unrelated repository names are redacted while the demo repository remains visible in static lists.
- The unsuccessful Repository actions attempt is removed; the working repository navigation menu is retained.
- The webhook section includes typing the dummy value in Bitbucket's Secret field. The following section begins with selecting Connections in CodeRabbit.
- The Bitbucket reconnection detour is removed. The PR's Change Stack link leads directly to the successful loading sequence, with a corrected caption.

## Package and validation

| Artifact | Purpose |
| --- | --- |
| [Final video](deliverables/CodeRabbit-Readiness-Bitbucket-Cloud-2026-10-22-v2.mp4) | Current customer deliverable. |
| [Poster](deliverables/preview-v2.png) | Opening image. |
| [Timeline](deliverables/timeline-v2.json) | Chapter order, durations, and source-cut notes. |
| [Validation](deliverables/validation-v2.json) / [media metadata](deliverables/media-info-v2.json) | Successful full decode, stream inventory, resolution, and visual checks. |
| [Visual check sheet](deliverables/qa-contact.jpg) | Representative rendered frames. |
| [Edit plan](production/edit-plan.json) / [typing intervals](production/typing-intervals.json) | Retiming and cut provenance from the preceding local export. |
| [Redacted chapter clips](production/chapters) / [assembly script](production/assemble.py) | Portable sources for recreating the published edit. |
| [SHA-256 manifest](SHA256SUMS) | Integrity hashes for the package. |

The exported video decoded end to end without errors. OCR checked 1,736 frames: two frames per second across the complete video, plus fifteen frames per second through scope scrolling. No matches remained for the known unrelated repository names, debugging-banner text, or Chrome profile label. Representative frames and the changed transitions were also inspected visually. OCR sampling is a validation aid rather than a guarantee about every frame.

Published chapter clips already contain the redactions, captions, and timing adjustments. Unredacted recordings, the superseded local export, OCR text containing the hidden names, generated masks, and caches remain outside this package. The edit plan's `local-original-chapters/` paths identify unpublished inputs and are not required for assembly.

Reassemble with Python 3 and FFmpeg on PATH:

```sh
python3 reports/2026-10-22/bitbucket-onboarding/production/assemble.py
```

The script writes `production/build/readiness-v2.mp4`, copying the video stream without re-encoding. It performs no browser actions, cloud mutations, or CodeRabbit review. Verify the published package from this directory with `shasum -a 256 -c SHA256SUMS`.
