# R6-21 Crypto inside a fenced code block in Markdown docs

Example of our signing setup:

```python
from cryptography.hazmat.primitives.asymmetric import rsa
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
```

This is documentation, but the code is real and copy-pasteable.
