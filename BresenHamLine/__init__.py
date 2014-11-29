#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2014-10-24 22:11:00
# @Author  : Usual (cuihao5135@gmail.com)
# @Link    : blog.chrics.cn

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

endPts = (
	(400, 300),
	(0, 0),
)

def bresenhamPts(endPts):
	if endPts[0][0] > endPts[1][0]:
		endPts = endPts[::-1]

	start, stop = endPts
	dx, dy = stop[0] - start[0], abs(stop[1] - start[1])
	twoDy, twoDyMinuxDx = 2 * dy, 2 * (dy - dx)
	ychange = (stop[1] - start[1]) / dy

	p = 2 * dy - dx
	s = set([start])
	x, y = start

	for x in range(x + 1, stop[0]):
		if (p < 0):
			p += twoDy
		else:
			y += ychange
			p += twoDyMinuxDx

		s.add((x, y))

	return s

def draw():

	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1, 0, 0)

	points = bresenhamPts(endPts)
	glBegin(GL_POINTS)

	for i in points:
		glVertex2iv(i)

	glEnd()
	glFlush()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(400, 300)
	glutInitWindowPosition(100, 120)
	glutCreateWindow("Simple Point")
	
	glMatrixMode(GL_PROJECTION)
	gluOrtho2D(0, 400, 0, 300)

	glutDisplayFunc(draw)
	glutMainLoop()

if __name__ == "__main__":
	main()
