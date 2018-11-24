from random import *
from math import *
import sys
from scipy.spatial import *
import matplotlib.pyplot as plt
import numpy as np

def dist(pta,ptb = [0,0]):
    return sqrt((pta[0]-ptb[0])**2 + (pta[1]-ptb[1])**2)

screenx = 500
screeny = 500

numOfPts = 30
points = np.random.rand(numOfPts, 2)   # 30 random points in 2-D
for i in range(numOfPts):
    points[i][0] = (points[i][0]-0.5)*screenx
    points[i][1] = (points[i][1]-0.5)*screenx
hull = ConvexHull(points)

pts = []
for i in range(len(points[hull.vertices,0])):
    pts.append([points[hull.vertices,0][i],points[hull.vertices,1][i]])
print(pts)

def pushApart(ps):
    dst = 0.1
    dst2 = dst**2
    lth = len(ps)
    for i in range(0,lth):
        for j in range(i+1,lth):
            if dist(ps[i],ps[j]) < dst2:
                hx = ps[j][0] - ps[i][0]
                hy = ps[j][1] - ps[i][1]
                hl = sqrt(hx**2+hy**2)
                hx /= hl
                hy /= hl
                dif = dst - hl
                hx *= dif
                hy *= dif
                ps[j][0] += hx
                ps[j][1] += hy
                ps[i][0] -= hx
                ps[i][1] -= hy
    return ps

iter = 3
for asdf in range(iter):
    pts = pushApart(pts)

rset = []
disp = [0,0]
difficulty = 1
maxDisp = 0.05
for i in range(len(pts)):
    dispLen = (uniform(0,1)**difficulty) * maxDisp
    theta = uniform(0,2*pi)
    disp = [dispLen*cos(theta),dispLen*sin(theta)]
    rset.append(pts[i])
    mid = [(pts[i][0]+pts[(i+1)%len(pts)][0])/2, (pts[i][1]+pts[(i+1)%len(pts)][1])/2]
    rset.append([mid[0]+pts[i][0], mid[1]+pts[i][1]])
pts = rset

def fixAngles(ps):
    for i in range(len(ps)):
        prev = (i-1)%len(ps)
        next = (i+1)%len(ps)
        px = ps[i][0] - ps[prev][0]
        py = ps[i][1] - ps[prev][1]
        pl = dist([px,py])
        px /= pl
        py /= pl
        nx = ps[i][0] - ps[next][0]
        ny = ps[i][1] - ps[next][1]
        nl = dist([nx,ny])
        nx /= nl
        ny /= nl
        a = atan2(px*ny-py*nx,px*nx+py*ny)
        if abs(a) > 5/9*pi:
            nA = 100 * a / abs(a) * pi / 180
            diff = nA - a
            c = cos(diff)
            s = sin(diff)
            newX = nx * c - ny * s
            newY = nx * s + ny * c
            newX *= nl
            newY *= nl
            ps[next][0] = ps[i][0] + newX
            ps[next][1] = ps[i][1] + newY
    return ps


iter = 3
for asdf in range(iter):
    pts = pushApart(pts)

plt.plot(points[:,0], points[:,1], 'o')
plt.plot([item[0] for item in pts+pts[:1]], [item[1] for item in pts+pts[:1]], 'k-o')
plt.show()

