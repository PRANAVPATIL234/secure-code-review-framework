# Compliance Mapping

## Security Standards Integrated

This secure code review framework maps vulnerabilities and findings against multiple industry-recognized security standards.

---

# OWASP Top 10 Mapping

| OWASP Category | Example Detection |
|----------------|------------------|
| A01 Broken Access Control | RBAC misconfigurations |
| A02 Cryptographic Failures | MD5 usage |
| A03 Injection | SQL Injection, Command Injection |
| A05 Security Misconfiguration | Weak permissions |
| A07 Identification and Authentication Failures | Hardcoded credentials |

---

# CWE Mapping

| CWE ID | Description |
|--------|-------------|
| CWE-78 | OS Command Injection |
| CWE-89 | SQL Injection |
| CWE-327 | Broken Cryptographic Algorithm |
| CWE-798 | Hardcoded Credentials |

---

# CERT Secure Coding Mapping

| CERT Rule | Description |
|-----------|-------------|
| MSC61-J | Avoid insecure cryptographic algorithms |
| IDS00-J | Prevent injection vulnerabilities |
| FIO30-C | Exclude user input from command execution |

---

# SANS/CWE Top 25 Mapping

| SANS Category | Example |
|---------------|---------|
| Injection Flaws | SQL Injection |
| Credential Exposure | Hardcoded secrets |
| Weak Cryptography | MD5 usage |

---

# Tools Used

| Tool | Security Function |
|------|------------------|
| SonarQube | Static Analysis |
| Semgrep | OWASP SAST |
| Gitleaks | Secret Detection |
| OWASP Dependency-Check | Dependency CVE Analysis |
| Grafana | Reporting & Visualization |

---

# Compliance Objectives Achieved

- OWASP-aligned scanning
- CWE vulnerability classification
- Secure SDLC enforcement
- Centralized compliance reporting
- Automated DevSecOps security validation