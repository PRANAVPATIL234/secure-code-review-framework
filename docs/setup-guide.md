# Setup Guide

## Prerequisites

- Docker Desktop
- Git
- Python 3.x
- GitHub Account
- Windows/Linux/macOS

---

# Step 1 — Clone Repository

git clone <repository-url>

cd secure-code-review-framework

---

# Step 2 — Start SonarQube

docker-compose up -d

---

# Step 3 — Access SonarQube

URL:
http://localhost:9000

Default Credentials:
- Username: admin
- Password: admin

---

# Step 4 — Install SonarScanner

Download SonarScanner CLI and add it to PATH.

Verify installation:

sonar-scanner --version

---

# Step 5 — Install Semgrep

pip install semgrep

Verify:

semgrep --version

---

# Step 6 — Install Gitleaks

Download:
https://github.com/gitleaks/gitleaks/releases

Add gitleaks.exe to PATH.

Verify:

gitleaks version

---

# Step 7 — Install Grafana

docker run -d --name grafana -p 3000:3000 grafana/grafana

Access:
http://localhost:3000

Default Credentials:
- admin/admin

---

# Step 8 — Run Semgrep Scan

semgrep --config rules/semgrep .

---

# Step 9 — Run Gitleaks

gitleaks detect --source .

---

# Step 10 — Run Dependency Check

docker run --rm -v ${PWD}:/src owasp/dependency-check --scan /src/test-app --format HTML --out /src/reports

---

# Step 11 — Configure GitHub Actions

Create:

.github/workflows/security-pipeline.yml

Push changes to trigger automated scans.

---

# Step 12 — Configure RBAC

Inside SonarQube:
- create users
- create groups
- assign permissions
- enable authentication

---

# Step 13 — Access Reports

Reports are stored inside:

reports/

---

# Supported Security Features

- Static Analysis
- SAST
- Secret Detection
- Dependency Scanning
- CI/CD Security
- RBAC
- Dashboards