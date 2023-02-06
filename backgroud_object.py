from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
from mid_point_line import *
from mid_point_circle import *
from transformation import *

k_x = 0.995
k_y = 0.995

def draw_road(scr_width , y0 =-280, w= 20, color = (1,1,1)):
    x = 0
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    while x <= scr_width/2:
        glVertex2f(x, y0)
        glVertex2f(-x, y0)
        glVertex2f(x, y0+w)
        glVertex2f(-x, y0+w)
        x+=1
    glEnd()

def building_row(scr_width, y = 0, size = 20, color = (1,1,1), points = []):
    glColor3f(color[0], color[1], color[2])
    if not len(points):
        x = -scr_width/2
        width = [1,2,3,4,5]
        height = [1,2,3,4,5]
        while x <= scr_width/2:
            w = random.choice(width)
            h = random.choice(height)
            points.extend(mid_line(x,y,x+w*size,y))
            points.extend(mid_line(x,y,x,y+h*size))
            points.extend(mid_line(x+w*size,y,x+w*size,y+h*size))
            points.extend(mid_line(x+w*size,y+h*size,x,y+h*size))
            for a in range(w):
                for b in range(h):
                    window_x = x + size/3 + size * a
                    window_y = y + size/3 + size * b
                    w_size = size/3
                    points.extend(mid_line(window_x, window_y,window_x + w_size, window_y))
                    points.extend(mid_line(window_x+ w_size, window_y,window_x+ w_size, window_y+ w_size))
                    points.extend(mid_line(window_x+ w_size, window_y+ w_size,window_x, window_y + w_size))
                    points.extend(mid_line(window_x, window_y,window_x, window_y + w_size))
            x+=w*size

    glBegin(GL_POINTS)
    for a in points:
        glVertex2f(a[0], a[1])
    glEnd()
     
    return points

def sun(x0, y0, t = 0,points = [], r = 30, sun_counter = 0):
    global k_x, k_y
    glColor3f(1, 1, 0)
    b = 0
    if len(points) == 0:
        points.extend(mid_circle(r, x0 = x0, y0 = y0))
        num = 40/360 * math.pi
        for a in range(20):
            if b:
                x1 = x0 + math.sin(num*a) * (r +20)
                y1 = y0 + math.cos(num*a) * (r +20)
                x2 = x0 + math.sin(num*a) * (r+30)
                y2 = y0 + math.cos(num*a) * (r+30)
                b = 0
            else :
                x1 = x0 + math.sin(num*a) * (r+20)
                y1 = y0 + math.cos(num*a) * (r+20)
                x2 = x0 + math.sin(num*a) * (r+15)
                y2 = y0 + math.cos(num*a) * (r+15)
                b = 1
            points.extend(mid_line(x1,y1,x2,y2))
        
    
    glBegin(GL_POINTS)
    i =0
    if sun_counter == 20:
        if k_x == 0.995:
            k_x = 1.005
            k_y = 1.005
        else:
            k_x = 0.995
            k_y = 0.995
        sun_counter = 0
    while i< len(points):
        points[i] = (points[i][0] - x0, points[i][1]-y0)
        points[i] = rotate(t,points[i][0],points[i][1])
        points[i] = scaling(k_x = k_x, k_y = k_y, x = points[i][0], y = points[i][1])
        points[i] = (points[i][0] + x0, points[i][1]+y0)
        glVertex2f(points[i][0], points[i][1])
        i+=1
    sun_counter+=1
    glEnd()
    return points , sun_counter

def moon(x0, y0, t = 0,points = [], r = 30, moon_counter = 0):
    global k_x, k_y
    glColor3f(1, 1, 1)
    b = 0
    if len(points) == 0:
        points.extend(mid_circle(r, x0 = x0, y0 = y0))
        points.extend(mid_circle(r/3, x0 = x0 + r/2, y0 = y0-r/2))
        points.extend(mid_circle(r/4, x0 = x0 + r/2, y0 = y0-r/2))
        points.extend(mid_circle(r/5, x0 = x0 + r/2, y0 = y0-r/2))
        points.extend(mid_circle(r/5, x0 = x0 - r/4, y0 = y0 + r/4))
        points.extend(mid_circle(r/6, x0 = x0 - r/4, y0 = y0 + r/4))
        points.extend(mid_circle(r/6, x0 = x0+r/3, y0 = y0+r/3))
        
    
    glBegin(GL_POINTS)
    i =0
    if moon_counter == 20:
        if k_x == 0.995:
            k_x = 1.005
            k_y = 1.005
        else:
            k_x = 0.995
            k_y = 0.995
        moon_counter = 0
    while i< len(points):
        points[i] = (points[i][0] - x0, points[i][1]-y0)
        points[i] = rotate(t,points[i][0],points[i][1])
        points[i] = scaling(k_x = k_x, k_y = k_y, x = points[i][0], y = points[i][1])
        points[i] = (points[i][0] + x0, points[i][1]+y0)
        glVertex2f(points[i][0], points[i][1])
        i+=1
    moon_counter+=1
    glEnd()
    return points , moon_counter