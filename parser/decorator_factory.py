"""R6-03 RSA call sits inside a nested closure returned by a decorator factory (deep nesting)."""
from cryptography.hazmat.primitives.asymmetric import rsa


def with_key(bits):
    def outer(fn):
        def inner(*a, **k):
            key = rsa.generate_private_key(public_exponent=65537, key_size=bits)
            return fn(key, *a, **k)
        return inner
    return outer


@with_key(2048)
def use(key, data):
    return key
