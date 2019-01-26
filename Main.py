import struct
import Color
import Clear
import ClearColor
import Finish
import Init
import Vertex
import ViewPort
import Window

def char(c):
	return struct.pack("=c", c.encode('ascii'))

def word(c):
	return struct.pack("=h", c)

def dword(c):
	return struct.pack("=l", c)

Color.glColor(0,0,0,0)

print(color)


