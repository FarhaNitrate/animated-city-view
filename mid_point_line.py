from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def dezone(x, y, zone):
  if zone == 0:
    return x, y
  elif zone == 1:
    return y , x
  elif zone == 2:
    return -y , x
  elif zone == 3:
    return -x , y
  elif zone == 4:
    return -x, -y
  elif zone == 5:
    return -y , -x
  elif zone == 6:
    return y , -x
  elif zone == 7:
    return x , -y
  else:
    print("problem")
    return x , y

def zone_fnc(x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2 - y1
  if abs(dx) >= abs(dy) and (dx >= 0 and dy >= 0):
    zone = 0
    return x1, y1, x2, y2, zone
  elif abs(dy) > abs(dx) and (dx >= 0 and dy >= 0):
    zone = 1
    return y1, x1, y2, x2, zone
  elif abs(dy) > abs(dx) and (dx < 0 and dy >= 0):
    zone = 2
    return y1, -x1, y2, -x2, zone
  elif abs(dx) >= abs(dy) and (dx < 0 and dy >= 0):
    zone = 3
    return -x1, y1, -x2, y2, zone
  elif abs(dx) >= abs(dy) and (dx < 0 and dy < 0):
    zone = 4
    return -x1, -y1, -x2, -y2, zone
  elif abs(dy) > abs(dx) and (dx < 0 and dy < 0):
    zone = 5
    return -y1, -x1, -y2, -x2, zone
  elif abs(dy) > abs(dx) and (dx >= 0 and dy < 0):
    zone = 6
    return -y1, x1, -y2, x2, zone
  elif abs(dx) >= abs(dy) and (dx >= 0 and dy < 0):
    zone = 7
    return x1, -y1, x2, -y2, zone

def mid_line(x1, y1, x2, y2):
    lst = []
    zone = 0
    x1 , y1 , x2, y2, zone = zone_fnc(x1, y1, x2, y2)
    dx = x2 - x1
    dy = y2 - y1
    d = 2*dy - dx
    incE = 2*dy
    incNE = 2*(dy-dx)
    y = y1
    x = x1
    #glBegin(GL_POINTS)
    while (x<=x2):
        x_t , y_t = dezone(x , y , zone)
        #glVertex2f(x_t,y_t)
        lst.append((x_t, y_t))
        if (d>0):
            y += 1
            d += incNE
        else:
            d += incE
        x += 1
    #glEnd()
    return lst
