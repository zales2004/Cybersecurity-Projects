# Enterprise Active Directory SOC & PAM Lab

A hands-on Enterprise Security Operations Center (SOC) laboratory built to demonstrate Active Directory security monitoring, Windows security auditing, Splunk SIEM integration, detection engineering, controlled security testing, privileged-access monitoring, and evidence-driven incident investigation.

## Overview

This project simulates an enterprise-style Active Directory security monitoring environment using Windows Server 2022, Active Directory, Splunk Enterprise, Splunk Universal Forwarder, Kali Linux, Windows Defender Firewall, and VirtualBox.

The laboratory follows a practical SOC workflow:

**Build → Audit → Collect → Detect → Investigate → Document**

The objective is not simply to deploy security tools, but to demonstrate how a SOC analyst can collect Windows security telemetry, identify relevant activity, correlate events, investigate security scenarios, develop reusable SPL detections, and document findings using evidence.

## Environment

The laboratory consists of three primary systems:

- **DC01** — Windows Server 2022 / Active Directory Domain Controller — `192.168.56.101`
- **Kali Linux** — Controlled security-testing host — `192.168.56.102`
- **Splunk Enterprise** — SIEM, indexing, search, and investigation platform — `192.168.56.1`

Windows telemetry generated on DC01 is collected using **Splunk Universal Forwarder 10.4.3** and forwarded to Splunk Enterprise over **TCP 9997**.

The Active Directory domain used in the laboratory is:

**`corp.local`**

## Active Directory & Privileged Access

The Active Directory environment was organized into separate identity areas for standard users, administrative identities, security identities, service accounts, server accounts, and temporary SOC-testing identities.

Privileged access was represented through groups including:

- `IT-Admins`
- `Security-Admins`
- `PAM-Admins`
- `Domain Admins`
- `Group Policy Creator Owners`

The project uses Active Directory security events to provide PAM-oriented visibility into privileged group membership changes.

Event IDs **4728** and **4729** were used to identify additions and removals from security-enabled global groups, allowing the investigation of who was added or removed, which group was affected, and when the change occurred.

## Security Auditing & Telemetry

Advanced Audit Policy was configured on DC01 to generate security telemetry covering:

- Authentication
- Account management
- Privileged activity
- Process creation
- Directory services
- Policy changes
- File and registry activity
- Sensitive privilege use
- System security activity

Key Windows Event IDs investigated throughout the project include:

- **4624** — Successful Logon
- **4625** — Failed Logon
- **4688** — Process Creation
- **4720** — User Account Created
- **4722** — User Account Enabled
- **4724** — Password Reset
- **4725** — User Account Disabled
- **4726** — User Account Deleted
- **4728** — Member Added to Security-Enabled Global Group
- **4729** — Member Removed from Security-Enabled Global Group
- **4738** — User Account Changed

## SOC Investigations

The laboratory contains multiple investigation scenarios designed around realistic Windows and Active Directory security telemetry.

### Authentication Investigation

Successful and failed authentication events were correlated using timestamp, source IP, username, and logon type.

Controlled activity from the Kali testing host was investigated to identify sequences of failed authentication followed by successful authentication.

### Account Lifecycle Investigation

A temporary `soc.audit` identity was used to simulate account manipulation.

The observed lifecycle included account creation, privileged group assignment, account modification, disable/enable activity, password reset, and eventual deletion.

This demonstrated how a SOC analyst can reconstruct an identity lifecycle by correlating multiple Windows security events rather than investigating each event in isolation.

### Privileged Group Investigation

Active Directory group membership changes were investigated using Events 4728 and 4729.

The investigation focused on:

- Member identity
- Target group
- Acting account
- Domain context
- Timestamp
- Event type

### Process Execution Investigation

Windows Event ID 4688 was used to investigate selected process execution activity.

The dashboard focused on processes such as:

- `cmd.exe`
- `powershell.exe`
- `reg.exe`
- `rundll32.exe`
- `wevtutil.exe`
- `taskkill.exe`
- `curl.exe`
- `ipconfig.exe`

These processes were treated as investigation leads rather than automatically malicious activity. Their significance depends on additional context such as the executing user, parent process, command line, network activity, timestamp, and surrounding security events.

### Firewall Investigation

Windows Defender Firewall logging was enabled and forwarded to Splunk.

A controlled ICMP blocking scenario generated firewall telemetry showing repeated traffic from Kali Linux to DC01 being blocked.

Source: `192.168.56.102`

Destination: `192.168.56.101`

Protocol: `ICMP`

Action: `DROP`

## Controlled Security Testing

Security-testing activities were performed only within the isolated laboratory environment.

Testing included LDAP authentication testing, controlled failed authentication, network connectivity testing, firewall blocking, and command/discovery activity.

An example LDAP authentication test used:

