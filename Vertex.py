# Cambiar el color de un punto del ViewPort
import Color

def glVertex(self, x, y, glColor):
    x = ((((x + 1)/2) * (self.width)) + self.x)
    y = ((((y + 1)/2) * (self.height)) + self.y)
    self.framebuffer[x][y] = bytes ([r, g, b])