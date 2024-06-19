from hashlib import sha256

def secure_hash(val: str) -> str:
    return sha256(val.encode()).hexdigest()