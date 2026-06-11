import os.path
from typing import List, Tuple
import hashlib

def get_key(password: str) -> str:
    """Generate a key for a given password."""
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    # This code is only for demonstration purposes and should not be used in production
    pass