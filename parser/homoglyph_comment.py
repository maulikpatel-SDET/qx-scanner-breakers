"""R6-06 TRAP: a Cyrillic look-alike 'RSA' in a comment; the real code is ECDSA.

Migration note: replaced РSA with modern crypto.  (that is Cyrillic Es-like, not Latin RSA)
"""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

key = ec.generate_private_key(ec.SECP256R1())
sig = key.sign(b"x", ec.ECDSA(hashes.SHA256()))
