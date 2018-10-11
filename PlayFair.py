import numpy as np
import sys

class Playfair:
    def __init__(self, keyword, input_file, output_file):
        self.input = input_file
        self.output = output_file
        self.keyword = self.word_to_ascii_letter(keyword.upper())
        self.ascii_alphabet = [x for x in np.arange(65,91) if x!=74] # stworzenie alfabetu ASCII i  usunięcie J
        self.new_alphabet = self.del_keyword_from_alphabet() # alfabet bez liter, które są w kluczu
    def del_keyword_from_alphabet(self):
        """
        Usuwanie z ogólnego alfabetu liter, które znajdują się w kluczu
        :return: nowy alfabet
        """
        new_alphabet = [x for x in self.ascii_alphabet if x not in self.keyword]
        return new_alphabet
    def split_text(self, text):
        """
        Zamiana tekstu na same duże litery oraz podzał tekstu na osobne słowa
        :param text: tekst do zaszyfrowania
        :return: tablica ze słowami
        """
        text = text.upper()
        split_text = text.split()
        return split_text
    def check_double_letter(self, splited_text):
        """
        Sprawdzenie czy w jakimś słowie nie ma podwójnej literki, jeśli tak to rozdzielenie tych liter literą X
        :param splited_text: podzielony tekst na słowa
        :return: tablica z nowymi słowami
        """
        new_splited_text = []
        for word in splited_text:
            new_word = []
            for i in range(0, len(word)):
                new_word.append(word[i])
                if i+1 != len(word):
                    if word[i] == word[i+1]:
                        new_word.append('X')
            new_splited_text.append(new_word)
        return new_splited_text
    def word_to_ascii_letter(self, splited_text):
        """
        Zamiana słów na kod ascii, utworzenie tablicy z pojedyńczymi literami
        :param splited_text: tablica ze słowami
        :return: tablica liter w kodzie ascii
        """
        all_ascii_letter = []
        for word in splited_text:
            for letter in word:
                if letter == 'J': #jeśli w tekscie zakodowanym jest J -> zamiana na I
                    letter='I'
                all_ascii_letter.append(ord(letter))
        return all_ascii_letter
    def is_even(self, letter):
        """
        Sprawdzenie czy zakodowany tekst ma parzystą ilośc liter, jeśli nie to na koniec dodany jest 'X' w kodzie ascii,
        czyli 88
        :param letter: tablica z literami zakodowanymi w ascii
        :return: tablica liter
        """
        if len(letter)%2 != 0:
            letter.append(88)
        return letter
    def add_letter_to_matrix(self):
        """
        Stworzenie macierzy 5x5, dodanie klucza do tablicy oraz pozostałych liter
        :return: macierz 5x5 z kluczem i alfabetem w ascii
        """
        matrix = np.zeros((5,5)) # macierz 5x5
        i = 0
        j = 0
        for word in self.keyword: # macierz z uzupełnionym kluczem
            matrix[i][j] = word
            j+=1
            if j+1 > 5:
                i+=1
                j=0
        for word in self.new_alphabet: # reszta alfabetu
            matrix[i][j] = word
            j+=1
            if j + 1 > 5:
                i += 1
                j = 0
        return matrix
    def make_pair(self, letters):
        """
        Utworzenie par liter
        :param letters:  tablica ze literami
        :return: tablica z parami liter
        """
        letters_pair = []
        for i in range(0,len(letters)-1, 2):
            letters_pair.append([letters[i], letters[i+1]])
        return letters_pair
    def encode_pair(self,letters_pair, matrix):
        """
        Zaszyfrowanie poszczególnych par
        :param letters_pair: latblica z parami liter
        :param matrix: maciez 5x5
        :return: zaszyfrowane pary
        """
        new_pair = []
        for pair in letters_pair:
            where_1 = np.where(matrix==pair[0])
            where_2 = np.where(matrix==pair[1])
            v1,c1 = where_1
            v2, c2 = where_2
            v1 = v1[0]
            v2 = v2[0]
            c1 = c1[0]
            c2 = c2[0]
            if v1 == v2: # ten sam wiersz -> kolumna +1
                if c1+1==5:
                    one = matrix[v1][0]
                else:
                    one = matrix[v1][c1 + 1]
                if c2+1 ==5:
                    two = matrix[v2][0]
                else:
                    #one = matrix[v1][c1+1]
                    two = matrix[v2][c2+1]
            elif c1 == c2: # ta sama kolumna -> wiersz +1
                if v1 + 1 == 5:
                    one = matrix[0][v1]
                else:
                    one = matrix[v1 + 1][c1]
                if v2 + 1 == 5:
                    two = matrix[0][v2]
                else:
                    two = matrix[v2+1][c2]
            else: # inny wiersz i klumna -> po kwadracie, ten sam wiersz lecz przeciwne kolumna
                one = matrix[v1][c2]
                two = matrix[v2][c1]

            new_pair.append([one,two])
        return new_pair
    def decode_pair(self, letter_pair, matrix):
        """
        Rozszyfrowanie par
        :param lettter_pair: pary słów zaszyfrowanych
        :param matrix: macierz z uzupełnionymi literami
        :return: odszyfrowane pary
        """
        new_pair = []
        for pair in letter_pair:
            where_1 = np.where(matrix == pair[0])
            where_2 = np.where(matrix == pair[1])
            v1, c1 = where_1
            v2, c2 = where_2
            v1 = v1[0]
            v2 = v2[0]
            c1 = c1[0]
            c2 = c2[0]
            if v1 == v2: # ten sam wiersz -> kolumna -1
                if c1 - 1 == -1:
                    one = matrix[v1][4]
                else:
                    one = matrix[v1][c1 - 1]
                if c2 - 1 == -1:
                    two = matrix[v2][4]
                else:
                    two = matrix[v2][c2 - 1]
            elif c1 == c2: # ta sama kolumna -> wiersz -1
                if v1 - 1 == -1:
                    one = matrix[0][c1]
                else:
                    one = matrix[v1 - 1][c1]
                if v2 - 1 == -1:
                    two = matrix[0][c2]
                else:
                    two = matrix[v2 - 1][c2]
            else: # inny wiersz i kolumna -> te same wiersze, lecz przeciwne kolumny
                one = matrix[v1][c2]
                two = matrix[v2][c1]
            new_pair.append([one, two])

        return new_pair
    def ascii_pair_to_letter(self, ascii_pair):
        """
        Zamiana ascii na litery
        :param ascii_pair: pary w ascii
        :return: litery
        """
        letter_text = []
        for pair in ascii_pair:
            for p in pair:
                letter_text.extend(chr(int(p)))

        return letter_text
    def encode(self):
        """
        #-1. odczytanie tekstu z pliku
        #0. podział tekstu na słowa
        #1. sprawdzanie podwojnych liter
        #2. zamiana słów na ascii
        #3. sprawdzenie parzystości ciągu znaków do zaszyfrowania
        #4. Utworzenie macierzy 5x5 z kluczem oraz resztą alfabetu
        #5. stworzenie par liter do zaszyfrowania
        #6. zaszyfrowanie par
        #7. zamiana kody ascii na litery
        Główna fumkcja do kodowania
        :param text: tekst do zaszfrowania

        """
        with open(self.input) as f:
            text = f.read()

        splited_text = self.split_text(text)

        without_double_letter = self.check_double_letter(splited_text)

        ascii_letter = self.word_to_ascii_letter(without_double_letter )

        even_text = self.is_even(ascii_letter)
        matrix = self.add_letter_to_matrix()
        pair_letter = self.make_pair(even_text)

        encode_text = self.encode_pair(pair_letter, matrix)
        encode_text2 = self.ascii_pair_to_letter(encode_text)
        encode_text2 = np.array(encode_text2)
        file = open(self.output, 'w')
        for word in encode_text2:
            file.write(str(word))

        #return encode_text2
    def decode(self):
        """
        #-1. odczytanie tekstu z pliku
        #0. zamiana zaszyfrowanego tekstu na wielkie litery
        #1. zamiana słów na ascii i na pojedyncze litery
        #2. stworzenie par liter
        #3. uwtorzenie macierzy
        #4. odkodowanie par
        #5. zamiana ascii na litery
        Główna funkcja do odkodowania
        :param text:
        """
        with open(self.output) as file:
            text = file.read()
        decode_text = self.word_to_ascii_letter(text)
        pair_word_de = self.make_pair(decode_text)
        matrix = self.add_letter_to_matrix()
        decode = self.decode_pair(pair_word_de, matrix)
        decode_text = self.ascii_pair_to_letter(decode)
        file = open('odczyfrowane.txt', 'w')
        for word in decode_text:
            file.write(str(word))
        #return decode_text

if __name__ == '__main__':

    print("Podaj klucz: ")
    klucz = input()
    print("Podaj nazwe pliku wejściowego: ")
    input_file = input()
    print("Podaj nazwe pliku wyjściowego: ")
    output_file = input()
    pf = Playfair(keyword=klucz, input_file=input_file, output_file=output_file)
    print("Kodowanie")
    pf.encode()
    print("Odkodowanie")
    pf.decode()




