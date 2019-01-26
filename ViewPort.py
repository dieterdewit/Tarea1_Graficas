# Definir el area de edicion de la imagen
def glViewPort(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width -1
    self.height = height -1