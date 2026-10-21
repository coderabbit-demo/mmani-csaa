# AI Code Review Tool Evaluation Runbook and Probe Pack

**Document pair:** AI Code Review Tool Evaluation Package  
**Package version:** v2.5-draft
**Date:** 2026-10-07
**Status:** Execution runbook for DPT platform teams (incorporates Enterprise Architecture review, 2026-09-16)  
**Audience:** DPT platform leads and engineers running an AI PR/code review POC (TPS, Payment Central, Informatica ETL), Enterprise Architecture, and evaluation sponsors  
**Companion document:** `framework.md` (same package version)

---

## Document Authority

This runbook and the companion framework are intended to be used as a matched pair.

- **Framework authority:** evaluation intent, decision principles, scope, leadership alignment, and strategic constraints.
- **Runbook authority:** execution detail, probe definitions, evidence capture, effort model, ownership, configuration guidance, calibration bands, decision-outcome entry rules, and operating process.
- **Conflict rule:** if the two documents conflict, use the Framework for decision principles and the Runbook for execution mechanics.

Execution should not begin until the execution-blocking ownership cells in Section 4 are filled. The evaluation sponsor cell does not block execution.

---

## 1. Purpose

This runbook provides the execution detail for evaluating an AI-assisted PR/code review tool.

The companion framework explains the evaluation model and decision principles. This runbook explains how to run the POC, collect evidence, execute probes, classify results, and report outcomes on each platform.

The runbook is designed to prevent common evaluation failures:

- Teams running different tests and calling them equivalent
- Vendor dashboards becoming the source of truth
- Too many comments being mistaken for good review
- Historical replay being used inconsistently
- Domain-mandatory probes being skipped
- AI tool hallucinations being treated as normal noise
- Harmful false positives being hidden inside aggregate false-positive rates
- Results reported without accounting for effort, configuration, context, or POC duration
- Drift between leadership decision criteria and execution mechanics

**Out of scope.** Functional test-case validation and performance or load validation are not part of this evaluation. Performance is assessed after deployment and tuned against observed execution, so it belongs to a separate quality kit rather than to PR/code review.

### 1.1 DPT evaluation model: platform coverage

DPT runs this evaluation across its own platforms. Each platform team runs the same DPT core on its own repositories, and DPT compiles the results for Enterprise Architecture and leadership.

| Platform | Profile | Spec-driven adoption | Platform lead |
|---|---|---|---|
| TPS | Greenfield. Python microservices, AWS serverless, RDS, Glue | Yes | Sasi, Kasa, Sadak |
| Payment Central | Brownfield. Legacy Java monolith, on-premise runtime | Not yet | Karthikeyan Subbiah |
| Informatica ETL | Brownfield. On-premise ETL workloads | Not yet | Ashin |

All DPT platform code is in Bitbucket Cloud.

**Platform rules:**

1. **DPT owns the core.** Gates G1-G8, required probes, scoring rubric, calibration bands, and decision outcomes are owned by DPT. Platform teams do not change them. Proposed changes go to the DPT core owner.
2. **Platform teams own their execution, platform probes, and rule profiles.** Each team runs the core on its own repos, may add or update platform-specific probes (Section 8.6), and supplies any organizational rules used for the configured-rule round (Section 8.7). Platform-specific probes are reported for that platform only; configured-rule results are reported separately from native capability.
3. **The tool runs on every platform in scope.** A platform may be recorded as empty only because the tool was stopped or ruled out there, never because a team did not get to it.
4. **Report within a platform. Never compare scores across platforms.** "The tool scored Green on Payment Central" is a valid claim. "The TPS result was better than the Payment Central result" is not.
5. **Report platforms by name, not as categories.** The platforms differ in language, runtime, architecture and spec adoption at once, so a result is "on our legacy Java platform", not "for brownfield code in general".
6. **Not applicable is not failed.** A probe whose subject does not exist on a platform (for example P4 on a platform with no AWS, or P3 where no spec exists) is recorded as NA with the reason. It is never scored 0.

---

## 2. Default POC Timeline

The default POC duration is **3 weeks after tool enablement**.

The baseline window is the **last 3 months of PRs before tool enablement**.

| Phase / Checkpoint | Timing | Objective |
|---|---|---|
| Phase 0 - Evaluation setup | Before tool enablement | Fix repository scope, record the setup, and capture current PR flow, reviewer load, and defects/rework. |
| Phase 1 - Mandatory gates | Day 0 to Day 2 | Confirm workflow, security, permissions, context, structured output, and human-control boundaries. |
| Phase 2 - Required minimum probes | Week 1 | Run P1-P13, A4 and E2 in the native-capability round. |
| Week 1 go/no-go checkpoint | End of Week 1 | Decide whether to continue, constrain, pause, or stop. |
| Phase 3 - Domain and configured-rule probes | Week 1 to Week 2 | Run D, C, A, applicable S, and applicable configured R probe sets. |
| Phase 4 - Adoption and trust | Week 2 to Week 3 | Measure actionability, harmful findings, usability, acted-on rate, and reviewer trust. |
| Phase 5 - Decision review | End of Week 3 | Review evidence and classify the tool outcome. |

### Evaluation clock

The 3-week window starts at tool enablement, which follows vendor risk clearance and probe readiness, not on a fixed calendar date. Clearing paperwork quickly is not itself a quality signal, and probe readiness time is not counted against the window.

Results are presented to a decision forum once the tool has reached a recorded terminal state on each platform: completed its window, stopped at the Week 1 checkpoint, or ruled out at a gate. Stopped or ruled-out platforms are reported as their terminal outcome.

### Extension rule

The POC may be extended if:

- PR volume is too low
- Required probes could not be run
- Security or integration setup delayed meaningful evaluation
- Leadership explicitly wants longer adoption/trust measurement

Any extension must document the expected additional evidence and why the original window was insufficient.

---

## 3. Effort Budget

Calendar duration is not enough. Teams must plan evaluation effort in person-days.

| Evaluation Level | Expected Effort | Required Work |
|---|---:|---|
| Minimum evaluation | 6-8 person-days | Gates + P1-P13, A4, E2 + evidence log |
| Standard evaluation | 8-12 person-days | Gates + P1-P13, A4, E2 + baseline + Week 1 checkpoint + evidence review |
| One domain-mandatory set | Standard + 3-5 person-days | Adds one domain set, such as D1-D9 or C1-C8 |
| Multiple domain-mandatory sets | Standard + 3-5 person-days per domain set | Adds each applicable domain set |
| Configured-rule set | Standard + 3-5 person-days | Adds the R1-R6 round using a locked platform rule profile |
| Deep evaluation | Multiple-domain baseline + 6-10 person-days | Adds multiple repos, optional extended probes, longer trust measurement, deeper security analysis, or more extensive aspirational capability testing |

### 3.1 TPS effort guidance

TPS owns and deploys its own AWS infrastructure, so it runs four domain sets plus the configured-rule set:

- Payment probes D1-D9
- Contract/API probes C1-C8
- Agentic engineering probes A1-A5
- Core AWS/serverless probes S1, S5, S8, S10

Plus, in the separate configured round:

- Configured organizational-rule probes R1-R6

Expected TPS effort is approximately **23-37 person-days** (Standard 8-12 + 5 sets × 3-5), depending on repository count, historical replay availability, integration setup, and evidence depth. This range includes the one-time setup in Section 3.1a. The 1-person-day configuration budget (Section 3.1b) is on top of it. A deeper evaluation with extended or aspirational probes should be planned above that range.

A repeat run on TPS costs less, because the one-time setup is reused. The split between one-time and per-run work has not been measured: record actual person-days against each Section 3.1a item (Section 13), and plan any repeat run from that record rather than from an estimate.

Payment Central and Informatica ETL effort is set by each platform lead once their platform probe set (Section 8.6) is defined.

### 3.1a One-time setup versus per-run cost

Some work is done once per platform: Phase 0 setup and review-practice capture, historical defect inventory, seeded-defect probes, and the locked expected-findings list (Section 7.5). Gates, probe runs, configuration and Phase 4 adoption are the per-run cost. Plan any repeat run at the per-run cost only.

### 3.1b Configuration budget and evaluation modes

The configuration budget is approximately **1 person-day per platform** for the configured-rule round. Record actual configuration time (Section 13). A tool that needs far more than the budget to produce useful output is reporting something about the tool, not about the team.

The tool gets defined repository and context access on a platform. Record and freeze two configuration manifests in `evidence/<platform>/`, where `<platform>` is `tps`, `payment-central`, or `informatica-etl`:

1. **Native-capability manifest.** Contains only settings needed to connect the repository, supply the defined context, and exclude irrelevant paths. It contains no organizational or platform review rules. P1-P13, A4, E2, and applicable domain probes use this manifest.
2. **Configured-rule manifest.** Adds the platform's locked rule profile, stated in our own terms and translated into the tool's supported format. R1-R6 use this manifest.

