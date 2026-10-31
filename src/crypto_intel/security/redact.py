"""Expanded redaction for zero-trust. v0.53."""
import re

SECRET_PATTERNS = [
    re.compile(r"(?i)(private[_ ]?key|seed|mnemonic|bip39|wif|pem|aws[_ ]?key|github[_ ]?pat|api[_ ]?key|secret|telegram[_ ]?bot|discord[_ ]?token)"),
    re.compile(r"[1-9A-HJ-NP-Za-km-z]{32,44}"),  # Solana-style
    re.compile(r"0x[a-fA-F0-9]{64}"),  # hex private key
    re.compile(r"eyJ[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+"),  # JWT
    re.compile(r"[A-Za-z0-9+/]{40,}={0,2}"),  # high-entropy base64
    re.compile(r"[A-Za-z0-9]{32,}"),  # generic long tokens
    re.compile(r"(?i)(bot[_ ]?token|access[_ ]?token).{0,10}[A-Za-z0-9]{20,}"),
]

def redact(text: str) -> str:
    if not isinstance(text, str):
        text = str(text)
    for pat in SECRET_PATTERNS:
        text = pat.sub("[REDACTED]", text)
    return text
