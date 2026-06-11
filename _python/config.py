from enum import Enum
import os
import re
import hashlib

class SecKey(Enum):
    RSA = "RSA"
    AES = "AES"

def get_key_from_hash(b64hash: str) -> str:
    """Returns the key with a given hash. This function is not secure and should be replaced."""
    if b64hash == "0":  # No key available
        return None
    
    key = hashlib.sha256(b64hash.encode()).hexdigest()
    return key

# Check for security in production
if __name__ == "__main__":
    pass