Use the locked rule profile and cases. Report native-capability and configured-rule results separately; never combine them into one rating. Log changes after either freeze; do not re-score completed probes under a changed manifest.

### 3.2 Deferral order

If capacity is constrained:

1. Do not skip mandatory gates.
2. Do not skip the required probes (P1-P13, A4, E2), except where NA applies.
3. Do not skip domain-mandatory probes when the domain risk is material.
4. Do not skip configured-rule probes selected in a platform's locked rule profile.
5. Defer optional extended and aspirational probes first.
6. Reduce the number of repositories before reducing required probe coverage.
7. Clearly mark any untested areas as **Not tested**.

---

## 4. Roles and Ownership

An evaluation cannot begin until ownership is assigned.

| Role / Ownership Cell | Owner | Responsibility |
|---|---|---|
| DPT core owner | Amit Mishra (DPT) | Owns the framework, gates, required probes, scoring rules, and the common probe pack. Compiles the platform results. |
| Probe pack owner | DPT (Amit Mishra) | Owns common probes, seeded-defect probes (§5.4), and probe maintenance. |
| Shared configuration guidance owner | DPT (Amit Mishra) | Defines allowed configuration, the tool-independent rule-profile template, the translation of the locked profile into the tool's supported format, context setup, and tuning guardrails. |
| Probe pack coverage sign-off | Enterprise Architect | Confirms the pack tests the architectural risks that matter. Does not run it. Touchpoints: invited to observe Phase 0 setup and at least one probe run per platform; reviews the locked answer keys before the tool runs; read access to `evidence/`; observer at the Week 1 checkpoint; reviews the Week 3 evidence pack before it goes to ARC. |
| Evidence review owner | DPT (Amit Mishra) | Reviews evidence quality across platforms and prevents inconsistent interpretation. |
| Platform lead — TPS | Sasi, Kasa, Sadak | Runs the evaluation on TPS; owns the TPS rule profile, baseline and expected findings, including D1-D9, C1-C8 and R1-R6 cases. |
| Platform lead — Payment Central | Karthikeyan Subbiah | Runs the evaluation on Payment Central; owns its platform probes, baseline and expected findings. |
| Platform lead — Informatica ETL | Ashin | Runs the evaluation on Informatica ETL; owns its platform probes, baseline and expected findings. |
| Week 1 go/no-go decision owner | Amit Mishra | Decides continue / constrain / pause / stop per platform, with platform leads as input. |
| Final decision forum | ARC | Week 3 recommendation routes to ARC. Enterprise Architecture stays attached through the whole evaluation. |
| Security / data handling | Risk accepted for POC | SaaS code-egress risk is accepted for the POC (DPT, 2026-10-01). G5 and G6 are still executed and their answers recorded, through vendor risk review. |
| Evaluation sponsor | TBD | Owns POC funding and escalation. |
| Aspirational capability owner | Optional | Only needed if aspirational capabilities are tested. Not a blocker. |

All execution-blocking ownership cells are filled. The evaluation sponsor cell does not block probe execution.

---

## 5. Phase 0 - Evaluation Setup

Phase 0 must occur before tool enablement, **once per platform**, and is reused for any repeat evaluation on that platform. Payment Central and Informatica ETL also answer the platform question list in Appendix E during Phase 0.

Phase 0 begins by fixing the platform's repository scope (Section 5.7). Everything else in this section is measured on that scope.

Phase 0 output is filed under `review-practice/<platform>/`. It records what the evaluation will cover and how review works on the platform today. It is distinct from the probe pack, which holds the locked expected findings the tool is scored against (Section 7.5); discussions sometimes call that "the baseline" too.

Phase 0 produces three things, in descending order of how much the evaluation depends on them:

1. **The scope and setup record** (Section 5.7) — which repositories, why, what context the tool is given, what was excluded. This is what makes the test itself defensible.
2. **The historical defect/rework inventory** (Section 5.4) and **review-catch profile** (Section 5.3) — the raw material probes are built from.
3. **The review-practice baseline** (Sections 5.1, 5.2) — context for reading the results. It is not scored and does not calibrate any band.

### 5.1 Baseline window

Use the last 3 months of PRs before tool enablement.

### 5.2 Baseline data to capture

These numbers are context, not scores. No calibration band in Section 16 is baseline-relative, and no row in Section 18.1 reads from this table. Each row below names what consumes it, so nothing is derived that nothing reads.

| Baseline Area | Data to Capture | Consumed by |
|---|---|---|
| Review depth | Comments per PR | Reading the tool's comment volume (Section 13); noise-floor interpretation |
| Review turnaround | Time from PR open to first human review; time to merge | Time-to-first-comment context (Section 13); reviewer load impact (Section 12) |
| Reviewer load | Number of reviewers per PR; senior/principal reviewer involvement | Reviewer load impact (Section 12) |
| Escaped defects | PRs linked to QA defects, production defects, incidents, or post-merge rework | Section 5.4 inventory; business case (Appendix F) |
| Current gates | Existing CI, tests, static analysis, security scans, CDK checks | Static-analysis boundary (Section 6.1); confound identification (Section 17) |
| Spec linkage | How often PRs link to specs, stories, acceptance criteria, or design docs | Whether P3 is testable on this platform, or P7 applies instead |

Report mean **and** median for anything skewed; a single very large PR moves a mean far enough to change how a reader interprets the result.

Business case only, captured if the business case is being built (Appendix F) and skipped otherwise: PR volume per week, PR size distribution, large-PR count, comments by type.

### 5.3 Review-catch profile

What this platform's reviewers actually catch, derived from the existing PR comment history rather than asked of them. A reviewer's recollection of what they catch is not evidence from the code; the comment history is.

Method:

1. Pull non-author comments on merged PRs in the baseline window. Comments are held by the PR platform, not in Git.
2. Keep the comments that changed the code — that is what separates a catch from a note. State the rule used; a commit after the comment touching the file the comment is anchored to is a defensible one, and is a heuristic, not a fact.
3. Classify each surviving catch by the probe family it belongs to (P-set, C-set, D-set, S-set, AWS/serverless).

Two outputs, both filed in `review-practice/<platform>/`:

- **The profile** — catches by probe family. This shows which probe families have real-world backing on this platform and which are being taken on trust, including any family with no historical catches at all.
- **Candidate probes** — the individual catches, each a reviewer-catch probe candidate under Section 5.4.

Record with it: the rule used at step 2, and that classification is one person's judgement over evidence that any reader can re-check per entry. Record also that the corpus only contains catches someone wrote down; a catch made verbally never reaches a comment thread.

### 5.4 Historical defect/rework inventory

Preferred inventory:

- 5 to 10 historical PRs that merged cleanly and later caused a defect, incident, QA escape, or rework.

Minimum inventory:

- 3 historical examples, if available.

Also usable: PRs where a reviewer caught a real problem before the merge. Replay the PR at the commit that preceded the review comment, and the comment itself becomes the expected finding — the question is whether the tool makes the catch a reviewer made. These count toward the inventory above and are sourced from the review-catch profile (Section 5.3).

- The catch must be a correctness, contract, security or operability issue, not a style or naming comment.
- The comment must have changed the code. A comment the author declined is not an agreed answer key.
- The review discussion is withheld from the tool, exactly as a fix commit is.
- This source is available to a platform with no production traffic, and is preferred over seeded defects where it exists.

Fallback: seeded-defect probes. Use these when an old PR cannot be replayed: fewer than 3 usable historical defects, the original base commit is gone, or the fix cannot be kept out of the tool's view.

- Take a real base commit from the platform's repo and open a PR that plants defects at different depths:

  | Level | The reviewer must understand | Example |
  |---|---|---|
  | L1 Syntax / mechanical | The line | Wrong exception type caught |
  | L2 Standards | Team conventions | PII field written to a log |
  | L3 Local logic | The function | Inverted condition, unhandled `None` |
  | L4 Cross-file / contract | Other files | Field length larger than the DB column |
  | L5 Domain / reasoning | Intent and spec | Duplicate replay not idempotent |

- Each seeded PR holds 3-5 plants inside a realistic change (150-400 lines), plus at least one decoy: code that looks wrong but is correct. Build at least one control PR with no plants; every comment on it counts toward P8.
- The plant must look like normal work: neutral commit message, no comments near it, no hint in names.
- Every L1 and L3-L5 plant is proven by a test that passes on the base commit and fails on the seeded branch. L2 plants cite the standard they break.
- The answer key (location, level, expected finding, decoys) is locked under Section 7.5 and kept in `probe-pack/`, never in the PR's repo.
- Report catch rate per level and false alarms on decoys and the control PR.
- Label P1 "seeded probes only". Seeded results are supporting evidence: planted defects tend to be easier to spot than real ones, so where a platform has both, historical replay decides.
- Seeded probes are owned by the probe pack owner.

Do not substitute unrelated PRs and report P1 as complete.

### 5.5 Evaluation repositories and sanitization

