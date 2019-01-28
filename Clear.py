import Color
import Window

from Window import glCreateWindow

# Limpiar pantalla con un solo color
def glClear():
    framebuffer = [
        [
            glColor(r, g, b)
            for x in range(widthW)
        ]
        for y in range(heightW)
    ]
