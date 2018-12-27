from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global xrot
global yrot
global radius
global height


def init():
    global xrot
    global yrot
    global radius
    global height

    xrot = 0.0
    yrot = 0.0
    radius = 3 ** 0.5
    height = 2


def resize(width, height):
    ar = width / height

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-ar, ar, -1.0, 1.0, 2.0, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


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


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    glTranslated(0.0, -2, -10)
    glRotatef(-90, 1, 0, 0)
    glRotatef(yrot, 1, 0, 0)
    glRotatef(xrot, 0, 1, 0)
    glColor3d(0, 0, 0)
    glutWireCone(1,2,10,10)

    glTranslated(3, 0, 0)
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
