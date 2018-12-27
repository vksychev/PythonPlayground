from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global radius
global height
global push

def init():
    global radius
    global height
    global push

    push = [0,0,0]
    radius = 0.4
    height = 2
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glRotatef(-90, 1.0, 0.0, 0.0)


def resize(width, height):
    ar = width / height

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-ar, ar, -1.0, 1.0, 2.0, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def specialkeys(key, x, y):
    global push
    global height
    if key == GLUT_KEY_UP:
        height *= 2
    if key == GLUT_KEY_DOWN:
        height /= 2
    if key == GLUT_KEY_RIGHT:
        push = [height,0,0]
    if key == GLUT_KEY_LEFT:
        push = [0,0,0]
    glutPostRedisplay()


def draw():
    global push
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()

    glTranslated(0.0, 0, -8)
    glRotatef(30, 1, 0, 0)
    glRotatef(30, 0, 1, 0)
    glColor3d(1, 0, 1)
    glutWireCube(height)
    glTranslated(-height / 2, height / 2, height / 2)
    glTranslated(push[0], push[1], push[2])

    glColor3d(0, 0, 0)
    glutWireSphere(radius, 32, 32)

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
