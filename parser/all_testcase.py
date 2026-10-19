from cryptography.hazmat.primitives.asymmetric import rsa
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

from cryptography.hazmat.primitives.asymmetric import rsa as r
key = r.generate_private_key(public_exponent=65537, key_size=2048)

import cryptography.hazmat.primitives.asymmetric as asymmetric
rsa = getattr(asymmetric, "rsa")
key = getattr(rsa, "generate_private_key")(
    public_exponent=65537,
    key_size=2048
)

import cryptography.hazmat.primitives.asymmetric as asymmetric
rsa = getattr(asymmetric, "r" "s" "a")
key = getattr(rsa, "generate" "_private_key")(
    public_exponent=65537,
    key_size=2048
)


def generate_key():
    from cryptography.hazmat.primitives.asymmetric import rsa

    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
key = generate_key()


from cryptography.hazmat.primitives.asymmetric.rsa import *
key = generate_private_key(
    public_exponent=65537,
    key_size=2048
)

print(key)