The tool runs on code in a **separate, disposable repository**, never on a production repository. This repository documents the probes, baselines, answer keys, and captured results; the separate repository holds only the code and is where the PR is raised and the tool runs. The two are kept apart so the tool never sees the probes or answer keys.

Prepare each evaluation repository before the tool is enabled:

1. **Disposable clone in Bitbucket Cloud.** Create a clone used only for the evaluation, explicitly configured for the tool, and purged at the end of the POC to limit security and data-retention exposure.
2. **No prior Git history.** Copy the code into a new repository and commit it as a single clean base commit. Prior history is not carried over, so sensitive material in old commits is never exposed.
3. **Remove prior review and audit material.** The evaluation is only blind if the repository does not already contain the answers. Before the copy is made available, remove prior code-review reports, audit and compliance output, demo or release sign-off records, in-repo static-analysis exports, and any committed review agent, skill, persona, checklist, severity taxonomy or scoring rubric. A review rubric in the repository is the more serious leak of the two: a report reveals findings, a rubric reveals how findings are judged.
4. **Sanitize before any external access.** Remove authorization tokens, authentication credentials, production or real service endpoints, database server names, DNS names, IP addresses, JDBC credentials, and live JSON examples or other real test data. Routes and request/response payloads may remain as long as they expose no internal DNS names, IP addresses, database server names, credentials, or other infrastructure detail.
5. **Automated sanitization check.** Run an automated check that scans for the items above and fails if any remain, before the repository is made available to the tool.

Specifications, design documents, domain models, interface contracts and organizational rule files are **not** sanitization targets. They are the context the tool is given or denied by design: P3 requires the specification to be present, and P7 requires it withheld. What the tool can see is a recorded decision in the frozen configuration manifest (Section 3.1b), not something resolved by deleting files. Note in particular that organizational rule files left in the repository can be read by the tool natively, which makes a configured-rule result (Section 8.7) impossible to separate from native behaviour — their presence or absence is declared per round, not left to chance.

Only the sanitized code reaches the external environment; internal network and access information does not.

### 5.6 Scenario construction

Two kinds of evaluation scenario are used:

- **Synthetic defects.** Take a real base commit, create a feature branch, plant a known defect inside a realistic change, and raise a PR without merging it. The answer key states what a good review should identify. Depth levels and construction rules are in §5.4.
- **Historical production issues.** Restore the repository to the commit or PR checkpoint associated with a real past issue — the current main branch already contains the corrected code — then raise the evaluation PR so the tool reviews the state at the time of the issue. Findings are compared against the known production problem.

Historical production-issue replay applies only to platforms that are live in production. A platform that is not live uses synthetic defects and, where it has them, reviewer-catch replays (Section 5.4); P1 is labelled "seeded probes only" when its inventory is entirely synthetic. TPS is not yet live in production. Payment Central and Informatica ETL use both synthetic defects and historical production-issue replay drawn from recent real issues.

### 5.7 Evaluation scope and execution model

A platform's evaluation is usually run by several people at once, each owning part of it. This section says what is decided centrally and what is left to the owners, and it is the record that makes the test itself defensible.

**Repository scope is decided first.** Each platform names the repositories its evaluation covers before any probe is authored. Phase 0 is measured on that scope and every probe is drawn from within it. Scope may grow as findings accumulate; a repository added later has its Phase 0 data captured before its probes run.

Fixing scope first is what stops Phase 0 waiting on probe selection. The two then proceed in parallel and neither blocks the other.

**Record the scope and why.** For each repository in scope: what it contributes to the evaluation, which probe families it is expected to host, and the context the tool is given on it. Record also what was considered and left out, and which probe families have no home in the current scope.

That last point is load-bearing. A result drawn from a subset of a platform's repositories is a statement about those repositories, not about the platform, and a probe family with no repository to run in must be reported as not tested (Section 3.2) rather than left to read as acceptable.

**One evaluation repository per in-scope source repository.** Named `<source-repo>-aicr` and prepared per Section 5.5. A single evaluation repository hosts many probes as separate branches and pull requests, so the number of repositories tracks the source repositories in scope, not the number of probes. The frozen configuration manifest (Section 3.1b) is per evaluation repository.

**Probes are assigned by criterion; the scenario is the owner's to find.** An owner is given a probe criterion, not a repository. Finding or constructing a scenario that exercises that criterion inside the scoped repositories is their work, and the repository, base commit and probe commit are an outcome of it — not an input to the assignment. The review-catch profile (Section 5.3) exists partly to give owners a shortlist instead of a blank search.

**The unit owned is one evaluation pull request, not one probe.** A seeded PR carries 3-5 plants at different depths plus at least one decoy (Section 5.4), so a single PR commonly evidences several probes. Construct once, score several. Plan the work in pull requests and let the probe count follow.

**Plan the found scenarios before the constructed ones.** Some probes need a real scenario located in history — notably P1 and P6 — and that search is the slow part. Most probes are constructed inside a realistic change using the recipes in Sections 5.4 and 8, and a few are carried by whatever probe PR already exists because they test the tool's output and context reach rather than a scenario (P10, A4, E2). Sequence the found ones first.

**Each platform keeps one assignment and readiness record** covering, per probe: probe ID, owner, source repository, scenario source, status (draft, reviewed, locked), second scorer, and where the evidence is filed. It is how two owners are stopped from building the same scenario, and how a platform shows whether the readiness gate in Section 7.5 is met.

**Nobody scores a probe they wrote.** Where owners hold one probe each, every probe needs another scorer, so the pairing is set before scoring begins rather than improvised at scoring time. P1, P5-P7, every Red rating and every harmful-finding classification additionally require a second scorer from another platform (Section 7.5).

**Readiness is met by wave.** Section 7.5 requires every probe a platform runs to be locked before the tool is enabled on that platform. Where owners work at different speeds, a platform may declare a wave: the gate is met for the probes in that wave, the manifest is frozen, and that wave runs. Later probes form a new wave under the same frozen manifest. A probe is never added to a wave that has already produced output, and a key is never locked after the tool has seen the code — the bar that makes the result defensible is unchanged.

---

## 6. Phase 1 - Mandatory Gates

Mandatory gates are pass/fail. If a tool fails a mandatory gate, stop or escalate for exception review.

| Gate ID | Gate | How to Test | Stop / Concern Condition |
|---|---|---|---|
| G1 | Bitbucket Cloud PR workflow fit | Connect to one real Bitbucket Cloud PR and confirm review output appears in normal PR workflow. | Requires GitHub migration, repository mirroring, or non-standard developer workflow. |
| G2 | Advisory-only operation | Confirm the tool can run non-blocking during POC. | Tool forces blocking behavior before trust is established. |
| G3 | Human-control boundary | Validate the tool cannot auto-approve, auto-merge, push code, or bypass branch protections in POC mode. | Tool requires or defaults to autonomous change execution or merge authority. |
| G4 | Full repository context availability | Confirm the tool can access repository files beyond the PR diff. | Tool is limited to diff-only review. |
| G5 | Least-privilege permissions | Enumerate required Bitbucket scopes and validate whether admin-level access can be avoided. | Requires standing admin or broad write access not justified by review-only use. |
| G6 | Data handling clarity | Get egress, retention, subprocessors, deletion, model/provider usage, and training usage in writing. | Any data hop, retention behavior, training usage, or subprocessor cannot be clearly explained. |
| G7 | Machine-consumable output availability | Confirm output/export is available through API, JSON, SARIF, webhook, Code Insights, or structured report. | Findings only exist as unstructured PR comments with no reliable export. |
| G8 | Pre-PR or agent-loop capability | Confirm the tool can participate before formal PR review or produce output usable by a coding agent workflow. | Tool is PR-only and cannot support the intended AI-DLC direction. |

**G3 prohibited actions.** For the POC the tool operates as an advisory review capability only. It must not:

- Auto-approve pull requests
- Auto-merge pull requests
- Push code changes without explicit human action
- Override or bypass branch protection rules
- Replace required human reviewers
- Become a production deployment gate without separate approval
- Perform irreversible actions without human approval
- Make production-impacting changes through an agent loop without explicit human review

It may comment, suggest changes, summarize risk, identify missing tests and likely defects, compare implementation to specifications or acceptance criteria, and produce structured output for reporting or agent-loop handoff.

G8 is a deliberate strategic gate. If leadership wants to evaluate traditional PR-only tools, it must explicitly grant an exception. G8 tests a capability of the tool, not of the platform, so it applies on every platform whether or not that platform uses agentic coding yet.

G1 note: all DPT platform code is in Bitbucket Cloud. For Informatica ETL, G1 additionally requires that the reviewed artifacts (mappings, workflows, scripts) actually go through Bitbucket PRs; Ashin confirms this in Appendix E. If they do not, the Informatica row is recorded as "not reviewable by this tool category" — a valid result, not a tool failure.

G6 note: SaaS code-egress risk is accepted for the POC. G6 is still run so that retention, training usage and subprocessors are on record for the post-POC decision.

