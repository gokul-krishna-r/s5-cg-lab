from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time

ROTATE_X=[0,0,0,0,0]
ROTATE_Y=[0,0,0,0,0]
WINDOW_SIZE=500
POINT_SIZE=10
SPEED=[0,2,3,5,4]
THETA=[0,40,180,70,190]
BOB_RADIUS=[60,10,5,25,40]
DIS=[0,100,200,300,400]
def init():

   glClearColor(1.0,1.0,1.0,1.0)
   gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
def drawCircle(x,y,BOB_RADIUS):
   glColor3f(0,0,0)
   glBegin(GL_TRIANGLE_FAN)
   glVertex2f(x,y)
   for i in range(0,360,1):
        glVertex2f(BOB_RADIUS*math.cos(math.pi*i/180)+x,BOB_RADIUS*math.sin(math.pi*i/180)+y)
   glEnd()
def drawCircleOrbit(dis):
    glColor3f(0,1,0)
    glBegin(GL_POINTS)
    theta = 0.0
    while theta <= 6.28:
        x = float(dis) * math.cos(theta)
        y = float(dis) * math.sin(theta)
        glVertex2f(x , y)
        theta += 0.005
    glEnd()
def drawSolarSystem(noOfCircles):
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(1.0,0,0)
   for i in range(0,noOfCircles):
      drawCircleOrbit(DIS[i])
      drawCircle(ROTATE_X[i],ROTATE_Y[i],BOB_RADIUS[i])
   glFlush()
   glutSwapBuffers()


def animatePlanetOne(noofPlanets):
   global ROTATE_X
   global ROTATE_Y
   global SPEED
   global DIS
   glutPostRedisplay()
   glutTimerFunc(int(1000/60),animatePlanetOne,noofPlanets)
   for i in range(0,noofPlanets):
      ROTATE_X[i]=DIS[i]*math.cos(math.radians(THETA[i]))
      ROTATE_Y[i]=-DIS[i]*math.sin(math.radians(THETA[i]))
      if( THETA[i]==360):
         THETA[i]=0
      THETA[i]=THETA[i]+SPEED[i]
   




def main():
   glutInit(sys.argv)
   glutInitWindowPosition(0,0)
   glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
   glutInitDisplayMode(GLUT_RGB)
   glutCreateWindow("Pendulum")
   glutDisplayFunc(lambda:drawSolarSystem(5))
   glutTimerFunc(0,animatePlanetOne,5)
   glutIdleFunc(lambda:drawSolarSystem(5))
   init()
   glutMainLoop()
main()