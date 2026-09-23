> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.

# SSH Hardening Checker

SSH security hardening checker for authorized security testing — grabs the SSH service banner and
prints an OpenSSH hardening checklist (key-only auth, root login, Kex/MAC/Cipher, login grace
time, and user restrictions). Standard library only, v1.1.0.

![MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![GitHub stars](https://img.shields.io/github/stars/5h4d0wn1k/ssh-hardening-checker)
![GitHub last commit](https://img.shields.io/github/last-commit/5h4d0wn1k/ssh-hardening-checker)
![GitHub issues](https://img.shields.io/github/issues/5h4d0wn1k/ssh-hardening-checker)

## Why

SSH is the front door of nearly every server, and its defaults are rarely the secure choice. This
tool makes the audit repeatable: it connects to a host, reads the SSH banner (revealing the server
version), then prints the canonical OpenSSH hardening checklist — disable password auth, disable
root login, enforce strong KexAlgorithms/MACs/Ciphers, tighten LoginGraceTime and MaxAuthTries, and
scope users with AllowUsers/AllowGroups. It is a focused, dependency-free SSH-security and
hardening educational tool for use only against SSH servers you own or hold explicit written
authorization to test.

## Features

- **Banner grab** — async SSH banner retrieval with configurable timeout.
- **Version identification** — the banner reveals the server/OpenSSH version.
- **Hardening checklist** — static, current OpenSSH best-practice guidance printed on every run.
- **Zero dependencies** — Python standard library only (Python 3.8+).

## Quickstart

Prerequisite: Python 3.8+ (standard library only).

```bash
python ssh_hardening_check.py --host 192.0.2.10
python ssh_hardening_check.py --host 192.0.2.10 --port 2222 --timeout 5.0
python ssh_hardening_check.py --help
```

Run it against a sandbox VM or your own lab host first.

## Project structure

- `ssh_hardening_check.py` — analyzer and CLI (`--host`, `--port`, `--timeout`).
- `requirements.txt` — dependency notes (stdlib only).
- `CHANGELOG.md` — release history; `VERSION` — current version (1.1.0).

## Documentation

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [SECURITY.md](SECURITY.md)
- [ETHICS.md](ETHICS.md) · [SCOPE.md](SCOPE.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep the tool dependency-free and the guidance current.

## License

MIT — see [LICENSE](LICENSE).