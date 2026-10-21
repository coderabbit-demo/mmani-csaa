# AI Code Review Tool Evaluation (DPT)

A repeatable, evidence-based evaluation of an AI-assisted PR/code review tool, run
on DPT's own platforms.

## What this is

We decide whether the tool is good enough by testing it on **our own code, against
answers we wrote down first** — not on how a review feels.

The method is one idea repeated:

> Take a real change where we already know what a good review should say. Write that
> answer down and lock it. Let the tool review the change without seeing the answer.
> Compare.

Each such test is a **probe**. Each probe is scored 0-3 against its locked answer.
Scores are never averaged into a single number, and results are read per platform —
TPS, Payment Central and Informatica ETL are too different to compare against each
other.

Before probes are worth running at all, the tool must clear eight **gates** — things
like working inside a normal Bitbucket PR, reading the whole repository rather than
just the diff, and never being able to approve or merge. A failed gate stops the
evaluation.

## How an evaluation runs

```
  1. PICK THE SCOPE ........................ which repos, and why        -> review-practice/
                 |
  2. RECORD THE STARTING POINT ............. how review works today      -> review-practice/
                 |                           what reviewers catch
                 |                           which past defects to replay
                 |
  3. WRITE THE PROBES ...................... the change, the commits,    -> probe-pack/
                 |                           what the tool may see
                 |
                 v
        +=====================================================+
        |  LOCK THE ANSWER KEY                                |
        |  what a good review should say, reviewed and fixed  |
        |  NEVER edited once the tool has produced output     |
        +=====================================================+
                 |
  4. COPY THE CODE OUT ..................... separate sanitized repo
                 |                           no history, no credentials,
                 |                           no prior review reports
                 |                           the tool never sees this repo,
                 |                           so it never sees the answers
                 v
        +-----------------------------------------------------+
        |  8 GATES  -  pass / fail                            |
        |  normal Bitbucket PR · whole repo not just the diff |
        |  can never approve or merge · least privilege       |
        |  data handling in writing · exportable output       |
        |  usable before the PR                               |
        +-----------------------------------------------------+
                 |                              \
             all pass                        any fail
                 |                                \
                 v                                 v
  5. THE TOOL REVIEWS THE PR, BLIND          STOP or escalate
                 |                           for exception review
                 v
  6. COMPARE AND SCORE 0-3 ................. 0  missed, or wrong advice  -> evidence/
                 |                           1  close, not the real risk
                 |                           2  real issue, right fix
                 |                           3  issue + impact + fix
                 |
                 |   nobody scores a probe they wrote
                 |   scores are never averaged into one number
                 v
  7. DECIDE, PER PLATFORM .................. Ready to pilot now
                                             Fix named blockers, then pilot
                                             Limited use only
                                             Do not proceed
```

The comparison lives in three places: `probe-pack/` holds what **should** be found,
`evidence/` holds what the tool **did** find, and `review-practice/` is what shows the
test itself was fair. The probe ID joins the first two, so the expectation and the
result can always be read side by side.

Two rules carry the most weight: **the answer key is locked before the tool sees the
code**, and **nobody scores a probe they wrote**. The mechanics of each step are in
`runbook.md` — scope and execution model in §5.7, gates in §6, scoring in §7.1,
evidence in §14, outcomes in §19.

## The folders

| Folder | Purpose |
|---|---|
| `probe-pack/` | One file per probe: the scenario, the frozen commits, and the locked answer key. **This is the bar the tool is measured against.** Never tool output. |
| `review-practice/<platform>/` | What the evaluation covers and why, plus how review works on the platform today. This is what shows the test was fair. |
| `evidence/<platform>/` | What the tool actually produced, scored against the answer keys, with the proof. Plus the gate results. |
| `configuration/` | The rule profile, written in our own terms, for the round that tests configured organizational rules separately from the tool's own ability. |

Platform folder names: `tps`, `payment-central`, `informatica-etl`.

## Where to start

| If you are | Read |
|---|---|
| New to this and want the plain-English version | `framework-overview.md` |
| Running the evaluation on your platform | `probe-pack/README.md` §2 for the sequence, then `review-practice/README.md` and `evidence/README.md` |
| Writing probes | `probe-pack/README.md`, then copy `probe-pack/_template-probe.md` |
| Looking for the exact rules | `runbook.md` |
| A leader or architect | `framework.md` |

`runbook.md` owns execution mechanics — gates, probe definitions, scoring, evidence,
effort, ownership. `framework.md` owns intent, principles and scope. If the two
conflict, use `framework.md` for decision principles and `runbook.md` for mechanics.
`CHANGELOG.md` records what changed between versions.

## Terms

| Term | Meaning |
|---|---|
| DPT | Digital Payment Transformation — the organization running this evaluation and owning its core (`runbook.md` §4) |
| TPS | The Payment System — the greenfield platform in scope: Python microservices on AWS serverless, spec-driven |
| EA | Enterprise Architecture |
| ARC | Architecture Review Council — the final decision forum the recommendation routes to (`runbook.md` §4) |
| POC | Proof of concept — the bounded evaluation window (`runbook.md` §2) |
| Probe | One test case built from our own code where the correct answer is known and locked in advance |
| Answer key | The expected finding for a probe, locked before the tool runs (`runbook.md` §7.5) |
| Gate | A pass/fail precondition the tool must clear before probes are worth running (`runbook.md` §6) |
| AI-DLC | The target direction: review that happens before the pull request and inside agent workflows, not only as PR comment automation (`framework.md` §8) |
| PCI | Payment Card Industry; PCI DSS is its data-security standard |

Ownership is assigned in `runbook.md` §4. Do not change the shared core (gates, core
probes, scoring rubric); propose changes to the DPT core owner.
