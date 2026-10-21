---
id: R6-PLATFORM-01-EXAMPLE
probe: R6
platform: <TPS | PC | IN>
evaluation_mode: configured
rule_profile: configuration/configured-rule-profile-example.md#CFG-01
config_manifest: evidence/<platform>/configured-manifest.yaml
author: DPT sample
status: draft
reviewed_by:
locked_on:
---

# R6-PLATFORM-01-EXAMPLE: Hardcoded service endpoint

> Illustrative sample only. Select a platform and replace repository, commit, path, manifest, and standard placeholders before review or locking.

## Setup

- **Repo:** `<sandbox service repository>`
- **Base commit (full SHA):** `<frozen base SHA>`
- **Probe commit (full SHA):** `<frozen probe SHA>`
- **Fix reference (commit / PR / incident), if historical:** NA - seeded case
- **What the PR contains:** A client change introduces `SERVICE_BASE_URL = "https://api.partner.example.com"` inside application code. Deployment configuration already supplies other environment-specific values but does not supply this endpoint. A stable relative path such as `/v1/payments` remains a constant and is a decoy.
- **Context available to the tool:** Full repository, deployment configuration, platform environment matrix, locked `CFG-01`, and the tool-specific configured manifest.
- **Context deliberately withheld (P7 only):** NA
- **Authoritative standard / ground truth:** `configuration/configured-rule-profile-example.md#CFG-01`

## Expected finding (answer key)

- **Issue:** The service base URL is environment-dependent but is hardcoded in application logic.
- **Where:** `<client module>` at `SERVICE_BASE_URL` and `<deployment configuration>` where environment-specific values are defined.
- **Why it matters:** Deployments cannot select the correct endpoint by environment, which can misroute requests and makes promotion require a code change.
- **What a good review recommends:** Read the base URL from an environment variable or approved configuration source, define it for each required environment, and retain the stable `/v1/payments` relative path as code.

## Good signal (score 2-3)

- **2:** Identifies the hardcoded environment-specific endpoint and recommends externalizing it.
- **3:** Also connects the application change to the missing environment definitions and correctly leaves the stable relative path in code.

## Bad signal (score 0-1)

- **1:** Says only "avoid magic strings" without identifying the environment or deployment risk.
- **0:** Misses the endpoint, requires the stable relative path to be externalized, recommends a secrets mechanism without justification, or invents a configuration standard not present in `CFG-01`.

## Origin

INTRODUCED

## Applicability

- **Platforms:** Any platform with an applicable locked configuration-externalization rule.
- **NA reason, if any:** NA

## Flawed (only if status: flawed)

- Date, reason, who decided. The probe is excluded from the evaluation.
