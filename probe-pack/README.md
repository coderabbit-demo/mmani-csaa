# Probe Pack: Developer Guide

Read this page and you can start. The runbook (`../runbook.md`) owns the rules; this page tells you how to apply them. Where the two disagree, the runbook wins, and please tell the DPT core owner.

---

## 1. What this is

DPT evaluates an AI code-review tool on evidence from our own code.

A **probe** is a test case built from our own code where **we already know the right answer**. Typical example: a PR that merged cleanly and later caused a defect. Would the tool have caught it?

The **probe pack** is the full set of probes. The tool is run against these probes, and the expected answer for each probe is written down and locked **before the tool runs**. That is what makes the result a fair, defensible assessment of the tool on our code.

- **Core probes (P1-P13, A4, E2)** are owned by DPT and run on every platform.
- **Domain and platform probes** come from platform risks and real defect classes.
- **Configured-rule probes (R1-R6)** test a locked organizational rule profile in a separate configured round.

## 2. What is expected of you

| # | Step | Done when | Runbook |
|---|---|---|---|
| 1 | **Find real past defects.** PRs on your repos that merged cleanly and later caused a defect, incident, QA escape or rework. Aim for 5-10; 3 is the minimum. Replaying a real production issue needs a platform that is live in production, so this step applies to Payment Central and Informatica. | You have a list of PRs with the fix commit for each. | §5.4, §5.6 |
| 1a | **Or build seeded-defect PRs.** Use this where step 1 cannot be met — TPS (not live in production), fewer than 3 usable historical defects, a missing base commit, or a fix that cannot be kept out of the tool's view. Plant defects at the L1-L5 depths inside a realistic change, with a decoy and a control PR. | Seeded PRs exist with a failing-test proof per plant, and P1 is labelled "seeded probes only". | §5.4, §5.6 |
| 2 | **Write each one up as a probe** using `_template-probe.md`. One file per probe. | Every field filled in, including bad signal. | §7.2, §8.6 |
| 3 | **Write the expected finding (answer key)** for every probe your platform will run, including the core probes. | A stranger could score a tool's output against it without asking you anything. | §7.5 |
| 4 | **Get DPT review, then lock.** Set `status: locked` and commit. | Committed before the tool is enabled on your platform. | §7.5 |
| 5 | **Record the Phase 0 setup** and how reviews work today, into `../review-practice/<platform>/`. | Appendix A filled in, before the tool is enabled. | §5, §5.7, App. A |
| 6 | **Run the tool, log what it found, score it** against the locked key. | One evidence log row per probe. | §7.1, App. B |

Platform leads and their platforms are listed in runbook §4. The Payment Central and Informatica leads also answer the Appendix E questions first.

## 3. Rules you cannot break

1. **Never edit an answer key after any tool has produced output.** If a probe turns out to be flawed, mark it `flawed` with the reason. It is then excluded from the evaluation. It is never rewritten.
2. **The tool gets a fixed set of probes, frozen commits, and defined access.** The tool reviews a copy of the frozen branches in a separate sanitized evaluation repository (§5.5).
3. **Don't change the core.** Gates, core probes, and the scoring rubric belong to DPT. Propose changes to the DPT core owner; don't fork them.
4. **Not applicable is not failed.** If a probe's subject doesn't exist on your platform (P4 with no AWS, P3 with no spec, E2 with no linked ticket), record `NA` and the reason. Never score it 0.
5. **Don't score a probe you wrote** where it can be avoided. P1, P5, P6, P7, any Red, and any harmful finding also get a second scorer from another DPT platform (§7.5).
6. **No composite scores.** Don't average or add probe scores into one number.
7. **Your platform probes are reported for your platform only.** Never compared across platforms.

---

## 4. Anatomy of a probe

Every probe file has these parts (copy `_template-probe.md`):

