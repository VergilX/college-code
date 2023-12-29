from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def triangle(v1_x, v1_y, v2_x, v2_y, v3_x, v3_y, r, g, b, a):
    glColor3f(r, g, b, a) # Color of triangle

    glBegin(GL_TRIANGLES) # Start triangle construction

    # Define vertices
    glVertex2f(v1_x, v1_y)
    glVertex2f(v2_x, v2_y)
    glVertex2f(v3_x, v3_y)
    
    # End construction
    glEnd()

def circle(radius, center_x, center_y, start_angle, stop_angle, color_r, color_g, color_b, color_a):
    glColor3f(color_r, color_g, color_b, color_a) # Set color of circle using parameters

    # Begin circle construction
    glBegin(GL_TRIANGLE_FAN)

    # Plot centre and apply 360degree
    glVertex2f(center_x, center_y) # Centre
    for theta in range(start_angle, stop_angle+1):
        theta_in_radians = theta * (math.pi/180)
        glVertex2f( center_x+radius*math.cos(theta_in_radians), center_y+radius*math.sin(theta_in_radians) )

    # Finish circle definition
    glEnd()

def line( x1, y1, x2, y2, r, g, b, a):
    glColor3f(r, g, b, a)
    glLineWidth(10)

    glBegin(GL_LINES)

    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    # Make circles using functions defined above
    circle(75, 0, 0, 0, 360, 1, 1, 1, 1) # Body
    circle(30, 0, 105, 0, 360, 1, 1, 1, 1) # Head
    # Nose
    triangle(0, 95, 0, 105, 20, 96, 0.7, 0, 0, 1)

    # Eyes
    circle(5, 15, 120, 0, 360, 0, 0, 0, 1)
    circle(5, -15, 120, 0, 360, 0, 0, 0, 1)
    
    #hand
    line(50, 50, 80, 65, 0, 0.5, 0, 1)
    line(-50, 50, -80,  65 , 0,  0.5, 0, 1)


    # display on screen (memory->screen)
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)

    # Window description functions
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("Anish is gay")

    glutDisplayFunc(draw) # must be after window definitions
    init()
    glutMainLoop()
    

main()
