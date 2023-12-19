from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

for func in dir(gl):
    print(func)

for func in dir(glu):
    print(func)

for func in dir(glut):
    print(func)
