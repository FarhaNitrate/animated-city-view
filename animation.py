from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from car_object import *
from traffic_light import *
import random
from backgroud_object import *

WIDTH = 800
HEIGHT = 600
p = -WIDTH//2 +50
q = HEIGHT//2 -50
r = 10
a = create_car(body_size=100,x0 = 200, y0=-250, curr_s = -3 * random.uniform(0.8,1.0), accelaration=0.03)
car_gap = 50
count = 0
need_car = 0
car_lst = [a]
new_car = a
num = []
sun_points = []
sun_counter = 0
moon_points, moon_counter = [], 0
day_night = input("'d' for Daytime\n'n' for Night time\n:").strip()[0]
change = int(input("Auto change Lights?\n1:No\n2:Yes\n:"))-1
state = int(input("Input state of traffic light\n1: Green\n2: Yellow\n3: Red\n:"))
b = traffic_light(x0 = -350, y0 = -150, delay=100, change = change)
b.state = state
if b.state == 2:
    b.next_state = 1
else:
    b.next_state = 2

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-WIDTH//2, WIDTH//2, -HEIGHT//2, HEIGHT//2, 0.0, 1)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    global p , q, r , a , count, num, sun_points, sun_counter, moon_points, moon_counter, day_night

    if day_night == "n":
        glClearColor(71/255, 89/255, 112/255, 0)
        
    else:
        glClearColor(110/255, 103/255, 5/255, 0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    if day_night == "n":
        moon_points, moon_counter = moon(-200,200, points = moon_points, t = 0.01, moon_counter = moon_counter)
    else:
        sun_points , sun_counter = sun(200, 200, points = sun_points, t = 0.01, sun_counter = sun_counter)

    num = building_row(800, points=num)
    draw_road(800, w = 50)
    #glPointSize(1)
    #num_display_2("662", start = 0, size = 20, gap = 20)
    glColor3f(1, 1, 1)
    #circle_design1(0,0 , 300, num = 300)

    global b , car_gap
    if b.state == 2:
        if b.next_state == 1:
            for car in car_lst:
                car.accelarate()
        elif b.next_state == 3:
            for car in car_lst:
                if car.x0 > b.x0 + 2*car_gap:
                    car.deacclerate()
    
    elif b.state == 3:
        for car in car_lst:
            if car.x0 > b.x0 + 2*car_gap:
                car.curr_s = 0

    if count == b.delay:
        count = 0
        b.state_change()
    b.draw()
    count +=1

    global new_car, WIDTH
    if (new_car.x0 < WIDTH/2 - car_gap *3 ) and len(car_lst) < 11:
        new_car = create_car(body_size=100, x0 = 400, y0=-250, curr_s = -3 * random.uniform(0.8,1.0),accelaration=0.03)
        car_lst.append(new_car)

    del_target = None
    #print(len(car_lst))
    for car in car_lst:
        if not (car.x0 < -WIDTH/2 - car.body_size - car_gap):
            car.move()
            car.draw()
        else:
            del_target = car

    if del_target!= None:
        car_lst.remove(del_target)


    glutPostRedisplay()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(WIDTH, HEIGHT) #window size
glutInitWindowPosition(0,0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutMainLoop()