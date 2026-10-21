# Payment Central Platform Probes

Platform-specific probes for Payment Central, owned by the Payment Central lead (runbook §8.6). DPT reviews them for consistency with the core rubric.

- One file per probe, using `../_template-probe.md`. IDs: `PC1`, `PC2`, ...
- Each probe is derived from a real defect class seen on the platform and carries a locked expected finding (runbook §7.5).
- Organize probes into separate packs by workload where the platform reviews workloads differently (for example data-layer vs application-service). Omit dimensions that do not apply.
- Supply the contract artifacts that are valid probe inputs where they exist: API specifications, Swagger/OpenAPI documents, and database schema files.
- Scenarios may be synthetic defects or historical production-issue replay (runbook §5.6). The code is reviewed in a separate sanitized evaluation repository (runbook §5.5); results are documented under `../../evidence/payment-central/`.

Candidate defect classes are in runbook §8.6; the platform question list is in Appendix E.
