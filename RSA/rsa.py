from rsa_generator import RSA_generator


class RSA:

    def __init__(self):
        self.rsa_generator = RSA_generator()
        self.private_key = self.rsa_generator.private_key()
        self.public_key = self.rsa_generator.public_key()

    def prepare_text(self, text_to_encrypt):
        char_text = [ord(letter) for letter in text_to_encrypt]
        return char_text

    def encrypt(self, text):
        text_to_encrypt = self.prepare_text(text)
        encrypted = [self.power(letter, self.public_key[0], self.public_key[1]) for letter in text_to_encrypt]
        return encrypted

    def prepare_decrypted(self, text):
        text_ = [chr(letter) for letter in text]
        return text_

    def power(self,x, y, p):
        res = 1
        x = x % p
        while (y > 0):
            if ((y & 1) == 1):
                res = (res * x) % p
            y = y >> 1
            x = (x * x) % p
        return res

    def decrypt(self, encrypted_text):
        encrypted_text = [self.power(c, self.private_key[0], self.private_key[1]) for c in encrypted_text]
        return self.prepare_decrypted(encrypted_text)

rsa = RSA()
text = 'Ala ma psa'*5
encrypt = rsa.encrypt(text)
print(encrypt)
decrypt = rsa.decrypt(encrypt)
print(decrypt)

