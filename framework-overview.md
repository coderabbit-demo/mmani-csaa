# AI Code-Review Evaluation Framework — Overview

**Authoritative documents:** `runbook.md` (rules) and `framework.md` (decision model). Where this page and those differ, they win. The package version is recorded in both.

## What this framework is

It is a fair, repeatable test kit for an AI code-review tool. It tells you, with evidence, whether the tool is good enough to trust on our code.

It states capability criteria rather than product-specific behaviour, and it refuses to produce a single marketing-style score, because one number hides the things that matter.

## What it gives you

Three things, in order:

1. **Gates — the deal-breakers.** Eight pass/fail checks a tool must clear before it is even worth scoring: works inside Bitbucket the way we work, stays advisory (cannot auto-merge or approve), safe with our data, can see the whole repo not just the diff, and so on. Fail a gate and you stop or get an explicit exception.

2. **Probes — the test questions.** Each probe is one specific thing a good reviewer should do — catch a real bug, stay quiet on a harmless change, admit when it does not have enough context instead of bluffing, spot a payment-specific risk. Every probe has its correct answer written and locked before the tool runs.

3. **A decision, backed by evidence.** The tool gets a plain 0–3 on each probe case, kept with proof. Case scores roll up to a Green / Yellow / Red rating per probe, and those ratings decide one of four outcomes — *ready to pilot now*, *fix named blockers then pilot*, *limited use only*, or *do not proceed* — never a blended number.

## How you use it to evaluate a tool

This is the method, step by step:

1. **Capture a baseline first.** Before switching the tool on, record how review works today (volume, turnaround, reviewer load, past escaped defects). That is what you measure improvement against.

2. **Build the test set from our own code.** Write down what a good reviewer should catch, and lock those answer keys so no one can quietly grade the tool on a curve later. Two kinds of case are used: real past defects replayed at the commit where they existed, and defects deliberately planted in a realistic change. Replaying a real production issue needs a platform that is live in production, so TPS uses planted defects only, while Payment Central and Informatica use both.

3. **Run the gates.** Any deal-breaker fails and you stop here. Cheap, fast, saves wasted effort.

4. **Run the probes and score the tool.** Turn it loose on the locked test cases, score 0–3 against the pre-written answers, and keep the evidence (comments, screenshots, exports).

5. **Run two separate rounds.** One for what it catches out of the box, one for how well it follows our rules once configured. Report them separately — needing heavy tuning to reach useful output is a different proposition from useful output out of the box.

6. **Report within a platform, not across.** TPS, Payment Central, and Informatica are too different to compare directly. The tool runs on every platform, and you judge the results inside each one.

7. **Decide on the whole picture.** Gates, plus what it caught, plus what it missed, plus any confidently-wrong ("harmful") findings, plus how much effort it took. That is the recommendation that goes to the architecture group / ARC.

## The line to close on

This framework turns "can we trust this AI reviewer?" from a gut call into a graded, evidence-based test. Same questions, same locked answers, same scoring, on every platform. Whatever we recommend, anyone in the room can open the evidence and check our work.

## Where to find the full details

For the exact rules, here is where each part is written down in this repository.

**1. Where the gates are defined.** The eight deal-breaker gates, each with how to test it and what makes it fail, are in [`runbook.md` Section 6](runbook.md#6-phase-1---mandatory-gates). A one-line summary is in [`framework.md` Section 8](framework.md#8-mandatory-gates-summary).

**2. Where the probes are defined.** The core probes every platform runs (P1–P13, plus A4 and E2) are in [`runbook.md` Section 7](runbook.md#7-phase-2---required-minimum-probe-pack), summarised in [`framework.md` Section 9](framework.md#9-required-probes-summary). The domain and platform probes (payment, API/contract, agentic, AWS/serverless, and the platform-specific ones) and the configured-rule probes (R1–R6) are in [`runbook.md` Section 8](runbook.md#8-phase-3---domain-mandatory-probes), summarised in [`framework.md` Section 10](framework.md#10-domain-platform-and-configured-rule-probes-summary). The actual probe files and their locked answer keys live in the [`probe-pack/`](probe-pack/) folder — start with [`probe-pack/README.md`](probe-pack/README.md), and copy [`probe-pack/_template-probe.md`](probe-pack/_template-probe.md) for each new probe.

**3. How a probe is run, and where the result goes.** The recipe is the same every time, which is what makes the result defensible:

- A probe freezes an exact PR (a base commit and a probe commit) together with its answer key, written and locked before the tool ever runs.
- The tool reviews that frozen PR.
- A person scores what the tool said against the answer key, 0 to 3, and keeps the proof (the tool's comment, a screenshot, an export). The scale and how scores roll up to a final outcome are in [`runbook.md` Section 7.1](runbook.md#71-probe-scoring-rubric) and [Section 19](runbook.md#19-decision-outcomes).
- The score and its evidence are recorded in the evidence log (template in [`runbook.md` Appendix B](runbook.md#21-appendix-b---evidence-log-template)) and filed in a per-platform folder, `evidence/<platform>/`. The evaluation's scope, setup and before-picture live in `review-practice/<platform>/`. The `probe-pack/` folder holds only the probes and answer keys, never the tool's output, so it can be handed over or reused on its own.

**TPS vs Payment Central vs Informatica (ETL).** The recipe above is identical on all three; what changes is *which* probes apply, because the platforms are very different, and results are always kept and read per platform rather than averaged across them. The exact applicability grid is in [`runbook.md` Section 8.1](runbook.md#81-domain-applicability-by-dpt-platform). In plain terms:

- **TPS** — greenfield, Python on AWS serverless, spec-driven. Runs the widest set: the core probes plus the payment, API/contract, agentic, AWS/serverless, and configured-rule probes.
- **Payment Central** — a legacy Java system with no AWS. Skips the AWS and agentic probes, runs the core probes with the payment and contract probes where they apply, and adds its own platform-specific probes (`PC1`, `PC2`, …). The "is this a newly introduced bug or pre-existing old debt?" probe (P6) matters most here.
- **Informatica (ETL)** — on-premise ETL. Runs the core probes and its own platform-specific probes (`IN1`, `IN2`, …), plus payment probes where the data is payment data. This only applies if Informatica changes actually go through Bitbucket pull requests; if they do not, that platform is recorded as "not reviewable by this tool category" and no further probes are built.
