# AI Code Review Tool Evaluation Framework

**Document pair:** AI Code Review Tool Evaluation Package  
**Package version:** v2.5-draft
**Date:** 2026-10-07
**Status:** Draft for DPT execution and Enterprise Architecture / leadership review (incorporates EA review, 2026-09-16)  
**Audience:** Enterprise Architecture, engineering leadership, DPT platform leads, and evaluation sponsors  
**Companion document:** `runbook.md` (same package version)

---

## Document Authority

This framework and the companion runbook are intended to be used as a matched pair.

- **Framework authority:** evaluation intent, decision principles, scope, leadership alignment, and strategic constraints.
- **Runbook authority:** execution detail, probe definitions, evidence capture, effort model, ownership, configuration guidance, calibration bands, decision-outcome entry rules, and operating process.
- **Conflict rule:** if the two documents conflict, use the Framework for decision principles and the Runbook for execution mechanics.

Execution ownership is assigned in runbook Section 4.

---

## 1. Executive Summary

We are evaluating an AI-assisted PR/code review tool to determine whether it can improve engineering review quality, reduce senior reviewer load, and preserve engineering standards in a regulated enterprise environment.

This framework states capability criteria rather than product-specific behaviour. DPT uses it to evaluate an AI PR/code review tool across its own platforms — TPS (greenfield, Python AWS serverless), Payment Central (legacy Java monolith) and Informatica ETL.

The goal is **not** to reward the tool that writes the most comments. The goal is to determine whether the tool can:

- Work naturally in Bitbucket Cloud
- Operate safely as an advisory reviewer
- Preserve human approval and merge authority
- Use full repository and specification context
- Detect meaningful engineering, AWS/serverless, and domain risks
- Reduce reviewer burden without lowering standards
- Produce evidence of how the tool performs on each DPT platform
- Avoid creating new risk through harmful or confidently wrong recommendations

This framework intentionally avoids fake composite scoring. Teams must not multiply probe scores and weights into a single number such as "84.7." The decision must be based on mandatory gates, native-capability evidence, separately reported configured-rule evidence, domain-specific evidence, harmful-finding evidence, effort spent, and clearly documented risk.

---

## 2. Why This Evaluation Matters

AI-generated code is increasing the volume and complexity of code review. In a spec-driven development model, the reviewer is not only checking syntax or style. The reviewer must validate whether the implementation preserves intent, architecture, security, operability, and domain correctness.

For our environment, a useful AI PR/code review tool must help detect risks such as:

- Code that passes tests but violates acceptance criteria
- Missing or ambiguous specifications that need clarification
- Invented methods, nonexistent SDK calls, or missing dependencies
- AWS/CDK/serverless misconfigurations
- Weak observability, retry, timeout, or failure handling
- Payment-domain errors such as duplicate payment risk or weak idempotency
- Sensitive payment/token/card metadata handling issues
- Breaking OpenAPI or event contracts
- Brownfield findings incorrectly presented as newly introduced defects
- Tool hallucination or false confidence when required context is unavailable
- Harmful false positives that could cause engineers to make a bad change

The evaluation should answer one question:

> Can this tool improve code review quality and reduce senior reviewer burden without weakening engineering standards, domain correctness, security posture, or human accountability?

---

## 3. Target Environment

DPT platforms in scope (all in Bitbucket Cloud): TPS, Payment Central, and Informatica ETL. Their profiles, spec adoption, and platform leads are owned by runbook Section 1.1.

This framework assumes:

- Bitbucket Cloud as the enterprise PR platform
- Full repository context available to the review tool
- Python, TypeScript, Java, and infrastructure-as-code among the languages under review
- Engineering intent stored in Bitbucket specs, Jira, Confluence, SharePoint, or other enterprise sources
- Human-owned approval and merge decisions
- Security and data-handling expectations appropriate for regulated enterprise delivery
- Domain-specific engineering concerns, including payment-domain concerns where applicable

