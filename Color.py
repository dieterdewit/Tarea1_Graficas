# Cambia el color para glVertex
def glColor(self, r, g, b):
    r = r * 255
    g = g * 255
    b = b * 255
    color = bytes ([r, g, b])
    return color
    #return glColor
