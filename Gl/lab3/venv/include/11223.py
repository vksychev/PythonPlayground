from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys

left_up_front = [0, 0, 1]
middle_up_front = [4, 0, 1]
right_up_front = [8, 0, 1]

left_up_middle = [0, 0, 0]
middle_up_middle = [4, 0, 0]
right_up_middle = [8, 0, 0]

left_up_back = [0, 0, -1]
middle_up_back = [4, 0, -1]
right_up_back = [8, 0, -1]

left_up_front_2 = [0, 0, 1]
middle_up_front_2 = [4, 0, 1]
right_up_front_2 = [8, 0, 1]

left_up_middle_2 = [0, 0, 0]
middle_up_middle_2 = [4, 0, 0]
right_up_middle_2 = [8, 0, 0]

left_up_back_2 = [0, 0, -1]
middle_up_back_2 = [4, 0, -1]
right_up_back_2 = [8, 0, -1]

# left_up_front = [0, 0, 1]
# middle_up_front = [0, -4, 4]
# right_up_front = [0, -8, 1]
#
# left_up_middle = [2, 0, 0]
# middle_up_middle = [8, -4, 0]
# right_up_middle = [2, -8, 0]
#
# left_up_back = [0, 0, -1]
# middle_up_back = [0, -4, -4]
# right_up_back = [0, -8, -1]


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


def set():
    global up
    global front
    global down
    global back
    global left
    global right
    up = [[left_up_front,
           middle_up_front,
           right_up_front],
          [left_up_middle,
           middle_up_middle,
           right_up_middle],
          [left_up_back,
           middle_up_back,
           right_up_back]]

    down = [[left_up_front_2,
             middle_up_front_2,
             right_up_front_2],
            [left_up_middle_2,
             middle_up_middle_2,
             right_up_middle_2],
            [left_up_back_2,
             middle_up_back_2,
             right_up_back_2]]


def drawP(cp, np):
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in range(np):
        for j in range(3):
            if j != 1:
                glVertex3fv(cp[i][j])
    glEnd()


angle = 0
xrot = 0
yrot = 0
step = 0.002
steps = 0
step1 = False


def render():
    global xrot
    global yrot
    global angle
    global step
    global steps
    global step1
    set()
    z = -30
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    if not step1:
        for line in up:
            line[1][0] = 4 * cos(radians(angle))
            line[1][1] = -4 * sin(radians(angle))
            line[2][0] = 8 * cos(radians(angle))
            line[2][1] = -8 * sin(radians(angle))

        for line in down:
            line[1][0] = 4 * cos(radians(angle * 3))
            line[1][1] = 4 * sin(radians(angle * 3))
            line[2][0] = 8 * cos(radians(angle * 3))
            line[2][1] = 8 * sin(radians(angle * 3))

    elif (step * steps < 1):

        up[0][1][2] += (step * 6)
        up[1][0][0] += (step * 2)
        up[1][1][0] += (step * 12)
        up[1][2][0] += (step * 2)
        up[2][1][2] -= (step * 6)



        down[0][1][2] += (step * 6)
        down[1][0][0] -= (step * 2)
        down[1][1][0] -= (step * 12)
        down[1][2][0] -= (step * 2)
        down[2][1][2] -= (step * 6)
        steps += 1


    # glRotate(angle,0,0,1)
    glTranslate(0, 0, z)
    glPushMatrix()
    # glRotate(45,0,1,0)
    glEnable(GL_MAP2_VERTEX_3)
    glRotate(xrot, 0, 1, 0)
    glRotate(-yrot, 1, 0, 0)

    glMap2f(GL_MAP2_VERTEX_3, 0, 10, 0, 10, up)
    glMapGrid2f(10, 0, 10, 10, 0, 10)
    glEvalMesh2(GL_LINE, 0, 10, 0, 10)
    drawP(up, 3)

    glMap2f(GL_MAP2_VERTEX_3, 0, 10, 0, 10, down)
    glMapGrid2f(10, 0, 10, 10, 0, 10)
    glEvalMesh2(GL_LINE, 0, 10, 0, 10)
    drawP(down, 3)

    glPopMatrix()
    glutSwapBuffers()
    if (angle >= 90):
        step1 = True
    else:
        angle += 0.5


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


def specialkeys(key, x, y):
    global xrot
    global yrot

    if key == GLUT_KEY_UP:
        yrot -= 2.0
    if key == GLUT_KEY_DOWN:
        yrot += 2.0
    if key == GLUT_KEY_LEFT:
        xrot -= 2.0
    if key == GLUT_KEY_RIGHT:
        xrot += 2.0

    glutPostRedisplay()


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow("1")
glutDisplayFunc(render)
glutReshapeFunc(resize)
glClearColor(1, 1, 1, 1)
glutTimerFunc(0, timer, 0)
glutSpecialFunc(specialkeys)

glEnable(GL_NORMALIZE)
glEnable(GL_RESCALE_NORMAL)
my_init()

glutMainLoop()
