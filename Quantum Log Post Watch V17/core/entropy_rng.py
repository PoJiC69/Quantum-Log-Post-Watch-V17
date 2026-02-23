import os
import time
import hashlib

def quantum_entropy():
    seed = os.urandom(32) + str(time.time()).encode()
    return hashlib.sha256(seed).hexdigest()