`hydra -l soc.test -P hydra-test.txt ldap2://192.168.56.101`

Controlled Windows authentication testing used:

`runas /user:corp\john cmd.exe`

The resulting Windows and network telemetry was collected and investigated through Splunk.

## Splunk & Detection Engineering

Splunk Enterprise serves as the centralized SIEM platform for the laboratory.

The project uses SPL to transform raw Windows telemetry into focused detection and investigation searches.

XML Windows events were parsed using `xmlkv`, while `rex` was used for explicit extraction of required XML fields.

Detection and investigation searches were developed for:

- Authentication failures
- Authentication timelines
- Account creation and modification
- Account enable/disable activity
- Password resets
- Account deletion
- Privileged group membership
- Process execution
- Firewall activity

This provides a reusable investigation layer rather than relying only on manual inspection of raw Windows events.

## Splunk SOC Dashboard

The project includes an **Active Directory SOC Monitoring Dashboard** designed as the analyst-facing investigation interface.

The dashboard provides visibility into:

- Total Events by Data Source
- Failed Logon Count
- Successful Logon Count
- Suspicious Authentication Activity
- Authentication Incident Summary
- Account Management Activity
- Account Activity by Event Type
- Account Manipulation & Privilege Escalation
- Privilege / Group Membership Changes
- Interesting Process Executions
- Firewall Activity
- Network Threat Blocking

A captured dashboard snapshot contained:

- **58,056** Security events
- **3,235** System events
- **417** PowerShell Operational events
- **61** Windows Firewall events
- **15** failed logons
- **7,934** successful logons
- **104** account-change events
- **32** account-creation events
- **29** password-reset events
- **26** account-enable events
- **1** account deletion event
- **1** account disable event

## Project Outcome

The completed laboratory demonstrates an end-to-end SOC workflow beginning with Windows and Active Directory infrastructure deployment and continuing through security auditing, centralized telemetry collection, detection engineering, investigation, dashboard development, and incident documentation.

The project demonstrates practical exposure to:

- SOC monitoring
- SIEM operations
- Splunk
- SPL
- Windows Event Log analysis
- Active Directory security
- Authentication investigation
- Account lifecycle monitoring
- Privileged-access monitoring
- PAM-oriented monitoring
- Process execution analysis
- Firewall monitoring
- Detection engineering
- Security investigation
- Incident documentation

## Documentation

Two separate professional reports are included with the project:

### Enterprise Active Directory SOC & PAM Project Report

The complete project report documenting the laboratory architecture, Windows Server and Active Directory implementation, privileged-access model, security auditing, Splunk integration, firewall monitoring, controlled testing, SOC investigations, detection engineering, dashboard design, SOC workflow, outcomes, and limitations.

### Splunk Active Directory SOC Monitoring Dashboard Report

A dedicated dashboard report containing the actual Splunk dashboard evidence, authentication findings, account monitoring results, privileged-group activity, process execution evidence, and firewall-blocking investigation.

## Technologies

**Windows & Identity:** Windows Server 2022, Active Directory Domain Services, Advanced Audit Policy

**SIEM & Detection:** Splunk Enterprise, Splunk Universal Forwarder 10.4.3, Splunk SPL, Windows Event Logs

**Security Testing:** Kali Linux, LDAP authentication testing, controlled network testing

**Network & Infrastructure:** Windows Defender Firewall, VirtualBox, Host-Only Networking

## Scope

This is a controlled cybersecurity laboratory created for hands-on SOC training and portfolio demonstration.

Security activity was intentionally generated inside the isolated environment. The observed events represent controlled investigation scenarios and do not independently establish confirmed real-world compromise.

The PAM component demonstrates PAM-oriented privileged-access monitoring using Active Directory groups and Windows security telemetry. It does not represent deployment of a commercial enterprise PAM platform.

## Author

**Alen Sales K S**

B.Tech Computer Science & Engineering  
Cybersecurity / SOC Enthusiast

---

⭐ **Enterprise Active Directory SOC & PAM Lab — Security Monitoring, Detection Engineering, Investigation & Evidence-Driven SOC Operations**


---

## Portfolio navigation

This repository is part of my hands-on cybersecurity learning portfolio by **Alen Sales K S**. I document lab work to make the methodology, evidence, limitations, and lessons learned easier to review.

- [NetTrace — Network Traffic Analysis](https://github.com/zales2004/NetTrace)
- [Splunk SOC L1 Investigation](https://github.com/zales2004/splunk-soc-l1-incident-investigation)
- [Greenholt Phishing Investigation](https://github.com/zales2004/greenholt-phishing-investigation)

## Scope and responsible use

All security testing described here is for authorized training environments, intentionally vulnerable targets, or systems I own or have permission to assess. Findings should be interpreted in the context of the documented lab and supporting evidence; they should not be treated as proof of compromise on unrelated real-world systems.
