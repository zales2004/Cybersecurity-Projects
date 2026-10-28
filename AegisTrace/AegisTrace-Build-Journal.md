# AegisTrace — Build Journal

> **Tagline:** Detect the threat. Trace the evidence. Verify the response.

## Project goal

Build a practical, evidence-grounded SOC investigation platform that collects endpoint telemetry, detects suspicious activity, correlates events into incident timelines, distinguishes observed facts from hypotheses, maps supported behavior to MITRE ATT&CK, maps relevant defensive techniques to MITRE D3FEND, and recommends proportionate response actions.

This is a portfolio project built and tested in an isolated lab. Claims about features will be marked complete only when there is implementation evidence and a reproducible test.

## Agreed architecture and technology stack

### Lab and telemetry
- **Ubuntu Server 24.04 LTS VM:** AegisTrace application host and Linux telemetry source.
- **Windows endpoint / host:** Windows security telemetry source.
- **Wazuh agents:** Collect endpoint telemetry from the supported lab endpoints.
- **Wazuh manager, indexer, and dashboard:** Central monitoring stack planned to run on the Windows host using Docker with WSL2.
- **VirtualBox:** Isolated VM environment for the initial single-host MVP; expand to a small virtual network only if time permits.

### AegisTrace application
- **Python + FastAPI:** Backend/API for detections, incidents, evidence, and response recommendations.
- **SQLite:** Initial local persistence for events, alerts, incidents, evidence references, and audit records.
- **Evidence-validation layer:** Checks that timeline statements and AI explanations are supported by collected event records.
- **MITRE ATT&CK:** Map observed, supported adversary behavior.
- **MITRE D3FEND:** Link relevant defensive measures to findings and recommendations.
- **AI-generated explanations:** Optional analyst assistance only; hypotheses must remain distinct from observed facts and must be checked against evidence.
- **Dashboard / API:** Present alerts, incident timelines, evidence references, confidence rationale, and recommended actions.
- **Response workflow:** Recommendations first; disruptive actions require explicit approval. Any automatic block must be lab-only, time-bounded, verified, auditable, and reversible.

## Scope priorities

**Option A — Required MVP:** One-host / single-VM flow that can be completed and demonstrated reliably.

1. Collect and normalize Linux authentication telemetry.
2. Detect repeated SSH failures and suspicious success-after-failure sequences.
3. Persist alerts and deduplicate repeated detections.
4. Correlate events into an evidence-linked incident timeline.
5. Expose incidents and evidence through a FastAPI service.
6. Validate generated explanations against the evidence records.
7. Provide ATT&CK mapping, D3FEND-oriented defensive guidance, and a clear audit trail.

**Option B — Stretch goals if the MVP is stable:** Add Windows telemetry, IP reputation enrichment, file hash lookup and local file scanning/quarantine workflow, a dashboard, and a small multi-host virtual network. Do not let stretch goals prevent a tested MVP.

## Day 1 — Setup, architecture, and baseline verification

**Day 1 objective:** Make the project layout and environment reproducible, record the agreed architecture, and verify the existing baseline before adding new features.

### Environment
- [ ] Confirm the Ubuntu Server 24.04 LTS VM boots and has network access required for the lab.
- [ ] Record VM resources, IP addressing, and the lab-only scope; do not publish private IPs or sensitive host details.
- [ ] Create or confirm the project directory on Ubuntu.
- [ ] Create/use the Python virtual environment named `.aegis` (do not use `.venv`).
- [ ] Record Python and package versions from the actual environment.
- [ ] Confirm the existing SQLite database path and inspect its schema without deleting or resetting data.
- [ ] Record how the application is started and how logs are collected.

### Existing baseline to verify against the working code
Prior project work identified these components as already implemented: Linux authentication collection, SSH detection, SQLite storage, deduplication, and alert persistence. Keep them intact. On Day 1, rerun the relevant checks and record the exact commands, outputs, and test results before marking them verified in this journal.

