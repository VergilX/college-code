from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import sin, cos, pi
import sys

WINDOW_SIZE = 600
DEFAULT_COLOR = [1, 1, 1, 1]

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-(WINDOW_SIZE//2), WINDOW_SIZE//2, -(WINDOW_SIZE//2), WINDOW_SIZE//2)

def polygon(vertices: list, color: list=DEFAULT_COLOR):
    glColor3f(*color)

    glBegin(GL_POLYGON)
    for vertex in vertices:
        print("vertex: ", vertex)
        glVertex2fv(vertex)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    vertices = []

    n = int(input("Enter number of spokes: "))
    """
    r = int(input("Enter radius: "))
    xc, yc = int(input("Enter center x: ")), int(input("Enter center y: "))
    """
    r = 100
    xc, yc = 0, 0
    base_angle = 360//n
    base_angle_in_rad = base_angle * (pi/180)
    # print(base_angle_in_rad)
    print(r*sin(base_angle_in_rad), r*cos(base_angle_in_rad))
    # print(r*sin(base_angle), r*cos(base_angle))
    
    # exit()

    # First triangle
    x1, y1 = r, 0
    x2, y2 = r*cos(base_angle_in_rad), r*sin(base_angle_in_rad)
    # x2, y2 = r*cos(base_angle), r*sin(base_angle)

    x3, y3 = (x1+x2), (y1+y2)

    print(x1, y1, x2, y2, x3, y3)

    vertices.extend([
        [x1, y1],
        [x2, y2],
        [x3, y3]
    ])

    polygon(vertices)


    """
    # Logic implementation
    for angle in range(1, 361, base_angle/2):
        # On circle
        if angle % base_angle == 0:
            x = 
        # outside circle
        else:
            pass
    """


    polygon(vertices)
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("Nemesis")

    glutDisplayFunc(display)

    init()
    glutMainLoop()

main()