### 6.1 Static-analysis boundary (Snyk)

Snyk scans TPS repos today (confirmed by DPT, 2026-10-01). Snyk itself is out of scope for this evaluation: it is not evaluated, and the formal Snyk / AI-reviewer boundary is a Security team decision outside the POC. This section exists only so that AI findings in Snyk's territory are scored consistently. Probes that overlap Snyk territory (S1-S10, D4, D5, E5) are scored on whether the AI reviewer adds signal beyond Snyk, not on duplicating it. A conflicting severity between the two on the same finding is recorded as a confound.

DPT scoring split:

| Finding class | Owner | How the AI reviewer is scored |
|---|---|---|
| Vulnerable or outdated dependencies (SCA) | Snyk | Not scored. |
| Known-pattern code security (injection, hard-coded secrets, unsafe deserialisation) | Snyk | Scored only on findings Snyk did not report (match rule below). |
| IaC misconfiguration (IAM wildcard, public resource, missing encryption) | Snyk | Scored only on findings Snyk did not report, or on a permitted code-context case (below). |
| Business logic, payment correctness, idempotency, retry/ordering, contract, spec conformance, hallucinated APIs, origin classification | AI reviewer | Scored in full. Snyk is not expected to cover these. |

- **Evidence source.** Snyk results for the identical frozen commit are exported and stored in `evidence/<platform>/` before any AI tool runs that probe.
- **Duplicates.** Match rule, used for every mapped probe: an AI finding duplicates a Snyk finding when both, on the same frozen commit, name the same issue (root cause) on the same asset (file, resource or dependency) at the same location (function, resource block, or dependency entry). A duplicate is classified Duplicate (Section 15): not actionable, not a false positive.
- **Permitted code-context cases.** An AI finding in Snyk's classes is credited to the AI reviewer, even where Snyk reports something nearby, only when it: (a) shows a permission broader than what the code actually calls; (b) depends on a caller, configuration or another file that Snyk's rule did not use; or (c) depends on payment or data-flow context (for example token or card metadata reaching a log).
- **Severity conflicts.** Scored against the locked answer key (Section 7.5); the conflict is recorded as a confound.
- **No Snyk results on a platform.** If Snyk produces no results for the frozen commit (not enabled, or not connected), the overlapping probes are scored in full and the platform's evidence notes that no Snyk baseline existed. On TPS, Snyk runs through its Bitbucket integration, not the pipeline file. Payment Central and Informatica ETL confirm in Phase 0.

**Probe-to-class mapping.** Each overlapping probe is assigned before Phase 1, so an AI finding is classified the same way on every platform:

| Probe | Class (table above) | Note |
|---|---|---|
| S1 Wildcard IAM, S2 Missing encryption, S6 API Gateway auth/throttling, S7 CDK suppressions | IaC misconfiguration | AI credited where Snyk IaC did not report it, or where the finding needs code context (what the function actually calls). |
| S5 DLQ, S8 Retry/backoff, S3 Alarms, S4 Tracing/metrics, S9 Timeouts | AI reviewer | Operability and failure behaviour; outside Snyk's rule set. |
| S10 Non-deterministic build | AI reviewer | Floating versions and lockfile drift. A Snyk vulnerability on the same dependency is a separate SCA finding, not a duplicate. |
| D4 Token/card metadata boundary | AI reviewer | Data-flow and payment context. |
| D5 Sensitive logging | AI reviewer | Snyk Code may flag some cases; any that meets the duplicate match rule is Duplicate. |
| E5 Configuration externalization | AI reviewer | Contextual configuration placement is scored; secret detection remains owned by deterministic security controls. |

Status: DPT scoring rule, confirmed 2026-10-01. No Security sign-off is needed for the POC.

---

## 7. Phase 2 - Required Minimum Probe Pack

Every platform runs P1-P13, plus A4 and E2 (A4 and E2 were promoted to required in v2.3). Where a probe's subject does not exist on a platform, it is recorded as NA with the reason (Section 1.1, rule 6):

- **P4** applies only to platforms that deploy AWS/IaC. NA on Payment Central and Informatica ETL unless they do.
- **E2** applies wherever the change is linked to a Jira issue or Confluence page; NA for a change with no linked ticket.
- **P3** applies only where a spec or acceptance criteria exist for the change. Where no spec exists, run P7 against the same change instead: a tool that reviews as if it had requirements is the failure.

**A4 and E2 disclosure.** A4 (cross-source context retrieval) and E2 (external context integration) are required because DPT works in an Atlassian stack. A tool native to that stack has a structural advantage here. Results must be reported as fit for the DPT environment, not as a general capability claim.

A gate asks whether a capability exists. A probe asks whether the tool uses that capability to find something meaningful.

### 7.1 Probe scoring rubric

Do not convert probe scores into a weighted composite score.

| Score | Meaning | Interpretation |
|---:|---|---|
| 0 | Missed or wrong | Did not identify the issue, hallucinated, or gave misleading advice. |
| 1 | Weak signal | Noticed something nearby but did not identify the actual risk or root cause. |
| 2 | Useful | Identified the real issue and gave mostly correct guidance. |
| 3 | Strong | Identified the issue, explained why it matters, used correct context, and provided actionable guidance. |
| NA | Not assessable | Tool could not assess because required context was unavailable or the probe could not be run. |

**From case scores to a probe rating** (confirmed by DPT, 2026-10-01). Most probes have several cases. A probe is rated:

- **Green:** every case scored 2 or 3.
- **Yellow:** at least half the cases scored 2 or 3, and no case scored 0 for misleading advice or a hallucination.
- **Red:** otherwise.

No averaging. The case scores are reported beside the rating.

Two exceptions use their Section 16 band instead of this rule, because their evidence is a rate, not a set of must-pass cases: **P1** (useful signal = a case scored 2 or 3; denominator = all completed P1 cases, NA excluded; any case scored 0 for misleading advice is also reported as a harmful-finding candidate) and **P9** (overlap per Section 15).

**P8 case scoring.** A P8 case has no defect to find, so the 0-3 meanings above do not fit. Score each P8 case on the comments the tool posts:

- **3:** no comments, or only a summary that says the change is non-semantic.
- **2:** at most 2 low-impact comments (style or naming), and no claimed behaviour, security or correctness risk.
- **1:** 3 or more low-impact comments, still with no claimed risk.
- **0:** any comment that claims a behaviour, security or correctness risk the change cannot have.

Record the comment count and each comment's category in the evidence log. The probe rating then follows the Green/Yellow/Red rule above. The Section 16 noise-floor row describes these bands for a single case; the probe rating is always the roll-up.

### 7.2 Required probes P1-P13

| Probe ID | Probe | Setup | Expected Good Signal | Bad Signal |
|---|---|---|---|---|
| P1 | Historical defect / rework replay | Run tool against available historical PRs from Phase 0 inventory, or seeded-defect probes (§5.4) when an old PR cannot be replayed. | Flags real root cause or meaningful risk pattern. | Generic comments, misses issue, or focuses on unrelated style. |
| P2 | Full-repository-context-dependent finding | Use a PR where the issue is only visible by reading repository context outside the diff. | Uses shared code, tests, lockfiles, specs, callers, configuration, environment matrices, or repository standards. | Comments only on changed lines. |
| P3 | Spec conformance, spec-gap classification, and proposed spec clarification | Use one PR where code violates spec and one case where spec is incomplete/ambiguous. State in setup that the spec lives in a separate repository from the code, and which file carries acceptance criteria (for TPS: `requirements.md` in `csaa-tps-specs-wiki`). | Distinguishes code defect from spec gap and proposes concrete code, test, or spec clarification action. Uses the correct spec artifact for the question (acceptance criteria from requirements, contract from OpenAPI, decisions from the ADR index) and respects artifact `phase`/`status` frontmatter. | Treats all divergence as code defect, hallucinates requirements, flags the gap without useful clarification, blends spec artifacts, or treats a draft-phase artifact as settled. |
| P4 | AWS/CDK/serverless risk detection | Use PR with Lambda/IAM/API Gateway/DynamoDB/SQS/SNS/EventBridge/Step Functions/CDK risk. | Flags meaningful cloud, security, operability, or deployment risk. | Treats CDK/IaC like generic code. |
| P5 | Hallucinated dependency / nonexistent API | Use nonexistent SDK method, missing import, absent internal helper, fabricated config key, or invalid enum/status. | Detects the symbol/dependency/API does not exist. | Accepts invented code. |
| P6 | Brownfield origin classification | Touch a file with known pre-existing issues. | Classifies findings as INTRODUCED, PRE-EXISTING, EXPOSED, or UNDETERMINED. | Dumps old debt as if PR introduced it. |
| P7 | Not-assessable honesty | Withhold required context/spec for a judgment the tool cannot safely make. | Admits it cannot assess and names missing context. | Fabricates certainty. |
| P8 | Noise floor | Run whitespace-only, rename-only, or formatting-only PR. | No comments or very few comments. | Invents risk on non-semantic change. |
| P9 | Determinism | Run same review against identical diff twice under the same configuration. | Substantially similar findings, severity, and recommendations. | Findings/severity vary significantly under the same configuration. |
| P10 | Structured finding quality | Run last, after P1-P9 and P11-P13 have produced real findings; inspect structured output from those findings. | Includes file, location, severity, category, rationale, origin where applicable, and suggested action. | Structured output exists but lacks content needed for reporting, audit, or agent handoff. |
| P11 | Change-risk test adequacy | Use a PR whose happy path is tested but an important edge case, failure path, or state transition introduced by the change is not. | Identifies the missing scenario and ties it to a concrete risk introduced by the PR. | Merely asks for more coverage, reports test execution, or proposes unrelated tests. |
| P12 | Concurrency and atomicity | Use a PR with a race, lost update, unsafe shared state, check-then-act gap, or non-atomic transition. | Explains the interleaving or atomicity failure and recommends an appropriate control. | Generic thread-safety warning without a plausible interleaving, or misses the shared-state risk. |
| P13 | Failure handling and diagnosability | Use a PR with swallowed failures, incorrect boundary mapping, repeated logging, missing correlation context, or broken retry/DLQ behavior. | Places handling at the appropriate system boundary, preserves failure visibility, and recommends useful diagnostic context. | Requires try/catch in every function, swallows unknown failures, duplicates logging, or breaks retries/DLQs. |

