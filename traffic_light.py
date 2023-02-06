from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from mid_point_circle import *
from mid_point_line import *

import math
from transformation import *

class traffic_light:
    def __init__(self, x0=0, y0=0, size = 100 ,delay = 10000, y_delay = 1000,change = 1):
        self.change = change
        self.x0 = x0
        self.y0 = y0
        self.delay = delay
        self.state = 1
        self.next_state = 2
        self.size = size

    def state_change(self):
        if self.change:
            temp = ""
            if self.state == 3 and self.next_state == 2:
                temp = 1
            elif self.state == 1 and self.next_state == 2:
                temp = 3
            elif self.state == 2:
                temp = 2
            self.state = self.next_state
            self.next_state = temp
    
    def draw(self):
        lst = []
        x0 = self.x0
        y0 = self.y0
        lst.extend(mid_line(0, 0, 0, self.size))
        lst.extend(mid_line(0, self.size, self.size/2, self.size))
        lst.extend(mid_line(self.size/2, self.size, self.size/2, 0))
        lst.extend(mid_line(self.size/2, 0, 0, 0))
        lst.extend(mid_line(0 , self.size/2, -200,self.size/2))
        lst.extend(mid_circle(self.size/8, self.size/4, self.size/4))
        lst.extend(mid_circle(self.size/8, self.size/4, 2*self.size/4))
        lst.extend(mid_circle(self.size/8, self.size/4, 3*self.size/4))
        glBegin(GL_POINTS)
        for a in lst:
            x,y = a[0] , a[1]
            glVertex2f( x + self.x0, y + self.y0)
        glEnd()
        lst = []
        r = self.size/8
        while r>1:
            lst.extend(mid_circle(r, self.size/4, self.state*self.size/4))
            r-=1
        if self.state == 1:
            glColor3f(0, 1, 0)
        elif self.state == 2:
            glColor3f(1, 1, 0)
        else :
            glColor3f(1, 0, 0)

        glBegin(GL_POINTS)
        for a in lst:
            x,y = a[0] , a[1]
            glVertex2f( x + self.x0, y + self.y0)
        glEnd()

