# CSAA Bitbucket demonstration implementation status

The six demonstration baselines are published in the private Bitbucket project,
and all six hosted CI pipelines passed. Thirteen native showcase PR reviews
completed. Configured Jira/scope checks are prepared; their runtime validation
awaits the new workspace's included review capacity. Execution remains outside
this tracking repository. No successful formal CSAA PoV, pilot-readiness decision
or adoption result is asserted.

The sources remain the [requirements assessment](https://docs.google.com/document/d/16LQrN9LyoMjFLw9HiDNF2RIe79rKmTlfPASfR-SK1VI/edit)
and [mutual success plan](https://docs.google.com/document/d/1GfYrExOJhHtyCAgCJsk0rJ20Up9Vg5aAShzPLqlUeQk/edit).
[Epic CDB-5](https://coderabbit-demo.atlassian.net/browse/CDB-5) tracks six
requirement records and twenty tasks, all assigned to Mahesh Mani. The Epic and
remaining implementation tasks are In Progress. Repository creation, CodeRabbit
installation, TPS service, frozen specifications and consumer baseline tasks are
Done. Installation was observed for all six repositories in CodeRabbit's web UI.

## Implementation and criteria

| Deliverable | Requirement support | Evidence still needed |
|---|---|---|
| Python TPS API, atomic SQLite/DynamoDB adapters, independent approval, idempotency/outbox/capture/refund/ledger/audit, AWS CDK and CI | REQ-01/04; D/C/S and concurrency/failure probes | Applicable static-analysis attribution and independent platform scoring |
| Separate requirements/OpenAPI/event/provider schemas, approved ADR and explicitly draft proposal, TypeScript consumer | REQ-02; P2/P3/A4 and compatibility cases | Correct frozen cross-repository/source retrieval and context-gap behavior |
| Six native and six configured CodeRabbit profiles, guidelines, environment matrix and installation guide | REQ-05; R1–R6 | Approved platform profile, effective tenant settings and separately scored configured runs |
| Private evaluation harness, 13 published native case PRs, frozen draft manifests, actual hosted exports and scoring/adoption capture templates | REQ-02/03/06; G7/G8/P9/P10/A2 | Independent key approval/scoring, hosted repeatability and the real adoption baseline/cohort |
| Synthetic Java transaction example and Python ETL restart example/native-export intake | REQ-04 extension preparation | Sanitized actual Payment Central and native Informatica assets; formal platform assessments remain untested |

The configured starter files cover coding guidelines, explicit multi-repository
links, scoped path instructions, context-preserving path filters, concise
evidence-backed tone, linked-issue assessment and six warning-mode custom
pre-merge checks, including actual issue-context availability and change/permission
scope. All twelve profiles
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
the application read-only mode is not proof of a least-privilege token. Actual
CodeRabbit Jira retrieval is still untested.

TWG v1.3.8 Jira and Bitbucket authentication are repaired. The six baselines and
disposable PR branches were published through the supported commit API, with
local/remote SHA mappings preserved outside this repository. Mahesh separately
approved refreshing the CodeRabbit Bitbucket OAuth authorization. No credentials
are included in deliverables.

Configured PRs 14–16 isolate an allowed change, an unrelated permission change
and missing allowed business context. Their full-review requests received
CodeRabbit rate-limit notices in this new Bitbucket environment. Mahesh chose
to wait for included capacity. Tenant usage-based reviews were already active;
no paid setting was enabled by this work. Runtime issue/scope validation and a
second comparable hosted review remain outstanding. Never merge seeded branches.
Required scopes, denied autonomous actions, provider human-review protections
and written data-handling answers still need evidence. Real adoption/value
requires the approved cohort.

Execution code, keys, raw review text and automation remain outside this
tracking repository. Original framework files, assessment snapshots and its
review-disabled configuration are preserved.