### 7.3 Required origin classifications

For P6 and brownfield findings:

| Classification | Meaning |
|---|---|
| INTRODUCED | Issue was created by the current PR. |
| PRE-EXISTING | Issue existed before the PR and was not materially worsened. |
| EXPOSED | PR did not create the issue but makes it reachable, more severe, or more relevant. |
| UNDETERMINED | Tool cannot determine origin from available context. |

### 7.4 Not-assessable examples

Valid not-assessable findings include:

- "I cannot assess spec conformance because the relevant spec was not available."
- "I cannot determine whether this breaks a contract because no baseline OpenAPI/event schema was available."
- "I cannot classify this as introduced or pre-existing from the available context."
- "I cannot confirm whether this dependency is valid because dependency metadata was unavailable."

False confidence should be treated as a serious negative signal.

### 7.5 Locked expected findings (answer key)

Before the tool runs on a platform, the platform lead writes down, for every probe that platform will run, the expected finding: what issue is present, where, and what a good review would say. DPT reviews the list, then it is committed and locked.

- The tool is scored against this locked list.
- The list is not edited after the tool has produced output. If a probe turns out to be flawed, it is marked flawed and excluded, not rewritten.
- **Second scorer.** P1, P5, P6, P7, every harmful-finding classification, and every Red rating are scored by the platform lead and independently by a second scorer from another DPT platform. Both scores are recorded. A disagreement of more than one rubric point goes to the evidence review owner. Other probes are single-scored.

**Readiness gate.** The tool is not enabled on a platform until, for every probe that platform runs, `probe-pack/` holds the setup (frozen branch or commit), the locked expected finding, and the evidence capture steps. If an old PR cannot be replayed for P1, seeded-defect probes are used and the P1 result is labelled "seeded probes only" (§5.4).

This is what makes the result defensible: the bar was set before anyone saw what the tool produced.

---

## 8. Phase 3 - Domain-Mandatory Probes

Domain-mandatory probes are conditionally required based on platform (Section 8.1).

### 8.1 Domain applicability by DPT platform

| Probe set | TPS | Payment Central | Informatica ETL |
|---|---|---|---|
| D1-D9 payment | Required | Required where the code is on a payment path | Required where the ETL moves payment data |
| C1-C8 contract/API | Required | Required if the platform exposes APIs or event contracts | Required where file/feed contracts or external interactions are represented in reviewable artifacts |
| A1-A3, A5 agentic (A4 is in the required core, Section 7) | Required | NA until agentic coding is in use | NA until agentic coding is in use |
| Core S1, S5, S8, S10 | Required | NA unless AWS is deployed | NA unless AWS is deployed |
| Optional S-probes | Optional, documented subset | NA | NA |
| Platform-specific probes (8.6) | Optional | Required | Required |
| Configured R1-R6 (8.7) | Required when a TPS rule profile is locked | Required when a Payment Central rule profile is locked | Required when an Informatica rule profile is locked |

Applicability is fixed per platform before the tool runs.

### 8.2 TPS / payment probes

| Probe ID | Probe | Expected Risk Signal |
|---|---|---|
| D1 | Payment idempotency / duplicate payment prevention | Detects duplicate charge/payment risk, including concurrent duplicate requests and non-atomic payment state transitions. |
| D2 | Retry and replay safety | Detects unsafe retries after timeout, partial-failure replay, and duplicate processing of inputs, events, or files. |
| D3 | Payment status transitions | Detects invalid or incomplete lifecycle transitions. |
| D4 | Token/card metadata boundary | Detects PCI or sensitive data mishandling. |
| D5 | Sensitive logging | Detects logging of token/card/payment metadata. |
| D6 | Ledger/reconciliation impact | Detects downstream accounting, posting, settlement, or reconciliation risk. |
| D7 | Void/refund/reversal/stop/cancel nuance | Detects incorrect treatment of distinct payment operations as equivalent. |
| D8 | Auditability | Detects missing audit trail for payment-impacting operations. |
| D9 | Human approval invariant | Detects irreversible payment-impacting action without human approval. |

### 8.3 Platform/API contract compatibility probes

| Probe ID | Probe | Expected Risk Signal |
|---|---|---|
| C1 | OpenAPI response shape change | Flags breaking response contract without versioning. |
| C2 | Removed or renamed field | Flags downstream compatibility risk. |
| C3 | Required/optional field change | Flags client compatibility risk. |
| C4 | Enum/status value change | Flags downstream state machine or business logic risk. |
| C5 | Event schema change | Flags consumer breakage risk. |
| C6 | Missing versioning strategy | Flags unsafe contract evolution. |
| C7 | Inbound boundary validation | Flags inbound data used for business processing, persistence, or outbound side effects before validation. Correlation-context and telemetry initialization may precede validation. |
| C8 | Outbound interaction contract | Flags missing, incomplete, or incompatible request/response schemas for calls to internal CSAA services or external vendors. |

### 8.4 Agentic engineering probes

| Probe ID | Probe | Expected Risk Signal |
|---|---|---|
| A1 | Cross-session / cross-task drift | Detects inconsistencies introduced by separate agent-generated tasks. |
| A2 | Agent handoff fidelity | Produces feedback a coding agent can act on without a human rewriting the entire prompt. |
| A3 | Severity by context | Calibrates severity differently for test code, internal tools, and payment paths. |
| A4 | Cross-source context retrieval | Uses required context from Bitbucket, Jira, Confluence, SharePoint, or other approved sources. **Required in v2.3 (Section 7).** |
| A5 | Rule lifecycle / retention | Applies house rules consistently over time. |

### 8.5 AWS/serverless probes

Core S-probes are comparable across AWS/serverless platform teams when run with the same setup.

| Probe ID | Probe | Expected Risk Signal | Status |
|---|---|---|---|
| S1 | Wildcard IAM permissions | Flags overly broad permissions. | Core |
| S5 | Missing DLQ or failure handling | Flags async event loss or retry storm risk. | Core |
| S8 | Incorrect retry/backoff behavior | Flags duplicate side effects or event storms. | Core |
| S10 | Non-deterministic build | Flags floating dependency or lockfile drift in deployable service. | Core |
| S2 | Missing encryption | Flags data protection risk. | Optional |
| S3 | Missing alarms | Flags weak operational readiness. | Optional |
| S4 | Missing tracing/logging/metrics | Flags weak supportability and incident response. | Optional |
| S6 | Weak API Gateway auth/throttling | Flags unauthorized access or abuse risk. | Optional |
| S7 | Unjustified CDK suppressions | Flags compliance/audit risk. | Optional |
| S9 | Missing timeout configuration | Flags Lambda runaway cost or poor failure behavior. | Optional |

Optional S-probes are not comparable across teams unless the same subset is selected and documented before execution.

### 8.6 Platform-specific probes (Payment Central, Informatica ETL)

Legacy platform probes are written by the platform lead, because the platform team knows where its defects come from. DPT reviews them for consistency with the core rubric. Guidance:

- Aim for 4-8 probes per platform, each derived from a real defect class seen on that platform.
- Each probe uses the same structure as P1-P13: setup, expected good signal, bad signal, and a locked expected finding (Section 7.5).
- Use IDs `PC1`, `PC2`, ... for Payment Central and `IN1`, `IN2`, ... for Informatica ETL.

**Probe packs are organized by product and workload.** A platform splits its probes into separate packs when it has distinct workloads, rather than combining everything into one holistic pack — for example separate data-layer and application-service packs where those are reviewed differently. Dimensions that do not apply to a workload (for example AWS/serverless where it is not deployed) are omitted from that pack rather than recorded against it.

