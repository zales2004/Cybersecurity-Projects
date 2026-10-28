# splunk-soc-l1-incident-investigation
SOC L1 incident investigation using Splunk, authentication log analysis, detection queries, and security monitoring dashboard.
Overview
SOC L1 investigation project using **Splunk Enterprise** to analyze authentication logs, detect suspicious login activity, and monitor security events.

Tools
- Splunk Enterprise
- SPL
- Authentication Logs
- SIEM / SOC Investigation

Investigation
- Ingested authentication logs into Splunk
- Analyzed successful and failed logins
- Identified suspicious source IPs
- Investigated repeated failed login attempts
- Correlated login activity with privilege escalation
- Created a SOC monitoring dashboard

 Key Finding
Multiple failed login attempts were identified from:

`185.220.**.**`

The activity was followed by a successful `admin` login and a `PRIVILEGE_ESCALATION` event, making the sequence suspicious.


---

## Portfolio navigation

This repository is part of my hands-on cybersecurity learning portfolio by **Alen Sales K S**. I document lab work to make the methodology, evidence, limitations, and lessons learned easier to review.

- [NetTrace — Network Traffic Analysis](https://github.com/zales2004/NetTrace)
- [Active Directory SOC & PAM Lab](https://github.com/zales2004/Enterprise-Active-Directory-Pam-Soc-Lab)
- [Greenholt Phishing Investigation](https://github.com/zales2004/greenholt-phishing-investigation)

## Scope and responsible use

All security testing described here is for authorized training environments, intentionally vulnerable targets, or systems I own or have permission to assess. Findings should be interpreted in the context of the documented lab and supporting evidence; they should not be treated as proof of compromise on unrelated real-world systems.
