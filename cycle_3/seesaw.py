from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import numpy as py
sys.setrecursionlimit(10**6) 

WINDOW_SIZE=500

ROTATEX,ROTATEY=0,0
theta=0
dir=0


def init():
   gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
   glClearColor(1,1,1,1)


def drawTriangle():
   glBegin(GL_POLYGON)
   glVertex2f(-50,-50)
   glVertex2f(50,-50)
   glVertex2f(0,25)
   glEnd()
def drawLine():
   global ROTATEX,ROTATEY,ENDX,ENDY
   glLineWidth(10)
   glBegin(GL_LINES)
   glVertex2f(ROTATEX,25+ROTATEY)
   glVertex2f(-ROTATEX,25-ROTATEY)
   glEnd()
def drawScene():
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(1,0,0)
   drawTriangle()
   drawLine()
   glutSwapBuffers()

def animate(temp):
   glutPostRedisplay()
   glutTimerFunc(int(1000/60),animate,int(0))
   global theta,ROTATEX,ROTATEY,dir

   ROTATEX=200*math.cos(math.radians(theta))
   ROTATEY=200*math.sin(math.radians(theta))
   if(dir==0):
      theta+=1
      if(theta>30):
         dir=1
   elif(dir==1):
      theta-=1
      if(theta<-30):
         dir=0
   elif(dir==2):
      theta=0
  

   

def keyboard(key,x,y):
   key=key.decode()
   global dir
   if(key=="s"):
      dir=2
   elif(key=="w"):
      dir=0


def main():
   glutInit(sys.argv)
   glutInitWindowPosition(0,0)
   glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
   glutInitDisplayMode(GLUT_RGB)
   glutCreateWindow("Hello")
   glutTimerFunc(0,animate,0)
   glutDisplayFunc(drawScene)
   glutKeyboardFunc(keyboard)
   init()
   glutMainLoop()
main()