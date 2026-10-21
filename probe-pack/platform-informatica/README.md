# Informatica ETL Platform Probes

Platform-specific probes for Informatica ETL, owned by the Informatica lead (runbook §8.6). DPT reviews them for consistency with the core rubric.

- One file per probe, using `../_template-probe.md`. IDs: `IN1`, `IN2`, ...
- Each probe is derived from a real defect class seen on the platform and carries a locked expected finding (runbook §7.5).
- Organize probes into separate packs by workload where that helps; omit dimensions that do not apply (for example AWS/serverless).
- Supply the contract artifacts that are valid probe inputs where they exist: API specifications, Swagger/OpenAPI documents, mapping/parameter files, and database schema files.
- Scenarios may be synthetic defects or historical production-issue replay (runbook §5.6). The code is reviewed in a separate sanitized evaluation repository (runbook §5.5); results are documented under `../../evidence/informatica-etl/`.

Informatica code is held in a common repository; for the initial evaluation it is copied into a disposable sanitized clone and is not modified in place (runbook §5.5).

Build Informatica probes only if Informatica changes are reviewed in Bitbucket PRs (Appendix E, question 12); otherwise the Informatica row is recorded as "not reviewable by this tool category."
