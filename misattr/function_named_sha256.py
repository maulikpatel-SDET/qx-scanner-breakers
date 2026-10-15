"""R6-09 A user function named rsa_generate() that really makes ECDSA, and ecdsa_sign() that uses RSA."""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, padding, rsa


def rsa_generate():
    return ec.generate_private_key(ec.SECP256R1())       # name says rsa, body is ecdsa


def ecdsa_sign(data: bytes):
    k = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return k.sign(data, padding.PKCS1v15(), hashes.SHA256())   # name says ecdsa, body is rsa
