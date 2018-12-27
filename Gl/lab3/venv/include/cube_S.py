from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys

anglePyramid = 0.0
refreshMills = 15
mills = 0


def my_init():
    glClearColor(0, 0, 0, 0)


def resize(width, height):
    ar = width / height

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-ar, ar, -1.0, 1.0, 2.0, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


up = True
step = 0


def draw():
    global mills
    global z
    global dz
    global anglePyramid
    global refreshMills
    global step
    global up
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0.0, -6.0)
    glRotatef(anglePyramid, 0.0, 1.0, 1.0)
    R = 1
    glRotatef(-90, 1.0, 0.0, 0.0)

    glBegin(GL_TRIANGLES)

    sb = 10
    sl = 10
    blue = 0.1
    green = 0.1
    red = 0.1

    glColor3f(red, green, blue)

    for b in range(-90, 90, sb):

        bl = radians(b)
        bb = radians(b + sb)
        for l in range(0, 361, sl):
            ll = radians(l)
            lz = R * sin(bl)
            bz = R * sin(bb)

            if mills > 50000:
                if b > 0:
                    nl = R*(b/90)**4
                    nz = R*((b+sb)/90)**4
                    kz=lz+ step*nl /100000
                    bbz = bz + step*nz /100000
                    if up:
                        step += 1
                    else:
                        step -= 1

                    if step <= 0:
                        up = True
                    if kz < lz + nl:
                        lz = kz
                        bz = bbz


                    else:
                        lz += R*(b/90)**4
                        bz += R*((b+sb)/90)**4
                        up = False

            else:
                mills += 1

            glVertex3f(R * cos(bl) * sin(ll), R * cos(bl) * cos(ll), lz)
            glVertex3f(R * cos(bb) * sin(ll), R * cos(bb) * cos(ll), bz)
            ll = radians(l + sl)
            glVertex3f(R * cos(bb) * sin(ll), R * cos(bb) * cos(ll), bz)
            ll = radians(l)

            glVertex3f(R * cos(bl) * sin(ll), R * cos(bl) * cos(ll), lz)
            ll = radians(l + sl)
            glVertex3f(R * cos(bl) * sin(ll), R * cos(bl) * cos(ll), lz)
            glVertex3f(R * cos(bb) * sin(ll), R * cos(bb) * cos(ll), bz)
        red += 0.15
        if red >= 1:
            blue += 0.15
        if blue >= 1:
            green +=0.15
        glColor3f(red, green, blue)

    glEnd()

    glutSwapBuffers()
    anglePyramid += 0.4


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
