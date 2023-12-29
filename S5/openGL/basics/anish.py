from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

def Init():
    glClear(0,0,0,1)
    gluOrtho2D(300,-300,300,-300)

def draw(cx,cy,r,start_angle, end_angle, increment):
    glLineWidth(3)
    glColor3f(0,1,0)
    glBegin(GL_POINTS)
    # glVertex2f(cx,cy)
    for i  in range(start_angle,end_angle,increment):
        glVertex2f(cx+r*math.cos(math.pi*i/180),cy+r*math.sin(math.pi*i/180))
    glEnd() 

def circle():
    draw(0,0,60,90,-136, -1)
    draw(0,120,60,45, 270,1)
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowPosition(500,500)
    glutInitWindowSize(600,600)
    glutCreateWindow("SAMPLE")
    glutDisplayFunc(circle)
    Init()
    glutMainLoop()
main() 

