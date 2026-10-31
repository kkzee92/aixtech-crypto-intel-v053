from crypto_intel.security.redact import redact
from crypto_intel.security.audit import seal_event

def test_redact_secret():
    assert "[REDACTED]" in redact("api_key=abc123def456ghi789")

def test_seal_has_hashes():
    event = seal_event({"test": True})
    assert "sha256" in event and "sha512" in event and "merkle_proxy" in event
