from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from mid_point_circle import *
from mid_point_line import *
import math
from transformation import *
import random

class car:
    def __init__(self, body_size = 200, x0 = 0, y0 = 0, max_speed = 2, accelaration = 0.01, curr_s = -1, show_tyre = 1):
        self.body_size = body_size
        self.max_s = max_speed
        self.curr_s = curr_s
        self.a = accelaration
        self.show_tyre = show_tyre
        self.x0 = x0
        self.y0 = y0
        self.body_points = []
        self.body_points.extend(mid_line(0, 0, body_size, 0))
        self.body_points.extend(mid_line(0, 0, 0, body_size/4))
        self.body_points.extend(mid_line(0, body_size/4, body_size/8, body_size/4))
        self.body_points.extend(mid_line(body_size/8, body_size/4, body_size/2, body_size/2))
        self.body_points.extend(mid_line(body_size/2, body_size/2, body_size*3/4 , body_size/2))
        self.body_points.extend(mid_line(body_size*3/4 , body_size/2 , body_size, body_size/4))
        self.body_points.extend(mid_line(body_size, body_size/4, body_size, 0))
        self.color = (random.uniform(0.8,1.0), random.uniform(0.8,1.0), random.uniform(0.8,1.0))

        self.tyre1_points = []
        self.tyre2_points = []
        tyre_width = 2
        for a in range(tyre_width):
            self.tyre1_points.extend(mid_circle(body_size/8+a, body_size/4, 0))
            self.tyre2_points.extend(mid_circle(body_size/8+a, body_size*3/4, 0))
        x = math.cos(math.pi/4) * body_size/8
        y = math.sin(math.pi/4) * body_size/8
        r = body_size/8
        self.tyre_r = r

        self.tyre1_points.extend(mid_line(body_size/4, 0, body_size/4+r, 0))
        self.tyre1_points.extend(mid_line(body_size/4, 0, body_size/4-r, 0))
        self.tyre1_points.extend(mid_line(body_size/4, 0, body_size/4, r))
        self.tyre1_points.extend(mid_line(body_size/4, 0, body_size/4, -r))
        self.tyre1_points.extend(mid_line(body_size/4, 0, body_size/4+x, 0+y))
        self.tyre1_points.extend(mid_line(body_size/4, 0, body_size/4+x, 0-y))
        self.tyre1_points.extend(mid_line(body_size/4, 0, body_size/4-x, 0-y))
        self.tyre1_points.extend(mid_line(body_size/4, 0, body_size/4-x, 0+y))
    
        self.tyre2_points.extend(mid_line(body_size/4 + body_size/2, 0, body_size/4+r+ body_size/2, 0))
        self.tyre2_points.extend(mid_line(body_size/4+ body_size/2, 0, body_size/4-r+ body_size/2, 0))
        self.tyre2_points.extend(mid_line(body_size/4+ body_size/2, 0, body_size/4+ body_size/2, r))
        self.tyre2_points.extend(mid_line(body_size/4+ body_size/2, 0, body_size/4+ body_size/2, -r))
        self.tyre2_points.extend(mid_line(body_size/4+ body_size/2, 0, body_size/4+x+ body_size/2, 0+y))
        self.tyre2_points.extend(mid_line(body_size/4+ body_size/2, 0, body_size/4+x+ body_size/2, 0-y))
        self.tyre2_points.extend(mid_line(body_size/4+ body_size/2, 0, body_size/4-x+ body_size/2, 0-y))
        self.tyre2_points.extend(mid_line(body_size/4+ body_size/2, 0, body_size/4-x+ body_size/2, 0+y))

    def draw(self):
        glBegin(GL_POINTS)
        glColor3f(self.color[0],self.color[1],self.color[2])
        for a in self.body_points:
            x,y = a[0] , a[1]
            glVertex2f( x + self.x0, y + self.y0)
        if self.show_tyre:
            for a in self.tyre1_points:
                x,y = a[0] , a[1]
                glVertex2f( x + self.x0, y + self.y0)
            for a in self.tyre2_points:
                x,y = a[0] , a[1]
                glVertex2f( x + self.x0, y + self.y0)
        glEnd()

    def move(self):
        self.x0 += self.curr_s
        self.y0 += 0
        i = 0
        while i < len(self.tyre1_points):
            self.tyre1_points[i] = translate(self.tyre1_points[i][0], self.tyre1_points[i][1], move_x= -self.body_size/4 )
            self.tyre1_points[i] = rotate(self.curr_s/(self.tyre_r*2), self.tyre1_points[i][0], self.tyre1_points[i][1])
            self.tyre1_points[i] = translate(self.tyre1_points[i][0], self.tyre1_points[i][1], move_x= +self.body_size/4 )
            i+=1
        
        i = 0
        while i < len(self.tyre2_points):
            self.tyre2_points[i] = translate(self.tyre2_points[i][0], self.tyre2_points[i][1], move_x= -self.body_size*3/4 )
            self.tyre2_points[i] = rotate(self.curr_s/(self.tyre_r*2), self.tyre2_points[i][0], self.tyre2_points[i][1])
            self.tyre2_points[i] = translate(self.tyre2_points[i][0], self.tyre2_points[i][1], move_x= +self.body_size*3/4 )
            i+=1
    
    def accelarate(self, direction = -1):
        if abs(self.max_s)> abs(self.curr_s):
            self.curr_s += self.a * direction
    
    def deacclerate(self, direction = -1):
        if self.curr_s > 0:
            self.curr_s -= self.a * direction

def create_car(body_size , x0 , y0 , curr_s , max_speed = -2 , accelaration = 0.01):
    return car(body_size , x0 , y0 , max_speed , accelaration , curr_s )


