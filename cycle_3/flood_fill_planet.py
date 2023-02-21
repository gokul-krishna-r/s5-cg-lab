from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import numpy as py
sys.setrecursionlimit(10**6) 

WINDOW_SIZE=500
rx=int(input("Enter x coordinate of first point: "))
ry=int(input("Enter y coordinate of first point: "))

ROTATEX,ROTATEY=0,0
theta=0


def init():
   gluOrtho2D(0,WINDOW_SIZE,0,WINDOW_SIZE)
   glClearColor(1,1,1,1)

def drawEllipse():
   global rx,ry
   angle=0.0
   glBegin(GL_POINTS)
   while(angle<=360):
      glVertex2f(rx*math.cos(math.radians(angle))+300,ry*math.sin(math.radians(angle))+300)
      angle+=1
   glEnd()

def drawCircle(x,y,r):
   angle=0.0
   glBegin(GL_LINES)
   while(angle<=360):
      glVertex2f(x,y)
      glVertex2f(r*math.cos(math.radians(angle))+x,r*math.sin(math.radians(angle))+y)
      angle+=1
   glEnd()
def drawScene():
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(1,0,0)
   drawEllipse()
   drawCircle(300,300,50)
   drawCircle(ROTATEX+300,ROTATEY+300,30)
   glFlush()
   glutSwapBuffers()

def animate(temp):
   glutPostRedisplay()
   glutTimerFunc(int(1000/60),animate,int(0))
   global theta,ROTATEX,ROTATEY
   ROTATEX=rx*math.cos(math.radians(theta))
   ROTATEY=ry*math.sin(math.radians(theta))
   theta+=1
   if(theta>360):
      theta=0

def floodFill(x,y,oldColor,newColor):
   color=glReadPixels(x,y,1.0,1.0,GL_RGB,GL_FLOAT,None)
   print(color[0][0],x,y)
   if(all(color[0][0]==oldColor) ):
      glColor3f(*newColor)
      glPointSize(2)
      glBegin(GL_POINTS)
      glVertex2i(x,y)
      glEnd()
      glFlush()
    
      floodFill(x+2,y,oldColor,newColor)
      floodFill(x-2,y,oldColor,newColor)
      floodFill(x,y+2,oldColor,newColor)
      floodFill(x,y-2,oldColor,newColor)
   
   
   


def mouse(btn,state,x,y):
   y=WINDOW_SIZE-y
   if(btn==GLUT_LEFT_BUTTON):
      if(state==GLUT_DOWN):
         floodFill(x,y,(1,0,0),(0,1,0))

def main():
   glutInit(sys.argv)
   glutInitWindowPosition(0,0)
   glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
   glutInitDisplayMode(GLUT_RGB)
   glutCreateWindow("Hello")
   glutTimerFunc(0,animate,0)
   glutDisplayFunc(drawScene)
   glutMouseFunc(mouse)
   init()
   glutMainLoop()
main()
