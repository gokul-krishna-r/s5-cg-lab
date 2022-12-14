from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

def init():
	glClearColor(1.0, 1.0, 1.0, 1.0)
	gluOrtho2D(-100, 100.0, -100, 100.0)

def plotaxes():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0, 0.0, 0.0)
	glBegin(GL_LINES)
	glVertex2f(0, -500)
	glVertex2f(0, 500)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(500, 0)
	glVertex2f(-500, 0)
	glEnd()

def plotgrid():
	glColor3f(0.25,0.25,0.25)
	for i in range(-500, 500, 50):
		if i != 0:
			glBegin(GL_LINES)
			glVertex2f(i, 500)
			glVertex2f(i, -500)
			glEnd()
			glBegin(GL_LINES)
			glVertex2f(500, i)
			glVertex2f(-500, i)
			glEnd()

def plotTriangle(x1, x2, x3, y1, y2, y3):
	 
	glBegin(GL_LINES)
	glVertex2f(x1, y1)
	glVertex2f(x2, y2)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(x2, y2)
	glVertex2f(x3, y3)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(x3, y3)
	glVertex2f(x1, y1)
	glEnd()

def drawTranslated(x1, x2, x3, y1, y2, y3, tx, ty):
	points = [[x1, y1], [x2, y2], [x3, y3]]
	newpoints = []
	for point in points:
		newpoints.append([point[0]+tx, point[1]+ty])
	print(newpoints)
	plotaxes()
	plotgrid()
	glColor3f(0, 0, 1)
	plotTriangle(x1, x2, x3, y1, y2, y3)
	glColor3f(1, 0, 1)
	plotTriangle(newpoints[0][0], newpoints[1][0], newpoints[2][0], newpoints[0][1], newpoints[1][1], newpoints[2][1])
	glFlush()

def drawRotatedAboutPoint(x1, x2, x3, y1, y2, y3, theta, px, py):
	points = [[x1, y1], [x2, y2], [x3, y3]]
	newpoints = []
	for point in points:
		newpoints.append([round((point[0]-px) * math.cos(theta) - (point[1]-py) * math.sin(theta))+px,round((point[0]-px) * math.sin(theta) +(point[1]-py) * math.cos(theta))+py])
	plotaxes()
	plotgrid()
	glColor3f(0, 0, 1)
	plotTriangle(x1, x2, x3, y1, y2, y3)
	glColor3f(1, 0, 1)
	plotTriangle(newpoints[0][0], newpoints[1][0], newpoints[2][0], newpoints[0][1], newpoints[1][1], newpoints[2][1])
	glFlush()

def drawScaledAboutPoint(x1, x2, x3, y1, y2, y3, tx, ty, px, py):
	points = [[x1, y1], [x2, y2], [x3, y3]]
	newpoints = []
	for point in points:
		newpoints.append([(point[0] - px)*tx, (point[1] - py)*ty])
	plotaxes()
	plotgrid()
	glColor3f(0, 0, 1)
	plotTriangle(x1, x2, x3, y1, y2, y3)
	glColor3f(1, 0, 1)
	plotTriangle(newpoints[0][0] + px, newpoints[1][0] + px, newpoints[2][0] + px, newpoints[0][1] + py, newpoints[1][1] + py, newpoints[2][1] + py)
	glFlush()


def rotateAboutPoint(x1, x2, x3, y1, y2, y3):
	theta = (math.pi/180) * int(input("\nEnter Degress to be rotated: "))
	px = int(input("X Coordinate of point: "))
	py = int(input("Y Coordinate of point: "))
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	glutCreateWindow("2D Transformations - rotate about point")
	glutDisplayFunc(lambda: drawRotatedAboutPoint(x1, x2, x3, y1, y2, y3, theta, px, py))
	init()
	glutMainLoop()


def scaleAboutPoint(x1, x2, x3, y1, y2, y3):
	tx = int(input("\nEnter Scale along x: "))
	ty = int(input("\nEnter Scale along y: "))
	px = int(input("X Coordinate of point: "))
	py = int(input("Y Coordinate of point: "))
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	glutCreateWindow("2D Transformations - scaling about point")
	glutDisplayFunc(lambda: drawScaledAboutPoint(x1, x2, x3, y1, y2, y3, tx, ty, px, py))
	init()
	glutMainLoop()

def translate(x1, x2, x3, y1, y2, y3, tx, ty):
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	glutCreateWindow("2D Transformations - translation")
	glutDisplayFunc(lambda: drawTranslated(x1, x2, x3, y1, y2, y3, tx, ty))
	init()
	glutMainLoop()

def main():
	print("\nEnter Triangle co-ordinates:")
	x1 = float(input("\n\tx1: "))
	y1 = float(input("\n\ty1: "))
	side = float(input("\n\tside: "))
	x2 = x1 + side
	y2 = y1
	x3 = x1+side/2
	y3 = y1+0.86602540378*side
	print("\nChoose Transformations:\n\t1.Translation\n\t2.Rotation around a point\n\t3.Scaling about a point")
	ch = int(input("\nYour Choice: "))
	if ch == 1:
		translationX = int(input("\nX translation: "))
		translationY = int(input("\nY translation: "))
		translate(x1, x2, x3, y1, y2, y3, translationX, translationY)
	elif ch == 2:
		rotateAboutPoint(x1, x2, x3, y1, y2, y3)
	elif ch == 3:
		scaleAboutPoint(x1, x2, x3, y1, y2, y3)


main()
