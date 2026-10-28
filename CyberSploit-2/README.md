# CyberSploit 2 — CTF Walkthrough

A complete hands-on penetration testing walkthrough of the **CyberSploit 2** vulnerable CTF machine, covering reconnaissance, service enumeration, web enumeration, credential discovery, SSH access, local enumeration, Docker-based privilege escalation, and root-level compromise.

> **Lab Environment:** Authorized vulnerable CTF / virtual machine  
> **Attacker Machine:** Kali Linux  
> **Target:** CyberSploit 2  
> **Focus:** Web Reconnaissance, Credential Discovery, SSH, Docker Security & Linux Privilege Escalation

---

## 🎯 Objective

The objective of this assessment was to identify the exposed attack surface, discover credential-related information through web enumeration, obtain an initial SSH foothold, perform local enumeration, identify Docker as a privilege-escalation vector, and ultimately obtain root-level access.

### Attack Chain


Reconnaissance
      ↓
Nmap Enumeration
      ↓
HTTP Service
      ↓
Web Source Analysis
      ↓
Credential Discovery
      ↓
ROT47 Decoding
      ↓
SSH Access
      ↓
Local Enumeration
      ↓
Docker Discovery
      ↓
Host Filesystem Mount
      ↓
chroot
      ↓
Root Access
      ↓
Flag Discovery


---

## 🖥️ Target Information

| Item                 | Details                 |
| -------------------- | ----------------------- |
| Machine              | CyberSploit 2           |
| Target IP            | 192.168.29.79           |
| Open Services        | 22/tcp SSH, 80/tcp HTTP |
| SSH Version          | OpenSSH 8.0             |
| Web Server           | Apache 2.4.37           |
| Initial User         | shailendra              |
| Initial Access       | SSH                     |
| Privilege Escalation | Docker                  |
| Final Privilege      | root                    |
| Flag Location        | `/root/flag.txt`        |

---

## 🛠️ Tools Used

* Kali Linux
* Nmap
* SSH
* Browser
* HTML Source Inspection
* ROT47
* Linux Command-Line Utilities
* Docker
* chroot

---

# 🔎 Walkthrough

## 1. Reconnaissance

The first step was identifying the target and enumerating the services exposed by the machine.

Nmap service detection was performed using:

bash
nmap -sV 192.168.29.79


The scan revealed:

text
22/tcp  SSH
80/tcp  HTTP


The HTTP service was prioritized for further information gathering.



## 🌐 2. Web Enumeration

The HTTP service was opened in a browser and the webpage was inspected.

The page contained credential-related information in the form of a:

text
Username / Password / Handle

table.

Further inspection of the HTML source revealed an encoded-looking value together with a **ROT47** clue.

The encoded value identified during the lab was:

text
D92:=6?5C2 / 4J36CDA=@:E`


The ROT47 clue provided the direction for decoding the value and continuing the credential-discovery process.

### Key Lesson

Web enumeration should not stop at the visible webpage.

During a CTF assessment, inspect:

* HTML source
* Comments
* Hidden fields
* JavaScript
* Linked resources
* `robots.txt`
* Metadata
* Encoded or obfuscated strings

---

# 🔐 3. Credential Discovery

The encoded-looking value was analyzed using the ROT47 clue.

The decoding process resulted in credentials that could be tested against the exposed SSH service.

The discovered username was:

```text
shailendra
```

This provided the information required to attempt SSH authentication.

### Security Lesson

**Obfuscation is not encryption.**

ROT47 is not a secure method for protecting passwords or sensitive credentials.

---

# 🔑 4. SSH Initial Access

Since SSH was exposed on port 22 and valid credentials had been identified, SSH access was attempted:

```bash
ssh shailendra@192.168.29.79
```

Authentication succeeded and an interactive shell was obtained:

```text
[shailendra@localhost ~]$
```

This established the initial foothold on the target.

---

# 🕵️ 5. Local Enumeration

After gaining SSH access, local enumeration was performed.

The home directory contained:

```text
hint.txt
```

The hint was inspected and returned:

```text
docker
```

This indicated that Docker should be investigated as a potential privilege-escalation vector.

### Key Lesson

Initial access is not the end of the assessment.

After obtaining a low-privileged shell, investigate:

* Current user
* Groups
* Sudo permissions
* Running services
* Installed software
* Docker
* SUID binaries
* Cron jobs
* File permissions
* Kernel version
* Interesting files
* Configuration files
* Local hints

---

# 🐳 6. Docker Privilege Escalation

The lab identified Docker as the key privilege-escalation path.

The demonstrated command was:

```bash
docker run -v /:/mnt --rm -it alpine chroot /mnt bash
```

### Command Breakdown

#### `docker run`

Creates and starts a Docker container.

#### `-v /:/mnt`

Mounts the host filesystem `/` inside the container at:

```text
/mnt
```

Conceptually:

text
Host Filesystem
       /
       │
       │ Docker Volume Mount
       ▼
Container
       │
       ▼
      /mnt


`--rm`

Removes the container after it exits.

#### `-it`

Provides an interactive terminal.

#### `alpine`

Uses the Alpine Linux container image.

#### `chroot /mnt bash`

Changes the apparent root directory to `/mnt` and launches Bash.

Because `/mnt` contains the host filesystem, this provides access to the host environment.

The resulting shell was then verified as root.

---

# 👑 7. Root Verification

After executing the Docker-based privilege-escalation technique, the resulting privileges were verified.

`bash
whoami


