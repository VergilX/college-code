from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy
import sys

DEFAULT_COLOR = [1, 1, 1, 1]
WINDOW_SIZE = 600

sys.setrecursionlimit(100000)

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def point(x, y, color: list=DEFAULT_COLOR):
    glColor3f(*color)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def line(x1, y1, x2, y2, color: list=DEFAULT_COLOR):
    glColor3f(*color)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def square(vertices: list, color: list=DEFAULT_COLOR):
    glColor3f(*color)

    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()

def triangle(vertices: list, color: list=DEFAULT_COLOR):
    glColor3f(*color)

    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()

def get_pixel(x, y):
    pixel = glReadPixels(x, WINDOW_SIZE-y, 1, 1, GL_RGB, GL_FLOAT)
    return [round(color, 1) for color in pixel[0][0]]

def set_pixel(x, y, fill_color: list):
    glColor3f(*fill_color)
    glBegin(GL_POINTS)

    # Convert window coordinates to cartesian 
    # and plot
    cartesian_x = x-WINDOW_SIZE//2
    cartesian_y = WINDOW_SIZE//2-y
    glVertex2f(cartesian_x, cartesian_y)

    glEnd()
    glutSwapBuffers()

def boundary_fill(x, y, boundary_color: list, new_color: list):
    pixel = get_pixel(x, y)
    print(pixel, boundary_color, pixel == boundary_color)
    if (pixel != boundary_color and pixel!=new_color):
        print(x, y)
        set_pixel(x, y, new_color)

        # four point movement excluding boundary
        # if exceeding boundary, don't do dat
        boundary_fill(x+1, y, boundary_color, new_color)
        boundary_fill(x, y+1, boundary_color, new_color)
        boundary_fill(x-1, y, boundary_color, new_color)
        boundary_fill(x, y-1, boundary_color, new_color)

    return

def flood_fill(x, y, old_color: list, new_color: list):
    pixel = get_pixel(x, y)

    if (pixel == old_color):
        set_pixel(x, y, new_color)

        # four point movement
        flood_fill(x+1, y, old_color, new_color)
        flood_fill(x, y+1, old_color, new_color)
        flood_fill(x-1, y, old_color, new_color)
        flood_fill(x, y-1, old_color, new_color)

def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        # print(x, y, "  ", end="")
        # print(get_pixel(x, y))

        # Add filling algorithm
        flood_fill(x, y, [1, 0, 0], [0, 1, 1])

def draw():
    # square with boundary
    glClear(GL_COLOR_BUFFER_BIT)
    # square([[0, 0], [0, 100], [100, 100], [100, 0]], [1, 0, 0])
    # square([[-300, -300], [-300, 300], [300, 300], [300, -300]])
    # line(0, 0, 0, 100)
    # line(0, 100, 100, 100)
    # line(100, 100, 100, 0)
    # line(0, 0, 100, 0)

    triangle([[0, 0], [100, 100], [200, 0]], [1, 0, 0])

    # point(0, 0)

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("Filling")
    glPointSize(1)

    glutDisplayFunc(draw)

    # mouse click
    glutMouseFunc(mouse_click)

    init()
    glutMainLoop()

main()
