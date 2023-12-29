from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import math

bushesAt = [[0,300,100],[100,300,50],
            [200,300,75],[600,300,50],
            [675,300,75],[800,300,90]]
spotsToPaint = []
allThePaintedSpots = []
spot_height = 1
stickMan = [100,200]
treeVal = [[100,200,150,(71,46,1),(59,104,9)],
           [800,200,120,(72,45,2),(58,115,8)],
           [600,200,140,(73,44,2),(57,146,7)],
           [300,200,120,(74,43,4),(56,137,6)],
           [700,200,130,(75,42,5),(55,108,5)],
           [200,200,110,(76,41,6),(54,149,4)]]

def pine_tree(x,y,size,trunkclr,leafclr):
    glColor3ub(*trunkclr)
    glRectf(x+0.25*size,y,x+0.75*size,y+2*size)
    glColor3ub(*leafclr) # the `*` is used for unpacking the parameter from tuple
    glBegin(GL_TRIANGLES)
    glVertex2f(x-size,y+2*size)
    glVertex2f(x+2*size,y+2*size)
    glVertex2f(x+size/2,y+4*size)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(x-size/2,y+3*size)
    glVertex2f(x+1.5*size,y+3*size)
    glVertex2f(x+size/2,y+5*size)
    glEnd()

def pineTrees():
    global treeVal
    for tree in treeVal:
        pine_tree(tree[0],tree[1],tree[2],tree[3],tree[4])

def green_circle(centre_x,centre_y,radii):
    glColor3ub(6,89,40)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(centre_x,centre_y)
    for i in range(300+1):
        theta = i*(2.0*math.pi/300)
        x =  centre_x + radii*math.cos(theta)
        y =  centre_y + radii*math.sin(theta)
        glVertex2f(x,y)
    glEnd()

def bushes():
    glColor3ub(6,89,40)
    glRectf(0,200,800,300)
    global bushesAt
    for bush in bushesAt:
        green_circle(bush[0],bush[1],bush[2])

def head():
    pass

def stick_man():
    global stickMan
    pass

def generate_spots(x,ystart,ystop):
    global spotsToPaint 
    for y in range(ystart,ystop):
        spotsToPaint.append([x,y])
generate_spots(200,200,400)
generate_spots(250,200,400)
generate_spots(300,200,400)
generate_spots(350,350,400)
generate_spots(400,350,400)
generate_spots(450,200,400)
generate_spots(500,200,400)
generate_spots(550,200,400)

def sky():
    glColor3ub(103, 163, 252)   
    glRectf(0,0,800,800)

def ground():
    glColor3ub(54, 160, 81)   
    glRectf(0,0,800,200)

def paint_spot(blx,bly):
    global spot_height
    glColor3ub(188, 153, 115)
    spot_width = 50
    glRectf(blx, bly, blx+spot_width, bly+spot_height)

def painted_spots_loop():
    global allThePaintedSpots
    if len(allThePaintedSpots) == 0:
        return
    for spot in allThePaintedSpots:
        paint_spot(spot[0],spot[1])

def uncolored_house_struct():
    glColor3ub(170, 136, 100)   
    glRectf(200,200,600,400)

def door_handle():
    #glColor3ub(141, 140, 140)   
    glColor3ub(35, 35, 35)   
    glRectf(425,250,435,275)

def door_border():
    glColor3ub(73, 41, 7)   
    glRectf(350,200,450,350)

def inner_door():
    dw = 10 #design width for the door
    glColor3ub(89, 50, 7)   
    glRectf(350+dw,200+dw,450-dw,350-dw)

def door():
    door_border()
    inner_door()
    door_handle()

def chimmeny():
    glColor3ub(127, 96, 63)
    glRectf(550,400,600,600)
    glColor3ub(153, 29, 10)
    glRectf(545,600,605,620)


def roof():
    glBegin(GL_QUADS)
    glColor3ub(153, 29, 10)
    glVertex2f(100.0,400.0)
    glVertex2f(300,500)
    glVertex2f(500,500)
    glVertex2f(700.0,400.0)
    glEnd()

def draw_screen():
    time.sleep(0.01)
    sky()
    ground()
    #pine_tree(100,300,100)
    pineTrees()
    bushes()
    uncolored_house_struct()
    door()
    chimmeny()
    roof()
    painted_spots_loop()
    global allThePaintedSpots
    global spotsToPaint
    if(len(spotsToPaint)>0):
        tempSpot = spotsToPaint.pop(0)
        allThePaintedSpots.append(tempSpot)

def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_screen()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Man Painting His House")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
