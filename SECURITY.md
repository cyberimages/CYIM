# Security Policy

## Supported Versions

The following versions of **CyberGenerateOS** are currently supported with security updates:

| Version    | Supported          |
|------------|--------------------|
| 1.x        | ✅ Yes             |
| 0.x (Beta) | ❌ No              |

---

## Reporting a Vulnerability

We take security issues seriously and appreciate your efforts to responsibly disclose vulnerabilities.

### How to Report

1. **Email**:
   - Send details of the vulnerability to **[security@cybergenerateos.com](mailto:security@cybergenerateos.com)**.
   - Include:
     - A clear and concise description of the issue.
     - Steps to reproduce the vulnerability.
     - Potential impact and severity.
     - Any possible fixes or mitigation strategies.

2. **PGP Encryption (Optional)**:
   - Use our PGP key to encrypt sensitive information. The public key can be found [here](https://example.com/pgp-key).

3. **Response Timeline**:
   - We aim to acknowledge receipt of reports within **48 hours**.
   - You can expect a detailed response with an assessment and potential next steps within **5 business days**.

---

## Security Best Practices

To minimize risks while using **CyberGenerateOS**, we recommend the following:

1. **Keep Dependencies Updated**:
   - Regularly update all dependencies listed in `requirements.txt` and `package.json`.
   - Use tools like `npm audit` and `pip-audit` to check for known vulnerabilities.

2. **Use Secure Configurations**:
   - Ensure sensitive data (e.g., API keys, database credentials) is stored securely in `.env` files.
   - Set proper file permissions for sensitive files (`chmod 600 .env`).

3. **Enable HTTPS**:
   - Always deploy CyberGenerateOS over HTTPS in production environments.
   - Use certificates from a trusted Certificate Authority (CA).

4. **Restrict API Access**:
   - Use IP whitelisting or token-based authentication to secure API endpoints.
   - Regularly rotate API keys and tokens.

---

## Responsible Disclosure

We follow the principles of **responsible disclosure** and request that you:

- Avoid publicly disclosing the vulnerability until a fix is released.
- Provide us reasonable time (e.g., 90 days) to address the issue before making it public.

---

## Acknowledgements

We appreciate the contributions of security researchers and community members who help make **CyberGenerateOS** a safer platform. If your vulnerability report leads to a significant fix, we’d be happy to include your name in our [Security Hall of Fame](https://example.com/security-hall-of-fame).

Thank you for helping to secure **CyberGenerateOS**!
