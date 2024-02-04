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

def triangle(vertices: list, color: list=DEFAULT_COLOR):
    glColor3f(*color)

    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        print("vertex: ", vertex)
        glVertex2fv(vertex)
    glEnd()

def polygon(vertices: list, color: list=DEFAULT_COLOR):
    glColor3f(*color)

    glBegin(GL_POLYGON)
    for vertex in vertices:
        print("vertex: ", vertex)
        glVertex2fv(vertex)
    glEnd()

def circle(center: list, radius, color: list=DEFAULT_COLOR):
    glColor(*color)

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(*center)

    for angle in range(0, 361):
        angle_in_radian = angle * (pi/180)
        glVertex2f(radius*cos(angle_in_radian), radius*sin(angle_in_radian))
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    vertices = []

    n = int(input("Enter number of spokes: "))
    """
    r = int(input("Enter radius: "))
    xc, yc = int(input("Enter center x: ")), int(input("Enter center y: "))
    """
    radius = 100
    xc, yc = 0, 0
    center = [xc, yc]
    base_angle = 360//n
    base_angle_in_rad = base_angle * (pi/180)

    # First triangle
    x1, y1 = radius, 0
    x2, y2 = radius*cos(base_angle_in_rad), radius*sin(base_angle_in_rad)

    x3, y3 = (x1+x2), (y1+y2)

    print(x1, y1, x2, y2, x3, y3)

    vertices.extend([
        [x1, y1],
        [x3, y3],
        [x2, y2]
    ])

    print(x3, y3)
    # Rotating first triangle n-1 times
    for i in range(n):
        # Don't need to repeat the first point, it's included in the last one
        # x1, y1 = x1*cos(base_angle_in_rad) - y1*sin(base_angle_in_rad), x1*sin(base_angle_in_rad) + y1*cos(base_angle_in_rad)

        x2, y2 = x2*cos(base_angle_in_rad) - y2*sin(base_angle_in_rad), x2*sin(base_angle_in_rad) + y2*cos(base_angle_in_rad)

        x3, y3 = x3*cos(base_angle_in_rad) - y3*sin(base_angle_in_rad), x3*sin(base_angle_in_rad) + y3*cos(base_angle_in_rad)

        vertices.extend([
            # [x1, y1],
            [x3, y3],
            [x2, y2]
        ])

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