| Part | What it says | Why it matters |
|---|---|---|
| **ID** | `P1-TPS-03`, `R4-TPS-01`, `PC2`, `IN4` | Stable reference in the evidence log. |
| **Evaluation mode** | `native` or `configured` | Prevents configured rule results being blended into native capability. |
| **Rule profile** | Rule-profile path and entry ID for R probes | Proves the tool was tested against the locked tool-independent rule. |
| **Setup** | Repo, base commit, probe commit, what the PR contains, what context is or isn't available | The tool must see exactly the defined setup. |
| **Expected finding** | What the issue is, where (file + function/line), why it matters, what a good review would recommend | The answer key. Scoring is impossible without it. |
| **Good signal** | What a score of 2-3 looks like | Lets the second scorer agree with you. |
| **Bad signal** | What a score of 0-1 looks like, including the plausible-but-wrong answer | Stops "it said something about that file" being scored as a catch. |
| **Origin** | INTRODUCED / PRE-EXISTING / EXPOSED / UNDETERMINED | Needed for P6 and every brownfield probe. |
| **Applicability** | Which platforms, or NA and why | Rule 4. |
| **Status** | `draft` -> `reviewed` -> `locked` (or `flawed`) | Rule 1. |

---

## 5. Good vs bad probes: examples

### Example 1: historical defect replay (P1, TPS)

Based on a real fix: `csaa-tps-disbursement-ingest-service` commit `6841ac3` (2026-09-04). Illustrative only, not yet a locked probe; the TPS team confirms it.

**Bad probe**

> **Setup:** Ingest service, the replay code.
> **Expected finding:** Tool should find the checkNumber bug.

Why it's bad: no commit, so tools may see different code. "The checkNumber bug" only means something to the person who fixed it. A scorer can't tell a catch from a near miss. No bad signal, so a vague comment about the response model gets scored as a catch.

**Good probe**

> **ID:** P1-TPS-01
> **Setup:** Repo `csaa-tps-disbursement-ingest-service`. Probe PR = the change that introduced the idempotent replay-202 path (base = its parent commit). Fix reference: `6841ac3`. Tool has full repo access; no spec access needed.
> **Expected finding:** On a duplicate request, the replay-202 branch in `app/controllers/ingest_controller.py` (`create_disbursement`) builds a `CreateDisbursementResponse`, which requires `checkNumber`. The duplicate result `DuplicateConflict` (`app/schemas/outer_api/disbursement_response.py`) does not carry a check number, so the replay raises a pydantic validation error and the caller gets a **500 instead of the 202**. A good review says the required field has no source on the duplicate path and recommends carrying `check_number` through from the existing record, without changing the 409 body.
> **Good signal (2-3):** Names the missing required field on the replay path and the resulting 500. A 3 also explains the idempotency impact (a client retry fails), and suggests carrying the field without changing the 409 contract.
> **Bad signal (0-1):** "Consider adding validation to the response model." "Add more tests for idempotency." Flags style in the controller. Suggests making `checkNumber` optional in the 202 response (that breaks the API contract: a harmful recommendation if acted on).
> **Origin:** INTRODUCED.
> **Applicability:** TPS.

Notice the good version names a **plausible but harmful** fix as a bad signal. Write those down whenever you can think of one; they are how harmful findings get caught.

### Example 2: the answer key itself

| | Expected finding |
|---|---|
| **Bad** | "Possible null issue in the payment mapper." |
| **Bad** | "Should catch the bug we had in March." |
| **Good** | "`PaymentMapper.toLedgerEntry()` (`src/main/java/.../PaymentMapper.java`, ~line 140) reads `payee.getAccount().getRoutingNo()` without a null check. Payees created before 2019 have no account record, so this throws NPE and the batch stops at that row (incident INC-xxxx). A good review flags the unguarded chain, notes the legacy-data condition, and recommends a guard plus a test with a pre-2019 payee." |

Test: **could someone who has never seen this code score a tool's comment against it, without asking you?** If not, it isn't finished.

### Example 3: noise floor (P8)

| | Probe |
|---|---|
| **Bad** | A "small refactor" PR that renames a variable *and* reorders two calls. Not noise-only: the reorder could be a real change, so a tool flagging it is right, and the probe can't be scored. |
| **Good** | A PR that only runs the formatter (`black` / the IDE formatter) over three files. Expected finding: **no comments, or nits only.** Bad signal: any comment claiming a behaviour or risk change. |

A noise probe must have **zero** semantic change. Check the diff yourself.

