import struct
from random import randint as random

def char(c):
	return struct.pack("=c", c.encode('ascii'))

def word(c):
	return struct.pack("=h", c)

def dword(c):
	return struct.pack("=l", c)

def color(r, g, b):
	return bytes ([b, g, r])

class Bitmap(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.framebuffer = []
		self.clear()

	def clear(self):
		self.framebuffer = [
			[
				color(0, 0, 0)
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

	def point(self, x, y, color):
		self.framebuffer[x][y] = color

r = Bitmap(600, 400)
r.point(100,200, color(255, 255, 0))
r.write("out.bmp")