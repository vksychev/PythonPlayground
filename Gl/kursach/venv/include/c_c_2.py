from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys
import pygame
from ansible.modules.network.panos._panos_nat_policy import add_nat

anglePyramid = 0.0
refreshMills = 15
mills = 0


def resize(width, height):
    ar = width / height

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-ar, ar, -1.0, 1.0, 2.0, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def my_init():
    global light_position
    global down

    light_position = [0, 0, 11, 0.0]
    glClearColor(0, 0, 0, 0)

    glEnable(GL_COLOR_MATERIAL)

    down = True


def loadTexture(name):
    textureSurface = pygame.image.load(name)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid


R = 2.1
g = 9.8 / 100000
dy = 0
v = 0
vx = 0.01
dawn = False
x = 0.8
a = 0

def draw():
    global dy
    global v
    global anglePyramid
    global dawn
    global x
    global vx
    global a
    id = loadTexture("4.png")
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, -1, -10.0)
    glEnable(GL_TEXTURE_2D)

    #glRotate(anglePyramid, 1, 1, 0)
    quadratic = gluNewQuadric()
    gluQuadricNormals(quadratic, GLU_SMOOTH)
    gluQuadricTexture(quadratic, GL_TRUE)
    glBegin(GL_TRIANGLES)

    glTexCoord2f(0, 0)
    glVertex3f(-1, 0, -1)
    glTexCoord2f(1, 0)
    glVertex3f(1, 0, -1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 0, 1)

    glTexCoord2f(1, 0)
    glVertex3f(1, 0, -1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 0, 1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 0, 1)

    glTexCoord2f(0, 0)
    glVertex3f(-1, 0, 1)
    glTexCoord2f(1, 0)
    glVertex3f(-1, 0, -1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 2, 1)

    glTexCoord2f(1, 0)
    glVertex3f(-1, 0, -1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 2, -1)
    glTexCoord2f(1, 1)
    glVertex3f(-1, 2, 1)

    glTexCoord2f(0, 0)
    glVertex3f(-1, 0, -1)

    glTexCoord2f(1, 0)
    glVertex3f(-1, 2, -1)

    glTexCoord2f(0, 1)
    glVertex3f(1, 0, -1)

    glTexCoord2f(1, 0)
    glVertex3f(-1, 2, -1)
    glTexCoord2f(0, 1)
    glVertex3f(1, 0, -1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 2, -1)

    glTexCoord2f(0, 0)
    glVertex3f(1, 2, -1)
    glTexCoord2f(1, 0)
    glVertex3f(1, 2, 1)
    glTexCoord2f(0, 1)
    glVertex3f(1, 0, -1)

    glTexCoord2f(1, 0)
    glVertex3f(1, 0, 1)
    glTexCoord2f(0, 1)
    glVertex3f(1, 2, 1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 0, -1)

    glTexCoord2f(0, 0)
    glVertex3f(-1, 0, 1)
    glTexCoord2f(1, 0)
    glVertex3f(-1, 2, 1)
    glTexCoord2f(0, 1)
    glVertex3f(1, 0, 1)

    glTexCoord2f(1, 0)
    glVertex3f(-1, 2, 1)
    glTexCoord2f(0, 1)
    glVertex3f(1, 0, 1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 2, 1)

    glTexCoord2f(0, 0)
    glVertex3f(-1, 2, -1)
    glTexCoord2f(1, 0)
    glVertex3f(1, 2, -1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 2, 1)

    glTexCoord2f(1, 0)
    glVertex3f(1, 2, -1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 2, 1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 2, 1)
    glEnd()

    glTranslate(-1+x, 2.95-dy, -1)
    x+=vx
    glRotate(degrees(atan(1 / 3)), 1, 0, 0)
    glRotate(-a, 0, 0, 1)
    gluCylinder(quadratic, 1, 0, 3, 16, 6)
    glRotate(a, 0, 0, 1)
    glRotate(-degrees(atan(1 / 3)), 1, 0, 0)

    glDisable(GL_TEXTURE_2D)

    glutSwapBuffers()
    anglePyramid += 1
    a+=1
    if dawn:
        v += g * 15
        dy += v
    if -1+x >= 1.2:
        anglePyramid = anglePyramid % 360
        dawn = True


def timer(value):
    global refreshMills
    glutPostRedisplay()
    glutTimerFunc(refreshMills, timer, 0)


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow("1")
glutDisplayFunc(draw)
glutReshapeFunc(resize)
glClearColor(1, 1, 1, 1)
glutTimerFunc(0, timer, 0)
glEnable(GL_NORMALIZE)
glEnable(GL_RESCALE_NORMAL)
my_init()

glutMainLoop()
