"""R6-10 A local class named 'rsa' shadows the real module; the real RSA call is qualified differently."""
from cryptography.hazmat.primitives.asymmetric import rsa as _real_rsa


class rsa:                      # shadows the name 'rsa' in this scope
    @staticmethod
    def generate_private_key(**kw):
        return "NOT A KEY"


fake = rsa.generate_private_key()                       # calls the class, no crypto
real = _real_rsa.generate_private_key(public_exponent=65537, key_size=2048)   # real RSA-2048
