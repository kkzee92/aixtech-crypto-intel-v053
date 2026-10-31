"""Hash-chained audit log with multi-hash seal. v0.53."""
import hashlib
import json
from datetime import datetime, timezone

def seal_event(event: dict, prev_hash: str = "") -> dict:
    event["timestamp"] = datetime.now(timezone.utc).isoformat()
    event["prev_hash"] = prev_hash
    event["residency"] = "synthetic"
    event["version"] = "0.53"
    payload = json.dumps(event, sort_keys=True).encode()
    event["sha256"] = hashlib.sha256(payload).hexdigest()
    event["sha3"] = hashlib.sha3_256(payload).hexdigest()
    event["blake2b"] = hashlib.blake2b(payload, digest_size=32).hexdigest()
    event["sha512"] = hashlib.sha512(payload).hexdigest()
    # Simple Merkle-style root proxy
    event["merkle_proxy"] = hashlib.sha256(event["sha256"].encode() + event["sha3"].encode()).hexdigest()
    return event
