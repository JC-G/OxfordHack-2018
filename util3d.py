from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
import numpy
import pygame
import random
import math
textureArray = {}
scsz = (800,600)
class Sprite3d:
    def __init__(self,fileName,x,y,z,r):
        self.imageData = makeTexture(fileName)

        self.pos = (x,y,z)
        self.radius = r
        self.relativeHeight = r*self.imageData[2]/self.imageData[1]
    def setPos(self,x,y,z):
        self.pos = (x,y,z)
    def move(self,dx,dy,dz):
        self.pos = (self.x+dx,self.y+dy,self.z+dz)

def enablePerspective():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, scsz[0]/scsz[1], 0.001, 1000.0)
    glMatrixMode(GL_MODELVIEW)

def enableFlat():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)

def makeTexture(fileName):
    if fileName in textureArray:
        print("IN")
        return textureArray[fileName]
    image = Image.open(fileName)
    imageData = numpy.array(list(image.getdata()), numpy.uint8)

    textureID = glGenTextures(1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glBindTexture(GL_TEXTURE_2D, textureID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
    print(image.size)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.size[0], image.size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, imageData)
    szx = image.size[0]
    szy = image.size[1]
    print(szx,szy)
    image.close()
    textureArray[fileName] = (textureID,szx,szy)
    return textureArray[fileName]

def renderSprite(spr):
    glBindTexture(GL_TEXTURE_2D,spr.imageData[0])
    glBegin(GL_QUADS)
    glTexCoord(0,0)
    glVertex3f(spr.pos[0]-spr.radius,spr.pos[1],spr.pos[2])
    glTexCoord(0,1)
    glVertex3f(spr.pos[0]-spr.radius,spr.pos[1]+spr.relativeHeight,spr.pos[2])
    glTexCoord(1,1)
    glVertex3f(spr.pos[0]+spr.radius,spr.pos[1]+spr.relativeHeight,spr.pos[2])
    glTexCoord(1,0)
    glVertex3f(spr.pos[0]+spr.radius,spr.pos[1],spr.pos[2])

    glTexCoord(0,0)
    glVertex3f(spr.pos[0],spr.pos[1],spr.pos[2]-spr.radius)
    glTexCoord(0,1)
    glVertex3f(spr.pos[0],spr.pos[1]+spr.relativeHeight,spr.pos[2]-spr.radius)
    glTexCoord(1,1)
    glVertex3f(spr.pos[0],spr.pos[1]+spr.relativeHeight,spr.pos[2]+spr.radius)
    glTexCoord(1,0)
    glVertex3f(spr.pos[0],spr.pos[1],spr.pos[2]+spr.radius)


    glEnd()

def initGLPG(screen_size):
    global scsz
    scsz = screen_size
    pygame.init()
    screen = pygame.display.set_mode(screen_size, pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF)

    glViewport(0, 0, screen_size[0], screen_size[1])

    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    viewport = glGetIntegerv(GL_VIEWPORT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glEnable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_ALPHA_TEST)
    glAlphaFunc(GL_GREATER,0.001)
    return screen
def drawTerrain(terr):
    glBindTexture(GL_TEXTURE_2D,terr.img)
    glBegin(GL_QUADS)
    glTexCoord(0,0)
    glVertex3f(-1,0,-1)

    glTexCoord(0,1)
    glVertex3f(-1,0,1)

    glTexCoord(1,1)
    glVertex3f(1,0,1)

    glTexCoord(1,0)
    glVertex3f(1,0,-1)
    glEnd()




if __name__ == "__main__":
    screen = initGLPG((640,480))
    theta = 0
    ml = True
    s = Sprite3d("tree.png",0,0,0,1)
    clock = pygame.time.Clock()


    trees = []
    for x in range(10):
        trees.append(Sprite3d("tree.png",0.1*random.randint(0,100)-5,0,0.1*random.randint(0,100)-5,1))

    while ml:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ml = False

        glClearColor(0.5, 0.5, 0.5, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity( )
        enablePerspective()
        #enableFlat()
        gluLookAt(10*math.cos(theta), 10, 10*math.sin(theta), 0, 0, 0, 0, 1, 0)
        theta+=0.01
        for t in trees:
            renderSprite(t)
        pygame.display.flip()


    pygame.quit()