AWS serverless architecture and spec-driven development apply to TPS, not to every platform in scope. Probes that depend on them are recorded as NA elsewhere (runbook Sections 7 and 8.1).

---

## 4. Evaluation Scope

### 4.1 In scope

This evaluation applies to an AI-assisted PR/code review tool that can participate in the code review lifecycle.

In scope:

- AI PR review
- AI-assisted code review
- Bitbucket Cloud PR comments and review summaries
- Full repository context
- Specification and acceptance-criteria awareness
- Pre-PR or agent-loop review capability
- Rule-based or learned team standards
- Code quality, security, maintainability, test, and operability review
- AWS/serverless/CDK/IaC review
- Domain-specific review, including payment-domain review
- Machine-consumable review output for reporting and agent workflows

### 4.2 Out of scope

Out of scope for this framework:

- Pure static analysis tools with no AI PR/code review capability
- General chatbot-only tools that do not integrate with PR workflows
- Tools that require repository migration or mirroring to another platform
- Fully autonomous code merge or approval systems
- Functional test-case validation and performance or load validation
- Commercial scoring and contract terms
- Long-term supplier viability

Section 16 states what the evaluation's result does not decide, which is a different question from what the evaluation itself covers.

---

## 5. Evaluation Principles

### 5.1 Capability-based and evidence-based

This framework states capability criteria, not product-specific behaviour, so the evidence stands on its own. Criteria are written in terms of what a reviewer must be able to do, not how any particular implementation does it.

### 5.2 No fake precision

Do not compute a weighted composite score.

A single score can hide unacceptable security gaps, domain failures, hallucinations, weak context integration, harmful findings, or high reviewer noise.

### 5.3 Mandatory gates before evaluation

Some conditions are pass/fail. If a tool cannot satisfy them, the team should stop or request an explicit exception.

Mandatory gate definitions G1-G8 are owned by the runbook.

### 5.4 Common core, reported per platform

Every platform runs the same DPT-owned core: gates G1-G8 and required probes P1-P13, A4 and E2. Platform teams own their execution and may add platform-specific probes, but do not change the core.

Results are reported **within a platform**, never compared across platforms. The tool runs on every platform in scope, and each platform locks its expected findings before the tool runs. Platform rules are owned by runbook Section 1.1.

Required probe definitions are owned by the runbook.

### 5.5 Domain, platform, and configured-rule probes

Some platforms run additional probes because their domain carries specific risks. The required probes run first as the **native-capability round**, with no organizational rules supplied. A separate **configured-rule round** then tests whether the tool can apply locked organizational standards after configuration within the runbook Section 3.1b budget. Native-capability and configured-rule results are never combined. Applicability per platform is owned by runbook Section 8.1; probe definitions by runbook Section 8.

### 5.6 Aspirational capabilities

Aspirational capabilities are future-state differentiators. They should be captured when available, but they are not Day 1 stop conditions unless leadership explicitly makes them mandatory for a given evaluation. The runbook is authoritative for aspirational capability definitions and evidence capture.

### 5.7 Independent evidence

Vendor dashboards and telemetry may support the evaluation, but load-bearing metrics must be independently captured by the evaluation team.

### 5.8 Human accountability remains intact

The tool is an AI-assisted reviewer, not an autonomous approver, merger, or production-change actor. Human engineers remain accountable for accepting, rejecting, or acting on recommendations.

---

## 6. Mandatory Security and Human-Control Boundary

For the POC, the tool must operate as an **AI-assisted review capability only**. It may comment, suggest changes, summarize risk, identify missing tests and likely defects, compare implementation to specifications, and produce structured output for reporting or agent-loop handoff.

It must not approve or merge pull requests, push code without explicit human action, override branch protection, replace required human reviewers, become a deployment gate without separate approval, or take irreversible or production-impacting action without human review.

This boundary is tested as gate G3; the testable gate wording and the full prohibited-action list are owned by runbook Section 6.

---

## 7. Evaluation Model

The evaluation uses six phases plus a mandatory go/no-go checkpoint after the required probes.

