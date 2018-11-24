#adapted from http://blog.meltinglogic.com/2013/12/how-to-generate-procedural-racetracks/

from random import *
from math import *
import sys
from scipy.spatial import *
import numpy as np
from turtle import *
import turtle
from tkinter import *
from PIL import Image
from glob import glob

# below is the code to generate the track -- don't touch if at all possible
def dist(pta,ptb = [0,0]):
    return sqrt((pta[0]-ptb[0])**2 + (pta[1]-ptb[1])**2)

screenx = 500
screeny = 500

def run():
    numOfPts = 30
    points = np.random.rand(numOfPts, 2)   # 30 random points in 2-D
    for i in range(numOfPts):
        points[i][0] = (points[i][0]-0.5)*screenx
        points[i][1] = (points[i][1]-0.5)*screeny
    hull = ConvexHull(points)

    pts = []
    for i in range(len(points[hull.vertices,0])):
        pts.append([points[hull.vertices,0][i],points[hull.vertices,1][i]])

    def pushApart(ps):
        dst = 20
        lth = len(ps)
        for i in range(0,lth):
            for j in range(i+1,lth):
                if dist(ps[i],ps[j]) < dst:
                    hx = ps[j][0] - ps[i][0]
                    hy = ps[j][1] - ps[i][1]
                    hl = dist([hx,hy])
                    hx /= hl
                    hy /= hl
                    dif = dst - hl
                    hx *= dif
                    hy *= dif
                    ps[j][0] -= hx
                    ps[j][1] -= hy
                    ps[i][0] += hx
                    ps[i][1] += hy
        return ps

    for asdf in range(5):
        pts = pushApart(pts)

    rset = []
    disp = [0,0]
    difficulty = 200
    maxDisp = 1
    for i in range(len(pts)):
        dispLen = (uniform(0,1)**difficulty) * maxDisp
        theta = uniform(0,2*pi)
        disp = [dispLen*cos(theta),dispLen*sin(theta)]
        rset.append(pts[i])
        mid = [(pts[i][0]+pts[(i+1)%len(pts)][0])/2, (pts[i][1]+pts[(i+1)%len(pts)][1])/2]
        rset.append([mid[0]+pts[i][0], mid[1]+pts[i][1]])
    pts = rset

    def fixAngles(ps):

        angl = 60

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
            nx = -nx
            ny = -ny
            nl = dist([nx,ny])
            nx /= nl
            ny /= nl
            a = atan2(px*ny-py*nx,px*nx+py*ny)
            if abs(a) > angl * pi / 180:
                nA = angl * a / abs(a) * pi / 180
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


    iter = 5
    for asdf in range(iter):
        pts = fixAngles(pts)
        pts = pushApart(pts)

    def selfIntersects(ps):
        for i in range(len(ps)-2):
            pta = ps[i]
            ptb = ps[i+1]
            pta = [(pta[0]+ptb[0])/2, (pta[1]+ptb[1])/2]
            ptm = [(pta[0]+ptb[0])/2, (pta[1]+ptb[1])/2]
            for j in range(i+2, len(ps)-1):
                ptc = ps[j]
                ptd = ps[j+1]
                ptn = [(ptc[0]+ptd[0])/2, (ptc[1]+ptd[1])/2]
                ad = dist(pta,ptd)
                bc = dist(ptb,ptc)
                mn = dist(ptm,ptn)
                if mn < ad and mn < bc:
                    return True
        return False

    #all the code above does the hard work -- don't touch it if at all possible.

    if selfIntersects(pts):
        pts = run()
    else:
        colormode(255)
        screensize(0, 0)
        # original size of canvas is 500 x 500 -- want it to be 250 x 250
        mapwidth = max([pt[0] for pt in pts]) - min([pt[0] for pt in pts])
        mapheight = max([pt[1] for pt in pts]) - min([pt[1] for pt in pts])
        squarelength = max(mapheight,mapwidth)

        dx = (max([pt[0] for pt in pts]) + min([pt[0] for pt in pts]))/2
        dy = (max([pt[1] for pt in pts]) + min([pt[1] for pt in pts]))/2
        for i in range(len(pts)):
            pts[i][0] -= dx
            pts[i][1] -= dy

        penwidth = 80
    
        for i in range(len(pts)):
            pts[i][0] = pts[i][0] / squarelength * (800 - penwidth*3)
            pts[i][1] = pts[i][1] / squarelength * (800 - penwidth*3)
        
        hideturtle()
        up()
        turtle.speed(0)
        goto(pts[0])
        width(penwidth)
        pen(pencolor=(104,104,104))
        down()
        for item in pts:
            goto(item)
        goto(pts[0])
        up()
        width(2)
        pen(pencolor=(200,200,200))
        down()
        for item in pts:
            goto(item)
        goto(pts[0])
        up()
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file = "track.eps")

        img = Image.open("track.eps").convert('RGBA')
        img = img.resize((1024,1024), Image.ANTIALIAS)
        pixeldata = list(img.getdata())

        for i,pixel in enumerate(pixeldata):
            if pixel[:3] == (255,255,255):
                pixeldata[i] = (86,176,0)

        img.putdata(pixeldata)
        img.save("track.png","png")

        return pts

if __name__ == "__main__":
    run()