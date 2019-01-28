import struct
import random

from random import randint

def char(c):
	return struct.pack("=c", c.encode('ascii'))

def word(c):
	return struct.pack("=h", c)

def dword(c):
	return struct.pack("=l", c)

def glColor(r, g, b):
    r = r * 255
    g = g * 255
    b = b * 255
    color = bytes ([r, g, b])
    return color

class PuntoBlanco(object):
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.framebuffer = []
        self.glClear()

    def glClear(self):
        self.framebuffer = [
            [
                glColor(0, 0, 0)
                    for x in range(self.width)
            ]
            for x in range(self.height)
        ]   
        
    def write(self, filename):
        f = open(filename, "bw")

		#file header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 * 40 * self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

		#image header 40
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])

        f.close()

    def glVertex(self, x, y, color):
        #x = ((((x + 1)/2) * (self.width)) + self.x)
        #y = ((((y + 1)/2) * (self.height)) + self.y)
        self.framebuffer[x][y] = color


r = PuntoBlanco(480, 480, 0, 0)

for sum0 in range(0,479):
    if random.random() <= 1:
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
        r.glVertex(randint(0,479), randint(0,479), glColor(1,1,1))
    else:
        r.glVertex(randint(0,479), randint(0,479), glColor(0,0,0))

"""
for sum1 in range(0,479):
    r.glVertex(randint(0,479), randint(0,479), glColor(1,1,0))

for sum2 in range(0,479):
    r.glVertex(randint(0,479), randint(0,479), glColor(1,0,0))

for sum3 in range(0,479):
    r.glVertex(randint(0,479), randint(0,479), glColor(0,1,0))

for sum4 in range(0,479):
    r.glVertex(randint(0,479), randint(0,479), glColor(0,1,1))

for sum5 in range(0,479):
    r.glVertex(randint(0,479), randint(0,479), glColor(0,0,1)) 
"""
r.write("cable.bmp")