from PIL import Image
import random
import numpy as np

class Cryptography_visual:

    def __init__(self):
        self.image = Image.open('input.png')
        self.image = self.image.convert('1')
        self.image.save('inputBW.png')
        self.out1 = Image.new("1", [size * 2 for size in self.image.size])
        self.out2 = Image.new("1", [size * 2 for size in self.image.size])
        self.sizeX = self.image.size[0]
        self.sizeY = self.image.size[1]

    def put_pixel_to_image(self):
        for i in range(0,self.sizeX, 1):
            for j in range(0, self.sizeY, 1):
                pixel = self.image.getpixel((i,j))
                x = random.randint(0,10)
                if pixel == 0: #BLACK -> diffrent
                    if x % 2 == 0:
                        #IMAGE OUT1
                        self.out1.putpixel((i*2, j*2),255)
                        self.out1.putpixel((i*2+1, j*2), 255)
                        self.out1.putpixel((i*2, j*2+1), 0)
                        self.out1.putpixel((i*2+1, j*2+1), 0)
                        #IMAGE OUT2
                        self.out2.putpixel((i * 2, j * 2), 0)
                        self.out2.putpixel((i * 2 + 1, j * 2), 0)
                        self.out2.putpixel((i * 2, j * 2 + 1), 255)
                        self.out2.putpixel((i * 2 + 1, j * 2 + 1), 255)
                    else:
                        # IMAGE OUT1
                        self.out1.putpixel((i * 2, j * 2), 0)
                        self.out1.putpixel((i * 2 + 1, j * 2), 0)
                        self.out1.putpixel((i * 2, j * 2 + 1), 255)
                        self.out1.putpixel((i * 2 + 1, j * 2 + 1), 255)
                        # IMAGE OUT2
                        self.out2.putpixel((i * 2, j * 2), 255)
                        self.out2.putpixel((i * 2 + 1, j * 2), 255)
                        self.out2.putpixel((i * 2, j * 2 + 1), 0)
                        self.out2.putpixel((i * 2 + 1, j * 2 + 1), 0)
                if pixel == 255: #WHITE -> the same
                    if x % 2 == 0:
                        # IMAGE OUT1
                        self.out1.putpixel((i * 2, j * 2), 255)
                        self.out1.putpixel((i * 2 + 1, j * 2), 255)
                        self.out1.putpixel((i * 2, j * 2 + 1), 0)
                        self.out1.putpixel((i * 2 + 1, j * 2 + 1), 0)
                        # IMAGE OUT2
                        self.out2.putpixel((i * 2, j * 2), 255)
                        self.out2.putpixel((i * 2 + 1, j * 2), 255)
                        self.out2.putpixel((i * 2, j * 2 + 1), 0)
                        self.out2.putpixel((i * 2 + 1, j * 2 + 1), 0)
                    else:
                        # IMAGE OUT1
                        self.out1.putpixel((i * 2, j * 2), 0)
                        self.out1.putpixel((i * 2 + 1, j * 2), 0)
                        self.out1.putpixel((i * 2, j * 2 + 1), 255)
                        self.out1.putpixel((i * 2 + 1, j * 2 + 1), 255)
                        # IMAGE OUT2
                        self.out2.putpixel((i * 2, j * 2), 0)
                        self.out2.putpixel((i * 2 + 1, j * 2), 0)
                        self.out2.putpixel((i * 2, j * 2 + 1), 255)
                        self.out2.putpixel((i * 2 + 1, j * 2 + 1), 255)

        self.out1.show()
        self.out2.show()
        self.out1.save('out1.png')
        self.out2.save('out2.png')
    def add_two_image_clean(self):
        image1 = Image.open('out1.png')
        image2 = Image.open('out2.png')
        output = Image.new('1', size=[int((image1.size[0]) / 2), int((image1.size[1]) / 2)])
        sizeX = output.size[0]
        sizeY = output.size[1]

        for i in range(0,sizeX, 1):
            for j in range(0, sizeY, 1):


                pixel1 = [image1.getpixel((i*2, j*2)), image1.getpixel((i*2+1, j*2)), image1.getpixel((i*2, j*2+1)), image1.getpixel((i*2+1, j*2+1))]
                pixel2 = [image2.getpixel((i*2, j*2)), image2.getpixel((i*2+1, j*2)),
                          image2.getpixel((i*2, j*2 + 1)), image2.getpixel((i*2+1, j*2+1))]
                #print("(i*2)", i*2, "(j*2)", j*2, "(i*2+1)", i*2+1,"(j*2)", j*2," (i*2)",i*2, "(j*2+1)", j*2+1, "(i*2+1)", i*2+1,"(j*2+1)", j*2+1)
                if np.array_equal(pixel1, pixel2):
                    output.putpixel((i,j),255)
                else:
                    output.putpixel((i,j),0)
        for i in range(sizeX-1, sizeX+1, 1):
            for j in range(sizeY - 1, sizeY + 1, 1):
                pixel1 = [image1.getpixel((i , j )), image1.getpixel((i + 1, j)),
                          image1.getpixel((i, j + 1)), image1.getpixel((i+ 1, j+1))]
                pixel2 = [image2.getpixel((i , j)), image2.getpixel((i + 1, j)),
                          image2.getpixel((i , j + 1)), image2.getpixel((i + 1, j+ 1))]

                # print("(i*2)", i * 2, "(j*2)", j * 2, "(i*2+1)", i * 2 + 1, "(j*2)", j * 2, " (i*2)", i * 2, "(j*2+1)",
                #       j * 2 + 1, "(i*2+1)", i * 2 + 1, "(j*2+1)", j * 2 + 1)
                if np.array_equal(pixel1, pixel2):
                    output.putpixel((int(i/2), int(j/2)), 255)
                else:
                    output.putpixel((int(i/2), int(j/2)), 0)


        output.show()
    def add_two_image(self):

        image1 = Image.open('out1.png')
        image2 = Image.open('out2.png')
        output = Image.new('1', image1.size)

        for x in range(image1.size[0]):
            for y in range(image1.size[1]):
                output.putpixel((x, y), min(image1.getpixel((x, y)), image2.getpixel((x, y))))

        output.show()
#622, 322




g = Cryptography_visual()
#g.put_pixel_to_image()
g.add_two_image()