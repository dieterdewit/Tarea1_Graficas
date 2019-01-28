import struct
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

    def glViewPort(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width -1
        self.height = height -1

    def glVertex(self, x, y, color):
        #x = ((((x + 1)/2) * (self.width)) + self.x)
        #y = ((((y + 1)/2) * (self.height)) + self.y)
        self.framebuffer[x][y] = color


r = PuntoBlanco(160, 192, 0, 0)

for cielo in range(0,159):
    r.glVertex(randint(0,159), randint(0,159), glColor(1,1,1))

for exp in range(70,110):
    r.glVertex(randint(70,110), randint(70,110), glColor(0,1,1))

for exp in range(70,110):
    r.glVertex(randint(70,110), randint(70,110), glColor(0,0,1))

for malo in range(25,30):
    r.glVertex(malo, 30, glColor(0,1,0))
    r.glVertex(malo, 35, glColor(0,1,0))
    for malo0 in range(30,36):
        r.glVertex(malo, malo0, glColor(0,1,0))
        r.glVertex(malo, malo0, glColor(0,1,0))

for malo in range(94,99):
    r.glVertex(malo, 78, glColor(0,1,0))
    r.glVertex(malo, 83, glColor(0,1,0))
    for malo0 in range(78,84):
        r.glVertex(malo, malo0, glColor(0,1,0))
        r.glVertex(malo, malo0, glColor(0,1,0))

for malo in range(125,130):
    r.glVertex(malo, 58, glColor(0,1,0))
    r.glVertex(malo, 63, glColor(0,1,0))
    for malo0 in range(58,64):
        r.glVertex(malo, malo0, glColor(0,1,0))
        r.glVertex(malo, malo0, glColor(0,1,0))

for mira in range(91,101):
    r.glVertex(mira, 75, glColor(0,0,1))
    r.glVertex(mira, 85, glColor(0,0,1))
    for mira2 in range(75,86):
        r.glVertex(91, mira2, glColor(0,0,1))
        r.glVertex(101, mira2, glColor(0,0,1))

for sum in range(62,106):
    ex = sum + 35
    yay = sum + 20
    r.glVertex(ex, yay, glColor(0,0,1))

for sum in range(15,59):
    ex = sum + 37
    yay = sum + 20
    r.glVertex(ex, yay, glColor(0,0,1))

for sum in range(15,59):
    ex = - sum - 20
    yay = sum + 37
    r.glVertex(yay, ex, glColor(0,0,1))

for sum in range(15,59):
    ex = - sum - 67
    yay = sum + 82
    r.glVertex(yay, ex, glColor(0,0,1))

for mira in range(51,141):
    r.glVertex(mira, 35, glColor(1,0,0))
    r.glVertex(mira, 125, glColor(1,0,0))
    for mira2 in range(35,126):
        r.glVertex(51, mira2, glColor(1,0,0))
        r.glVertex(141, mira2, glColor(1,0,0))

for mira in range(46,146):
    r.glVertex(mira, 30, glColor(1,1,0))
    r.glVertex(mira, 131, glColor(1,1,0))
    for mira2 in range(30,132):
        r.glVertex(46, mira2, glColor(1,1,0))
        r.glVertex(146, mira2, glColor(1,1,0))

for score in range(165,190):
    r.glVertex(score, 52, glColor(1,1,0))
    r.glVertex(score, 60, glColor(1,1,0))
    for score3 in range(52,61):
        r.glVertex(score, score3, glColor(1,1,0))
        r.glVertex(score, score3, glColor(1,1,0))

for score in range(185,190):
    r.glVertex(score, 46, glColor(1,1,0))
    r.glVertex(score, 60, glColor(1,1,0))
    for score3 in range(46,60):
        r.glVertex(score, score3, glColor(1,1,0))
        r.glVertex(score, score3, glColor(1,1,0))

for score in range(165,190):
    r.glVertex(score, 112, glColor(1,1,0))
    r.glVertex(score, 120, glColor(1,1,0))
    for score3 in range(112,121):
        r.glVertex(score, score3, glColor(1,1,0))
        r.glVertex(score, score3, glColor(1,1,0))

for score in range(185,190):
    r.glVertex(score, 106, glColor(1,1,0))
    r.glVertex(score, 120, glColor(1,1,0))
    for score3 in range(106,121):
        r.glVertex(score, score3, glColor(1,1,0))
        r.glVertex(score, score3, glColor(1,1,0))

for score in range(175,180):
    r.glVertex(score, 106, glColor(1,1,0))
    r.glVertex(score, 120, glColor(1,1,0))
    for score3 in range(106,121):
        r.glVertex(score, score3, glColor(1,1,0))
        r.glVertex(score, score3, glColor(1,1,0))

for score in range(165,170):
    r.glVertex(score, 106, glColor(1,1,0))
    r.glVertex(score, 120, glColor(1,1,0))
    for score3 in range(106,121):
        r.glVertex(score, score3, glColor(1,1,0))
        r.glVertex(score, score3, glColor(1,1,0))

for sum in range(130, 155):
    ex = sum + 36
    yay = sum - 60
    r.glVertex(ex, yay, glColor(1,1,1))








r.write("AtariSpace.bmp")