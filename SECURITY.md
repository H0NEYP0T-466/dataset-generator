# Security Policy

## Supported Versions

The following table lists the versions of this project that are currently supported with security updates.

| Version | Supported          | Notes |
| ------- | ------------------ | ----- |
| main    | :white_check_mark: | Active development branch; receives all security fixes |
| 1.0.0   | :white_check_mark: | Stable release; receives critical and high-severity fixes |
| < 1.0.0 | :x:                | No longer maintained |

> **Note**: Only the `main` branch and tagged releases (e.g., `v1.0.0`) are considered stable and eligible for security patches. Older commits or unreleased branches are not supported.

---

## Reporting a Vulnerability

We take the security of **DataForge — LLM Dataset Generator** seriously. If you discover a security vulnerability in this repository, please report it responsibly.

### Preferred Method: GitHub Private Vulnerability Reporting

1. Go to the repository’s **Security** tab.
2. Click on **"Report a vulnerability"**.
3. Fill out the form with as much detail as possible:
   - Description of the issue
   - Steps to reproduce
   - Affected components (e.g., backend API, frontend UI, model router)
   - Potential impact
4. Submit the report privately.

GitHub will acknowledge your submission within **48 hours**.

> 🔒 All reports submitted via private vulnerability reporting are handled confidentially and not made public until a fix is deployed.

---

## Disclosure Policy

We follow a **responsible disclosure timeline** to protect users while allowing time to develop and deploy fixes:

- Upon receiving a valid vulnerability report:
  - Acknowledge receipt within **48 hours**.
  - Begin internal investigation and assign priority based on severity.
- For **critical** vulnerabilities (e.g., remote code execution, data leakage):
  - Public disclosure occurs **within 7 days** of patch deployment.
- For **high/moderate** severity issues:
  - Public disclosure occurs **within 30 days** of patch deployment.
- All disclosures include:
  - Description of the vulnerability
  - Affected versions
  - Mitigation steps or fix details
  - Credit to reporter (if desired)

We encourage coordinated disclosure and will work with reporters to ensure timely resolution.

---

## Security Response Process

After a vulnerability is reported:

1. **Triage & Validate** (within 48 hours)
   - Confirm the issue exists and assess severity using CVSS scoring.
2. **Develop Fix**
   - Assign engineer(s) to resolve the issue.
   - Apply secure coding practices (input validation, least privilege, etc.).
3. **Test & Review**
   - Conduct internal testing and peer review.
4. **Deploy Patch**
   - Release fix in next minor/patch update or hotfix.
5. **Notify Community**
   - Update changelog, GitHub advisory, and optionally notify downstream users.
6. **Close Report**
   - Mark vulnerability as resolved in private report.

All contributors and maintainers are bound by confidentiality during this process.

---

## Out of Scope

The following types of findings are **not considered vulnerabilities** under this policy:

- **False positives** due to misconfiguration (e.g., missing `.env` file, unsecured local instance).
- **Denial-of-service via resource exhaustion** from legitimate usage (e.g., large dataset generation).
- **Insecure direct object references (IDOR)** without authentication context (this app runs locally; no user auth by design).
- **Client-side XSS** due to user-controlled input rendering (React sanitization mitigates most risks).
- **Missing HTTPS** — this application is intended for **local development only** and does not expose external endpoints.
- **Dependency vulnerabilities** in transitive dependencies unless they lead to **direct exploitability** (we monitor via Dependabot).
- **Social engineering**, phishing, or physical access attacks.
- **Third-party service abuse** (e.g., OpenAI/Groq API overuse) — these are governed by provider terms.

> ⚠️ While we aim for robust defaults, this tool is **not designed for production deployment without additional hardening**. Users must secure their own environments.

---

## Security Best Practices

To use **DataForge — LLM Dataset Generator** safely:

- ✅ Run only in **trusted, isolated environments** (e.g., local machine or secured container).
- ✅ Never expose the FastAPI server (`uvicorn`) to public networks — it binds to `localhost:8005` by default.
- ✅ Use `.env` files to store API keys and keep them out of version control.
- ✅ Regularly update dependencies using `pip install --upgrade -r backend/requirements.txt` and `npm audit fix`.
- ✅ Enable ESLint and TypeScript strict mode to catch common bugs early.
- ✅ Monitor logs via the built-in logger (`backend/logger/setup.py`) for suspicious activity.
- ✅ Disable auto-reload (`--reload`) in production-like setups to reduce attack surface.

---

Thank you for helping us keep DataForge secure!  
For general questions, open an issue or contact the maintainer at [H0NEYP0T-466](https://github.com/H0NEYP0T-466).