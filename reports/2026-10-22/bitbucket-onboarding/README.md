# Bitbucket Cloud onboarding recording — October 22, 2026

The current customer video is [CodeRabbit Readiness v3](deliverables/CodeRabbit-Readiness-Bitbucket-Cloud-2026-10-22-v3.mp4): **12:13.1, 3024 × 1964, 30 fps, silent**. It shows the laptop's main-screen browser with visible cursor movements, clicks, and typed input. Small action captions are permanently burned into the video.

This retake supersedes the [October 21 walkthrough](../../2026-10-21/coderabbit-readiness/README.md), which is preserved as a historical package.

## Coverage

The video follows the CodeRabbit Bitbucket Cloud documentation through service-account guidance, API-token scopes, workspace connection, and installation on `coderabbit-test-repo` in the `coderabbit-demo` project. It demonstrates Account fields and the repository webhook, Jira OAuth authorization, a repository scope, root `.coderabbit.yaml` configuration, mock PR creation, a completed review, Change Stack, pre-merge checks, and an actual `@coderabbitai help` exchange. The terminal section shows the recorded CLI installation, version check, and `cr auth login --help` output.

Account credentials are dummy demonstrations without Save. The added Bitbucket webhook shot visibly types `DEMO_WEBHOOK_SECRET_NOT_VALID`, then the dummy entry is discarded off camera without saving. The existing webhook secret remains configured. Jira OAuth and the demo repository installation were completed in the separate demo environment; CLI authentication is not completed in the video.

These are onboarding demonstration artifacts. Formal CSAA evaluation remains unscored. No review was run against this tracking repository, and its disabled-review configuration is preserved.

## Latest revision

Version 3 removes the browser debugging-banner mask, Chrome profile mask, and repository-name masks after feedback on their appearance. All 45 chapter durations and frame counts match v2. The 24 title, transition, and CLI clips are byte-identical to v2. All other edits remain as described below.

- Non-typing footage plays at 1.2× speed; protected typing intervals retain their existing speed. This also accelerates cards and holds from the prior cut.
- The original browser debugging banner, Chrome profile, and repository names are visible again in v3. The redacted v2 remains available.
- The unsuccessful Repository actions attempt is removed; the working repository navigation menu is retained.
- The webhook section includes typing the dummy value in Bitbucket's Secret field. The following section begins with selecting Connections in CodeRabbit.
- The Bitbucket reconnection detour is removed. The PR's Change Stack link leads directly to the successful loading sequence, with a corrected caption.

## Package and validation

| Artifact | Purpose |
| --- | --- |
| [Final video v3](deliverables/CodeRabbit-Readiness-Bitbucket-Cloud-2026-10-22-v3.mp4) | Current customer deliverable without the v2 masks. |
| [Redacted video v2](deliverables/CodeRabbit-Readiness-Bitbucket-Cloud-2026-10-22-v2.mp4) | Preserved previous version. |
| [Poster](deliverables/preview-v2.png) | Opening image. |
| [Current timeline](deliverables/timeline-v3.json) / [v2 timeline](deliverables/timeline-v2.json) | Chapter order, durations, and source-cut notes. |
| [v3 validation](deliverables/validation-v3.json) / [v3 media metadata](deliverables/media-info-v3.json) | Successful full decode, stream inventory, resolution, and visual checks. |
| [v3 visual check sheet](deliverables/qa-contact-v3.jpg) | Representative rendered frames. |
| [Edit plan](production/edit-plan.json) / [typing intervals](production/typing-intervals.json) | Retiming and cut provenance from the preceding local export. |
| [v3 browser clips](production/chapters-v3) / [v2 and shared clips](production/chapters) / [assembly script](production/assemble.py) | Portable sources for recreating either published edit. |
| [Preservation check](deliverables/preservation-check-v3.json) / [revision notes](deliverables/revision-notes-v3.json) | Sampled pixel comparison outside the removed overlays and the scope of the v3 change. |
| [SHA-256 manifest](SHA256SUMS) | Integrity hashes for the package. |

Both exported versions decoded end to end without errors. All v3 chapter durations and frame counts match v2, and the intro, transitions, and CLI clips are identical. Sampled pixel comparisons outside the removed overlays showed only minor encoding differences. For the historical redacted v2, OCR checked 1,736 frames: two frames per second across the complete video, plus fifteen frames per second through scope scrolling. No matches remained for the known unrelated repository names, debugging-banner text, or Chrome profile label. Representative frames and the changed transitions were also inspected visually. OCR sampling is a validation aid rather than a guarantee about every frame.

Published chapter clips already contain their final captions and timing adjustments. The v2 browser clips retain masks; the v3 browser clips omit them. Raw capture sessions, the superseded local first export, OCR text, generated masks, and caches remain outside this package. The edit plan's `local-original-chapters/` paths identify unpublished inputs and are not required for assembly.

Reassemble with Python 3 and FFmpeg on PATH:

```sh
python3 reports/2026-10-22/bitbucket-onboarding/production/assemble.py
```

The script defaults to v3 and writes `production/build/readiness-v3.mp4`; pass `--version v2` to recreate the preserved redacted edit. It assembles the selected version, copying the video stream without re-encoding. It performs no browser actions, cloud mutations, or CodeRabbit review. Verify the published package from this directory with `shasum -a 256 -c SHA256SUMS`.
