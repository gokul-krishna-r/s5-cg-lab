from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE=500
CONSTX=[-50,50,0]
CONSTY=[-50,-50,40]
POSX=0
POSY=0
radX=-300
radY=0
THETA=0

def init():
   gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
   glClearColor(1,1,1,1)

def drawBall(x,y):
   glClear(GL_COLOR_BUFFER_BIT)
   glPointSize(5)
   glColor3f(1,0,0)
   glBegin(GL_LINES)
   
   for i in range(0,361):
      x=50*math.cos(math.radians(i))
      y=50*math.sin(math.radians(i))
      glVertex2f(0+radX,0+radY)
      glVertex2f(x+radX,y+radY)
   glEnd()
   glFlush()
   glutSwapBuffers()

def animate(value):
   glutPostRedisplay()
   global THETA
   global POSX
   global POSY
   global radX,radY
   THETA+=3
   radX+=3
   radY=80*math.sin(math.radians(THETA))
   if(radX>(WINDOW_SIZE-50)):
      radX=-500
   glutTimerFunc(int(1000/60),animate,0)
   if(THETA>180):
      THETA=0

   

def main():
   global POSX,POSY
   glutInit(sys.argv)
   glutInitWindowPosition(0,0)
   glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
   glutInitDisplayMode(GLUT_RGB)
   glutCreateWindow("Hello")
   glutTimerFunc(0,animate,0)
   glutDisplayFunc(lambda:drawBall(POSX,POSY))
   init()
   glutMainLoop()
main()