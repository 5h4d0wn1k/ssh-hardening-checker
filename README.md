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

### 1. Disable Password Authentication

```bash
# In /etc/ssh/sshd_config
PasswordAuthentication no
```

### 2. Disable Root Login

```bash
# In /etc/ssh/sshd_config
PermitRootLogin no
```

### 3. Use Strong Key Exchange

```bash
# In /etc/ssh/sshd_config
KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group-exchange-sha256
```

### 4. Limit Login Attempts

```bash
# In /etc/ssh/sshd_config
MaxAuthTries 3
LoginGraceTime 30
```

### 5. Restrict Users

```bash
# In /etc/ssh/sshd_config
AllowUsers user1 user2
# OR
AllowGroups sshusers
```

## Examples

### Example 1: Basic Check

```bash
# Check SSH hardening
python ssh_hardening_check.py --host 192.168.1.100
```

### Example 2: Custom Port

```bash
# Check SSH on custom port
python ssh_hardening_check.py \
  --host 192.168.1.100 \
  --port 2222
```

## Use Cases

- **Security Audits**: Check SSH configuration on your servers
- **Hardening**: Implement SSH security best practices
- **Penetration Testing**: Authorized security assessments
- **Educational Purposes**: Learn about SSH security hardening

## Legal Disclaimer

⚠️ **IMPORTANT**: This tool is for authorized security testing and educational purposes only.

- Only test SSH servers you own or have explicit written authorization to test
- Follow responsible disclosure practices
- Comply with all applicable laws and regulations

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Always get explicit authorization before testing any SSH server!