Result:

`text
root


Additional verification:

```bash
id
```

Successful `whoami` output confirmed that root-level access had been obtained.

---

# 🚩 8. Flag Discovery

After obtaining root access, the `/root` directory was inspected.

The final flag was located at:

text
/root/flag.txt

Reading the file produced:




# 📊 Findings

| ID   | Finding                                               | Impact                     |
| ---- | ----------------------------------------------------- | -------------------------- |
| F-01 | Credential-related information exposed in web content | Initial Access             |
| F-02 | ROT47 used as simple obfuscation                      | Credential Disclosure      |
| F-03 | SSH exposed with usable credentials                   | Remote Access              |
| F-04 | Docker capability enabled host filesystem access      | Critical / Root Compromise |

---

# 🔗 Complete Attack Chain


01. RECONNAISSANCE
        │
        ▼
192.168.29.79
        │
        ▼
02. NMAP
        │
        ├── 22/tcp SSH
        └── 80/tcp HTTP
        │
        ▼
03. WEB ENUMERATION
        │
        ▼
HTML / Credential Information
        │
        ▼
04. ROT47
        │
        ▼
Credential Discovery
        │
        ▼
05. SSH
        │
        ▼
shailendra
        │
        ▼
06. LOCAL ENUMERATION
        │
        ▼
hint.txt → docker
        │
        ▼
07. DOCKER
        │
        ▼
Host / → Container /mnt
        │
        ▼
08. chroot
        │
        ▼
whoami → root
        │
        ▼
09. FLAG
        │
        ▼
/root/flag.txt
```

---

# 🧠 Key Takeaways

### 1. Enumerate Before Exploiting

Identify available services and understand the attack surface before attempting exploitation.

### 2. Inspect Web Source

The visible webpage is not always the complete application.

HTML source code and exposed resources can reveal sensitive information.

### 3. Understand Encoding

ROT47 provides obfuscation but does not provide secure protection for credentials.

### 4. Validate Discovered Credentials

When credentials are discovered, determine which exposed services can legitimately authenticate the account.

### 5. Enumerate After Initial Access

Once a shell is obtained, perform another enumeration phase focused on privilege escalation.

### 6. Understand Docker Security

Excessive Docker privileges can become a serious security risk when containers can access the host filesystem.

### 7. Verify Privilege Escalation

Never assume that a privilege-escalation technique succeeded.

Use:

```bash
whoami
id
```

to verify the resulting privilege level.

### 8. Follow the Principle of Least Privilege

Users and services should only have the permissions required for their intended functions.

---

# 🛡️ Security Recommendations

The demonstrated attack path highlights several defensive improvements:

* Remove credentials from publicly accessible web content.
* Never use ROT47 or similar encoding as password protection.
* Restrict Docker administrative privileges.
* Apply least-privilege principles.
* Harden SSH authentication and access controls.
* Monitor suspicious container creation.
* Monitor containers using sensitive host filesystem mounts.
* Keep the operating system patched.
* Keep exposed services updated.
* Regularly review user and service permissions.

---


---

# ⚠️ Disclaimer

This repository is intended strictly for:

* Authorized CTF competitions
* Vulnerable virtual machines
* Cybersecurity training
* Educational laboratories
* Authorized penetration-testing environments

Do not use these techniques against systems without explicit authorization.

---

# 👤 Author

**Alen**


---

## Portfolio navigation

This repository is part of my hands-on cybersecurity learning portfolio by **Alen Sales K S**. I document lab work to make the methodology, evidence, limitations, and lessons learned easier to review.

- [Cybersploit 1 CTF Walkthrough](https://github.com/zales2004/cybersploit-1-ctf-walkthrough)
- [Metasploitable 2 Lab](https://github.com/zales2004/metasploitable-2-ctf-walkthrough)
- [Sunset: Noontide](https://github.com/zales2004/sunset-noontide-pentesting)

## Scope and responsible use

All security testing described here is for authorized training environments, intentionally vulnerable targets, or systems I own or have permission to assess. Findings should be interpreted in the context of the documented lab and supporting evidence; they should not be treated as proof of compromise on unrelated real-world systems.
