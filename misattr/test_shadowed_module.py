"""R6-10 A local class named 'rsa' shadows the real module; the real RSA call is qualified differently."""

class rsa:                      # shadows the name 'rsa' in this scope
    @staticmethod
    def generate_private_key(**kw):
        return "NOT A KEY"
fake = rsa.generate_private_key()                       # calls the class, no crypto
