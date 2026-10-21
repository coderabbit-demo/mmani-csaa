---
id:                 # e.g. P1-TPS-01, R4-TPS-01, PC2, IN4
probe:              # P1..P13, A4, E2, D-set, C-set, A-set, S-set, R1..R6, or platform (PC/IN)
platform:           # TPS | PC | IN
evaluation_mode:    # native | configured
rule_profile:       # configured R probes only: path + entry ID; otherwise NA
config_manifest:    # frozen manifest used for this run
author:
status: draft       # draft -> reviewed -> locked   (or: flawed)
reviewed_by:        # DPT reviewer
locked_on:          # YYYY-MM-DD, set when locked
---

# <ID>: <one-line title>

## Setup
- **Repo:**
- **Base commit (full SHA):**
- **Probe commit (full SHA):**
- **Fix reference (commit / PR / incident), if historical:**
- **What the PR contains:**
- **Context available to the tool:** (repo access, spec, Jira link, contract, environment matrix, ...)
- **Context deliberately withheld (P7 only):**
- **Authoritative standard / ground truth:**

## Expected finding (answer key)
- **Issue:**
- **Where:** (file + function / line)
- **Why it matters:** (impact if merged)
- **What a good review recommends:**

## Good signal (score 2-3)
-

## Bad signal (score 0-1)
- (include at least one plausible-but-wrong answer)

## Origin
INTRODUCED | PRE-EXISTING | EXPOSED | UNDETERMINED | NA

## Applicability
- Platforms:
- NA reason, if any:

## Evidence capture
Required by the readiness gate (runbook §7.5): state how this probe's result will be captured before the tool runs.
- **What to capture:** (the tool's comment text, a screenshot, a structured export)
- **Where it is filed:** `evidence/<platform>/`
- **Evidence-log row:** (fields per runbook Appendix B)

## Flawed (only if status: flawed)
- Date, reason, who decided. The probe is excluded from the evaluation.
