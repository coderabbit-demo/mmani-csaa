# Repository purpose

This repository tracks the CSAA AI code review evaluation framework, its CodeRabbit
assessment, requirements, mitigations, decisions and eventual evaluation evidence.

## No code reviews

- Do not run CodeRabbit or another code review agent in this repository.
- Do not open a pull request to obtain a code review or add review automation.
- Keep `.coderabbit.yaml` configured to disable automatic reviews and exclude all
  paths from review.
- Commit authorized tracking and documentation changes directly to the repository.
  If branch protection requires a pull request, surface that constraint instead of
  weakening protections.

## Evaluation integrity

- Preserve the original framework requirements and their source references.
- Keep proposed mitigations separate from executed and validated results.
- Keep locked answer keys out of any repository or context supplied to the tool
  under evaluation. This tracking repository is not a probe execution repository.
- Preserve existing evidence and frozen results when adding a later assessment.
- Use `TRACKING.md` for the repository index and `reports/` for dated reports.
