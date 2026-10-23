# Path-instruction candidates — October 23, 2026

The [editable assessment](https://docs.google.com/document/d/16LQrN9LyoMjFLw9HiDNF2RIe79rKmTlfPASfR-SK1VI/edit)
now has a **Potential PI prompt (proposed)** column in its probe, gate, platform
and framework-gap tables. The October 21 assessment and all Met ratings are
preserved; this extension proposes configuration options and does not re-score
the evaluation or convert demonstration observations into formal probe results.

- [Updated assessment](coderabbit-assessment.md), [HTML](coderabbit-assessment.html)
  and [structured assessment](coderabbit-assessment.json).
- [Native Google Doc PDF export](coderabbit-assessment.pdf) and
  [Word export](coderabbit-assessment.docx).
- [Candidate library](path-instruction-candidates.json): 78 entries, including 63
  candidate prompts and 15 explicit explanations of gaps a PI cannot close.
- [Verification](validation.json): original table cells and ratings preserved,
  all 33 supplied-package hashes unchanged, and ten six-column tables on
  landscape Letter pages with a total width of 10 inches.

For P8, the prompt normally suppresses findings on proven non-semantic changes,
assigns low priority to a useful optional formatting suggestion, and still calls
out a demonstrated semantic regression hidden by a rename or reformat.

## Use in an approved configured round

Select and consolidate the relevant candidate text into
`reviews.path_instructions` in an approved evaluation repository. Suggested globs
are illustrative and must be replaced with the actual matching paths. Supply
accessible, versioned standards where a candidate refers to an approved profile,
state machine, specification or exception. Do not install every overlapping
candidate wholesale or expose locked keys, seeded-defect locations or expected
probe answers to the reviewer.

Freeze selected instructions in a declared configured/remediation manifest and
re-run the same locked assets with positive cases and clean controls. Preserve
native results and report additional configuration effort separately. A prompt
can guide review behavior; it cannot grant access, enforce permissions, guarantee
determinism, change a public export schema, or supply missing evaluator evidence.
See [CodeRabbit path-instruction documentation](https://docs.coderabbit.ai/configuration/path-instructions),
checked October 23, 2026. The prior assessment's pinned mono references remain
the implementation basis; this extension does not claim a newer source audit.

The tracking repository's `.coderabbit.yaml` remains unchanged with reviews
disabled. None of these candidates has been applied here or to a live evaluation
configuration. No formal gates or probes were executed for this extension.

## Rebuild text snapshots

From the repository root:

```sh
python3 scripts/build_coderabbit_report.py --report-dir reports/2026-10-23
python3 scripts/export_report_markdown.py --report-dir reports/2026-10-23
```

These commands use the dated structured assessment and original runbook. PDF and
Word snapshots are exports of the edited native Google Doc. Later Drive edits
require new exports and a dated check-in; they do not synchronize automatically.
