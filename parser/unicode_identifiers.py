"""R6-05 Non-ASCII identifiers (valid Python). The variable and alias are Unicode."""
from cryptography.hazmat.primitives.asymmetric import rsa as rÅ

ключ = rÅ.generate_private_key(public_exponent=65537, key_size=2048)
