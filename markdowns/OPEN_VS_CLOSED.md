# Open-Source vs. Closed-Source Software

**Project:** Server Monitoring System  
**Team:** Laurin, Ahmed, Waleed, Markuss, Tim

---

## 1. Difference Between Open-Source and Proprietary Software

**Open-Source Software** is software whose source code is publicly available.
Anyone can view, modify, and distribute the code freely. Open-source projects
are typically developed by communities and are often free of charge.

Examples: Linux, Python, GitHub Actions, pytest, psutil

**Proprietary (Closed-Source) Software** is software whose source code is
kept secret by the developer. Users can only use the software under specific
license terms. Modifications are not permitted.

Examples: Microsoft Windows, Adobe Photoshop, GitHub (partially)

| Criterion | Open-Source | Proprietary |
|-----------|-------------|-------------|
| **Source code** | Publicly available | Secret |
| **Cost** | Usually free | Often license fees required |
| **Customization** | Freely modifiable | Not permitted |
| **Support** | Community-based | Official vendor support |
| **Security** | Transparent, auditable | Dependent on vendor |
| **Updates** | Community-driven | Controlled by vendor |

---

## 2. Infrastructure Used in This Project

### Tools and Technologies

| Tool | Type | Purpose |
|------|------|---------|
| **Python 3.11** | Open-Source | Programming language for monitoring modules |
| **psutil** | Open-Source | System data collection (RAM, CPU, disk) |
| **pytest** | Open-Source | Automated testing framework |
| **flake8** | Open-Source | Code quality linting |
| **Bandit** | Open-Source | Security analysis |
| **GitHub** | Partially proprietary | Repository hosting and CI/CD |
| **GitHub Actions** | Partially proprietary | CI/CD pipeline execution |
| **Gmail SMTP** | Proprietary | Email notifications |

### Assessment

The majority of tools used in this project are **open-source**. Python, psutil,
pytest, flake8 and Bandit are all fully open-source and freely available.
GitHub and GitHub Actions are partially proprietary – while the platform is
free to use, the infrastructure and code are owned by Microsoft.

---

## 3. Lock-in Effects

A **lock-in effect** occurs when a company or project becomes so dependent on
a specific vendor or technology that switching to an alternative becomes
difficult, expensive, or risky.

### Lock-in Effects in This Project

**GitHub / GitHub Actions:**  
Our CI/CD pipeline is built specifically for GitHub Actions using the
`.github/workflows/ci.yml` syntax. If we wanted to migrate to a different
platform (e.g., GitLab CI or Jenkins), the entire pipeline configuration
would need to be rewritten. This represents a **medium lock-in risk**.

**Gmail SMTP:**  
The email notification system is configured for Gmail's SMTP server. Switching
to a different email provider would require changes to the `config.ini` file.
This is a **low lock-in risk** since the configuration is easily changed.

**Python:**  
Python is open-source and platform-independent. There is **no lock-in risk**
here, as the code can run on any system with Python installed.

---

## 4. How to Handle Lock-in Effects in the Future (Should-have)

To minimize lock-in effects, the company should consider the following measures:

- **Use open standards:** Prefer tools and formats that follow open standards
  (e.g., YAML for configuration, Markdown for documentation) to ensure
  portability across platforms.

- **Abstract vendor-specific code:** Isolate platform-specific configurations
  (e.g., GitHub Actions syntax) in separate files so they can be replaced
  without affecting the core application.

- **Evaluate alternatives regularly:** Periodically review whether the chosen
  tools are still the best option or whether better alternatives exist.

- **Avoid proprietary data formats:** Store data in open formats (e.g., CSV,
  JSON) rather than vendor-specific formats to ensure data portability.

- **Document dependencies:** Maintain a clear list of all external dependencies
  (as done in `requirements.txt`) so that replacements can be identified quickly.

---

## 5. Generalized Analysis of Open-Source vs. Proprietary Software (Could-have)

### Opportunities of Open-Source Software

- **Cost savings:** No license fees, especially beneficial for startups and
  educational institutions.
- **Transparency:** The source code can be audited for security vulnerabilities
  by anyone, leading to faster identification and fixing of bugs.
- **Community support:** Large communities provide free support, tutorials,
  and extensions.
- **Independence:** No dependency on a single vendor – if support is
  discontinued, the community can continue development.
- **Customization:** Software can be adapted to specific needs without
  requiring vendor approval.

### Risks of Open-Source Software

- **No guaranteed support:** Community support may be slow or unavailable
  for critical issues.
- **Security responsibility:** Organizations must monitor and apply security
  updates themselves.
- **Compatibility issues:** Rapid community-driven updates can sometimes
  break existing functionality.

### Proprietary Software as a Threat to Democracy (Could-have)

Proprietary software can pose risks to democratic societies and individual
freedoms in several ways:

- **Surveillance potential:** Closed-source software can contain hidden
  tracking or backdoor functionality that users cannot detect or prevent.
- **Digital dependency:** When critical infrastructure (e.g., government
  systems, healthcare) relies on proprietary software, entire nations become
  dependent on private corporations.
- **Information asymmetry:** Corporations control what data is collected and
  how it is used, while users have no insight or control.
- **Monopolization:** Large proprietary software vendors can dominate markets
  and suppress competition, limiting innovation.

**Recommended measures:**

| Actor | Measure |
|-------|---------|
| **Companies** | Prefer open-source tools where possible; audit vendor contracts for data rights |
| **Government** | Mandate open-source software for public sector applications; fund open-source development |
| **Private users** | Use open-source alternatives (e.g., LibreOffice, Linux, Firefox); stay informed about data privacy |