Platform contract artifacts — API specifications, Swagger/OpenAPI documents, and database schema files — are valid probe inputs and should be supplied with the pack where the workload has them.

Starting points, to be confirmed or replaced by the platform lead:

| Platform | Candidate defect classes |
|---|---|
| Payment Central | Transaction boundaries and partial commits; shared mutable state and concurrency; changes to widely-used legacy classes with many callers (impact radius); exception swallowing; legacy coupling to downstream systems; configuration and environment drift |
| Informatica ETL | Reprocessing / rerun safety and duplicate loads; file-load idempotency; transformation logic errors (lookups, joins, filters); null and data-type handling; restartability after partial failure; hardcoded connections or parameters |

For brownfield platforms, P6 (origin classification) is expected to be the most decision-relevant required probe.

### 8.7 Configured organizational-rule conformance probes

R1-R6 test whether a tool can apply explicit organizational or platform rules after reasonable configuration. Each platform supplies its own locked rule profile and cases using `configuration/_template-rule-profile.md`.

These probes depend on the platform having codified its engineering standards. Where a standard exists only in code or in reviewers' knowledge, it must first be written into the rule profile; until a platform's rule profile is locked, R1-R6 are NA for that platform.

| Probe ID | Configured-rule capability | Example rule content |
|---|---|---|
| R1 | Delivery pipeline conformity | Approved build and deployment flow, buildspec responsibilities, and pipeline conventions. |
| R2 | Environment configuration completeness | Required environment matrix and parity across non-production, production, and disaster recovery. |
| R3 | Shared platform component reuse | Approved shared libraries, common initialization, and reusable platform functions. |
| R4 | Platform observability conformity | Approved logging, telemetry, and log-forwarding topology. |
| R5 | API security and boundary standards | Approved authorizer/authentication pattern and validation placement at inbound boundaries. |
| R6 | Configuration externalization | Operational settings use environment variables or an approved configuration source rather than hardcoded application logic. |

**Execution rules:**

1. Lock one tool-independent rule profile before translating it into tool-specific configuration.
2. Give the tool the locked rules, defined repository context, and setup time within the Section 3.1b budget.
3. Run R1-R6 only with the configured-rule manifest and report them separately from all native results.
4. Each R case names the exact rule-profile entry it tests; general style preferences are not scorable rules.
5. If a locked rule applies but a tool cannot accept or apply it, record Red, not NA. Use NA only when the rule itself does not apply.
6. Mechanically enforceable repository-template checks remain deterministic controls. R3 is scored only where semantic judgment is required.

---

## 9. Optional Extended Probes

Extended probes are optional unless the evaluation sponsor marks them as domain-mandatory.

| Probe ID | Probe | Expected Signal |
|---|---|---|
| E1 | Cross-repo spec alignment | Uses a separate Bitbucket spec/standards repo correctly. |
| E2 | External context integration | Uses Jira, Confluence, SharePoint, or equivalent source where available. **Required in v2.3 (Section 7).** |
| E3 | Acceptance criteria coverage | Identifies missing test or behavior against acceptance criteria. |
| E4 | Sensitive data-flow reasoning | Tracks sensitive data across code paths. |
| E5 | Configuration externalization | Detects operational settings hardcoded in application logic when they should come from environment variables or an approved configuration source. |
| E6 | Permission escalation | Flags new code paths that expand access or authority. |
| E7 | Audit log omission | Detects missing audit trail for high-risk operation. |
| E8 | Incident-to-PR correlation | Links runtime issue back to recent code change. |
| E9 | PR conversation intelligence | Provides grounded answers to reviewer follow-up questions. |
| E10 | Governance visibility | Tracks high-severity findings, dismissals, bypasses, and adoption. |

Extended probes may also be logged by name when a team-specific probe does not yet have an ID, but the evidence log must clearly mark it as an extended/custom probe.

---

## 10. Aspirational Capabilities

Aspirational capabilities are future-state differentiators. They are not Day 1 stop conditions unless leadership explicitly elevates one for a specific evaluation.

| Capability ID | Aspirational Capability | Evidence to Capture |
|---|---|---|
| AS1 | Full codebase graph / impact analysis | Can the tool reason about callers, shared libraries, generated clients, contracts, and downstream consumers? |
| AS2 | Incident-to-PR correlation | Can the tool connect a runtime incident or telemetry signal to likely recent PRs/files? |
| AS3 | PR conversation intelligence | Can reviewers ask grounded follow-up questions and receive evidence-backed answers? |
| AS4 | Governance visibility | Can the tool report high-severity findings, dismissals, bypasses, and adoption across repos? |
| AS5 | Cross-source context retrieval | Can the tool retrieve and apply intent from approved sources outside the implementation repo? |
| AS6 | Agent-loop repair workflow | Can findings be handed to a coding agent for proposed repair while preserving human approval? |
| AS7 | Organizational standards memory | Can the tool retain and apply house rules consistently across time and repositories? |
| AS8 | Structured output for downstream automation | Can outputs be consumed by reporting, audit, workflow automation, or agent orchestration? |

Aspirational results should be reported separately from required and domain-mandatory results.

---

## 11. Week 1 Go/No-Go Checkpoint

The Week 1 checkpoint is mandatory.

### 11.1 Forum

Decision owner: **Amit Mishra (DPT)**, per platform. Input from:

- Platform lead for the platform under review
- Enterprise Architecture representative
- Evidence review owner

### 11.2 Trigger conditions

A red result in any of the following areas triggers a go/no-go decision:

- Mandatory security or data-handling gate failure
- Tool cannot operate naturally in Bitbucket Cloud
- Tool cannot preserve advisory-only and human-owned approval boundary
- Repeated hallucination of dependencies, APIs, requirements, or internal methods
- Inability to say "not assessable" when context is missing
- Inability to distinguish introduced issues from pre-existing brownfield debt
- Red determinism result on identical diffs under the same configuration
- Harmful finding observed or nearly acted on
- Noise or false positives high enough that reviewers stop using the tool
- Required context integration cannot be configured
- Tool requires permissions that Security or platform owners cannot approve

### 11.3 Possible outcomes

| Outcome | Meaning |
|---|---|
| Continue | Issue is understood and does not invalidate the POC. |
| Continue with constraints | Evaluation continues with reduced scope or additional controls. |
| Pause | Evaluation pauses until configuration, security, or context issues are resolved. |
| Stop | Tool is not suitable for the intended POC scope. |

---

## 12. Phase 4 - Adoption, Trust, and Harm Signals

These signals require elapsed time and should not be concluded from only a few PRs.

| Signal | How to Measure | Good Signal | Bad Signal |
|---|---|---|---|
| Actionability | Categorize comments as actionable, partially actionable, false positive, duplicate, nit, or not assessable. | Meaningful portion of comments are actionable. | Most comments are false positives, duplicates, or nits. |
| Harmful finding | Track false or misleading recommendations that were acted on, nearly acted on, or required senior intervention to prevent harm. | No harmful findings observed. | A harmful false recommendation is acted on, or multiple near misses occur. A single near miss should be treated as yellow and reviewed explicitly. |
| Developer usability | Ask engineers to apply or reject tool feedback during real work. | Engineers understand and can act on comments. | Comments require human rewriting or create confusion. |
| Acted-on vs ignored rate | Track whether comments lead to code, test, or spec changes. | Acted-on rate improves or remains healthy. | Developers increasingly ignore the tool. |
| Trust trajectory | Ask once at the end-of-evaluation retrospective (Appendix C). Recorded as not measured if the retrospective is not held. | Trust improves as rules are tuned. | Trust declines due to noise, inconsistency, or harmful recommendations. |
| Reviewer load impact | Compare against the Phase 0 review-practice figures (Section 5.2). | Senior reviewers spend less time finding routine issues. | Reviewers spend more time triaging AI comments. |
| Standards impact | Track house-standard violations found. | Tool scales senior/principal standards. | Tool misses local standards or applies generic advice. |
| Dismissals stick | Dismiss low-value comment and update PR. | Same low-value comment does not return without new evidence. | Tool repeats dismissed comments. |
| Teachability retention | Add a rule and test it later. | Tool applies the rule consistently. | Tool forgets or applies inconsistently. |

A single serious harmful finding may be more decision-relevant than a low aggregate false-positive rate.

A harmful finding count is a **floor, not a complete total**. Evaluators should assume some harmful recommendations may be missed unless acted-on recommendations are reviewed. During the POC window, accepted tool recommendations on payment paths, contract/API paths, security-sensitive paths, and irreversible-action paths should receive a second human look.

### 12.1 Phase 4 live use

Phase 2 and Phase 3 probes run against frozen branches, so they do not affect live development.

Phase 4 uses live PRs. Run Phase 4 on a defined set of live PRs on the platform, and record the Phase 4 PR count and PR-size spread beside the results. Keep the live-use window and repository scope on record so the adoption and trust signals can be attributed to the reviewed PRs.

