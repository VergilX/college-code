from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import pi, cos, sin

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

"""
def get_choice():
    print("Enter what transformation is to be done: ")
    """

def triangle(vertices, color):
    glColor3f(*color)

    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2fv(vertex)

    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    vertices = [
            [0, 0],
            [100, 0],
            [0, 100]
            ]
    triangle(vertices, (0, 0, 0.5))

    theta = 180 * (pi/180)

    glColor3f(0, 1, 0, 1)
    for vertex in vertices:
        vertex[0] = vertex[0]*cos(theta) + vertex[1]*sin(theta)
        vertex[1] = vertex[1]*cos(theta) - vertex[0]*sin(theta)

    print(vertices)
    triangle(vertices, (0, 0.75, 0))

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)

    glutInitWindowPosition(600, 0)
    glutInitWindowSize(600, 600)
    glutCreateWindow("2D transformations")

    glutDisplayFunc(draw)
    init()
    glutMainLoop()

main()
