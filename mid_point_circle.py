from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def mid_circle(r , x0 = 0, y0 = 0):
    lst = []
    d = 1 - r
    x = 0
    y = r
    while (x<=y):
        """
        glBegin(GL_POINTS)
        glVertex2f((x + x0), (y + y0))
        glVertex2f((y+x0),(x+y0))
        glVertex2f((-x+x0),(-y+y0))
        glVertex2f((-y+x0),(-x+y0))
        glVertex2f((-x+x0),(y+y0))
        glVertex2f((y+x0),(-x+y0))
        glVertex2f((x+x0),(-y+y0))
        glVertex2f((-y+x0),(x+y0))
        glEnd()
        """
        lst.extend([((-y+x0),(x+y0)),((x+x0),(-y+y0)),((x + x0), (y + y0)),((y+x0),(x+y0)),((-x+x0),(-y+y0)),((-y+x0),(-x+y0)),((-x+x0),(y+y0)),((y+x0),(-x+y0))])
        if (d<0):
            d += 2*x+3
        else:
            d+= 2*x - 2*y + 5
            y-=1
        x+=1
    return lst

