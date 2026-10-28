# NetTrace — Network Traffic Analysis & Security Investigation

NetTrace is a hands-on cybersecurity project focused on **network traffic analysis using Wireshark**. The project analyzes an authorized home-LAN packet capture to understand network communication, investigate protocols, and identify security-relevant events.

## 🔍 What This Project Covers

- Protocol hierarchy analysis
- Network endpoint and conversation analysis
- DNS traffic investigation
- HTTP traffic analysis
- TLS and QUIC traffic analysis
- TCP retransmission analysis
- I/O Graph traffic visualization
- Wireshark Expert Information
- Security findings and recommendations

## 📊 Capture Overview

- **Packets analyzed:** 132,793
- **Tool:** Wireshark
- **Focus:** Network Security / PCAP Analysis / SOC Investigation

## 🛡️ Key Findings

The investigation identified:

- Significant TCP, UDP, TLS, and QUIC traffic
- DNS queries to public DNS resolvers
- A router administration interface accessible over HTTP
- TCP retransmissions and connection resets
- Encrypted QUIC/TLS traffic
- Various network events identified through Wireshark Expert Information

The analysis follows an **evidence-based approach** and does not classify normal network behavior as malicious without supporting evidence.

## 📄 Project Report

The complete analysis, screenshots, methodology, findings, and recommendations are available in the report:

## 🧰 Technologies & Skills

**Wireshark • PCAP Analysis • TCP/IP • DNS • HTTP • TLS • QUIC • Network Troubleshooting • Network Security • SOC Analysis**

## 🎯 Objective

The objective of NetTrace is to demonstrate practical ability to **capture, filter, investigate, interpret, and document network traffic using Wireshark** in a security-focused investigation workflow.

> **Note:** This project was performed using an authorized home-LAN packet capture. The raw PCAP is not included to protect private network and DNS information.
