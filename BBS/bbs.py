class BBS:

    def __init__(self, p, q, seed):
        """
         p is prime number
         q is a prime number
         seed is the x0
         mfactor is compute by p * q
         """
        self.p = p
        self.q = q
        self.seed = seed
        self.xn = seed
        self.m_factor = p * q



    def get_random(self, n):
        """
          generation of bits string,
          n is the lenght of the number to generate in bits
        """
        out = ''
        for i in range(n):
            self.xn = pow(self.xn, 2, self.m_factor)
            out += str(self.xn % 2)
        return out

    def get_random_int(self, n):
        """
        The same as above but return the value as an integer
        """
        x = self.get_random(n)
        return int(x, 2), int(x)
