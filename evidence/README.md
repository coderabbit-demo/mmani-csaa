# Evidence

**What this is:** what the tool actually produced, and how it scored. The results
side of the comparison.

The tool runs on code in a separate sanitized evaluation repository
(`../runbook.md` §5.5). The results are documented **here**, alongside the probes
and their locked answer keys. The two are kept apart so the tool never sees the
probes or the keys — not so the results live elsewhere.

## How the comparison works

Three artifacts, one per stage:

| Stage | Artifact | Lives in |
|---|---|---|
| What should be found | *Expected finding (answer key)*, locked before the run | `../probe-pack/<category>/<probe-id>.md` |
| What the tool found | The tool's actual comment, with a link or export | `evidence/<platform>/` |
| How well it did | Score 0-3 against the key, plus actionability and harm | `evidence/<platform>/` |

The probe ID is the join. An evidence record carries the probe's ID, so the
expectation and the result can always be read side by side.

## What goes here

```
evidence/
  tps/
  payment-central/
  informatica-etl/
```

One folder per platform, named exactly as above. Inside each: the scored probe
results, the gate results for G1-G8, the frozen configuration manifests
(`../runbook.md` §3.1b), and the proof behind each score — screenshots, exports,
links to the tool's comment.

Results are read **per platform** and never averaged across platforms or combined
into a single number (`../runbook.md` §7.1, §18.2).

## Order of work

1. Prepare and sanitize the evaluation repository (§5.5).
2. Connect the tool and freeze the native-capability manifest (§3.1b).
3. Run the gates G1-G8 and record them (§6). A failed mandatory gate stops the
   evaluation or escalates for exception review — do not score probes against a
   tool that has not cleared the gates.
4. Run the native probes and score each against its locked key (§7.1).
5. Run the configured round R1-R6 under the configured manifest, reported
   separately from all native results (§8.7).
6. Roll up to the per-platform results table (§18.1).

## Rules worth knowing before you file anything

- A score needs proof. A score with no link, screenshot or export is not evidence.
- The answer key is never edited after the tool has produced output. A flawed probe
  is marked flawed and excluded, not rewritten (§7.5).
- Load-bearing numbers are measured by the evaluation team. Vendor dashboards are
  supporting evidence only, and any use of them must be stated (§14.1, §14.3).
- Native and configured-rule results stay separate and are never presented as one
  rating (§3.1b, §8.7).
- Nobody scores a probe they wrote (`../probe-pack/README.md` §3, rule 5).
- A probe that was not run is recorded as `NA` with a reason, or as *not tested* —
  never omitted. An omission reads as a pass.

## Where the rules are

| Topic | Runbook |
|---|---|
| Scoring rubric 0-3, roll-up to Green/Yellow/Red | §7.1 |
| Gates G1-G8 | §6 |
| Evidence collection rules | §14 |
| Evidence record field list | Appendix B |
| Per-platform results table | §18.1 |
| Decision outcomes | §19 |
