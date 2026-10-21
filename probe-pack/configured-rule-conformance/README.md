# Configured Organizational-Rule Conformance (R1-R6)

Use this set to test whether a review tool can apply explicit organizational or platform rules after configuration within the runbook Section 3.1b budget. R results are reported separately from native-capability results.

| ID | Capability | Expected signal |
|---|---|---|
| R1 | Delivery pipeline conformity | Detects a meaningful deviation from the approved build and deployment flow. |
| R2 | Environment configuration completeness | Detects a missing or inconsistent setting across the platform's required environment matrix. |
| R3 | Shared platform component reuse | Detects unnecessary reimplementation of an approved shared capability or incorrect placement of business logic. |
| R4 | Platform observability conformity | Detects deviation from the approved logging, telemetry, or log-forwarding pattern. |
| R5 | API security and boundary standards | Detects a missing approved authorization control or validation occurring after business processing, persistence, or outbound side effects. |
| R6 | Configuration externalization | Detects operational settings hardcoded in application logic instead of supplied through environment variables or an approved configuration source. |

## Required setup

1. Copy `configuration/_template-rule-profile.md` and create one tool-independent platform profile.
2. Review and lock the profile before any tool-specific translation is written.
3. Translate the entries into the tool's supported configuration format.
4. Freeze the tool's configured manifest in `evidence/<platform>/`.
5. Create one probe file per case using `../_template-probe.md`, set `evaluation_mode: configured`, and reference the exact profile entry.
6. Run the tool on the frozen commits with the defined repository context and configuration budget.

A mandatory profile entry that a tool cannot accept or apply is Red. NA is only for a rule that does not apply to the platform. Mechanically enforceable checks remain deterministic controls; use R probes only when review requires semantic judgment.

## Worked sample

- Tool-independent rule profile: `configuration/configured-rule-profile-example.md`, entry `CFG-01`
- Matching probe case: `probe-pack/configured-rule-conformance/R6-configuration-externalization-example.md`

The sample demonstrates a hardcoded environment-specific service endpoint, a stable relative-path decoy, the configured-manifest reference, and the 0-3 scoring signals. Select a platform and replace every placeholder before reviewing or locking a real case.
