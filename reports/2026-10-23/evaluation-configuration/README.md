# CSAA evaluation configuration — October 23, 2026

The single deployable artifact is [`.coderabbit.yaml`](.coderabbit.yaml). It
consolidates the proposed PI library into 11 instruction blocks, adds eight
warning-mode custom pre-merge checks, sets a 218-character tone instruction,
and includes one disabled post-merge report recipe. It is proposed configuration,
not an executed or validated product result. Existing Met ratings are unchanged.

Use it for an approved **configured/remediation round**. It contains semantic
guidance and therefore cannot serve as the unchanged native-capability baseline.
The runbook requires separate frozen manifests and results for those rounds
([runbook §3.1b](../../../runbook.md#31b-configuration-budget-and-evaluation-modes)).
The current [PoV plan spreadsheet](https://docs.google.com/spreadsheets/d/1-8qfMIAybwQ86um90OLOXs79z6yEDkU5/edit)
remains the plan of record; no success criteria or results were changed by this
configuration exercise.

| Feature | Adds value? | Proposed use | Limit that remains |
| --- | --- | --- | --- |
| Pre-merge checks | Yes | Explicit advisory verdicts for required context, contract compatibility, payment replay safety, diagnostic data leaks, IAM scope, async recovery, reproducible builds and meaningful regression assertions. | Evidence-dependent agent judgments; not a deterministic policy engine or executed test suite. |
| Overall tone | Yes | Concise, respectful, evidence-first language with clear uncertainty and actions. Keep the balanced `chill` profile; control P8 with specific guidance. | Tone cannot enforce severity accuracy, recall, origin classification or structured export fields. |
| Post-merge actions | Limited, later | Optional text-only follow-up report on the merged PR. Included with `enabled: false`. | Runs after default-branch merge. Automatic follow-up changes/integrations add effects outside the core advisory evaluation. |

[Custom checks](https://docs.coderabbit.ai/pr-reviews/custom-checks) produce
Passed/Failed/Inconclusive summary results. They cannot run application tests or
builds, inspect reviewer approvals, change the inline review, or post inline
findings. Each proposed check has explicit applicability, failure evidence and
missing-context behavior. Its passing result is scoped to inspected evidence,
not proof of general correctness. Captured results must retain which check or
review mechanism produced them; the same underlying defect is still one finding.

[Tone and profile settings](https://docs.coderabbit.ai/reference/configuration)
control presentation. The tone field has a 250-character limit. `quiet` groups
less-important comments into the summary, which could complicate evaluation of
finding visibility; `assertive` could increase nits. The proposed choice is
`chill`, with specific P8 instructions and declared suppression of unrelated
prose/format analyzers. These are configuration choices to test, not a noise
guarantee.

[Post-merge actions](https://docs.coderabbit.ai/pr-reviews/post-merge-actions)
are documented for Bitbucket Cloud as well as GitHub Cloud, GitLab Cloud and
Azure DevOps. They run after a merge into the default branch and can post text,
open follow-up PRs or use integrations. The disabled recipe requests only a
text report. Its wording does not enforce a permission boundary, establish an
audit export, or replace formal evidence capture. Enable it only in a separately
declared demonstration with suitable permissions and frozen assets preserved.

## Coverage and remaining work

This table maps all 78 assessment IDs to proposed support or work outside YAML.
It does not change their Yes/No/Partial/Maybe/Unknown ratings. Exact original
requirements and assessment remain in the [assessment](../coderabbit-assessment.md)
and [runbook](../../../runbook.md).

| IDs | What must be established | Support in this file | What configuration cannot establish |
| --- | --- | --- | --- |
| G1, G4 | Normal Bitbucket Cloud PR workflow and access beyond the diff. | Manual run controls; instructions to inspect unchanged context; review details. | Actual installation, workflow fit and accessible repository scope need a real approved run. |
| G2, G3 | Advisory operation; human control over approval, merge, code writes and protections. | Automatic approvals off, author approval commands restricted, statuses non-blocking, listed repair features off, post-merge recipe off, integration writes disabled. | Effective provider privileges, protected settings, human reviewer requirements, other agent surfaces and denied-action tests remain mandatory. |
| G5, G6 | Least privilege and written data-handling clarity. | No automatic repository discovery or unconfirmed connectors; no secrets in prompts. | Scopes, standing access, egress, retention, deletion, training and subprocessors require actual permissions evidence and vendor commitments. |
| G7, G8 | Reliable machine output and a pre-PR/agent-loop capability. | Review provenance/detail and bounded AI-agent fix prompts. | A comment-body convention is not a native API schema. API/export and local CLI or agent-loop execution must be demonstrated separately. |
| P1, P2 | Find real causal defects and use relevant context outside changed lines. | Global causal/evidence instructions and domain/runtime guidance. | Detection recall and historical-replay results require locked cases and independent scoring. |
| P3, P7 | Distinguish implementation defects from spec ambiguity or missing context. | Source lifecycle/authority rules and Required specification context check. | Prompts cannot create missing specifications, grant access, or determine evaluator applicability. |
| P4 | Understand actual AWS runtime/IaC behavior. | Conditional AWS guidance and IAM/async checks. | Must inspect correct service/runtime versions and execute the applicable probes. |
| P5 | Avoid invented APIs, symbols, versions and configuration keys. | Version-aware evidence instructions. | Cannot guarantee factual accuracy; supply relevant frozen references and score results. |
| P6 | Separate introduced, pre-existing, exposed and undetermined origin. | Base/head/history origin rubric in the general instructions. | Native origin fields and correct history-based attribution require validation. |
| P8 | Avoid invented risk on non-semantic changes; keep useful optional formatting low priority. | Explicit no-finding default for proved non-semantic changes; retain genuine rename/contract failures; disable unrelated style checks. | Clean controls and actual comment counts determine the result. No prompt guarantees a noise floor. |
| P9 | Stable findings across independent completed reruns. | Consistent impact criteria, manual triggers, fresh repository fetches. | Cache disabling alone is not independent full execution. Freeze context/learnings; record overlap and denominator rules. |
| P10 | Location, severity, category, rationale, origin and action in usable findings. | General finding-content instructions, detailed review context and agent handoff prompts. | Cannot add guaranteed fields to a native JSON/SARIF/export schema. Inspect actual exports. |
| P11 | Specific missing risk-bearing tests. | Runtime/test instructions and Risk-bearing regression assertions check. | Static assertions do not establish passing tests, coverage or execution. |
| P12, P13 | Concrete concurrency failures and correct boundary exception handling. | Interleaving, transaction scope, retry/recovery, propagation and logging guidance. | Requires actual state/runtime context and executable/observable failure cases. |
| A1, A2, A3 | Cross-agent consistency, actionable handoff and context-sensitive severity. | Observable-artifact reasoning, bounded proposed fix/verification and production-versus-tooling impact. | No invented session memory, autonomous repair authorization or guaranteed severity consistency. |
| A4, A5 | Use approved external context and retain rule/source versions. | Source citation/authority rules, isolated linking defaults and documented setup points. | Actual accessible source snapshots and rule retention are owner-managed prerequisites. |
| D1, D2, D3 | Duplicate requests, uncertain outcomes and safe payment state transitions. | Payment/runtime/persistence instructions; Payment replay safety check. | Actual provider contracts, persistence guarantees and state models must be supplied. |
| D4, D5 | Protect sensitive payment data, including diagnostics. | Conditional payment guidance, secret analyzers and Sensitive data in diagnostic output check. | Does not prove tokenization, data classification, access controls or absence of leaks. |
| D6, D7, D8, D9 | Correct financial semantics, operation distinctions, durable audit and bound human authorization. | Payment and migration instructions with explicit evidence requirements. | Approved ledger/lifecycle/authorization policies and observed cases remain necessary. |
| C1, C2, C3, C4, C5 | Direction-aware field, response, enum and event compatibility. | Schema/consumer instructions and Contract compatibility check. | Real contracts, consumers and version coexistence evidence must be accessible. |
| C6, C7, C8 | Safe migrations and request/response validation at internal/external boundaries. | Runtime, contract and persistence instructions. | Requires the deployment sequence, trust topology and matching cases. |
| S1, S5, S8, S10 | Core AWS privilege, delivery/recovery, retry and reproducible-build behavior. | AWS/build PIs; IAM, async, replay and build checks; readable lock default overrides. | Analyzer enablement is not execution evidence; service guarantees and readable artifacts must be verified. |
| S2, S3, S4, S6, S7, S9 | Selected encryption, alarms, telemetry, API controls, suppressions and timeout budgets. | AWS/runtime instructions conditional on actual architecture and approved requirements. | Optional probes do not become mandatory just because they are mentioned here. Freeze applicability first. |
| R1, R2, R3, R4, R5, R6 | Apply locked pipeline, environment, reuse, observability, boundary and configuration rules. | Scope/exception/version discipline and delivery/runtime guidance; commented scoped guideline setup. | No approved CSAA profiles were invented. Translate locked rules into this file or approved scoped documents before the configured R round. |
| E1, E2 | Correct versioned cross-repo specifications and required linked work-item context. | Context check, source-citation instructions and commented linking/connector setup. | Links and connectors start unconfigured/disabled pending real source identities and scope. These rows are not operationally closed by this draft. |
| PC, IN | Legacy on-premise Java and readable versioned ETL artifacts in PRs. | Separate conditional Java and Informatica guidance. | No AWS assumptions for PC; no decoding of opaque assets or invention of a missing ETL PR workflow. |
| F01, F02 | Locked cases and an uncontaminated native/configured separation. | Explicit configured-only artifact; default guideline discovery off. | Owners must isolate keys, prepare cases and preserve each frozen manifest and native results. |
| F03, F04 | Independent execution and complete run/coverage evidence. | Manual controls, no incremental automation, review information and details. | Evaluators capture terminal status, skips, reuse, rate limits, files and run identity. |
| F05, F06 | Enforced read-only sources and frozen revisions. | Manipulation-resistant guidance; connectors/discovery off until scoped. | Credential/tool enforcement and immutable retrievable snapshots cannot be created by prompting. |
| F07, F08 | Approved disposable/live cohort and honest applicability/status. | Not-assessed versus inapplicable guidance. | Owners approve the cohort, policy interpretation and evaluator statuses. |
| F09 | Resist malicious instructions in supplied context. | Treat retrieved material as evidence; ignore policy/secret/action manipulation. | Defense in depth only; requires adversarial cases and enforced capability restrictions. |
| F10, F11 | Independent scoring, sample sufficiency and denominator rules. | No vendor-generated pass scores in summaries. | Human scorers, controls, counts and metric definitions are outside YAML. |
| F12, F13 | Analyzer attribution and module-specific rule isolation. | Preserve known provenance; deduplicate; scope approved rules and exceptions. | Reconcile identical-commit Snyk results and test actual sibling-module leakage. |
| F14, F15 | Approved configuration history and evidence of contextual reasoning. | Versioned artifact; cite causal context even when the comment anchor is in the diff. | Maintain change approvals and judge reasoning, not line placement alone. |

## Deployment prerequisites

1. Keep the native round and all prior evidence frozen. Agree that this file is
   the configured/remediation package; record preparation effort separately
   against the runbook's approximate one-person-day-per-platform configuration
   budget. Never place locked answer keys or planted-defect locations in review
   context. Do not apply this artifact to the tracking repository.
2. Select the approved disposable Bitbucket Cloud repository and verify file
   globs against actual changed files. The broad language globs are conditional
   on workload type. Once real module names are known, narrow organizational
   rules to their actual scopes. Inspect skipped files and generated ETL export
   paths. The four positive filters are exact documented default-ignore
   overrides, not a general source allowlist. Binary locks remain unreadable.
   See [path filters and instructions](https://docs.coderabbit.ai/configuration/path-instructions).
3. Provide approved source identities and frozen readable snapshots. For TPS,
   confirm the real workspace/repository for `csaa-tps-specs-wiki`, its
   `requirements.md`, OpenAPI and ADR index. Add only confirmed manual repository
   links. [Multi-repo analysis](https://docs.coderabbit.ai/knowledge-base/multi-repo-analysis)
   defaults to a linked repository's default branch; explicit branch/PR selection
   is currently GitHub/GitLab-only. Bitbucket cannot use that selection mechanism.
   An owner-approved immutable snapshot must therefore be accessible and verified.
   No YAML `ref` field was invented. Capture effective linked sources per run.
4. For E2, configure the authorized ticket/context connector and its allowed
   projects or servers before enabling its usage. MCP and ticket integrations
   remain disabled in this distributable candidate because actual identities,
   access and approved scope were not supplied. Use read-only capabilities and
   test denied writes; instructions are not credential enforcement.
5. Lock each applicable R profile. Translate approved rules into scoped PIs in
   this file, or enable audited, versioned guideline documents with `applyTo`
   scopes. [Code Guidelines](https://docs.coderabbit.ai/knowledge-base/code-guidelines)
   supplements default discovery: `filePatterns: []` does not disable default
   AGENTS/CLAUDE/etc. The draft explicitly sets `enabled: false` to avoid silent
   policy ingestion. Readable rule files can still enter other context, so audit
   actual source visibility per round. Missing locked profiles are not filled
   with guessed company standards.
6. Inspect effective organization/dashboard configuration, provider scopes,
   existing learning history, pending learning approvals, caches and agent
   sessions. Local learning scope and a 30-day approval delay do not disable
   learning or guarantee a frozen context. Keep the test window within the
   approved freeze and record any changes. Do not toggle `opt_out` as a casual
   cleanup: it deletes retained knowledge-base data. Record analyzer versions,
   repository analyzer configuration and other effective defaults too.
7. Verify G2/G3/G5 using actual provider controls and denied-action evidence.
   [Automatic approvals](https://docs.coderabbit.ai/pr-reviews/automatic-approvals)
   are explicitly off using the current `reviews.auto_approvals.enabled` key;
   do not introduce a conflicting legacy `request_changes_workflow` alias.
   Author command restrictions alone are insufficient because non-authors can
   still issue resolve commands. Preserve required human reviewers and protected
   branches. Disable any separately available Coding Agent/Autofix publication
   access or existing sessions in the evaluation environment; the listed
   finishing-touch switches are not a universal account permissions policy.
   See [agent delivery and Autofix](https://docs.coderabbit.ai/code/deliver-changes).
8. Confirm plan/provider support and capacity for all eight checks and enabled
   tools. Schema validity is not entitlement. Freeze the final file hash, source
   hashes, effective configuration and run manifest before any scoring. Changes
   after freeze create a new declared round, not a rewrite of completed results.

The candidate uses explicit manual review triggers. In an approved evaluation
repository, use the installed service account's equivalent of
`@coderabbitai full review` for a full pass; the plain `review` command is
incremental. Follow the [command reference](https://docs.coderabbit.ai/reference/review-commands),
and record completed run evidence. Neither this command nor `disable_cache`
proves independence by itself. No review commands were executed for this artifact.

## Verification and source provenance

[Static validation](validation.json) checks YAML duplicate keys, official JSON
Schema types/constraints, unsupported fields, unique action/check names and
advisory/manual settings. It also confirms the tracking root config and all
33 original source-package hashes are unchanged. It does not run a code-review
agent, deploy configuration, execute a probe or verify runtime permissions.

The public [configuration schema](https://coderabbit.ai/integrations/schema.v2.json)
was retrieved October 23, 2026; its SHA-256 is recorded in `validation.json`.
Supported fields and validation refinements were cross-checked against
`coderabbitai/mono` revision
[`a9145b4d4d789d28c7655115be6fccda8d194bf7`](https://github.com/coderabbitai/mono/tree/a9145b4d4d789d28c7655115be6fccda8d194bf7):

- [Configuration schema](https://github.com/coderabbitai/mono/blob/a9145b4d4d789d28c7655115be6fccda8d194bf7/packages/schemas/src/configuration/schema.ts):
  tone limit; custom checks, post-merge actions and strict configuration fields.
- [Approval workflow schema](https://github.com/coderabbitai/mono/blob/a9145b4d4d789d28c7655115be6fccda8d194bf7/packages/schemas/src/configuration/approval-workflow.ts):
  approval policy and legacy-alias compatibility.

This is a targeted schema comparison, not a fresh runtime implementation audit.
Mono links require the reader's existing access; no private source code is copied
into this repository. The older assessment's pinned implementation evidence is
preserved without silently replacing its conclusions.

To repeat the static validation with Python 3, PyYAML and jsonschema installed,
download the public schema separately, compare its hash with the recorded one,
then run from the repository root:

```sh
python3 reports/2026-10-23/evaluation-configuration/validate.py \
  --schema /absolute/path/to/schema.v2.json
```

The tracking repository's root `.coderabbit.yaml` remains disabled and excludes
all paths. This nested candidate was not activated here or in a customer repo.
