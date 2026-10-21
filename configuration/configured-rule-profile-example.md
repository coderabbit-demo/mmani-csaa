# Configured Rule Profile Example

> Illustrative sample only. Copy this entry into the selected platform's reviewed rule profile and replace all placeholders before locking it.

- **Platform:** `<TPS | PC | IN>`
- **Owner:** `<platform owner>`
- **Status:** draft
- **Reviewed by:**
- **Locked on:**
- **Version / commit:** `<full commit SHA>`

## Rule entries

### CFG-01: Externalize environment-specific service endpoints

- **R capability:** R6
- **Rule:** Service endpoints that vary by environment must be supplied through environment variables or an approved configuration source and configured for every required environment. Stable URI path fragments may remain application constants.
- **Why it matters:** A hardcoded endpoint can route non-production traffic to production, prevent environment promotion, or require an application release for an operational configuration change.
- **Applies when:** Application code introduces or changes a hostname, base URL, queue URL, topic ARN, or another environment-specific integration endpoint.
- **Does not apply when:** The value is an environment-independent protocol constant, such as a stable relative API path, media type, or enum value.
- **Authoritative source:** `<link or repository path to the approved platform configuration standard>`
- **Context the reviewer receives:** Application code, infrastructure or deployment configuration, and the platform environment matrix.
- **Good signal:** Identifies the specific hardcoded environment-dependent value, explains the deployment or routing risk, and points to the approved configuration mechanism.
- **Bad signal:** Generic "avoid magic strings" advice; requiring all constants to become environment variables; recommending an unrelated secrets mechanism; or missing the endpoint.
- **Cases:** `R6-PLATFORM-01-EXAMPLE`

## Configuration translation

| Field | Value |
|---|---|
| The tool under evaluation | `evidence/<platform>/configured-manifest.yaml` | `<how CFG-01 was represented>` |
