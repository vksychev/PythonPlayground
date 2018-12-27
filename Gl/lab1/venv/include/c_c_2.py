from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global xrot
global yrot
global radius
global height
global s_x
global s_y
global step
def init():
    global xrot
    global yrot
    global radius
    global height
    global s_x
    global s_y
    global step
    step = 0
    s_x = 0
    s_y = 0
    xrot = 0.0
    yrot = 0.0
    radius = 3 ** 0.5
    height = 2


def resize(width, height):
    ar = width / height

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-ar, ar, -1.0, 1.0, 2.0, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def specialkeys(key, x, y):
    global xrot
    global yrot
    global s_x
    global s_y
    global step

    steps = 20
    dy = (3-2) / steps
    dx = 3/steps
    if key == GLUT_KEY_UP:
        yrot -= 2.0
    if key == GLUT_KEY_DOWN:
        yrot += 2.0
    if key == GLUT_KEY_LEFT:
        xrot -= 2.0
    if key == GLUT_KEY_RIGHT:
        xrot += 2.0
    if key == GLUT_KEY_F1:
        if step < steps:
            s_x += dx
            s_y += dy
            step += 1
    glutPostRedisplay()


def draw():
    global s_x
    global s_y
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    glTranslated(-1, -2, -1)
    glRotatef(-90, 1, 0, 0)
    glRotatef(yrot, 1, 0, 0)
    glRotatef(xrot, 0, 1, 0)
    glColor3d(0, 0, 0)

    glutWireCone(1,3,10,10)

    glTranslated(3-s_x, 0, 0+s_y)
    glColor3d(1, 0, 1)

    glutWireCylinder(1,4,10,10)

    glPopMatrix()
    glutSwapBuffers()


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow("1")
glutDisplayFunc(draw)
glutReshapeFunc(resize)
glClearColor(1, 1, 1, 1)
glutSpecialFunc(specialkeys)
init()
glutMainLoop()
