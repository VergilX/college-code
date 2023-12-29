from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def triangle():
    pass

def draw():
    glColor3f(0, 0, 1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    glVertex2f(0, 50)
    glVertex2f(50, 50)

    glEnd()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutDisplayFunc(draw)

    # Window description functions
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("Anish is gay")

    init()
    glutMainLoop()
    

main()
