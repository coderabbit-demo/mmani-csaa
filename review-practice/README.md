# Review practice (Phase 0)

**What this is:** the record of what the evaluation covers and how code review works
on a platform today, written before the tool is enabled.

The probes prove what the tool found. This folder is what proves **the test was
fair** — which repositories were used and why, what the tool was allowed to see,
what was left out, and what nobody got around to testing. Those are the questions a
reader asks when a result is disputed, and this is where they are answered.

**What this is not:** the expected answer for a probe. That is the **answer key**,
and it lives inside the probe file in `../probe-pack/` under
*Expected finding (answer key)*, reviewed and locked before the tool runs
(`../runbook.md` §7.5). If you are looking for "the known bug this probe should
catch", it is there, not here.

> **On the folder name.** The runbook calls part of this folder's contents the
> *baseline* — a review-practice baseline, which is the right word for it. But
> "baseline" is also used informally for the probe pack, because the probe pack
> holds the expected findings the tool is measured against. The folder is named
> `review-practice/` so the two cannot be confused: **this folder describes the
> team and the test setup; `../probe-pack/` is the bar the tool is measured
> against.**

## What goes here

```
review-practice/
  tps/
  payment-central/
  informatica-etl/
```

One folder per platform, named exactly as above. Inside each:

| File | Contents | Runbook |
|---|---|---|
| `phase0-record.md` | Scope, setup, and the review-practice figures | §5.7, §5.2, App. A |
| `review-catch-profile.md` | What reviewers actually catch, from the PR comment history, plus the candidate probes it yields | §5.3 |
| `defect-inventory.md` | Historical defect/rework inventory | §5.4 |
| `assignments.md` | Probe ownership and readiness tracking | §5.7 |
| `raw/` | The exports the numbers came from | §5.2 |

## What matters most here, in order

1. **Scope and setup.** Which repositories, why those, what each contributes, what
   context the tool is given, what was excluded, and which probe families have no
   home in the current scope. A result drawn from four repositories is a statement
   about those four, not about the platform — and a probe family with nowhere to run
   is reported as *not tested*, never left to read as acceptable.
2. **The defect inventory and the review-catch profile.** These are raw material,
   not statistics: P1 probes and reviewer-catch probes are built from them.
3. **The review-practice figures.** Context for reading the results. They are not
   scored, and no calibration band in `../runbook.md` §16 is relative to them.
   §5.2 names what consumes each figure, so nothing is derived that nothing reads.

## How reviewer input is captured

By reading the PR comment history, not by asking (§5.3). A reviewer's recollection
of what they catch is not evidence from the code; the comment history is. The same
pass also yields a shortlist of candidate probes, which is the point — it answers
"what do our reviewers catch" and "what should we build a probe from" at once.

There is no pre-enablement survey. The only question no measurement can answer —
whether trust in the tool rose or fell — is asked once at the end-of-evaluation
retrospective (`../runbook.md` Appendix C).

## When it happens

Once per platform, before the tool is enabled there, and reused for any repeat
evaluation on that platform.

Scope is fixed first (§5.7), which is what lets this folder and probe authoring
proceed in parallel instead of waiting on each other. Once the tool is enabled the
window has closed and the figures cannot be recaptured — keep `raw/`.
