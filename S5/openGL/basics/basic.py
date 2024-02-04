from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import sin, cos, pi
import sys
import time

DEFAULT_COLOR = [1, 1, 1, 1] # Don't mean to be racist here
CENTER = [0, 0]

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

def circle(center: list, radius, start=0, stop=360, color: list=DEFAULT_COLOR, hollow=False):
    glColor3f(*color)

    if not hollow:
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(*center)
    else:
        glBegin(GL_POINTS)

    for angle in range(start, stop+1):
        angle_in_radian = (pi/180) * angle
        glVertex2f( center[0]+(radius*cos(angle_in_radian)), 
                    center[1]+(radius*sin(angle_in_radian)) )

    glEnd()

def draw():
    """ Draw whatever shit you want here using
        the above functions
    """
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw anything you want
    # point(0, 0, [0, 1, 0, 1])
    # line(1, 1, 100, 100, [1, 1, 1, 1])
    # square([[0, 0], [0, 100], [100, 100], [100, 0]], [0, 1, 1, 1])
    # triangle([[0, 0], [50, 50], [100, 0]], [1, 1, 0, 1])
    circle([0, 0], 100, 90, 270, hollow=True)
    circle([0, -200], 100, 270, 450, hollow=True)

    glutSwapBuffers() 

def animate():
    global CENTER

    glClear(GL_COLOR_BUFFER_BIT)

    # draw and update what you want
    circle(CENTER, 50)

    CENTER[0] += 10
    if CENTER[0] == 250:
        CENTER[0] = -250
    time.sleep(0.1)
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("BASICS")
    glPointSize(2)

    glutDisplayFunc(draw)
    
    # for animation
    glutDisplayFunc(animate)
    glutIdleFunc(animate)

    init()
    glutMainLoop()

main()
