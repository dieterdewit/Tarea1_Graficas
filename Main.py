import struct
import Color
import Clear
import ClearColor
import Finish
import Init
import Vertex
import ViewPort
import Window

from Clear import glClear

def char(c):
	return struct.pack("=c", c.encode('ascii'))

def word(c):
	return struct.pack("=h", c)

def dword(c):
	return struct.pack("=l", c)

Color.glColor(0, 0, 0)

class PuntoBlanco(object):
	def __init__(self):
		self.framebuffer = []
		self.glClear()

	def glClear(self):
		self.framebuffer = [
			[
				color(0, 0, 0)
					for x in range(widthW)
			]
			for x in range(heightW)
		]

	def glfinish(self, filename):
		f = open(filename, "bw")

		#Header del Archivo
		f.glFinish(char('B'))
		f.glFinish(char('M'))
		f.glFinish(dword(1680 * self.width * self.height))
		f.glFinish(dword(0))
		f.glFinish(dword(54))

		#Header de la Imagen
		f.glFinish(dword(40))
		f.glFinish(dword(self.width))
		f.glFinish(dword(self.height))
		f.glFinish(word(1))
		f.glfinish(word(24))
		f.glfinish(dword(0))
		f.glFinish(dword(self.width * self.height * 3))
		f.glFinish(dword(0))
		f.glFinish(dword(0))
		f.glFinish(dword(0))
		f.glFinish(dword(0))

		for x in range(self.height):
			for y in range(self.width):
				f.glFinish(self.framebuffer[x][y])

		f.close()

	def point(self, x, y, glColor):
		self.framebuffer[x][y] = glColor


	Window.glCreateWindow(600,400)

r = PuntoBlanco()
r.point(100,200, glColor(1,1,1))
r.write("punto.bmp")

	






