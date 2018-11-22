from dh import DH
from random import randint

class User:
    def __init__(self, DH, number=randint(1, 999)):
        self.dh = DH
        self.x = number
        self.X_or_Y = self.private()

    def power(self, x, y, p):
        res = 1
        x = x % p
        while (y > 0):
            if ((y & 1) == 1):
                res = (res * x) % p
            y = y >> 1
            x = (x * x) % p
        return res

    def private(self):
        return self.power(self.dh.g, self.x, self.dh.n)

    def key(self, Y):
        return  self.power(Y,  self.x, self.dh.n)



dh = DH()
print('Number n:', dh.n)
print('Number g:', dh.g)

userA =  User(dh)
userB = User(dh)
print('Private number A', userA.x)
print('Private number B', userA.x)

X = userA.private()
Y = userB.private()


print('key A: ' , userA.key(Y))
print('key B: ' , userB.key(X))




