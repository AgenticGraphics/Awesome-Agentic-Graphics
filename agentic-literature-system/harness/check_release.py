"""Scan staged/tracked release files without printing matched private values.

Run from anywhere inside the repository. This checks the Git index by default,
so ignored run traces, environments and local credentials are never uploaded.
It complements review; it is not proof that arbitrary content is safe to share.
"""
import argparse
import ipaddress
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
RULES = {
    'machine-home-path': re.compile(r'(?:/' + r'Users/|/' + r'home/|[A-Za-z]:\\' + r'Users\\)\S+'),
    'private-document-link': re.compile(r'https?://docs\.google\.com/(?:document|spreadsheets|presentation)/d/[^\s)"\']+'),
    'private-key': re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----'),
    'provider-secret': re.compile(r'\b(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16})\b'),
    'credential-in-url': re.compile(r'https?://[^\s/@]+:[^\s/@]+@'),
}
EXCLUDED_PARTS = {'.git', '.venv', 'venv', '__pycache__', '.pytest_cache', 'runs', 'cache', 'daily-history'}


def inspect_text(text):
    findings = []
    for number, line in enumerate(text.splitlines(), 1):
        for rule, pattern in RULES.items():
            if pattern.search(line):
                findings.append({'line': number, 'rule': rule})
        for match in re.findall(r'(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])', line):
            try:
                address = ipaddress.ip_address(match)
            except ValueError:
                continue
            # Loopback in synthetic tests is generic, never a developer host address.
            if address.is_private and not address.is_loopback:
                findings.append({'line': number, 'rule': 'non-loopback-private-ip'})
    return findings


def scan():
    paths = subprocess.check_output(['git', 'ls-files', '-z', '--', 'agentic-literature-system', 'README.md'], cwd=ROOT).decode().split('\0')
    findings = []
    checked = 0
    for name in filter(None, paths):
        path = Path(name)
        if any(part in EXCLUDED_PARTS for part in path.parts) or path.name.startswith('.env') and path.name != '.env.example':
            findings.append({'file': name, 'rule': 'generated-or-private-file'})
            continue
        raw = subprocess.check_output(['git', 'show', ':' + name], cwd=ROOT)
        try:
            text = raw.decode('utf-8')
        except UnicodeDecodeError:
            findings.append({'file': name, 'rule': 'unexpected-binary-file'})
            continue
        checked += 1
        findings.extend({'file': name, **hit} for hit in inspect_text(text))
    return {'passed': checked > 0 and not findings, 'files_checked': checked, 'findings': findings}


if __name__ == '__main__':
    result = scan()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['passed'] else 1)
