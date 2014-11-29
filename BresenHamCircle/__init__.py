#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
	Draw a circle in BresenHam algorithm.
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawCircle(x0, y0, r):
	x, y, p = 0, r, 1-r

	L = []
	L.append((x, y))

	for x in range(int(r)):
		if p < 0:
			p = p + 2 * x + 3
		else:
			y -= 1
			p = p + 2 * x + 3 - 2 * y

		L.append((x, y))

		if x >= y: break

	N = L[:]
	for i in L:
		N.append((i[1], i[0]))

	L = N[:]
	for i in N:
		L.append((-i[0], i[1]))
		L.append((i[0], -i[1]))
		L.append((-i[0], -i[1]))

	N = []
	for i in L:
		N.append((x0+i[0], y0+i[1]))

	return N

def projection():
	glMatrixMode(GL_PROJECTION)
	gluOrtho2D(0, 400, 0, 300)

def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1, 0, 0)

	glBegin(GL_POINTS)

	for i in drawCircle(150, 150, 100):
		glVertex2iv(i)

	glEnd()
	glFlush()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(400, 300)
	glutInitWindowPosition(100, 120)
	glutCreateWindow("Simple Point")
	projection()
	glutDisplayFunc(draw)
	glutMainLoop()

if __name__ == "__main__":
	main()
