from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import time

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def circle():
    pass

def line():
    pass

def draw():
    pass

def main():
    glutInit(sys.argv)
    glutInitWindowSize(600, 600)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("SNOWMAN")
    
    init()
    glutDisplayFunc(lambda: draw())
    glutMainLoop()

main()
