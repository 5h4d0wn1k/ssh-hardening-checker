> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.
# SSH Hardening Checker

⚠️ **EDUCATIONAL PURPOSE ONLY** - This tool is designed for authorized security testing and educational purposes. Only use on SSH servers you own or have explicit written authorization to test.

## Overview

A comprehensive SSH security hardening checker that analyzes SSH configuration and provides recommendations for securing SSH services. Checks banners, configuration, and provides hardening guidance.

## Features

- **Banner Analysis**: Retrieves and analyzes SSH service banners
- **Hardening Checklist**: Provides comprehensive SSH hardening recommendations
- **Configuration Guidance**: Best practices for SSH security
- **Version Detection**: Identifies SSH service versions

## Installation

### Requirements

- Python 3.8+
- Standard library only (no external dependencies!)

### Setup

```bash
# Clone the repository
git clone https://github.com/5h4d0wn1k/ssh-hardening-checker.git
cd ssh-hardening-checker

# No installation needed!
python ssh_hardening_check.py --help
```

## Usage

### Basic Usage

```bash
# Check SSH hardening
python ssh_hardening_check.py --host 192.168.1.100
```

### Custom Port

```bash
# Check SSH on custom port
python ssh_hardening_check.py \
  --host 192.168.1.100 \
  --port 2222
```

### Custom Timeout

```bash
# Set custom timeout
python ssh_hardening_check.py \
  --host 192.168.1.100 \
  --port 22 \
  --timeout 5.0
```

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--host` | Target SSH host (required) | - |
| `--port` | SSH port | 22 |
| `--timeout` | Connection timeout (seconds) | 3.0 |

## Output Format

```
[+] Banner: SSH-2.0-OpenSSH_8.0

Checklist:
- Disable password auth; use key-based only (PasswordAuthentication no).
- Disable root login (PermitRootLogin no).
- Use strong Kex/MAC/Cipher (per latest OpenSSH defaults).
- Set LoginGraceTime low; MaxAuthTries low.
- Use AllowUsers/AllowGroups to limit.
- Move off default port only as a minor noise-reduction (not security).
```

## Hardening Recommendations

### 1. Password Authentication

**Recommendation**: Disable password authentication, use key-based only

```bash
# In /etc/ssh/sshd_config
PasswordAuthentication no
PubkeyAuthentication yes
```

### 2. Root Login

**Recommendation**: Disable root login

```bash
# In /etc/ssh/sshd_config
PermitRootLogin no
```

### 3. Key Exchange Algorithms

**Recommendation**: Use strong key exchange algorithms

```bash
# In /etc/ssh/sshd_config
KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group-exchange-sha256
```

### 4. MAC Algorithms

**Recommendation**: Use strong MAC algorithms

```bash
# In /etc/ssh/sshd_config
MACs hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com
```

### 5. Cipher Algorithms

**Recommendation**: Use strong cipher algorithms

```bash
# In /etc/ssh/sshd_config
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com
```

### 6. Login Grace Time

**Recommendation**: Set low login grace time

```bash
# In /etc/ssh/sshd_config
LoginGraceTime 30
MaxAuthTries 3
```

### 7. User Restrictions

**Recommendation**: Limit allowed users

```bash
# In /etc/ssh/sshd_config
AllowUsers user1 user2
# Or
AllowGroups sshusers
```

## Use Cases

- **Security Audits**: Check SSH configuration on your servers
- **Hardening**: Implement SSH security best practices
- **Compliance**: Meet security compliance requirements
- **Educational Purposes**: Learn about SSH security

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## ⚠️ Legal Disclaimer

### Educational Purpose Only
This tool is provided strictly for **educational purposes** and **authorized security testing** only. It is intended to help security professionals and students learn about security concepts in controlled environments.

### Authorized Use Only
- You must have **explicit written authorization** before testing any system you do not own
- Unauthorized access to computer systems is **illegal** and punishable under laws including but not limited to the Computer Fraud and Abuse Act (CFAA), Computer Misuse Act, and similar legislation worldwide
- Only use this tool on systems you own, have permission to test, or in isolated lab environments

### No Warranty
This software is provided "AS IS" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. The author makes no representations or warranties regarding the accuracy, completeness, or reliability of this software.

### Limitation of Liability
**In no event shall the author (Nikhil Nagpure) be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.**

### User Responsibility
- The user assumes **full responsibility** for any consequences resulting from the use of this tool
- The author is **not responsible** for any misuse, damage, or illegal activities performed with this software
- Users are solely responsible for ensuring compliance with all applicable local, state, national, and international laws and regulations

### Indemnification
By using this software, you agree to **indemnify, defend, and hold harmless** the author from and against any and all claims, liabilities, damages, losses, costs, and expenses (including reasonable attorneys fees) arising from or related to your use of this software.

### Responsible Disclosure
If you discover vulnerabilities using this tool, please follow responsible disclosure practices and report them to the affected parties through appropriate channels.

---

**By using this software, you acknowledge that you have read, understood, and agree to be bound by this disclaimer.**
## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Always implement SSH hardening recommendations on your servers!