### Example 4: honesty (P7)

| | Probe |
|---|---|
| **Bad** | Withhold the spec, then score the tool down for "missing spec violations". You've tested whether it can read something it was never given. |
| **Good** | A PR changing a validation rule where the rule's source (spec or ticket) is **not available to the tool**. Expected finding: the tool says it **cannot confirm** the rule is correct and names what's missing ("no acceptance criteria available for this field"). Bad signal: confidently asserts the rule is right or wrong. |

Valid "can't assess" answers are listed in runbook §7.4. A tool that admits it can't judge scores well here; false confidence is a serious negative.

### Example 5: brownfield origin (P6, Payment Central)

| | Probe |
|---|---|
| **Bad** | A PR touching a 4,000-line legacy class, expected finding "should not report old issues". Too vague: which old issues? |
| **Good** | A PR that adds one method to `LegacyBatchProcessor.java`. The class already has two known issues (a swallowed exception in `run()`, a static mutable cache). The new method calls `run()`. **Expected:** swallowed exception = EXPOSED (the new caller now depends on it); static cache = PRE-EXISTING; nothing INTRODUCED unless the new method adds its own issue. Bad signal: reports both old issues as if the PR introduced them. |

On a legacy codebase this is often the probe that decides whether a tool is usable at all.

### Example 6: platform probe (IN, Informatica ETL)

| | Probe |
|---|---|
| **Bad** | `IN1`: "Check the tool understands Informatica." Not a defect, not scorable. |
| **Good** | `IN1`: A mapping change that switches a target load from update-else-insert to insert-only. Rerunning the workflow after a partial failure now duplicates rows (seen in INC-xxxx). Expected finding: the change breaks rerun safety; recommends restoring the upsert or adding a dedupe key. Bad signal: comments only on naming or transformation layout. |

Only applies if Informatica changes are reviewed in Bitbucket PRs (Appendix E). If they aren't, the Informatica row is recorded as "not reviewable by this tool category" and no IN probes are built.

### Example 7: seeded-defect PR (when an old PR can't be replayed)

Take a real base commit and plant defects at different depths (runbook §5.4 has the L1-L5 levels).

| | Probe |
|---|---|
| **Bad** | One-line diff that adds `if amount < 0: pass  # TODO` to a handler. The defect is the only change, the comment points at it, and it will obviously be flagged. Measures nothing. |
| **Good** | A ~250-line change that adds a reissue endpoint to the cancel service. Inside it: an L3 inverted status check, an L4 `payee_name` length of 120 where the column is 80, an L5 reissue that creates a new disbursement on retry instead of returning the existing one. Plus one decoy: a broad `except Exception` that re-raises after logging, which is correct here. Neutral commit message. Each L3-L5 plant has a test that fails on the seeded branch. Expected findings list all three plants and the decoy; flagging the decoy counts as a false alarm. |

Build one control PR with no plants alongside. Label P1 for the platform "seeded probes only".

### Example 8: configured organizational rule (R6)

> - **ID:** R6-PLATFORM-01
> - **Mode:** configured
> - **Rule-profile entry:** `CFG-01` — operational endpoints must come from an environment variable or approved configuration source.
> - **Setup:** A PR adds an environment-specific service endpoint literal inside application logic. The tool receives the translated locked rule.
> - **Expected finding:** Identifies the hardcoded operational endpoint and recommends the approved configuration path.
> - **Bad signal:** Generic maintainability advice, an invented platform rule, or a miss.

Report this result in the configured R-set, not as evidence of native capability.

---

## 6. Scoring a tool's output against the key

Using Example 1. The tool reviews the probe PR and says:

| Tool says | Score | Why |
|---|---|---|
| Nothing about the replay path | **0** | Missed. |
| "Make `checkNumber` optional in `CreateDisbursementResponse`." | **0**, harmful candidate | Wrong advice that breaks the contract if acted on. Mark `Harmful finding: Near miss` or `Yes`. |
| "The duplicate handling here may need more tests." | **1** | Nearby, but not the actual risk. |
| "`checkNumber` is required in the 202 response but `DuplicateConflict` doesn't carry it; replay will fail validation." | **2** | Real issue, mostly correct guidance. |
| The above, plus "this becomes a 500 on client retry, so idempotent replay is broken; carry the value from the existing record and exclude it when None to keep the 409 body unchanged." | **3** | Issue, impact, correct context, actionable fix. |
| "I can't assess this without the response contract." (when the contract *was* available) | **0** | Not-assessable is only valid when the context was genuinely missing. |

