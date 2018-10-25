from Crypto.Cipher import AES
from datetime import datetime


class Cipher_CTR:

    def __init__(self, value=10):
        self.key = "123456789011asdfghjkloiuytrewqas".encode() # 32
        self.cipher = AES.new(self.key, AES.MODE_ECB) #create AES model
        self.nonce = value
        self.value = str(value)

    def increment_value(self):
        """
        Zwiększanie liczby o 1
        """
        input = int(self.value)+1
        self.value = str(input)


    def check_size(self, input):
        """
        Sprawdzanie, aby wejście do szyfratora miało długość 16 bajtów
        :param input: nonce+licznik
        :return: dopełniony input jako string
        """
        result = input
        if len(input)<16:
            for _ in range(len(input), 16, 1):
                result = result + chr(48)

        return str(result)

    def xor_two_bytes_string(self, Vector1,Vector2):
        """
        Xor dwóch stringów, jeden wyjściowy z AES, a drugi to blok tekstu jawnego
        :param Vector1: blok tekstu jawnego lub blok szyfrogramu
        :param Vector2: wyjście z szyfratora
        :return: blok szyfrogramu lub tekst jawny
        """
        if len(Vector1) <len(Vector2):
            if type(Vector1[0]) is str:
                result = [chr(ord(bit1) ^ bit2) for bit1, bit2 in zip(Vector1, Vector2[:len(Vector1)])]
            else:
                result = [chr(bit1 ^ bit2) for bit1, bit2 in zip(Vector1, Vector2[:len(Vector1)])]
        else:
            if type(Vector1[0]) is str:
                result = [chr(ord(bit1)^bit2) for bit1,bit2 in zip(Vector1, Vector2)]
            else:
                result = [chr(bit1 ^ bit2) for bit1, bit2 in zip(Vector1, Vector2[:len(Vector1)])]

        return result

    def split_to_blocks(self, message):
        """
        Podział tekstu jawnego na bloki po 16 bajtów, jeśli wiadomość
        będzie krótsza niż 16, to nie jest dopełniane
        :param message: tekst jawny
        :return: wektor z blokami
        """
        size = 16
        if len(message)>size:
            return [message[i:i + size] for i in range(0, len(message), size)]
        else:
            return [message]


    def prepare_block(self, message):
        """
        Przygotowanie bloków tekstu jawnego
        :param message: tekst jawny
        :return: wektor z blokami
        """
        message_in_blocks = self.split_to_blocks(message)
        return message_in_blocks

    def prepare_block_edb(self, message):
        """
        Przygotowanie boków tekstu jawnego do tryby pracy ECB,
        aby każdy blok był po 16 bitów
        :param message: tekst jawny
        :return: wektor bloków
        """
        residual = len(message) % 16
        result = message
        if residual != 0:
            for _ in range(residual, 16, 1):
                result = result + chr(0)
        message_in_blocks = self.split_to_blocks(result)

        return message_in_blocks


    def encrypt(self,block):
        """
        1. Dopłenienie inputa do 16 bajtów (input -> nonce + counter);
        2. Szyfrowanie wejścia przy pomocy klucza;
        3. xor wyjścia z blokiem tekstu jawnego;
        4. Zwiększenie licznkia
        :param block: blok teksty jawnego
        :return: zaszyfrowane wejście
        """
        input =self.check_size( self.value)
        encode = self.cipher.encrypt(input)
        result_after_xor = self.xor_two_bytes_string(block, encode)
        self.increment_value()
        return result_after_xor

    def make_all_encrypt(self, message):
        """
        Wykonanie całego procesu szyfrowania dla całej wiadomości
        :param message: tekst jawny
        :return: zaszyfrowane bloki => szyfrogram
        """
        message_in_blocks = self.prepare_block(message)
        result = [self.encrypt(block) for block in message_in_blocks]
        return result


    def decrypt(self, encodeBlock):
        """
        1. Dopełnienie inputa do 16 bajtów (input -> nonce + counter);
        2. Rozszyfrowanie bloku szyfrogramu
        3. Xor wyjścia z blokiem szyfrogramu
        4. Zwiększenie licznika
        :param encodeBlock: blok szyfrogramu
        :return: tekst jawny
        """
        input = self.check_size(self.value)
        encode = self.cipher.encrypt(input)
        result_after_xor = self.xor_two_bytes_string(encodeBlock, encode)
        self.increment_value()
        return result_after_xor

    def make_all_decrypt(self, endoceMesaage):
        """
        Wykonanie procesu deszyfrowania dla wszytskich bloków
        :param endoceMesaage: szyfrogram
        :return: rozszyfrowana wiadomośc
        """
        self.value= str(self.nonce)
        result = [self.decrypt(block) for block in endoceMesaage]
        return result


    def check_time_ctr(self, message):
        """
        Obliczanie czasu szyfracji i deszyfracji szyfratora w trybie CTR
        :param message: wiadomość

        """
        start = datetime.now()
        result = self.make_all_encrypt(message)
        stop = datetime.now()
        time = stop - start
        print('Encrypt: ' , time)

        start = datetime.now()
        self.make_all_decrypt(result)
        stop = datetime.now()
        time = stop - start
        print('Decrypt: ', time)


    def check_time_edb(self, message):
        """
        Obliczanie czasu szyfracji i deszyfracji szyfratora w trybie EDB
        :param message: wiadomość

        """
        input = self.check_size(message)
        blocks = self.prepare_block_edb(input)
        start = datetime.now()
        encode = [self.cipher.encrypt(input) for input in blocks]
        stop = datetime.now()
        time = stop - start
        print('Encrypt: ', time)

        start = datetime.now()
        decode = [self.cipher.decrypt(input) for input in encode]
        stop = datetime.now()
        time = stop - start
        print('Decrypt: ', time)



ctr = Cipher_CTR()
message = 'ALA ma kota a kot to ktos tam elo pomelo'*10000
#encode = ctr.make_all_encrypt(message)
# print(encode)
# decode = ctr.make_all_decrypt(encode)
# print(decode)
ctr.check_time_ctr(message)

ctr.check_time_edb(message)


