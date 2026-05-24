# User Guide

## Overview

This guide explains how to use the Secure Code Review Framework.

---

# Running Security Scans

## Semgrep

semgrep --config rules/semgrep .

---

## Gitleaks

gitleaks detect --source .

---

## Dependency Check

docker run --rm -v ${PWD}:/src owasp/dependency-check --scan /src/test-app --format HTML --out /src/reports

---

# Viewing SonarQube Results

Open:

http://localhost:9000

View:
- vulnerabilities
- code smells
- security hotspots

---

# Viewing Grafana Dashboard

Open:

http://localhost:3000

Dashboard:
Secure Code Review Metrics

---

# Understanding Severity Levels

| Severity | Description |
|----------|-------------|
| Critical | Immediate remediation required |
| High | Major security risk |
| Medium | Moderate vulnerability |
| Low | Informational issue |

---

# Remediation Workflow

1. Review findings
2. Identify vulnerable code
3. Apply secure coding fixes
4. Re-run scans
5. Validate remediation

---

# Supported Security Features

- Static analysis
- Secret detection
- Dependency scanning
- CI/CD automation
- RBAC governance
- Reporting dashboards

---

# Best Practices

- Avoid hardcoded credentials
- Use strong cryptography
- Validate user input
- Keep dependencies updated
- Follow OWASP guidelines

---

# Screenshots

## SonarQube Dashboard

![SonarQube](screenshots/sonarqube-dashboard.png)

## Grafana Dashboard

![Grafana](screenshots/grafana-dashboard.png)