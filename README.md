# Cybersecurity-task-15

Project Overview

This project demonstrates a complete Vulnerability Assessment and Risk Prioritization process using Nessus Essentials.

The objective was to:

Identify vulnerabilities in a target Ubuntu system

Map findings to CVE and CVSS scores

Classify vulnerabilities based on severity and impact

Prioritize remediation efforts

1. Scope of Assessment

Target System:

Ubuntu 25.04 (Host-only lab network)

IP Address: 192.168.195.130

Scan Type:

Basic Network Scan (Nessus Essentials)

🛠 Tools Used

Nessus Essentials

Ubuntu Server (Target)

Kali Linux (Scanner machine)

Python (Risk prioritization automation)

Excel (Risk matrix creation)

🔍 Steps Performed (Based on Mini Guide)
1️⃣ Defined Scope

Targeted Ubuntu server within isolated lab network.

2️⃣ Configured Scanner

Enabled service detection

Enabled OS detection

Enabled vulnerability plugins

3️⃣ Ran Vulnerability Scan

Executed full scan and monitored plugin execution.

4️⃣ Reviewed Vulnerabilities

Identified:

Open SSH service

Outdated packages

Weak SSH configuration

Missing security patches

5️⃣ Mapped to CVE & CVSS

Each vulnerability mapped to:

CVE ID

CVSS v3 Score

Severity (Critical/High/Medium/Low)

6️⃣ Classified by Risk

Used: Risk = CVSS Score × Asset Value × Exploitability

7️⃣ Prioritized

Critical vulnerabilities addressed first.

8️⃣ Recommended Remediation

Provided patching and configuration hardening recommendations.

2. Vulnerability Assessment Report 

A vulnerability assessment was conducted on Ubuntu server (192.168.195.130).

Total Findings:

Critical: 2

High: 4

Medium: 6

Low: 3

Key Risk: Outdated OpenSSH version vulnerable to brute force and potential exploitation.

Sample Findings Table
Vulnerability	CVE	CVSS	Severity	Risk Level
OpenSSH Outdated	CVE-2023-38408	9.8	Critical	High
Weak SSH Config	N/A	7.5	High	High
Missing Security Updates	Multiple	8.1	High	High
TLS Weak Cipher	CVE-2021-3449	5.9	Medium	Medium

Risk Priority List
High Priority

Patch OpenSSH immediately

Disable password authentication

Enable Fail2Ban

Medium Priority

Remove weak ciphers

Enable firewall rules

Low Priority

Disable unused services
