"""R6-11 Comments and a constant claim RSA-4096; the actual key is RSA-1024 (weak)."""
from cryptography.hazmat.primitives.asymmetric import rsa

RSA_KEY_SIZE = 4096                                     # claims 4096
key = rsa.generate_private_key(public_exponent=65537, key_size=1024)   # really 1024
