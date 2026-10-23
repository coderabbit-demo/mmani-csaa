"""Prepare scoped cell updates for the supplied PoV workbook; never write XLSX."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BASE = "https://github.com/coderabbit-demo/mmani-csaa/blob/78a005921f893ade0ea83cff64898be70291ce56/"
operations = []


def put(sheet, address, values):
    if isinstance(values, str):
        values = [[values]]
    operations.append({"sheet": sheet, "range": address, "values": values})


def link(url, label):
    return '=HYPERLINK("' + url + '","' + label + '")'


sheet = "Overview"
put(sheet, "A2", "CSAA DPT working draft. Updated October 23, 2026. Dates, scope and commitments require joint confirmation.")
overview = {
    "B4": "CSAA Digital Payment Transformation (DPT)",
    "B5": "TBD. Per-platform enablement after vendor-risk clearance and locked probe-wave readiness.",
    "B6": "TBD. Proposed three weeks after each platform is enabled. Record any approved extension or earlier stop.",
    "B7": "Proposed weekly. Day/time TBD. Amit Mishra owns the mandatory Week 1 checkpoint per platform.",
    "B8": "TBD. Proposed end of Week 3: DPT evidence compilation, Enterprise Architecture review and ARC outcome.",
    "B9": "TBD. Confirm eligible developers, actual pilot participants and repository counts separately by platform.",
    "B10": "Bitbucket Cloud for TPS, Payment Central and Informatica. Sanitized <source-repo>-aicr evaluation repos; mmani-csaa is tracking only, with reviews disabled.",
    "B11": "Jira projects and linked-ticket conventions TBD. Confluence/specification sources and frozen revisions require confirmation.",
    "B12": "TBD. Approved read-only external context, source permissions, egress and provider/plan support must be validated. SharePoint/other-source route is not assumed available.",
    "B13": "TPS: Python/AWS serverless, RDS and Glue. Payment Central: legacy Java/on-premise. Informatica ETL: readable mappings/workflows and feed/restart semantics. Advisory review; human approval/merge retained.",
}
for address, value in overview.items():
    put(sheet, address, value)
put(sheet, "A13", "Platform scope")
put(sheet, "A16:D24", [
    ["Customer", "CTO", "TBD. Confirm named CTO", "TBD"],
    ["Customer", "Project Lead", "Amit Mishra. Runbook responsibility; formal title TBD", "TBD"],
    ["Customer", "Technical Lead", "TPS: Sasi, Kasa, Sadak. Payment Central: Karthikeyan Subbiah. Informatica: Ashin. Primary contacts/titles TBD", "TBD"],
    ["Customer", "Security / vendor-risk lead", "TBD. Confirm accountable contact", "TBD"],
    ["Customer", "Executive Sponsor", "TBD. Confirm funding/escalation owner", "TBD"],
    ["Customer", "Decision forum", "Enterprise Architecture review; ARC final forum. Individual representatives TBD", "TBD"],
    ["CodeRabbit", "Account Executive", "TBD. Confirm account owner", "TBD"],
    ["CodeRabbit", "Solutions Engineer", "TBD. Confirm technical PoV owner", "TBD"],
    ["CodeRabbit", "Executive Sponsor", "TBD. Confirm sponsor", "TBD"],
])
put(sheet, "A26:D28", [
    ["Evaluation basis", link(BASE + "runbook.md", "DPT v2.5 runbook"), "PI candidates", link(BASE + "reports/2026-10-23/path-instruction-candidates.json", "Proposed prompts and limits")],
    ["Tracking", link("https://github.com/coderabbit-demo/mmani-csaa", "mmani-csaa"), "Formal results", "Not yet evaluated"],
    ["Plan status", "Draft for joint confirmation", "Updated", "October 23, 2026"],
])

sheet = "Success Criteria"
put(sheet, "A2", "DPT v2.5 is authoritative. Required criteria are High priority. Score each platform independently; retain native/configured results separately. All outcomes are pending.")
criteria = [
    ["Codebase Context Depth", "G4/P2: demonstrate a finding that depends on unchanged callers, shared code, tests, lockfiles or configuration. Cite the contextual artifact and explain the causal connection to the changed behavior.", "High. File availability alone is not proof of use. A correct inline comment can be anchored to a changed line. Record inaccessible required context.", "Not yet evaluated"],
    ["Cross-Repo Context", "P3/E1: use the approved, frozen separate spec repository. Distinguish a code violation from a missing/ambiguous spec. Use requirements.md for acceptance criteria, OpenAPI for contracts and ADRs for decisions, respecting phase/status.", "High. For TPS, confirm csaa-tps-specs-wiki and the approved revision. Propose a concrete code/test action or spec clarification. Do not invent requirements.", "Not yet evaluated"],
    ["External Context Ingestion", "A4/E2: retrieve and apply the linked ticket and approved design/acceptance context. Cite the source/version. Record any required retrieval failure and its effect on the assessment.", "High. A4 is required core. E2 is NA only when the change has no linked ticket. Confirm Jira, Confluence, SharePoint/other routes, permissions and frozen sources; PIs cannot create access.", "Not yet evaluated"],
    ["Global & Repo Specific Configuration", "A5/R1-R6: lock a tool-independent platform rule profile, translate approved rules into supported configuration and test positive cases/decoys. Verify path/module scope, approved exceptions and retention over time.", "High. Report the configured round separately. R-set is NA until its profile is locked; inability to apply an applicable locked rule is a failed result. Budget about one configuration person-day per platform. PI library linked on Overview.", "Not yet evaluated"],
    ["Review Signal Quality", "P1/P5-P10: useful replay signal >=40% of completed comparable P1 cases; P5/P6/P7 Green; silent noise control or at most 2 low-impact comments without claimed risk; P9 overlap >=80% on independent identical-input runs. P10 captures complete actionable finding evidence.", "High. Verify hallucination resistance, origin and not-assessable honesty. Preserve raw file/location/severity/category/rationale/origin/action. Freeze configuration/context, use full/fresh runs, record duplicate/not-assessable counts and define empty denominators. Bands are calibration aids.", "Not yet evaluated"],
    ["Pre-PR & Agent Workflow", "G7/G8/A1-A3: demonstrate approved local pre-PR/agent-usable output, a feedback handoff without rewriting, cross-task consistency against shared contracts, and severity calibrated to tests/tools/payment impact.", "High. Inspect the actual public export and proposed patch. Preserve the human approval boundary. A text prompt does not add an export field or authorize autonomous code changes.", "Not yet evaluated"],
    ["Bitbucket, Security & Human Control", "G1-G3/G5-G6: prove normal Bitbucket Cloud PR operation, advisory/non-blocking behavior, least-privilege roles/scopes and written data-handling answers. Test denied approval/merge/push/bypass effects and document egress, retention, deletion, subprocessors, model/provider and training usage.", "High. Day 0-2 gate evidence is mandatory. Recorded POC SaaS-egress risk acceptance does not replace G5/G6 execution. Required gate failure stops or escalates the platform evaluation. Prompts are not permission controls.", "Not yet evaluated"],
    ["Change-Risk Tests & Failure Safety", "P11-P13: identify the change-specific untested edge/failure/state transition, explain a plausible concurrency interleaving or atomicity failure, and preserve correct boundary handling, correlation, retries and DLQs.", "High. Require a concrete cause and appropriate control. Avoid generic coverage demands, try/catch everywhere, duplicate logging and unsafe retries. The evaluator's harness proves the planted risk; a PI does not run the test suite.", "Not yet evaluated"],
    ["Payment, Contract & Platform Risk", "Run applicable D1-D9, C1-C8 and A probes. TPS includes P4 and core S1/S5/S8/S10; preselect other S probes. Cover Payment Central transaction/legacy risks and readable Informatica mapping/feed/restart semantics where reviewable.", "High for applicable core. Preserve Snyk provenance and assess added AI signal on identical commits. Do not apply AWS-only rules to on-premise platforms. Binary/unavailable ETL artifacts need a reviewability decision, not a prompt workaround.", "Not yet evaluated"],
    ["Adoption, Trust & Business Value", "During approved Weeks 2-3 live use, classify findings independently. Initial Phase 4 Green bands: actionable >=60%, false positive <20%, no harmful finding observed. Measure reviewer load and end-window trust against the platform baseline.", "High. Denominator excludes Duplicate and Not assessable; Partially actionable stays separate. Accepted high-risk advice receives a second human look. Resolve live-use authorization first. Usage and acceptance counts are not quality scores or measured ROI.", "Not yet evaluated"],
    ["Pilot Readiness & Decision", "Amit Mishra owns the Week 1 continue/constrain/pause/stop decision per platform. End Week 3: DPT compiles evidence, Enterprise Architecture reviews and ARC receives the platform outcome under runbook section 19.", "High. Outcomes: Ready to pilot now; Fix named blockers, then pilot; Limited use only; Do not proceed. Preserve NA/untested/invalid distinctions and frozen results. Acted-on harmful advice on payment/contract/security/irreversible paths triggers Do not proceed. Commercial approval is separate.", "Not yet evaluated"],
]
put(sheet, "A5:D15", criteria)

sheet = "Milestone Tracker"
put(sheet, "A2", "Proposed relative schedule. Calendar dates are TBD. Blank status means unconfirmed; In progress may mean a draft exists and does not imply customer acceptance. Owner roles require confirmation.")
milestones = {
    6: ["Pre-PoV", "Intro / Discovery call", "", "", "TBD (account owner)", "Amit Mishra", "Requirements are available. Confirm discovery completion, attendees and date; no meeting completion is inferred."],
    7: ["Pre-PoV", "Product Demo", "", "", "TBD (technical owner)", "Platform leads", "Demonstration assets exist in tracking. Confirm the customer demo, audience and feedback; demonstration observations are not formal CSAA gate results."],
    8: ["Pre-PoV", "Align on Business Value Assessment", "", "In progress", "TBD (account owner)", "Amit Mishra / platform leads", "Draft measurement definitions are mapped. Capture the three-month PR/reviewer-load baseline. Salary, developer counts, review-time reduction and defect economics require customer inputs; no ROI is asserted."],
    9: ["Pre-PoV", "Agree teams, repositories and evaluation cohort", "", "In progress", "TBD (technical owner)", "Platform leads", "TPS, Payment Central and Informatica are the candidate platforms. Confirm exact code/spec repos and participants; create sanitized <source-repo>-aicr copies. Resolve disposable-only versus live Phase 4 policy."],
    10: ["Pre-PoV", "Agree success criteria and PoV plan", "", "In progress", "TBD (technical owner)", "Amit Mishra", "This spreadsheet is the current plan; joint acceptance is pending. Lock waves, independent scorers and answer keys outside tool context. Resolve NA/not-tested semantics and any policy exceptions before execution."],
    11: ["Pre-PoV", "Agree evaluation communication channel", "", "", "TBD (account owner)", "Amit Mishra", "Confirm the approved channel, participants and evidence/escalation process. No Slack channel creation or notification is assumed."],
    13: ["Pre-PoV", "Senior developers and leads: workflow / evidence briefing", "", "", "TBD (technical owner)", "Platform leads", "Brief independent scorers on locked cases, origin labels, missing-context honesty, finding classification and the human-control boundary. Nobody scores a case they wrote."],
    14: ["Day 0-2", "Install approved pilot repositories and validate G1-G8", "", "", "TBD (technical owner)", "Security / platform leads", "After risk clearance and readiness: confirm service account, scoped credentials, egress, effective settings and written data-handling records. Preserve advisory review; record actual denied-action checks and public export/pre-PR output."],
    15: ["Week 1", "Complete native probes and Week 1 checkpoint", "", "Not started", "TBD (technical owner)", "Amit Mishra", "Run applicable P1-P13 and A4/E2 with the frozen native manifest. Capture completed, independent runs and raw findings. Amit decides continue / constrain / pause / stop per platform with EA/evidence input."],
    16: ["Weeks 1-2", "Domain cases and separate configured-rule round", "", "Not started", "TBD (technical owner)", "Platform leads", "Run applicable D/C/A/S and PC/IN cases. Lock each R1-R6 profile; select general PI/custom-check candidates in a new manifest, about one configuration person-day per platform. Preserve original results and record effort/residual gaps."],
    18: ["Week 1", "User demo for the approved PoV cohort", "", "", "TBD (technical owner)", "Platform leads", "Confirm participants, reviewer/agent workflow and evidence capture. Broader enablement remains conditional on the Week 1 decision and approved scope."],
    19: ["Weeks 2-3", "Enable approved cohort repositories and users", "", "Not started", "TBD (technical owner)", "Security / platform leads", "Enable only approved repositories/users after the checkpoint. Resolve live-PR authorization first; record cohort/window limits. Never enable review on the mmani-csaa tracking repository."],
    20: ["Weeks 2-3", "Weekly progress and evidence check-ins", "", "Not started", "TBD (technical owner)", "Amit Mishra / platform leads", "Track PR count/size, actionability, false positives, duplicates, not-assessable findings, reviewer load and confounds per platform. Give accepted high-risk advice a second human review. Record changes and incidents."],
    22: ["Week 3", "Developer sentiment retrospective", "", "Not started", "TBD (technical owner)", "Platform leads", "Use runbook Appendix C once at the end of the window. Record not measured if the retrospective is absent. Include usability, trust, harmful findings and senior triage effort; sentiment does not override required gates."],
    23: ["Week 3", "Score success criteria from independent evidence", "", "Not started", "TBD (technical owner)", "DPT evidence owner / EA", "Score locked cases 0-3 with the runbook outcome rules. Separate native, configured and remediation results and NA/not-tested/invalid states. Do not combine scores or average platforms. Preserve original failures and misses."],
    24: ["Week 3", "Executive readout and business value assessment", "", "Not started", "TBD (account owner)", "Amit Mishra / EA / ARC", "Present evidence-based per-platform recommendations, open blockers, setup effort and unmeasured value. Extend only for named missing evidence under recorded approval. Contract/purchase decisions remain separate."],
    26: ["Post-PoV", "Vendor selection decision (conditional)", "", "", "TBD (account owner)", "TBD (sponsor)", "Only after applicable pilot-entry rules and customer decision. Do not assume vendor selection, purchase or rollout from this working plan."],
    27: ["Post-PoV", "Commercial terms (conditional)", "", "", "TBD (account owner)", "TBD (procurement)", "Confirm actual seat/cohort scope, quote and commercial approvals separately. No price, savings or commitment is supplied."],
    28: ["Post-PoV", "MSA review (conditional)", "", "", "TBD (account/legal)", "TBD (legal/security)", "Confirm legal owners and required agreement review only if proceeding. This plan does not accept terms."],
    29: ["Post-PoV", "MSA approval (conditional)", "", "", "TBD (account/legal)", "TBD (legal approver)", "Customer approval and signatory authority remain unconfirmed; no approval is inferred."],
    30: ["Post-PoV", "Order form signature (conditional)", "", "", "TBD (account owner)", "TBD (signatory)", "Separate authorized commercial action. No contract start date or signature commitment is established."],
    31: ["Post-PoV", "Pilot / production rollout plan (conditional)", "", "", "TBD (technical owner)", "TBD (rollout owner)", "Agree scope, owners and retention/evaluation-copy cleanup only after entry rules are met. Re-run named fixes under new manifests on the same locked assets and preserve original evidence."],
}
for row, values in milestones.items():
    put(sheet, f"A{row}:G{row}", [values])

sheet = "Configuration Checklist"
config = {
    4: ["Confirm Bitbucket setup authority and runtime scopes", "https://docs.coderabbit.ai/platforms/bitbucket-cloud", "", "TBD (Security/admin)", "Separate one-time workspace/repository installation authority from the ongoing service-account role and token scopes. Obtain approval for least privilege; verify effective denied actions and G3/G5. Do not assume standing admin is required for review."],
    5: ["Install on approved sanitized repositories only", "https://docs.coderabbit.ai/getting-started/quickstart", "", "TBD (platform/admin)", "Confirm the code/spec inventory and <source-repo>-aicr evaluation copies. Do not install or enable reviews on mmani-csaa. Production/live-use scope needs explicit policy resolution."],
    6: ["Disable automatic review until controlled enablement", "https://docs.coderabbit.ai/configuration/auto-review", "", "TBD (technical owner)", "Use explicit/manual runs for frozen probes as approved. Declare automatic/incremental behavior for the adoption cohort. The tracking repository remains excluded with automatic reviews disabled."],
    7: ["Assign seats to confirmed pilot users only", "https://docs.coderabbit.ai/management/seat-assignment", "", "TBD (account/admin)", "Participant count, eligible population, actual users and entitlements are TBD. Confirm pilot scope and commercial terms separately; no seat count is assumed."],
    9: ["Set and freeze the review profile", "https://docs.coderabbit.ai/reference/configuration#param-profile", "", "TBD (technical owner)", "Predeclare the native profile and all effective overrides. A later quieter profile is a configuration/remediation change; preserve the original noise and quality results."],
    10: ["Inventory coding guidelines and approved standards", "https://docs.coderabbit.ai/knowledge-base/code-guidelines", "", "Platform leads / CR TBD", "Identify automatically discovered guideline files, versions and scope. Do not leak locked answer keys or load new house rules into the native round without declaring them. R profiles require owner approval."],
    11: ["Configure review paths and verify required context", "https://docs.coderabbit.ai/configuration/path-instructions", "", "Platform leads / CR TBD", "Confirm readable code, IaC, tests, manifests/lockfiles and Informatica exports. A PI cannot override an excluded path. Do not remove must-find cases to lower noise; validate both reviewed scope and context availability."],
    12: ["Link approved code and specification repositories", "https://docs.coderabbit.ai/knowledge-base/multi-repo-analysis", "", "Platform leads / CR TBD", "Confirm approved Bitbucket code/spec repos, frozen source revisions, requirements.md/OpenAPI/ADR roles and phase/status. Record provider/plan branch-selection limits and the actual supplied snapshot."],
    13: ["Define actionable PR output and evidence capture", "https://docs.coderabbit.ai/getting-started/yaml-configuration", "", "TBD (technical owner)", "P10 needs actual file/location/severity/category/rationale/origin/action and agent handoff evidence. Comment-body guidance can help; it cannot add native export fields. Preserve raw output and mark adapter/unavailable fields explicitly."],
    14: ["Select path instructions for a separate configured round", "https://docs.coderabbit.ai/configuration/path-instructions", "In progress", "Platform leads / CR TBD", "Candidate library prepared October 23, not applied or validated. See Overview link. Replace illustrative globs, consolidate applicable rules and freeze a new manifest. P8: normally no finding for proven non-semantic changes; low priority only for useful optional formatting advice."],
    15: ["Establish the approved shared configuration baseline", "https://docs.coderabbit.ai/configuration/configuration-inheritance", "", "TBD (technical owner)", "Inventory inheritance/global overrides, learnings, enabled tools and external sources. Export the effective result. Prompt text is not a permission boundary; approved provider controls must enforce human authority."],
    16: ["Freeze per-repository configuration manifests", "https://docs.coderabbit.ai/getting-started/yaml-configuration", "", "Platform leads / CR TBD", "Record code/spec SHAs, tool/CLI version, profile, path rules, sources, scopes, review mode and approved exceptions per platform. Preserve native, configured and remediation manifests/results separately."],
    18: ["Trial Change Stack in the approved workflow", "https://docs.coderabbit.ai/pr-reviews/change-stack", "", "TBD (technical owner)", "Confirm provider/plan availability and usefulness on actual Bitbucket pilot work. This optional enablement item does not replace any required gate or probe."],
    19: ["Validate review commands and independent reruns", "https://docs.coderabbit.ai/guides/commands", "", "TBD (technical owner)", "Use actual completed full reviews or supported CLI fresh mode for independent P9 repeats; log reused/skipped/partial/failed runs. Freeze context and configuration and predeclare the both-empty overlap rule."],
    20: ["Control learnings and knowledge-base sources", "https://docs.coderabbit.ai/knowledge-base/learnings", "", "TBD (technical owner)", "Inventory evolving learnings and source revisions. Local scope is not an immutable freeze. Do not reset a shared organization's knowledge casually; isolate the approved evaluation setup and record residual variation."],
    21: ["Validate the approved CLI / IDE / agent route", "https://docs.coderabbit.ai/cli/reference", "", "Platform leads / CR TBD", "Actual IDEs, agents and managed installation are TBD. Demonstrate G8 and A2 through a supported local route with structured raw output, terminal completion and human-approved proposed repairs."],
    22: ["Validate dashboard and raw findings export", "https://docs.coderabbit.ai", "", "TBD (technical owner)", "Confirm actual provider/plan metrics, export fields and provenance. Dashboards support evidence; independently classified findings and locked-case results are primary. Do not treat usage or acceptance as actionability."],
    24: ["Define warning-mode custom checks where appropriate", "https://docs.coderabbit.ai/pr-reviews/custom-checks", "", "Platform leads / CR TBD", "Use approved general invariants in a declared configured round. A custom-check summary is distinct from inline review and cannot run the application test suite, enforce G3 or alone satisfy P10."],
    25: ["Connect approved issue-tracker context", "https://docs.coderabbit.ai/integrations/issue-integrations", "", "TBD (source owner)", "Confirm Jira projects, linked-ticket conventions, access, frozen references and data handling. A4 is core; E2 is NA only without a linked ticket. Required-context retrieval failure must be recorded."],
    26: ["Validate approved read-only MCP / external context", "https://docs.coderabbit.ai/knowledge-base/mcp-context", "", "Security / source owner TBD", "Confirm whether approved external context is needed and supported. Enumerate tools/data hops, constrain credentials, test denied writes and protect against embedded instructions. A PI cannot create a connector, permission or immutable snapshot."],
}
for row, values in config.items():
    put(sheet, f"A{row}:E{row}", [values])

sheet = "PR Feedback"
put(sheet, "A2", "Log real findings only. Preserve raw severity/output and manifest ID. Independently classify Useful? and False positive?. Record duplicates, not-assessable findings and harmful acted-on advice in notes. Demonstration findings are not customer PoV results.")
put(sheet, "G4:H4", [["Evidence / evaluator notes", "Origin / manifest"]])

sheet = "BVA Inputs"
put(sheet, "A2", "CSAA inputs are pending. Template sample assumptions have been cleared. Blank values are unknown, not zero; calculated savings remain blank until required inputs exist.")
input_notes = {
    6: "TBD. CSAA fully loaded senior salary and currency for the eligible cohort; no accepted amount supplied.",
    7: "TBD. CSAA eligible senior developers; distinguish actual participants from total population.",
    9: "TBD. Measure review effort from the platform's three-month baseline; no review-time percentage is agreed.",
    11: "TBD. Measure change in senior review/triage effort against the same cohort baseline. No 25% reduction is assumed.",
    15: "TBD. CSAA fully loaded junior salary and currency; no accepted amount supplied.",
    16: "TBD. CSAA eligible junior developers; no population count is assumed.",
    18: "TBD. Customer baseline for junior review-related effort; keep its definition consistent with follow-up measurement.",
    20: "TBD. Measure junior effort change; no reduction factor or savings target has been accepted.",
    24: "TBD. Actual merged PRs per month for the scoped platform/cohort; use the Phase 0 inventory.",
    26: "TBD. Independently verified distinct bugs fixed per scoped PR; do not use raw comment count as bugs.",
    28: "TBD. Historical defect escape assumptions require CSAA evidence. TPS is not production-live; do not invent its incident history.",
    30: "TBD. CSAA-supported cost per production defect, currency and scope; no generic $10,000 assumption.",
}
for row, note in input_notes.items():
    put(sheet, f"B{row}:D{row}", [["", "", note]])
formulas = {
    8: '=IF(COUNT(B6:B7)<2,"",B6*B7)',
    10: '=IF(COUNT(B8:B9)<2,"",B8*B9)',
    12: '=IF(COUNT(B10:B11)<2,"",B10*B11)',
    17: '=IF(COUNT(B15:B16)<2,"",B15*B16)',
    19: '=IF(COUNT(B17:B18)<2,"",B17*B18)',
    21: '=IF(COUNT(B19:B20)<2,"",B19*B20)',
    25: '=IF(COUNT(B24)<1,"",B24*12)',
    27: '=IF(COUNT(B25:B26)<2,"",B25*B26)',
    29: '=IF(COUNT(B27:B28)<2,"",B27*B28)',
    31: '=IF(COUNT(B29:B30)<2,"",B29*B30)',
    34: '=IF(COUNT(B12,B21,B31)<3,"",SUM(B12,B21,B31))',
}
for row, formula in formulas.items():
    put(sheet, f"B{row}", formula)
put(sheet, "D34", "A modeled potential annual benefit only after all inputs are approved. Avoid double-counting effort and defect costs; this is not measured ROI or a purchase justification.")
put(sheet, "A36", "Value targets are fewer material misses, lower senior triage/rework and sustained developer trust. Report per platform; no composite quality score or measured financial return is established.")

sheet = "Metrics"
put(sheet, "A2", "Capture CSAA baseline and PoV results separately per platform. Blank numeric inputs are not measured. Never blend native/configured or probe/live rates; usage and acceptance are context, not quality scores.")
metrics = [
    ["Active users", "", "", "TBD cohort", "Eligible-user roster and actual usage", "Confirm population and active-user definition/window. Customer PoV values are pending."],
    ["PRs reviewed", "", "", "Record scoped cohort", "Bitbucket/CR run records", "Count completed reviews and report skipped/reused/partial runs separately. Preserve PR-size spread."],
    ["PRs merged", "", "", "Record same cohort", "Bitbucket merge events", "Use the same PR cohort/window as reviewed PRs; merges do not establish review quality."],
    ["% PRs merged", '=IF(COUNT(B6:B7)<2,"",IF(B6=0,"",B7/B6))', '=IF(COUNT(C6:C7)<2,"",IF(C6=0,"",C7/C6))', "No quality target", "Merged / reviewed in the same cohort", "Blank if required inputs are missing or denominator is zero. Define cohort/cutoffs before comparison."],
    ["CR suggestions (total)", "", "", "Record raw count", "Raw export, reconciled to review records", "Preserve duplicates and not-assessable counts separately. Comment volume is not a bug or quality measure."],
    ["# suggestions accepted", "", "", "No agreed count target", "Observed code/test/spec actions", "Use actual acted-on evidence. Acceptance does not establish correctness; high-risk accepted advice needs a second human look."],
    ["Acceptance rate (overall)", '=IF(COUNT(B9:B10)<2,"",IF(B9=0,"",B10/B9))', '=IF(COUNT(C9:C10)<2,"",IF(C9=0,"",C10/C9))', "No agreed rate target", "Accepted / suggestions in same cohort", "This is not actionable rate. Blank if input is missing or denominator is zero; keep source counts."],
    ["Acceptance rate - critical", "", "", "Measure; threshold TBD", "Raw severity and acted-on evidence", "Record numerator/denominator and preserve vendor severity. Do not infer safety from acceptance."],
    ["Acceptance rate - major", "", "", "Measure; threshold TBD", "Raw severity and acted-on evidence", "Same cohort/window and original severity; no measured customer result supplied."],
    ["Acceptance rate - minor", "", "", "Measure; threshold TBD", "Raw severity and acted-on evidence", "Separate nits, duplicates and correct minor findings; raw acceptance is not actionability."],
    ["Review turnaround time", "", "", "Improvement target TBD", "Three-month baseline and matched PoV PR timing", "Use consistent start/end events and report sample size, PR size and reviewer-load confounds."],
    ["PR cycle / merge time", "", "", "Improvement target TBD", "Bitbucket timestamps for the same cohort", "Separate queue/review/author time where available. No causal productivity claim from a few PRs."],
    ["Defect escape rate", "", "", "Target TBD by platform", "Verified production defects / scoped delivery", "Requires actual baseline and exposure period. TPS is not production-live; record true NA or not measured explicitly."],
    ["Per-PR incumbent cost vs. per-seat cost", "", "", "Quote/scope TBD", "Actual incumbent spend and approved CR quote", "Align period, currency, users and PR cohort. Commercial comparison is separate from review-quality scoring."],
    ["Developer sentiment score", "", "", "End-window retrospective", "Runbook Appendix C survey", "Record not measured if absent. Trust is supporting evidence; required gates and harmful-action stop rules still control."],
    ["Actionable finding rate", "", "", ">=60% initial Green", "Independent finding classification, runbook section 15", "Phase 4 denominator excludes Duplicate and Not assessable. Partially actionable is a separate rate. Report numerator/denominator; keep probe and live rates separate."],
    ["False-positive rate", "", "", "<20% initial Green", "Independent finding classification, runbook section 15", "Include harmful false positives once in the false-positive numerator and report harm separately. Same denominator as actionability; report per platform."],
    ["Harmful findings / near misses", "", "", "None observed", "Acted-on/near-miss review and senior intervention log", "Harm count is a floor. One caught near miss is Yellow; multiple near misses or acted-on harmful advice trigger the runbook decision rules. Accepted high-risk advice gets a second look."],
    ["P1 useful replay signal", "", "", ">=40% initial Green", "Useful signal / completed comparable P1 cases", "Use locked historical/seeded cases and independent scoring. Keep the actual case inventory and completed denominator."],
    ["P9 finding overlap", "", "", ">=80% initial Green", "Matched pairs / union, runbook section 15", "Independent identical-input full/fresh runs. Same issue/location; severity differs by at most one level. Retain both raw runs and matching sheet; define both-empty handling."],
    ["Configuration effort (person-days)", "", "", "Plan about 1 person-day/platform", "Actual setup/tuning effort log", "Budget is not a measured result or cap. Separate native setup, locked R-profile configuration and later remediation."],
    ["Duplicate finding count", "", "", "Report count separately", "Independent distinct-finding classification", "Several comments on one root cause count as one distinct finding; classify the extras as Duplicate and exclude them from the quality-rate denominator."],
    ["Senior reviewer triage / rework effort (hours)", "", "", "Reduction target TBD", "Phase 0 reviewer-load baseline and matched cohort", "Measure hours spent finding issues and triaging AI advice separately. Do not assert salary savings before the CSAA inputs and effort change are established."],
    ["Not-assessable finding count", "", "", "Report count separately", "Independent missing-context classification", "Exclude correctly not-assessable findings from quality-rate denominators, but retain their count and missing source. This does not make an untested required capability NA."],
]
put(sheet, "A5:F28", metrics)

payload = {
    "date": "2026-10-23",
    "target": "https://docs.google.com/spreadsheets/d/1-8qfMIAybwQ86um90OLOXs79z6yEDkU5/edit",
    "sourceType": "Existing XLSX edited in place through Google Sheets Office editing",
    "supersedes": "The prior Google Docs mutual success plan is historical; this workbook is the current PoV plan.",
    "basis": ["DPT framework/runbook v2.5", "October 21 assessment and MSP draft", "October 23 PI candidates", "Original seven-tab PoV workbook"],
    "operations": operations,
    "successCriteriaCount": len(criteria),
    "formalEvaluationResults": "Not yet evaluated",
    "datesAndOwners": "Unconfirmed dates, contacts and commitments remain TBD; validated date/status cells retain allowed values.",
}
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "pov-plan-mapping.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"operations": len(operations), "tabs": len({x['sheet'] for x in operations}), "criteria": len(criteria)}))
