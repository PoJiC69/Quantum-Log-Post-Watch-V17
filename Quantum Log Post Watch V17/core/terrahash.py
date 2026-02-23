import hashlib

def terrahash8192(data: bytes) -> str:
    h = data
    for _ in range(16):  # chained hashing
        h = hashlib.sha512(h).digest()
    return h.hex()
