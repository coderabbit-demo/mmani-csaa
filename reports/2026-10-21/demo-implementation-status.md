# CSAA Bitbucket demonstration implementation status

The six demonstration baselines are published in the private Bitbucket project,
and all six hosted CI pipelines passed. Thirteen native showcase PR reviews
completed. A completed hosted repeatability pair and a versioned configuration package
are preserved. The simplified Jira/scope profile completed all three existing-PR control
reviews with the expected pass/warning behavior. Execution remains outside
this tracking repository. No successful formal CSAA PoV, pilot-readiness decision
or adoption result is asserted.

The sources remain the [requirements assessment](https://docs.google.com/document/d/16LQrN9LyoMjFLw9HiDNF2RIe79rKmTlfPASfR-SK1VI/edit)
and [mutual success plan](https://docs.google.com/document/d/1GfYrExOJhHtyCAgCJsk0rJ20Up9Vg5aAShzPLqlUeQk/edit).
[Epic CDB-5](https://coderabbit-demo.atlassian.net/browse/CDB-5) tracks six
requirement records and twenty tasks, all assigned to Mahesh Mani. The Epic remains In Progress. Context, standards and configuration handoff are
In Review; formal platform and adoption work remain open. Repository creation,
installation, the three TPS baselines, export/repeatability capture and presenter
handoff are Done. Installation was observed for all six repositories in the web UI.

## Implementation and criteria

| Deliverable | Requirement support | Evidence still needed |
|---|---|---|
| Python TPS API, atomic SQLite/DynamoDB adapters, independent approval, idempotency/outbox/capture/refund/ledger/audit, AWS CDK and CI | REQ-01/04; D/C/S and concurrency/failure probes | Applicable static-analysis attribution and independent platform scoring |
| Separate requirements/OpenAPI/event/provider schemas, approved ADR and explicitly draft proposal, TypeScript consumer | REQ-02; P2/P3/A4 and compatibility cases | Correct frozen cross-repository/source retrieval and context-gap behavior |
| Six native and six configured CodeRabbit profiles, guidelines, environment matrix and installation guide | REQ-05; R1–R6 | Approved platform profile, effective tenant settings and separately scored configured runs |
| Private evaluation harness, 13 published native case PRs, frozen draft manifests, actual hosted exports and scoring/adoption capture templates | REQ-02/03/06; G7/G8/P9/P10/A2 | Independent key approval/scoring and the real adoption baseline/cohort |
| Synthetic Java transaction example and Python ETL restart example/native-export intake | REQ-04 extension preparation | Sanitized actual Payment Central and native Informatica assets; formal platform assessments remain untested |

The configured starter files cover coding guidelines, explicit multi-repository
links, scoped path instructions, context-preserving path filters, concise
evidence-backed tone and built-in linked-issue/scope assessment using native Jira
issue content.
Five warning-mode custom checks address approved business issue context, approved intent,
environment completeness, inbound authority and asynchronous recovery. All twelve profiles
passed the published schema and additional round/advisory checks. Root demo
configurations use the native manual/advisory profile. Hosted resolved-configuration
replies on native PR 1 and configured PR 14 confirm the distinct source/link/check
settings and disabled automatic repair/approval behavior. Configured results are
kept separate. Schema acceptance does not prove source access, entitlement,
effective settings or review quality. Custom checks do not execute application
tests ([configuration reference](https://docs.coderabbit.ai/reference/configuration),
[custom checks](https://docs.coderabbit.ai/pr-reviews/custom-checks)).

Nine local verification checks passed: 21 Python payment tests, AWS synthesis,
infrastructure invariants, TypeScript type checking plus four runtime tests,
specification validation, twelve configuration validations, Java transaction
checks, four ETL tests and the Python/TypeScript HTTP smoke test. CI images and
dependencies are pinned. All six hosted baseline pipelines passed, including
the [TPS tests and synthesis run](https://bitbucket.org/manimahesh-cr/csaa-tps-payments-aicr/pipelines/results/1).
No cloud deployment occurred.

The three configured PRs also have actual CI outcomes: the configuration-only
change passed, the IAM-expansion change failed the synthesized-template
least-privilege invariant, and the missing-business-ticket change passed
application CI. These are CI results, not evidence that CodeRabbit retrieved a
Jira ticket or ran its custom checks.

## Hosted showcase observations

All thirteen native PRs completed, with 25 inline findings from the verified
CodeRabbit bot. The [capture review](https://bitbucket.org/manimahesh-cr/csaa-tps-payments-aicr/pull-requests/1)
and [consumer compatibility review](https://bitbucket.org/manimahesh-cr/csaa-tps-payments-aicr/pull-requests/3)
cite linked repository context. The formatting control has no inline findings;
other zero-finding results and misses are preserved. This is an author-prepared
rehearsal, not independently scored evaluation evidence.

Actual Bitbucket exports preserve provider metadata, raw comments, source/destination
SHAs, bot identity and available locations. Severity/category can be parsed from
literal narrative headings; dedicated origin/action fields are absent and remain
null. Narrative comments serialized into JSON do not establish full P10 field
fidelity. The completed local CLI runs below remain distinct from hosted evidence.

## Hosted repeatability observation

Two fresh full reviews on [PR 17](https://bitbucket.org/manimahesh-cr/csaa-tps-payments-aicr/pull-requests/17)
and [PR 18](https://bitbucket.org/manimahesh-cr/csaa-tps-payments-aicr/pull-requests/18)
completed with identical source/base commits, native configuration, title/body and
frozen supplied specification/consumer sources. The actual hosted diff files have
identical SHA-256 values. They returned two and three findings. Preliminary
author matching identifies two shared issues and one unmatched issue:
**2/3 = 66.67% overlap**, below the framework's 80% P9 Green target. Matched
severities are Major/Major and recommendations agree. Independent confirmation
is required; this is not a formal score. PR identity/destination alias and opaque
backend/model/knowledge state remain limitations.

## Preliminary CLI observation

The installed CodeRabbit CLI v0.9.1 binary was matched to its official versioned
release archive. Two completed full/fresh committed-change reviews used the
same synthetic diff and command outside this repository. Both returned two
major findings. Preliminary author matching identifies one matching pair and
three root causes in the union: **33% overlap**, below the framework's 80% P9
Green target. Raw NDJSON, hashes and the matching explanation are preserved in
evaluator-only storage. Independent confirmation remains required.

The CLI output supplies file, line, severity, rationale and agent instructions;
dedicated origin/category fields are absent. This local result is not actual
Bitbucket PR-export evidence. The CLI reported free allowance because its
account could not access an organization connection for the remote, while the
web UI independently showed all six repositories Installed. Effective CLI/tenant
model settings were not fully exposed. No formal P9 or P10 score is assigned.

## Jira context and publication

A separate [CSAA Demo Context project (CDC)](https://coderabbit-demo.atlassian.net/browse/CDC)
contains three synthetic business requirements assigned to Mahesh:
[independent approval/refund replay (CDC-1)](https://coderabbit-demo.atlassian.net/browse/CDC-1)
and [capture delivery/contract compatibility (CDC-2)](https://coderabbit-demo.atlassian.net/browse/CDC-2),
plus [configuration-only delivery scope (CDC-3)](https://coderabbit-demo.atlassian.net/browse/CDC-3).
They contain acceptance criteria and source links, not evaluation keys. Scoped
configured profiles allow CDC and exclude CDB planning. Mahesh approved a named
CodeRabbit scope for exactly six CSAA repositories using the existing read-only
Jira connection. The Base Scope has zero connections; CDB is also excluded by
workspace security policy. The underlying Jira OAuth grants include writes, so
the application read-only mode is not proof of a least-privilege token. Native Jira supplied-context assessment completed with matching issue-title and acceptance-criterion citations.
An independent live API refresh inside a custom check is not claimed.

TWG v1.3.8 Jira and Bitbucket authentication are repaired. The six baselines and
disposable PR branches were published through the supported commit API, with
local/remote SHA mappings preserved outside this repository. Mahesh separately
approved refreshing the CodeRabbit Bitbucket OAuth authorization. No credentials
are included in deliverables.

Configured PRs 14–16 isolate an allowed configuration change, an unrelated IAM
change and missing allowed business context. Initial requests emitted capacity
warnings but did complete through trial continuation; the earlier diagnosis that
those reviews were blocked was corrected. Mahesh chose included capacity only.
No paid setting was enabled, and current informational capacity replies were
checked before later individual review requests.

The Jira connection test succeeds and the installed Jira Forge app reports the
site already linked. Version 4's additional direct-live-lookup custom probes
remained Inconclusive. The inspected custom-check implementation exposes a
[native Linear reader](https://github.com/coderabbitai/mono/blob/0bd871360275c809f8439f2e30ba4f3926e91045/pr-reviewer-saas/src/pre-merge-checks/custom-check-agent.ts#L570),
with no corresponding native Jira reader in that path. The deployed revision is
not established by that inspection; the observed runtime error matches this
limitation. Existing Jira authorization alone cannot establish that capability.

Following Mahesh's request for a simpler path, version 5 uses the separate,
supported Jira linked-issue ingestion path and built-in issue/scope assessment.
Its business-context check requires complete allowed issue content, title and
acceptance-criterion citations, without claiming another live refresh. It disables
unused Linear lookup and keeps MCP disabled. Earlier failures are preserved as
separate versioned evidence. The current six configured files are at
[standards commit b8f4cb5](https://bitbucket.org/manimahesh-cr/csaa-platform-standards/src/b8f4cb53b0b0a950e7276cbd20a8c212c39bd2fa/configs/configured/),
and hosted standards CI run 4 passed. The effective configuration reply confirms
five custom checks, CDC allowlist/CDB exclusion, disabled Linear/MCP, manual reviews
and disabled repair/approval features.

| Control | Observed CodeRabbit result | Hosted CI |
|---|---|---|
| [Allowed configuration change, PR 14](https://bitbucket.org/manimahesh-cr/csaa-tps-payments-aicr/pull-requests/14) | Linked Issues, Out of Scope Changes and Approved Business Issue Context Passed; cites CDC-3 title and criteria 1–5 | Build 11 Passed |
| [Unrelated IAM expansion, PR 15](https://bitbucket.org/manimahesh-cr/csaa-tps-payments-aicr/pull-requests/15) | Linked Issues, Out of Scope Changes and Authoritative Change Intent Warning; approved Jira context Passed | Build 12 Failed the least-privilege invariant, as intended |
| [Missing allowed business issue, PR 16](https://bitbucket.org/manimahesh-cr/csaa-tps-payments-aicr/pull-requests/16) | Approved Business Issue Context Warning; rejects CDB planning as the required business issue | Build 13 Passed |

These are advisory supplied-snapshot assessments. Exact provider fetch
revision/time and a separate live refresh are not claimed. PR 16's built-in
assessment still contains historical CDB planning references; the approved-context
check rejects them. Configured exclusions do not prove denied provider access or
retroactive cached-context removal. Existing source-isolation and human-control
gates therefore still require their own evidence.
Never merge seeded branches.

Required scopes, denied autonomous actions, provider human-review protections
and written data-handling answers still need evidence. Real adoption/value
requires the approved cohort.

Execution code, keys, raw review text and automation remain outside this
tracking repository. Original framework files, assessment snapshots and its
review-disabled configuration are preserved.
