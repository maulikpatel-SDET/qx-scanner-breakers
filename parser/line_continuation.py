"""R6-01 The call is split across lines with backslash continuations and comments between args."""
from cryptography.hazmat.primitives.asymmetric import rsa

key = rsa.\
    generate_private_key(  # noqa
        public_exponent=65537,
        key_size=2048,       # 2048-bit
    )
