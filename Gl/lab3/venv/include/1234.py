from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys

# const
left_up_front = [-8, 0, 1]
start_front = [8, 0, 1]

right_up_front = start_front
start_back = [8, 0, -1]

right_up_back = start_back

fin_front = [-2, 0, 9]
fin_back = [0, 0, 9]

def set():
    global up
    global front
    global down
    global back
    global left
    global right
    left_up_back = [left_up_front[0], left_up_front[1], left_up_front[2] - 2]
    left_up_middle = [left_up_front[0], left_up_front[1], left_up_front[2] - 1]
    right_up_middle = [right_up_front[0]-(right_up_front[0] - right_up_back[0]) / 2,
                       left_up_front[1],
                       right_up_front[2]-(right_up_front[2] - right_up_back[2]) / 2]
    middle_up_back = [0, left_up_front[1], left_up_back[2]]
    middle_up_middle = [-1, left_up_front[1], left_up_middle[2]]
    middle_up_front = [-2, left_up_front[1], left_up_front[2]]
    left_middle_front = [left_up_front[0], left_up_front[1] - 1, left_up_front[2]]  # check 2 was 1
    middle_middle_front = [middle_up_front[0], left_middle_front[1], left_middle_front[2]]
    right_middle_front = [right_up_front[0], left_middle_front[1], right_up_front[2]]

    left_down_front = [left_up_front[0], left_up_front[1] - 2, left_up_front[2]]
    middle_down_front = [middle_up_front[0], left_down_front[1], left_down_front[2]]
    right_down_front = [right_up_front[0], left_down_front[1], right_up_front[2]]

    left_down_middle = [left_up_front[0], left_down_front[1], left_up_middle[2]]
    middle_down_middle = [middle_up_middle[0], left_down_middle[1], left_down_middle[2]]
    right_down_middle = [right_up_middle[0], left_down_middle[1], right_up_middle[2]]

    left_down_back = [left_up_front[0], left_down_front[1], left_up_back[2]]
    middle_down_back = [middle_up_back[0], left_down_back[1], left_down_back[2]]
    right_down_back = [right_up_back[0], left_down_back[1], right_up_back[2]]

    left_middle_back = [left_up_front[0], left_middle_front[1], left_up_back[2]]
    middle_middle_back = [middle_up_back[0], left_middle_front[1], left_up_back[2]]
    right_middle_back = [right_up_back[0], left_middle_front[1], right_up_back[2]]

    left_middle_left = [left_up_front[0], left_middle_front[1], left_up_middle[2]]

    right_middle_right = [right_up_middle[0], left_middle_front[1], right_up_front[2]]


    up = [[left_up_front,
           middle_up_front,
           right_up_front],
          [left_up_middle,
           middle_up_middle,
           right_up_middle],
          [left_up_back,
           middle_up_back,
           right_up_back]]

    front = [[left_up_front,
              middle_up_front,
              right_up_front],
             [left_middle_front,
              middle_middle_front,
              right_middle_front],
             [left_down_front,
              middle_down_front,
              right_down_front]]

    down = [[left_down_front,
             middle_down_front,
             right_down_front],
            [left_down_middle,
             middle_down_middle,
             right_down_middle],
            [left_down_back,
             middle_down_back,
             right_down_back]]
    back = [[left_up_back,
             middle_up_back,
             right_up_back],
            [left_middle_back,
             middle_middle_back,
             right_middle_back],
            [left_down_back,
             middle_down_back,
             right_down_back]]

    left = [[left_down_front, left_down_middle, left_down_back],
            [left_middle_front, left_middle_left, left_middle_back],
            [left_up_front, left_up_middle, left_up_back]]

    right = [[right_down_front, right_down_middle, right_down_back],
             [right_middle_front, right_middle_right, right_middle_back],
             [right_up_front, right_up_middle, right_up_back]]


# cp =[[[-0.75,-0.75,-0.5],
#       [-0.25,-0.75,0],
#       [0.25,-0.75,0]],
#      [[0.75,-0.75,-0.5],
#      [-0.75,-0.25,-0.5],
#       [0.75,-0.25,-0.5]],
#      [[-0.75,0.25,-0.5],
#       [0.75,0.25,-0.5],
#       [-0.75,0.75,-0.5]],
#      [[-0.25,0.75,0.75],
#       [0.25,0.75,0.75],
#       [0.75,0.75,-0.5]]]
up = []
front = []
down = []
back = []
left = []
right = []





def drawP(cp, np):
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in range(np):
        for j in range(3):
            if j != 1:
                glVertex3fv(cp[i][j])
    glEnd()


angle = 0.01

def render():
    global angle
    global right_up_back
    global fin_back
    global start_back
    global fin_front
    global start_front
    global fin_front
    global right_up_front
    set()
    z = -20
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # glRotate(angle,0,0,1)
    glTranslate(0, 0, z)
    glPushMatrix()
    # glRotate(45,0,1,0)
    glEnable(GL_MAP2_VERTEX_3)
    glRotate(90, 1, 0, 0)

    glMap2f(GL_MAP2_VERTEX_3, 0, 10, 0, 10, up)
    glMapGrid2f(10, 0, 10, 10, 0, 10)
    glEvalMesh2(GL_LINE, 0, 10, 0, 10)
    drawP(up, 3)

    glMap2f(GL_MAP2_VERTEX_3, 0, 10, 0, 10, front)
    glEvalMesh2(GL_LINE, 0, 10, 0, 10)
    drawP(front, 3)

    glMap2f(GL_MAP2_VERTEX_3, 0, 10, 0, 10, down)
    glEvalMesh2(GL_LINE, 0, 10, 0, 10)
    drawP(down, 3)

    glMap2f(GL_MAP2_VERTEX_3, 0, 10, 0, 10, back)
    glEvalMesh2(GL_LINE, 0, 10, 0, 10)
    drawP(back, 3)

    glMap2f(GL_MAP2_VERTEX_3, 0, 10, 0, 10, left)
    glEvalMesh2(GL_LINE, 0, 10, 0, 10)
    drawP(left, 2)

    glMap2f(GL_MAP2_VERTEX_3, 0, 10, 0, 10, right)
    glEvalMesh2(GL_LINE, 0, 10, 0, 10)
    drawP(right, 2)

    glPopMatrix()
    glutSwapBuffers()
    #0, left_up_front[1], 6
    right_up_back =[start_back[0]*(1-angle)+fin_back[0]*angle, start_back[1]*(1-angle)+fin_back[1]*angle, start_back[2]*(1-angle)+fin_back[2]*angle]
    right_up_front =[start_front[0]*(1-angle)+fin_front[0]*angle, start_front[1]*(1-angle)+fin_front[1]*angle, start_front[2]*(1-angle)+fin_front[2]*angle]

    if angle <1:
        angle +=0.01




def my_init():
    glClearColor(0, 0, 0, 0)


def timer(value):
    glutPostRedisplay()
    glutTimerFunc(15, timer, 0)


def resize(width, height):
    ar = width / height

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-ar, ar, -1.0, 1.0, 2.0, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw():
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(0, 0, -6)


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow("1")
glutDisplayFunc(render)
glutReshapeFunc(resize)
glClearColor(1, 1, 1, 1)
glutTimerFunc(0, timer, 0)

glEnable(GL_NORMALIZE)
glEnable(GL_RESCALE_NORMAL)
my_init()

glutMainLoop()
