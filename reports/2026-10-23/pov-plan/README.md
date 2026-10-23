# Current CSAA PoV plan

The [shared seven-tab workbook](https://docs.google.com/spreadsheets/d/1-8qfMIAybwQ86um90OLOXs79z6yEDkU5/edit)
is the current PoV plan. It replaces the prior Google Docs mutual success plan,
which is retained only as a historical snapshot. The provided XLSX was edited in
place through Google Sheets Office editing, retaining its identity, sharing,
tab order, template comments, dropdowns and merged sections.

## Mapping

| Tab / range | Mapped content |
| --- | --- |
| Overview A2:D28 | Customer, proposed relative dates/cadence, platform and repository scope, context integrations, known DPT leads, unconfirmed contacts and source links. |
| Success Criteria A5:D15 | Eleven criteria covering context, specifications, external retrieval, configuration, review quality, agent/local workflow, human/security gates, test/concurrency/failure risks, domain/platform coverage, adoption/trust and pilot decisions. Every outcome remains Not yet evaluated. |
| Milestone Tracker A6:G31 | Phase 0 readiness, Day 0-2 gates, Week 1 checkpoint, separate configured/domain work, approved Weeks 2-3 adoption, Week 3 readout and conditional commercial/rollout activities. Date cells remain blank until actual dates are agreed. |
| Configuration Checklist A4:E26 | Bitbucket setup authority and runtime scopes, approved repositories/users, source/configuration freeze, path-instruction candidates, public evidence export and read-only context controls. Drafting a candidate does not mean it has been deployed. |
| PR Feedback A2:H19 | Evidence-capture guidance and clearer origin/manifest columns. The finding log remains empty; no demonstration PRs or results were invented. |
| BVA Inputs A2:D36 | Generic salary/headcount/reduction/defect assumptions cleared. Required customer inputs remain blank, with explanatory notes. Existing calculation relationships now stay blank until numeric prerequisites are supplied. |
| Metrics A5:F28 | Usage, acceptance, timing, financial comparison and trust definitions, plus distinct actionability, false positives, harm, P1 replay, P9 overlap, configuration effort, duplicate and not-assessable counts, and reviewer hours. Baseline/result inputs remain unmeasured. |

The basis is DPT framework/runbook v2.5, the October 21 assessment/MSP draft and
the [October 23 PI candidates](../path-instruction-candidates.json). The live
workbook links to the runbook and candidate library. It does not depend on the old
Google Doc for ongoing plan updates.

## Decisions and unknowns

- Joint acceptance, calendar dates, participant/repository counts, named
  CodeRabbit owners, email addresses and commercial commitments remain pending.
- Blank milestone/configuration statuses mean unconfirmed. In progress can
  indicate preparation of draft material, as described in the row notes; it does
  not establish customer approval or a passed gate.
- The template's Week 4 readout was mapped to the proposed end of Week 3 per
  platform. Approved extensions or an earlier stop must be recorded.
- Actionability and suggestion acceptance are separate measures. Quality-rate
  denominators exclude Duplicate and Not assessable; partially actionable stays
  separate. Keep probe/live and native/configured results separate, with no
  composite or cross-platform averaging.
- The live-use/disposable-only conflict and NA/not-tested distinctions still
  require an owner decision. Written risk records, permission enforcement and
  actual execution evidence cannot be replaced by prompts.
- No formal evaluation was executed or re-scored during this mapping. Existing
  demonstration observations are not customer PoV results. No measured ROI,
  vendor selection, contract or production-rollout commitment is asserted.

## Snapshots and verification

- `csaa-pov-plan.xlsx` is a download of the completed file, not a replacement
  workbook uploaded under a new ID.
- `source-templates/csaa-pov-plan-original.xlsx` preserves the supplied template.
- `pov-plan-mapping.json` records the scoped cell mapping; `build_mapping.py`
  regenerates that mapping without editing a workbook or calling a service.
- `validation.json` records cell readback, formula, dropdown, comment, merge and
  scope-preservation checks. All seven populated views were inspected in the
  external Chrome work profile.

Drive edits do not automatically update Git snapshots. Export and check in later
revisions with their date/basis recorded. Review automation remains disabled in
the tracking repository; no PIs were applied to an evaluation configuration.
