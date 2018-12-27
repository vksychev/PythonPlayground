from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys
import pygame
from ansible.modules.network.panos._panos_nat_policy import add_nat

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
v = 1
animateDown = False
a = 0
angle = 0
anglePyramid = 0.0
angleDown = 0.0
angleDown_2 = 0
s = sqrt(2)
ss = 0
sss = 0
xrot = 0
yrot = 0
def draw():
    global dy
    global xrot
    global yrot
    global z
    global a
    global v
    global anglePyramid
    global angleDown
    global angleDown_2
    global angle
    global s
    global ss
    global sss
    global animateDown
    id = loadTexture("1.png")
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(0, 0, -10)


    glEnable(GL_TEXTURE_2D)
    quadratic = gluNewQuadric()
    gluQuadricNormals(quadratic, GLU_SMOOTH)
    gluQuadricTexture(quadratic, GL_TRUE)
    #glRotate(90, 0, 1, 0)
    glRotate(xrot, 0, 1, 0)
    glRotate(-yrot, 1, 0, 0)
    glTranslatef(0, -16, 0)
    glutSolidCube(32)
    glTranslatef(0, 16, 0)
    glRotate(-90, 1, 0, 0)
    glTranslatef(0.5 - 0.5 * cos(radians(angle)), 0, 0.5 * sin(radians(angle)))
    glRotate(angle, 0, 1, 0)
    gluCylinder(quadratic, 0.5, 0.5, 2, 16, 6)
    glRotate(-angle, 0, 1, 0)
    glTranslatef(-0.5 + 0.5 * cos(radians(angle)), 0, -0.5 * sin(radians(angle)))
    glRotate(90, 1, 0, 0)

    glTranslatef(-1.45, 0, 0)
    glTranslatef(1 - cos(radians(anglePyramid)), sin(radians(anglePyramid)), 0)
    if angle > 90:
        glTranslatef(0, sqrt(1/3)*sin(radians(angleDown*2)), -1 + s*cos(radians(angleDown+45))-sss)
    if angleDown >= 90:
        glTranslatef(0, 0, -ss)

    glRotate(-anglePyramid, 0, 0, 1)
    glRotate(-angleDown, 0, 1, 0)
    glRotate(-angleDown_2, 1, 0, 0)

    glBegin(GL_TRIANGLES)

    # bot 1
    glTexCoord2f(0, 0)
    # d
    glVertex3f(-1, 0, -1)
    glTexCoord2f(1, 0)
    glVertex3f(1, 0, -1)
    glTexCoord2f(0, 1)
    # d
    glVertex3f(-1, 0, 1)

    # bot 2

    glTexCoord2f(1, 0)
    glVertex3f(1, 0, -1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 0, 1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 0, 1)

    # back

    glTexCoord2f(0, 0)
    # d
    glVertex3f(-1, 0, -1)
    glTexCoord2f(1, 0)
    glVertex3f(1, 0, -1)
    glTexCoord2f(0, 1)
    # d
    glVertex3f(0, 2, 0)

    # left
    glTexCoord2f(0, 0)
    # d

    glVertex3f(-1, 0, -1)
    glTexCoord2f(1, 0)
    # d

    glVertex3f(-1, 0, 1)
    glTexCoord2f(0, 1)
    # d
    glVertex3f(0, 2, 0)

    # right

    glTexCoord2f(0, 0)
    glVertex3f(1, 0, -1)
    glTexCoord2f(1, 0)
    glVertex3f(1, 0, 1)
    glTexCoord2f(0, 1)
    # d
    glVertex3f(0, 2, 0)

    # front

    glTexCoord2f(0, 0)
    # d

    glVertex3f(-1, 0, 1)
    glTexCoord2f(1, 0)
    glVertex3f(1, 0, 1)
    glTexCoord2f(0, 1)
    # d

    glVertex3f(0, 2, 0)

    glEnd()
    glTranslatef(-1 + cos(radians(anglePyramid)), -sin(radians(anglePyramid)), 0)
    glRotate(anglePyramid, 0, 0, 1)
    glDisable(GL_TEXTURE_2D)

    glutSwapBuffers()

    if anglePyramid >= degrees(atan(1 / 2)):
        animateDown = True

    if degrees(atan(1 / 2)) > anglePyramid:
        anglePyramid += 3

    if animateDown:
        if angle > 90:
            if angleDown_2 < 45:
                angleDown_2 = angleDown_2+1/2
            if angleDown < 90:
                angleDown = angleDown+1
                v = 0.1
                sss += 0.025
            else:
                v = v - 0.1*v
                ss += v

        else:
            if anglePyramid < 90 + degrees(atan(1 / 2)) - 45:
                anglePyramid = degrees(atan(1 / 2))+ angle
            angle = angle + v

            v = 1.05*v

    a +=0.5


def timer(value):
    global refreshMills
    glutPostRedisplay()
    glutTimerFunc(refreshMills, timer, 0)

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
glutDisplayFunc(draw)
glutReshapeFunc(resize)
glClearColor(1, 1, 1, 1)
glutTimerFunc(0, timer, 0)
glutSpecialFunc(specialkeys)

glEnable(GL_NORMALIZE)
glEnable(GL_RESCALE_NORMAL)
my_init()

glutMainLoop()