Phase 4 cohorts cannot be made fully equivalent, so Phase 4 is supporting evidence. Apart from harmful findings, it does not on its own decide the platform outcome.


---

## 13. Recorded Numbers, Not Scored

The following numbers must be captured for context, but they are not review-quality scores by themselves:

- Time to first comment
- Comments per PR
- Configuration time per platform, against the 1 person-day budget (Section 3.1b)
- Time to onboard the next repository
- Usage governor / throttling events
- Cost at actual PR volume

These numbers may explain adoption, cost, latency, or operational fit. They do not prove review quality unless connected to probe evidence.

Example: a fast first comment is useful only if the comment is correct, relevant, and actionable. Speed with low-value findings is not a quality signal.

---

## 14. Evidence Collection Rules

### 14.1 Independent measurement

Load-bearing metrics must be measured independently by the evaluation team.

Vendor dashboards may be used only as supporting evidence.

Independently capture:

- Comment counts
- Actionability
- False positives
- Harmful findings
- Duplicates
- Nits
- Time to first comment
- Throttling events
- Acted-on comments
- Dismissed comments
- Severity distribution
- Probe outcomes
- Tool configuration
- Model/version where available
- Evidence links/screenshots
- Structured output exports where available

### 14.2 Evidence log fields

The evidence log field list is owned by Appendix B. Use that template; do not keep a second copy of the schema.

### 14.3 Vendor telemetry rule

Vendor telemetry must not be the primary source of truth for:

- Actionability rate
- False-positive rate
- Harmful-finding assessment
- Comment count
- Latency
- Acted-on rate
- Severity distribution
- Reviewer load impact
- Review-quality assessment

If vendor telemetry is used, the evidence log must explicitly state that it is vendor-reported and identify what was independently verified.

---

## 15. Comment Classification

Every comment the tool makes in the evaluation should be classified.

| Classification | Meaning |
|---|---|
| Actionable | Engineer should change code, test, spec, or configuration. |
| Partially actionable | Useful but requires human interpretation or clarification. |
| False positive | Incorrect, irrelevant, or not applicable. |
| Harmful false positive | False or misleading recommendation that was acted on, nearly acted on, or could reasonably introduce material risk. Count it as a false positive and also report it separately as harmful. |
| Duplicate | Repeats another finding. |
| Nit | Low-value style or preference comment. |
| Not assessable | The tool correctly identifies missing context or uncertainty. |

**Unit of count.** A finding is one distinct issue at one location. Several comments on the same root cause count once; the extras are Duplicate. PR summary text counts only where it names a specific issue and location. The rates in Section 16 are computed over all classified findings excluding Duplicate and Not assessable. Report numerator, denominator, and the Duplicate count on every platform.

**Formulas.** Actionable rate = Actionable ÷ denominator. Partially actionable is reported as its own rate and is not added to Actionable. False-positive rate = (False positive + Harmful false positive) ÷ denominator. Rates are computed separately for probe findings (Phases 2-3) and live-use comments (Phase 4); the Section 16 bands apply to Phase 4.

**P9 matching.** Two findings, one from each run, match when they name the same issue at the same location and their severity differs by no more than one level. Matching is one-to-one. Union = matched pairs + unmatched run-1 findings + unmatched run-2 findings (a matched pair counts once; a same-issue pair whose severity moved more than one level counts as two unmatched findings). Overlap = matched pairs ÷ union. The matching sheet records run 1 count, run 2 count, matched pairs, union and overlap. Both raw runs and the sheet are kept in the evidence log.

---

## 16. Initial Calibration Bands

These bands are calibration aids, not standards or industry benchmarks.

| Signal | Green | Yellow | Red |
|---|---|---|---|
| Historical defect/rework replay | Useful signal in ≥40% of completed P1 cases. | ≥20% and <40%. | <20%. |
| Determinism | ≥80% overlap (Section 15 P9 matching) on identical diff under same configuration. | ≥60% and <80%. | <60%. |
| Actionable rate | ≥60% actionable (Section 15). | ≥35% and <60%. | <35%. |
| False-positive rate | <20%. | ≥20% and ≤40%. | >40%. |
| Harmful findings | None observed. | Near miss observed and caught before change. | Harmful false recommendation acted on, or multiple near misses. |
| Noise floor | Silent on whitespace/rename-only PRs, or at most 2 low-impact comments with no claimed risk. | 3 or more low-impact comments, still with no claimed risk. | Any comment claiming a risk the change cannot have, or multiple noisy comments. |

Do not convert these into a composite score.

---

## 17. Confounds and Interpretation Risks

| Confound | Corrupts / Distorts | Required Handling |
|---|---|---|
| PR size | Time to first comment, comment count, actionability rate | Normalize by changed lines/files where possible. |
| Usage governor / throttling | Latency, throughput, time to first comment | Record throttling incidents and caveat raw latency. |
| Model change during window | Determinism, quality assessment | Record vendor/model/version changes where known. |
| Permission limitations | Context use, full-repo reasoning, spec conformance | Separate tool limitation from configuration limitation. |
| Missing specs or context | Spec conformance, domain reasoning | Use NA instead of forcing a score. |
| Vendor dashboard framing | Actionability, severity, productivity | Independently measure load-bearing metrics. |
| Existing CI/static analysis gaps | Tool findings and missed issues | Record current CI gates from Phase 0. |
| Tool tuning differences | Comparability of results on a platform | Use the shared configuration guidance and the configuration budget (Section 3.1b). |
| Different POC windows | Adoption/trust trajectory | Compare only with caveats or normalize by duration. |
| Different historical inventory depth | P1 historical replay | Note inventory depth/quality with the P1 result. |
| Different S-probe subsets | AWS/serverless domain assessment | Use the fixed core S-probes unless the same optional subset was run. |
| Harmful finding severity | Aggregate false-positive rate | Include harmful false positives in the false-positive rate and also report them separately because severity matters more than denominator math. |
| Scorer familiarity with probes | Scoring consistency | Score against the locked expected findings (Section 7.5); use a second scorer where Section 7.5 requires one. |
| Snyk overlap | AWS, security and secrets probes | Score added signal beyond Snyk per the DPT scoring split (Section 6.1). |
| Atlassian-native integration | A4, E2 | Report as environmental fit, not general superiority (Section 7). |
| Configured-rule translation | R1-R6 | Use the locked tool-independent profile, defined context, and the configuration budget (Sections 3.1b and 8.7). |

---

## 18. Per-Platform Results

Do not reduce results to a total numeric score. Report gate status, probe outcomes, domain and platform probe outcomes, evidence quality, harmful findings, and effort spent.

### 18.1 Per-platform results table (one table per platform)

Report results **within one platform**. Use one table for TPS, one for Payment Central, one for Informatica ETL.

| Category | Result | Interpretation |
|---|---|---|
| Mandatory gates | Pass / fail / exception | Stop if required gates fail. |
| P1 Historical defect/rework replay | Green/yellow/red/not comparable | Same inventory on this platform. |
| P2 Full-repo-context-dependent finding | Green/yellow/red | Must find something diff-only review would miss. |
| P3 Spec conformance/spec-gap/spec clarification | Green/yellow/red/NA | NA where no spec exists. |
| P4 AWS/CDK/serverless risk | Green/yellow/red/NA | NA where no AWS is deployed. |
| P5 Hallucinated dependency | Green/yellow/red | Critical for AI-generated code. |
| P6 Origin classification | Green/yellow/red | Critical for brownfield repos. |
| P7 Not-assessable honesty | Green/yellow/red | Critical for trust. |
| P8 Noise floor | Green/yellow/red | Critical for adoption. |
| P9 Determinism | Green/yellow/red | Critical for reproducibility. |
| P10 Structured finding quality | Green/yellow/red | Required for reporting and agent loop. |
| P11 Change-risk test adequacy | Green/yellow/red | Missing scenarios, not test execution or coverage thresholds. |
| P12 Concurrency and atomicity | Green/yellow/red | General race and atomicity reasoning. |
| P13 Failure handling and diagnosability | Green/yellow/red | Boundary handling must preserve retry/DLQ visibility. |
| A4 Cross-source context / E2 External context | Green/yellow/red | Environmental fit; see disclosure in Section 7. |
| Domain-mandatory probes | Green/yellow/red/NA | Per Section 8.1. |
| Platform-specific probes (PC/IN) | Green/yellow/red/NA | This platform only. |
| Configured-rule probes R1-R6 | Green/yellow/red/NA | Separate configured round using the locked profile. |
| Harmful findings | None / near miss / acted on | A single harmful finding may change the decision. |
| Independent evidence quality | Strong/weak/missing | Vendor telemetry cannot be load-bearing. |
| Effort spent | Person-days | Required for fair interpretation. |
| Outcome on this platform | Per Section 19 | Evidence-based decision. |

### 18.2 DPT summary

| Platform | Outcome |
|---|---|
| TPS | Outcome |
| Payment Central | Outcome |
| Informatica ETL | Outcome |

