"""R6-04 Everything on one physical line with semicolons."""
from cryptography.hazmat.primitives.asymmetric import rsa as r; import sys; k=r.generate_private_key(public_exponent=65537,key_size=2048); sys.exit(0)
