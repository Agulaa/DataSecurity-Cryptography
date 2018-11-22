from itertools import cycle

class Test:

    def __init__(self, numbers_gen, bits_gen):
        self.numbers_gen = numbers_gen
        self.bits_gen = bits_gen

    def one_bit(self):
        zero_num = len([x for x in self.bits_gen if x==1])
        print(zero_num)
        if zero_num > 9725 and zero_num < 10275:
            return True
        else:
            return False

    def double_bit_test(self):

        count_00, count_01, count_10, count_11 = 0, 0, 0, 0
        for i in range(1, len(self.bits_gen)):
            lastElem,thisElem = self.bits_gen[i], self.bits_gen[i-1]
            pom = str(lastElem) + str(thisElem)
            if pom == "00":
                count_00 += 1
            elif pom == "01":
                count_01 += 1
            elif pom == "10":
                count_10 += 1
            elif pom == "11":
                count_11 += 1

        print('00:', count_00)
        print('01:', count_01)
        print('10:', count_10)
        print('11:', count_11)
        return  count_00, count_01, count_10, count_11

    def poker_test(self):
        dec_list = []
        for i in range(0, len(self.bits_gen), 4):
            binary = str(self.bits_gen[i]) + str(self.bits_gen[i + 1]) + str(self.bits_gen[i + 2]) + str(self.bits_gen[i + 3])
            to_decimal = int(binary, 2)
            dec_list.append(to_decimal)
        out = []
        for j in range(0, 16):
            out.append(dec_list.count(j))
        sum_ = [i * i for i in out]
        x = (16.0 / 5000.0) * float(sum(sum_)) - 5000.0
        print(x)
        return x

    def long_sequence(self):
        max_seq = 0
        len_seq = 0

        for i in range(1,len(self.bits_gen)):
            if self.bits_gen[i-1] == self.bits_gen[i]:
                len_seq+=1
            else:
                if len_seq > max_seq:
                    max_seq = len_seq
                len_seq = 0
        print(max_seq)