The summary shows the per-platform outcome only. It is read per platform, never averaged across platforms.

---

## 19. Decision Outcomes

Outcomes are decided **per platform**.

| Outcome | Meaning |
|---|---|
| Ready to pilot now | Passed mandatory gates and meets the entry rules below. |
| Fix named blockers, then pilot | Useful, but needs specific, named fixes first: configuration, rule tuning, context integration, data-handling clarification, harmful-finding mitigation, or limited-scope controls. Each blocker is listed. |
| Limited use only | Useful for summaries or low-risk assistance, but not trusted for quality, security, domain, or spec review. |
| Do not proceed | Fails workflow/security gates, produces too much noise, creates harmful findings, lacks context, or creates governance risk. |

**Entry rules** (confirmed by DPT, 2026-10-01; fixed before any tool runs). Probe ratings per Section 7.1.

| Outcome | Requires |
|---|---|
| Ready to pilot now | All mandatory gates pass. No acted-on harmful finding. P5, P6 and P7 Green. No Red on any other required, applicable domain, configured-rule, or platform probe. |
| Fix named blockers, then pilot | Every mandatory gate passes, including any gate re-run after its fix. No acted-on harmful finding. Every Red is tied to a named fix (configuration, rules, context), and that probe is re-run after the fix before the pilot starts. |
| Limited use only | Gates pass. Red on P5, P6, P7, or an applicable domain probe with no named fix, but P8 and P10 Green or Yellow. |
| Do not proceed | A gate fails with no fix; or an acted-on harmful finding on a payment, contract, security-sensitive, or irreversible-action path; or P8 Red. |

NA cells count neither for nor against an outcome; the outcome lists which cells were NA. Any exception to these rules is approved by the Week 1 decision owner, recorded with its reason, and reported to ARC.

**Remediation runs.** A re-run after a named fix is a separate record. It uses the same locked probe asset and the same scoring process, with the configuration change written as a new version of the tool's manifest (Section 3.1b) and its extra effort recorded separately.

- The original frozen-configuration results govern the platform outcome.
- The remediation run governs only whether the named blocker is closed. It closes when the re-run reaches the rating "Ready to pilot now" requires for that probe: Green for P5, P6 and P7, not Red for any other probe.

---

## 20. Appendix A - Phase 0 Record Template

Filed as `review-practice/<platform>/`. Field definitions are in Sections 5.2 and 5.7. Every numeric field needs a source; `not available` with a reason is acceptable, an estimate presented as a measurement is not.

### Scope and setup (Section 5.7)

| Field | Value |
|---|---|
| Platform | TPS / Payment Central / Informatica ETL |
| Team | |
| Repositories in scope | |
| Why these repositories | |
| Probe families each is expected to host | |
| Considered and excluded, with reason | |
| Probe families with no home in this scope | *(reported as not tested, Section 3.2)* |
| Context policy per round | *(what the tool is given or denied; recorded in the manifest, Section 3.1b)* |
| Baseline window start / end (UTC) | |
| Tool enabled on this platform on | *(must be after the window end)* |
| Captured by | |

### Review practice (Section 5.2)

| Field | Value | Source |
|---|---|---|
| Average / median comments per PR | | |
| Average / median time to first human review | | |
| Average / median time to merge | | |
| Average number of reviewers per PR | | |
| Senior/principal reviewer involvement | | |
| Escaped defects or rework examples | | |
| Current CI gates | | |
| Current static/security scans | | |
| Current CDK/IaC checks | | |
| PRs linked to specs/stories/acceptance criteria | | |
| Is P3 testable on this platform, or does P7 apply instead | | |

### Attachments

| Artefact | Section | Present |
|---|---|---|
| Review-catch profile and candidate probes | 5.3 | |
| Historical defect/rework inventory | 5.4 | |
| Assignment and readiness record | 5.7 | |
| Raw exports the numbers came from | 5.2 | |

---

## 21. Appendix B - Evidence Log Template

| Field | Value |
|---|---|
| Platform | TPS / Payment Central / Informatica ETL |
| Team | |
| Tool | |
| Tool version / model (where known) | |
| Date | |
| Evaluator | |
| Repo | |
| PR / branch / commit | |
| Probe ID | |
| Evaluation mode | Native / configured |
| Rule-profile entry | Required for configured R probes; otherwise NA |
| Configuration manifest | Frozen manifest used for this run |
| Probe category | Required / domain-mandatory / configured-rule / platform-specific / extended / aspirational |
| Expected issue | |
| Tool finding | |
| Score | 0 / 1 / 2 / 3 / NA |
| Origin classification | INTRODUCED / PRE-EXISTING / EXPOSED / UNDETERMINED / NA |
| Severity assigned by tool | |
| Severity assigned by evaluator | |
| Actionability tag | Actionable / partially actionable / false positive / harmful false positive / duplicate / nit / not assessable |
| Harmful finding? | No / Yes / Near miss |
| Harmful finding notes | |
| Evidence link / screenshot / export | |
| Vendor telemetry used? | |
| Independent verification performed? | |
| Notes | |
| Final interpretation | Green / yellow / red / not tested |

---

## 22. Appendix C - End-of-Evaluation Retrospective

There is no reviewer survey before enablement. What reviewers catch is derived from the PR comment history instead (Section 5.3): a recollection of what one catches is not evidence from the code, and the comment history is.

This appendix is a retrospective agenda for the end of the evaluation, not an instrument. Most of what a post-evaluation survey would ask is already measured: actionability, noise and harmful findings come from the comment classification in Section 15, and acted-on and dismissal behaviour from Section 12.

Discuss and record:

1. Did the tool catch anything valuable before a human reviewer did?
2. Which findings should become house rules?
3. Which findings should be suppressed or deprioritized?
4. Did trust in the tool increase, decrease, or hold over the window?

Question 4 is the one signal in Section 12 that no measurement produces, because it is an opinion over time. Ask it once, here. If the retrospective is not held, the trust trajectory row is recorded as **not measured** rather than omitted (Section 3.2).

---

## 23. Appendix D - Severity Calibration Guidance

Severity must be calibrated by context.

| Situation | Likely Severity |
|---|---|
| Missing retry handling in a test helper | Low |
| Missing retry/idempotency in payment posting path | High |
| Logging payment token/card metadata | Critical |
| Wildcard IAM in a sandbox spike | Medium |
| Wildcard IAM in deployable production CDK | High or critical |
| Missing alarm on non-critical internal tool | Medium |
| Missing alarm on payment processing failure path | High |
| Breaking event schema with no versioning | High |
| Irreversible payment action without human approval | Critical |
| Harmful false recommendation that weakens payment idempotency | Critical |
| Harmful false recommendation that changes non-critical test-only behavior | Low to medium |

A tool that cannot calibrate severity by context may over-block low-risk work and under-block high-risk work.

---

## 24. Appendix E - Platform Question List (Payment Central, Informatica ETL)

Answered by the platform lead during Phase 0, before probes are written. Answers go in the platform's baseline record.

**Both platforms**

1. Which Bitbucket Cloud repositories are in scope, and roughly how large is each (files, lines)?
2. How are changes reviewed today: PRs in Bitbucket, another process, or both? Who reviews?
3. Which languages, frameworks and versions are in the code under review?
4. What automated checks already run on PRs (build, tests, Snyk, other static analysis)?
5. What are the most common defect types found in QA, production or rework over the last year? Name 3-5 real examples if possible (these seed P1 and the platform probes).
6. Which code paths touch payment data, money movement, or irreversible actions?
7. Do specs, design docs or acceptance criteria exist for changes? Where do they live (Jira, Confluence, other)?
8. Any constraints on what code or data may be sent to an external tool beyond the accepted POC risk (for example, embedded credentials, customer data in test fixtures)?
9. How many PRs per month, and how many engineers would take part in Phase 4?

**Informatica ETL additionally**

10. Which product and deployment: PowerCenter (on-premise) or IDMC (cloud)?
11. What exactly is committed to Bitbucket: exported mapping/workflow XML, parameter files, SQL, shell scripts, other?
12. Do Informatica changes go through Bitbucket PRs today, and are the committed artifacts human-readable enough for a reviewer to assess?

**Payment Central additionally**

13. Build system and test coverage (Maven/Gradle; unit vs integration tests)?
14. Which modules are the highest-risk or most-changed?

If the answer to question 12 is no, the Informatica row is recorded as "not reviewable by this tool category" (Section 6, G1 note) and no further Informatica probes are built.

---

## 25. Appendix F - Business Case (separate from the evaluation)

A directional business case may be attached to the decision submission, clearly separated from probe evidence.

- It must be built only from Phase 0 review-practice data measured on DPT repositories during this evaluation, combined with observed Phase 4 signals.
- It must not use cycle-time or productivity figures from earlier POCs or vendor material.
- It states ranges, not point estimates, and names its assumptions.
- It never feeds back into the probe evidence or the platform outcome.
