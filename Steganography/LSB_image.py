from PIL import Image
import numpy as np

class LSB_image:

    def __init__(self, text, R, G, B):
        self.image = Image.open("pobrane.png")
        self.image_pixels = np.asarray(Image.open('pobrane.png'))
        self.text_ = ["{0:b}".format(ord(letter)) for letter in text]
        self.text = np.array(self.text_prepare(self.text_))
        self.R = R
        self.G = G
        self.B = B

    def text_prepare(self, text):
        newText = []
        for w in text:
            w = self.chceck_size_text(w)
            newText.extend([int(x) for x in w ])
        return newText

    def chceck_size_text(self, color):

        size = len(color)
        add = ''
        for _ in range(size, 8):
            add += '0'
        result = add + color
        return str(result)
    
    def chceck_size(self, color):

        size = len(color)
        add = ''
        for _ in range(size, 8):
            add+='2'
        result = add + color
        return str(result)

    def change_to_bin_rgb(self, rgb):

        r = "{0:b}".format(rgb[0])
        g = "{0:b}".format(rgb[1])
        b = "{0:b}".format(rgb[2])

        r1 = self.chceck_size(r)
        g1 = self.chceck_size(g)
        b1 = self.chceck_size(b)
        res = np.array([r1,g1,b1])

        return res

    def make_binary_matrix(self):

        array_ = np.empty(shape=(self.image_pixels.shape[0],self.image_pixels.shape[1], 3), dtype=np.int64)
        for x in range(self.image_pixels.shape[0]):
            for y in range(self.image_pixels.shape[1]):
                array_[x][y]=self.change_to_bin_rgb(self.image_pixels[x][y])

        return array_

    def check(self, number):
        result= []
        for x in number:
            if x == 2 or x == 0:
                result.append(0)
            if x == 1:
                result.append(1)
        return result


    def difftrent_bit(self):
        matrix = self.make_binary_matrix()
        start = 0
        for x in range(matrix.shape[0]):
            for y in range(matrix.shape[1]):
                if start < len(self.text):
                    r = [int(x) for x in str(matrix[x][y][0])]

                    g = [int(x) for x in str(matrix[x][y][1])]

                    b = [int(x) for x in str(matrix[x][y][2])]
                    stop = start + self.R

                    r[-self.R:] = self.text[start:stop]

                    start = stop
                    stop += self.G
                    g[-self.G:] = self.text[start:stop]
                    start = stop
                    stop += self.B

                    if stop < len(self.text):
                        b[-self.B:] = self.text[start:stop]
                    elif start < len(self.text):
                        b[-self.B:] = self.text[start:]
                    start = stop
                    r = self.check(r)
                    g = self.check(g)
                    b = self.check(b)

                    matrix[x][y][0] = str(self.make_str(r))

                    matrix[x][y][1] = str(self.make_str(g))
                    matrix[x][y][2] = str(self.make_str(b))
                else:
                    r = [int(x) for x in str(matrix[x][y][0])]

                    g = [int(x) for x in str(matrix[x][y][1])]

                    b = [int(x) for x in str(matrix[x][y][2])]
                    r = self.check(r)
                    g = self.check(g)
                    b = self.check(b)

                    matrix[x][y][0] = str(self.make_str(r))

                    matrix[x][y][1] = str(self.make_str(g))
                    matrix[x][y][2] = str(self.make_str(b))


        return matrix


    def make_str(self, word):
        w = ''
        for x in word:
            w+=str(x)

        return w

    def make_pixel(self):
        matrix = self.difftrent_bit()
        array_ = np.ones(shape=(self.image_pixels.shape[0], self.image_pixels.shape[1], 3), dtype=np.int64)
        for x in range(matrix.shape[0]):
            for y in range(matrix.shape[1]):

                r = int(str(int(matrix[x][y][0])),2)
                g = int(str(int(matrix[x][y][1])),2)
                b = int(str(int(matrix[x][y][2])),2)
                array_[x][y] = [r,g,b]

        return array_



    def create_image(self):
        newMatrix = self.make_pixel()
        im = Image.fromarray(np.uint8(newMatrix))
        im.show()
        im.save("result.png")


    def decode_image(self):
        image = Image.open("result.png")
        image_pixels = np.asarray(image)
        array_ = np.ones(shape=(image_pixels.shape[0], image_pixels.shape[1], 3), dtype=np.int64)
        text = ''

        for x in range(image_pixels.shape[0]):
            for y in range(image_pixels.shape[1]):
                array_[x][y] = image_pixels[x][y]

                r = str(bin(array_[x][y][0]))
                g = str(bin(array_[x][y][1]))
                b = str(bin(array_[x][y][2]))

                text += r[-self.R:]
                text += g[-self.G:]
                text += b[-self.B:]
        result_text = ''
        for w in text:
            if w !='b':
                result_text+=w


        result = []
        for x in range(0,len(result_text), 8):
            result.append(chr(int(result_text[x:x+8],2)))

        print(result)
        return result

lsb = LSB_image('Ala ma kota'*500,1,6,1 )

lsb.make_binary_matrix()



lsb.create_image()
lsb.decode_image()



