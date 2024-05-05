from diffiehellman import DiffieHellman


class User():
    def __init__(self):
        self.pubkey = None
        self.privkey = None
        self.obj = None

    def generate_keys(self):
        dh1 = DiffieHellman(group=14, key_bits=540)
        self.privkey = dh1.get_private_key()
        self.pubkey = dh1.get_public_key()
        self.obj = dh1


    def generate_shared_key(self,key):
        sharedkey = self.obj.generate_shared_key(key)
        return sharedkey
