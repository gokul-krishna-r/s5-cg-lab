from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE=500
POINT_SIZE=7
GLOBAL_X=0
GLOBAL_Y=-100
DROPLET_X=[20,-10]
DROPLET_Y=[600,600]
def init():
   glClearColor(1.0,1.0,1.0,1.0)
   gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
def drawBucket():
   glLineWidth(POINT_SIZE)
   glBegin(GL_QUADS)
   glVertex2f(55,105)
   glVertex2f(-55,105)
   glVertex2f(-55,-105)
   glVertex2f(55,-105)
   glEnd()
def drawWater(y):
   glColor3f(0,0,1)
   glBegin(GL_POLYGON)
   glVertex2f(50,y)
   glVertex2f(-50,y)
   glVertex2f(-50,-100)
   glVertex2f(50,-100)
   glEnd()
def drawPipeWater(x,y):
   glColor3f(0,0,1)
   glBegin(GL_POLYGON)
   glVertex2f(x,y)
   glVertex2f(x+10,y)
   glVertex2f(x+10,y-30)
   glVertex2f(x,y-30)
   glEnd()
def drawScene():
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(1.0,0,0)
   drawBucket()
   drawWater(GLOBAL_Y)
   for i in range(0,2):
      drawPipeWater(DROPLET_X[i],DROPLET_Y[i])
   glFlush()
   glutSwapBuffers()

def keyboardChk(key,x,y):
   key=key.decode()
   global GLOBAL_Y
   if(key=='s'):
      animate(2)
   if(key=='e'):
      GLOBAL_Y=-100
   
def animate(pos):
   global GLOBAL_Y
   global DROPLET_Y
   glutPostRedisplay()
   if GLOBAL_Y==100:
      DROPLET_Y=[600,600]
      return
   glutTimerFunc(int(1000/60),animate,pos)
   GLOBAL_Y=GLOBAL_Y+1
   if(GLOBAL_Y>100):
      GLOBAL_Y=-100
   for i in range(0,pos):
      DROPLET_Y[i]=DROPLET_Y[i]-((i+1)*5)
      if(DROPLET_Y[i]<=GLOBAL_Y):
         DROPLET_Y[i]=DROPLET_Y[i]+400
  
   
   

def main():
   glutInit(sys.argv)
   glutInitWindowPosition(0,0)
   glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
   glutInitDisplayMode(GLUT_RGB)
   glutCreateWindow("Pendulum")
   glutDisplayFunc(drawScene)
   glutKeyboardFunc(keyboardChk)
   glutIdleFunc(drawScene)
   init()
   glutMainLoop()
main()