- [ ] Confirm Linux authentication events are collected.
- [ ] Test a controlled failed SSH login in the lab and verify the event is visible.
- [ ] Verify the detection threshold and alert fields from the actual code/configuration.
- [ ] Confirm duplicate events do not create duplicate alerts unexpectedly.
- [ ] Confirm alerts persist after restarting the application.
- [ ] Confirm the existing database and working code are preserved.

### Day 1 deliverables
- [ ] A documented project directory layout and setup commands.
- [ ] A short architecture/data-flow diagram or Mermaid diagram.
- [ ] A baseline verification record with date, commands, expected result, actual result, and evidence location.
- [ ] A list of known gaps and the next smallest implementation step.
- [ ] No credentials, tokens, unredacted logs, or private packet captures committed.

**Day 1 status:** Setup and verification checklist. Do not mark a checkbox complete until the corresponding action has actually been performed and its result recorded.

## Development roadmap after Day 1

### Milestone 2 — Harden event normalization and detections
- [ ] Define a normalized event model with timestamp, host, username, source IP, event type, outcome, and evidence reference.
- [ ] Validate required fields, timestamp parsing, and malformed events.
- [ ] Test positive and negative cases for repeated SSH failures and success-after-failure.
- [ ] Include supporting event IDs and the correlation window in each finding.

### Milestone 3 — Incident correlation and FastAPI
- [ ] Build incident records from related events.
- [ ] Expose health, alert, incident, and evidence endpoints.
- [ ] Correlate by host, account, source address, event type, and time where appropriate.
- [ ] Link every timeline observation to its supporting records.
- [ ] Show missing telemetry and plausible alternative explanations.

### Milestone 4 — Evidence validation and mappings
- [ ] Separate observed events, analyst inferences, and AI-generated hypotheses in the data model and UI.
- [ ] Validate each generated factual claim against evidence records.
- [ ] Map only supported behavior to MITRE ATT&CK.
- [ ] Map relevant defensive measures to MITRE D3FEND.
- [ ] Explain confidence using evidence coverage, source reliability, and uncertainty; do not present confidence as proof.

### Milestone 5 — Enrichment and defensive workflow
- [ ] Add optional IP reputation enrichment with source and lookup timestamp recorded.
- [ ] Add local file scanning and SHA-256 calculation in a controlled lab.
- [ ] Add hash reputation lookups only when a provider and API terms are confirmed.
- [ ] If quarantine is implemented, test restore/rollback and preserve file metadata.
- [ ] Make response recommendations auditable and require approval for disruptive actions.
- [ ] If timed blocking is implemented, test expiry and rollback in the isolated lab.

### Milestone 6 — Windows telemetry and stretch architecture
- [ ] Verify Wazuh manager/indexer/dashboard deployment and health before onboarding endpoints.
- [ ] Onboard Windows telemetry and confirm expected event fields.
- [ ] Correlate Linux and Windows events only when the evidence supports a relationship.
- [ ] Add a small virtual network only after the single-host MVP is stable.

## Session log

Use one entry for each real work session.

### Session template
- **Date:**
- **Day / milestone:**
- **Objective:**
- **Environment / versions:**
- **Files or configuration changed:**
- **Commands and tests run:**
- **Expected result:**
- **Actual result:**
- **Evidence / sanitized output:**
- **What failed or remains uncertain:**
- **Next step:**

## Evidence and safety rules

- Use only owned systems, isolated lab VMs, or explicitly authorized targets.
- Preserve existing working code and databases; inspect compatibility before modifying them.
- Do not commit passwords, API keys, access tokens, private IP details where unnecessary, personal network captures, or unredacted sensitive logs.
- Never present simulated events as real-world incident evidence.
- Do not label an event malicious without supporting context.
- Keep AI-generated hypotheses distinguishable from directly observed facts.
- Record versions, commands, tests, and limitations so another person can reproduce the result.
