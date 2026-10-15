"""R6-07 RSA and ECDSA key generation on the SAME physical line."""
from cryptography.hazmat.primitives.asymmetric import ec, rsa

a = rsa.generate_private_key(public_exponent=65537, key_size=2048); b = ec.generate_private_key(ec.SECP256R1())
