from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import time

sq_vertices = [
        [0, 0],
        [0, 50],
        [50, 50],
        [50, 0]
        ]

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def square(vertices):
    global sq_vertices

    glColor3f(1, 1, 1, 1)
    glBegin(GL_QUADS)

    for vertex in sq_vertices:
        print(vertex)
        glVertex2f(vertex[0], vertex[1])

    # Reset if hits the edges
    if sq_vertices[1][0] >= 300:
        sq_vertices = [
                [-300, 0],
                [-300, 50],
                [-250, 50],
                [-250, 0]
                ]

    glEnd()
    glutSwapBuffers()

def draw():
    global sq_vertices

    glClear(GL_COLOR_BUFFER_BIT)
    time.sleep(0.2)
    square(sq_vertices)

    for vertex in sq_vertices:
        vertex[0] += 5
        # vertex[1] += 1

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("animation")

    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    # glutTimerFunc(0, animate, 0)

    init()
    glutMainLoop()

main()
