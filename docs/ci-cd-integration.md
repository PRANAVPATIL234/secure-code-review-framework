# CI/CD Integration

## Overview

The framework integrates with GitHub Actions to automate security scanning during software development workflows.

---

# CI/CD Workflow

Developer Push / Pull Request
↓
GitHub Actions
↓
Semgrep Scan
↓
Gitleaks Scan
↓
Dependency-Check Scan
↓
Security Reports

---

# GitHub Actions Workflow

Location:

.github/workflows/security-pipeline.yml

---

# Integrated Jobs

| Job | Purpose |
|-----|---------|
| Semgrep | SAST scanning |
| Gitleaks | Secret detection |
| Dependency-Check | CVE scanning |

---

# Security Quality Gates

The pipeline:
- blocks vulnerable commits
- detects secrets
- prevents insecure merges
- enforces secure SDLC

---

# CI/CD Features

- Automated scanning
- Parallel execution
- Pull request validation
- Severity-based detection
- Security enforcement

---

# GitHub Secrets

Configured Secret:

| Secret | Purpose |
|--------|---------|
| SONAR_TOKEN | SonarQube authentication |

---

# Benefits

- Continuous security validation
- Reduced manual effort
- Faster vulnerability detection
- Automated DevSecOps workflow

---

# Screenshots

Add screenshots here.

## GitHub Actions Workflow

![GitHub Actions](screenshots/github-actions.png)