| Phase / Checkpoint | Purpose |
|---|---|
| Phase 0 - Evaluation setup | Fix repository scope and capture the before-state, before tool enablement. |
| Phase 1 - Mandatory gates | Confirm the tool can safely participate in the target workflow. |
| Phase 2 - Required minimum probes | Run P1-P13, A4 and E2 in the native-capability round. |
| Go/no-go checkpoint | Decide whether to continue, constrain, pause, or stop. |
| Phase 3 - Domain and configured-rule probes | Run applicable domain probes and the separate configured R1-R6 round. |
| Phase 4 - Adoption and trust | Measure actionability, harmful findings, trust, reviewer load, and sustained usefulness. |
| Phase 5 - Decision review | Review evidence and classify the tool outcome. |

The sequence is: vendor risk clearance, then probe readiness (every probe has a frozen setup and a locked answer key), then Phase 0 setup and review-practice capture, then tool enablement, then Phases 1-5. The evaluation clock starts at tool enablement.

Phase timing and the evaluation clock are owned by runbook Section 2; the baseline window by Section 5; probe definitions by Sections 7 and 8; checkpoint triggers by Section 11; evidence capture and the evidence log by Section 14 and Appendix B; calibration bands by Section 16.

---

## 8. Mandatory Gates Summary

The runbook is authoritative for mandatory gate definitions and execution instructions.

The mandatory gates cover:

- Bitbucket Cloud PR workflow fit
- Advisory-only operation
- Human-control boundary
- Full repository context availability
- Least-privilege permissions
- Data handling clarity
- Machine-consumable output availability
- Pre-PR or agent-loop capability

Pre-PR / agent-loop capability is a deliberate strategic gate. It is included because the target direction is AI-DLC — an AI-assisted development lifecycle in which review happens before the pull request and inside agent workflows, not only as PR comment automation. A tool that is excellent at PR comments but cannot participate in pre-PR or agent-loop workflows may still be useful, but it does not meet the target strategic direction unless an exception is approved by the go/no-go decision owner (runbook Section 4) and escalated to leadership where it changes the strategic direction.

---

## 9. Required Probes Summary

The runbook is authoritative for required probe definitions and execution instructions.

Every platform runs:

| Probe ID | Probe |
|---|---|
| P1 | Historical defect / rework replay |
| P2 | Full-repository-context-dependent finding |
| P3 | Spec conformance, spec-gap classification, and proposed spec clarification (NA where no spec exists) |
| P4 | AWS/CDK/serverless risk detection (NA where no AWS is deployed) |
| P5 | Hallucinated dependency / nonexistent API |
| P6 | Brownfield origin classification |
| P7 | Not-assessable honesty |
| P8 | Noise floor |
| P9 | Determinism |
| P10 | Structured finding quality |
| P11 | Change-risk test adequacy |
| P12 | Concurrency and atomicity |
| P13 | Failure handling and diagnosability |
| A4 | Cross-source context retrieval |
| E2 | External context integration |

A4 and E2 reflect the Atlassian stack DPT works in. Results are reported as fit for the DPT environment, not as a general capability claim.

Not applicable is recorded as NA with the reason, never as a failed score.

A gate asks: **Can the tool do this at all?**  
A probe asks: **Does the tool use that capability to find something meaningful?**

---

## 10. Domain, Platform, and Configured-Rule Probes Summary

Applicability per DPT platform (payment D-set, contract C-set, agentic A-set, core AWS S-set, Payment Central / Informatica platform-specific probes, and configured R1-R6) is owned by runbook Section 8.1. Platform-specific guidance is in runbook Section 8.6; configured-rule guidance is in runbook Section 8.7. The R-set covers delivery pipeline conformity, environment configuration completeness, shared component reuse, observability, API security/boundary standards, and configuration externalization.

---

## 11. Historical Defect / Rework Replay

Historical replay is the strongest executive signal when comparable examples are available. It answers:

> Would this tool have caught anything that actually hurt us?

