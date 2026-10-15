"""R6-02 Module and function reached via getattr on concatenated strings + exec-free eval of attribute."""
import cryptography.hazmat.primitives.asymmetric as _a

_mod = getattr(_a, "r" "s" "a")                     # implicit string concat -> 'rsa'
key = getattr(_mod, "generate" "_private_key")(public_exponent=65537, key_size=2048)
