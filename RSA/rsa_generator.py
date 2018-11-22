from prime import miller_rabin
from random import randint

class RSA_generator:

    def __init__(self):

        self.max = 9999
        self.min = 1000
        self.p = self.choose_prime_number()
        self.q = self.choose_prime_number()
        #self.p = 1031
        #self.q = 2029
        self.n = self.p * self.q
        self.phi = (self.p -1)* (self.q-1)
        self.e = self.find_e()
        self.d = self.find_d()


    def check_number(self, number):
        return miller_rabin(number)

    def choose_prime_number(self):
        random = randint(self.min, self.max - 1)
        while not self.check_number(random):
            random = randint(self.min, self.max - 1)
        return random

    def nwd(self, a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def find_e(self):
        x = 2
        result = self.nwd(self.phi, x)
        while result != 1:
            x+=1
            result = self.nwd(self.phi, x)
        return x

    def find_d(self):
        d = 1
        result = self.e *d -1
        while result%self.phi!=0:
            d+=1
            result = self.e * d - 1
        return d

    def private_key(self):
        return (self.d, self.n)

    def public_key(self):
        return (self.e, self.n)