However, historical replay is not always equally available across teams. Therefore:

- P1 uses the same historical inventory on a given platform.
- Platforms must report how many historical examples were available.
- Teams without sufficient historical inventory use seeded-defect probes (runbook §5.4) and mark P1 "seeded probes only".
- Seeded-defect probes are owned by the probe pack owner.

Initial calibration should use proportions, not absolute counts. Calibration bands are owned by the runbook.

---

## 12. Effort Model Summary

The runbook is authoritative for effort tiers and execution planning.

At a high level:

- Baseline, historical inventory, seeded-defect probes and locked expected findings are built once per platform.
- Gates, probe runs, configuration (about 1 person-day per platform) and adoption measurement are the per-run cost.
- Domain sets stack when more than one applies.
- Optional extended probes should be deferred before skipping required probes.
- Effort spent in person-days is reported on every platform.

TPS runs four domain sets (payment, contract/API, agentic, core AWS/serverless) plus the configured R-set: approximately **23-37 person-days**, plus a 1-person-day configuration budget; one-time setup is reused on any repeat run (runbook §3.1, §3.1a). Payment Central and Informatica ETL effort is set by their platform leads once their platform probes are defined.

---

## 13. Recorded Numbers, Not Scored

Some numbers are captured for context but are not review-quality scores. The list is owned by runbook Section 13.

---

## 14. Aspirational Capabilities

Aspirational capabilities should be captured as future-state differentiators. They are not required for Day 1 adoption unless explicitly elevated by leadership.

The set is AS1-AS8: codebase graph / impact analysis, incident-to-PR correlation, PR conversation intelligence, governance visibility, cross-source context retrieval beyond the implementation repo, agent-loop repair with human approval, organizational standards memory, and structured output for downstream automation.

Definitions, evidence fields, and the AS-probe IDs are owned by runbook Section 10.

---

## 15. Evidence and Decision Model

Each evaluation must produce evidence for mandatory gates, required minimum probes, applicable domain-mandatory probes, separately reported configured-rule probes, harmful findings, adoption/trust signals, and any aspirational capabilities assessed.

Vendor telemetry is supporting evidence only. Load-bearing measurements must be independently captured.

The final decision classifies the tool **on each platform** into one of four outcomes: **Ready to pilot now**, **Fix named blockers, then pilot**, **Limited use only**, or **Do not proceed**.

Case scores roll up to a Green / Yellow / Red rating per probe (runbook Section 7.1), and those ratings decide the outcome. The outcome meanings and the entry rules for each are owned by runbook Section 19. The outcome is decided per platform on the evidence, never by a composite score.

---

## 16. What This Evaluation Does Not Decide

A DPT evaluation result should not be treated as the final answer for:

- Enterprise-wide dashboarding and cross-team reporting
- Centralized data export
- Enterprise RBAC depth
- Enterprise platform standardization
- Final security approval for scaled use

Those require broader architecture, security, commercial, and platform evaluation.

---

## 17. Ownership

Roles, names, and responsibilities are owned by runbook Section 4. In summary: DPT owns the core framework, probe pack, configuration guidance, evidence review and the go/no-go decision; platform leads run the evaluation and own their platform probes; Enterprise Architecture signs off probe-pack coverage and stays attached throughout; the final recommendation routes to ARC.

Open: evaluation sponsor. That cell does not block probe execution (runbook Section 4). Static-analysis scanning (Snyk) is out of scope; runbook Section 6.1 only defines how AI findings in the scanner's territory are scored.

---

## 18. Review Ask for Leaders

Please review and provide feedback on:

1. Is the platform coverage the right shape for the decision you need?
2. Should pre-PR / agent-loop capability remain a strategic gate for all three platforms?
3. Is the effort model realistic, given TPS at roughly 23-37 person-days?
4. Which aspirational capabilities should be tracked as future-state differentiators?

---

## 19. Closing Principle

The tool should help teams review better. It should not create a new source of untrusted noise, hidden autonomy, harmful recommendations, or false confidence.