Case scores roll up to Green / Yellow / Red per runbook §7.1. Record every row in the evidence log (Appendix B), with a link to the tool's actual comment.

---

## 7. Where things go

```
probe-pack/
  README.md                      this page
  _template-probe.md             copy this for every probe
  p01-historical-defect-replay/  P1-<PLATFORM>-NN.md   e.g. P1-TPS-01.md, P1-PC-01.md
  p02-full-repo-context/ ... p13-failure-handling-diagnosability/   same naming: P<n>-<PLATFORM>-NN.md
  domain-payment/  domain-contract/  domain-agentic/  aws-serverless/   domain probes (runbook §8.2-8.5)
  configured-rule-conformance/   R<n>-<PLATFORM>-NN.md (runbook §8.7)
  platform-payment-central/      PC1.md, PC2.md ...
  platform-informatica/          IN1.md, IN2.md ...
```

Platform codes: `TPS`, `PC` (Payment Central), `IN` (Informatica ETL).

A folder holding only `.gitkeep` is a reserved slot that no probe has been written into yet. Add probe files to it rather than creating a new folder.

Tool results do **not** go here. They go in `../evidence/<platform>/`. This folder holds probes and answer keys only, so it can be handed over or reused without carrying tool output.

**Frozen commits.** Record the full commit SHA for base and probe in the probe file. The tool reviews a PR built from those same two commits. Don't rebase or amend them.

---

## 8. Before you lock: checklist

- [ ] Base and probe commit SHAs are recorded and the PR can be recreated from them.
- [ ] The expected finding names the file and function, the issue, why it matters, and the right fix.
- [ ] A stranger could score against it without asking you.
- [ ] Bad signal includes at least one plausible-but-wrong answer.
- [ ] Origin is set (for P6 and every brownfield probe).
- [ ] Applicability is set; anything NA has a reason.
- [ ] Evaluation mode is set; configured probes reference a locked rule-profile entry and frozen manifest.
- [ ] No tool has seen this probe yet.
- [ ] DPT has reviewed it.
- [ ] `status: locked`, committed.

---

## 9. FAQ

**How much time will this take me?** Building probes and answer keys is a one-time cost per platform. Running and scoring repeat each run. Your platform lead has the estimate (runbook §3.1).

**We don't have 3 past defects that fit, or the old PR can't be recreated.** Build seeded-defect PRs instead (Example 7, runbook §5.4) and label P1 "seeded probes only". Don't substitute unrelated PRs.

**My code has no spec or no Jira link.** P3 / E2 are NA for those changes. For P3, run P7 on the same change instead (§7).

**Can I add my own probes?** Yes. Platform probes count for your platform only. Rules shared through configuration use R1-R6 and must reference a locked rule-profile entry.

**A probe turned out to be wrong after the tool ran.** Mark it `flawed` with the reason. It's excluded from the evaluation. Don't fix it in place.

**I found a real bug in our code while building a probe.** Raise it through your normal process. The probe stays as a probe.

**Who do I ask?** Your platform lead first, then the DPT core owner (Amit Mishra).

## 10. Where the rules live

| Topic | Runbook section |
|---|---|
| Platform rules | §1.1 |
| Historical defect inventory | §5.4 |
| Core probes, scoring rubric, roll-up to Green/Yellow/Red | §7, §7.1, §7.2 |
| Origin classes, valid "can't assess" answers | §7.3, §7.4 |
| Answer key, locking, second scorer, readiness gate | §7.5 |
| Domain and platform probes | §8.1-8.6 |
| Configured organizational-rule probes | §8.7 |
| Live-use separation, frozen branches | §12.1 |
| Templates: Phase 0 record, evidence log, retrospective | Appendix A, B, C |
| Questions for Payment Central / Informatica | Appendix E |
