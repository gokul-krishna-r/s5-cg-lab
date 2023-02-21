from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import numpy as py
sys.setrecursionlimit(10**6) 

WINDOW_SIZE=500
 
xt,yt=0,0
theta=0
dir=0
apex=200

def init():
   gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
   glClearColor(1,1,1,1)


def drawTriangle():
   global apex
   glBegin(GL_POLYGON)
   glVertex2f(-25+xt,50+yt)
   glVertex2f(75+xt,50+yt)
   glVertex2f(xt,apex+yt)
   glEnd()

def drawScene():
   global xt,yt
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(1,0,0)
   drawTriangle()
   glBegin(GL_POLYGON)
   glVertex2f(-200+xt,50+yt)
   glVertex2f(-200+xt,-50+yt)
   glVertex2f(-100+xt,-10+yt)
   glVertex2f(-50+xt,-50+yt)
   glVertex2f(150+xt,-50+yt)
   glVertex2f(200+xt,0+yt)
   glVertex2f(150+xt,50+yt)
   glEnd()
   glFlush()
   glutSwapBuffers()

def animate(temp):
   glutPostRedisplay()
   glutTimerFunc(int(1000/60),animate,int(0))
   

   

def keyboard(key,x,y):
   key=key.decode()
   global xt,yt,apex
   
   if(key=="a"):
      xt-=3
   elif(key=="d"):
      xt+=3
   elif(key=="w"):
      yt+=3
   elif(key=="s"):
      yt-=3
   
   if(apex==200):
      apex=-200
   elif(apex==-200):
      apex=200
 

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