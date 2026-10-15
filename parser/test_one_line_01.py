import cryptography.hazmat.primitives.asymmetric as _a
import cryptography.hazmat.primitives.asymmetric.rsa
 
_mod = getattr(_a, "rsa")
 
key = getattr(_mod, "generate_private_key")(
    public_exponent=65537,
    key_size=2048
)
 
print(key)
