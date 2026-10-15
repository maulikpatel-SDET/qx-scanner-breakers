"""R6-08 Variable names lie: 'ecdsa_key' holds RSA, 'rsa_key' holds ECDSA."""
from cryptography.hazmat.primitives.asymmetric import ec, rsa

ecdsa_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)   # actually RSA
rsa_key = ec.generate_private_key(ec.SECP256R1())                           # actually ECDSA
