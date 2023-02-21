from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE=500
CONSTX=[-50,50,0]
CONSTY=[-50,-50,40]
POSX=[0,0,0]
POSY=[0,0,0]
radX=0
radY=0
THETA=0

def init():
   gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
   glClearColor(1,1,1,1)

def drawTriangle(x,y):
   glClear(GL_COLOR_BUFFER_BIT)
   glPointSize(5)
   glColor3f(1,0,0)
   glBegin(GL_POLYGON)
   for i in range(0,3):
      glVertex2f(POSX[i]+radX,POSY[i]+radY)
   glEnd()
   glFlush()
   glutSwapBuffers()

def animate(value):
   glutPostRedisplay()
   global THETA
   global POSX
   global POSY
   global radX,radY
   THETA+=1
   radX=200*math.cos(math.radians(THETA))
   radY=200*math.sin(math.radians(THETA))
   for i in range(0,3):
      POSX[i]=(CONSTX[i]*math.cos(math.radians(THETA)))-(CONSTY[i]*math.sin(math.radians(THETA)))
      POSY[i]=(CONSTY[i]*math.cos(math.radians(THETA)))+(CONSTX[i]*math.sin(math.radians(THETA)))
   glutTimerFunc(int(1000/60),animate,0)
   if(THETA>360):
      THETA=0

   

def main():
   global POSX,POSY
   glutInit(sys.argv)
   glutInitWindowPosition(0,0)
   glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
   glutInitDisplayMode(GLUT_RGB)
   glutCreateWindow("Hello")
   glutTimerFunc(0,animate,0)
   glutDisplayFunc(lambda:drawTriangle(POSX,POSY))
   init()
   glutMainLoop()
main()