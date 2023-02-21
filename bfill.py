import numpy as np
import sys
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

windowsize=800
pointsize=5
sys.setrecursionlimit(1000000)
boundary=[1,0,0]

def Clearscreen():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(0,windowsize,0,windowsize)

def getpixel(x,y):
    pixel = glReadPixels(x,windowsize-y, 1, 1, GL_RGB, GL_FLOAT)
    return np.array([round(x, 1) for x in pixel[0][0]])

def setpixel(x,y,fill_color=(0,0,0)):
    glPointSize(pointsize+4)
    glColor3f(*fill_color)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()

def plotrectangle():
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glLineWidth(pointsize)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(10,10)
    glVertex2f(10+windowsize/2,10)
    glVertex2f(10+windowsize/2,10+windowsize/2)
    glEnd()
    glFlush()

def boundaryfill(x, y, fillcolor, boundarycolor):
    color=getpixel(x,y)
    if not (all(color == fillcolor)) and not all (color == boundarycolor):
        setpixel(x,y,fillcolor)
        boundaryfill(x + pointsize, y, fillcolor, boundarycolor)
        boundaryfill(x, y + pointsize, fillcolor, boundarycolor)
        boundaryfill(x - pointsize, y, fillcolor, boundarycolor)
        boundaryfill(x, y - pointsize, fillcolor, boundarycolor)


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        boundaryfill(x, y, [0, 1, 0], boundary)


def main():
    glutInit()
    glutCreateWindow("Boundary Fill")
    glutInitWindowSize(700,700)
    glutDisplayFunc(plotrectangle)
    glutMouseFunc(mouse_click)
    Clearscreen()
    glutMainLoop()

main()