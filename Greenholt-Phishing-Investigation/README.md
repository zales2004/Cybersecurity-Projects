# 🔐 Greenholt PLC — Phishing Email Investigation

> **SOC Analyst | Phishing Analysis | Threat Intelligence | OSINT | Incident Response**

A hands-on phishing email investigation conducted as part of my SOC Analyst training and practical cybersecurity portfolio.

The investigation focused on analyzing a suspicious financial-transfer email, identifying indicators of compromise (IOCs), validating the threat using email/header analysis and threat intelligence, and documenting the findings in a professional SOC-style incident report.

---

## 🚨 Investigation Verdict

**TRUE POSITIVE — MALICIOUS PHISHING / BEC ATTEMPT**

The email contained multiple indicators consistent with a phishing/BEC attempt, including suspicious sender infrastructure, sender/Reply-To inconsistency, financial social engineering, and a deceptive attachment.

---

## 🎯 Investigation Objectives

- Analyze suspicious email headers
- Investigate sender and Reply-To information
- Analyze SPF, DKIM and DMARC
- Investigate originating IP and domain
- Analyze suspicious attachment and file hash
- Perform OSINT and threat intelligence research
- Identify Indicators of Compromise (IOCs)
- Map observed techniques to MITRE ATT&CK
- Determine the final alert classification
- Recommend SOC remediation actions
- Document the investigation in a professional incident report

---

## 🔎 Investigation Process

### 1. Email Analysis

Investigated:

- Sender address
- Display name
- Reply-To address
- Return-Path
- Originating IP
- Transfer reference
- Email content and social-engineering indicators

### 2. Email Authentication

Reviewed:

- SPF
- DKIM
- DMARC

Authentication results were evaluated together with other email artifacts rather than being treated as proof of legitimacy on their own.

### 3. Attachment Analysis

**Attachment:**
`SWT_#09674321____PDF__.CAB`

**SHA-256:**
`2e91c533615a9bb8929ac4bb76707b2444597ce063d84a4b33525e25074fff3f`

The attachment presented a file-type mismatch, with analysis identifying it as a **RAR archive** despite the deceptive filename/extension.

### 4. Threat Intelligence & OSINT

Practiced using security analysis and threat-intelligence platforms including:

- VirusTotal
- URLScan.io
- ANY.RUN
- Sandbox analysis
- IP/domain reputation checks
- IOC investigation

---

## 🚩 Key Indicators

| Indicator | Value |
|---|---|
| Sender | `info@mutawamarine.com` |
| Reply-To | `info.mutawamarine@mail.com` |
| Originating IP | `192.119.71.157` |
| Domain | `mutawamarine.com` |
| Attachment | `SWT_#09674321____PDF__.CAB` |
| SHA-256 | `2e91c533615a9bb8929ac4bb76707b2444597ce063d84a4b33525e25074fff3f` |

---

## 🧠 MITRE ATT&CK Mapping

| Technique | Description |
|---|---|
| **T1566** | Phishing |
| **T1566.001** | Spearphishing Attachment |
| **T1036** | Masquerading |

---

## 🚨 SOC Assessment

**Classification:** `TRUE POSITIVE`

**Severity:** `High`

The combination of financial social engineering, sender/Reply-To inconsistency, suspicious infrastructure, unsolicited attachment, and file-type mismatch strongly supports classification as a malicious phishing/BEC attempt.

---

## 🛡️ Recommended Response

- Quarantine the malicious email
- Search the environment for related IOCs
- Identify other recipients of the same campaign
- Block malicious sender/domain indicators where appropriate
- Analyze the attachment in an isolated sandbox
- Check endpoint telemetry for execution
- Investigate user interaction with the email
- Reset credentials if compromise is confirmed

---

## 📄 Investigation Report

A professional SOC-style incident investigation report was created documenting:

- Investigation findings
- Email artifacts
- Authentication analysis
- Attachment analysis
- IOCs
- Threat assessment
- MITRE ATT&CK mapping
- Recommended remediation

**Analyst:** Alen Sales K S

> Investigated, analyzed, reported, and documented as part of my practical SOC Analyst training.

---

## 🧰 Skills Demonstrated

`Phishing Analysis` `Email Security` `Threat Intelligence` `OSINT`  
`IOC Analysis` `Incident Response` `MITRE ATT&CK` `Malware Analysis`  
`SPF` `DKIM` `DMARC` `VirusTotal` `URLScan` `ANY.RUN`

---

## 📌 Disclaimer

This investigation was performed in a controlled cybersecurity training/lab environment for educational and defensive security purposes.


---

## Portfolio navigation

This repository is part of my hands-on cybersecurity learning portfolio by **Alen Sales K S**. I document lab work to make the methodology, evidence, limitations, and lessons learned easier to review.

- [SOC Alert Triage](https://github.com/zales2004/soc-alert-triage-investigation-thm-Soc-simulator)
- [Splunk SOC L1 Investigation](https://github.com/zales2004/splunk-soc-l1-incident-investigation)

## Scope and responsible use

All security testing described here is for authorized training environments, intentionally vulnerable targets, or systems I own or have permission to assess. Findings should be interpreted in the context of the documented lab and supporting evidence; they should not be treated as proof of compromise on unrelated real-world systems.
