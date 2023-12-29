from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
from queue import Queue
import numpy as np

windowsize_x=500
windowsize_y=500
ws = 250

class background:
    
    water_level_y = windowsize_y/2 
    water_color = [0,0,1]
    sealevel=windowsize_y/2-water_level_y
    
    def _init_(self,level):
        self.water_level_y=level
        self.sealevel=windowsize_y/2-self.water_level_y
        
    def water(self):
        water_level_coordinates=[[-windowsize_x,-windowsize_y],[windowsize_x,-windowsize_y],[windowsize_x,self.sealevel],[-windowsize_x,self.sealevel]]
        polygon(self.water_color,water_level_coordinates)
        
    def waves(self,control):
        wave_count=8
        wave_amplitude=15
        x_increment=(windowsize_x/2)/(wave_count)
        
        points=[]
        xx=0
        yy=0
        shift=0
        if(control<25):
            shift=0
            
        else:
            shift=20
                    
        xx=self.sealevel
        yy=self.sealevel+wave_amplitude   
        y_val=[xx,yy]
        #wave 0 - 250
        for i in range(int(wave_count)+1):
            points.append([x_increment*(i)+shift,y_val[i%2]])
            
        print(points)
            
        polygon(self.water_color,points)
        
        
        points=[]
        #wave 0 - 250
        for i in range(int(wave_count)+1):
            points.append([0-x_increment*(i)+shift,y_val[i%2]])
            
        print(points)
            
        polygon(self.water_color,points)
        
    def boat(self,start_x,start_y,color=[1,0,0]):
        boat_color= color
        boat_width=60
        boat_height=40
        triangle_base=40
        rec_x=start_x+triangle_base
        rec_y=start_y+self.sealevel
        
        #rectangle
        rectangle_points=[[rec_x,rec_y],[rec_x+boat_width,rec_y],[rec_x+boat_width,rec_y+boat_height],[rec_x,rec_y+boat_height]]
        polygon(boat_color,rectangle_points)
        
        #left_triangle
        triangle_points1=[[rec_x,rec_y],[rec_x-triangle_base,rec_y+boat_height],[rec_x,rec_y+boat_height]]
        polygon(boat_color,triangle_points1)
        
        #right_triangle
        triangle_points2=[[rec_x+boat_width,rec_y],[rec_x+boat_width+triangle_base,rec_y+boat_height],[rec_x+boat_width,rec_y+boat_height]]
        polygon(boat_color,triangle_points2)
        
        #flag_pole
        flag_width=10
        flag_height=100
        pole_points=[[rec_x+boat_width/2,rec_y],[rec_x+boat_width/2+flag_width,rec_y],[rec_x+boat_width/2+flag_width,rec_y+flag_height],[rec_x+boat_width/2,rec_y+flag_height]]
        polygon(boat_color,pole_points)
        
        #flag
        flag_w=30
        flag_h=30
        flag_color=boat_color
        flag_points=[[rec_x+boat_width/2+flag_width,rec_y+flag_height-flag_h],[rec_x+boat_width/2+flag_width+flag_w,rec_y+flag_height-flag_h/2],[rec_x+boat_width/2+flag_width,rec_y+flag_height]]
        polygon(flag_color,flag_points)
        
    def rock(self,start_x,start_y):
        rock_color= [0.8,0.8,0.8]
        rock_width=60
        rock_height=40
        rec_x=start_x
        rec_y=start_y+self.sealevel
        
        #rectangle
        rectangle_points=[[rec_x,rec_y],[rec_x+rock_width,rec_y],[rec_x+rock_width,rec_y+rock_height],[rec_x,rec_y+rock_height]]
        polygon(rock_color,rectangle_points)
        
        
    
        
        
    
def circle(r,center,colour,angle=360):  
	glColor3f(colour[0],colour[1],colour[2])  
	glBegin(GL_TRIANGLE_FAN)  
	glVertex2f(center[0],center[1])  
	for i in range(0,angle+1,):  
		glVertex2f(r*math.cos(math.pi*i/180)+center[0],r*math.sin(math.pi*i/180)+center[1])  
	glEnd()  
	glFlush()
 
def polygon(color,list):
    glColor3f(color[0],color[1],color[2]) 
    glBegin(GL_POLYGON)
    for coordinate in list:
        glVertex2f(coordinate[0],coordinate[1])
    glEnd() 
    
def click_callback(button, state, x, y):
    global mouse_x, mouse_y
    mouse_x, mouse_y = x, glutGet(GLUT_WINDOW_HEIGHT) - y
    mouse_x=mouse_x-windowsize_x/2
    mouse_y=mouse_y-windowsize_y/2
    print(f"Mouse Clicked at: ({mouse_x:.2f}, {mouse_y:.2f})")
    

    
def animation():
    boat_max_inc=220
    boat_max_sink=165
    i=0
    
    for i in range (0,boat_max_inc):
        glClear(GL_COLOR_BUFFER_BIT)
        bg= background(windowsize_x/3*2)
        bg.water()
        bg.waves(i%50)
        bg.boat(-windowsize_x/2 + i,0)
        bg.rock(100,0)
        time.sleep(0.01)
        glutSwapBuffers()
        
    k=i
    
    for i in range (0,boat_max_sink):
        glClear(GL_COLOR_BUFFER_BIT)
        bg= background(windowsize_x/3*2)
        bg.water()
        bg.waves(i%50)
        bg.boat(-windowsize_x/2 +k,0-i,[1-(i/boat_max_sink),0,i/boat_max_sink])
        bg.rock(100,0)
        time.sleep(0.01)
        glutSwapBuffers()
        
    glFlush()
        
    i=boat_max_sink-2
    
        
    #flood_fill(-windowsize_x/2+boat_max_inc+40, -i-70, [0, 1, 0.5], get_pixel(-windowsize_x/2+boat_max_inc+40, -i-70))
            
    
        
def Display():
        animation()
    

	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(windowsize_x,windowsize_y)
	glutInitWindowPosition(0,0)
	glutCreateWindow("Ship sinking")
	glutDisplayFunc(lambda:Display())
	glutMouseFunc(click_callback)
	gluOrtho2D(-windowsize_x/2,windowsize_x/2,-windowsize_y/2,windowsize_y/2)
	glutMainLoop()
 
main()