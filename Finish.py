# Escribe el archivo
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

        

