# Escribe el archivo
def glfinish(self, filename):
		f = open(filename, "bw")

		#Header del Archivo
		f.write(char('B'))
		f.write(char('M'))
		f.write(dword(1680 * self.width * self.height))
		f.write(dword(0))
		f.write(dword(54))

		#Header de la Imagen
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

        

