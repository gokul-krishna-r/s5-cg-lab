from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE=500
scal=2
dir=0
theta=0

consX=[[-50,50,0],
      [-50,-50,-200],
      [50,50,200],
      [-50,50,0]]
consY=[[50,50,200],
      [50,-50,0],
      [50,-50,0],
      [-50,-50,-200]]
PosX=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
PosY=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
radX=0
radY=0

def init():
   gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
   glClearColor(1,1,1,1)
def drawTriangle(x1,y1,x2,y2,x3,y3):
   glBegin(GL_POLYGON)
   glVertex2f(x1,y1)
   glVertex2f(x2,y2)
   glVertex2f(x3,y3)
   glEnd()

def drawStar():
   glClear(GL_COLOR_BUFFER_BIT)
   glPointSize(5)
   glColor3f(1,0,0)
   for i in range(0,4):
      drawTriangle(PosX[i][0]*scal+radX,PosY[i][0]*scal+radY,PosX[i][1]*scal+radX,PosY[i][1]*scal+radY,PosX[i][2]*scal+radX,PosY[i][2]*scal+radY)
   glFlush()
   glutSwapBuffers()

def animate(value):
   glutPostRedisplay()
   global scal
   global theta
   global dir,radX,radY
   glutTimerFunc(int(1000/60),animate,0)
   theta+=1
   for i in range(0,4):
      for j in range(0,3):
         PosX[i][j]=consX[i][j]*math.cos(math.radians(theta))-consY[i][j]*math.sin(math.radians(theta))
         PosY[i][j]=consY[i][j]*math.cos(math.radians(theta))+consX[i][j]*math.sin(math.radians(theta))
   radX=100*math.cos(math.radians(theta))
   radY=100*math.sin(math.radians(theta))
   if(theta>360):
      theta=0
   if(dir==0):
      scal-=0.006
      if(scal<0):
         dir=1
   if(dir==1):
      scal+=0.01
      if(scal>1):
         dir=0
   

   

def main():
   global POSX,POSY
   glutInit(sys.argv)
   glutInitWindowPosition(0,0)
   glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
   glutInitDisplayMode(GLUT_RGB)
   glutCreateWindow("Hello")
   glutTimerFunc(0,animate,0)
   glutDisplayFunc(lambda:drawStar())
   init()
   glutMainLoop()
main()
