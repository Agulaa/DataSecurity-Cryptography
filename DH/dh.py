from prime import miller_rabin
from random import randint
from math import gcd as bltin_gcd

class DH:

    def __init__(self):
        self.min = 128
        self.max = 20_000
        self.n = self.choose_prime_number() # wybór liczby pierwszej, która minimalnie ma 512 bitów
        self.g = self.choose_prime_roots() # wybór losowego pierwiastka pierwotnego modulo n
        #self.n = 23
        #self.g = 5

    def check_number(self, number):
        return miller_rabin(number)

    def choose_prime_number(self):
        random = randint(self.min, self.max - 1)
        while not self.check_number(random):
            random = randint(self.min, self.max - 1)
        return random


    def choose_prime_roots(self):
        result = self.primeRoots(self.n)
        which = randint(0,len(result))
        return result[which]

    def primeRoots(self,modulo):
        required_set = {num for num in range(1, modulo) if bltin_gcd(num, modulo)}
        return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
                                                                for powers in range(1, modulo)}]
