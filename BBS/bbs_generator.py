from random import randint
from bbs import BBS
from prime import miller_rabin
from test_fips import Test


class BBS_Generator:
    def __init__(self, max, n):
        """
        :param max: max number where the prime numbers are chosen
        :param n: length in bits for the generated number
        self.numbers_gen - list with generated number
        """
        self.max = max
        self.n = n
        self.numbers_gen = []
        self.bits_gen = []

    def check_number(self, number):
        """
        Check if number is prime and is Bluma number
        :param number:
        :return:
        """
        return number % 4 == 3 and miller_rabin(number)

    def choose_prime_number(self):
        random = randint(3, self.max - 1)
        while not self.check_number(random):
            random = randint(3, self.max - 1)
        return random

    def generate_numbers(self, nb_to_generate):
        p = self.choose_prime_number()
        print("** Choose p prime number ** =>", p)
        q = self.choose_prime_number()
        print("** Choose q prime number ** =>", q)

        seed = randint(1, self.max - 1) # set seed
        bbs = BBS(p, q, seed) # inicialization BBS with p, q and seed

        for i in range(nb_to_generate):
            x, y = bbs.get_random_int(self.n)
            self.numbers_gen.append(x)
            self.bits_gen.append(y)
        print(self.numbers_gen)
        print(self.bits_gen)
            #print("number ", i, " random value = ",x)

max_number_prime = int(20_000_000)
nb_bits_output = int(1)
nb_numbers_to_generate = int(20_000)

bbs = BBS_Generator(max_number_prime, nb_bits_output)
bbs.generate_numbers(nb_numbers_to_generate)

test = Test(bbs.numbers_gen, bbs.bits_gen)
print('Pojedynczy bit')
test.one_bit()
print('pary')
test.double_bit_test()
print('poker test')
test.poker_test()
print('long sequence')
test.long_sequence()
