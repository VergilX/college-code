from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import time

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def line(vertices):
    glColor3f(1, 1, 1, 1)
    glLineWidth(2)
    glBegin(GL_LINES)
    # Define vertices
    for vertex in vertices:
        glVertex2fv(vertex)

    glEnd()
    glutSwapBuffers()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    n = int(input("Enter number of lines: "))

    for i in range(n):
        vertices = []
        print(f"Vertex {i+1}")
        for j in range(2):
            vertices.append([ int(input(f"x{j+1}: ")), int(input(f"y{j+1}: ")) ])
            print(vertices)
        line(vertices)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Ass-win is.. you know")
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(600, 0)

    glutDisplayFunc(lambda: draw())
    # glutIdleFunc(lambda: draw())

    init()
    glutMainLoop()

main()
