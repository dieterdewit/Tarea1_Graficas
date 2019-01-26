# Limpiar pantalla con un solo color
def glClear(self):
    self.framebuffer = [
        [
            color(r, g, b)
            for x in range(self.width)
        ]
        for y in range(self.height)
    ]
