from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from math import sin, cos, pi

# Function to draw a circle
def draw_circle():
    glColor3f(1, 0, 1)
    glLineWidth(2)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for i in range(0, 361):
        glVertex2f( 0.5*cos(pi*i/180), 0.5*sin(pi*i/180) )
    glEnd()
    glFlush()

# Function to handle all drawings
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white
    draw_circle()
    glutSwapBuffers()

# Initialize OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Set clear color to black
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set the coordinate system

# Main function
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"OpenGL Circle Example")
    glutDisplayFunc(lambda: draw())
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
