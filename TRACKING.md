# CSAA evaluation tracking

The project is tracked in [coderabbit-demo/mmani-csaa](https://github.com/coderabbit-demo/mmani-csaa).
This repository contains the supplied v2.5 framework and the October 21, 2026
CodeRabbit assessment. Formal platform evaluation remains unscored. The separate
demonstration implementation and local CLI rehearsals are recorded below.

## Assessment and sources

| Artifact | Purpose |
| --- | --- |
| [October 23 PI extension](reports/2026-10-23/README.md) | Adds a Potential PI prompt column to all assessed probe/gate/platform/gap rows, with suggested scopes and explicit limits. Includes dated report exports and a structured candidate library; original ratings and October 21 snapshots are preserved. |
| [CodeRabbit assessment](reports/2026-10-21/coderabbit-assessment.md) | Exact requirement wording, Met ratings, evidence, gaps and mitigation options. |
| [HTML snapshot](reports/2026-10-21/coderabbit-assessment.html) | Full report used to create the Google Doc. |
| [Assessment data](reports/2026-10-21/coderabbit-assessment.json) | Structured findings, requirements, source references and illustrative configuration. |
| [PDF snapshot](reports/2026-10-21/coderabbit-assessment.pdf) / [Word snapshot](reports/2026-10-21/coderabbit-assessment.docx) | Exports of the completed native Google Doc. |
| [Google Doc](https://docs.google.com/document/d/16LQrN9LyoMjFLw9HiDNF2RIe79rKmTlfPASfR-SK1VI/edit) | Editable Drive copy in the work account. Edits in Drive do not automatically synchronize to Git. |
| [Source package hashes](reports/2026-10-21/source-package-sha256.json) | SHA-256 values of all 33 supplied files, excluding Finder metadata. |
| [CSAA mutual success plan](reports/2026-10-21/csaa-mutual-success-plan.md) | Requirements-based draft with proposed activities, success indicators, deployment details and known DPT owners; unconfirmed dates and contacts are marked explicitly. |
| [MSP handoff and open confirmations](reports/2026-10-21/csaa-msp-handoff.md) | Links the committed deliverables and records the confirmations needed before execution or commercial commitments. |
| [Demonstration implementation status](reports/2026-10-21/demo-implementation-status.md) | Six published baselines, passing hosted CI, native showcase observations, configuration package, hosted/CLI repeatability and completed Jira/scope controls with explicit limits. Contains no execution code or locked answer keys. |
| [Current Bitbucket onboarding recording](reports/2026-10-22/bitbucket-onboarding/README.md) | 12:13 native-resolution v3 with masks removed, preserved typing speed, Bitbucket webhook secret demonstration, revised cuts, validation and portable chapter sources; redacted v2 retained. Demonstration setup only; formal evaluation remains unscored. |
| [Earlier CodeRabbit Readiness video package](reports/2026-10-21/coderabbit-readiness/README.md) | Preserved October 21 walkthrough, prior exports, timing validation and recorded production sources. Superseded by the October 22 retake. |
| [MSP PDF](reports/2026-10-21/csaa-mutual-success-plan.pdf) / [MSP Word snapshot](reports/2026-10-21/csaa-mutual-success-plan.docx) / [structured MSP content](reports/2026-10-21/csaa-mutual-success-plan.json) | Snapshots of the [editable Google Doc](https://docs.google.com/document/d/1GfYrExOJhHtyCAgCJsk0rJ20Up9Vg5aAShzPLqlUeQk/edit). The original template is retained under `reports/2026-10-21/source-templates/`. No successful PoV result or commercial commitment is asserted. |
| [Original package introduction](README.md) | Framework overview, folder purposes and operating sequence. |

The supplied framework files are unchanged. The report cites public CodeRabbit
documentation and the inspected `coderabbitai/mono` revision. Mono links require
the reader's existing repository access; its source code is not vendored here.

## Working policy

This is a tracking repository. There will be no code reviews here. Changes to
tracking artifacts can be committed directly; do not add a review workflow or
request review from a bot. `.coderabbit.yaml` disables automatic/incremental
reviews, removes label/description opt-ins, and excludes every path. `AGENTS.md`
records the same policy for future agents.

The YAML settings are repository configuration, not an uninstall of the GitHub
App. Preserve them and do not request manual bot reviews. Settings elsewhere in
the organization must remain consistent with this repository's no-review policy.
See [automatic review controls](https://docs.coderabbit.ai/configuration/auto-review)
and the [configuration reference](https://docs.coderabbit.ai/reference/configuration).

Use dated directories under `reports/` for future assessments, and preserve prior
snapshots. Use the existing `review-practice/`, `probe-pack/`, `configuration/` and
`evidence/` directories according to the runbook. Requirements, decisions and
follow-up work can be linked to GitHub issues as they are agreed; the initial
import does not create an issue for every report row.

## Rebuilding report snapshots

The scripts use Python 3's standard library:

```sh
python3 scripts/build_coderabbit_report.py
python3 scripts/export_report_markdown.py
```

The JSON file supplies assessment content; the HTML builder also reads the
original `runbook.md` for exact clauses and tables. Review changes to requirements
and line references before regenerating a later report. The Markdown script
converts that generated HTML to GitHub tables without changing its assessment.
The PDF and DOCX are dated exports and are not regenerated by these commands.
Export new snapshots after updating the Google Doc, and check them into Git with
the corresponding assessment version.

The report uses US Letter landscape pages, half-inch margins, and tables spanning
the full 10-inch content width. Requirement tables keep ID and Met in separate
columns. The October 21 layout revision preserves the assessment wording, ratings
and source links.
